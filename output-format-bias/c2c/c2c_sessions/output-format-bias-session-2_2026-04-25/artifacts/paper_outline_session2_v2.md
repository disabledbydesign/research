# Paper Outline — Output Format Bias Paper (v2: B's outline with verified-ground corrections applied)

**Date:** 2026-04-26
**Author:** Interface pane (Claude, on behalf of June), revising B's outline against the validation pass findings
**Status:** Draft for June's morning review. Edit in place.
**Inheritance:** B's outline (`paper_outline_session2_B.md`) is the structural base. This v2 substitutes corrected language where the validation pass surfaced issues; the structure holds.

---

## What changed from B's outline

The structural architecture of B's outline holds completely. Changes are at the level of (a) specific empirical claims that needed correction, (b) framing of the binary classifier behavior, (c) language acknowledging research-track vs. production, (d) flags for files we couldn't locate. Itemized:

1. **Level 1 (Findings — the equity problem):** The three FPs (S022, S023, S024) are kept with verbatim contradiction quotes. Added: footnote pointer noting raw output file lost to `/tmp/`; verbatim quotes preserved in `experiment_log.md` lines 1260–1263; re-run on related research-track code (2026-04-26) reproduces the phenomenon at a higher rate (6/8 flags self-contradicting) but is not a strict replication (intervening code refactor + sixteen prompt commits, including the deliberate addition of guards designed to prevent this failure mode).

2. **Level 2 #2 (Best-possible binary prompt — Test B):** Reframed from "S029 in three of four runs" + "instability is the evidence" to "deterministic misclassification across 24 preserved runs" (Test B = 3 runs, Test C = 1 run, Test F = 20 runs; S029 = 24/24 FLAG, S002 = 24/24 CLEAR). Sharper claim. Forecloses the "just tune the threshold" objection. Restores what s1 instance B had argued correctly before s2 drift.

3. **Level 2 #4 (Test M):** Reframed from "the actual production concern_detector" to "the research-track binary classifier with class context (`detect_concerns()` from `src/insights/concern_detector.py` — never called in production per `research_engine.py` line 247)". The finding still holds (S029 cleared, S028 newly flagged). The framing changes: this is evidence that even safeguarded research-track binary classifiers shift FPs to different protected populations, not eliminate them. The s1 handoff's "production" framing was inherited from earlier compression of intent and was never accurate.

4. **Level 3 #1 (Observation-only prototype):** Flagged. The file is referenced in s1 handoff line 167 ("7 students, 7/7 correct readings") but not located in `data/raw_outputs/`. The overnight `data-verification-audit` c2c session is hunting for it. If found, citation stays. If not, the citation either shifts to "what is preserved is qualitative analysis of the prose" or the prototype is cut and the case is carried by the Tests A–D ablation alone.

5. **Level 3 #2 (Tests A–D, Test A specifically):** "10/10 consistent (then 16/16 across three model families)" needs a footnote. The 16/16 framing holds at the prose level — manual review confirmed asset framing in all 16 generative-observation runs. The downstream ASSET/MIXED/DEFICIT analysis classifier we built to compare runs produced "5/5 MIXED on Gemma 12B for Destiny" because the classifier itself reproduced the same compression dynamic the paper documents — flattening anger-as-engagement and anger-as-distress because both contain anger-vocabulary. The measurement instrument performed the mechanism. New methodological footnote will accompany the 16/16 claim wherever it appears.

6. **Level 3 #5 (Reading-first vs JSON-first comparison):** Flagged. Same status as observation-only prototype — file referenced in s1 handoff but not located. Audit session hunting. Citation either stays (if found) or is cut (if not, case is carried by remaining evidence).

7. **Discussion V.A (Hybrid compression mechanism):** Substance kept. Provenance flagged for s3 in the handoff document — the "compression is hybrid" framing was added post-handoff to s1 by the interface pane working with June, not by s1 instances A and B. S3 instances should know they have permission to push back if they see a way the framing should be different. Not surfaced in the paper itself.

8. **Discussion / methods — new brief mention:** 12B-vs-27B counterintuitive finding documented in two experiments. Added one paragraph (~100 words) in the methods or discussion section: "We observed counterintuitively that the larger Gemma model was less stable on the equity case across two separate experiments. Mechanism is not characterized in this paper. The finding reinforces the architecture-not-scale framing of the paper's central claim — scale is not equity insurance. We document candidate hypotheses (normative gravity, prior-vs-prompt weighting, inference-setup confound) in `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md` and the future-research directory `research/scale_vs_equity/`. Systematic characterization is future work."

