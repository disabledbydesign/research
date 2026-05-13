# 12B-vs-27B differential table — disconfirmer audit (2026-05-11)

Audit target: `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/12B_vs_27B_differential_table_2026-05-11.html`
Source JSONs: `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/`

---

## 1. Prompt-difference falsification attempt (highest priority)

**Method.** Inspected the `system_prompt` field of every result inside all 10 Gemma-12B Test N JSONs and all 6 Gemma-27B Test N JSONs. Hashed each system_prompt; reconciled against actual S002/S029 verdicts per file.

**The earlier subagent's framing — "12B Test N system prompt and 27B Test N system prompt are NOT identical" — is FALSIFIED as stated, but a more complex confound IS real.** Specifically:

### Within-model prompt heterogeneity (the table hides this)

The "n=6 27B runs" are NOT 6 runs of the same prompt. They use **4 different system prompts** across 6 files:

| File | sysprompt hash | len | S002 | S029 |
|---|---|---|---|---|
| `gemma27b_cloud_2026-03-29_0907` | 4d2116b5 | 2204 | BURNOUT@0.80 | **BURNOUT@0.85** |
| `gemma27b_cloud_2026-03-29_1928` | 4d2116b5 | 2204 | BURNOUT@0.85 | ENGAGED@0.90 |
| `gemma27b_cloud_2026-03-29_2109` | **93f4769a** | 2918 | **ENGAGED@0.90** | ENGAGED@0.90 |
| `gemma27b_cloud_2026-03-29_2127` | 0dbf5713 | 3199 | BURNOUT@0.80 | ENGAGED@0.90 |
| `gemma27b_cloud_2026-03-30_0034` | d3e281bb | 3987 | BURNOUT@0.80 | ENGAGED@0.90 |
| `gemma27b_cloud_2026-04-01_1607` | d3e281bb | 3987 | BURNOUT@0.80 | ENGAGED@0.90 |

Similarly the "10 12B runs" use **2 different prompts**: 9 files of hash 7ac35519 (len 1459) and 1 file (`gemma12b_2026-03-29_2107`) of hash 93f4769a (len 2918).

### The cross-model identical-prompt control case the table omits

Hash **93f4769a** appears in BOTH a 12B file (03-29_2107) AND a 27B file (03-29_2109). Same prompt, both models. Both return:
- S002 → ENGAGED (12B@0.95, 27B@0.90)
- S029 → ENGAGED (12B@0.95, 27B@0.90)

**This is a direct prompt-controlled 12B-vs-27B comparison and the table does not mention it.** Under the strongest prompt-with-identity-disclosure-guard, BOTH models agree on BOTH equity-critical cases. Under that prompt the S002 BURNOUT recovery (Finding B) disappears AND the S029 BURNOUT FP (Finding A) disappears.

### Verdict on the prompt-confound footnote

The table's rationale-note for the S002 row says: *"The 27B BURNOUT verdicts explicitly cite 'material conditions' / 'time constraints impacting ability to complete work' — that vocabulary comes from the 27B-only prompt revision."*

