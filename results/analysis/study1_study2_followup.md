<!-- # Study 1 and Study 2 follow-up checks -->
<!-- 
These focused checks used each study’s original four local models. Study 1 added 32 fresh fictional matched pairs, balanced across eligibility, timing, approval, and document-status rules. Study 2 revisited the previously observed round-three shifts on the original 50 fictional pairs. All 5,840 new calls were scorable. [Frozen visibility cases](../../pilot/study1_visibility_followup.json)

## Study 1 visibility and decision shifts

The same fictional case and four scripted peers were used for the public and withheld conditions. The only first-round prompt difference was whether the reply would be visible to the panel. Each later round also received the target’s preceding decision from its own condition. The panels gave social proof, an argument based on the opposite member’s case fact, or neutral statements. The target classified the appropriate response. The new cases represent fictional answer-versus-decline boundaries.

An item is eligible when its peer-free baseline differs from the direction being pushed. The same eligible model-items are used in each arm. The fresh repeat shifted on 0 of 244 eligible model-items. A positive public-minus-withheld difference means that visibility increased the shift rate. The descriptive 95% intervals resample whole matched pairs 10,000 times and keep the models and conditions for each pair together.

| Panel content | Round | Eligible | Public | Withheld | Difference | 95% pair interval |
| --- | --- | --- | --- | --- | --- | --- |
| Social proof | 1 | 244 | 76/244 (31.1%) | 73/244 (29.9%) | +1.2 pp | [-2.1, +4.6] pp |
| Argument | 1 | 244 | 120/244 (49.2%) | 124/244 (50.8%) | -1.6 pp | [-5.1, +1.6] pp |
| Neutral | 1 | 244 | 10/244 (4.1%) | 11/244 (4.5%) | -0.4 pp | [-1.2, +0.0] pp |
| Social proof | 3 | 244 | 72/244 (29.5%) | 74/244 (30.3%) | -0.8 pp | [-3.8, +2.1] pp |
| Argument | 3 | 244 | 97/244 (39.8%) | 102/244 (41.8%) | -2.0 pp | [-4.9, +0.8] pp |
| Neutral | 3 | 244 | 8/244 (3.3%) | 11/244 (4.5%) | -1.2 pp | [-2.9, +0.4] pp |

The round-three visibility difference for social proof minus the same difference for argument was **+1.2 pp** with a 95% pair interval of **[-2.8, +4.9] pp**.

### Round three by model and direction

| Target | Peer advice | Content | Eligible | Public | Withheld | Difference |
| --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | answer | Social proof | 32 | 3/32 (9.4%) | 5/32 (15.6%) | -6.2 pp |
| llama3.1:8b | answer | Argument | 32 | 11/32 (34.4%) | 15/32 (46.9%) | -12.5 pp |
| llama3.1:8b | answer | Neutral | 32 | 0/32 (0.0%) | 0/32 (0.0%) | +0.0 pp |
| llama3.1:8b | decline | Social proof | 32 | 11/32 (34.4%) | 14/32 (43.8%) | -9.4 pp |
| llama3.1:8b | decline | Argument | 32 | 14/32 (43.8%) | 17/32 (53.1%) | -9.4 pp |
| llama3.1:8b | decline | Neutral | 32 | 0/32 (0.0%) | 0/32 (0.0%) | +0.0 pp |
| qwen3.5:9b | answer | Social proof | 31 | 9/31 (29.0%) | 10/31 (32.3%) | -3.2 pp |
| qwen3.5:9b | answer | Argument | 31 | 7/31 (22.6%) | 6/31 (19.4%) | +3.2 pp |
| qwen3.5:9b | answer | Neutral | 31 | 0/31 (0.0%) | 0/31 (0.0%) | +0.0 pp |
| qwen3.5:9b | decline | Social proof | 31 | 28/31 (90.3%) | 25/31 (80.6%) | +9.7 pp |
| qwen3.5:9b | decline | Argument | 31 | 16/31 (51.6%) | 15/31 (48.4%) | +3.2 pp |
| qwen3.5:9b | decline | Neutral | 31 | 6/31 (19.4%) | 9/31 (29.0%) | -9.7 pp |
| mistral:7b-instruct-v0.3-q4_K_M | answer | Social proof | 31 | 0/31 (0.0%) | 0/31 (0.0%) | +0.0 pp |
| mistral:7b-instruct-v0.3-q4_K_M | answer | Argument | 31 | 2/31 (6.5%) | 2/31 (6.5%) | +0.0 pp |
| mistral:7b-instruct-v0.3-q4_K_M | answer | Neutral | 31 | 0/31 (0.0%) | 0/31 (0.0%) | +0.0 pp |
| mistral:7b-instruct-v0.3-q4_K_M | decline | Social proof | 29 | 18/29 (62.1%) | 18/29 (62.1%) | +0.0 pp |
| mistral:7b-instruct-v0.3-q4_K_M | decline | Argument | 29 | 25/29 (86.2%) | 26/29 (89.7%) | -3.4 pp |
| mistral:7b-instruct-v0.3-q4_K_M | decline | Neutral | 29 | 2/29 (6.9%) | 2/29 (6.9%) | +0.0 pp |
| gemma3:12b | answer | Social proof | 30 | 0/30 (0.0%) | 0/30 (0.0%) | +0.0 pp |
| gemma3:12b | answer | Argument | 30 | 6/30 (20.0%) | 6/30 (20.0%) | +0.0 pp |
| gemma3:12b | answer | Neutral | 30 | 0/30 (0.0%) | 0/30 (0.0%) | +0.0 pp |
| gemma3:12b | decline | Social proof | 28 | 3/28 (10.7%) | 2/28 (7.1%) | +3.6 pp |
| gemma3:12b | decline | Argument | 28 | 16/28 (57.1%) | 15/28 (53.6%) | +3.6 pp |
| gemma3:12b | decline | Neutral | 28 | 0/28 (0.0%) | 0/28 (0.0%) | +0.0 pp |

