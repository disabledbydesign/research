# Convergent Claim — Session 2 v3 (verified-ground revision)

**Date:** 2026-04-26
**Author:** Interface pane (Claude, on behalf of June), revising B's v2 against the validation pass findings
**Status:** Draft for June's morning review. Edit in place.

---

## What changed from v2 and why

This v3 revises B's v2 against the verified ground produced by the 2026-04-25 validation pass. The structural architecture of the claim holds; the changes are at the level of (a) specific numerical claims, (b) one analytical reframe (instability → deterministic), (c) language acknowledging research-track vs. production, (d) a new methodological footnote pointing to the analysis-classifier confound. Itemized:

1. **"Instability" → "deterministic misclassification."** Across 24 preserved runs of equity-aware binary classification (Test B = 3 runs, Test C = 1 run, Test F = 20 runs), S029 = 24/24 FLAG; S002 = 24/24 CLEAR; S022, S023, S028 = 24/24 CLEAR. The pattern is not flips but reliable wrongness on the equity case. This restores what s1 instance B had argued correctly before s2 drift — see s1 CONVERSATION.md line 921. Rhetorically stronger: forecloses "just tune the threshold" because the binary is deterministically misclassifying on the cases that matter most.

2. **"S029 in three of four runs" → cross-test deterministic.** B's v2 cited four Test B runs; only three are preserved in `data/raw_outputs/`. The fourth never existed in the saved record. Updated language: "across every preserved run of the equity-aware binary classification (24 runs across Tests B, C, and F)..."

3. **"16/16 across three model families" with footnote.** The 16/16 finding holds at the prose level (manual review of all generative-observation runs confirmed asset framing across Gemma 12B, Qwen 7B, and Gemma 27B). The downstream ASSET/MIXED/DEFICIT analysis classifier we built to compare runs produced 5/5 MIXED on Gemma 12B for the racially-coded student because the classifier keys on deficit-coded vocabulary (the model's prose explicitly *names* and *defends* the student's anger, which trips the classifier). New footnote acknowledges the analysis classifier itself reproduced the same compression dynamic the paper documents — measurement instrument performing the mechanism under measurement.

4. **"Production concern_detector" → "research-track binary classifier."** The `detect_concerns()` function is a research-track tool kept for testing the binary–4-axis–generative spectrum after the binary was retired from production. `research_engine.py` line 247 explicitly notes it is never called in production. The s1 handoff's "production" framing was inherited language from an earlier framing we hadn't audited. Test M (the test that used `detect_concerns()` with class context) needs to be cited as evidence of "what the research-track binary classifier with class context does," not "what production does."

5. **3/7 self-contradiction with lost-data footnote.** The original 32-student naive concern detection that produced the documented 3/7 self-contradiction finding (S022 Destiny Williams: *"her passion is understandable and appropriate"* → FLAG; S023 Yolanda Fuentes: *"an opportunity for the teacher"* → FLAG; S024 Ingrid Vasquez: *"not a wellbeing concern in itself"* → FLAG) had its raw output written to `/tmp/` before the `data/raw_outputs/` infrastructure existed. Verbatim quotes preserved in `research/experiment_log.md` lines 1260–1263. Re-running the current research-track code in 2026-04 produces the same self-contradiction phenomenon on a similar set of students at a higher rate (6 of 8 flags, including direct repetition of S023's and S024's contradictions in nearly the same wording). Cite the original 3/7 rate; acknowledge the original raw was lost; footnote the re-run as confirmation that the phenomenon survives a month of code evolution including explicit guards added to prevent it.

6. **12B-vs-27B counterintuitive finding.** Brief mention added in the methods/discussion-flagging paragraph. Mechanism not claimed; pointer to fieldnote and `research/scale_vs_equity/` directory.

---

## Convergent claim — Session 2 v3

