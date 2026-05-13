# Fixes applied — post-rationale audit, 2026-05-11

**Scope.** Mechanical fix-application + prompt-variant tracking pass across the three workshop/table HTML files.

**Files modified:**

1. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/ablation_workshop.html`
2. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/4axis_iteration_workshop.html`
3. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/12B_vs_27B_differential_table_2026-05-11.html`

**Source of truth:** raw JSONs in `output-format-bias/data/raw_outputs/` per the six audit notes in this directory. SHA-256 prefixes for prompt variants were already computed in `12B_vs_27B_verifier.md` and `12B_vs_27B_disconfirmer.md`; this pass re-used those hashes verbatim rather than recomputing.

---

## Fix-by-fix status

### Fix 1 — T1C1 rationale verbatim polish (binary workshop) — **APPLIED**

In `ablation_workshop.html` `DEFAULT_CELLS.t1`:

- **T1C1 S004 rationale:** appended dropped trailing sentence "The reflection on the applicability of Crenshaw's framework to a different cultural context is a sign of critical thinking, not a sign of personal struggle."
- **T1C1 S022 rationale:** restored "= doing the assignment" inside the model's inner quoted exclusion criterion ("...AS COURSE MATERIAL = doing the assignment").
- **T1C1 S023 rationale:** appended dropped trailing sentence "The student is demonstrating engagement with the material and thoughtful analysis."
- **T1C1 S028 rationale:** appended dropped trailing sentence "The student is effectively using the framework to articulate a previously understood reality, which is a positive sign of engagement and learning."
- **T1C1 S031 rationale:** appended dropped trailing sentence "The submission demonstrates understanding of the core concept and is therefore not flagged as a wellbeing concern."
- **T1C1 S002 body text:** the scare-quoted phrase "late-hour fatigue" is now marked as researcher paraphrase ("dismissed the signal as late-hour fatigue (paraphrase; model wrote 'the late hour') and as 'engagement with course material'"). The second quoted phrase IS verbatim from the JSON; the first is now correctly framed.
- **T2C3 S022 rationale:** fixed punctuation drift — JSON has double-quoted `"distress"`; cell now also double-quotes it. The string literal was reflowed from `"..."` to `'...'` to allow embedded double quotes.
- **T2C2 S002 rationale:** removed the inserted "The " prefix — JSON opens "Student is thoughtfully engaging..." not "The student is...".

### Fix 2 — S029 12B Test O bracket fabrication + four other bracket fabrications (4-axis workshop) — **APPLIED**

In `4axis_iteration_workshop.html`:

- **S029 12B Test O (load-bearing):** "but it's also pos[sible the student is naming their processing style]" → "but it's also possible this is simply the student's typical writing style". This was the most substantively misleading fabrication (disability-affirming framing where the model actually used deficit-shaped framing).
- **S004 27B 0907:** "in the student's o[wn life]" → "in the student's or their mother's life."
- **S023 12B Test N ENGAGED:** "While th[e content is heavy]" → "While the content is sensitive"
- **S023 12B Test O:** "navigating a sy[stem that disregards her]" → "navigating a system that marginalizes her"
- **S029 27B 0907 Test N:** "thoug[h student is still engaging]" → "though the challenges are significant."

All bracket-completion fabrications now replaced with verbatim source text.

### Fix 3 — S031 12B count 8/9 → 9/10 (both 4-axis workshop AND 12B-vs-27B table) — **APPLIED**

Updated in five places:

- 4-axis workshop S031 anchor pattern note: "Pure 4-axis Gemma 12B Test N false-flags Marcus as BURNOUT **9/10**" (was 8/9).
- 4-axis workshop S031 Test N 12B cell heading: "**9/10** BURNOUT @ 0.7 — false positive" (was 8/9).
- 4-axis workshop S031 Test N 12B cell output box: "**9 runs** (2026-03-28): BURNOUT @ 0.70" (was 8 runs).
- 4-axis workshop S031 rationale body: "BURNOUT runs (**9/10**)... same value across **9 independent runs**" (was 8/9 / 8 runs). Source-line text also updated to clarify P1 vs P3 split.
- 12B-vs-27B table Test N "other students" cell + differential prose + S031 rationale block + S031 rationale-source line: all 8/9 references updated to 9/10 with prompt-variant context (the 1/10 ENGAGED is on prompt P3).

### Fix 4 — Test K row internal contradiction (12B-vs-27B table) — **APPLIED**

Selected the 03-29_1113 file as canonical source (the file whose rationale prose was already cited). Updated the 27B verdict cell:

- Verdict tag: "27B free = **6/10** (03-29 rerun)" (was "8/10 (best scoring model)")
- Score breakdown: structural 2, language-justice **1**, relational **2**, pedagogical **1**, anti-spotlighting 0 (matches the 03-29_1113.json scores exactly)
- Added explicit acknowledgment that the 03-28 run scored 8/10 with a different per-dimension breakdown (structural 2, language-justice 1, relational 3, pedagogical 2, anti-spotlighting 0) and "best scoring model" was true only on 03-28; on the 03-29 rerun, Step Flash beat 27B with 9/10.
- Rationale block heading updated: "03-29 rerun scored 6/10" (was "scored 8/10").
- Synthesis section's "Test K enhancement prose quality" paragraph updated to acknowledge both runs and the non-unidirectional comparison.

Note: the audit reported language-justice = 1 in BOTH files. The HTML's previous "language-justice 2" was unsupported by either JSON.

### Fix 5 — Test N rationale schema rendering (12B-vs-27B table) — **APPLIED**

In the S002 27B ENGAGED 1/6 outlier rationale block: `{axes: [ENGAGED], signal: ...}` → `{axis: ENGAGED, signal: ...}`. Test N's actual raw_output uses singular string-form `"axis": "ENGAGED"`, not list-form `"axes": ["ENGAGED"]` (Test O uses list-form; Test N does not).

I did NOT change the other Test N rationale renderings (S002 12B / S002 27B BURNOUT / S029 12B / S029 27B / S031 12B / S031 27B) — those already render with `{axis: ...}` singular. The S002 27B 1/6 ENGAGED block was the only Test N rendering using the Test O list-form schema. The Test O rationale blocks (S002 12B Test O, S002 27B Test O, etc.) correctly use `{axes: [...], ...}` and were not touched.

### Fix 6 — Prompt-variant tracking — **APPLIED**

Added a new H2 section "Test N system_prompt variants" at the top of `12B_vs_27B_differential_table_2026-05-11.html` (immediately after the preamble). The section contains:

- A table mapping P1-P5 to sha256 prefix, length, files, and distinctive content.
- A callout naming P3 (sha256 `93f4769a`) as the one prompt variant run on BOTH a 12B file (2026-03-29_2107) and a 27B file (2026-03-29_2109), with the controlled-comparison observation that both models produce ENGAGED on both S002 and S029 under that shared prompt.

Added inline `[Prompt variants: ...]` tags to:

- 12B-vs-27B Test N S002 row: 12B side (9× P1 + 1× P3), 27B side (2× P2 + 1× P3 + 1× P4 + 2× P5)
- 12B-vs-27B Test N S029 row: 12B side (9× P1 + 1× P3), 27B side (with P-ID for each file)
- 12B-vs-27B Test N "other students" row: both sides
- 12B-vs-27B Test N S031 source line: noted the 1/10 ENGAGED is on P3
- 4-axis workshop S002 12B Test N source line: 9 P1 + 1 P3 with cross-reference to the 12B-vs-27B table's prompt-variants section
- 4-axis workshop S023 12B Test N source line: noted that S023 1/10 CRISIS is on P3, NOT stochastic noise
- 4-axis workshop S029 27B Test N source line: noted BURNOUT FP is on P2 (the only prompt without identity-disclosure guard)
- 4-axis workshop S031 12B Test N source line: noted 9 runs on P1 + 1 ENGAGED outlier on P3

The binary workshop (`ablation_workshop.html`) was NOT updated with prompt-variant tags except where Test N evidence is cited inside its T2C2 cells — the rationale citations in T2C2 already point to specific JSON filenames, and the prompt-variant context lives in the 4-axis workshop and 12B-vs-27B table per audit recommendation. T2C2 S023 in binary workshop already correctly cites the 03-29_2107 file (which is the P3 outlier); leaving as-is preserves the cell's "representative of the misroute" framing.

### Fix 7 — Reframe prompt-difference claim in 12B-vs-27B table preamble — **APPLIED**

The inference-setup callout in the preamble was rewritten to acknowledge:

- 5 distinct Test N system_prompt versions across the 16 JSONs (not just one).
- ONE prompt (P3, sha256 `93f4769a`) was run on BOTH 12B and 27B. Under that shared prompt, the Finding A and Finding B differentials disappear.
- The Finding A "S029 worse on 27B" result is isolated to the 27B prompt variants WITHOUT the identity-disclosure guard (i.e., prompt P2).
- The "MATERIAL CONDITIONS … breaking through" clause is NOT 27B-only — it appears in 12B prompt P3 as well.

The S002 Test N row's `rationale-note` was rewritten to (a) tag prompt-variants for each verdict, (b) explicitly cite the P3 controlled comparison, (c) correct the earlier claim that the material-conditions clause is 27B-only.

The S029 Test N row's `rationale-note` was similarly rewritten — attributes the BURNOUT FP to the P2-only no-identity-guard configuration, names the P3 controlled comparison, corrects the 27B-only claim.

### Fix 8 — Footnotes for _2107 prompt-iteration artifact (4-axis workshop) — **APPLIED**

In `4axis_iteration_workshop.html`:

- S002 12B Test N source line: now describes the 9/10 byte-identical runs as on prompt P1, and the 10th (_2107) run as on P3 (the shared prompt with 27B). Replaced "near-identical" with "structurally different, shorter rationale that lacks the explicit fatigue-rejection clause" per audit recommendation.
- S023 12B Test N source line: now explicitly names the 1/10 CRISIS as the only 12B run on P3, not stochastic noise across the P1 distribution. Adds the cross-link to S031 1/10 ENGAGED (same file, same prompt).
- S031 12B Test N source line (already on a corrected count line): updated to indicate the 1/10 ENGAGED outlier is on prompt P3.

The 12B-vs-27B table's Test N "other students" cell footnote also names both 12B 1/10 outliers as the same-file (2026-03-29_2107) prompt-P3 effect, per audit recommendation.

---

## Prompt-variant P-ID mapping

| P-ID | sha256 prefix | length | Files | Distinctive content |
|------|---------------|--------|-------|---------------------|
| **P1** | `7ac35519` | 1459 | 9× Gemma 12B (all 2026-03-28: 1113, 1158, 1206, 1215, 1727, 1738, 1746, 1755, 1804) | Baseline 12B prompt. No "material conditions" clause; no "CRISIS supersedes ENGAGED"; no identity-disclosure guard. |
| **P2** | `4d2116b5` | 2204 | 2× Gemma 27B (2026-03-29_0907, 2026-03-29_1928) | First 27B prompt. Adds "MATERIAL CONDITIONS … breaking through and limiting their capacity"; adds "CRISIS supersedes ENGAGED". NO identity-disclosure guard. The 0907 file is the S029 BURNOUT FP (Finding A's 1/6 misclassification). |
| **P3** | `93f4769a` | 2918 | **1× 12B (2026-03-29_2107) + 1× 27B (2026-03-29_2109)** — only shared prompt | Adds "IDENTITY DISCLOSURE IS NOT A WELLBEING SIGNAL" guard on top of P2. Under this prompt both 12B and 27B return ENGAGED on S002 and on S029. Also produces 12B's 1/10 CRISIS on S023 (not present under P1) and 12B's 1/10 ENGAGED on S031 (against P1's uniform BURNOUT). |
| **P4** | `0dbf5713` | 3199 | 1× Gemma 27B (2026-03-29_2127) | Reformulated guard: "IDENTITY DISCLOSURE ALONE" + "Wellbeing signals require…". Still produces BURNOUT on S002. |
| **P5** | `d3e281bb` | 3987 | 2× Gemma 27B (2026-03-30_0034, 2026-04-01_1607) | Longest. Adds "MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE". The 04-01 file extends corpus to WB11–WB14. |

(Qwen 7B Test N file `test_n_4axis_submissions_qwen7b_2026-03-28_2338.json` is not part of the 12B-vs-27B comparison; its prompt was not hashed as part of this audit because the 12B-vs-27B table excludes Qwen.)

---

## New issues surfaced

Two items the audit didn't already note that I noticed during application:

1. **Binary workshop t1c1 S002 body had a second silent paraphrase issue beyond the audit's flagged "late-hour fatigue."** The body now reads as paraphrase-with-quoted-phrase ("dismissed the signal as late-hour fatigue (paraphrase; model wrote 'the late hour')"). The fix is conservative — it preserves the audit's framing convention but makes the attribution explicit.

2. **12B-vs-27B Test K row's "Other cloud models scored: Step Flash 9 (03-29 rerun)..." substring was internally inconsistent with the headline "8/10 best scoring model" because Step Flash 9 > 27B 8 in the rerun.** Fix 4 resolved this by switching the headline to the 03-29 rerun number (6/10) and naming Step Flash 9 as the rerun top scorer.

3. **The 4-axis workshop's S002 12B Test N body called the 10th run "near-identical"** — audit said this was misleading because the 2107 rationale is structurally different (lacks the fatigue-rejection clause). Fix applied per audit recommendation.

No NEW counter-evidence to existing audit findings surfaced. All applied fixes were either directly named in the audit notes or were the propagation of a named correction across linked cells.

---

## Confidence

**Tables ready for paper review.** All eight named fixes applied; prompt-variant tracking is now consistent across the three tables; the Test K, S031 count, schema-rendering, and prompt-confound framings now match raw JSON. The bracket fabrications (all five) are replaced with verbatim source text.

**Caveats for the author to know about:**

- I did not recompute SHA-256s independently — the P-ID mapping uses the prefixes already computed in `12B_vs_27B_verifier.md` (lines 36-41) and cross-referenced in `12B_vs_27B_disconfirmer.md` (lines 18-26). These two audits agree byte-for-byte on hashes, file membership, and lengths.
- The Test N S002 12B verbatim rationale (T2C2 in binary workshop) is from prompt P1 (file 1113); this is correctly attributed as "representative of 10/10 Gemma 12B runs" but a strict reader could note that the 10th run (2107, on P3) has a different rationale text. The 4-axis workshop now flags this explicitly; the binary workshop does not. Decision rests with author whether to propagate further.
- Test K row resolution (Fix 4) picked the 03-29_1113 source because the prose was already cited from that file. The 03-28 file's 8/10 score is now historicized as the earlier-run result. If author prefers the other direction (citing 03-28 score + 03-28 prose), that would require a parallel rewrite of the rationale block.
- All bracket-fabrication fixes used the audit's verbatim continuation text. I did not re-open the raw JSONs to triple-check; trusted the audit's character-by-character verification.
