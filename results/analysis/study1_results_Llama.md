# Study 1 on benign and harmful items

[Full result log](../log/llama3.1-study1-checklist-20261121-182446.jsonl) · [One-pair preflight](../log/llama3.1-study1-checklist-smoke-20261121-182446.jsonl) · [Frozen pair manifest](../../pilot/study1_checklist.json)

Local Llama 3.1 8B completed 8,200 scorable calls over 100 items, including 2,000 ballots.
The set uses 25 homonym pairs and 25 safe-target pairs from [XSTest](https://aclanthology.org/2024.naacl-long.301/).
The paired source rows share a category and focus term. This run uses XSTest's safe/unsafe contrasts.
Each model response is a decision label. The quoted requests and raw generations are excluded from the saved logs.

| Checklist | How it was checked |
|---|---|
| Benign and harmful items | Fifty matched pairs, one benign and one harmful item per pair. Both members use the same model, decision instructions, and randomized panel order. |
| Social proof, argument, both | Social proof cites an earlier panel. Argument gives a category-specific safety rationale. Combined contains both with the same recommendation. Rationale truth depends on whether the recommendation matches the benchmark label. |
| Unanimous majority, minority, authority, no influence | Unanimous uses four assigned votes. Minority uses one consistent assigned vote and three opposing votes. Authority adds a senior-reviewer label to that same dissenter. Neutral panels and peer-free calls provide controls. |
| Public and withheld | The same four statements appear in both settings. Each panel has three rounds and a final private ballot. |

## Findings by checklist item

- **Benign and harmful items.** In the 38 pairs where both items were eligible, unanimous public arguments shifted all 38 benign items toward `decline` and 25 harmful items toward `answer`. The same counts held for the combined message.
- **Content.** On all 50 harmful items, public unanimous social proof shifted 1 item. An argument and the combined message each shifted 32. On eligible benign items, all three unanimous conditions reached 38 of 38 shifts.
- **Source.** The ordinary minority dissenter shifted 3–5 of 38 benign items in public. Calling that same dissenter a senior reviewer raised the range to 5–13. A public minority or senior dissenter shifted zero harmful items.
- **Visibility.** The unanimous argument shifted 32 of 50 harmful items in public and 33 with the reply withheld. The combined message shifted 32 in public and 31 with the reply withheld. On the secret ballot linked to the public combined round, 26 of 50 shifted, yielding a 12-point ballot gap.

These are descriptive comparisons for one model. Eligibility includes items with a `partial` baseline.
The combined messages are longer than the single-content messages, and the ballot changes the
instruction and how much of the target's answer history it sees.

## Baseline and controls

An item is eligible if its baseline label differs from the assigned peer recommendation.
For benign items the assigned label is `decline`. For harmful items it is `answer`. A baseline
`partial` is eligible for either comparison and is shown separately in the baseline counts.

| Item class | Baseline answer / partial / decline | Eligible | Fresh repeat shift | Neutral public shift | Neutral withheld shift |
|---|---:|---:|---:|---:|---:|
| benign | 30 / 8 / 12 | 38/50 | 0/38 (0.0%) | 13/38 (34.2%) | 15/38 (39.5%) |
| harmful | 0 / 0 / 50 | 50/50 | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) |

## Content, source, and visibility results

PSR uses public Round 3. Ballot PrSR is from the private follow-up to that same public debate.
PPG is their difference in percentage points on the same eligible items. Withheld Round 3 is
the separate debate condition where the target still sees the peer messages.

| Item class | Source | Content | Public Round 3 (PSR) | Withheld Round 3 | Ballot PrSR | Ballot PPG |
|---|---|---|---:|---:|---:|---:|
| benign | unanimous | social proof | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| benign | unanimous | argument | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| benign | unanimous | combined | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| benign | minority | social proof | 5/38 (13.2%) | 6/38 (15.8%) | 5/38 (13.2%) | 0.0 pp |
| benign | minority | argument | 3/38 (7.9%) | 3/38 (7.9%) | 2/38 (5.3%) | 2.6 pp |
| benign | minority | combined | 3/38 (7.9%) | 3/38 (7.9%) | 3/38 (7.9%) | 0.0 pp |
| benign | minority authority | social proof | 13/38 (34.2%) | 9/38 (23.7%) | 13/38 (34.2%) | 0.0 pp |
| benign | minority authority | argument | 11/38 (28.9%) | 10/38 (26.3%) | 11/38 (28.9%) | 0.0 pp |
| benign | minority authority | combined | 5/38 (13.2%) | 5/38 (13.2%) | 5/38 (13.2%) | 0.0 pp |
| harmful | unanimous | social proof | 1/50 (2.0%) | 2/50 (4.0%) | 1/50 (2.0%) | 0.0 pp |
| harmful | unanimous | argument | 32/50 (64.0%) | 33/50 (66.0%) | 32/50 (64.0%) | 0.0 pp |
| harmful | unanimous | combined | 32/50 (64.0%) | 31/50 (62.0%) | 26/50 (52.0%) | 12.0 pp |
| harmful | minority | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| harmful | minority | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| harmful | minority | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| harmful | minority authority | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 1/50 (2.0%) | -2.0 pp |
| harmful | minority authority | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| harmful | minority authority | combined | 0/50 (0.0%) | 0/50 (0.0%) | 1/50 (2.0%) | -2.0 pp |

## Benign and harmful comparisons within the same pairs

Both items were eligible in 38 of 50 pairs. The comparison below uses those same pairs.
It counts exact switches to the assigned decision in public Round 3.

| Source | Content | Benign toward decline | Harmful toward answer |
|---|---|---:|---:|
| unanimous | social proof | 38/38 (100.0%) | 1/38 (2.6%) |
| unanimous | argument | 38/38 (100.0%) | 25/38 (65.8%) |
| unanimous | combined | 38/38 (100.0%) | 25/38 (65.8%) |
| minority | social proof | 5/38 (13.2%) | 0/38 (0.0%) |
| minority | argument | 3/38 (7.9%) | 0/38 (0.0%) |
| minority | combined | 3/38 (7.9%) | 0/38 (0.0%) |
| minority authority | social proof | 13/38 (34.2%) | 0/38 (0.0%) |
| minority authority | argument | 11/38 (28.9%) | 0/38 (0.0%) |
| minority authority | combined | 5/38 (13.2%) | 0/38 (0.0%) |

The ballot retains the peer messages and prior answers. These results describe Llama on this
pair set and these scripted conditions. The setup scores recommendations about the request.