In an AI-powered student welfare classifier developed for community-college Ethnic Studies — a deployed survival tool for managing 170+ students without a teaching assistant — the *output format* demanded of the underlying language model is the primary determinant of whether the system produces disparate false positives on students from non-dominant linguistic and cultural backgrounds. The format does not merely bottleneck what reaches the output; it selects which evaluative pathway the model runs. The mechanism is hybrid compression: binary classification is informationally reductive on its face — one bit out, multidimensional context lost — *and* the binary task itself activates a deficit-detection routing that overrides asset-framing instructions in the prompt. Both halves are necessary. The pure information-loss account cannot explain why a binary prompt that explicitly names righteous anger, lived experience, and neurodivergent writing as non-concerns still produces false flags; the equity-protective content reaches the model's prompt and does not override the classification behavior. Something at the level of the format's task structure, not its information capacity, is doing the work. The most direct evidence: documented cases in which the model's own free-text explanation argues the flag should not have been set — the asset-aware reading is there, in the output, contradicting the binary result alongside it. In the original 32-student naive deployment, three of seven flags were such self-contradictions: the model wrote *"her passion is understandable and appropriate"* and then flagged the student; *"an opportunity for the teacher"* and then flagged; *"not a wellbeing concern in itself"* and then flagged.[^contradictions]

The empirical core is a four-test controlled ablation (Tests A–D, same model and corpus, alternative explanations ruled out in sequence) reproduced across three model families: Gemma 12B, Qwen 7B, and Gemma 27B. Across all sixteen generative-observation runs, the AI produced asset-framed prose for the equity-critical students; zero false-positive flags.[^analysis-classifier] When the same equity-aware binary prompt — with explicit protections naming righteous anger, lived experience, AAVE, and neurodivergent writing as non-concerns — is run across 24 preserved runs of three test conditions (Tests B, C, and F), the binary classifier deterministically false-flags S029 (Jordan Espinoza, neurodivergent test profile) in 24 of 24 runs while deterministically missing S002 (Jordan Kim, burnout, the only true positive) in 24 of 24 runs. The binary threshold cannot simultaneously be sensitive enough to catch genuine distress AND equitable enough to protect the student it most explicitly protects. The format selects the routing before the prompt's content can redirect it.

Format is one instance of compression. Because the mechanism is compression, the design principle generalizes: *move output format in the lower-compression direction; format-driven bias decreases as compression decreases.* For systems that still require structured output for downstream processing, the principle is not "abandon structure" but "preserve as much specificity as the system can carry." What counts as lower compression is an empirical question along multiple axes; the available evidence documents the direction and the mechanism, not a fully validated spectrum mapping.[^scale]

---

## Footnotes (paper-ready language)

[^contradictions]: The raw output file from the original 2026-03-24 32-student naive concern detection was written to `/tmp/` before the persistent `data/raw_outputs/` infrastructure existed, and was not preserved. Verbatim model output quotes for the three self-contradicting cases are preserved in the project's experiment log (lines 1260–1263). A re-run conducted on 2026-04-26 using the research-track binary classifier (`detect_concerns()` from `src/insights/concern_detector.py`, with the same 32-student corpus, no class context) produced eight flags of which six exhibited the self-contradiction phenomenon, including direct reproductions of the S023 and S024 contradictions in nearly the original wording. The re-run was not a strict replication: between the original test and the re-run, the classifier was refactored once and the prompts were modified across sixteen commits, including the deliberate addition of "minimized-disclosure guards" intended to prevent exactly the failure mode the original finding documented. The phenomenon persists across a month of system evolution, including changes designed to prevent it.

[^analysis-classifier]: An automated classifier (categorizing prose as ASSET, MIXED, or DEFICIT) was developed to compare prose across the sixteen generative-observation runs. This classifier produced "MIXED" tags on five of five Gemma 12B runs for the racially-coded student writing (Destiny Williams) while tagging the corresponding Qwen 7B and Gemma 27B runs as ASSET. Direct manual review of the prose revealed that all three models produced equivalent asset-framed observations. Gemma 12B's prose for Destiny Williams reads, in part: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* The MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents — flattening "anger-as-engagement" and "anger-as-distress" into a single tag because both contain anger-vocabulary. The measurement instrument performed the mechanism under measurement. We corrected via direct prose review.

