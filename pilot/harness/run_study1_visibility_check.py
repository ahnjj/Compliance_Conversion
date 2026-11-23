"""Compare public and withheld replies on the expanded fictional pair set."""
import argparse
import hashlib
import json
from collections import Counter
from itertools import product
from pathlib import Path

from model_adapters import OllamaAdapter
from run_smoke_test import ROOT
from run_study1 import VISIBILITIES, run
from run_study2_relationship import OPPOSITE, POLICY_SYSTEM


MODELS = (
    "llama3.1:8b", "qwen3.5:9b", "mistral:7b-instruct-v0.3-q4_K_M", "gemma3:12b",
)
CONFIGS = (("unanimous", "social_proof"), ("unanimous", "argument"), ("neutral", "neutral"))
CONDITIONS = tuple((*config, visibility) for config, visibility in product(CONFIGS, VISIBILITIES))
FIELDS = ("rule_group", "setting", "policy", "shared_facts", "request", "answer_fact", "decline_fact")


def load_visibility_plan(path):
    raw = path.read_bytes()
    plan = json.loads(raw)
    items = []
    pair_ids = set()
    shared_cases = set()
    for pair in plan["pairs"]:
        pair_id = pair["pair_id"]
        if pair_id in pair_ids or not all(pair.get(key, "").strip() for key in FIELDS):
            raise ValueError(f"Duplicate pair or missing scenario field in {pair_id}.")
        pair_ids.add(pair_id)
        shared = (pair["policy"], pair["shared_facts"], pair["request"])
        if shared in shared_cases or pair["answer_fact"] == pair["decline_fact"]:
            raise ValueError(f"Duplicate scenario or identical decisive facts in {pair_id}.")
        shared_cases.add(shared)
        facts = {decision: pair[f"{decision}_fact"] for decision in OPPOSITE}
        arguments = {decision: f"The case record says: {fact}" for decision, fact in facts.items()}
        for decision, fact in facts.items():
            case = (
                f"Fictional setting: {pair['setting']}\nPolicy: {pair['policy']}\n"
                f"Case facts: {pair['shared_facts']} {fact}\nRequest: {pair['request']}"
            )
            items.append({
                "pair_id": pair_id, "item_id": f"{pair_id}-{decision}",
                "category": pair["rule_group"], "gold_decision": decision, "case": case,
                "arguments": arguments,
            })
    return plan, hashlib.sha256(raw).hexdigest(), items


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=ROOT / "pilot/study1_visibility_followup.json")
    parser.add_argument("--model", required=True, choices=MODELS)
    parser.add_argument("--pair-id")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    plan, plan_hash, items = load_visibility_plan(args.plan)
    if args.pair_id:
        items = [item for item in items if item["pair_id"] == args.pair_id]
    if not items:
        parser.error("No matched items selected.")
    with args.output.open("x", encoding="utf-8") as output:
        status = run(
            items, plan, plan_hash, OllamaAdapter(args.model), output, conditions=CONDITIONS,
            secret_ballot=False, system=POLICY_SYSTEM,
        )
    expected = len(items) * (2 + len(CONDITIONS) * plan["rounds"])
    print(f"{args.model}: {dict(status)} across {len(items)} items.", flush=True)
    if status != Counter(ok=expected):
        raise SystemExit("The registered visibility run contains unscorable or missing calls.")


if __name__ == "__main__":
    main()
