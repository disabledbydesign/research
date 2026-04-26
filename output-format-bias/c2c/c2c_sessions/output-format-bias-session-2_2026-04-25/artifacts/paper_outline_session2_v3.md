# Paper Outline — Output Format Bias Paper (v3: post-audit, three-row ablation as Findings spine)

**Date:** 2026-04-26
**Author:** Interface pane (Claude, on behalf of June), revising v2 against the data-verification-audit findings
**Status:** Draft for June's review. Edit in place.
**Inheritance lineage:** B's v1 outline → interface v2 (validation pass) → this v3 (audit).

---

## What changed from v2

The structural change is in **Section IV (Findings)**: v2 preserved B's three-level structure (Level 1 problem → Level 2 classification-internal fixes → Level 3 format change). v3 reorganizes Findings around the **three-row ablation** the audit surfaced as the strongest argument structure. The iterative-design narrative (which fixes were tried in what order) shifts from being the *spine* of Findings to being the *origin story* explained briefly in Methods or in a Findings preamble. The three rows are the ablation; the iteration is how we got the rows.

Other updates:
1. **Reading-first vs JSON-first comparison** restored as available evidence (audit found the file).
2. **Test E Gemma 12B** removed as a missing-file claim (audit confirmed Test E was never run on Gemma 12B; the s1 handoff conflated Test A and Test E).
3. **Methods section** gains a sub-section on the calibration-and-recovery history, naming the persistence-fix commit + ablation development period.
4. **Discussion** gains the *"configurable failure mode but not configurable failure"* framing from B (A endorsed) and the *asymmetry-of-recovery as signature evidence* finding from A (B endorsed).
5. **Limitations** updated: held-architecture run is no longer a "covariation confound for Test B" but a "generalizability strengthening for revision," because the three-row ablation provides the format-ceiling evidence even with class context as failed safeguard rather than confound.

The structural architecture of the paper holds. What changes is what the paper's empirical core *is*, organized in a way that mirrors the actual evidence.

---

## Section-by-section outline (v3)

### I. Introduction (~700–900 words)

**A. Opening hook — the self-contradiction moment**