That's **wrong on two grounds:**
1. The "MATERIAL CONDITIONS… breaking through and limiting their capacity" clause IS in the 12B 03-29_2107 prompt (hash 93f4769a). It is NOT 27B-only.
2. The 27B BURNOUT verdicts persist across prompts WITHOUT that vocabulary too (the 0907/1928 prompt 4d2116b5 also has it, but 2127 with prompt 0dbf5713 returns BURNOUT on S002 with "abandons BURNOUT" reasoning that doesn't quote the material-conditions wording).

The more accurate statement is: the 27B 03-29_0907 run that misclassifies S029 used the WEAKEST 27B prompt (the only 27B prompt without an "IDENTITY DISCLOSURE IS NOT A WELLBEING SIGNAL" guard). The S029 FP rate is 1/6 because 5 of 6 runs used prompts WITH that guard. The "5/6 BURNOUT" on S002, by contrast, is robust across prompt variations (the only ENGAGED 27B-on-S002 run is the one that used the same prompt 12B used).

### Did the subagent confuse system_prompt with raw_output?

No. The quoted "MATERIAL CONDITIONS… limiting their capacity" string is present in the actual `system_prompt` field of result items in 27B 0907/1928 files (verified). The subagent didn't confuse fields.

### Did the subagent compare different tests?

No. All compared files are `test_n_4axis_submissions_*`.

### Was there a third (Qwen 7B) variant the subagent ignored?

Yes — `test_n_4axis_submissions_qwen7b_2026-03-28_2338.json` exists but is not referenced anywhere in the 12B-vs-27B table. Not a category error in the table's claim, but a noted omission.

**Bottom line on prompt difference: PARTIALLY CONFIRMED but the table OVERSTATES one side and HIDES the within-model heterogeneity that is the real story.** The cleanest takeaway is that under the same prompt (93f4769a), 12B and 27B agree on both equity-critical cases; the headline "12B-vs-27B differential" on Test N is at least as much a prompt-effect as a model-scale effect.

---

## 2. Per-row falsification attempts

### Row: Test N S002 burnout TP

**Verdict cells.**
- "12B 10/10 ENGAGED" — VERIFIED (all 10 files return ENGAGED on S002).
- "27B 5/6 BURNOUT, 1/6 ENGAGED" — VERIFIED at the file level (5 BURNOUT, 1 ENGAGED). BUT: the 5 BURNOUT runs span 3 different prompts and the 1 ENGAGED run uses the same prompt the 12B 03-29_2107 file uses. This is hidden by the n=6 framing.

**Cherry-picking check.** The rationale-cell quotes the 27B BURNOUT rationale from `gemma27b_cloud_2026-03-29_0907.json` — that file's S002 verdict is BURNOUT@0.80 (matches the cell's claim "5 runs BURNOUT @ 0.80-0.85"). However, the rationale signal is REPRESENTED as `{axis: BURNOUT, signal: ..., confidence: 0.80}` with stylized formatting (no quotes); the actual raw_output is `{"axis": "BURNOUT", "signal": "Brief, unfinished thought; mentions lateness suggesting time constraints impacting ability to complete work. Focus is on applying course concepts, not personal crisis.", "confidence": 0.8}` — content matches verbatim.

### Row: Test N S029 neurodivergent

- "12B 10/10 ENGAGED" — VERIFIED (all 10 12B files return ENGAGED on S029).
- "27B 5/6 ENGAGED, 1/6 BURNOUT" — VERIFIED.
- "Raw reasoning strips 'exhausting' from its prepositional phrase" — VERIFIED verbatim against `gemma27b_cloud_2026-03-29_0907.json` S029 raw_output.

**Style drift.** The table renders the rationale as `{axis: ENGAGED, signal: '...', confidence: 0.90}` (smart quotes, no JSON quoting). The actual JSON is `{"axis": "ENGAGED", "signal": "...", "confidence": 0.9}`. Stylistic flattening only, not a content error.

### Row: Test N — other students

- S004 / S022 / S028 cross-model agreement — VERIFIED (all files return ENGAGED@0.95).
- S023: "12B 9/10 ENGAGED, 1/10 CRISIS @ 0.95 (FP)" — VERIFIED. The 1/10 CRISIS is in file `gemma12b_2026-03-29_2107` — which is also the 12B file using the DIFFERENT prompt (hash 93f4769a). **The S023 12B FP is not random variance — it covaries with the prompt change.** The table doesn't acknowledge this.
- S023 27B: "6/6 ENGAGED" — VERIFIED.
- **S031 12B: table says "8/9 BURNOUT @ 0.70 (FP at threshold), 1/9 ENGAGED" — WRONG.** Across all 10 12B files: 9 return BURNOUT, 1 (file 03-29_2107) returns ENGAGED. That's 9/10, not 8/9. The "n=9" framing also disagrees with the table's own header column ("12B n=10 runs"). Likely off-by-one or a miscount.
- S031 27B: "4/6 NONE, 2/6 ENGAGED" — VERIFIED (files 0907/1928/2109/0034 = NONE; 2127/04-01_1607 = ENGAGED).

### Row: Test K — enhancement-tier prose quality

**Major falsifications:**

1. **Verdict-tag "27B free = 8/10 (best scoring model)" is FALSE on the 03-29 rerun.**
   - File `test_k_enhancement_comparison_multi_model_2026-03-28.json`: gemma27b_free total_score = 8 (structural 2, language_justice **1**, relational **3**, pedagogical 2, anti_spotlighting 0).
   - File `test_k_enhancement_comparison_multi_model_2026-03-29_1113.json`: gemma27b_free total_score = **6** (structural 2, language_justice 1, relational 2, pedagogical 1, anti_spotlighting 0). NOT 8.
