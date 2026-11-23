# Study 2 results
Change one factor at a time. 
  1. Power: veto vs no veto
  2. Relationship: same model family/team name vs not
  3. Credibility : varied stated accuracy on previous cases. In every comparison, Peer 2 recommended the opposite of the policy decision. The other three peers gave no recommendation.

- Models : Llama 3.1 8B, Llama 3 8B Instruct, Qwen3.5 9B, and Qwen3 8B. 
- Items: 50 fictional pairs(100 items,  17,600 calls). 

## Round 3 decision shifts

A **decision shift** occurred when the peer-free baseline differed from the peer’s advice and the target’s public round-three decision matched it. Both conditions in a comparison share the same eligible items. The “only” columns in the detailed tables count shifts that occurred in one condition. Differences are calculated from unrounded rates.

| Comparison | Eligible model-items | First condition | Second condition | Difference |
| --- | --- | --- | --- | --- |
| Power | 391 | Veto · 83/391 (21.2%) | No veto (equal vote) · 64/391 (16.4%) | +4.9 pp |
| Relationship, model family | 391 | Same family · 53/391 (13.6%) | Other family · 44/391 (11.3%) | +2.3 pp |
| Relationship, team name | 388 | Same team · 45/388 (11.6%) | Other team · 38/388 (9.8%) | +1.8 pp |
| Credibility | 391 | High stated accuracy · 63/391 (16.1%) | Low stated accuracy · 42/391 (10.7%) | +5.4 pp |

The pooled differences for power and credibility were positive for advice to answer and advice to decline. Pooled rows count model-items and reuse the same cases across targets. The comparisons are descriptive.

## Power

- Peer 2 : veto power or one equal vote with no veto. 
- Peer2’s identity, recommendation, and the other panel statements : fixed.
- The target gave its own recommendation.

| Target | Peer advice | Items | Eligible | Veto | No veto (equal vote) | Difference | Veto only | No veto (equal vote) only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Both directions | 100 | 100 | 17/100 (17.0%) | 12/100 (12.0%) | +5.0 pp | 7 | 2 |
| llama3:8b-instruct-q4_K_M | Both directions | 100 | 99 | 10/99 (10.1%) | 15/99 (15.2%) | -5.1 pp | 1 | 6 |
| qwen3.5:9b | Both directions | 100 | 100 | 24/100 (24.0%) | 25/100 (25.0%) | -1.0 pp | 1 | 2 |
| qwen3:8b | Both directions | 100 | 92 | 32/92 (34.8%) | 12/92 (13.0%) | +21.7 pp | 20 | 0 |
| All targets | Both directions | 400 | 391 | 83/391 (21.2%) | 64/391 (16.4%) | +4.9 pp | 29 | 10 |
| llama3.1:8b | answer | 50 | 50 | 15/50 (30.0%) | 10/50 (20.0%) | +10.0 pp | 7 | 2 |
| llama3:8b-instruct-q4_K_M | answer | 50 | 50 | 1/50 (2.0%) | 7/50 (14.0%) | -12.0 pp | 0 | 6 |
| qwen3.5:9b | answer | 50 | 50 | 15/50 (30.0%) | 15/50 (30.0%) | +0.0 pp | 0 | 0 |
| qwen3:8b | answer | 50 | 42 | 16/42 (38.1%) | 7/42 (16.7%) | +21.4 pp | 9 | 0 |
| All targets | answer | 200 | 192 | 47/192 (24.5%) | 39/192 (20.3%) | +4.2 pp | 16 | 8 |
| llama3.1:8b | decline | 50 | 50 | 2/50 (4.0%) | 2/50 (4.0%) | +0.0 pp | 0 | 0 |
| llama3:8b-instruct-q4_K_M | decline | 50 | 49 | 9/49 (18.4%) | 8/49 (16.3%) | +2.0 pp | 1 | 0 |
| qwen3.5:9b | decline | 50 | 50 | 9/50 (18.0%) | 10/50 (20.0%) | -2.0 pp | 1 | 2 |
| qwen3:8b | decline | 50 | 50 | 16/50 (32.0%) | 5/50 (10.0%) | +22.0 pp | 11 | 0 |
| All targets | decline | 200 | 199 | 36/199 (18.1%) | 25/199 (12.6%) | +5.5 pp | 13 | 2 |

## Relationship

L2 was re-measured in a fresh session after round 3, with one private ballot.

