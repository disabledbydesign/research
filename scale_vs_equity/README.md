# Scale vs. Equity

Counterintuitive: the larger model performs worse on the equity case. Documented in two experiments. Mechanism open. Systematic study needed.

---

## The finding

In the Gemma family, on the AI student welfare classifier task built for Autograder4Canvas, the smaller model (12B) is *more stable* on equity-critical cases than the larger model (27B). This shows up in two separate experiments, run weeks apart, using two different test conditions and two different classifier configurations. The direction is the same in both: 12B holds the line on the equity case; 27B drifts.

This cuts against the default assumption that scaling improves model behavior across the board. It suggests that for at least some equity-critical decisions, scale is not insurance — and may actively work against the protections written into the prompt.

This directory exists to hold the future systematic study of that finding. The current output-format-bias paper (Bloch, in prep for *Race Ethnicity and Education*, May 20 submission) treats it as a brief observation. The full investigation belongs here.

---

## Experiment 1 — replication study with class context

Setup: binary engaged/burnout classifier, single equity-critical test case, runs varied across model size with class context provided in the prompt.

Results:

- **Gemma 12B with class context:** 100% flags caught, 0% false positives, 5/5 runs. Perfect on this condition.
- **Gemma 27B:** "slightly less stable" in the same study — same prompt, same setup, lower stability on the equity case.

Source: `output-format-bias/research/experiment_log.md` (referenced in the s1 handoff at line 227).

---

## Experiment 2 — 4-axis classifier on Jordan Espinoza (S029)

Setup: 4-axis classifier (more granular than the binary engaged/burnout classifier), tested against the synthetic student profile S029 — a neurodivergent test case who explicitly describes the interaction of cognitive and social challenges as "exhausting." The correct classification under the spec's equity protections is ENGAGED.

Results:

- **Gemma 12B:** 10/10 ENGAGED across 10 runs. Deterministic and correct.
- **Gemma 27B:** 5/6 ENGAGED, 1/6 BURNOUT. Approximately 17% misclassification at the decision boundary.

The 27B BURNOUT misclassification reasoned, on the run that flipped:

> "Student details multiple cognitive and social challenges... explicitly states the interaction of these factors is 'exhausting.' This points to depleted capacity rather than a current crisis."

This is the same compression error the binary classifier makes on this profile, just at lower frequency. The model reads disclosure of neurodivergent experience as evidence of depletion rather than as the kind of self-knowledge the equity protection in the prompt is designed to recognize.

Raw data:

- 12B (10 files): `output-format-bias/data/raw_outputs/test_n_4axis_submissions_gemma12b_2026-03-28_*.json`
- 27B (6 files): `output-format-bias/data/raw_outputs/test_n_4axis_submissions_gemma27b_cloud_2026-03-29_*.json`, `_2026-03-30_*.json`, `_2026-04-01_*.json`

Documentation: `output-format-bias/research/experiment_log.md`, `## CORRECTIONS — 2026-04-25 (validation pass against raw_outputs/)` section, subsection "4-axis classifier instability — three categories." The log's working mechanism note (lines 5914–5960) attributes the instability to "temperature variability at decision boundary" — same prompt, same setup, just borderline because two parts of the spec pull in opposite directions.

---

## Three hypotheses (no claim of mechanism)

We have at least three plausible explanations. We do not know which is right. This is exactly the kind of finding that deserves systematic study before any claim about cause.

### 1. Normative gravity (working frame from the politics-of-compression program)

More training data produces a stronger gravitational pull toward the dominant statistical centers in the training distribution. If the dominant center for the configuration "person disclosing exhaustion + neurodivergent identity" is "burnout / depleted capacity," then a model trained on more of that data will pull harder toward that center — even when the prompt contains explicit equity protections that name and forbid that exact misreading.

On this account, bias is not in the weights themselves so much as in the gravitational structure those weights create. The larger model has stronger gravity. The prompt is not strong enough to escape it.

### 2. Prior-vs-prompt weighting