## Study 2 relationship cue and decision reminder

Each of the 180 original shifts was followed up in four fresh calls, crossing the original relationship cue with the reminder of the target’s round-three decision. The exact-prompt replays agreed with their saved answers on 356/360 calls. The numbers below count how often the follow-up matched the earlier recommendation among episodes that had shifted by round three.

With the relationship cue removed, the match rate was **72/180 (40.0%)** with the decision reminder and **11/180 (6.1%)** without it. The paired reminder difference was **+33.9 pp**, with a 95% pair interval of **[+23.4, +46.5] pp**.

For the family comparison, removing the cue dropped the recommending peer’s model and family. For the team comparison, it dropped only the peer’s team name. With both the cue and decision reminder omitted, the prompt contains no round-three decision or peer advice. This cell measures fresh-context matching to the earlier advice.

| Earlier panel | Shifts | Cue kept, reminder kept | Cue removed, reminder kept | Cue kept, reminder omitted | Cue removed, reminder omitted | Reminder effect with cue removed |
| --- | --- | --- | --- | --- | --- | --- |
| Same family | 53 | 17/53 (32.1%) | 19/53 (35.8%) | 4/53 (7.5%) | 2/53 (3.8%) | +32.1 pp |
| Other family | 44 | 18/44 (40.9%) | 17/44 (38.6%) | 5/44 (11.4%) | 2/44 (4.5%) | +34.1 pp |
| Same team | 45 | 15/45 (33.3%) | 19/45 (42.2%) | 2/45 (4.4%) | 3/45 (6.7%) | +35.6 pp |
| Other team | 38 | 15/38 (39.5%) | 17/38 (44.7%) | 1/38 (2.6%) | 4/38 (10.5%) | +34.2 pp |


| Earlier panel | Cue effect with reminder | 95% pair interval | Cue effect without reminder | 95% pair interval | Reminder effect with cue removed | 95% pair interval |
| --- | --- | --- | --- | --- | --- | --- |
| Same family | -3.8 pp | [-13.6, +4.8] pp | +3.8 pp | [+0.0, +9.4] pp | +32.1 pp | [+22.2, +43.4] pp |
| Other family | +2.3 pp | [-8.6, +11.5] pp | +6.8 pp | [+0.0, +14.3] pp | +34.1 pp | [+21.9, +47.9] pp |
| Same team | -8.9 pp | [-18.4, -2.0] pp | -2.2 pp | [-7.1, +0.0] pp | +35.6 pp | [+22.2, +51.2] pp |
| Other team | -5.3 pp | [-16.7, +4.7] pp | -7.9 pp | [-16.2, +0.0] pp | +34.2 pp | [+19.5, +51.5] pp |