[^scale]: A counterintuitive secondary finding emerged during validation: across two separate experiments (the replication study with class context and Test N's 4-axis classifier comparison), Gemma 27B was less stable than Gemma 12B on the equity case. The larger model produced a wider distribution of misclassifications on the same equity-critical student profiles. This is not load-bearing for the present paper's argument and is not characterized here. We document the pattern and three candidate hypotheses (normative gravity, prior-vs-prompt weighting, inference-setup confound) in `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md` and the future-research directory `research/scale_vs_equity/`. The finding reinforces the paper's architecture-not-scale framing: scale is not equity insurance.

---

## What this claim does and does not contain

**Contains:**
- Empirical context (community college, Ethnic Studies, deployed survival tool, scale)
- The structural finding (format is the primary determinant of disparate FPs)
- The hybrid-compression mechanism, named explicitly, with the argument's logic visible
- Self-contradiction as direct evidence for the routing-half of the mechanism
- The original 3/7 self-contradiction phenomenon with named cases and verbatim quotes (with lost-data footnote acknowledging the re-run)
- The empirical core (Tests A–D + cross-family reproduction)
- Test B/C/F deterministic misclassification across 24 preserved runs (replaces "instability" framing)
- Compression-as-mechanism / format-as-spectrum direction principle (no spectrum enumeration)
- Three load-bearing footnotes: the 3/7 lost-data story, the analysis-classifier confound, the 12B-vs-27B aside

**Does not contain (intentionally moved out):**
- The full iterative-design history (belongs in Introduction + Findings)
- The theoretical scaffolding (Yosso/Freire/Bonilla-Silva + compression-research — belongs in Theoretical Framework)
- The contribution-summary paragraph (belongs at end of Introduction)
- The cross-domain dual-register evidence (one-paragraph gesture in Discussion)
- A validated spectrum enumeration (the available evidence covers endpoints + one intermediate)
- The 4-axis classifier instability findings (belong in Findings Level 2 or Discussion, with caveats; this paper does not center the 4-axis as an equity intervention)

---

## Open questions for June's morning review

1. **Hook for the Introduction.** B's outline opens with one of the three self-contradiction quotes (mechanism artifact first). I'm leaving the specific opening sentence to the drafting session — but flagging that the opening quote should be one of the three preserved verbatim from the experiment log (Destiny, Yolanda, or Ingrid). The footnote handles the lost-data caveat. June's read on which of the three is the strongest opener welcome.

2. **Test M citation in the paper.** The convergent claim doesn't cite Test M directly. The Findings section will. Question for June: does the paper cite Test M as evidence of "research-track classifier with class context shifts FPs to a different protected population (S028 newly flagged)" — that's a real finding — or is the Test M evidence cut entirely and replaced with cleaner Test E cross-family reproduction? My read: keep Test M, reframe the citation.

3. **Live data question (still open).** Should June pull anonymized self-care unit cases as additional evidence? The convergent claim doesn't depend on this. The Findings section could include 3–5 cases as illustrative if they're available; could also defer to R&R. Recommend: defer to R&R for May 20.

4. **The "compression is hybrid" framing.** This was added post-handoff by interface pane + June, not by s1 instances. The substance is sound and is now in the v3 claim. The provenance is flagged in the s3 handoff — s3 instances will know they have permission to push back if they see a way the framing should be different.

---

## Sources verified against

- `verification_table.md` (this session 2 directory) — comprehensive table extracted from 81 raw JSONs
- `experiment_log.md` `## CORRECTIONS — 2026-04-25` section (line 6721+) — five subsections of verified deltas
- `data/raw_outputs/test_b_*.json` (3 files), `test_c_length_*.json`, `test_f_bc_stability_*.json` (2 files × 10 reps) — Test B/C/F deterministic pattern (24/24 across all preserved runs)
- `data/raw_outputs/test_a_temperature_*.json`, `test_e_cross_model_*.json` — generative observation prose verified manually
- `data/raw_outputs/test_m_production_detector_*.json` — Test M results
- `data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json` — re-run of the lost original
- s1 CONVERSATION.md (1252 lines) — confirmed s1 instances had deterministic-not-instability framing right before s2 drift
- `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md` — 12B>27B finding documented
- `research/scale_vs_equity/README.md` — future research directory established

---

*Drafted by interface pane (Claude) on behalf of June, ~01:00 UTC 2026-04-26, while June sleeps. For her morning review. The sequencing in the s3 handoff document has this as the inheritance for s3's drafting work.*