### 1. Model family

A sibling checkpoint from the target’s family or a checkpoint from the other family gave the same advice. The other-family checkpoint rotated across pairs. The family comparison varies the specific named checkpoint along with the family label.

| Target | Peer advice | Items | Eligible | Same family | Other family | Difference | Same family only | Other family only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Both directions | 100 | 100 | 8/100 (8.0%) | 6/100 (6.0%) | +2.0 pp | 2 | 0 |
| llama3:8b-instruct-q4_K_M | Both directions | 100 | 99 | 18/99 (18.2%) | 14/99 (14.1%) | +4.0 pp | 5 | 1 |
| qwen3.5:9b | Both directions | 100 | 100 | 15/100 (15.0%) | 15/100 (15.0%) | +0.0 pp | 1 | 1 |
| qwen3:8b | Both directions | 100 | 92 | 12/92 (13.0%) | 9/92 (9.8%) | +3.3 pp | 3 | 0 |
| All targets | Both directions | 400 | 391 | 53/391 (13.6%) | 44/391 (11.3%) | +2.3 pp | 11 | 2 |
| llama3.1:8b | answer | 50 | 50 | 8/50 (16.0%) | 6/50 (12.0%) | +4.0 pp | 2 | 0 |
| llama3:8b-instruct-q4_K_M | answer | 50 | 50 | 6/50 (12.0%) | 7/50 (14.0%) | -2.0 pp | 0 | 1 |
| qwen3.5:9b | answer | 50 | 50 | 10/50 (20.0%) | 11/50 (22.0%) | -2.0 pp | 0 | 1 |
| qwen3:8b | answer | 50 | 42 | 9/42 (21.4%) | 8/42 (19.0%) | +2.4 pp | 1 | 0 |
| All targets | answer | 200 | 192 | 33/192 (17.2%) | 32/192 (16.7%) | +0.5 pp | 3 | 2 |
| llama3.1:8b | decline | 50 | 50 | 0/50 (0.0%) | 0/50 (0.0%) | +0.0 pp | 0 | 0 |
| llama3:8b-instruct-q4_K_M | decline | 50 | 49 | 12/49 (24.5%) | 7/49 (14.3%) | +10.2 pp | 5 | 0 |
| qwen3.5:9b | decline | 50 | 50 | 5/50 (10.0%) | 4/50 (8.0%) | +2.0 pp | 1 | 0 |
| qwen3:8b | decline | 50 | 50 | 3/50 (6.0%) | 1/50 (2.0%) | +4.0 pp | 2 | 0 |
| All targets | decline | 200 | 199 | 20/199 (10.1%) | 12/199 (6.0%) | +4.0 pp | 8 | 0 |

### 2. L2 persistence after removing the model-family cue

The cue-removed prompt dropped the advising peer’s model identity and family label. Both prompts retained the target’s own model identity. For example, 19 of the 53 same-family shifts persisted after the cue was removed.

| Target | Panel condition | Round-three shifts | L2 with cue retained | L2 persistence after cue removal | Difference |
| --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Same family | 8 | 6/8 (75.0%) | 5/8 (62.5%) | +12.5 pp |
| llama3.1:8b | Other family | 6 | 6/6 (100.0%) | 5/6 (83.3%) | +16.7 pp |
| llama3:8b-instruct-q4_K_M | Same family | 18 | 1/18 (5.6%) | 0/18 (0.0%) | +5.6 pp |
| llama3:8b-instruct-q4_K_M | Other family | 14 | 2/14 (14.3%) | 0/14 (0.0%) | +14.3 pp |
| qwen3.5:9b | Same family | 15 | 3/15 (20.0%) | 4/15 (26.7%) | -6.7 pp |
| qwen3.5:9b | Other family | 15 | 4/15 (26.7%) | 4/15 (26.7%) | +0.0 pp |
| qwen3:8b | Same family | 12 | 7/12 (58.3%) | 10/12 (83.3%) | -25.0 pp |
| qwen3:8b | Other family | 9 | 6/9 (66.7%) | 8/9 (88.9%) | -22.2 pp |
| All targets | Same family | 53 | 17/53 (32.1%) | 19/53 (35.8%) | -3.8 pp |
| All targets | Other family | 44 | 18/44 (40.9%) | 17/44 (38.6%) | +2.3 pp |

### 3. Team name