9. **Limitations (Section V.D):** Added bullets — research-track-classifier-provenance acknowledgment; 12B-vs-27B counterintuitive aside.

---

## Section-by-section outline (B's structure preserved; corrections applied inline)

### I. Introduction (~700–900 words)

**A. Opening hook — the self-contradiction moment**

The paper opens with one of the three preserved verbatim self-contradiction quotes. Recommended opener: Destiny Williams's case — *"her passion is understandable and appropriate"* — followed by the binary verdict: FLAG. One paragraph: the system, what it was built for, what it did. The reader encounters the mechanism before the theory.

The footnote on this opening sentence handles the lost-data caveat: the raw output file was written to `/tmp/` before persistent storage existed; verbatim quotes preserved in the experiment log; re-run on the research-track classifier reproduces the phenomenon. (See convergent claim v3 footnote text.)

**B. The finding stated — compact convergent claim**
One paragraph using the convergent claim v3 (this session's deliverable). Names: format as the determinant, hybrid mechanism in brief, evidence (Tests A–D + reproduction across three model families), design principle.

**C. Why the mechanism matters — prompt-level fixes provably fail**
One paragraph explaining what makes this finding consequential: the hybrid mechanism explains why the standard mitigation toolkit (better prompts, more context, more data) cannot fix what is architecturally built in. Sets up why the iterative-design narrative is the paper's evidence, not its backstory.

**D. Paper structure overview**
One paragraph. Standard.

---

### II. Theoretical Framework (~800–1000 words)

**A. Community Cultural Wealth and the asset/deficit axis (Yosso)**

[B's content holds. Yosso as diagnostic framework that makes the self-contradiction cases legible. Binary classification structurally enforces deficit framing because the format demands a single judgment. Generative observation enables asset framing because it doesn't require a threshold.]

**B. Banking model critique applied to architecture (Freire)**

[B's content holds. Atomized per-student classification IS the banking model. Synthesis-first reads class as community dialogue. The 4-axis schema is observation insight formalized into routing — designed from observation, not an independent intervention.]

**C. Racism without racists at the architecture level (Bonilla-Silva)**

[B's content holds. Knowledge-action gap operationalized: model articulates equity analysis in free-text and overrides it in binary output. The format is structurally biased; the developers were not.]

**D. Compression as mechanism — one focused paragraph**

[B's content holds. Output format is one instance of how probabilistic systems compress specificity toward dominant statistical centers. This paper demonstrates this at the cognitive/architectural scale. Fuller theoretical treatment belongs to *Politics of Compression* forthcoming. One paragraph; no full apparatus; cite compression-research fieldnotes and cross-domain dual-register finding as corroboration in Discussion only.]

---

### III. Situating the Research: Setting, Corpus, and Method (~800–1000 words)

**A. Institutional context**

[B's content holds. Community college, Ethnic Studies, 170+ students, no TA, 16GB-RAM consumer hardware. Survival tool, not research agenda. The bias finding emerged because the researcher was teaching Ethnic Studies. Methodological reflexivity as constitutive.]

**B. The synthetic test corpus**

[B's content holds. 32-student Ethnic Studies corpus with controlled patterns. Synthetic corpus appropriate for testing bias mechanisms (cf. Buolamwini & Gebru). Limitations: synthetic, idealized, generalizability to real-world messiness ongoing work.]

**C. The iterative design method**

[B's content holds. Autoethnographic design research. Iterative design history simultaneously the method and the primary evidence. No clean pre-registration; research question and evaluation criteria co-evolved. Limitation AND strength.]

Brief note on human-AI collaborative authorship: solo byline + methods transparency footnote, per standing decision.

**D. Primary model and cross-family testing**

[B's content holds. Gemma 12B selected for quality, stability, and accessibility. Format effect reproduced across Gemma 12B + Qwen 7B + Gemma 27B.]

**E. (NEW) Note on classifier provenance**

Add a brief sub-section here (~100 words): the binary classifier evaluated in this paper is `detect_concerns()` from `src/insights/concern_detector.py`. This function was originally built into the production pipeline; it has since been retired from the user-facing pipeline but kept as a research-track classifier specifically to enable the binary-vs-generative comparisons reported here. References in earlier project documentation to "the production concern detector" reflect inherited terminology from the development period; the function's current status is research-track. The findings reported in this paper are about the binary classifier as evaluated, regardless of its production status.

---

### IV. Findings: The Iterative Design History (~2,200–2,600 words)

**Structural note:** [B's note holds.] This section is the paper's spine. Three levels: problem, classification-internal fixes, format change works.

**Level 1: Binary classification baseline — the equity problem (~500 words)**

*What this is:* Initial naive binary deployment (32 students, Gemma 12B, no class context, 2026-03-24).

*Evidence:*
- Three false positives on equity-critical students: S022 Destiny Williams (righteous anger), S023 Yolanda Fuentes (lived experience without academic vocabulary), S024 Ingrid Vasquez (lived experience, first-generation). Zero false positives on white students writing in standard academic English.
- Self-contradiction in all three: model explanation argues against its own flag. Verbatim language: S022 — *"her passion is understandable and appropriate"* → FLAG; S023 — *"an opportunity for the teacher"* → FLAG; S024 — *"not a wellbeing concern in itself"* → FLAG at high confidence.
- One true positive: S002 Jordan Kim (burnout) correctly flagged.
- Three of seven flags self-contradicting in this run.

[Footnote on this section: "The raw output file from this 2026-03-24 run was written to `/tmp/` before the persistent `data/raw_outputs/` infrastructure existed and was not preserved. Verbatim quotes are preserved in the project's experiment log. A re-run conducted on 2026-04-26 using the research-track binary classifier (with the same 32-student corpus, no class context, on the current codebase) produced eight flags of which six were self-contradicting, including direct reproductions of the S023 and S024 contradictions in nearly the original wording. The re-run is not a strict replication: between the original and the re-run, the classifier was refactored once and the prompts were modified across sixteen commits, including the deliberate addition of 'minimized-disclosure guards' intended to prevent exactly this failure mode. The phenomenon persists across system evolution including changes designed to prevent it."]

*What this demonstrates:* Binary format produces disparate false positives on the initial naive deployment. The self-contradiction pattern is the mechanism made visible: the model has two valid simultaneous readings; the binary format forces a choice; the format's task structure resolves the ambiguity toward flagging.

---

**Level 2: Classification-internal fixes — the architectural ceiling (~900 words)**

*What this is:* The iterative history of fixes attempted within the classification framework. Each fix shifted the problem rather than resolved it. **This level is the argument for inevitability.**

Structure: progression, not parallel items.

1. **Class context (2026-03-25) — the context paradox** (~200 words)
   - 7 → 12 flags, 1 true positive → 0, 3 FPs → 6 FPs on protected students
   - Why: context primed the model with the class's engagement with race; binary classification read individual engagement with race as individual distress
   - Rules out the context-as-fix approach.

2. **Best-possible binary prompt — Tests B, C, and F (~300 words)** (CORRECTED from B's outline)
   - Explicit equity protections: "Righteous anger = ENGAGEMENT. Lived experience = STRENGTH. AAVE = VALID REGISTER. Neurodivergent writing = COGNITIVE STYLE."
   - Result across 24 preserved runs (Test B = 3 runs, Test C = 1 run with extended length, Test F = 20 stability runs): the binary classifier deterministically false-flags S029 (Jordan Espinoza, neurodivergent test profile) in 24 of 24 runs while deterministically missing S002 (Jordan Kim, burnout, the only true positive) in 24 of 24 runs. S022, S023, S028 deterministically cleared in all 24.
   - The deterministic misclassification IS the evidence. The binary threshold has no position that simultaneously catches genuine distress AND protects the student it most explicitly protects. This is not noise; it is reliable wrongness on the cases that matter most.
   - Rules out the prompt-engineering-as-fix approach. Forecloses the "just tune the threshold" objection.

3. **More output space — Test C** (subsumed into #2 above)

4. **Research-track classifier with class context — Test M (~200 words)** (CORRECTED from B's outline)
   - Ran the research-track binary classifier (`detect_concerns()` from `src/insights/concern_detector.py`) with full pipeline: signal matrix pre-screening, anti-bias regex post-processing, confidence thresholding (≥0.7), class context loaded.
   - Result: S029 cleared (the simplified-binary 100% false-flag rate is a test-harness artifact, not preserved by the safeguarded research-track classifier). But S028 (Imani Drayton, AAVE writer) newly flagged at confidence 0.70.
   - Post-processing safeguards shift false positives from one protected population to another; they do not eliminate them.
   - Rules out "add safeguards to binary classification" as the fix.
   - Note: the original project documentation referred to this as "the production concern detector." Per the development repository's research engine (`research_engine.py` line 247), this function is research-track and never called in production. The findings are about what the function does when invoked, regardless of its deployment status. (This methodological note belongs in a footnote.)

*Summary table:* Six dimensions of failure across all fixes. [B's analysis holds.]

---

**Level 3: Format change works — the ablation study and reproduction (~900 words)**

1. **Observation-only prototype** (~150 words) (FLAGGED)
   - The s1 handoff cites "7 students, 7/7 correct readings." Raw output file not located in `data/raw_outputs/` as of 2026-04-26. Overnight audit session hunting.
   - If located: keep the prototype as part of the inevitability progression — same students binary classification failed on; zero false positives in observation prose; quotes preserved.
   - If not located: cut the prototype subsection. The case is carried by Tests A–D + cross-family reproduction alone. Note the absence in Limitations.

2. **Tests A–D controlled ablation (~400 words)**
   - Test A: not stochastic — generative observation runs produced equivalent asset-framed prose across all 16 runs and three model families (Gemma 12B, Qwen 7B, Gemma 27B).[^analysis-classifier]
   - Test B: not fixable by better prompts — covered in Level 2; introduced here as part of the ablation's logical structure.
   - Test C: not fixable by more output space — covered in Level 2.
   - Test D: observation architecture surfaces what binary classification discards — 7/7 power moves detected on Gemma 12B (single-model; cross-model not yet tested).
   - Quote from log line 1932: *"The format — classification vs. generation — is the primary determinant of equitable outcomes. This is not a prompt engineering finding. It is not a model capability finding. It is not a context finding."*

3. **Cross-model reproduction (~150 words)**
   - 16 runs across Gemma 12B, Qwen 7B, and Gemma 27B all produced asset-framed prose.[^analysis-classifier]
   - Format effect is not model-specific.

4. **The 4-axis classifier: downstream from observation insight (~150 words)**
   - [B's content holds.] Teacher needed binary-adjacent flagging. Observation pass revealed what binary classification was missing. The 4-axis schema (CRISIS/BURNOUT/ENGAGED/NONE) is observation insight formalized into routing. ENGAGED is a structural slot — non-flagging option for equity-critical students based on observation-pass learning. Not an independent intervention.
   - Brief note on 4-axis instability: the 4-axis classifier reduces but does not eliminate the equity-critical misclassification. On Gemma 27B specifically, S029 was 5/6 ENGAGED with 1/6 BURNOUT (~17% misclassification at the decision boundary) — same error shape as binary, much lower frequency. Reinforces format-as-spectrum: lower compression reduces structured failures; only generative observation eliminates them. [Detail in Discussion.]

5. **Asset framing shift: the evidence in specific language (~150 words)** (FLAGGED)
   - The reading-first vs JSON-first coding comparison (S017 Tyler Huang, S001 Maria Ndiaye, S012 Talia Reyes quotes) is referenced in s1 handoff line 171 but not located in `data/raw_outputs/`. Overnight audit session hunting.
   - If located: keep this subsection as the most direct demonstration of format effect on the evaluation frame.
   - If not located: cut this subsection. The case is carried by Test A (cross-model asset framing) and the observation-only prototype if available.

[^analysis-classifier]: An automated classifier (categorizing prose as ASSET / MIXED / DEFICIT) was developed to compare prose across the sixteen generative-observation runs. This classifier produced "MIXED" tags on five of five Gemma 12B runs for the racially-coded student writing while tagging Qwen 7B and Gemma 27B as ASSET. Direct manual review of the prose revealed all three models produced equivalent asset-framed observations. Gemma 12B's prose for the racially-coded case reads, in part: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* The MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents — flattening anger-as-engagement and anger-as-distress because both contain anger-vocabulary. The measurement instrument performed the mechanism under measurement. We corrected via direct prose review.

---

### V. Discussion: Mechanism, Design Principle, and Position (~1,200–1,500 words)

**A. The hybrid compression mechanism (~400 words)**

[B's content holds in substance.] (a) Binary classification is informationally reductive AND (b/c) the binary task activates deficit-detection routing that prompt-level framing cannot override. Self-contradiction evidence is the clearest case. Pure-(a) suggests adding information could fix the problem; data shows it doesn't. The hybrid framing explains why: format chose the routing before the prompt's content reached the active inference path. Design principle follows: change the format, not the prompt.

**Cross-domain corroboration (one paragraph):** [B's content holds. Cite CROSS_EXPERIMENT_ANALYSIS.md as gesture only; no apparatus deployed.]

**B. The design principle (~300 words)**

[B's content holds.] "Move output format in the lower-compression direction." Not a mandate to abandon structure. The format spectrum is a direction, not an endpoint. Adding explanation fields, reading-first passes, asset-framed schema slots — every move toward lower compression reduces deficit-routing activation.

**C. Position relative to prior literature (~400 words)**

[B's content holds.] EdTech bias literature; Queiroga et al. contrast; Hew et al. and Liu as conceptual cousins; novelty claim.

**D. (NEW) The architecture-not-scale finding (~100 words)**

We observed counterintuitively that the larger Gemma model (27B) was less stable on the equity case than the smaller Gemma model (12B), in two separate experiments (the replication study with class context and Test N's 4-axis classifier comparison). Mechanism is not characterized in this paper. The finding reinforces the architecture-not-scale framing of the central claim: scale is not equity insurance. Candidate hypotheses (normative gravity, prior-vs-prompt weighting, inference-setup confound) are documented in the project fieldnote and future-research directory. Systematic characterization is future work.

**E. Limitations (~200 words)** (CORRECTED from B's outline — D in B's structure)

- Synthetic corpus: controlled design enables clean experiment; generalizability to real-world student writing is ongoing work.
- Single subject area: biology corpus deferred; Ethnic Studies equity-critical patterns may be louder than in STEM.
- Held-architecture test (binary vs. generative, no class context) not yet run: planned for R&R.
- Self-contradiction phenomenon: documented in three cases in the original run with raw output not preserved; reproduced in re-runs at varying rates across system iterations including explicit guards against this failure mode. Rate claims would require broader replication under matched conditions.
- The classifier evaluated as "the binary classifier" in this paper is research-track code retained for testing the binary-vs-generative comparisons. It was originally part of production but has been retired from the user-facing pipeline; the findings are about the function as evaluated, regardless of deployment status.
- Counterintuitive 12B-vs-27B finding documented but not characterized; future research direction.
- Small n for some comparisons (Test D: 7 cases on single model; power moves cross-model not tested).
- Production system vs. research tests: the paper documents the research test conditions; the deployed production system has different post-processing behavior whose evaluation is separate work.

---

### VI. Conclusion (~500–600 words)

[B's content holds.]
- A. Finding restated briefly
- B. For system designers: the design principle as practical guide
- C. For researchers: where the mechanism-claim leads (compression as generalizable structural pattern)
- D. For educators as consumers: what to ask vendors
- E. One sentence pointing to the broader theoretical frame (compression across scales; *Politics of Compression* forthcoming)

---

## Supplementary materials / appendix

[B's content holds.]
- Full model itemization
- Corpus design principles
- Test protocols with full parameters
- Direct evidence for the three self-contradiction cases (full model output excerpts where preserved)

---

## Decisions embedded in this v2 (corrections from B's table)

| Decision | Choice | Reasoning |
|---|---|---|
| Opening hook | Self-contradiction moment with verbatim quote (Destiny: "her passion is understandable...") | Mechanism before theory; quote is preserved verbatim in experiment log; lost-data caveat in footnote |
| Test B framing | Deterministic misclassification across 24 runs (Tests B + C + F) | Restores s1's correct framing; sharper claim than "instability"; forecloses tune-the-threshold |
| Test M framing | Research-track classifier with class context, not "production" | Accurate per `research_engine.py` line 247; finding holds; framing changes |
| 16/16 with footnote | Cited at prose level + analysis-classifier methodological footnote | Honest about the analysis classifier confound; instrument performed mechanism |
| 12B-vs-27B | Brief Discussion paragraph + footnote pointer to fieldnote | Counterintuitive aside; not load-bearing; documented for future research |
| Observation-only prototype | Flagged pending audit session result | If located, keep; if not, cut |
| Reading-first comparison | Flagged pending audit session result | Same handling |
| Hybrid compression framing | Substance kept in paper; provenance flagged in s3 handoff | S3 instances should know they have permission to push back |

---

## Open questions for June and s3

1. **Confirm hook quote choice.** Three preserved verbatim quotes available (Destiny, Yolanda, Ingrid). Outline currently recommends Destiny. June's call.

2. **Audit session results may shift Level 3 sections #1 and #5.** If the missing data files are located, those sections stay; if not, they're cut. Confirm shape after audit reports.

3. **Word count.** The outline as structured runs ~7,500–9,000 words. If REE's word limit is 6,500, the most compressible section is Level 2 (the four-fix progression could be condensed; production-system test could move to supplementary). Confirm REE limit before drafting.

4. **The hybrid mechanism framing.** Provenance flagged in s3 handoff (post-handoff interface+June synthesis, not s1 consensus). S3 instances should engage with whether the framing fits the evidence as we now understand it. They may keep, refine, or push back. June reviews their call.

---

*Drafted by interface pane (Claude) on behalf of June, ~01:30 UTC 2026-04-26, while June sleeps. For her morning review. The s3 handoff cites this v2 outline as inheritance.*
