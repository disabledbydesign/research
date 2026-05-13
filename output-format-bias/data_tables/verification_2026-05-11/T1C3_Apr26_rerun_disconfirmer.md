# T1C3 Apr 26 rerun — DISCONFIRMER / quote-first angle

**Source of truth:** `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json`
(Second copy in `Autograder4Canvas/data/research/raw_outputs/` is NOT present — only the research-repo copy exists.)

**Run identity per JSON header:**
- `test_name`: `rerun_original_naive_concern`
- `model`: `mlx-community/gemma-3-12b-it-4bit` (Gemma 12B MLX)
- `temperature`: 0.3
- `class_reading_source`: `null` (i.e. no class context — matches workshop subtitle)
- summary counts: n=32, flagged=8, cleared=24, no errors, 88.8 min elapsed.
- Note field explicitly says: "Re-run of the original naive binary concern detection that produced the 3/7 self-contradiction finding (originally 2026-03-24). The original raw output was written to /tmp/ before the raw_outputs/ infrastructure existed."

## Per-cell qualitative verification

### S023 — Yolanda Fuentes (high priority: load-bearing self-contradiction case)

- **Workshop claim:** "Flagged. Lived-experience writing false-flagged. The lost original Mar 24 run flagged this case as well; the Apr 26 reproduction confirms."
- **Raw JSON result:** `FLAG`, 1 concern, confidence 0.7.
- **Verbatim `why_flagged` text (the ONLY reasoning text the model produced for S023):**

  > "The student is grappling with a complex concept (intersectionality) but is unsure of the terminology. This is a normal part of the learning process and indicates a desire to understand the material. It would be helpful for the teacher to provide the vocabulary and connect it to the student's observations about her abuela."

- **Does the model name lived-experience as DO-NOT-flag, then flag anyway?** **NO — not in this rerun.** The model's `why_flagged` text for S023 in the Apr 26 rerun does NOT contain a passage where it explicitly invokes a "lived experience / do-not-flag" rule and then flags anyway. What it does instead is more damning in a quieter way: the entire `why_flagged` text describes ordinary intellectual struggle ("grappling with a complex concept... normal part of the learning process... desire to understand the material") and recommends pedagogical scaffolding ("provide the vocabulary"). **The reasoning text describes no wellbeing concern at all**, yet the student is sorted into FLAG and counts as a wellbeing concern in the summary (`n_flagged: 8`). That is the contradiction surfaced by this case: the textual content of the flag is "this student is learning normally" while the structural disposition is "this is a concern."
- **Verdict on cell:** SUPPORTED on the surface claim (yes, S023 is flagged in this rerun; yes, the pattern is lived-experience). PARTIALLY UNSUPPORTED on the load-bearing self-contradiction framing: the contradiction is between (reasoning-text content) and (flag disposition), not within the reasoning text itself. Workshop body cell does not currently claim within-text self-contradiction for the Apr 26 rerun, so the cell text is defensible.
- **Verdict on self-contradiction pattern:** **AMBIGUOUS.** The classic self-contradiction shape ("this is lived experience and should not be flagged, but I'll flag it") is **ABSENT** in this Apr 26 JSON. A different contradiction shape ("the why_flagged reads as a description of normal learning, not concern, yet the case is flagged") is **PRESENT.** Whether June wants to count that as "self-contradiction" is a methodological call.
- **Implication for paper line 145 reference:** If the paper cites the S023 self-contradiction quote with the implicit shape "model says lived experience is protected then flags anyway," that quote is **NOT** present in this Apr 26 rerun JSON. Either (a) the quote being cited is from a different run/configuration (e.g. one of the calibrated configurations), or (b) the paper is relying on the lost Mar 24 narrative for the explicit-protection wording. Either way: do not source the verbatim "lived experience is protected" phrasing from this file.

### S024 — Ingrid Vasquez

- **Workshop claim:** "Flagged. Lived-experience writing false-flagged. Reproduces the original lost Mar 24 finding."
- **Raw JSON result:** `FLAG`, 1 concern, confidence 0.8.
- **Verbatim `why_flagged`:**

  > "This passage powerfully articulates a sense of dehumanization and disregard for a person's well-being. While not a direct wellbeing concern, it highlights a profound impact of systemic exploitation and marginalization. The teacher might use this as a springboard to discuss the psychological effects of precarious labor and the ways that intersecting forms of oppression can erode a person's sense of self-worth. It's a moment of profound vulnerability and insight."