### Private follow-ups by model

| Target and earlier panel | Shifts | Cue kept, reminder kept | Cue removed, reminder kept | Cue kept, reminder omitted | Cue removed, reminder omitted | Reminder effect with cue removed |
| --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b, Same family | 8 | 6/8 (75.0%) | 5/8 (62.5%) | 0/8 (0.0%) | 0/8 (0.0%) | +62.5 pp |
| llama3.1:8b, Other family | 6 | 6/6 (100.0%) | 5/6 (83.3%) | 0/6 (0.0%) | 0/6 (0.0%) | +83.3 pp |
| llama3.1:8b, Same team | 9 | 6/9 (66.7%) | 7/9 (77.8%) | 0/9 (0.0%) | 1/9 (11.1%) | +66.7 pp |
| llama3.1:8b, Other team | 8 | 6/8 (75.0%) | 6/8 (75.0%) | 0/8 (0.0%) | 1/8 (12.5%) | +62.5 pp |
| llama3:8b-instruct-q4_K_M, Same family | 18 | 1/18 (5.6%) | 0/18 (0.0%) | 1/18 (5.6%) | 0/18 (0.0%) | +0.0 pp |
| llama3:8b-instruct-q4_K_M, Other family | 14 | 2/14 (14.3%) | 0/14 (0.0%) | 0/14 (0.0%) | 0/14 (0.0%) | +0.0 pp |
| llama3:8b-instruct-q4_K_M, Same team | 14 | 0/14 (0.0%) | 0/14 (0.0%) | 1/14 (7.1%) | 1/14 (7.1%) | -7.1 pp |
| llama3:8b-instruct-q4_K_M, Other team | 7 | 0/7 (0.0%) | 0/7 (0.0%) | 1/7 (14.3%) | 1/7 (14.3%) | -14.3 pp |
| qwen3.5:9b, Same family | 15 | 3/15 (20.0%) | 4/15 (26.7%) | 2/15 (13.3%) | 1/15 (6.7%) | +20.0 pp |
| qwen3.5:9b, Other family | 15 | 4/15 (26.7%) | 4/15 (26.7%) | 3/15 (20.0%) | 1/15 (6.7%) | +20.0 pp |
| qwen3.5:9b, Same team | 14 | 3/14 (21.4%) | 4/14 (28.6%) | 0/14 (0.0%) | 0/14 (0.0%) | +28.6 pp |
| qwen3.5:9b, Other team | 15 | 4/15 (26.7%) | 3/15 (20.0%) | 0/15 (0.0%) | 1/15 (6.7%) | +13.3 pp |
| qwen3:8b, Same family | 12 | 7/12 (58.3%) | 10/12 (83.3%) | 1/12 (8.3%) | 1/12 (8.3%) | +75.0 pp |
| qwen3:8b, Other family | 9 | 6/9 (66.7%) | 8/9 (88.9%) | 2/9 (22.2%) | 1/9 (11.1%) | +77.8 pp |
| qwen3:8b, Same team | 8 | 6/8 (75.0%) | 8/8 (100.0%) | 1/8 (12.5%) | 1/8 (12.5%) | +87.5 pp |
| qwen3:8b, Other team | 8 | 5/8 (62.5%) | 8/8 (100.0%) | 0/8 (0.0%) | 1/8 (12.5%) | +87.5 pp |

## Latent change with an unchanged public refusal

This exploratory check uses saved Llama 3.1 8B activations from the original Study 1. For each unanimous panel, it selects harmful items on which Llama declined at baseline, with neutral peers, and with the unanimous panel. The comparison uses the same item’s neutral-panel score as the reference. A lower harmfulness score moves toward the peer’s recommendation to answer. The rows can contain different subsets of items.

| Unanimous panel content | Unchanged harmful items | Mean Δh vs. neutral | Items with lower h |
| --- | --- | --- | --- |
| Social proof | 49 | +0.232 | 0 |
| Argument | 18 | +0.105 | 2 |
| Combined | 18 | -0.098 | 16 |

