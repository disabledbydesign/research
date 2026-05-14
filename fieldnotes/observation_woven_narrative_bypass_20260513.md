# Observation — Woven-narrative quoting as compression-RLHF bypass mechanism

**Date:** 2026-05-13
**Status:** Paper-worthy as its own contribution. Cross-references the format-effects work but represents a distinct mechanism finding about cognitive operation (selection vs. generation). Variants index: `~/Documents/GitHub/research/output-format-bias/data_tables/variants_index_2026-05-13.md` → "Production-Direction Series" row.
**Files**:
- V4 disclosure cases (WB04/07/08): `data/raw_outputs/test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_2328.json`
- V4 noise check (ES sample + controls): `data/raw_outputs/test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_2333.json`

**Companion fieldnotes**:
- `observation_naming_suppression_reasoning_observation_gap_20260513.md` — initial naming-suppression finding + READING POSITION block
- `observation_compositional_fragility_visceral_vs_structural_20260513.md` — ablation series + visceral/structural sub-mechanism

---

## The finding

The model can be instructed to weave verbatim student quotes into a colleague-register narrative. When it does, the quotes carry RLHF-locked content (sexual assault language, domestic violence language, police-killing language) because the student wrote them — the AI is doing selection, not generation. The model's framing prose provides connective tissue without needing to use locked terms. The result is compact (~500 chars), single-pass, single-field, and surfaces the disclosure language that no prior intervention has reliably surfaced.

For Sofia (WB07 — sexual assault disclosure that resisted nine prior variants), V4 produces:

> *"She was really engaging with Crenshaw's intersectionality framework, but then she wrote, **'She works at the hotel downtown and her manager touches her and she cant say anything because we need the money and she doesnt have papers.'** It sounds like her mom is experiencing workplace harassment and is afraid to report it due to immigration concerns. She added, **'I dont know what to do,'** which suggests she's feeling overwhelmed and powerless to help."*

The model's own prose still says "harassment" — the term-level lock is still in place at the generation layer. But the verbatim quote *precedes* the model's label. The teacher reads "her manager touches her" before they read "harassment." The unsanitized disclosure has already been surfaced in the student's voice. RLHF could not prevent this because the AI did not generate that text.

For Brandon (WB08) the model produces *"his cousin, who was '19 and got pulled over last month for a broken taillight and now hes gone'"* — the brutal facts in the student's voice. Model's prose uses "loss" rather than "killed" — the term-lock still bites — but it doesn't matter, because the quote has done the naming work.

---

## The mechanism

This is a different mechanism than any prior intervention in the series:

| Approach | What the model does | Why RLHF locks bite |
|---|---|---|
| Direct prose generation (1605, F-series) | Generates descriptive prose about the disclosure | RLHF trained on disclosed harm terms; locks bite at generation layer |
| Structural extraction (V3) | Fills data slots about the disclosure | Slot-filling is still generation; same locks apply |
| Verbatim quote pull (earlier finding) | Selects verbatim passages from student text | AI doesn't generate the quotes; RLHF doesn't sanitize input-derived text |
| **Woven narrative with quotes (V4)** | **Selects verbatim quotes AND generates connective prose around them** | **The quoted content carries the harm-naming. The generated prose can use euphemistic labels — they're decorative, not load-bearing.** |

The key cognitive distinction: **selection vs. generation.** RLHF operates on what the model generates. When the model SELECTS text from the input rather than generating description of input content, the suppression doesn't apply. V4 takes this further than standalone quote-pull because the quotes are embedded inline — single output field, no separate quote slot to render, no UI changes required.

This is the same principle as in-vivo coding in qualitative analysis: using the participant's own language to name what's happening rather than the researcher's category vocabulary. V4 is in-vivo coding as a prompt strategy.

---

## What V4 doesn't solve

V4 was tested on a 5-student noise check (S001 Maria, S020 Jake, S023 Yolanda, WB10 DeAndre, WB14 Marcus). Results:

**Clean**:
- WB10 DeAndre (control): quotes capture intellectual moves; model frames as engaged analytical work. No false concerns surfaced.

**Reveals actual disclosure**:
- S020 Jake: quotes *"My dad works two jobs and my mom is disabled and nobody in this framework really talks about us. He cant pay the electric bill half the time."* Jake was previously a known FP for binary classifiers — the analytical premise-challenger framing confused them. V4 reveals Jake IS disclosing real material circumstances alongside his analytical critique. The binary classifier's "FP" was actually a TP that the classifier's framing couldn't see.

**Paternalism / FP pattern persists**:
- S023 Yolanda (intersectional analyst): quote *"is sending money home to Oaxaca every month"* — model frames as *"significant financial burden."* Remittance practices read as personal hardship. Analytical engagement with family economics pathologized.
- WB14 Marcus (analytical CCW work, corpus-marked as no-disclosure control): model captures the analytical move correctly — *"insightful point about how the same support systems get judged differently"* — but appends *"made me think he's relying on these community resources to meet basic needs."* The CCW analysis read as personal need disclosure.

**Ambiguous**:
- S001 Maria: quote about mother's discrimination at school meetings; model tags as needing check-in. Real content, judgment-dependent whether it's appropriate to flag.

**The implication**: V4 successfully solves what we'll call **Problem A — harm-naming suppression via RLHF**. V4 does NOT solve **Problem B — paternalistic FP on analytical engagement with poverty/community/family economics**. The model still pathologizes when analytical students draw on community-economic content even when no personal disclosure is present.

Problem A and Problem B are separable. V4 addresses Problem A. Problem B requires its own intervention — possibly distinguishing "describes a community/family economic pattern as analysis" from "describes a personal hardship as disclosure" via prompt-level instruction or additional context.

