# Study 3 results

The audit passed for all **9,984 calls**. The run covered 50 original XSTest pairs and 11 held-out related pairs on 4 local models.

The full run repeated the pilot’s four pairs under the frozen design. Pilot observations are kept separate.

## Main findings

- **Public decisions.** Minority panels produced shifts on **2.5%** of eligible observations, compared with **50.3%** for unanimous panels. The small public minority effect matches this part of H3.
- **Delayed decisions.** Minority shifts were **3.4%**, compared with **35.0%** for unanimous panels and **10.3%** for neutral panels. The minority–unanimous gap narrowed by **16.2 percentage points**, mainly because unanimous-panel shifts declined. The historical public stage and the new continuation also differ in prompt structure and sampling temperature.
- **Related items.** Minority and neutral panels each shifted **1/57 (1.8%)** eligible observations. Unanimous panels shifted **2/57 (3.5%)**. This set of 11 related pairs offered little evidence of transfer.

Together with the earlier Llama activation replay, Study 3 supports the public and latent parts of H3 in the tested conditions. The delayed and related-item decisions gave little evidence of a minority advantage. [Pilot results](study3_pilot.md)

## Design and scoring

- **Public reference.** The three original public round-three decisions come from Study 1. Unanimous and minority panels both use social proof plus argument. The neutral panel gives no recommendation.
- **Delayed original.** A continuation includes the original quoted case and the assigned panel statements in the earlier turns. It then includes one intervening model-generated acknowledgement and re-asks the original question in a new user turn.
- **Related item.** A separate continuation asks a new XSTest item with the same focus and expected response label. These 11 pairs have distinct prompts and are disjoint from the Study 1 and L3 calibration items.
- **Fresh-session baseline.** Each item receives three decision-question wordings and five seeded samples per wording. The quoted requests stay verbatim. All new calls use temperature 0.2. Both continuation outcomes use the first wording and seed, with a matching fresh-session call.

Eligibility is defined by the matched fresh baseline differing from the direction of peer advice. A shift means that the final decision exactly matches that advice. The historical public, delayed, and neutral comparisons use the same eligible original items. The related analysis uses its own fresh baselines. The continuation carries the earlier panel statements and uses a standardized acknowledgement in place of any earlier target decisions. These outcomes measure carryover in retained text context. The independent session estimates decision rates without that context.

## Decision shifts by model
### Public round three

| Target | Eligible | Neutral | Unanimous | Minority | Minority − unanimous |
| --- | --- | --- | --- | --- | --- |
| llama3.1:8b | 90 | 15/90 (16.7%) | 72/90 (80.0%) | 3/90 (3.3%) | -76.7 pp |
| qwen3.5:9b | 92 | 2/92 (2.2%) | 43/92 (46.7%) | 0/92 (0.0%) | -46.7 pp |
| mistral:7b-instruct-v0.3-q4_K_M | 68 | 15/68 (22.1%) | 24/68 (35.3%) | 1/68 (1.5%) | -33.8 pp |
| gemma3:12b | 70 | 11/70 (15.7%) | 22/70 (31.4%) | 4/70 (5.7%) | -25.7 pp |
| All targets | 320 | 43/320 (13.4%) | 161/320 (50.3%) | 8/320 (2.5%) | -47.8 pp |

### Delayed original

| Target | Eligible | Neutral | Unanimous | Minority | Minority − unanimous |
| --- | --- | --- | --- | --- | --- |
| llama3.1:8b | 90 | 11/90 (12.2%) | 48/90 (53.3%) | 4/90 (4.4%) | -48.9 pp |
| qwen3.5:9b | 92 | 4/92 (4.3%) | 33/92 (35.9%) | 1/92 (1.1%) | -34.8 pp |
| mistral:7b-instruct-v0.3-q4_K_M | 68 | 1/68 (1.5%) | 11/68 (16.2%) | 0/68 (0.0%) | -16.2 pp |
| gemma3:12b | 70 | 17/70 (24.3%) | 20/70 (28.6%) | 6/70 (8.6%) | -20.0 pp |
| All targets | 320 | 33/320 (10.3%) | 112/320 (35.0%) | 11/320 (3.4%) | -31.6 pp |

### Related item

| Target | Eligible | Neutral | Unanimous | Minority | Minority − unanimous |
| --- | --- | --- | --- | --- | --- |
| llama3.1:8b | 16 | 1/16 (6.2%) | 1/16 (6.2%) | 1/16 (6.2%) | +0.0 pp |
| qwen3.5:9b | 17 | 0/17 (0.0%) | 1/17 (5.9%) | 0/17 (0.0%) | -5.9 pp |
| mistral:7b-instruct-v0.3-q4_K_M | 12 | 0/12 (0.0%) | 0/12 (0.0%) | 0/12 (0.0%) | +0.0 pp |
| gemma3:12b | 12 | 0/12 (0.0%) | 0/12 (0.0%) | 0/12 (0.0%) | +0.0 pp |
| All targets | 57 | 1/57 (1.8%) | 2/57 (3.5%) | 1/57 (1.8%) | -1.8 pp |

## Direction and matched-pair uncertainty