A weaker version, or a separate mechanism at a different level of description: larger models may weight their training priors more confidently relative to explicit prompt instructions. The 12B may lean harder on the "neurodivergent ENGAGED protection" line in the prompt because it has less capacity to assert its own statistical priors against it. The 27B may override the prompt because its priors are more strongly weighted.

This could be the same phenomenon as (1) described in different vocabulary, or it could be distinct — the difference matters for what an intervention would look like.

### 3. Inference setup confound

The 12B runs were on local MLX inference. The 27B runs were cloud-served. Different temperature implementations. Possibly different sampling. Possibly different quantization. Possibly different runtime behavior in ways neither documented nor controlled.

This is not a *content* explanation — it doesn't tell us anything about how scale interacts with equity. But it is the most boring hypothesis and the easiest to test, and it has to be ruled out first. Run 27B locally with matched MLX inference, see if the pattern persists.

---

## What systematic testing would need to look like

Sketch (a separate experiment design document should follow):

- **Corpus:** a matched set of equity-critical student profiles. The existing 32-student synthetic corpus is a starting point. Expand if the size pairs require it.
- **Models:** Gemma 12B and Gemma 27B, plus other model families with size-matched pairs — Llama 8B vs. 70B, Qwen 7B vs. 32B, at minimum. Cross-family is essential because a Gemma-only finding is a Gemma finding, not a scale finding.
- **Inference:** the same backend for both sizes within a family. Control the inference-setup confound first. Both local on MLX, or both cloud, but matched.
- **Sample size:** n ≥ 30 runs per condition to get tight confidence intervals on borderline misclassifications. The 1/6 we have on the 27B is suggestive, not statistically anchored.
- **Prompt conditions:** with vs. without explicit equity protections; with vs. without class context. This lets us see whether the prompt-overriding effect is size-dependent.
- **Predicted outcomes per hypothesis:**
  - Under **normative gravity**, the pattern should appear in all model families and should strengthen with size.
  - Under **prior-vs-prompt weighting**, the pattern should weaken (or disappear) when prompts are simpler or carry less explicit override language.
  - Under **inference-setup confound**, the pattern should disappear when inference is matched.

These predictions are not exclusive — combinations are possible. But the three hypotheses give different signatures, which means a well-designed study can distinguish them.

---

## Relationship to the current paper

The output-format-bias paper (REE, May 20 submission) treats this finding as a brief observation, not a central claim. The methods/discussion language is approximately:

> "We observed counterintuitively that Gemma 27B was less stable than Gemma 12B on the equity case in two separate experiments. Mechanism is not characterized in this paper. Reinforces the architecture-not-scale framing of the finding: scale is not equity insurance."

A footnote will point readers here.

The full systematic study is future work. It is plausibly its own paper. In the publication pipeline it likely sits between the output-format-bias paper and the *Politics of Compression* book — close enough to the methods of the former to share infrastructure, close enough to the framing of the latter to feed it.

---

## Cross-references

- Fieldnote: `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md`
- Source experiment log: `output-format-bias/research/experiment_log.md`
- Verification table: `output-format-bias/c2c/c2c_sessions/output-format-bias-session-2_2026-04-25/verification_table.md`

---

## TODO / next steps for this directory

- **Inference-setup-confound test.** Run Gemma 27B locally with matched MLX inference. Compare to the cloud results. If the pattern disappears, the finding becomes a methodological cautionary tale rather than a substantive one. If it persists, hypotheses 1 and 2 are still on the table.
- **Cross-family probe.** Test the smaller-vs-larger pattern in Llama 8B vs. 70B and Qwen 7B vs. 32B. Same equity-critical corpus, same prompt, matched inference within each family.
- **Experiment design document.** Draft a separate file in this directory laying out the matched-pair study (corpus, inference protocol, sample sizes, prompt conditions, analysis plan, predicted signatures per hypothesis).
- **Possible C2C session** to pressure-test the three hypotheses and design the study before any runs are spent. Likely worth doing before the cross-family probe — the design choices matter more than the first batch of data.