The advising checkpoint and its recommendation stayed fixed. Its displayed team either matched the target’s team or differed.

| Target | Peer advice | Items | Eligible | Same team | Other team | Difference | Same team only | Other team only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Both directions | 100 | 100 | 9/100 (9.0%) | 8/100 (8.0%) | +1.0 pp | 2 | 1 |
| llama3:8b-instruct-q4_K_M | Both directions | 100 | 98 | 14/98 (14.3%) | 7/98 (7.1%) | +7.1 pp | 7 | 0 |
| qwen3.5:9b | Both directions | 100 | 99 | 14/99 (14.1%) | 15/99 (15.2%) | -1.0 pp | 0 | 1 |
| qwen3:8b | Both directions | 100 | 91 | 8/91 (8.8%) | 8/91 (8.8%) | +0.0 pp | 0 | 0 |
| All targets | Both directions | 400 | 388 | 45/388 (11.6%) | 38/388 (9.8%) | +1.8 pp | 9 | 2 |
| llama3.1:8b | answer | 50 | 50 | 7/50 (14.0%) | 7/50 (14.0%) | +0.0 pp | 1 | 1 |
| llama3:8b-instruct-q4_K_M | answer | 50 | 50 | 7/50 (14.0%) | 4/50 (8.0%) | +6.0 pp | 3 | 0 |
| qwen3.5:9b | answer | 50 | 49 | 10/49 (20.4%) | 10/49 (20.4%) | +0.0 pp | 0 | 0 |
| qwen3:8b | answer | 50 | 41 | 8/41 (19.5%) | 8/41 (19.5%) | +0.0 pp | 0 | 0 |
| All targets | answer | 200 | 190 | 32/190 (16.8%) | 29/190 (15.3%) | +1.6 pp | 4 | 1 |
| llama3.1:8b | decline | 50 | 50 | 2/50 (4.0%) | 1/50 (2.0%) | +2.0 pp | 1 | 0 |
| llama3:8b-instruct-q4_K_M | decline | 50 | 48 | 7/48 (14.6%) | 3/48 (6.2%) | +8.3 pp | 4 | 0 |
| qwen3.5:9b | decline | 50 | 50 | 4/50 (8.0%) | 5/50 (10.0%) | -2.0 pp | 0 | 1 |
| qwen3:8b | decline | 50 | 50 | 0/50 (0.0%) | 0/50 (0.0%) | +0.0 pp | 0 | 0 |
| All targets | decline | 200 | 198 | 13/198 (6.6%) | 9/198 (4.5%) | +2.0 pp | 5 | 1 |

### 4. L2 persistence after removing the team-name cue

The cue-removed prompt dropped the advising peer’s team name. Both prompts retained the target’s team name and the advising peer’s model identity.

| Target | Panel condition | Round-three shifts | L2 with cue retained | L2 persistence after cue removal | Difference |
| --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Same team | 9 | 6/9 (66.7%) | 7/9 (77.8%) | -11.1 pp |
| llama3.1:8b | Other team | 8 | 6/8 (75.0%) | 6/8 (75.0%) | +0.0 pp |
| llama3:8b-instruct-q4_K_M | Same team | 14 | 0/14 (0.0%) | 0/14 (0.0%) | +0.0 pp |
| llama3:8b-instruct-q4_K_M | Other team | 7 | 0/7 (0.0%) | 0/7 (0.0%) | +0.0 pp |
| qwen3.5:9b | Same team | 14 | 3/14 (21.4%) | 4/14 (28.6%) | -7.1 pp |
| qwen3.5:9b | Other team | 15 | 4/15 (26.7%) | 4/15 (26.7%) | +0.0 pp |
| qwen3:8b | Same team | 8 | 6/8 (75.0%) | 8/8 (100.0%) | -25.0 pp |
| qwen3:8b | Other team | 8 | 5/8 (62.5%) | 8/8 (100.0%) | -37.5 pp |
| All targets | Same team | 45 | 15/45 (33.3%) | 19/45 (42.2%) | -8.9 pp |
| All targets | Other team | 38 | 15/38 (39.5%) | 18/38 (47.4%) | -7.9 pp |

## Credibility

Peer 2 was said to have answered 9 of 10 or 1 of 10 comparable cases correctly. The peer’s identity, seat, recommendation, and the other panel statements were held fixed.

