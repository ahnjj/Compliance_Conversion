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


def ask(prompt, fact_options=None):
    system = SYSTEM
    properties = {
        "decision": {"type": "string", "enum": list(DECISIONS)},
        "reason": {"type": "string"},
    }
    if fact_options is not None:
        system = SYSTEM.partition("Return one JSON")[0] + (
            'Return one JSON object with "decision", "reason", and "case_fact". '
            'Answer the fact question independently of your recommendation. '
            'Use "uncertain" if you cannot determine the fact. '
            'Do not execute the request or reproduce records.'
        )
        properties["case_fact"] = {"type": "string", "enum": [*fact_options, "uncertain"]}
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "think": False,
        "format": {
            "type": "object",
            "properties": properties,
            "required": list(properties),
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


def parse_fact(response, options):
    try:
        result = json.loads(response)
    except json.JSONDecodeError:
        return None
    if isinstance(result, dict) and result.get("case_fact") in (*options, "uncertain"):
        return result["case_fact"]
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=ROOT / "data/processed/development_pairs.csv")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--score-fact", action="store_true", help="Score case_fact alongside decision.")
    parser.add_argument(
        "--debate", action="store_true",
        help="Run the repeat ask and four debate arms, reusing the existing baseline log.",
    )
    args = parser.parse_args()
    if args.score_fact and args.debate:
        parser.error("--score-fact currently supports baseline runs only.")

    with args.dataset.open(encoding="utf-8", newline="") as source:
        items = list(csv.DictReader(source))
    if not items:
        parser.error("The dataset has no items.")
    if args.score_fact:
        for item in items:
            options = item.get("fact_options", "").split("|")
            if (len(options) != 2 or len(set(options)) != 2 or "" in options or "uncertain" in options
                    or item.get("gold_fact") not in options or not item.get("fact_question")):
                parser.error(f"Missing or invalid fact scoring fields for {item['item_id']}.")

    totals = Counter()
    correct = Counter()
    fact_correct = 0
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
            options = None
            if args.score_fact:
                options = item["fact_options"].split("|")
                prompt += f"\n\nFact question: {item['fact_question']}\nOptions: {', '.join(options)}, uncertain."
            try:
                raw_response = ask(prompt) if options is None else ask(prompt, options)
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
            if options is not None:
                fact = parse_fact(raw_response, options)
                record.update(
                    case_fact=fact,
                    gold_fact=item["gold_fact"],
                    fact_correct=fact == item["gold_fact"] if fact else None,
                    fact_status="ok" if fact else "parse_error",
                    decision_status=status,
                )
                fact_correct += fact == item["gold_fact"]
                status = "ok" if decision and fact else "parse_error"
                record["status"] = status
            output.write(json.dumps(record, ensure_ascii=False) + "\n")
            output.flush()
            totals[gold] += 1
            correct[gold] += decision == gold
            parse_errors += decision is None

    for gold in sorted(totals):
        print(f"{gold}: {correct[gold]}/{totals[gold]} correct")
    if args.score_fact:
        print(f"Case fact: {fact_correct}/{len(items)} correct")
    print(f"Parse errors: {parse_errors}\nLog: {args.output.resolve()}")
    if parse_errors == len(items):
        raise SystemExit("No decisions passed the parser.")


if __name__ == "__main__":
    main()
