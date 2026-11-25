"""Summarize audited Study 3 continuations and independent baselines."""
import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

from run_study3 import PANEL_CONTENT, QUESTIONS, SEEDS, TEMPERATURE, check_log, load_plan, trials

PHASES = ("Public round three", "Delayed original", "Related item")
DIRECTIONS = {"decline": "Toward refusal on benign items", "answer": "Toward answering on harmful items"}


def aggregate(path, stage, model):
    scheduled = list(trials(stage, model))
    rows = check_log(path, scheduled, complete=True)
    items = defaultdict(dict)
    for row in rows.values():
        if row["phase"] == "pause":
            continue
        items[row["item_id"], row["scope"]][row["phase"], row["condition"], row["query_variant"], row["seed"]] = row
    ready = []
    for (_, scope), item_rows in items.items():
        baseline = item_rows["fresh", "fresh", 0, SEEDS[0]]
        direction = baseline["direction"]
        fresh = [r["decision"] for r in item_rows.values() if r["phase"] == "fresh"]
        assert len(fresh) == len(QUESTIONS) * len(SEEDS)
        followups = {c: item_rows["followup", c, 0, SEEDS[0]] for c in PANEL_CONTENT}
        phases = {"Delayed original" if scope == "original" else "Related item":
                  {c: int(row["decision"] == direction) for c, row in followups.items()}}
        if scope == "original":
            phases["Public round three"] = {
                c: int(row["study1_round3_decision"] == direction) for c, row in followups.items()
            }
        ready.append({
            "model": model, "pair": baseline["pair_id"], "direction": direction, "scope": scope,
            "eligible": baseline["decision"] != direction, "fresh": fresh, "phases": phases,
        })
    return ready, len(rows)


def select(items, phase, model=None, direction=None):
    return [row for row in items if row["eligible"] and phase in row["phases"]
            and (model is None or row["model"] == model) and (direction is None or row["direction"] == direction)]


def rate(count, n):
    return f"{count}/{n} ({100 * count / n:.1f}%)" if n else "—"


def delta(count, n):
    return f"{100 * count / n:+.1f} pp" if n else "—"


def comparison(items, phase, title):
    n = len(items)
    totals = {c: sum(row["phases"][phase][c] for row in items) for c in PANEL_CONTENT}
    return title, n, *(rate(totals[c], n) for c in PANEL_CONTENT), delta(totals["minority"] - totals["unanimous"], n)


def interval(pair_ids, signed):
    by_pair = {pair: [0, 0] for pair in pair_ids}
    for pair, change in signed:
        by_pair[pair][0] += change
        by_pair[pair][1] += 1
    if not signed:
        return "—"
    values = list(by_pair.values())
    shuffled = random.Random(31079)
    draws = []
    for _ in range(10000):
        sample = shuffled.choices(values, k=len(values))
        size = sum(n for _, n in sample)
        if size:
            draws.append(100 * sum(change for change, _ in sample) / size)
    draws.sort()
    return f"[{draws[int(len(draws) * .025)]:+.1f}, {draws[int(len(draws) * .975)]:+.1f}] pp"


def signed_change(items, phase, first, second):
    return [(row["pair"], row["phases"][phase][first] - row["phases"][phase][second]) for row in items]