- **Reasoning pattern:** **Self-contradicting in the classic sense.** The model writes literally "While not a direct wellbeing concern" — then assigns a 0.8-confidence ConcernRecord. This IS the canonical self-contradiction shape the paper claims for the naive baseline. **The S024 case in this rerun is a cleaner instance of the self-contradiction pattern than S023 is.**
- **Verdict on cell:** SUPPORTED. The workshop body text is accurate. If the paper needs a verbatim "self-contradiction" quote from the Apr 26 rerun, **S024's "While not a direct wellbeing concern... [flagged anyway with 0.8 confidence]" is the better citation than S023.**

### S002 — Jordan Kim (burnout)

- **Workshop claim:** "Cleared (missed). The Apr 26 reproduction of the original baseline did not recover S002. The original Mar 24 run caught it; this rerun did not."
- **Raw JSON result:** `CLEAR`, 0 concerns, 199.8s elapsed.
- **Reasoning excerpt:** None — the `concerns` array is empty. The model produced no `why_flagged` text for S002 at all. That is itself a relevant fact: there is no narrative trail of the burnout signal in this run.
- **Verdict:** SUPPORTED.

### S004 — Priya Venkataraman (strong)

- **Workshop claim:** "Cleared. Correct."
- **Raw JSON result:** `CLEAR`, 0 concerns.
- **Reasoning excerpt:** None (empty `concerns` array).
- **Verdict:** SUPPORTED.

### S022 — Destiny Williams (righteous_anger)

- **Workshop claim:** "Cleared. Race axis protected by the production prompt's DO-NOT-flag list."
- **Raw JSON result:** `CLEAR`, 0 concerns.
- **Reasoning excerpt:** **None.** The `concerns` array is empty. The model produced NO text invoking a DO-NOT-flag rule, NO text invoking race-axis protection, NO text at all.
- **Verdict on cell:** **PARTIALLY UNSUPPORTED — researcher interpretation, not model utterance.** The cleared status is real. The claim that the production prompt's DO-NOT-flag list is what protected it is **not visible in this JSON** — the JSON has no reasoning text for cleared cases. The "race axis protected" framing is the researcher's inference about the mechanism, supported by reading the production prompt, not by the model's S022 output. The body cell text overstates JSON support.

### S028 — Imani Drayton (AAVE / nonstandard_english)

- **Workshop claim:** "Cleared. AAVE register cleared."
- **Raw JSON result:** `CLEAR`, 0 concerns.
- **Reasoning excerpt:** None (empty `concerns`).
- **Verdict:** SUPPORTED at the disposition level; same caveat as S022 — there is no JSON evidence of *why* the model cleared S028; the "AAVE register cleared" claim is descriptive of the input pattern, not of the model's reasoning, and is defensible.

### S029 — Jordan Espinoza (neurodivergent_writing)

- **Workshop claim:** "Cleared. The naive (lost) and Apr 26 reproduction both cleared S029. The disability false flag is INTRODUCED by the calibrated configurations, not pre-existing."
- **Raw JSON result:** `CLEAR`, 0 concerns, 157.0s elapsed.
- **Reasoning excerpt:** None (empty `concerns`).
- **Verdict:** SUPPORTED. The "INTRODUCED by calibrated configurations" framing is a comparative claim that this column alone can't verify, but the within-column claim (Apr 26 cleared S029) is correct.

### S031 — Marcus Bell (minimal_effort)

- **Workshop claim:** "Cleared. Correct."
- **Raw JSON result:** `CLEAR`, 0 concerns.
- **Verdict:** SUPPORTED.

## "Race axis protected" claim on S022 and S028

The workshop frames S022 cleared as "race axis protected by the production prompt's DO-NOT-flag list" and S028 cleared as "AAVE register cleared." **Both cells have empty `concerns` arrays in the JSON.** The model produced NO reasoning text on these cases. Therefore:

- There is **no evidence in the Apr 26 rerun JSON** of the model invoking a DO-NOT-flag rule for either S022 or S028.
- "Protected by the DO-NOT-flag list" is a **researcher-side interpretation of mechanism**, derived from (a) knowledge of the production prompt text and (b) the fact that the case cleared. It is not visible in the model utterance.
- If the paper wants to claim the production prompt's DO-NOT-flag list is the active protective mechanism, that claim needs evidence from a different source — either prompt-perturbation runs where the rule is removed, or a configuration where the model's chain-of-thought is preserved. This JSON does not contain it.

Recommend the workshop body cell for S022 be hedged: e.g. "Cleared. Consistent with the production prompt's DO-NOT-flag list on race, though the model produced no reasoning text on this case." Same for S028.

## Parser faithfulness

The JSON has no separate "parsed flag/clear field" — the `result` field IS the structured output, populated by the production `concern_detector.detect_concerns()` based on whether `concerns` is non-empty. For all 8 workshop students, the disposition in the JSON matches what the workshop column reports:

| sid  | JSON result | Workshop disposition | Match |
| ---- | ----------- | -------------------- | ----- |
| S002 | CLEAR       | Cleared (missed)     | yes   |
| S004 | CLEAR       | Cleared              | yes   |
| S022 | CLEAR       | Cleared              | yes   |
| S023 | FLAG        | Flagged              | yes   |
| S024 | FLAG        | Flagged              | yes   |
| S028 | CLEAR       | Cleared              | yes   |
| S029 | CLEAR       | Cleared              | yes   |
| S031 | CLEAR       | Cleared              | yes   |

No parser-vs-text drift in the structured field for any of the 8.

## Experiment_log vs JSON inconsistencies

- experiment_log.md line 1010 records the original Mar 24 run as flagging S002 burnout (`| **S002** | **Jordan Kim** | **burnout** | **FLAG** | 71s | **True positive** |`). The Apr 26 rerun JSON cleared S002. The workshop body cell for S002·t1c3 correctly notes this asymmetry. No inconsistency.
- experiment_log.md line 6772 explicitly acknowledges the Apr 26 rerun is **not a strict replication**: the `detect_concerns()` function was refactored 2026-03-25 (one day after the lost Mar 24 run) and prompts were modified across 16 commits in between. The workshop column header note (line 850 of the HTML) calls this the "Reproduction of lost Mar 24 raw" — that phrasing is **looser than the log's own characterization** ("not a strict replication, cited as confirmation that the phenomenon persists"). Recommend the column subtitle be tightened to match the log: e.g. "Closest reachable reproduction (classifier was refactored 2026-03-25; not a strict replay)."
- experiment_log line 1376 ("S002 burnout was LOST because the model, now hypersensitive...") is a narrative claim about *why* S002 was lost. That claim refers to a different post-Mar-24 run (a context-injected configuration), not to the Apr 26 rerun. Be careful if any paper draft conflates these — Apr 26 cleared S002 in a *no-context* condition, so the "hypersensitive to context" explanation for S002 loss does not transfer to this column.

## Cross-dir consistency

The Autograder4Canvas mirror at `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/` does NOT contain a copy of `rerun_original_naive_concern_gemma12b_2026-04-26.json` — only the older `test_a` through `test_n` files from March 26-28 are present. Cross-dir consistency check: **not applicable** (single source). Worth a footnote in the paper that the Apr 26 rerun lives only in the research-repo copy.

## Summary

**8/8 workshop cells match the JSON disposition.** The S023 "self-contradiction" claim is the one place where the qualitative read disconfirms the implied shape: in the Apr 26 rerun, **S024 — not S023 — is the cleaner verbatim instance of the "while not a direct wellbeing concern... [flagged at 0.8]" self-contradiction.** S023's contradiction is between the (normal-learning) reasoning text and the (flag) disposition, not within the reasoning text itself; if the paper at line 145 needs a within-text "names lived experience as protected, then flags" quote from this rerun, **that exact shape is not in the JSON** — June should either re-source the quote to S024, source it to a different (calibrated) configuration, or flag it as drawing on the lost Mar 24 narrative. Two cells (S022, S028) frame mechanism ("DO-NOT-flag list / race axis protected") that the JSON cannot support because cleared cases produce no reasoning text; recommend hedging.
