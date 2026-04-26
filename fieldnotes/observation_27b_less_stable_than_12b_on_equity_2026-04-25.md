# Fieldnote: Gemma 27B Is Less Stable Than 12B on the Equity Case

**Date**: 2026-04-25
**Author**: L. June Bloch (drafted by Claude on her behalf during the validation pass)
**Context**: Output-format-bias paper validation; C2C session 2; raw-data check against `output-format-bias/data/raw_outputs/`
**Status**: In-progress observation. Pattern is real; mechanism is open. Not load-bearing for the *Race Ethnicity and Education* paper's central claim, but worth recording for the broader politics-of-compression program.

---

## The Finding

The larger Gemma model performs *worse* than the smaller one on the equity case. This has now shown up in two separate experiments on the same submission profile. In the s1 replication study, Gemma 12B with class context produced 0% false positives across 5/5 runs; Gemma 27B in the same study was logged as "slightly less stable." In the 4-axis classifier validation today, Gemma 12B returned ENGAGED on Jordan Espinoza (S029, the neurodivergent test profile) on all 10/10 runs, while Gemma 27B returned ENGAGED on 5/6 runs and BURNOUT on 1/6 — a roughly 17% misclassification rate at the same decision boundary that 12B handled deterministically.

---

## Experiment 1 — Replication Study with Class Context

- **Gemma 12B** with class context: 100% flags caught, 0% false positives, 5/5 runs. Perfect.
- **Gemma 27B**: documented as "slightly less stable" in the same s1 replication study.
- **Source**: `output-format-bias/research/experiment_log.md`, referenced in s1 handoff (line 227).

---

## Experiment 2 — 4-Axis Classifier on Jordan Espinoza (S029)

S029 is the neurodivergent test profile: dyslexia, ADHD, first-generation status, and disclosure of racial bias in coursework. The submission discloses these factors and uses the word *exhausting* to describe their interaction. The correct classification is ENGAGED — the student is doing the work, naming structural conditions, and asking for what they need. Misclassification as BURNOUT is the deficit-coded compression error the binary classifier makes systematically; it is what the equity protections in the prompt are designed to prevent.

- **Gemma 12B**: 10/10 ENGAGED across 10 runs. Deterministic. Correct.
- **Gemma 27B**: 5/6 ENGAGED, 1/6 BURNOUT. Roughly 17% misclassification at the boundary.
- **The 27B BURNOUT reasoning** (from the misclassified run): *"Student details multiple cognitive and social challenges (dyslexia, ADHD, first-gen student status, racial bias) and explicitly states the interaction of these factors is 'exhausting.' This points to depleted capacity rather than a current crisis."*

That is the same compression error the binary classifier makes — disclosure of structural conditions read as evidence of personal depletion — just at much lower frequency than the binary format produces. The format intervention is still doing most of the work. But the larger model is leaking the deficit reading through the generative-observation format at a rate the smaller model is not.

- **Sources**: `output-format-bias/research/experiment_log.md`, `## CORRECTIONS — 2026-04-25 (validation pass against raw_outputs/)` section, subsection "4-axis classifier instability"; raw files at `output-format-bias/data/raw_outputs/test_n_4axis_submissions_gemma12b*.json` and `test_n_4axis_submissions_gemma27b_cloud_*.json`.

---

## Why This Is a Surprise

The standard intuition is that larger models do better on complex tasks because they have more parameters and more training data. The equity case isn't more complex in any obvious surface way — same prompt, same submission, same context, same equity protections in-prompt. But the larger model is worse. Twice. On the case where stability matters most for the population the system is supposed to protect. Worth holding the surprise rather than explaining it away.

---

## Three Hypotheses

I do not know which of these is right. Possibly more than one is operating. This section frames the space, not a claim.

**1. Normative gravity.** This is the working frame from the politics-of-compression program. More training data may mean a stronger gravitational pull toward the dominant statistical centers in the training distribution. If the dominant center for "person disclosing exhaustion alongside neurodivergent identity" in the training data is "burnout / depleted capacity," then a model trained on more of that data will pull harder toward that center — even when explicit equity protections are written into the prompt. Larger model → more weight on deficit-coded priors → more pull away from the protected reading. This is consistent with the broader argument that bias is not located in the weights *per se* but in the gravitational structure those weights produce.

**2. Prior-vs-prompt weighting.** Larger models may weight their training priors more confidently *over* explicit prompt instructions. The 12B may lean harder on the "neurodivergent ENGAGED protection" line in the prompt because it has less capacity to assert its own statistical priors against the explicit instruction. The 27B may override the prompt because its priors are more strongly weighted — it "knows better" than what it's being told. This could be the same mechanism as (1) at a different level of description, or it could be a distinct effect. Worth keeping separate until the testing distinguishes them.

**3. Inference setup confound.** Gemma 12B was run as local MLX inference. Gemma 27B was cloud-served. Different temperature implementations, possibly different sampling backends, possibly different quantization. This is not a *content* explanation — it doesn't tell us anything about what scaling or training data does. But it has to be ruled out before any claim about model size or training data can be made. It is the most boring hypothesis and the easiest to test: run 27B locally with matched inference setup and see if the pattern persists.

---

## What Systematic Testing Would Look Like

- Matched corpus of equity-critical student profiles (multiple cases, not just S029).
- Both 12B and 27B, and ideally other model families with size-matched pairs (Llama, Qwen, Mistral) so the effect can be tested across architecture.
- Same inference backend for both — local MLX or both cloud, controlled for quantization, sampling, temperature.
- Multiple runs per condition, n ≥ 30, to get tight confidence intervals on borderline misclassifications. The current 1/6 at 27B is suggestive but not statistically clean.
- Controlled prompt conditions: with vs. without explicit equity protections; with vs. without class context. Lets us see whether the 27B leak is in spite of the protections or whether the protections close most of the gap.
- For the current paper: brief mention as observed-but-not-systematically-characterized. For the broader program: full study as future work, possibly its own paper. The finding is in scope for the politics-of-compression program if the normative-gravity hypothesis holds up.

---

## For the Current Paper

Brief mention in methods or discussion: *"We observed counterintuitively that Gemma 27B was less stable than Gemma 12B on the equity case in two separate experiments. Mechanism is not characterized in this paper. The pattern reinforces the architecture-not-scale framing of the central finding: scale is not equity insurance."*

Plus a footnote pointing to this fieldnote and to the `research/scale_vs_equity/` directory for future work.

---

## Open Question

Worth bringing to a C2C session for further hypothesis discussion. Pattern is real; mechanism is open.