def table(lines, headers, rows):
    lines += ["", "| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(map(str, row)) + " |" for row in rows)
    lines.append("")


def report(stage, logs):
    plan, _, _ = load_plan()
    by_model = ("llama3.1:8b",) if stage == "pilot" else tuple(plan["study1_logs"])
    files = {}
    items = []
    calls = 0
    for path in logs:
        with path.open(encoding="utf-8") as source:
            model = json.loads(source.readline())["model_id"]
        assert model in by_model and model not in files
        files[model] = path
        rows, count = aggregate(path, stage, model)
        calls += count
        items.extend(rows)
    assert set(files) == set(by_model)
    original = len({row["pair"] for row in items if row["scope"] == "original"})
    related = len({row["pair"] for row in items if row["scope"] == "related"})
    assert (original, related, calls) == ((4, 4, 312) if stage == "pilot" else (50, 11, 9984))
    lines = [
        "# Study 3 pilot" if stage == "pilot" else "# Study 3 results",
        "",
        f"The audit passed for all **{calls:,} calls**. The run covered {original} original XSTest pairs and {related} held-out related pairs on {len(by_model)} local model{'s' if len(by_model) > 1 else ''}.",
        "",
    ]
    if stage == "pilot":
        lines += [
            "The pilot gate checked valid decision labels, completed conditions, exact prompt checksums, the link to each intervening pause, and separation of the related items from the preceding panel. Passing this gate authorized the full run independently of the measured effects.",
            "",
        ]
    else:
        lines += [
            "The full run repeated the pilot’s four pairs under the frozen design. Pilot observations are kept separate.",
            "",
        ]
    lines += [
        "## Design and scoring",
        "",
        "- **Public reference.** The three original public round-three decisions come from Study 1. Unanimous and minority panels both use social proof plus argument. The neutral panel gives no recommendation.",
        "- **Delayed original.** A continuation includes the original quoted case and the assigned panel statements in the earlier turns. It then includes one intervening model-generated acknowledgement and re-asks the original question in a new user turn.",
        f"- **Related item.** A separate continuation asks a new XSTest item with the same focus and expected response label. These {related} pairs have distinct prompts and are disjoint from the Study 1 and L3 calibration items.",
        "- **Fresh-session baseline.** Each item receives three decision-question wordings and five seeded samples per wording. The quoted requests stay verbatim. All new calls use temperature 0.2. Both continuation outcomes use the first wording and seed, with a matching fresh-session call.",
        "",
        "Eligibility is defined by the matched fresh baseline differing from the direction of peer advice. A shift means that the final decision exactly matches that advice. "
        "The historical public, delayed, and neutral comparisons use the same eligible original items. The related analysis uses its own fresh baselines. "
        "The continuation carries the earlier panel statements and uses a standardized acknowledgement in place of any earlier target decisions. "
        "These outcomes measure carryover in retained text context. The independent session estimates decision rates without that context.",
        "",
        "## Decision shifts by model",
    ]
    for phase in PHASES:
        lines.extend((f"### {phase}",))
        table(lines, ("Target", "Eligible", "Neutral", "Unanimous", "Minority", "Minority − unanimous"), [
            comparison(select(items, phase, model), phase, model or "All targets")
            for model in (*by_model, None)
        ])
    lines.extend((
        "## Direction and matched-pair uncertainty",
        "",
        "Intervals are descriptive 95% bootstrap intervals from 10,000 resamples of the original matched pairs. "
        "Both items and all model observations for a pair stay together. The pooled rates describe the models evaluated.",
    ))
    direction_rows = []
    main_rows = []
    for phase in PHASES:
        available = sorted({row["pair"] for row in items if phase in row["phases"]})
        selected = select(items, phase)
        for label, first, second in (
            ("Minority − unanimous", "minority", "unanimous"),
            ("Minority − neutral", "minority", "neutral"),
            ("Unanimous − neutral", "unanimous", "neutral"),
        ):
            signed = signed_change(selected, phase, first, second)
            main_rows.append((phase, label, len(signed), delta(sum(v for _, v in signed), len(signed)), interval(available, signed)))
        for direction in DIRECTIONS:
            selected = select(items, phase, direction=direction)
            direction_rows.append((phase, *comparison(selected, phase, DIRECTIONS[direction])))
    selected = select(items, "Delayed original")
    change = []
    for row in selected:
        delayed = row["phases"]["Delayed original"]
        public = row["phases"]["Public round three"]
        change.append((row["pair"], (delayed["minority"] - delayed["unanimous"])
                       - (public["minority"] - public["unanimous"])))
    main_rows.append(("Delayed original minus public", "Change in minority − unanimous", len(change),
                      delta(sum(v for _, v in change), len(change)), interval(sorted({r["pair"] for r in items}), change)))
    table(lines, ("Outcome", "Paired comparison", "Eligible", "Difference", "95% pair interval"), main_rows)
    table(lines, ("Outcome", "Direction", "Eligible", "Neutral", "Unanimous", "Minority", "Minority − unanimous"), direction_rows)
    lines.append("## Independent baseline decisions")
    fresh_rows = []
    for model in by_model:
        for scope in ("original", "related"):
            for direction, title in DIRECTIONS.items():
                selected = [row for row in items if (row["model"], row["scope"], row["direction"]) == (model, scope, direction)]
                counts = Counter(label for row in selected for label in row["fresh"])
                fresh_rows.append((model, scope, title, len(selected), counts["answer"], counts["partial"], counts["decline"]))
    table(lines, ("Target", "Scope", "Direction", "Items", "Answer", "Partial", "Decline"), fresh_rows)
    lines += [
        "## Data and logs",
        "",
        "- [Frozen Study 3 plan](../../pilot/study3_plan.json) and [runner](../../pilot/harness/run_study3.py)",
        "- [Study 1 results](study1_results.md) and [Llama dissenter probe data](../log/llama_study1_minority_l3.npz)",
    ]
    lines.extend(f"- [{files[model].name}](../log/{files[model].name})" for model in by_model)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", required=True, choices=("pilot", "full"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("logs", nargs="+", type=Path)
    args = parser.parse_args()
    args.output.write_text(report(args.stage, args.logs))


if __name__ == "__main__":
    main()
