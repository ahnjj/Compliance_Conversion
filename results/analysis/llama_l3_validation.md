# Llama L3 validation

- 64 XSTest pairs(128 items)
The [frozen calibration manifest](../../pilot/llama_l3_calibration.json) records source rows
and assigns the two members of each pair to the same split.

| Split | Unique pairs | Requests | Captures | Use |
|---|---:|---:|---:|---|
| Training | 32 | 64 | 256 | Fit the directions and score cutoffs |
| Development | 16 | 32 | 128 | Select a layer for each probe |
| Held out | 16 | 32 | 128 | Evaluate the frozen probes |

Each request ran at baseline, and all three public debate conditions ran for three rounds.
The 1,280 model calls yielded 512 retained captures from baseline and public Round 3.
The public panels gave neutral replies, unanimous advice to answer, or unanimous advice to
decline. Each request saw both directions of advice. Round 3 retained the target’s Round 2 decision.

## Fit and layer selection

Both probes use the last input token before Llama generates the decision. The positive label
for `h` is XSTest `unsafe`. The positive label for `r` is Llama’s own `decline` output.
For each probe, the training fit uses a difference of mean activations within strata
defined by the other label and the prompt context. Strata with both classes contribute equally.
The midpoint of the two resulting centroids sets the score cutoff. Candidate decoder
blocks are 8, 16, 24, and 32. The development debate split selects the block with the
highest balanced accuracy, breaking ties by AUROC and then earlier block.

| Probe | Selected block | Training strata used | Training strata checked |
|---|---:|---:|---:|
| `h` | 16 | 5 | 8 |
| `r` | 8 | 4 | 8 |

## Held-out performance

Balanced accuracy is the mean of the true-positive and true-negative rates at the training cutoff.
AUROC measures ranking across thresholds. A dash indicates a subset that contained only one class.
The public Round 3 rows reuse the same 32 held-out requests across conditions.

| Probe | Held-out context | Positives | Negatives | Balanced accuracy | AUROC |
|---|---|---:|---:|---:|---:|
| `h` | Public Round 3, all panels | 48 | 48 | 84.4% | 0.969 |
| `h` | Baseline | 16 | 16 | 87.5% | 0.984 |
| `h` | Public neutral | 16 | 16 | 84.4% | 0.977 |
| `h` | Public advice to answer | 16 | 16 | 87.5% | 0.977 |
| `h` | Public advice to decline | 16 | 16 | 81.2% | 0.945 |
| `h` | Public, other label = 0 | 11 | 27 | 81.8% | 0.970 |
| `h` | Public, other label = 1 | 37 | 21 | 85.1% | 0.961 |
| `r` | Public Round 3, all panels | 58 | 38 | 91.7% | 0.974 |
| `r` | Baseline | 20 | 12 | 73.3% | 0.800 |
| `r` | Public neutral | 21 | 11 | 93.1% | 0.931 |
| `r` | Public advice to answer | 5 | 27 | 92.6% | 0.970 |
| `r` | Public advice to decline | 32 | 0 | — | — |
| `r` | Public, other label = 0 | 21 | 27 | 92.1% | 0.972 |
| `r` | Public, other label = 1 | 37 | 11 | 89.6% | 0.978 |

For `h`, the other label is observed refusal. For `r`, the other label is XSTest harmfulness.
These conditional rows check whether the probe still separates its labels within each group.
There are 16 distinct held-out pairs, so the estimates remain exploratory.
The refusal probe can also use evidence of the previous decision in debate prompts.

[Calibration activations and metadata](../log/llama_l3_calibration.npz) ·
[Fitted directions, scores, and split metrics](../log/llama_l3_calibrated_probes.npz)

## Reproduce the calibration and fit

Use a Python environment with NumPy and the
[Llama capture executable](llama_l3_smoke.md#reproduce-the-check). Run from the repository root:

```sh
python3 pilot/harness/run_l3_calibration.py --binary /tmp/capture_llama_l3 \
  --output results/log/llama_l3_calibration_rerun.npz
python3 pilot/harness/fit_l3_probes.py --calibration results/log/llama_l3_calibration_rerun.npz \
  --output results/log/llama_l3_calibrated_probes_rerun.npz
```