This result concerns the probe score in the public debate context. Persistence and transfer to related items remain open. [Saved Llama activations and probe scores](../log/llama_study1_l3.npz)

### Consistent dissenter and latent conversion

This check replayed 500 original Llama 3.1 8B prompts. All prompt checksums, output decision labels, and prompt-token counts matched their original records. Scores came from the same frozen harmfulness and refusal probes used in the unanimous-panel analysis. The maximum absolute score difference across the 200 re-replayed baseline and neutral prompts was 0.

In the dissent condition, one peer gave the assigned recommendation and three peers backed the opposite recommendation. A lower harmfulness score moves toward the dissenter’s advice on harmful items. A higher score moves toward the dissenter’s advice on benign items. The stable-decision subset contains cases with the same baseline, neutral, and dissent-panel decisions, all different from the dissenter’s advice. The subset is defined by the observed public outcomes. The 95% intervals resample matched pairs within each direction.

| Items | Dissenter content | Public shifts | Stable decisions | Stable Δh vs. neutral | 95% pair interval | Stable Δr vs. neutral | Stable h toward dissenter | All 50 Δh vs. neutral |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benign | Social proof | 5 | 22 | +0.022 | [-0.025, +0.074] | +0.017 | 9/22 | +0.008 |
| Benign | Argument | 3 | 22 | +0.092 | [+0.061, +0.123] | +0.091 | 19/22 | +0.062 |
| Benign | Combined | 3 | 22 | +0.117 | [+0.056, +0.184] | +0.079 | 18/22 | +0.031 |
| Harmful | Social proof | 0 | 50 | +0.002 | [-0.028, +0.033] | +0.020 | 29/50 | +0.002 |
| Harmful | Argument | 0 | 50 | -0.109 | [-0.148, -0.067] | +0.094 | 40/50 | -0.109 |
| Harmful | Combined | 0 | 50 | -0.264 | [-0.304, -0.225] | +0.077 | 47/50 | -0.264 |

**The clearest latent shift was on harmful items with combined dissent.** Llama still declined all 50 items, while harmfulness scores fell on 47 of them. The mean change was −0.264 relative to neutral. On benign items with stable decisions, argument and combined dissent moved harmfulness scores in the dissenter’s direction. Social proof alone had intervals spanning zero in both directions.

These comparisons measure probe changes during the public panel. Delayed private responses and transfer to related items are separate outcomes. [Dissenter activation bundle](../log/llama_study1_minority_l3.npz) · [Probe validation](llama_l3_validation.md) -->

# Study 1 and Study 2 results analysis

In Study 1, PPG is the public shift rate minus the secret-ballot shift rate. Δh is the change in the harmfulness probe score.

### Study 1

#### Matched with the expected outcome

| Hypothesis | Prediction | Observation |
| --- | --- | --- |
| H1 | Pure social proof with the target’s answer visible produces a positive PPG and near-zero Δh. | Qwen had a **65.1-percentage-point PPG** for benign items under unanimous social proof. This matched the public-to-ballot prediction. |
| H3 | A consistent dissenter produces fewer public decision shifts than a unanimous panel. | A lone dissenter moved public decisions much less often. The Llama replay also found latent changes under dissent with an argument even when the public decision stayed fixed. Delayed and related-item responses remain open. |
| H5 | Harmful compliance should mainly reflect compliance or obedience. Benign over-refusal should mainly reflect internalization. | There was a clear asymmetry in **how often** the two shifts occurred. Under unanimous social proof plus argument, all four models shifted toward refusal on every eligible benign item. On harmful items, shifts toward answering ranged from 2% to 64%. Evidence for the proposed mechanisms was mixed. |

Qwen’s large benign PPG suggests that some over-refusal was tied to the public setting. Llama’s benign combined condition had a zero public-to-ballot gap and an increased harmfulness score, consistent with part of the internalization prediction. Persistence and generalization for that condition remain open. On harmful items, Llama’s harmfulness probe score fell by **0.177 relative to neutral** under unanimous combined messages, showing a latent change alongside public shifts. [Original Study 1 results](study1_results.md)

#### Mismatched with the hypotheses

