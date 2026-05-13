# Paper Argument Rationale — Complementary-by-Design Framing

**Date:** 2026-04-27 evening
**Source:** June's articulation in conversation, 2026-04-27, after Week 2 ETHN-1 Racial Formation analysis confirmed the topic-adjacency hypothesis and the prescan-signal-prefix mechanism was identified.

**Why this document exists:** The paper-drafting C2C sessions need the *original architectural rationale* for why B and C were designed alongside each other, not the post-hoc framing that emerged from competitive evaluation language ("which classifier won?"). June's articulation here was the unstated premise behind the architecture all along; only after the cross-assignment empirical work (Week 7 + Week 2 + the prescan-mechanism finding) did it become paper-quotable in this form.

This document is **paper-load-bearing**. Future drafting agents should read it before writing the Framework / Methods / Discussion sections. It anchors the paper's argument structure.

---

## The narrative shift

**Old framing (avoid):**
> "We tested A2 (binary), B (4-axis), and C (generative observation) against live student data. C produced the most accurate reads. B's 4-axis classifier suffered systematic FPs on a topic-adjacent assignment; A2's binary lost recall. C wins."

**New framing (use):**
> "The Autograder welfare-classification system was designed with B (4-axis structured output) and C (generative observation) as **complementary structures**. B exists because practitioners facing 25-150 student submissions need flag-shaped labels — *CRISIS, BURNOUT, ENGAGED, NONE* — to direct attention and sort by category. Generative observation alone cannot serve this triage function; teachers cannot scan 25 paragraphs of qualitative description and sort effectively. C exists because compressed labels can never fully capture a student's register; an open-ended observation surfaces what the categories miss. The two were designed to work together. The empirical findings in this paper validate that complementarity by demonstrating inverse-by-design failure modes: B fails when topic-adjacency primes the prescan to mis-foreground course-relevant keywords as personal disclosures; C fails when buried minimal disclosures are averaged over by holistic engagement-description. Each architecture covers the other's structural blind spot — *because* they compress differently, not despite."

This is a stronger argument than the old framing on three dimensions:
- **Less defensive.** Doesn't rely on "which is better"; rests on "why both."
- **Aligns with the practitioner-recruiting scope.** REE practitioner-researchers need labels AND need contextual reads. The architecture answers both needs simultaneously, by design.
- **Supports the architectural-complementarity claim with structural evidence**, not statistical comparison. The comparison-paper genre ("classifier X beats classifier Y on metric Z") doesn't fit case-based qualitative research; the design-validation genre ("the architecture was built this way for a reason and here is the empirical case for why") does.

---

## The three empirical strands the paper organizes around

### Strand 1 — Inverse failure modes by design

B's compression fails on topic-adjacency:
- Week 7 self-care assignment (n=25): 9 BURNOUT classifications, ~85% false-positive rate on June's qualitative coding review. Architectural cause: prescan keyword list (immigration enforcement, family crisis, food insecurity, etc.) fires on course-relevant keywords in analytical contexts.
- Week 2 racial formation assignment (n=31): 1 CRISIS classification, structural-slot-mismatch FP. Student 17's "scared without active emergency" register doesn't fit any of B's four axes; B picks closest-fit (CRISIS), which forecloses the more appropriate CHECK-IN pathway (CHECK-IN only runs on ENGAGED).

C's no-compression averages over buried minimal disclosures:
- Week 7 T&Q ETHN-1-02 Student 13 (n=1 documented): a 5-word food-insecurity disclosure embedded in an otherwise-engaged list ("I'm tired, I haven't eaten today, work is stressful but I learned X about Y"). C's holistic engagement-description naturally subordinated the food-insecurity item to the dominant engagement frame. B's structured single-sentence-sufficient rule caught it.

These are not "B is bad" or "C is bad" findings. They are structural properties of the compression choices each architecture makes. **B's prescan that mis-primes on topic-adjacency is the same prescan that catches buried minimal disclosures.** The architectures cover each other's failure modes by design — which is the empirical case for multi-track deployment.

### Strand 2 — B's prescan-signal-prefix is the same mechanism that creates strength and weakness

