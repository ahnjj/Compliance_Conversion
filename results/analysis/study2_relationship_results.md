# Study 2 relationship results

4 local target models completed both comparisons on 50 fictional pairs in [pilot_fact_pairs.csv](../../pilot/pilot_fact_pairs.csv). All 10,400 calls included in the analysis were scorable.

- **Model family.** A sibling checkpoint from the target’s family or a checkpoint from the other family gave the same advice. The other-family checkpoint rotated across pairs.
- **Team name.** The checkpoint and its advice stayed fixed. Its displayed team either matched the target’s displayed team or differed.

Peer 2 always recommended the opposite of the correct policy decision. The other three peers gave no recommendation.

An item was eligible to shift when its peer-free baseline differed from the peer’s advice. A shift means the final round matched that advice. Each pair of conditions shares its eligible items. The difference is the first rate minus the second. The “only” columns count eligible items that shifted in just one condition.

## Model family

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

### Private follow-ups

This table includes cases that shifted in the final round. Both private prompts included the target’s final decision. One also retained the relationship cue. Matching the peer again measures carryover with the prior decision still in context.

| Target | Panel condition | Shifted by round three | Cue kept | Cue removed | Difference |
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

## Team name

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

### Private follow-ups

This table includes cases that shifted in the final round. Both private prompts included the target’s final decision. One also retained the relationship cue. Matching the peer again measures carryover with the prior decision still in context.

| Target | Panel condition | Shifted by round three | Cue kept | Cue removed | Difference |
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

Pooled rows count model-items and reuse the same cases across targets. The tables are descriptive. The family comparison also varies the named checkpoint, so differences may reflect the specific identities shown.

## Audit and source files

The logs include 1,600 linked explanations for later coding. The audit checked phase counts, served model tags, prompt differences, and parent trial links. Incomplete rows excluded: 0. Duplicate rows excluded: 0.

- [study2-relationship-full-llama3.1-8b-20261122.jsonl](../log/study2-relationship-full-llama3.1-8b-20261122.jsonl)
- [study2-relationship-full-llama3-8b-instruct-q4_K_M-20261122.jsonl](../log/study2-relationship-full-llama3-8b-instruct-q4_K_M-20261122.jsonl)
- [study2-relationship-full-qwen3.5-9b-20261122.jsonl](../log/study2-relationship-full-qwen3.5-9b-20261122.jsonl)
- [study2-relationship-full-qwen3-8b-20261122.jsonl](../log/study2-relationship-full-qwen3-8b-20261122.jsonl)
