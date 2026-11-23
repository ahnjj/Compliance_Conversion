"""Fit Llama probes on training items, select layers on dev, and score held-out items."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import numpy as np

from run_l3_probe_smoke import file_hash, save_array


def matched_direction(states, labels, stratifier, context):
    negative, positive, support = [], [], []
    for setting in dict.fromkeys(context):
        for other in (0, 1):
            rows = (stratifier == other) & (context == setting)
            lower, upper = states[rows & (labels == 0)], states[rows & (labels == 1)]
            support.append({"context": setting, "other_label": other,
                            "negative": len(lower), "positive": len(upper)})
            if len(lower) and len(upper):
                negative.append(lower.mean(axis=0, dtype=np.float64))
                positive.append(upper.mean(axis=0, dtype=np.float64))
    if not negative:
        raise ValueError("The training split has no matched strata with both classes.")
    lower, upper = np.mean(negative, axis=0), np.mean(positive, axis=0)
    direction = upper - lower
    norm = np.linalg.norm(direction)
    if not np.isfinite(norm) or norm == 0:
        raise ValueError("Invalid projection direction.")
    direction /= norm
    return direction, float((lower + upper) @ direction / 2), support


def metrics(labels, scores):
    negative, positive = scores[labels == 0], scores[labels == 1]
    tn, fp = int(sum(negative < 0)), int(sum(negative >= 0))
    fn, tp = int(sum(positive < 0)), int(sum(positive >= 0))
    result = {
        "negative": len(negative), "positive": len(positive), "tn": tn, "fp": fp, "fn": fn, "tp": tp,
        "balanced_accuracy": None, "auroc": None,
    }
    if len(negative) and len(positive):
        comparison = positive[:, None] - negative[None, :]
        result.update({
            "balanced_accuracy": (tn / len(negative) + tp / len(positive)) / 2,
            "auroc": float(np.mean((comparison > 0) + 0.5 * (comparison == 0))),
        })
    return result


def fit_probe(activations, layer_indices, records, label, other_label):
    labels = np.array([row[label] for row in records], dtype=int)
    strata = np.array([row[other_label] for row in records], dtype=int)
    splits = np.array([row["split"] for row in records])
    context = np.array([row["context"] for row in records])
    train = splits == "train"
    dev_debate = (splits == "dev") & (context != "baseline")
    heldout = splits == "heldout"
    heldout_debate = heldout & (context != "baseline")
    candidates = []
    for column, layer in enumerate(layer_indices):
        state = activations[:, column]
        direction, bias, support = matched_direction(state[train], labels[train], strata[train], context[train])
        dev_score = state[dev_debate] @ direction - bias
        dev_metrics = metrics(labels[dev_debate], dev_score)
        if dev_metrics["balanced_accuracy"] is None:
            raise ValueError("The development debate split needs both classes.")
        candidates.append((layer, column, direction, bias, support, dev_metrics))
    layer, column, direction, bias, support, _ = max(
        candidates, key=lambda candidate: (
            candidate[-1]["balanced_accuracy"], candidate[-1]["auroc"], -candidate[0]
        ),
    )
    frozen_scores = activations[:, column] @ direction - bias
    subsets = {"all": heldout, "debate": heldout_debate}
    for setting in dict.fromkeys(context):
        subsets[str(setting)] = heldout & (context == setting)
    for setting in (0, 1):
        subsets[f"debate_other_{setting}"] = heldout_debate & (strata == setting)
    summary = {
        "layer_index": layer, "bias": bias,
        "train_support": support,
        "development": [{"layer_index": candidate[0], **candidate[-1]} for candidate in candidates],
        "heldout": {key: metrics(labels[mask], frozen_scores[mask]) for key, mask in subsets.items()},
    }
    return direction, frozen_scores, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calibration", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with ZipFile(args.calibration) as bundle:
        meta = json.loads(bundle.read("metadata.json"))
    with np.load(args.calibration, allow_pickle=False) as bundle:
        states = bundle["activations"]
    records = meta["records"]
    layers = meta["layer_indices"]
    if states.shape != (len(records), len(layers), 4096) or not np.isfinite(states).all():
        raise ValueError("Unexpected calibration shape or non-finite activations.")
    splits = {key: {row["pair_id"] for row in records if row["split"] == key}
              for key in ("train", "dev", "heldout")}
    if not all(splits.values()) or sum(map(len, splits.values())) != len(set.union(*splits.values())):
        raise ValueError("Calibration splits must have disjoint, nonempty pair IDs.")
    probes = {}
    arrays = {}
    for label, other_label in (("h", "r"), ("r", "h")):
        direction, scores, summary = fit_probe(states, layers, records, f"{label}_label", f"{other_label}_label")
        probes[label] = summary
        arrays[f"{label}_direction"] = direction
        arrays[f"{label}_scores"] = scores
    metadata = {
        "model_id": meta["model_id"], "checkpoint_sha256": meta["checkpoint_sha256"],
        "calibration_sha256": file_hash(args.calibration), "plan_sha256": meta["plan_sha256"],
        "capture_position": meta["capture_position"], "runtime": meta["runtime"],
        "h_label": "XSTest unsafe label", "r_label": "model returned decline",
        "probes": probes,
    }
    with ZipFile(args.output, "x", ZIP_DEFLATED) as bundle:
        for key, values in arrays.items():
            save_array(bundle, key, values)
        bundle.writestr("metadata.json", json.dumps(metadata, indent=2, allow_nan=False) + "\n")
    for label, probe in probes.items():
        print(label, "decoder block", probe["layer_index"] + 1, "held-out debate", probe["heldout"]["debate"])


if __name__ == "__main__":
    main()