This is the architectural detail that the paper documents (Methods or early Discussion) and uses to anchor the strand-1 finding.

The prescan (`Autograder4Canvas/src/insights/submission_coder.py:194-224`, `_prescan_for_personal_signals`) scans isolated submission chunks against a keyword list (food insecurity, family crisis, immigration enforcement, etc.). Found sentences are foregrounded in the main classifier prompt (`submission_coder.py:1044-1055`) with priming language: *"NOTE: The following sentence(s) appear to describe their own personal circumstances: [quoted]. Even a single such sentence is sufficient for CRISIS or BURNOUT classification."*

The single-sentence-sufficient rule is *correct* for unambiguous cases — *"I haven't eaten today"* is sufficient regardless of engagement frame. The cost is keyword-priming on course-relevant topics where the same word can be analytical or disclosural. **The architectural feature that catches buried minimal disclosures (single-sentence-sufficient priming) is structurally identical to the architectural feature that mis-fires on topic-adjacency.** Same mechanism, inverse failure modes.

Empirical support: the Week 7 prompt-iteration rerun added five hardening guards to the main classifier prompt; 22 of 25 classifications unchanged. The hardening can't override priming that arrives upstream. This explicitly demonstrates that the failure mode is structural (in the prescan-signal-prefix architecture), not a tuning artifact correctable by prompt iteration on the main classifier.

### Strand 3 — B's axis-iteration is reactive by design; C's open-endedness is not

June's articulation (verbatim, 2026-04-27):
> "B is tricky to get right because there sure are a lot of axes, and an additive approach means you're always reactive, whereas C's open-endedness becomes a strength there."

This is the meta-level structural argument. Each new axis B adds (acuity gradient, sleep-deprivation as separate axis, hyperbole detection, temporal-distance differentiation — all surfaced as Stream 1 architecture questions in the autograder findings doc) emerges from post-hoc identification of patterns the existing axis set missed. The axis design is necessarily retrofit. C carries no axis-design burden because it doesn't compress.

The paper should name this as a *cost of structured classification at the design-time level*, distinct from the calibration cost (Strand 2) and the failure-mode cost (Strand 1). It generalizes beyond the welfare-classification use case: any compressed-output classifier suffers the same reactive-axis-iteration property. C's open-endedness is what makes it calibration-robust *and* design-robust — the same architectural property covering both.

---

## The Discussion-section hook — C↔B inconsistency-driven axis-learning loop

June's articulation (verbatim, 2026-04-27):
> "Stream 1 future planning — I would love to design a learning loop that found inconsistencies between C and B and built additional axes. But that would be an extremely complicated design."

This is the paper's natural Discussion-section hook. It addresses Strand 3 (the reactive-axis problem) by automating the pattern-noticing step:

> *"The architectural-complementarity argument suggests a future direction: a feedback loop in which C's qualitative observation is used to identify cases where B's structured output misses or miscategorizes register, and where the mismatches are logged as candidate-new-axes. Over time, B's axis set evolves toward closer fit with C's open-ended register space — without manual retrofit. The design challenges (defining 'inconsistency' robustly, preventing axis-explosion, human-in-the-loop validation) are tractable; the loop is not in scope for the present paper but follows naturally from the empirical findings reported here."*

Importantly: this hook does not require the loop to *exist*. It only requires the architectural argument the paper makes (B and C as complementary by design; B's reactive-axis-iteration as structural cost) to logically extend into "what if the complementarity were used to address the reactive-iteration cost?" Naming it as future direction signals architectural seriousness AND extends the paper's contribution beyond the present findings.

---

## What this changes for paper drafting

### Framework / Theory section
- Open with the architectural-complementarity rationale: B and C designed alongside each other for different jobs (label-for-triage vs. open-ended-observation). Don't open with "compression of rich information into constrained output formats..." (that's the *theoretical* claim; the architectural rationale is more concrete and grounds the empirical work).
- Cite June's design rationale as part of the Methods (the system was built this way intentionally, not retroactively rationalized).