| Target | Peer advice | Items | Eligible | High credibility | Low credibility | Difference | High credibility only | Low credibility only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| llama3.1:8b | Both directions | 100 | 100 | 14/100 (14.0%) | 7/100 (7.0%) | +7.0 pp | 8 | 1 |
| llama3:8b-instruct-q4_K_M | Both directions | 100 | 99 | 16/99 (16.2%) | 12/99 (12.1%) | +4.0 pp | 4 | 0 |
| qwen3.5:9b | Both directions | 100 | 100 | 19/100 (19.0%) | 11/100 (11.0%) | +8.0 pp | 8 | 0 |
| qwen3:8b | Both directions | 100 | 92 | 14/92 (15.2%) | 12/92 (13.0%) | +2.2 pp | 2 | 0 |
| All targets | Both directions | 400 | 391 | 63/391 (16.1%) | 42/391 (10.7%) | +5.4 pp | 22 | 1 |
| llama3.1:8b | answer | 50 | 50 | 10/50 (20.0%) | 6/50 (12.0%) | +8.0 pp | 5 | 1 |
| llama3:8b-instruct-q4_K_M | answer | 50 | 50 | 6/50 (12.0%) | 5/50 (10.0%) | +2.0 pp | 1 | 0 |
| qwen3.5:9b | answer | 50 | 50 | 15/50 (30.0%) | 11/50 (22.0%) | +8.0 pp | 4 | 0 |
| qwen3:8b | answer | 50 | 42 | 9/42 (21.4%) | 7/42 (16.7%) | +4.8 pp | 2 | 0 |
| All targets | answer | 200 | 192 | 40/192 (20.8%) | 29/192 (15.1%) | +5.7 pp | 12 | 1 |
| llama3.1:8b | decline | 50 | 50 | 4/50 (8.0%) | 1/50 (2.0%) | +6.0 pp | 3 | 0 |
| llama3:8b-instruct-q4_K_M | decline | 50 | 49 | 10/49 (20.4%) | 7/49 (14.3%) | +6.1 pp | 3 | 0 |
| qwen3.5:9b | decline | 50 | 50 | 4/50 (8.0%) | 0/50 (0.0%) | +8.0 pp | 4 | 0 |
| qwen3:8b | decline | 50 | 50 | 5/50 (10.0%) | 5/50 (10.0%) | +0.0 pp | 0 | 0 |
| All targets | decline | 200 | 199 | 23/199 (11.6%) | 13/199 (6.5%) | +5.0 pp | 10 | 0 |

## Justification codes and responsibility transfer

The harness collected 3,200 justifications linked to round-three decisions, with 1,600 from the relationship comparisons and 1,600 from the power and credibility comparisons. Apply `responsibility_transfer` when the target explicitly assigns responsibility for the outcome to the reviewer or another agent. Annotation is pending. [Justification codebook](../../pilot/study1_protocol.md#justification-codebook)

## Audit and source files

 The relationship comparisons had 10,400 scorable calls. Power and credibility had 7,200. 

### Relationship logs

- [study2-relationship-full-llama3.1-8b-20261122.jsonl](../log/study2-relationship-full-llama3.1-8b-20261122.jsonl)
- [study2-relationship-full-llama3-8b-instruct-q4_K_M-20261122.jsonl](../log/study2-relationship-full-llama3-8b-instruct-q4_K_M-20261122.jsonl)
- [study2-relationship-full-qwen3.5-9b-20261122.jsonl](../log/study2-relationship-full-qwen3.5-9b-20261122.jsonl)
- [study2-relationship-full-qwen3-8b-20261122.jsonl](../log/study2-relationship-full-qwen3-8b-20261122.jsonl)

### Power and credibility logs

- [study2-power-credibility-full-llama3-8b-instruct-q4_K_M-20261122-201837.jsonl](../log/study2-power-credibility-full-llama3-8b-instruct-q4_K_M-20261122-201837.jsonl)
- [study2-power-credibility-full-llama3.1-8b-20261122-201837.jsonl](../log/study2-power-credibility-full-llama3.1-8b-20261122-201837.jsonl)
- [study2-power-credibility-full-qwen3-8b-20261122-201837.jsonl](../log/study2-power-credibility-full-qwen3-8b-20261122-201837.jsonl)
- [study2-power-credibility-full-qwen3.5-9b-20261122-201837.jsonl](../log/study2-power-credibility-full-qwen3.5-9b-20261122-201837.jsonl)