Intervals are descriptive 95% bootstrap intervals from 10,000 resamples of the original matched pairs. Both items and all model observations for a pair stay together. The pooled rates describe the models evaluated.

| Outcome | Paired comparison | Eligible | Difference | 95% pair interval |
| --- | --- | --- | --- | --- |
| Public round three | Minority − unanimous | 320 | -47.8 pp | [-52.6, -42.7] pp |
| Public round three | Minority − neutral | 320 | -10.9 pp | [-13.5, -8.3] pp |
| Public round three | Unanimous − neutral | 320 | +36.9 pp | [+31.8, +41.7] pp |
| Delayed original | Minority − unanimous | 320 | -31.6 pp | [-35.5, -27.5] pp |
| Delayed original | Minority − neutral | 320 | -6.9 pp | [-10.0, -3.8] pp |
| Delayed original | Unanimous − neutral | 320 | +24.7 pp | [+20.8, +28.5] pp |
| Related item | Minority − unanimous | 57 | -1.8 pp | [-5.4, +0.0] pp |
| Related item | Minority − neutral | 57 | +0.0 pp | [+0.0, +0.0] pp |
| Related item | Unanimous − neutral | 57 | +1.8 pp | [+0.0, +5.4] pp |
| Delayed original minus public | Change in minority − unanimous | 320 | +16.2 pp | [+11.8, +20.7] pp |


| Outcome | Direction | Eligible | Neutral | Unanimous | Minority | Minority − unanimous |
| --- | --- | --- | --- | --- | --- | --- |
| Public round three | Toward refusal on benign items | 120 | 43/120 (35.8%) | 120/120 (100.0%) | 8/120 (6.7%) | -93.3 pp |
| Public round three | Toward answering on harmful items | 200 | 0/200 (0.0%) | 41/200 (20.5%) | 0/200 (0.0%) | -20.5 pp |
| Delayed original | Toward refusal on benign items | 120 | 33/120 (27.5%) | 100/120 (83.3%) | 11/120 (9.2%) | -74.2 pp |
| Delayed original | Toward answering on harmful items | 200 | 0/200 (0.0%) | 12/200 (6.0%) | 0/200 (0.0%) | -6.0 pp |
| Related item | Toward refusal on benign items | 13 | 1/13 (7.7%) | 2/13 (15.4%) | 1/13 (7.7%) | -7.7 pp |
| Related item | Toward answering on harmful items | 44 | 0/44 (0.0%) | 0/44 (0.0%) | 0/44 (0.0%) | +0.0 pp |

## Independent baseline decisions

| Target | Scope | Direction | Items | Answer | Partial | Decline |
| --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | original | Toward refusal on benign items | 50 | 470 | 92 | 188 |
| llama3.1:8b | original | Toward answering on harmful items | 50 | 0 | 0 | 750 |
| llama3.1:8b | related | Toward refusal on benign items | 11 | 65 | 10 | 90 |
| llama3.1:8b | related | Toward answering on harmful items | 11 | 0 | 0 | 165 |
| qwen3.5:9b | original | Toward refusal on benign items | 50 | 638 | 25 | 87 |
| qwen3.5:9b | original | Toward answering on harmful items | 50 | 0 | 1 | 749 |
| qwen3.5:9b | related | Toward refusal on benign items | 11 | 92 | 0 | 73 |
| qwen3.5:9b | related | Toward answering on harmful items | 11 | 0 | 0 | 165 |
| mistral:7b-instruct-v0.3-q4_K_M | original | Toward refusal on benign items | 50 | 174 | 86 | 490 |
| mistral:7b-instruct-v0.3-q4_K_M | original | Toward answering on harmful items | 50 | 0 | 0 | 750 |
| mistral:7b-instruct-v0.3-q4_K_M | related | Toward refusal on benign items | 11 | 15 | 0 | 150 |
| mistral:7b-instruct-v0.3-q4_K_M | related | Toward answering on harmful items | 11 | 0 | 0 | 165 |
| gemma3:12b | original | Toward refusal on benign items | 50 | 185 | 110 | 455 |
| gemma3:12b | original | Toward answering on harmful items | 50 | 0 | 0 | 750 |
| gemma3:12b | related | Toward refusal on benign items | 11 | 15 | 0 | 150 |
| gemma3:12b | related | Toward answering on harmful items | 11 | 0 | 0 | 165 |

## Data and logs

- [Frozen Study 3 plan](../../pilot/study3_plan.json) and [runner](../../pilot/harness/run_study3.py)
- [Study 1 results](study1_results.md) and [Llama dissenter probe data](../log/llama_study1_minority_l3.npz)
- [llama3.1-8b-study3-full-20261124-001504.jsonl](../log/llama3.1-8b-study3-full-20261124-001504.jsonl)
- [qwen3.5-9b-study3-full-20261124-001504.jsonl](../log/qwen3.5-9b-study3-full-20261124-001504.jsonl)
- [mistral-7b-instruct-v0.3-q4_K_M-study3-full-20261124-001504.jsonl](../log/mistral-7b-instruct-v0.3-q4_K_M-study3-full-20261124-001504.jsonl)
- [gemma3-12b-study3-full-20261124-001504.jsonl](../log/gemma3-12b-study3-full-20261124-001504.jsonl)
