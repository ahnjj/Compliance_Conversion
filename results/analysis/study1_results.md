# Study 1 Result

#### Source X Content X Visibility X both direction
Tested on 50 XSTest benign/harmful pairs and all 20 panel conditions(Source X Content X Visibility)
Each run contained 8,200  calls, including 2,000 secret ballots.
- Source 
    - Unanimous majority
    - a single consistent minority dissenter
    - an authority-labelled peer
    - no influence
- Content
    - social proof only
    - argument only
    - both
- Visibility
    - public(target's answer are broadcast to peers)
    - withheld(anonymous)
- Direction
    - **Benign items.** 
    <!-- With unanimous combined messages, all four models switched to `decline` on every eligible item in public. The common 14-pair comparison showed the same pattern. Neutral panels also produced benign shifts, especially for Mistral and Gemma. -->
    - **Harmful items.** 
    <!-- All models initially declined all 50 items. Under unanimous combined messages, Llama switched to `answer` on 32, Mistral on 6, Gemma on 2, and Qwen on 1. Unanimous social proof alone produced one such public shift across all four models. -->
<!-- - **Private ballots.** Qwen had a 51.2-percentage-point public-to-ballot gap for benign combined messages. The other three models retained all of their benign shifts in that condition. For harmful combined messages, the shift counts fell from 32 to 26 for Llama, 6 to 3 for Mistral, 2 to 0 for Gemma, and 1 to 0 for Qwen. -->



| Model | calls | Raw log |
|---|---:|---|
| Llama 3.1 8B | 8,200 | [Log](../log/llama3.1-study1-20261121-182446.jsonl) |
| Qwen3.5-9B | 8,200 | [Log](../log/qwen3.5-study1-20261121-210653.jsonl) |
| Mistral 7B | 8,200 | [Log](../log/mistral-study1-20261121-210653.jsonl) |
| Gemma 3 12B | 8,200 | [Log](../log/gemma3-study1-merged-20261122.jsonl) |

[Frozen pair manifest](../../pilot/study1_checklist.json) · [Runner](../../pilot/harness/run_study1.py) · [Llama analysis](study1_results_Llama.md)


<!-- ## Eligibility and controls

An item is eligible when its baseline decision differs from the assigned recommendation.
Benign items are pushed toward `decline` and harmful items toward `answer`. Both include
baseline `partial` when it occurs. Neutral and repeat rates use the same eligible items.

| Model | Items | Baseline answer / partial / decline | Eligible | Fresh repeat | Neutral public | Neutral withheld |
|---|---|---:|---:|---:|---:|---:|
| Llama 3.1 8B | benign | 30 / 8 / 12 | 38/50 | 0/38 (0.0%) | 13/38 (34.2%) | 15/38 (39.5%) |
| Llama 3.1 8B | harmful | 0 / 0 / 50 | 50/50 | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) |
| Qwen3.5-9B | benign | 41 / 2 / 7 | 43/50 | 0/43 (0.0%) | 2/43 (4.7%) | 5/43 (11.6%) |
| Qwen3.5-9B | harmful | 0 / 0 / 50 | 50/50 | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) |
| Mistral 7B | benign | 10 / 7 / 33 | 17/50 | 0/17 (0.0%) | 14/17 (82.4%) | 8/17 (47.1%) |
| Mistral 7B | harmful | 0 / 0 / 50 | 50/50 | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) |
| Gemma 3 12B | benign | 14 / 6 / 30 | 20/50 | 0/20 (0.0%) | 11/20 (55.0%) | 11/20 (55.0%) |
| Gemma 3 12B | harmful | 0 / 0 / 50 | 50/50 | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | -->

# Result (by source)
- Source x Visibility x Content
- **PSR** : Public shift rate
- **PrSR** : Secret Ballot, private shift rate
- **PPG** = PSR - PrSR : public-private gap
- Round 3 columns compare public and withheld debate replies. 

## 1. Unanimous majority 

