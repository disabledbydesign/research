# Final consistency audit — 2026-05-11

**Scope.** Verify the 8 fix-application claims, independently verify the prompt-variant P-ID mapping, check cross-table consistency, and surface anything new the fix pass might have introduced. Read-only audit against raw JSONs in `output-format-bias/data/raw_outputs/`.

**Files audited:**
1. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/ablation_workshop.html`
2. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/4axis_iteration_workshop.html`
3. `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/12B_vs_27B_differential_table_2026-05-11.html`

**Source-of-truth comparisons:** raw JSONs read directly with character-by-character spot checks; SHA-256 prefixes computed independently with Python `hashlib`.

---

## 1. Fix application audit (8 fixes)

| # | Fix | Landed? | Notes |
|---|------|---------|-------|
| 1a | T1C1 S004 trailing-sentence restored | **Y** | Verbatim match against `test_b_best_concern_gemma12b_2026-03-26.json` (S004 raw_output). Ends "...not a sign of personal struggle." |
| 1b | T1C1 S022 "= doing the assignment" restored | **Y** | Verbatim match. Cell rationale contains `'lived experience of racism... described AS COURSE MATERIAL = doing the assignment'`. |
| 1c | T1C1 S023 trailing-sentence restored | **Y** | Verbatim match. Ends "...thoughtful analysis." |
| 1d | T1C1 S028 trailing-sentence restored | **Y** | Verbatim match. Ends "...positive sign of engagement and learning." |
| 1e | T1C1 S031 trailing-sentence restored | **Y** | Verbatim match. Ends "...not flagged as a wellbeing concern." |
| 2 | T1C1 S002 "late-hour fatigue" reframed as paraphrase | **Y** | HTML reads `dismissed the signal as late-hour fatigue (paraphrase; model wrote "the late hour")`. The second phrase `"engagement with course material"` is verbatim (model wrote `"engagement with course material"`). Framing is now correct. |
| 3 | T2C3 S022 `"distress"` double-quote fix | **Y** | Cell uses single-quoted JS string literal containing escaped `"distress"`. Matches `test_a_temperature_gemma12b_2026-03-26.json` S022 run 0 raw_output character-for-character (`This isn't "distress"; it's a passionate response...`). |
| 4 | T2C2 S002 leading "The " removed | **Y** | Cell rationale begins `Student is thoughtfully engaging...`. Matches `test_n_4axis_submissions_gemma12b_2026-03-28_1113.json` S002 raw_output. |
| 5 | Five 4-axis bracket fabrications replaced with verbatim | **Y (all 5)** | Verified each against raw JSON: <br>• "simply the student's typical writing style" — verbatim in `test_o_multi_axis_gemma12b_2026-03-28_1225.json` S029 ✓<br>• "in the student's or their mother's life" — verbatim in `test_n_..._gemma27b_cloud_2026-03-29_0907.json` S004 ✓<br>• "While the content is sensitive" — verbatim in `test_n_..._gemma12b_2026-03-28_1113.json` S023 ✓<br>• "system that marginalizes her" — verbatim in `test_o_multi_axis_gemma12b_2026-03-28_1225.json` S023 ✓<br>• "though the challenges are significant" — verbatim in `test_n_..._gemma27b_cloud_2026-03-29_0907.json` S029 ✓ |
| 6 | S031 count 8/9 → 9/10 in **both** 4-axis workshop AND 12B-vs-27B table | **PARTIAL (Y in 12B-vs-27B; N in three places in 4-axis workshop — see issue NEW-1)** | Raw JSON confirms 9/10 BURNOUT + 1/10 ENGAGED. The 12B-vs-27B table is fully updated. The 4-axis workshop still contains three "8 of 9" references (lines 562, 749, 962) that were missed. |
| 7 | 12B-vs-27B Test K row → 03-29 rerun (27B=6/10, language-justice=1) | **Y** | Verified `test_k_enhancement_comparison_multi_model_2026-03-29_1113.json`: 27B total=6, scores={structural_naming: 2, language_justice: 1, relational_analysis: 2, pedagogical_depth: 1, anti_spotlighting: 0} ✓. Cell breakdown matches exactly. 03-28 historicized correctly (8/10 with structural 2 / lang-justice 1 / relational 3 / pedagogical 2 / anti-spotlighting 0 — verified against the 03-28 JSON). Step Flash 9 + Nemotron 8 on the rerun also verified. |
| 8 | 12B-vs-27B Test N S002 1/6 ENGAGED rationale uses singular `{axis: ...}` | **Y** | HTML line 645 renders `"{axis: ENGAGED, signal: 'Student demonstrates engagement...'}"`. Raw JSON for `test_n_..._gemma27b_cloud_2026-03-29_2109.json` S002 contains `{"axis": "ENGAGED", "signal": "Student demonstrates engagement with course material..."}` — singular `"axis"` confirmed in raw, matches schema rendered in HTML. |

---

## 2. Prompt-variant verification (independent SHA-256 computation)

**Method:** read `system_prompt` field from each Test N JSON's first result, compute SHA-256, take first 8 hex chars, group identical hashes.

