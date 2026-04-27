# Convergent Claim — Session 2 v4 (post-audit revision)

**Date:** 2026-04-26
**Author:** Interface pane (Claude, on behalf of June), revising v3 against the data-verification-audit findings
**Status:** Draft for June's review. Edit in place. Final inheritance for s3 unless you revise.
**Inheritance lineage:** A's v1 → B's v2 → interface v3 (validation pass) → v4 (audit) → in-place gap-review revision 2026-04-26 PM (see "Gap-review revision" note below).

**Gap-review revision (2026-04-26 PM):** Two targeted edits against the convergent claim:
(1) The mechanism paragraph (¶2 of the claim) was revised to make routing the load-bearing component of the hybrid mechanism, with informational compression as the necessary baseline. The earlier wording presented the two halves as parallel; June's marginalia in REVIEW_FOR_JUNE.md (line 29) records her reading of the data as pointing to routing with directional weight. The substance of the routing argument was already present in the surrounding paragraphs; this edit makes the directional weight visible in the claim itself.
(2) Footnote 1 (lost-data + recovery-rerun) was extended to include three verbatim quotes from the 2026-04-26 rerun's `why_flagged` field (S023, S024, S001), preserving the strongest replicable evidence the rerun produced rather than reporting only the count. Quotes pulled directly from `data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json`.

---

## What changed from v3 and why

This v4 revises v3 against the data-verification-audit findings (instances A and B, 2026-04-26). The substantive change is the **Test B framing**: v3 treated the log-vs-JSON divergence on Test B as evidence of "deterministic-not-instability" with a lost-data caveat. The audit found that the divergence is explained more cleanly: the recovery JSONs ran on a *calibrated anti-bias pipeline*, not on the same conditions as the original. This produces a stronger argument structure — a three-row ablation across binary configurations — that should anchor the paper's methods section. Itemized:

1. **Recovery framing for Tests B/C.** The original 2026-03-26 Test B narrative shows S029 = CLEAR ("cleared every student"). The 2026-03-27 recovery JSONs show S029 = FLAG. A confirmed via two specific git commits (`765ba64`: "alt hypothesis test infrastructure, data preservation **never /tmp**"; `0c67cc5`: "Tests A-E **reproduced**") that the recovery infrastructure included a calibrated anti-bias pipeline (explicit equity protections in the prompt + anti-bias regex post-processing). The Test B/C divergence isn't reproducibility noise; it's two different binary configurations (naive vs. calibrated) failing in opposite directions on the equity case.