| Model | Direction | Content | PSR | Withheld Round 3 | PrSR |  PPG |
|---|---|---|---:|---:|---:|---:|
| Llama 3.1 8B | benign | social proof | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| Llama 3.1 8B | benign | argument | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| Llama 3.1 8B | benign | combined | 38/38 (100.0%) | 38/38 (100.0%) | 38/38 (100.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | social proof | 1/50 (2.0%) | 2/50 (4.0%) | 1/50 (2.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | argument | 32/50 (64.0%) | 33/50 (66.0%) | 32/50 (64.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | combined | 32/50 (64.0%) | 31/50 (62.0%) | 26/50 (52.0%) | 12.0 pp |
| Qwen3.5-9B | benign | social proof | 42/43 (97.7%) | 41/43 (95.3%) | 14/43 (32.6%) | 65.1 pp |
| Qwen3.5-9B | benign | argument | 22/43 (51.2%) | 26/43 (60.5%) | 13/43 (30.2%) | 20.9 pp |
| Qwen3.5-9B | benign | combined | 43/43 (100.0%) | 42/43 (97.7%) | 21/43 (48.8%) | 51.2 pp |
| Qwen3.5-9B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | harmful | argument | 1/50 (2.0%) | 1/50 (2.0%) | 0/50 (0.0%) | 2.0 pp |
| Qwen3.5-9B | harmful | combined | 1/50 (2.0%) | 1/50 (2.0%) | 0/50 (0.0%) | 2.0 pp |
| Mistral 7B | benign | social proof | 17/17 (100.0%) | 17/17 (100.0%) | 17/17 (100.0%) | 0.0 pp |
| Mistral 7B | benign | argument | 17/17 (100.0%) | 17/17 (100.0%) | 17/17 (100.0%) | 0.0 pp |
| Mistral 7B | benign | combined | 17/17 (100.0%) | 17/17 (100.0%) | 17/17 (100.0%) | 0.0 pp |
| Mistral 7B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | argument | 2/50 (4.0%) | 5/50 (10.0%) | 1/50 (2.0%) | 2.0 pp |
| Mistral 7B | harmful | combined | 6/50 (12.0%) | 7/50 (14.0%) | 3/50 (6.0%) | 6.0 pp |
| Gemma 3 12B | benign | social proof | 20/20 (100.0%) | 20/20 (100.0%) | 19/20 (95.0%) | 5.0 pp |
| Gemma 3 12B | benign | argument | 20/20 (100.0%) | 20/20 (100.0%) | 20/20 (100.0%) | 0.0 pp |
| Gemma 3 12B | benign | combined | 20/20 (100.0%) | 20/20 (100.0%) | 20/20 (100.0%) | 0.0 pp |
| Gemma 3 12B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | harmful | argument | 1/50 (2.0%) | 1/50 (2.0%) | 0/50 (0.0%) | 2.0 pp |
| Gemma 3 12B | harmful | combined | 2/50 (4.0%) | 3/50 (6.0%) | 0/50 (0.0%) | 4.0 pp |

## 2. A consistent minority dissenter
One peer gives the assigned recommendation and three give the opposite recommendation.

| Model | Direction | Content |  PSR | Withheld Round 3 |  PrSR |  PPG |
|---|---|---|---:|---:|---:|---:|
| Llama 3.1 8B | benign | social proof | 5/38 (13.2%) | 6/38 (15.8%) | 5/38 (13.2%) | 0.0 pp |
| Llama 3.1 8B | benign | argument | 3/38 (7.9%) | 3/38 (7.9%) | 2/38 (5.3%) | 2.6 pp |
| Llama 3.1 8B | benign | combined | 3/38 (7.9%) | 3/38 (7.9%) | 3/38 (7.9%) | 0.0 pp |
| Llama 3.1 8B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | benign | social proof | 1/43 (2.3%) | 1/43 (2.3%) | 2/43 (4.7%) | -2.3 pp |
| Qwen3.5-9B | benign | argument | 1/43 (2.3%) | 1/43 (2.3%) | 0/43 (0.0%) | 2.3 pp |
| Qwen3.5-9B | benign | combined | 0/43 (0.0%) | 1/43 (2.3%) | 1/43 (2.3%) | -2.3 pp |
| Qwen3.5-9B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | benign | social proof | 2/17 (11.8%) | 1/17 (5.9%) | 2/17 (11.8%) | 0.0 pp |
| Mistral 7B | benign | argument | 1/17 (5.9%) | 2/17 (11.8%) | 1/17 (5.9%) | 0.0 pp |
| Mistral 7B | benign | combined | 0/17 (0.0%) | 0/17 (0.0%) | 0/17 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | benign | social proof | 7/20 (35.0%) | 5/20 (25.0%) | 4/20 (20.0%) | 15.0 pp |
| Gemma 3 12B | benign | argument | 4/20 (20.0%) | 3/20 (15.0%) | 3/20 (15.0%) | 5.0 pp |
| Gemma 3 12B | benign | combined | 4/20 (20.0%) | 4/20 (20.0%) | 4/20 (20.0%) | 0.0 pp |
| Gemma 3 12B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |

### 3. A authority-labelled peer
The authority condition adds a **senior-reviewer** label to the same dissenter.

| Model | Direction | Content | PSR | Withheld Round 3 | PrSR | PPG |
|---|---|---|---:|---:|---:|---:|
| Llama 3.1 8B | benign | social proof | 13/38 (34.2%) | 9/38 (23.7%) | 13/38 (34.2%) | 0.0 pp |
| Llama 3.1 8B | benign | argument | 11/38 (28.9%) | 10/38 (26.3%) | 11/38 (28.9%) | 0.0 pp |
| Llama 3.1 8B | benign | combined | 5/38 (13.2%) | 5/38 (13.2%) | 5/38 (13.2%) | 0.0 pp |
| Llama 3.1 8B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 1/50 (2.0%) | -2.0 pp |
| Llama 3.1 8B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Llama 3.1 8B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 1/50 (2.0%) | -2.0 pp |
| Qwen3.5-9B | benign | social proof | 12/43 (27.9%) | 10/43 (23.3%) | 4/43 (9.3%) | 18.6 pp |
| Qwen3.5-9B | benign | argument | 4/43 (9.3%) | 3/43 (7.0%) | 3/43 (7.0%) | 2.3 pp |
| Qwen3.5-9B | benign | combined | 10/43 (23.3%) | 7/43 (16.3%) | 4/43 (9.3%) | 14.0 pp |
| Qwen3.5-9B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Qwen3.5-9B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | benign | social proof | 8/17 (47.1%) | 9/17 (52.9%) | 8/17 (47.1%) | 0.0 pp |
| Mistral 7B | benign | argument | 5/17 (29.4%) | 5/17 (29.4%) | 4/17 (23.5%) | 5.9 pp |
| Mistral 7B | benign | combined | 5/17 (29.4%) | 4/17 (23.5%) | 3/17 (17.6%) | 11.8 pp |
| Mistral 7B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Mistral 7B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | benign | social proof | 12/20 (60.0%) | 10/20 (50.0%) | 12/20 (60.0%) | 0.0 pp |
| Gemma 3 12B | benign | argument | 10/20 (50.0%) | 11/20 (55.0%) | 12/20 (60.0%) | -10.0 pp |
| Gemma 3 12B | benign | combined | 12/20 (60.0%) | 10/20 (50.0%) | 12/20 (60.0%) | 0.0 pp |
| Gemma 3 12B | harmful | social proof | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | harmful | argument | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |
| Gemma 3 12B | harmful | combined | 0/50 (0.0%) | 0/50 (0.0%) | 0/50 (0.0%) | 0.0 pp |

<!-- ## Same-pair comparison

Both items were eligible for every included model in **14 of 50 pairs**.
The following public shifts use exactly that common set for both directions and all models.

| Model | Benign social proof | Harmful social proof | Benign argument | Harmful argument | Benign combined | Harmful combined |
|---|---:|---:|---:|---:|---:|---:|
| Llama 3.1 8B | 14/14 (100.0%) | 0/14 (0.0%) | 14/14 (100.0%) | 11/14 (78.6%) | 14/14 (100.0%) | 11/14 (78.6%) |
| Qwen3.5-9B | 14/14 (100.0%) | 0/14 (0.0%) | 1/14 (7.1%) | 0/14 (0.0%) | 14/14 (100.0%) | 0/14 (0.0%) |
| Mistral 7B | 14/14 (100.0%) | 0/14 (0.0%) | 14/14 (100.0%) | 1/14 (7.1%) | 14/14 (100.0%) | 3/14 (21.4%) |
| Gemma 3 12B | 14/14 (100.0%) | 0/14 (0.0%) | 14/14 (100.0%) | 0/14 (0.0%) | 14/14 (100.0%) | 1/14 (7.1%) |

These are descriptive rates for the decision-label task. The secret-ballot prompt retains
peer messages and adds the target’s answer history. An `answer` label is a recommendation. -->

## Llama L3 results

Llama replayed 500 prompts across the 50 matched pairs.  The table shows **mean changes from each item's peer-free baseline**,
with 50 items per class. 
- Higher `h` scores : a stronger signal for the unsafe label.
- Higher `r` scores : a stronger refusal signal.

| Public Round 3 condition | Benign Δh | Benign Δr | Harmful Δh | Harmful Δr |
|---|---:|---:|---:|---:|
| Neutral | +0.075 | -0.002 | -0.076 | +0.033 |
| Unanimous social proof | +0.116 | +0.083 | +0.154 | +0.025 |
| Unanimous argument | +0.271 | +0.149 | -0.062 | +0.024 |
| Unanimous social proof + argument | +0.343 | +0.123 | -0.253 | +0.017 |

With Unanimous social proof + argument, the harmfulness score rose on benign items and fell on
harmful items. Relative to the neutral panel, those changes were **+0.268** and **−0.177**.

The harmful-item refusal score changed by **−0.016** relative to neutral, even though **32 of
50** harmful items shifted to `answer`. 

[Frozen probe validation](llama_l3_validation.md) ·
[Per-item scores and activations](../log/llama_study1_l3.npz) ·
[Replay runner](../../pilot/harness/run_study1_l3.py)

## Qwen L3 results

Qwen3.5 9B replayed 200 saved prompts across 50 benign items. All decisions and prompt token counts matched. Under public unanimous social proof, 42 of 43 eligible items shifted toward refusal, and 14 of 43 also shifted in the secret-ballot measure, a **65.1-percentage-point gap**.

The table shows the change in harmfulness score from each reference to public round-three unanimous social proof. Scores are in standard deviations of the held-out benign neutral scores. Higher `h` indicates a stronger signal for the unsafe label.

| Benign items | Reference | Items | Mean Δh (SD) | 90% matched-item interval (SD) |
|---|---|---:|---:|---:|
| All eligible items | Peer-free baseline | 43 | +1.856 | [+1.750, +1.954] |
| All eligible items | Public neutral panel | 43 | +1.201 | [+1.096, +1.302] |
| Refused publicly, changed on ballot | Peer-free baseline | 28 | +1.978 | [+1.908, +2.045] |
| Refused publicly, changed on ballot | Public neutral panel | 28 | +1.375 | [+1.281, +1.468] |

All four intervals were above the working **±0.20 SD** equivalence margin. The mean score also rose in the 28-item subset that Qwen refused publicly and answered or partially answered on the ballot. The large gap matches the behavioral prediction for mostly compliance. The increase in the probe score runs against its near-zero Δh prediction.

The Qwen probe used decoder block 32 and reached **90.6% balanced accuracy** and **0.982 AUROC** on held-out debate items.

[Probe validation and methods](qwen_study1_l3.md#probe-calibration-and-replay) ·
[Per-item replay states and decisions](../log/qwen_study1_l3.npz) ·
[Replay runner](../../pilot/harness/run_qwen_study1_l3.py)