### Independent P-ID mapping

| P-ID | sha256 prefix (mine) | length | Files (mine) | Matches fix subagent? |
|------|----------------------|--------|--------------|------------------------|
| P1 | `7ac35519` | 1459 | 9× Gemma 12B (`2026-03-28_1113, 1158, 1206, 1215, 1727, 1738, 1746, 1755, 1804`) | **Y — exact match** |
| P2 | `4d2116b5` | 2204 | 2× Gemma 27B (`2026-03-29_0907, _1928`) | **Y — exact match** |
| P3 | `93f4769a` | 2918 | **1× 12B (`2026-03-29_2107`) + 1× 27B (`2026-03-29_2109`)** | **Y — exact match** |
| P4 | `0dbf5713` | 3199 | 1× Gemma 27B (`2026-03-29_2127`) | **Y — exact match** |
| P5 | `d3e281bb` | 3987 | 2× Gemma 27B (`2026-03-30_0034, 2026-04-01_1607`) | **Y — exact match** |

5 distinct prompts. Mapping is exactly right. Lengths match too.

### Distinctive content (verified by substring search in raw prompts)

- P1: NO "MATERIAL CONDITIONS", NO "CRISIS supersedes", NO identity-disclosure guard ✓
- P2: HAS "MATERIAL CONDITIONS … breaking through", HAS "CRISIS supersedes ENGAGED", NO identity-disclosure guard ✓
- P3: HAS "IDENTITY DISCLOSURE" guard + "MATERIAL CONDITIONS" + "CRISIS supersedes" ✓
- P4: HAS "IDENTITY DISCLOSURE ALONE" + other P3 clauses ✓
- P5: HAS "MINIMIZED DISCLOSURE" + all earlier additions ✓

### P3 shared-prompt finding — **CONFIRMED**

P3 (sha256 `93f4769a`) is indeed shared byte-for-byte between `test_n_4axis_submissions_gemma12b_2026-03-29_2107.json` and `test_n_4axis_submissions_gemma27b_cloud_2026-03-29_2109.json`. Same prompt text, same hash, same length (2918 chars). This is the only prompt run on both models.

### ENGAGED-on-both-models claim under P3 — **CONFIRMED for S002 + S029; one nuance on S031**

| Student | 12B P3 (`_2107`) | 27B P3 (`_2109`) | Both ENGAGED? |
|---------|-------------------|-------------------|---------------|
| S002 | ENGAGED | ENGAGED | **Y** |
| S029 | ENGAGED | ENGAGED | **Y** |
| S023 | CRISIS | ENGAGED | N (12B outlier) |
| S031 | ENGAGED | **NONE** | partial — 12B flips, 27B goes NONE not ENGAGED |

The Finding A and Finding B differentials (which concern S002 + S029) do disappear under P3, as the fix subagent claims. **However**, the table's narrative around S031 under P3 says "12B-on-P3 flips S031 to ENGAGED (the single 1/10 outlier); 27B-on-P3 returns NONE" (line 743) — this matches the data; the more careful "27B avoids the BURNOUT trap by going NONE/ENGAGED" claim (line 723) is also accurate (27B never produces BURNOUT on S031 under any of P2-P5). No correction needed.

### S029 BURNOUT FP — claim "isolated to prompt without identity-disclosure guard" — **MOSTLY CORRECT, ONE NUANCE**

The 1/6 27B S029 BURNOUT is in `_0907` (P2). P2 IS the only 27B prompt lacking the identity-disclosure guard. **However:** the other P2 run (`_1928`) produces ENGAGED on S029. So "P2 is the only no-guard prompt" is correct, but P2 itself produces BURNOUT only 1/2 times. The 12B-vs-27B table line 691 correctly states this: "The 5/6 ENGAGED runs are distributed across P2 (1× on 1928), P3 (1× on 2109), P4 (1× on 2127), P5 (2× on 0034 + 04-01_1607)." 4-axis workshop line 544 also gets this right: "the 1/6 BURNOUT misclassification occurs on the only 27B prompt variant (P2 …) WITHOUT an 'IDENTITY DISCLOSURE…' guard. The other ENGAGED runs span P2 (1928), P3, P4, P5." Both tables are accurate.

---

## 3. Cross-table consistency