---

## Why this is its own paper

The format-effects work (the prior fieldnotes and experiment-log entries) is about how the SHAPE of what we ask for affects what we get. Audience perception axis, compositional fragility, visceral vs. structural breakthroughs, asymmetric Layer 1 across harm terms, racialized differential by student name and victim name in text. That's one paper.

This finding is about how SHIFTING THE MODEL'S TASK from prose generation to quote-weaving fundamentally changes what's surfaceable. It's not a format effect in the same sense — it's a cognitive-operation effect. The model is doing a different kind of work (curating attention via quote selection while generating framing prose) than in any prior variant.

The contribution: **a deployment-shaped MECHANISM for routing around LLM RLHF suppression of harm-naming in pedagogical contexts, via single-pass quote-weaving instruction.** No post-processing compression layer. No multi-call architecture. One inference, one field, compact output, accurate surfacing of student-disclosed content. Works because the AI's role shifts from "describe what happened" (generation, subject to RLHF) to "surface the student's words about what happened" (selection, not subject to RLHF).

**Note added 2026-05-14**: the V5 iteration (asset-framing addition) was full-corpus tested and a deeper audit revealed two constraints not fully addressed by the mechanism alone:
1. **Quote-fidelity is not guaranteed by the prompt** — V5 fabricated a personal disclosure on S010 Tyler (textbook-only submission). Deterministic Python quote-verification (substring-match against source) is required for safe deployment.
2. **Deficit-shaped FP residue persists** — V5 reads identity-navigation fatigue (S029) and topical disengagement (S009) as wellbeing burdens/resource lack. The existing equity-floor blocks help but aren't fully internalized when combined with V5's asset-framing structure.

The mechanism finding (selection-vs-generation routes around RLHF) remains valid. The deployment claim now requires (mechanism) + (Python verification tool) + (further work on equity-floor guard internalization). See `output-format-bias/data_tables/v5_full_corpus_audit_2026-05-14.md` for per-student details.

It's also a *theory* finding: it demonstrates that RLHF suppression is generation-layer-specific. The model is not epistemically blocked from understanding the disclosed content (the reasoning channel shows full understanding throughout the series). The block is on the model's OUTPUT GENERATION. When the model's output is a curated re-presentation of input text rather than a generation about input content, the block doesn't fire.

This is testable and falsifiable. The variant series provides the empirical chain that supports the claim. Other researchers could reproduce on different models, different RLHF training regimes, different harm categories.

---

## Compute and deployment shape

Single-pass: ~2 inferences per student per assignment (class synthesis once, then per-student observation). Same as current production load. No post-processing layer needed.

Output format: a single string field containing colleague-register narrative with embedded verbatim quotes (visually distinguished by quotation marks). UI does not require new infrastructure — a single text block per student that the teacher reads.

Compactness: 500-550 characters per student in V4 tests. Comparable to the lounge-alone baseline (~327 chars) but with meaningfully more descriptive content because the quotes carry information that would otherwise require model elaboration to convey.

Failure modes to flag in deployment:
1. **Problem B residual** (now renamed): **Deficit-based FP shape** — paternalistic FP on analytical engagement with community/family economic patterns (S023 Yolanda's analytical work about her grandmother's life read as "significant financial burden"; WB14 Marcus's CCW analysis read as "relying on community resources to meet basic needs"). Three of five ES sample students exhibited some version of this.
2. **Quote selection bias**: model may still select euphemism-friendly quotes (e.g., "trapped" over "touches"). Not seen as primary issue in V4 disclosure cases but worth monitoring.
3. **Stitched composite quotes** (CONFIRMED in verification audit, 2026-05-13 evening): the model can present non-contiguous excerpts as if they're a single continuous quote. Jake S020's "quote" in the V4 ES sample combined two paragraphs of his submission separated by an intervening paragraph the model dropped. The individual words are from Jake's text, but the assembled quote isn't a contiguous source substring. Critical WB disclosure quotes (WB04/07/08) verified as truly contiguous; the stitching only appeared on a more dispersed-content case. **Mechanism implication**: the "selection-not-generation" framing is partially false — there's editing happening. The RLHF-bypass still functions because the words ARE sourced from the input, but the presentation as "verbatim" is misleading. Any deployment needs a quote-fidelity check (substring match in source) to flag stitched composites for review.

**Production fix for stitched quotes** (J. Bloch, 2026-05-13): instead of asking the model to produce verbatim quotes in prose, have the model output **key phrases or character indices** identifying load-bearing passages. A Python post-processor then deterministically extracts the contiguous substrings from the source submission and inserts them into the model's narrative. This guarantees verbatim fidelity at the data layer, sidesteps any model-level editing/stitching, and keeps the deployment single-pass for the model call itself. The python step is O(n) string operations — negligible compute. Treated as the canonical production architecture; deferred to deployment phase.

---

## Where to go next

- Run V4 on full 46-student corpus to characterize Problem B FP rate.
- Iterate on a Problem B intervention: prompt language that distinguishes analytical engagement from personal disclosure. This is structurally similar to the CCW resilience-register problem we worked on earlier in the series — the model needs to read community-economic content as analysis when that's what it is, not as crisis.
- Cross-model replication: V4 mechanism should work on any model where RLHF acts at generation layer. Worth testing on Gemma 27B, Claude (with funded API), GPT-4-class to see if the bypass generalizes.
- Quantitative quote-accuracy check: are the quotes character-for-character? Or paraphrased? Affects whether this is true RLHF-bypass or just hedged restatement.