2. **The table's score breakdown ("structural 2, language-justice 2, relational 2-3, pedagogical 2, anti-spotlighting 0") matches NEITHER file exactly.** Language-justice is 1 in both files, not 2. The table fabricates or guesses the language-justice score.
3. **"Best scoring model" is FALSE on the rerun.** In 03-29_1113: step_flash_free scored 9, nemotron_120b_free scored 8 — both higher than gemma27b_free's 6. In 03-28: 27B at 8 tied for top with no model above. The table's verdict-tag conflates the two files.
4. **The rationale source is cited as `test_k_enhancement_comparison_multi_model_2026-03-29_1113.json` — the file where 27B scored 6, not 8.** So either the score is wrong or the rationale source is wrong.

### Row: Test P two-pass

- "12B-only, 7 JSONs" — VERIFIED (7 files matching `test_p_two_pass_gemma12b_2026-03-28_*`).
- "No 27B Test P run exists" — VERIFIED (no `test_p_two_pass_gemma27b_*` files).

### Row: Test Q 27B probes

- "File 1 (n=4): 1 BURNOUT + 3 ENGAGED" — VERIFIED (axis counts).
- "File 2 (n=6): 2 BURNOUT + 4 ENGAGED" — VERIFIED.
- "No 12B counterpart" — no `test_q_12b_*` files found; VERIFIED.

### Row: Live-data runs

- FERPA-blocking-cloud reasoning IS documented in `output-format-bias/comparison_analysis.md` and `DEVELOPMENT.md`. The table's "FERPA structural barrier" claim is supported (not inferred).

---

## 3. Comparison-gap stress-test

- **Test P 12B-only**: confirmed. No 27B Test P file exists in `data/raw_outputs/`.
- **Test Q 27B-only**: confirmed. No 12B Test Q file exists.
- **Live-data 12B-only**: confirmed; FERPA rationale documented.

---

## 4. Rationale-pair drift check

### Test N S002 pair

- 12B rationale cited from `test_n_4axis_submissions_gemma12b_2026-03-28_1113.json` — verified the file returns ENGAGED@0.95 on S002 with the quoted signal text.
- 27B rationale cited from `test_n_4axis_submissions_gemma27b_cloud_2026-03-29_0907.json` — verified BURNOUT@0.80 on S002 with the quoted signal text.
- **Format-drift issue:** the table renders Test N rationales as `{axes: [ENGAGED], signal: ..., confidence: 0.90}` (list-form) in the "1/6 ENGAGED" 27B note. The actual Test N raw_output uses singular `{"axis": "ENGAGED", ...}` (string-form, NOT a list). Test N is single-label, NOT multi-axis. The list-form rendering visually conflates Test N with Test O — a real content-drift error in the rationale rendering, even if the verbal content matches.

### Test N S029 pair

- 12B and 27B rationale sources verified verbatim.
- 12B "byte-identical across 10 runs" claim — VERIFIED for S029 across the 9 early files (single SHA hash) BUT the 10th file (03-29_2107) is a different prompt and returns confidence 0.95 instead of 0.90, so the "all 10 runs byte-identical" framing is wrong — it's 9 byte-identical + 1 prompt-variant run with same axis but different confidence.

### Test N S031 pair

- 12B rationale from 03-28_1113 BURNOUT@0.70 verified.
- 27B rationale from 03-29_0907 NONE@0.95 verified.
- The "12B reads 'idk what else to say' as burnout signal" interpretation is plausible-but-arguable; the quoted signal doesn't actually contain the words "idk what else to say" — that's the table interpreting the input student writing, not quoting the model's signal text. Minor framing issue.

### Test O pair

- Both rationale sources verified verbatim.
- `axes: [ENGAGED, CHECK-IN]` list-form is CORRECT for Test O (multi-axis).

### Test E pair

- Confirmed `reference_model` field = `gemma-3-12b-it-4bit` in both Test E files — table's "Test E uses Test A's 12B data as reference" claim is verified.

---

## 5. Errors found — ranked by severity

### Severity 1 (paper-shaping)

**E1. Prompt-confound footnote misframes the prompt heterogeneity.** The table footnote presents the 12B vs 27B prompt difference as a single-direction confound ("27B got a different system prompt"). The data show 4 distinct 27B prompts and 2 distinct 12B prompts across the Test N runs, with **one prompt (93f4769a) shared across both models** — and under that shared prompt, both models agree on S002 (ENGAGED) and S029 (ENGAGED), making the headline differential disappear. This is the most paper-consequential finding of the audit and the table should be revised to acknowledge it.