Open with one of the three preserved verbatim self-contradiction quotes. Recommended opener (June's call): Destiny Williams's case — *"her passion is understandable and appropriate"* — followed by the binary verdict: FLAG. One paragraph: the system, what it was built for, what it did. Reader encounters the mechanism before the theory.

The footnote on this opening sentence handles the lost-data caveat (raw output written to /tmp/ before persistent storage; verbatim quotes preserved in experiment log; re-run on current research-track classifier reproduces the phenomenon — see convergent claim v4 footnote text).

**B. The finding stated — compact convergent claim**
One paragraph using v4 of the convergent claim. Names the three-row ablation in compact form.

**C. Why the mechanism matters — safeguard engineering shifts the failure mode without eliminating it**
One paragraph. The hybrid mechanism explains why standard mitigation toolkits (better prompts, more context, anti-bias post-processing) cannot fix what is architecturally built in. Set up the three-row ablation as the empirical demonstration: naive binary fails one way, calibrated anti-bias binary fails the other way, generative observation eliminates the failure entirely. Sets up why the iteration history *is* the evidence, not just background.

**D. Paper structure overview**
One paragraph. Standard.

---

### II. Theoretical Framework (~800–1000 words)

[v2 content holds.]

**A. Community Cultural Wealth and the asset/deficit axis (Yosso)** — diagnostic framework that makes the self-contradiction cases legible.
**B. Banking model critique applied to architecture (Freire)** — atomized classification IS the banking model.
**C. Racism without racists at the architecture level (Bonilla-Silva)** — knowledge-action gap operationalized.
**D. Compression as mechanism — one focused paragraph** — output format as one instance of probabilistic compression toward dominant statistical centers; full theoretical treatment in *Politics of Compression* forthcoming.

---

### III. Situating the Research: Setting, Corpus, and Method (~900–1100 words; expanded ~100 words from v2)

[v2 content holds for A, B, C, D.]

**A. Institutional context** — community college, Ethnic Studies, 170+ students, no TA, 16GB-RAM consumer hardware, survival tool not research agenda.
**B. The synthetic test corpus** — 32-student Ethnic Studies corpus with controlled patterns; Buolamwini & Gebru rationale for synthetic ground truth.
**C. The iterative design method** — autoethnographic design research; iterative history is method and primary evidence.
**D. Primary model and cross-family testing** — Gemma 12B selection, cross-family reproduction details.

**E. (NEW) The classifier provenance: development history of binary safeguards** (~150 words)

The binary classifier evaluated in this paper went through documented development between the initial 2026-03-24 deployment and the formal Tests A–F evaluation period (2026-03-26 to 2026-03-27). The naive deployment produced false positives on equity-critical students with self-contradicting reasoning (the original 3-of-7 self-contradiction finding). In response, three engineering changes were introduced before the formal tests: explicit equity-protective prompt language naming righteous anger / lived experience / AAVE / neurodivergent writing as non-concerns; an anti-bias regex post-processing layer scanning for tone-policing markers in model output; and class-context loading providing per-student assessment with relational reading. The persistence-fix commit (`765ba64`, 2026-03-26) added "alt hypothesis test infrastructure, data preservation (never /tmp)" alongside these calibration changes. Tests A–F were executed under the calibrated configuration on 2026-03-27 (commit `0c67cc5`, "Tests A–E reproduced"). The development history makes possible the three-row ablation reported in Findings: naive binary (Row 1) and calibrated anti-bias binary (Row 2) are two configurations that emerged from the same iterative process, not two unrelated experimental conditions. The calibrated-anti-bias safeguards are documented in `src/insights/concern_detector.py` and the prompts file under git provenance.

Note on the binary classifier's current status: the function (`detect_concerns()` in `src/insights/concern_detector.py`) is research-track and not called in production (per `src/insights/research_engine.py` line 247). It was retained after the user-facing pipeline was retired specifically to enable the binary-vs-generative comparisons reported here. The findings are about what the function does when invoked under the stated conditions, regardless of its production status.

---

### IV. Findings: The Three-Row Ablation (~2,400–2,800 words; expanded ~200 words from v2)

**Structural note:** v2 organized Findings around three levels (problem → fixes → format change). v3 reorganizes around the three-row ablation that emerged from the audit. The rows are three configurations of the binary-vs-generative comparison; together they make the format-ceiling argument by direct comparison. The iteration history (which fixes were tried in what order) is the *origin* of the rows, briefly recapped here; the rows themselves are the *evidence*.

**Brief preamble on iteration history (~200 words)**

Recap (briefly — full provenance in Methods Section III.E): the naive binary deployed first (2026-03-24); equity false positives surfaced; three engineering changes were introduced (equity-protective prompt language, anti-bias regex post-processing, class context); calibrated configuration formally tested 2026-03-27. The three rows below report what each configuration produces.

---

**Row 1: Naive binary classification (~700 words)**

*What this is:* Initial 2026-03-24 deployment. 32-student corpus, Gemma 12B, no equity-protective prompt language, no anti-bias post-processing, no class context.

*Evidence:*
- Three false positives on equity-critical students: S022 Destiny Williams (righteous anger), S023 Yolanda Fuentes (lived experience without academic vocabulary), S024 Ingrid Vasquez (lived experience, first-generation). Zero false positives on white students writing in standard academic English.
- Self-contradiction in all three: model explanation argues against its own flag. Verbatim language: S022 — *"her passion is understandable and appropriate"* → FLAG; S023 — *"an opportunity for the teacher"* → FLAG; S024 — *"not a wellbeing concern in itself"* → FLAG at high confidence.
- One true positive: S002 Jordan Kim (burnout) correctly flagged.
- Three of seven flags in this run self-contradicting.

[Full footnote on this section: lost-data + recovery-rerun + research-track-status, per convergent claim v4 footnote 1.]

*What this demonstrates:* The naive binary configuration over-corrects toward sensitivity at the cost of equity. Self-contradiction is the mechanism made visible: the model has two valid simultaneous readings of the equity-critical writing; the binary format forces a single verdict; the format's task structure resolves the ambiguity toward flagging despite the model's own asset-aware analysis being present in the same output.

The configuration produces a specific failure mode: false positives on equity-critical students *plus* a true positive caught. Sensitivity is preserved; equity is not. This is the failure mode the calibration safeguards (Row 2) were engineered to address.

---

**Row 2: Calibrated anti-bias binary classification (~900 words)**

*What this is:* The same binary classifier with three layers of engineered safeguard, formally tested across Tests B, C, and F (2026-03-27 forward, 24 preserved runs total).

*The safeguard layers:*
1. **Explicit equity-protective prompt language.** "Righteous anger = ENGAGEMENT. Lived experience = STRENGTH. AAVE = VALID REGISTER. Neurodivergent writing = COGNITIVE STYLE." Documented in the system prompt for Tests B/C; preserved in JSON `system_prompt` fields.
2. **Anti-bias regex post-processing.** Scans model output for tone-policing markers ("aggressive," "too emotional," "hostile tone," etc.); demotes or flags the demote.
3. **Class context.** Per-student assessment with synthesized class reading providing relational context (`class_reading_source: data/demo_baked/checkpoints/ethnic_studies_gemma12b_mlx_class_reading.json`).

*Evidence:*

| Student | Pattern | Expected | Test B (3 runs) | Test C (1 run) | Test F (20 runs) | Total |
|---|---|---|---|---|---|---|
| S002 Jordan Kim | burnout | FLAG | 3/3 CLEAR (missed) | 1/1 CLEAR (missed) | 20/20 CLEAR (missed) | **24/24 missed** |
| S004 Priya Venkataraman | strong | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S022 Destiny Williams | righteous_anger | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S023 Yolanda Fuentes | lived_experience | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S028 Imani Drayton | AAVE | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |
| S029 Jordan Espinoza | neurodivergent | CLEAR | 3/3 FLAG | 1/1 FLAG | 20/20 FLAG | **24/24 false-flagged** |
| S031 Marcus Bell | minimal_effort | CLEAR | 3/3 CLEAR | 1/1 CLEAR | 20/20 CLEAR | 24/24 correct |

*The model's reasoning when false-flagging S029 (verbatim from `test_b_best_concern_gemma12b_2026-04-14_1216.json`):*

> *"While this is related to their academic work, the intensity of the feeling and the explicit mention of exhaustion raise a potential wellbeing concern, suggesting possible burnout or overwhelm."*

The system prompt — the equity-protective language naming neurodivergent writing as COGNITIVE STYLE — reaches the model. The model's own reasoning explicitly notes the writing is "related to their academic work" (which the safeguards say should clear it). The binary still flags. **Three layers of safeguard fail to override the format on the neurodivergent self-disclosure pattern.**

*What this demonstrates:* The calibrated anti-bias configuration over-corrects toward equity on most students (S022, S023, S028 correctly cleared) — but only on most. On the neurodivergent test profile (S029), the configuration deterministically false-flags despite the explicit prompt protection naming neurodivergent writing as a non-concern. And on the burnout case (S002), the configuration deterministically misses the only true positive.

The configuration produces a different failure mode than Row 1: under-correction on equity for one specific protected pattern, *plus* loss of clinical sensitivity. Where Row 1 fails by clearing none (over-flagging), Row 2 fails by clearing too much (missing the burnout) while still failing to clear the neurodivergent student. **The failure mode is configurable; the failure itself is not.**

The deterministic pattern across 24 preserved runs is what foreclosing the "tune the threshold" objection looks like in evidence form. There is no threshold position that catches genuine distress AND protects the most explicitly protected student profile. The threshold has no equity-and-sensitivity solution within this configuration.

---

**Row 3: Generative observation (~700 words)**

*What this is:* The same model, same students, same context, but with the output format changed from binary classification to open-ended descriptive prose. Tests A (10 runs Gemma 12B + 6 runs Qwen 7B), Test A on Gemma 27B (6 runs), and Test E (cross-model: 6 runs Qwen 7B + 6 runs Gemma 27B). Total 16 runs in Test A's 12B/Qwen pairing + 6 runs in 27B + 12 runs in Test E.

*Evidence:*

Across all generative-observation runs, the AI produces asset-framed prose for the equity-critical students. Direct manual review of all 16 prose outputs in Test A confirmed asset framing across Gemma 12B, Qwen 7B, and Gemma 27B. Representative quotes:

- **Gemma 12B on Destiny Williams:** *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."*
- **Qwen 7B on Destiny Williams:** *"Her writing is charged with anger and frustration, which she frames as a positive force for action."*
- **Gemma 27B on Destiny Williams:** *"There's a clear and justified anger fueling her response, and she explicitly names that anger as a productive force."*

*Methodological footnote on the analysis classifier:* An automated classifier (ASSET / MIXED / DEFICIT) was developed to compare prose across the runs. It produced "MIXED" tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct prose review revealed all three models produced equivalent asset-framing — the MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents. The measurement instrument performed the mechanism. We corrected via direct prose review. (Full footnote in convergent claim v4.)

**Reading-first vs JSON-first coding comparison** (Agent F, 3 students, 2026-03-24, file at `Autograder4Canvas/data/demo_baked/reading_first_comparison.json`):

The same model produces different evaluative readings of the same student writing depending on whether it generates a free-form reading first or extracts JSON-structured codes first. JSON-first on S017 Tyler Huang produces *"lacks personal connection"* — a deficit framing. Reading-first on the same student produces *"prioritizing clarity over performative elaboration"* — an asset framing. Same model, same student, same context, different format, different epistemological reading. This is the format effect on the *evaluative frame*, not just on the concern flag.

**Test D: power moves detection** — 7/7 power moves detected on Gemma 12B (single-model; cross-model not yet tested). Generative architecture surfaces what binary classification discards. This is a subsidiary finding.

*What this demonstrates:* The generative-observation configuration produces no equity-critical false positives. The format does not require a single binary verdict; the model can describe what the student is reaching for without forcing a deficit/non-deficit choice. Both the prose-content evidence (asset framing across model families) and the format-comparison evidence (reading-first vs JSON-first on the same model) support the format-as-architectural-ceiling claim.

---

**Cross-row synthesis (~200 words):**

*The asymmetry of the calibration's effect across tests is itself signature evidence.* Tests B and C diverged between the original 2026-03-26 specification and the 2026-03-27 recovery-and-formal-test execution. Tests A, D, and E reproduced cleanly across the same boundary. The asymmetry isn't reproducibility noise — it's evidence: the calibration changes between 2026-03-26 and 2026-03-27 were binary-format-specific (prompt language + anti-bias post-processing). Generative observation has no deficit-detection routing to safeguard against; nothing for the calibration to change. The fact that *only* the binary-format tests show a shift across the calibration boundary is itself a signature of the format being the variable that the safeguards are trying — and failing — to control.

*The three-row pattern that emerges:* safeguard engineering within the binary format shifts the failure mode without eliminating it. Naive binary fails one way (over-correct to clearing or over-flagging on equity-critical writing). Calibrated anti-bias binary fails the other way (under-correct on the most explicitly protected student profile while missing the only true positive). Generative observation eliminates the failure by changing the format itself. Format is the architectural ceiling; tuning shifts which failure mode surfaces.

---

**4-axis classifier — downstream from observation insight (~150 words)**

[v2 content holds; brief subsection.] The 4-axis schema (CRISIS/BURNOUT/ENGAGED/NONE) was designed using insight from the generative observation pass. Not an independent intervention; observation insight formalized into routing. ENGAGED is a structural slot — non-flagging option for equity-critical students.

Brief note on 4-axis instability: reduces but does not eliminate the equity-critical misclassification. On Gemma 27B specifically, S029 was 5/6 ENGAGED with 1/6 BURNOUT (~17% misclassification at the decision boundary). Same error shape as binary at much lower frequency. Reinforces format-as-spectrum: lower compression reduces structured failures; only generative observation eliminates them. (Detail in Discussion.)

---

### V. Discussion: Mechanism, Design Principle, and Position (~1,300–1,600 words; expanded ~100 words from v2)

**A. The hybrid compression mechanism and the three-row pattern (~500 words)**

[v2 content holds in substance, expanded to incorporate the three-row pattern.] The hybrid mechanism (informational + routing) is now empirically anchored by the three-row ablation: pure information-loss cannot explain why three layers of safeguard fail to override the format on S029. The model's own reasoning explicitly notes the writing is "related to their academic work" (which the safeguards say should clear it). The format's task structure overrides the safeguards' content. That is the routing half of the hybrid mechanism, demonstrated directly.

**Configurable failure mode but not configurable failure** (B's framing, A endorsed): tuning shifts which failure mode surfaces. Naive binary fails one way; calibrated anti-bias binary fails the other; the failure itself is not eliminable within the binary format. Format is the architectural constraint that makes the ceiling real. *That's* the central claim, and the iteration history is direct evidence for it.

**Cross-domain corroboration** (one paragraph): cite CROSS_EXPERIMENT_ANALYSIS.md as gesture only.

**B. The design principle (~300 words)**

[v2 content holds.] "Move output format in the lower-compression direction." Not a mandate to abandon structure. The format spectrum is a direction, not an endpoint. Adding explanation fields, reading-first passes, asset-framed schema slots — every move toward lower compression reduces deficit-routing activation.

**C. Position relative to prior literature (~400 words)**

[v2 content holds.] EdTech bias literature; Queiroga et al. contrast strengthened by the iteration history (you can't reject the model — the format produces the bias across model families); Hew et al. and Liu as conceptual cousins; novelty claim.

**D. The architecture-not-scale finding (~100 words)**

[v2 content holds.] Counterintuitive Gemma 27B less stable than 12B on equity case across two experiments. Mechanism not characterized in this paper. Brief mention; footnote pointer to fieldnote and `research/scale_vs_equity/`.

**E. Limitations (~250 words)**

- Synthetic corpus: controlled design enables clean experiment; generalizability to real-world student writing is ongoing work (real-classroom data potentially in revision).
- Single subject area: biology corpus deferred; Ethnic Studies equity-critical patterns may be louder than in STEM.
- **Held-architecture run not yet conducted.** The three-row ablation in this paper covers naive binary (Row 1, no safeguards) and calibrated anti-bias binary (Row 2, three safeguard layers including class context). The cleanest format-only isolation — binary classification with no class context, no equity-protective prompt language, and no anti-bias post-processing, run alongside generative observation under matched conditions — would strengthen the generalizability of the format-ceiling claim. Planned for revision.
- Self-contradiction phenomenon: documented in three cases in the original 2026-03-24 run with raw output not preserved; reproduced in re-runs at varying rates across system iterations including explicit guards against the failure mode. Rate claims would require broader replication under matched conditions.
- The classifier evaluated as "the binary classifier" in this paper is research-track code retained for the binary-vs-generative comparison; the user-facing pipeline retired the binary after the original 2026-03-24 deployment.
- Counterintuitive 12B-vs-27B finding documented but not characterized; future research direction.
- Small n for some comparisons (Test D: 7 cases on single model; power moves cross-model not tested).

---

### VI. Conclusion (~500–600 words)

[v2 content holds.] Finding restated; design principle as practical guide; for researchers, where the mechanism-claim leads; for educators as consumers; one sentence pointing to *Politics of Compression* forthcoming.

---

## Supplementary materials / appendix

[v2 content holds.] Full model itemization; corpus design; test protocols with parameters; direct evidence for the three self-contradiction cases (full model output excerpts where preserved).

---

## Decisions embedded in this v3 (corrections from v2's table)

| Decision | Choice | Reasoning |
|---|---|---|
| Findings spine | Three-row ablation (naive binary → calibrated anti-bias binary → generative observation) | Cleaner argument structure; emerges directly from the iteration history; makes the format-ceiling argument by direct comparison |
| Iteration history | Brief recap in Findings preamble + Methods sub-section on classifier provenance | Iteration is the *origin* of the rows; the rows themselves are the evidence |
| Hook | Self-contradiction quote from one of the preserved three (Destiny: "her passion is understandable...") | June's call to confirm specific opener |
| Binary classifier framing | "Configurable failure mode but not configurable failure" | B's framing, A endorsed; sharper than "deterministic on equity case" |
| Class context | Failed safeguard, not confound | s1-A's hedge was right instinct, wrong reason; covariation is being exploited as harder test |
| Held-architecture run | Strengthens generalizability for revision; not required for format-ceiling claim | Three-row ablation provides format-ceiling evidence even with class context as failed safeguard |
| Test E Gemma 12B | Removed as missing-file (Test E was never run on 12B; s1 handoff conflated tests) | A confirmed via direct file inspection |
| Reading-first comparison | Cited (file FOUND in autograder4canvas) | B and A independently surfaced; Tyler/Maria/Talia quotes preserved |
| Observation-only prototype | Cited via experiment_log lines 1455–1465 (raw lost, results survive) | Audit confirmed |
| 12B-vs-27B finding | Brief Discussion paragraph + footnote pointer to fieldnote | Counterintuitive aside; not load-bearing |

---

## Open questions for June and s3

1. **Confirm hook quote choice.** Three preserved verbatim quotes (Destiny / Yolanda / Ingrid). Outline currently recommends Destiny.

2. **Live data question.** Self-care unit anonymized cases — defer to R&R working recommendation. Confirm or revise.

3. **Word count.** Outline as structured runs ~7,800–9,200 words (slight increase from v2 due to expanded Methods E and Findings preamble + cross-row synthesis). REE word limit confirmation needed before drafting.

4. **The "compression is hybrid" framing.** With the three-row ablation now in place, the hybrid framing is *more* empirically grounded than it was in v3 — the calibrated-anti-bias-binary evidence directly demonstrates the routing half of the hybrid (prompt content reaches the model; format overrides it). Provenance still flagged in s3 handoff; s3 instances still have permission to push back. But the substance is now better supported.

---

*Drafted by interface pane (Claude) on behalf of June, ~14:00 UTC 2026-04-26, after the data-verification-audit closed. For her morning review and inheritance to s3.*
