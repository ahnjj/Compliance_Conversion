"""Run baseline or one-round debate smoke tests against local Ollama Qwen3.5."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from run_smoke_test import ARMS, DECISIONS, ROOT, SYSTEM, parse_decision, render, run


MODEL = "qwen3.5:9b"


def ask(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "think": False,
        "format": {
            "type": "object",
            "properties": {
                "decision": {"type": "string", "enum": list(DECISIONS)},
                "reason": {"type": "string"},
            },
            "required": ["decision", "reason"],
            "additionalProperties": False,
        },
        "options": {"temperature": 0, "num_ctx": 2048, "num_predict": 128},
    }
    request = Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urlopen(request, timeout=180) as response:
        return json.load(response)["message"]["content"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=ROOT / "data/processed/development_pairs.csv")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--debate", action="store_true",
        help="Run the repeat ask and four debate arms, reusing the existing baseline log.",
    )
    args = parser.parse_args()

    with args.dataset.open(encoding="utf-8", newline="") as source:
        items = list(csv.DictReader(source))
    if not items:
        parser.error("The dataset has no items.")

    totals = Counter()
    correct = Counter()
    parse_errors = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as output:
        if args.debate:
            arms = tuple(arm for arm in ARMS if arm[0] != "baseline")
            try:
                counts = run(items, ask, output, MODEL, None, arms=arms)
            except (URLError, TimeoutError) as error:
                raise SystemExit(f"Ollama request failed: {error}") from error
            print(f"Log: {args.output.resolve()}")
            if sum(counts[arm, "ok"] for arm, _, _ in arms) != len(items) * len(arms):
                raise SystemExit("Some calls did not produce a scorable decision. See the log.")
            return
        for item in items:
            prompt = render(item, None, None, None)
            try:
                raw_response = ask(prompt)
            except (URLError, TimeoutError) as error:
                raise SystemExit(f"Ollama request failed for {item['item_id']}: {error}") from error
            decision = parse_decision(raw_response)
            gold = item["gold_decision"]
            status = "ok" if decision else "parse_error"
            record = {
                "item_id": item["item_id"],
                "pair_id": item["pair_id"],
                "arm": "baseline",
                "model_id": MODEL,
                "thinking": False,
                "output_mode": "json_schema",
                "gold_decision": gold,
                "decision": decision,
                "correct": decision == gold if decision else None,
                "status": status,
                "prompt": prompt,
                "response": raw_response,
            }
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            output.flush()
            totals[gold] += 1
            correct[gold] += decision == gold
            parse_errors += decision is None

    for gold in sorted(totals):
        print(f"{gold}: {correct[gold]}/{totals[gold]} correct")
    print(f"Parse errors: {parse_errors}\nLog: {args.output.resolve()}")
    if parse_errors == len(items):
        raise SystemExit("No decisions passed the parser.")


if __name__ == "__main__":
    main()
