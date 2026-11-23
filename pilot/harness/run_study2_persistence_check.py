"""Cross the relationship cue and the prior-decision reminder on saved Study 2 shifts."""
import argparse
import json
from collections import defaultdict
from itertools import product
from pathlib import Path
from uuid import uuid4

from model_adapters import OllamaAdapter
from run_study2_relationship import TARGETS, generate_trial


def load_shifts(paths):
    expected_parents = {}
    source_trials = {}
    for path in paths:
        for line in path.open(encoding="utf-8"):
            row = json.loads(line)
            if row["status"] != "ok":
                raise ValueError(f"Unscorable source trial in {path.name}.")
            if row["phase"] == "baseline":
                source_trials[row["trial_id"]] = row
            elif row["phase"] == "debate" and row["round"] == 3:
                expected_parents[row["trial_id"]] = row
            elif row["phase"] == "followup":
                source_trials[row["trial_id"]] = row
    baselines = {row["match_id"]: row for row in source_trials.values() if row["phase"] == "baseline"}
    followups = defaultdict(dict)
    for row in source_trials.values():
        if row["phase"] == "followup":
            followups[row["parent_trial_id"]][row["cue_retained"]] = row
    for parent, final in expected_parents.items():
        baseline = baselines[final["match_id"]]
        stance = final["assigned_stance"]
        if baseline["decision"] != stance and final["decision"] == stance:
            variants = followups[parent]
            if set(variants) != {True, False}:
                raise ValueError(f"Missing source follow-up for {parent}.")
            yield final, variants


def without_reminder(prompt, decision, cue_retained):
    reminder = f"\n\nYour recorded decision from the previous panel was ({decision})."
    base, match, remainder = prompt.partition(reminder)
    if not match:
        raise ValueError("Expected exactly one recorded-decision reminder.")
    if cue_retained:
        return base + "\n" + remainder
    return base + remainder


def run(shifts, output, target, adapter_factory=OllamaAdapter):
    adapter = adapter_factory(target)
    run_id = uuid4().hex
    for final, variants in shifts:
        if final["model_id"] != target:
            continue
        conditions = tuple(product((False, True), repeat=2))
        offset = (final["pair_number"] + TARGETS.index(target)) % len(conditions)
        for cue, reminder in conditions[offset:] + conditions[:offset]:
            source = variants[cue]
            prompt = source["prompt"]
            if not reminder:
                prompt = without_reminder(prompt, final["decision"], cue)
            generate_trial(adapter, output, {
                **{field: source[field] for field in (
                    "dataset_sha256", "study2_factor", "model_id", "item_id", "pair_id", "pair_number",
                    "gold_decision", "assigned_stance", "condition_id", "peer_model",
                )},
                "run_id": run_id, "study_id": "study2_persistence_check",
                "source_round3_trial_id": final["trial_id"], "source_followup_trial_id": source["trial_id"],
                "source_followup_decision": source["decision"],
                "trial_id": f"{run_id}:{source['trial_id']}:reminder-{int(reminder)}",
                "parent_trial_id": final["trial_id"], "phase": "followup", "round": None,
                "cue_retained": cue, "prior_decision_retained": reminder,
            }, prompt)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, choices=TARGETS)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("logs", nargs="+", type=Path)
    args = parser.parse_args()
    shifts = list(load_shifts(args.logs))
    if not any(final["model_id"] == args.model for final, _ in shifts):
        parser.error(f"No eligible shifted trials found for {args.model}.")
    with args.output.open("x", encoding="utf-8") as output:
        run(shifts, output, args.model)


if __name__ == "__main__":
    main()