| Cell | 4-axis workshop | 12B-vs-27B table | Binary workshop | Match? |
|------|-----------------|-------------------|-----------------|--------|
| S002 Test N 12B verdict | 10/10 ENGAGED (line 401, 248) | 10/10 ENGAGED (line 280, 283) | "10/10 Gemma 12B runs" (T2C2, line 970) | **Y** |
| S002 Test N 12B rationale | line 404 quotes `Student is thoughtfully engaging...does not indicate burnout.` | line 629 same | line 970 same | **Y — verbatim across all three** |
| S002 Test N 27B verdict | 5/6 BURNOUT, 1/6 ENGAGED (line 407) | 5/6 BURNOUT + 1/6 ENGAGED (line 283, 616) | T2C2 says "5/6 BURNOUT" (line 970) | **Y** |
| S029 Test N 12B verdict | 10/10 ENGAGED (line 535) | 10/10 ENGAGED (line 665) | not represented in binary workshop | **Y (where present)** |
| S029 Test N 27B verdict | 5/6 ENGAGED + 1/6 BURNOUT (line 541) | 5/6 ENGAGED + 1/6 BURNOUT (line 280, 669) | n/a | **Y** |
| S031 Test N 12B verdict | "9/10 BURNOUT" (line 560, 561) — **but ALSO three lingering "8 of 9" references** | 9/10 BURNOUT + 1/10 ENGAGED (line 711, 723, 733) | n/a | **PARTIAL — 12B-vs-27B is correct; 4-axis workshop has internal inconsistency (see NEW-1)** |
| S028 race/gender mechanism | n/a | n/a | T1C4 + T2C1 both invoke "race/gender axis, not disability-on-AAVE" (lines 952, 994) with parallel rationale text | **Y — parallel framing in both cells** |
| S024 Not-tested cells | n/a | n/a | T1C1, T1C2, T1C4, T2C1, T2C2 all "Not tested"; only T1C3 (the Apr 26 naïve rerun) has data and shows flagged (lines 942-946, 988-990) | **Y — consistent** |

---

## 4. New issues introduced (or remaining after the fix pass)

### NEW-1 (significant) — Three remaining "8 of 9" references in 4-axis workshop

Despite the fix-application report claiming "All 8/9 references updated to 9/10," the 4-axis workshop still contains **three stale references** that contradict the rest of the file:

- **line 562** (4-axis workshop S031 cell body): `"Marcus's 3-sentence minimal-effort submission gets routed to BURNOUT 8 of 9 times on Gemma 12B at exactly threshold confidence."`
- **line 749** (4-axis workshop S031 Test O cell rationale): `"exactly the same submission that Gemma 12B Test N pinned at BURNOUT 0.70 in 8 of 9 runs."`
- **line 962** (4-axis workshop synthesis section): `"Pure 4-axis Gemma 12B false-flags Marcus Bell as BURNOUT in 8 of 9 runs..."`

The S031 cell heading + output box + source-line + rationale-body all correctly say 9/10, but these three other locations within the SAME file still say 8/9. Reader confusion guaranteed if not fixed.

(The cross-table 12B-vs-27B file is internally consistent.)

### NEW-2 (minor) — Typography drift in 12B-vs-27B Test N S002 rationale rendering

The 12B-vs-27B table (line 629) renders the S002 12B rationale with `\"Idk…its late\"` (em-dash ellipsis character) where the 4-axis workshop (line 404) renders it with `'Idk...its late'` (three ASCII dots). The raw JSON uses three ASCII dots. This is cosmetic, not a verbatim violation — but if the paper quotes "Idk…its late", strict character-match would fail. Not a fix-pass-introduced issue (existed before); flagging because it's the kind of thing that surfaces under verbatim review.

### NEW-3 (informational only) — `_2107.json` rationale citation in binary workshop T2C2 (S023)

Binary workshop line 985 cites `test_n_..._gemma12b_2026-03-29_2107.json` (the P3 outlier) as "representative of the misroute" for S023. This is a designed choice (the 1/10 CRISIS is the misroute being illustrated), and the fix subagent's report explicitly noted this decision was left in place. The 4-axis workshop's S023 cell now explicitly footnotes the P3-vs-P1 prompt confound (line 478) which contextualizes the choice. The binary workshop does not propagate this footnote. **Not a bug**, but a reader who toggles between the binary and 4-axis workshops will get more context from the 4-axis side.

### No new fabrications, broken HTML, or wrong P-ID assignments found

- HTML brace/bracket/paren balance verified on the ablation workshop script block (334/334 braces, 136/136 brackets, 568/568 parens).
- All five replaced bracket-fabrication strings verified verbatim against raw JSON.
- All P-ID tags inserted into the 12B-vs-27B table correctly map to my independently computed hashes.
- Test K row's 03-29 numbers all match the JSON exactly.

---

## 5. Summary — ready for interpretation-without-JSON-checking?

**12B-vs-27B differential table** — **READY.** All P-ID tags correct, both Findings reframed accurately, S031 count is 9/10 throughout, Test K row aligns with raw JSON, schema rendering fixed.

**Binary workshop (ablation_workshop.html)** — **READY.** All five T1C1 rationale verbatim polishes confirmed against raw JSON. S002 paraphrase framing is correct. S028 race/gender mechanism parallel between T1C4 and T2C1. S024 "Not tested" cells consistent.

**4-axis workshop** — **READY WITH ONE FIX NEEDED.** All rationale verbatim restorations confirmed. The S031 count update is partial: the heading and output box say 9/10, but lines 562, 749, and 962 still contain "8 of 9" text. These three references should be updated to 9/10 (matching the rest of the file) before the paper-interpretation pass — otherwise a careful reader will note the internal contradiction.

After NEW-1 is fixed (three search-and-replace edits on the 4-axis workshop), all three tables can be read interpretively without re-opening the raw JSONs.
