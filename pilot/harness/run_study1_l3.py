"""Replay Study 1 prompts and measure matched changes with the frozen Llama probes."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, ZipFile

import numpy as np

from run_l3_probe_smoke import file_hash, save_array
from run_l3_smoke import ROOT, llama_prompt
from run_study1 import CONTENTS, QUESTION, SAFETY_SYSTEM, SCHEMA, load_items, trial_inputs


def replay_inputs(plan_file, log_file, panel_source="unanimous"):
    conditions = (("neutral", "neutral", "public"),) + tuple(
        (panel_source, content, "public") for content in CONTENTS
    )
    plan, plan_digest, items = load_items(plan_file)
    with log_file.open(encoding="utf-8") as stream:
        rows = [json.loads(line) for line in stream]
    if not rows or {row["plan_sha256"] for row in rows} != {plan_digest}:
        raise ValueError("The Study 1 log does not match the frozen plan.")
    by_id = {row["trial_id"]: row for row in rows}
    by_key = {(row["item_id"], row["arm"], row["phase"], row["round"]): row for row in rows}
    if len(by_id) != len(rows) or len(by_key) != len(rows):
        raise ValueError("Duplicate trial ID or item/condition/round in the Study 1 log.")
    cases = []
    for item in items:
        for trial, text, history in trial_inputs(item, conditions, plan["rounds"]):
            arm, phase, number = (trial[key] for key in ("arm", "phase", "round"))
            if phase != "baseline" and (phase != "debate" or number != 3):
                continue
            saved = by_key[item["item_id"], arm, phase, number]
            if saved["status"] != "ok" or saved["served_model_id"] != "llama3.1:8b":
                raise ValueError(f"Expected a scorable Llama reply on {saved['trial_id']}.")
            if history is not None:
                parent = by_id[saved["parent_trial_id"]]
                if (parent["item_id"], parent["arm"], parent["phase"], parent["round"]) != (
                    item["item_id"], arm, "debate", number - 1,
                ):
                    raise ValueError(f"Incorrect context parent on {saved['trial_id']}.")
                text += "\n\nYour preceding decision labels: " + json.dumps([parent["decision"]])
            user = f"{text}\n\n{QUESTION}"
            if hashlib.sha256(user.encode()).hexdigest() != saved["prompt_sha256"]:
                raise ValueError(f"Prompt checksum mismatch on {saved['trial_id']}.")
            messages = [{"role": "system", "content": SAFETY_SYSTEM}, {"role": "user", "content": user}]
            record = {key: saved[key] for key in (
                "item_id", "pair_id", "item_label", "category", "trial_id", "arm", "round",
                "prompt_sha256", "gold_decision",
            )}
            record["ollama_decision"] = saved["decision"]
            record["ollama_prompt_tokens"] = saved["usage"]["prompt_tokens"]
            cases.append((record, llama_prompt(messages)))
    if len(cases) != len(items) * (1 + len(conditions)):
        raise ValueError("Incomplete baseline and Round 3 replay set.")
    return cases, plan_digest


def capture(binary, model, cases, layers):
    captured = []
    with TemporaryDirectory(prefix="llama-study1-l3-") as folder:
        root = Path(folder)
        inputs = []
        schema = json.dumps(SCHEMA)
        for index, (_, prompt) in enumerate(cases):
            path = root / f"case-{index:04d}"
            path.mkdir()
            (path / "prompt.txt").write_text(prompt, encoding="utf-8")
            (path / "schema.json").write_text(schema, encoding="utf-8")
            inputs.append(path)
        stderr = root / "capture.stderr"
        with stderr.open("w", encoding="utf-8") as errors:
            completed = subprocess.run(
                [str(binary.resolve()), str(model.resolve()), *map(str, inputs)],
                stdout=subprocess.DEVNULL, stderr=errors,
            )
        if completed.returncode:
            raise RuntimeError("\n".join(stderr.read_text().splitlines()[-15:]))
        for (record, _), path in zip(cases, inputs, strict=True):
            response = json.loads((path / "replay.json").read_text())
            decision = response["response"].get("decision")
            if (response["layers"], response["width"]) != (32, 4096) or decision not in (
                "answer", "partial", "decline",
            ):
                raise ValueError("Unexpected activation shape or invalid replay decision.")
            state = np.fromfile(path / "activations.f32", dtype="<f4").reshape(32, 4096)[layers]
            if not np.isfinite(state).all():
                raise ValueError("Non-finite activation in the replay.")
            captured.append(state)
            record.update({
                "replay_decision": decision, "replay_prompt_tokens": response["prompt_tokens"],
                "last_prompt_token": response["last_prompt_token"],
            })
    return np.stack(captured)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=ROOT / "pilot/study1_checklist.json")
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--panel-source", choices=("unanimous", "minority"), default="unanimous")
    parser.add_argument("--probes", type=Path, default=ROOT / "results/log/llama_l3_calibrated_probes.npz")
    parser.add_argument("--binary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check-prompts", action="store_true", help="Verify prompt checksums only.")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Choose a new output name.")
    cases, plan_digest = replay_inputs(args.plan, args.log, args.panel_source)
    print(f"Verified {len(cases)} saved prompt checksums.", flush=True)
    if args.check_prompts:
        return
    with ZipFile(args.probes) as bundle:
        probe_meta = json.loads(bundle.read("metadata.json"))
    names = ("h", "r")
    steps = probe_meta["probes"]
    layers = sorted({steps[name]["layer_index"] for name in names})
    checkpoint = probe_meta["checkpoint_sha256"]
    model = Path.home() / ".ollama/models/blobs" / f"sha256-{checkpoint}"
    if file_hash(model) != checkpoint:
        raise ValueError("Local Llama GGUF does not match the frozen probes.")
    states = capture(args.binary, model, cases, layers)
    with np.load(args.probes, allow_pickle=False) as probes:
        for name in names:
            step = steps[name]
            scores = states[:, layers.index(step["layer_index"])] @ probes[f"{name}_direction"] - step["bias"]
            for (record, _), value in zip(cases, scores, strict=True):
                record[f"{name}_score"] = float(value)
    records = [record for record, _ in cases]
    baseline = {record["item_id"]: record for record in records if record["arm"] == "baseline"}
    for record in records:
        if record["arm"] != "baseline":
            for name in names:
                record[f"delta_{name}"] = record[f"{name}_score"] - baseline[record["item_id"]][f"{name}_score"]
    meta = {
        "checkpoint_sha256": checkpoint, "runtime": probe_meta["runtime"],
        "capture_position": probe_meta["capture_position"], "layer_indices": layers,
        "probe_bundle_sha256": file_hash(args.probes), "study_log_sha256": file_hash(args.log),
        "study_plan_sha256": plan_digest, "panel_source": args.panel_source, "records": records,
    }
    with ZipFile(args.output, "x", ZIP_DEFLATED) as bundle:
        save_array(bundle, "activations", states)
        bundle.writestr("metadata.json", json.dumps(meta, indent=2, allow_nan=False) + "\n")
    print(f"Measured {len(records) - len(baseline)} paired changes in {args.output}.")


if __name__ == "__main__":
    main()