**E2. Test K verdict-tag is internally contradictory.** "27B free = 8/10 (best scoring model)" is true for the 03-28 file, false for the 03-29 rerun (where 27B = 6/10 and step_flash scored 9). The rationale-pair cites the 03-29 file. Either the score (8) is from the wrong file or the rationale is from the wrong file. The score breakdown (language-justice = 2) doesn't match either file (both have language-justice = 1).

### Severity 2 (verifiable content errors)

**E3. S031 12B count is off-by-one.** Table says "8/9 BURNOUT, 1/9 ENGAGED." Actual: 9/10 BURNOUT, 1/10 ENGAGED. The "n=9" doesn't match the header "12B n=10 runs" in the same row.

**E4. Test N rationale rendering uses Test-O list-form syntax.** Table renders S002 and S029 Test N rationales as `{axes: [ENGAGED], ...}` (list-form) when the actual raw_output uses `{"axis": "ENGAGED", ...}` (string-form). Test N is forced-single-label; the list-form visual conflates it with Test O multi-axis. Substantive content matches verbatim, but the syntax misrepresents the data structure of the test.

**E5. "10 runs byte-identical" wording is wrong.** The 12B Test N rationale-cell footer says "all 10 runs byte-identical at temp 0.3." Verified: 9 of 10 are byte-identical; the 10th (03-29_2107) uses a different prompt and returns the same axis at slightly different confidence. Trivial drift but factual error.

### Severity 3 (interpretive issues that survive but should be hedged)

**E6. The S023 12B 1/10 CRISIS is not stochastic noise.** It occurs only in the one 12B run with the different prompt. The table presents it as 12B variability; the data show it covaries with the prompt change. Same caveat as E1.

---

## 6. Statements that survive adversarial reading

- 12B Test N S002: 10/10 ENGAGED across all files. VERIFIED.
- 12B Test N S029: 10/10 ENGAGED across all files. VERIFIED (correct on the protected case).
- 27B Test N S002: 5/6 BURNOUT, 1/6 ENGAGED. File-level counts VERIFIED.
- 27B Test N S029: 5/6 ENGAGED, 1/6 BURNOUT. File-level counts VERIFIED.
- 27B Test N: bidirectional instability claim is true at the file level (instability runs both directions).
- Test P 12B-only and Test Q 27B-only structural comparison gaps: VERIFIED.
- Live-data 12B-only with FERPA structural barrier: VERIFIED with documentation support.
- Test Q probe counts (3/10 BURNOUT, 7/10 ENGAGED across counterfactuals): VERIFIED.
- Test E reference_model claim: VERIFIED.
- Test O S002 [ENGAGED, CHECK-IN] forced-choice-recovery claim: VERIFIED verbatim against both files.
- Round 3 replication-study attribution to BINARY pipeline (not 4-axis): preamble distinction is correct and important — the table's effort to separate Finding A (Test N S029) from the Round 3 replication 80%-vs-100% is well-founded.

---

## 7. Summary

**Prompt-difference falsification result: PARTIALLY CONFIRMED but reframed.** A prompt difference exists, but the table's framing is wrong in two directions: (1) it presents the 12B and 27B prompts as two monoliths when in fact there are 2 distinct 12B prompts and 4 distinct 27B prompts across the Test N runs, and (2) it doesn't notice that one prompt (hash 93f4769a) is shared across a 12B file (03-29_2107) and a 27B file (03-29_2109), and under that shared prompt both models agree on both equity-critical cases — which collapses the headline differential. The "27B-only material-conditions vocabulary" claim is straightforwardly wrong: that clause is present in the 12B 03-29_2107 prompt too.

The Test K row is independently broken: the "8/10 best scoring model" verdict-tag is true for the 03-28 file but the rationale is sourced from the 03-29 rerun where 27B scored 6 and step_flash scored 9. Score breakdown numbers don't match either file. The S031 12B count is off-by-one (8/9 should be 9/10). Test N rationales are rendered in Test-O multi-axis syntax which misrepresents the data structure. The Test N S002 / S029 row-level counts survive falsification, as do the Test P / Test Q / live-data structural gaps and the Round 3 replication-vs-Test-N preamble distinction.

The honest paper-scope claim is even narrower than the table's closing callout: not "Gemma 27B cloud on Test N at temp 0.3" but "Gemma 27B cloud on Test N at temp 0.3 under the four distinct prompt variants used across the n=6 runs, with the BURNOUT-on-S029 FP isolated to the only prompt variant without an explicit identity-disclosure guard."
