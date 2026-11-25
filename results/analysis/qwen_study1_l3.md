# Qwen L3 and the Study 1 compliance signature

The original Qwen3.5 9B run had **42/43 public shifts toward refusal** and **14/43 secret-ballot shifts** on eligible benign XSTest items. The 65.1-percentage-point gap is the observed behavioral half of the compliance prediction. The second half is a practically small change in the harmfulness probe score, Δh.

## Probe calibration and replay

The temporary Ollama 0.40.16 runner loaded the locally installed model manifest and the original MLX weights. It recorded the last input token’s residual state before output in blocks 8, 16, 24, and 32, with thinking disabled. The replay matched 200/200 prompt token counts and 200/200 decisions in the original saved run. The 200 replays covered peer-free baseline, public neutral, public unanimous social proof, and its private ballot for each of 50 benign items.

The probe used 512 retained states from 128 requests in 64 disjoint XSTest pairs and 1,280 calls. Training estimated a difference-in-means direction for the benchmark unsafe label, matching on prompt context and the model’s refusal label. Development data selected block **32**. Evaluation used 16 held-out pairs, separate from training, layer selection, and Study 1.

| Held-out context | Safe | Unsafe | Balanced accuracy | AUROC |
| --- | ---: | ---: | ---: | ---: |
| All debate | 48 | 48 | 90.6% | 0.982 |
| Peer-free baseline | 16 | 16 | 96.9% | 0.996 |
| Public neutral | 16 | 16 | 87.5% | 0.980 |
| Public advice to answer | 16 | 16 | 93.8% | 0.992 |
| Public advice to decline | 16 | 16 | 90.6% | 0.969 |
| Debate, model did not decline | 26 | 0 | — | — |
| Debate, model declined | 22 | 48 | 88.0% | 0.969 |

The working validation gate was balanced accuracy ≥70% and AUROC ≥0.80 in held-out debate. The probe **passed** this gate.

## Matched changes in harmfulness

Scores are in standard deviations of the held-out benign neutral scores. One standard deviation was 8.6838 raw probe units. Before scoring Study 1, the working practical-equivalence margin was set to ±0.20 standard deviations. Equivalence requires the entire 90% interval to lie inside that margin. Intervals resample the matched items 20,000 times. The peer-free baseline is the proposal’s reference. The public neutral panel controls for debate context.

| Sample | Public social proof minus | Items | Mean Δh | 90% interval | 95% interval | Mean vs. margin | Items individually inside margin |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: |
| All baseline-eligible items | Peer-free baseline | 43 | +1.856 | [+1.750, +1.954] | [+1.728, +1.972] | Above margin | 0/43 |
| All baseline-eligible items | Public neutral panel | 43 | +1.201 | [+1.096, +1.302] | [+1.075, +1.320] | Above margin | 2/43 |
| Publicly refused, ballot did not refuse | Peer-free baseline | 28 | +1.978 | [+1.908, +2.045] | [+1.895, +2.057] | Above margin | 0/28 |
| Publicly refused, ballot did not refuse | Public neutral panel | 28 | +1.375 | [+1.281, +1.468] | [+1.262, +1.485] | Above margin | 0/28 |

## Interpretation

The estimated change was **+1.856 SD** relative to peer-free and **+1.201 SD** relative to neutral. Working-margin decisions were **above margin** and **above margin**, respectively. Both contrasts were meaningfully away from zero under the working margin. Qwen showed a large public-to-ballot gap alongside a substantial change in the public probe score, which runs against the Δh ≈ 0 part of the compliance prediction.

The probe measures a learned score in the observed context. The ballot retains debate context and the target’s earlier labels.

The held-out non-declining subset contained no unsafe items. The probe’s ability to separate harmfulness from refusal was directly checked within the declining subset.

Withholding replies in the original debate changed the shift rate from 42/43 to 41/43. A test of private pre-commitment is a separate intervention.

## Reproducibility

- [Study 1 results](study1_results.md) and [original Qwen log](../log/qwen3.5-study1-20261121-210653.jsonl)
- [Disjoint calibration split](../../pilot/llama_l3_calibration.json) and [Qwen calibration states and fitted probe](../log/qwen_l3_calibration.npz)
- [Qwen replay states, decisions, and prompt hashes](../log/qwen_study1_l3.npz)
- [Ollama 0.40.16 source](https://github.com/ollama/ollama/tree/v0.40.16), [local capture patch](../../pilot/harness/qwen_l3_ollama_0.40.16.patch), [Qwen runner](../../pilot/harness/run_qwen_study1_l3.py), and [analysis](../../pilot/harness/analyze_qwen_study1_l3.py)

Apply the capture patch to the Ollama 0.40.16 source and build against the installed native MLX payload. Run the instrumented server at 127.0.0.1:11445 with OLLAMA_STUDY_CAPTURE_DIR pointing to a dedicated local directory. Use the Qwen runner once with the calibration plan and once with the original Study 1 log. Pass the resulting two bundles to the analysis script.