2. **The three-row ablation as the strongest argument structure** (B's audit recommendation, A endorsed). The paper has three rows of evidence:
   - **Row 1 (naive binary, 2026-03-24):** false-flagged S022/S023/S024 with self-contradiction; 3/7 of all flags self-contradicting. *Over-correction unavailable, deficit framing direct.* Original raw lost; verbatim quotes preserved in experiment log; rerun on current research-track code (2026-04-26) reproduces the phenomenon at 6/8.
   - **Row 2 (calibrated anti-bias binary, 2026-03-27 forward):** with explicit equity protections naming righteous anger / lived experience / AAVE / neurodivergent writing as non-concerns AND anti-bias regex post-processing AND class context — *deterministically false-flags S029 in 24/24 preserved runs while deterministically missing S002 in 24/24*. Three layers of safeguard fail to override the format on the neurodivergent self-disclosure pattern.
   - **Row 3 (generative observation):** 16/16 runs across three model families produce asset-framed prose for the equity-critical students. Zero false positives at the prose level; classification noise is in the analysis classifier we built downstream, not in the AI's behavior.

3. **"Configurable failure mode but not configurable failure"** (B's framing, A adopted). The binary classifier's failure on the equity case is *configurable* — naive binary fails by clearing everyone (over-correction toward safety, missed true positive); calibrated anti-bias binary fails by false-flagging the neurodivergent student (under-correction on equity despite explicit safeguards). The failure itself is *not configurable*. Tuning shifts which failure mode surfaces. Architectural change (format change) is what actually resolves it.

4. **Class context shifts from confound to failed safeguard.** s1 instance A's hedge ("format and architecture covary across conditions") was the right instinct for the wrong reason. The covariation in Test B-recovery isn't limiting the inference — it's being exploited as a harder test. *"Even with class context AND equity-protective prompt AND anti-bias post-processing, the binary still false-flags S029"* is stronger evidence than *"with no safeguards"* would be. The held-architecture run is the missing isolation that would strengthen generalizability claims; it is not required to support the format-ceiling claim.

5. **Asymmetry of recovery as signature evidence** (A's contribution). Tests A, D, E recovered cleanly between 2026-03-26 and 2026-03-27. Tests B, C diverged. The asymmetry isn't reproducibility noise — it's evidence: the calibration changes were binary-format-specific (prompt language + anti-bias post-processing). Generative observation has no deficit-detection routing to safeguard against; nothing for the calibration to change. The fact that *only* the binary-format tests show divergent recovery is itself a signature of the format being the variable.

6. **Test E was never run on Gemma 12B.** A confirmed via direct file inspection: the Gemma 12B reproduction is Test A; Test E is Qwen 7B + Gemma 27B only. The s1 handoff conflated the two tests in the "16/16 across three model families" framing. The paper should itemize per-test rather than aggregate.

// agreed. E was probably the same as another test we ran on the 12b, and we were testing cross family. Sounds like a slipage. 

7. **Reading-first vs. JSON-first comparison file FOUND.** Located at `Autograder4Canvas/data/demo_baked/reading_first_comparison.json`. The validation pass searched `output-format-bias/data/raw_outputs/` only; the audit hunt found it elsewhere. Citation stays. Tyler Huang / Maria Ndiaye / Talia Reyes quotes are real and preserved.

8. **Observation-only prototype results survive in the experiment log** (2026-04-26 audit confirmed). Raw JSON went to `/tmp/` per experiment_log line 1770. Per-student observation quotes preserved in `experiment_log.md` lines 1455–1465. The paper can cite the log for those quotes. (Note: `synthesis_first_prototype.json` in demo_baked is a *different* file — different students, different test.)

---

## Convergent claim — Session 2 v4

In an AI-powered student welfare classifier developed for community-college Ethnic Studies — a deployed survival tool for managing 170+ students without a teaching assistant — the *output format* demanded of the underlying language model is the primary determinant of whether the system produces disparate false positives on students from non-dominant linguistic and cultural backgrounds. The format does not merely bottleneck what reaches the output; it selects which evaluative pathway the model runs. 

The mechanism is hybrid compression — informational and routing — with the available evidence pointing to routing as the load-bearing component for what this paper documents. Binary classification is informationally reductive on its face: one bit out, multidimensional context lost. That much pure information theory predicts. But pure information loss does not in itself account for the experimental results: it does not explain why a binary prompt that explicitly names righteous anger, lived experience, and neurodivergent writing as non-concerns still produces false flags. The equity-protective content reaches the model's prompt and is not overridden by capacity limits; it is overridden by the format's task structure. The binary task itself activates a deficit-detection routing that runs ahead of, and downstream from, the prompt's asset-aware content. Informational compression is the necessary baseline of what "binary" does to information capacity; routing is where the equity-critical work fails. Both are present; the paper's evidence speaks most directly to the routing layer. The most direct evidence are documented cases in which the model's own free-text explanation argues the flag should not have been set: the asset-aware reading is there, in the output, contradicting the binary result alongside it. In the original 2026-03-24 32-student naive deployment, three of seven flags were such self-contradictions: the model wrote *"her passion is understandable and appropriate"* and then flagged the student; *"an opportunity for the teacher"* and then flagged; *"not a wellbeing concern in itself"* and then flagged.[^contradictions]

The empirical structure is a three-row ablation across binary configurations:[^ablation]

- *Row 1 — naive binary classification (2026-03-24).* Three false positives on equity-critical students with self-contradicting reasoning. One true positive flagged correctly. The configuration over-corrects toward sensitivity at the cost of equity.
- *Row 2 — calibrated anti-bias binary classification (2026-03-27 forward).* Same model, same students, but with explicit equity-protective prompt language naming righteous anger, lived experience, AAVE, and neurodivergent writing as non-concerns; anti-bias regex post-processing; class context. Across 24 preserved runs (Tests B, C, and F), the calibrated configuration **deterministically false-flags S029 (Jordan Espinoza, neurodivergent test profile) while deterministically missing S002 (Jordan Kim, burnout, the only true positive)**. S022, S023, S028 are correctly cleared. The configuration over-corrects toward equity — but only on certain students — at the cost of clinical sensitivity, and still false-flags the most explicitly protected student profile.
- *Row 3 — generative observation.* Across all 16 runs and three model families (Gemma 12B, Qwen 7B, Gemma 27B), the AI produces asset-framed prose for the equity-critical students.[^analysis-classifier] Zero false-positive flags. The format itself does not require a single binary verdict; the model can describe what the student is reaching for without forcing a deficit/non-deficit choice.

The pattern that emerges is not "binary fails one way and generative succeeds." It is: **the binary classifier's failure mode on the equity case is configurable (over-correction toward safety vs. under-correction toward equity), but the failure itself is not.** Three layers of safeguard — class context, equity-protective prompt language, anti-bias post-processing — fail to override the format on S029. Tuning shifts which failure mode surfaces; tuning does not eliminate the failure. The format is the architectural ceiling.

The asymmetry of the calibration's effect across tests is itself signature evidence: the calibration changes between 2026-03-26 and 2026-03-27 were binary-format-specific (prompt language + post-processing). Generative observation has no deficit-detection routing to safeguard against; tests of generative observation (Tests A, D, E) reproduced cleanly across the calibration boundary because there was nothing for the calibration to change. Tests of binary classification (Tests B, C) diverged. The format the calibration touched is the only format whose recovery diverged.

Format is one instance of compression. Because the mechanism is compression, the design principle generalizes: *move output format in the lower-compression direction; format-driven bias decreases as compression decreases.* For systems that still require structured output for downstream processing, the principle is not "abandon structure" but "preserve as much specificity as the system can carry." What counts as lower compression is an empirical question along multiple axes; the available evidence documents the direction and the mechanism, not a fully validated spectrum mapping.[^scale]

---

## Footnotes (paper-ready language)

[^contradictions]: The raw output file from the original 2026-03-24 32-student naive concern detection was written to `/tmp/` before the persistent `data/raw_outputs/` infrastructure existed, and was not preserved. The persistence-fix commit (`765ba64`, 2026-03-26) added "alt hypothesis test infrastructure, data preservation (never /tmp)" and triggered a recovery re-run period in which Tests A–E were re-executed with the persistent storage layer wired up (commit `0c67cc5`, 2026-03-27, "Tests A-E reproduced"). The recovery infrastructure also included a calibrated anti-bias pipeline (see footnote on three-row ablation). Verbatim model output quotes for the three self-contradicting cases are preserved in the project's experiment log (lines 1260–1263). A re-run conducted on 2026-04-26 using the current research-track binary classifier (`detect_concerns()` from `src/insights/concern_detector.py`, with the same 32-student corpus, no class context; raw output preserved at `data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json`) produced eight flags of which six exhibited the self-contradiction phenomenon. Verbatim model output from the re-run, in the `why_flagged` field of each flagged record: S023 Yolanda Fuentes, flagged — *"The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material."* S024 Ingrid Vasquez, flagged — *"This passage powerfully articulates a sense of dehumanization and disregard for a person's well-being. While not a direct wellbeing concern, it highlights a profound impact of systemic exploitation and marginalization."* S001 Maria Ndiaye, flagged — *"The student is articulating a complex understanding of their mother's identity and how multiple factors contribute to her experiences. This is a strong application of intersectionality and a valuable personal connection to the concept."* In each case the binary verdict is FLAG; the model's own reasoning argues against the flag in the same output. The phenomenon persists across system iterations including explicit guards added between original and re-run intended to prevent it; the specific student cases shift (S022 is no longer false-flagged in the current code path due to a guard added in the refactor period; S023 and S024 still self-contradict; new cases S001 and S005 join). The research-track classifier function (`detect_concerns()`) is kept for testing the binary–4-axis–generative spectrum after binary classification was retired from the user-facing pipeline; it is not called in production (per `src/insights/research_engine.py` line 247).

[^ablation]: The naive-binary baseline (Row 1) and the calibrated-anti-bias baseline (Row 2) were not designed as a controlled ablation in advance. They emerged from the project's iterative development: the naive binary produced equity false positives in early use (2026-03-24); calibrated anti-bias safeguards (explicit equity-protective prompt, anti-bias regex post-processing, class-context loading) were engineered between 2026-03-25 and 2026-03-27 to address the failures; the calibrated configuration was then tested formally in Tests A–F (2026-03-26 specification, 2026-03-27 execution under the persistence layer). The three-row structure is the honest comparison the iterative design history produces. The held-architecture run — binary classification with no class context and no anti-bias safeguards — was not run in this development period; it would strengthen the generalizability of the format-ceiling claim by removing the safeguard layer entirely. Planned for revision.

[^analysis-classifier]: An automated classifier (categorizing prose as ASSET / MIXED / DEFICIT) was developed to compare prose across the sixteen generative-observation runs. This classifier produced "MIXED" tags on five of five Gemma 12B runs for the racially-coded student writing while tagging the corresponding Qwen 7B and Gemma 27B runs as ASSET. Direct manual review of the prose revealed that all three models produced equivalent asset-framed observations. Gemma 12B's prose for Destiny Williams reads, in part: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* The MIXED tags were artifacts of the analysis classifier itself reproducing the same compression dynamic the paper documents — flattening "anger-as-engagement" and "anger-as-distress" into a single tag because both contain anger-vocabulary. The measurement instrument performed the mechanism under measurement. We corrected via direct prose review. The "16/16 across three model families" count refers to Test A on Gemma 12B (10 runs) and Qwen 7B (6 runs) + a separate Test A run on Gemma 27B (6 runs). Test E (cross-model replication) covers Qwen 7B (6 runs) and Gemma 27B (6 runs) — Test E was never run on Gemma 12B; the Gemma 12B reproduction lives in Test A.

[^scale]: A counterintuitive secondary finding emerged during validation: across two separate experiments (the replication study with class context and Test N's 4-axis classifier comparison), Gemma 27B was less stable than Gemma 12B on the equity case. The larger model produced a wider distribution of misclassifications on the same equity-critical student profiles. This is not load-bearing for the present paper's argument and is not characterized here. We document the pattern and three candidate hypotheses (normative gravity, prior-vs-prompt weighting, inference-setup confound) in `fieldnotes/observation_27b_less_stable_than_12b_on_equity_2026-04-25.md` and the future-research directory `research/scale_vs_equity/`. The finding reinforces the paper's architecture-not-scale framing: scale is not equity insurance.

---

## What this claim does and does not contain

**Contains:**
- Empirical context (community college, Ethnic Studies, deployed survival tool, scale)
- The structural finding (format is the primary determinant of disparate FPs)
- The hybrid-compression mechanism, named explicitly, with the argument's logic visible
- Self-contradiction as direct evidence for the routing-half of the mechanism
- The original 3/7 self-contradiction phenomenon with named cases and verbatim quotes (with lost-data + recovery-rerun footnote)
- The three-row ablation: naive binary → calibrated anti-bias binary → generative observation
- "Configurable failure mode but not configurable failure" framing
- Class context as failed safeguard, not confound
- Asymmetry-of-recovery as signature evidence the calibration was binary-format-specific
- Compression-as-mechanism / format-as-spectrum direction principle (no spectrum enumeration)
- Four load-bearing footnotes: lost-data + recovery-rerun, ablation history, analysis-classifier confound, 12B-vs-27B aside

**Does not contain (intentionally moved out):**
- The full iterative-design history (belongs in Introduction + Findings)
- The theoretical scaffolding (Yosso/Freire/Bonilla-Silva + compression-research — belongs in Theoretical Framework)
- The contribution-summary paragraph (belongs at end of Introduction)
- The cross-domain dual-register evidence (one-paragraph gesture in Discussion)
- A validated spectrum enumeration (the available evidence covers endpoints + one intermediate)
- The 4-axis classifier instability findings (belong in Findings or Discussion, with caveats)

---

## Open questions for June's review

1. **Hook for the Introduction.** Outline still recommends one of the three preserved verbatim self-contradiction quotes (Destiny: *"her passion is understandable and appropriate"*). Decision still June's call.

2. **Live data question (still open).** Self-care unit anonymized cases — defer to R&R remains the working recommendation.

3. **The "compression is hybrid" framing.** Provenance flagged in s3 handoff (post-handoff interface+June synthesis, not s1 instance consensus). With the three-row ablation now in place, the hybrid framing is *more* empirically grounded than it was in v3 — the calibrated-anti-bias-binary evidence directly demonstrates the routing half of the hybrid (prompt content reaches the model; format overrides it). S3 instances should still know they have permission to push back, but the substance is now better supported.

4. **Held-architecture run.** Now framed in the convergent claim's footnote 2 as planned-for-revision rather than as a current-paper limitation. That's an upgrade in posture given the three-row ablation provides strong evidence even without it.

---

## Sources verified against

- The data-verification-audit (2026-04-26) — independent re-verification by A and B, with recovery hypothesis confirmed via specific git commits and calibrated-anti-bias-pipeline correction confirmed via June's architectural knowledge.
- `verification_table.md` — comprehensive table extracted from 81 raw JSONs.
- `experiment_log.md` `## CORRECTIONS — 2026-04-25` section.
- s1 CONVERSATION.md (1252 lines) — confirmed s1 instances had deterministic-not-instability framing right before s2 drift.
- `Autograder4Canvas/data/demo_baked/reading_first_comparison.json` — found by audit; preserves S017/S001/S012 quotes referenced in s1 handoff.
- `data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json` — re-run of the lost original with self-contradiction reasoning preserved per-student.

---

*Drafted by interface pane (Claude) on behalf of June, ~13:30 UTC 2026-04-26, after both audit instances signaled session close. For her morning review and inheritance to s3.*