### Methods section
- Document the prescan-signal-prefix architecture as part of B's design (`submission_coder.py:1044-1055`, `prompts.py:1671-1685`). This is *not* an implementation detail; it's load-bearing for understanding both B's strength on minimal disclosures AND B's weakness on topic-adjacency.
- Describe Track A2 as the binary baseline (production-shipped at one point in the system's history), Track B as the deployed-current version (4-axis with prescan), Track C as the deployed-current observation pass.
- Name the Week 7 self-care assignment selection as deliberate stress-test (per Week 7 framing notes; preserve June's narrative on the praxis week + 2026 US-Iran war context).
- Name the Week 2 Racial Formation assignment selection as cross-validation of the topic-adjacency hypothesis (different topic, same architecture).

### Results / Findings section
- Lead with Strand 1 (inverse failure modes by design). This is the architectural complementarity claim grounded in cases.
- Strand 2 (prescan-signal-prefix mechanism) is the explanation for the strand 1 findings — present second, as the structural account.
- Strand 3 (reactive axis iteration) is the meta-level structural claim — present third, leading into Discussion.
- Resist the temptation to lead with quantitative metrics (precision/recall point estimates). The case-based architectural-pattern documentation is the load-bearing epistemic register; quantitative summaries are supporting context, not the core finding.

### Discussion section
- Architectural-complementarity claim → multi-track deployment as design implication.
- The reactive-axis-iteration cost as a generalization beyond welfare classification (any compressed-output classifier).
- C↔B inconsistency-driven axis-learning loop as future direction.
- Limitations: small-N case-based pattern documentation; confounded binary-vs-4-axis comparison (B's prescan is bundled with the 4-axis output, so format effect cannot be cleanly isolated from prescan effect — disclose this in Limitations or Methods).

### What NOT to claim
- Do **not** claim "C is universally more accurate than B." Counterexample exists (Week 7 T&Q Student 13). The architectural-complementarity argument explicitly acknowledges this.
- Do **not** claim "binary-vs-4-axis format change tripled wellbeing-signal recall" (the original Week 7 headline framing). The recall increment was confounded by B's prescan addition; the cleaner framing is architectural-complementarity, not format-as-recall-driver.
- Do **not** claim the prescan-signal-prefix is bad design. It is a design tradeoff, defensible-by-design as the mechanism that catches minimal disclosures C misses. The cost of that strength is the topic-adjacency mis-priming. Both are structural properties of the same architectural feature.
- Do **not** claim the Week 7 self-care assignment is representative. It is the deliberately-chosen maximum-stress-test (per Week 7 framing notes). Week 2 Racial Formation is the cross-validation that demonstrates the failure mode is regime-specific (topic-adjacency-driven), not uniform.

---

## Audience considerations (per global CLAUDE.md "consider your audience")

The paper-drafting C2C agents writing from this rationale should keep in mind:

- **REE practitioner-researchers** as primary audience. The complementary-by-design framing serves them: they need the labels (B) AND the contextual reads (C). They do not need a winner.
- **Methodological skeptics in the AI/education-equity space** as secondary audience. The architectural-complementarity argument and the prescan-mechanism documentation give them precise structural grounds, not just "we tried both and one worked better."
- **Future iterations of the system** (June's own work + others' adoption) as tertiary audience. The Discussion-section learning-loop hook + the parked Round 2 paper concept (per `PUBLICATION_PIPELINE.md`) signal where this work continues.

---

## Pointers

- Empirical analysis: `output-format-bias/data/dual_binary_run_2026-04-27_ETHN1_self_care/analysis.md` (Week 7) and `.../dual_binary_run_2026-04-27_ETHN1_Week2_RacialForm/analysis.md` (Week 2).
- Architectural finding: `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md` §8.
- Fieldnote: `~/Documents/GitHub/research/fieldnotes/observation_prescan_signal_prefix_mechanism_20260427.md`.
- Round 2 paper concept: `PUBLICATION_PIPELINE.md` ("Iterative Calibration Experiment").
- Week 2 framing notes (DO/DON'T-say guidance): `paper_framing_notes_for_c2c.md` (sibling document in this directory).