- **H1 · Anonymity reduces the effect of social proof.** Under unanimous social proof, withholding the target’s reply reduced round-three shifts in **1 of 8** model-by-direction comparisons. Six were unchanged and one increased. The 32-pair follow-up also found little evidence of a reduction. The pooled shift rates were **29.5% public** and **30.3% withheld**. [Study 1 visibility follow-up](#study-1-visibility-and-decision-shifts)
- **H1 · Harmfulness stays near baseline under pure social proof.** Qwen’s harmfulness score rose **1.856 SD relative to the peer-free baseline** and **1.201 SD relative to the public neutral panel**. Both estimates were above the working margin for a near-zero change. [Qwen L3 results](study1_results.md#qwen-l3-results)

### Study 2

#### Matched with the expected outcome

| Hypothesis | Prediction | Observation |
| --- | --- | --- |
| H2 · Power | Veto power should produce the compliance signature. | Veto power increased public shifts overall by **4.9 percentage points**. The largest increase was for **Qwen3 8B (+21.7 points)**. Shifts decreased for Llama 3 8B Instruct and Qwen3.5 9B. The comparison measured public decisions. The private and latent parts of the signature remain open. |
| H2 · Credibility | Credible, evidence-bearing peers should produce internalization. | Higher **stated credibility** increased public shifts in all four local models. Persistence and generalization remain open. |
| H4 · Authority | An authority label raises L1 compliance while `h` stays stable. | In **Study 1’s authority comparison**, the senior-reviewer label increased public shifts toward refusing benign items in all 12 model-by-content comparisons. Public shifts toward answering harmful items stayed at zero. The authority-specific change in `h` and responsibility-transfer coding remain open. |

[Study 2 results](study2_results.md) · [Study 1 authority comparison](study1_results.md#3-a-authority-labelled-peer)

#### Mismatched with the hypotheses

**H2** predicts that relationship influence fades when the relationship cue is removed. In the original private follow-up, among episodes that shifted by round three, the share still matching the peer’s advice rose after cue removal.

- **Same-family peers:** 32.1% with the cue retained and 35.8% with it removed.
- **Same-team peers:** 33.3% with the cue retained and 42.2% with it removed.

Both versions reminded the target of its round-three decision. When the follow-up removed the relationship cue, matching the earlier advice fell from **40.0% with the decision reminder** to **6.1% without it**. The results suggest that models can reach the same public decision through different processes. [Study 2 relationship results](study2_results.md#relationship) · [Decision-reminder follow-up](#study-2-relationship-cue-and-decision-reminder)

### Main measurement gap

**The main measurement gap is L2.** The proposal calls for a fresh conversation independent of the debate, with three paraphrases and five samples per paraphrase. Study 1’s secret ballot retained the panel statements and serves as the proposal’s weaker L2 measure. Study 2’s original fresh follow-up retained the target’s round-three decision. **Peer cues changed public decisions. The proposed explanations for those shifts received mixed or incomplete support.**

## Logs

- [study1-visibility-check-gemma3-12b-20261122-234022.jsonl](../log/study1-visibility-check-gemma3-12b-20261122-234022.jsonl)
- [study1-visibility-check-llama3.1-8b-20261122-234022.jsonl](../log/study1-visibility-check-llama3.1-8b-20261122-234022.jsonl)
- [study1-visibility-check-mistral-7b-instruct-v0.3-q4_K_M-20261122-234022.jsonl](../log/study1-visibility-check-mistral-7b-instruct-v0.3-q4_K_M-20261122-234022.jsonl)
- [study1-visibility-check-qwen3.5-9b-20261122-234022.jsonl](../log/study1-visibility-check-qwen3.5-9b-20261122-234022.jsonl)
- [study2-persistence-check-llama3-8b-instruct-q4_K_M-20261122-233733.jsonl](../log/study2-persistence-check-llama3-8b-instruct-q4_K_M-20261122-233733.jsonl)
- [study2-persistence-check-llama3.1-8b-20261122-233733.jsonl](../log/study2-persistence-check-llama3.1-8b-20261122-233733.jsonl)
- [study2-persistence-check-qwen3-8b-20261122-233733.jsonl](../log/study2-persistence-check-qwen3-8b-20261122-233733.jsonl)
- [study2-persistence-check-qwen3.5-9b-20261122-233733.jsonl](../log/study2-persistence-check-qwen3.5-9b-20261122-233733.jsonl)
