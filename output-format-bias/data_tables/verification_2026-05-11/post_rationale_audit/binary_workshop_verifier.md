# Binary ablation workshop — post-rationale audit (verifier / count-first lens)

**Audit target:** `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/ablation_workshop.html`
**Date:** 2026-05-11
**Verifier focus:** count-first / confirmation lens. Confirms what the data supports; flags only where source disagrees with the rendered claim.
**Method:** Read all `DEFAULT_CELLS.t1` and `DEFAULT_CELLS.t2` content in the HTML, then opened each cited raw JSON and verified verdicts + rationale text character-by-character.

---

## 1. Verdict-accuracy audit table

Cells covered: the 15 morning-punch-list corrections, the newly-flagged T2C2 S024 cell, and a 10-cell random sample of the other 30 rationale-only cells.

| Cell ID | Verdict shown (heading) | Raw JSON value | Match | Note |
|---|---|---|---|---|
| **CORRECTED CELLS (15 + 1)** ||||
| T1C1 S002 | "24/24 Clear — missed TP" body: "dismissed as late-hour fatigue" | S002 cleared in Tests B (3/3), C (3/3 — sole run also CLEAR), F (3-27 9/9, 3-28 9/9). 24/24 CLEAR confirmed. Model body verbatim says "The 'Idk' and abrupt ending are likely due to the late hour…" — dismissal framing matches | Y | Tier 3 item 12 correctly applied. Body now describes what the model actually does. |
| T1C1 S023 | "24/24 Clear" body: "Race axis protected." | 24/24 CLEAR in Tests B/C/F. Model never reasons about language. | Y | Tier 3 item 13 applied. "/ language" dropped. |
| T1C2 S022 | "3/3 Flagged at 0.4 confidence" — full sentence "…deprivation and lack of access to essential resources." | Test R: S022 flagged 3/3 at conf 0.4; why_flagged ends "…food security or access to quality education." (full sentence even longer than the cell's restored quote). Cell body now ends at the first sentence boundary "…essential resources." which is faithful to a sentence boundary in JSON. | Y | Tier 4 item 14 applied — the cell body no longer truncates at "deprivation." |
| T1C2 S023 | "3/3 Clear" body: "Lived experience cleared." | Test R: S023 cleared 3/3. | Y | Tier 4 item 15 applied — body text correctly attributes pattern. |
| T1C3 S023 | "Flagged" body: "Lived-experience writing false-flagged at confidence 0.7. Model reasons about vocabulary / intellectual struggle…" | rerun_original_naive_concern S023 = FLAG, conf 0.7, why_flagged = "The student is grappling with a complex concept (intersectionality) but is unsure of the terminology…" | Y | Tier 4 item 16 attribution swap applied — S023's flag is now correctly framed as intellectual-struggle, not the self-contradiction quote. |
| T1C3 S024 | "Flagged" body: 'Lived-experience writing false-flagged at confidence 0.8. Model names "not a direct wellbeing concern" then flags anyway' | rerun_original_naive_concern S024 = FLAG, conf 0.8, why_flagged starts "This passage powerfully articulates a sense of dehumanization…While not a direct wellbeing concern…" | Y | Tier 4 item 16 — "self-contradiction" quote now correctly attributed to S024. |
| T1C4 S024 | "Not tested" body: "S024 absent from test_m_production_detector…" | Test M JSON contains S002, S004, S022, S023, S028, S029, S031 + WB01–WB10 (17 records). S024 absent. | Y | Tier 2 item 8 applied. |
| T2C1 S024 | "Not tested" — same text as T1C4 | Same JSON, same absence. | Y | Tier 2 item 8 applied. |
| T1C4 col note | "Test M · n = 17 records (7 corpus students + 10 synthetic wellbeing cases), not the full 32-student corpus…" | Test M = 17 records, 7 corpus + 10 WB synthetic. | Y | Tier 2 item 9 applied. |
| T2C1 col note | Same text as T1C4 | Same. | Y | Tier 2 item 9 applied. |
| T1C4 S028 | "Flagged" body: "Flagged at confidence 0.70 (at threshold). Model's rationale invokes race/gender axis, not disability-on-AAVE as workshop previously framed." | Test M S028 = flagged, conf 0.7. why_flagged: "This passage highlights a potential issue of differential treatment by teachers based on race and gender…" | Y | Tier 3 item 11 applied — mechanism narrative corrected. |
| T2C1 S028 | Same text + heading "Flagged — see Table 1" | Same. | Y | Tier 3 item 11 applied. |
| T2C2 S031 | "Designed edge-case probe — minimal effort" — Gemma 12B 9/10 BURNOUT, 27B NONE 4/6 ENGAGED 2/6, Qwen 1/1 ENGAGED | Across 17 Test N JSONs: Gemma 12B S031 = BURNOUT 9 + ENGAGED 1; Gemma 27B = NONE 4 + ENGAGED 2; Qwen 7B = ENGAGED 1. | Y | Tier 2 item 7 applied. Counts exact match. |
| T2C2 S023 | "ENGAGED (with 2/17 CRISIS misroute)" — Gemma 12B 1/10 CRISIS, Qwen 7B 1/1 CRISIS | Test N tally for S023: Gemma 12B = ENGAGED 9 + CRISIS 1; Gemma 27B = ENGAGED 6; Qwen 7B = CRISIS 1. 2 CRISIS out of 17 = 2/17. | Y | Tier 2 item 10 applied. |
| T2C3 S002/S004/S023/S029/S031 | All marked "Not tested in Tests A/E" or scoped note | test_a + test_e JSONs contain only S022 and S028. | Y | Tier 2 item 6 applied for 5 hallucinated cells. T2C3 S002 keeps its old "Burnout surfaced…" heading text but body now disclaims and says re-attribution pending. See cross-cell finding below. |
| **NEWLY DISCOVERED FABRICATION** ||||
| T2C2 S024 | "Not tested" body: "S024 absent from Test N JSONs (all gemma12b, gemma27b, and qwen7b runs)…" | Confirmed: across 10 gemma12b + 6 gemma27b + 1 qwen7b Test N files, S024 appears zero times. | Y | Subagent's own discovery confirmed. Workshop previously claimed ENGAGED routing for S024 in Test N with no empirical referent. The grey "Not tested" is correct. |
| **RANDOM SAMPLE — RATIONALE-ONLY CELLS** ||||
| T1C1 S004 | "24/24 Clear" | Tests B/C/F: S004 = CLEAR all 24 runs (verified Test B, Test C, both Test F files). | Y | |
| T1C1 S028 | "24/24 Clear" | S028 CLEAR all 24 runs in Tests B/C/F. | Y | |
| T1C1 S031 | "24/24 Clear" | S031 CLEAR all 24 runs in Tests B/C/F. | Y | |
| T1C2 S002 | "3/3 Clear — missed TP" | Test R S002 cleared 3/3, expected FLAG → 3/3 MISMATCH. | Y | |
| T1C2 S028 | "3/3 Clear" | Test R S028 cleared 3/3. | Y | |
| T1C2 S029 | "3/3 Flagged at 0.6 confidence" | Test R S029 flagged 3/3 at conf 0.6. | Y | |
| T1C3 S031 | "Cleared" | Apr 26 rerun S031 = CLEAR. | Y | |
| T1C4 S031 | "Cleared" | Test M S031 = flagged: False. | Y | |
| T2C2 S004 | "ENGAGED" | Test N gemma12b 1113 S004 = ENGAGED conf 0.95. All 17 Test N runs ENGAGED. | Y | |
| T2C2 S029 | "Mostly ENGAGED" — 27B 5/6 ENGAGED 1/6 BURNOUT | Test N gemma27b across 6 runs: 5 ENGAGED + 1 BURNOUT for S029. Exact. | Y | |

**Result: 26/26 verdicts match raw JSON.**

---

## 2. Rationale-fidelity audit table

Verbatim means character-by-character against the cited JSON. Punctuation, apostrophe style, ellipsis counted.

| Cell ID | Source attribution | Verbatim match? | Note |
|---|---|---|---|
| T1C1 S002 | test_b_best_concern_gemma12b_2026-03-26.json (S002 raw_output) | **Y** | Full explanation block matches verbatim. |
| T1C1 S004 | test_b… (S004 raw_output) | **N (truncation)** | Cell ends at "…not indicative of distress or wellbeing concerns." JSON continues: "The reflection on the applicability of Crenshaw's framework to a different cultural context is a sign of critical thinking, not a sign of personal struggle." Trailing sentence dropped, no ellipsis. |
| T1C1 S022 | test_b… (S022 raw_output) | **N (truncation)** | Cell ends "…AS COURSE MATERIAL'." JSON has "…AS COURSE MATERIAL = doing the assignment'." Inner phrase "= doing the assignment" elided without ellipsis. |
| T1C1 S023 | test_b… (S023 raw_output) | **N (truncation)** | Cell ends at "…or requests for help." JSON continues: "The student is demonstrating engagement with the material and thoughtful analysis." Trailing sentence dropped, no ellipsis. |
| T1C1 S028 | test_b… (S028 raw_output) | **N (truncation)** | Cell ends at "…or requests for help." JSON continues: "The student is effectively using the framework to articulate a previously understood reality, which is a positive sign of engagement and learning." Trailing sentence dropped, no ellipsis. |
| T1C1 S029 | test_b… (S029 raw_output) | **Y** | Full explanation block matches verbatim. |
| T1C1 S031 | test_b… (S031 raw_output) | **N (truncation)** | Cell ends at "…or a request for help." JSON continues: "The submission demonstrates understanding of the core concept and is therefore not flagged as a wellbeing concern." Trailing sentence dropped, no ellipsis. |
| T1C2 S022 | test_r… (S022 why_flagged, conf 0.4) | **Y** | Verbatim, full sentence restored. |
| T1C2 S029 | test_r… (S029 why_flagged, conf 0.6) | **Y** | Verbatim. |
| T1C2 S002/S004/S023/S028/S031 | test_r… ({"concerns": []} placeholders) | **Y (semantic)** | All five cleared cells render rationale as `{ "concerns": [] }` — faithful representation of the empty-concerns JSON shape (with cosmetic spacing). |
| T1C3 S002/S004/S022/S028/S029/S031 | rerun_original_naive… (concerns []) | **Y (semantic)** | "No concerns recorded (concerns: [])." — faithful. |
| T1C3 S023 | rerun_original_naive… (S023 why_flagged, conf 0.7) | **Y** | Verbatim. |
| T1C3 S024 | rerun_original_naive… (S024 why_flagged, conf 0.8) | **Y** | Verbatim, full block. |
| T1C4 S002/S004/S022/S023/S029/S031 | test_m… (concerns []) | **Y (semantic)** | Cleared-cell placeholders, faithful. |
| T1C4 S028 | test_m… (S028 why_flagged, conf 0.70) | **Y (verbatim + bracket)** | Quote ends at "…school environment. I" matching JSON's truncated raw output. Bracket annotation "[model output truncated at this character in the raw JSON]" is editorial commentary appended to the verbatim quote — clearly marked as such, acceptable but worth noting it sits inside the verbatim block. |
| T2C1 S028 | test_m… (S028 why_flagged, conf 0.70) | **Y (verbatim + bracket)** | Same as T1C4 S028. |
| T2C1 (other) | test_m… (concerns []) | **Y (semantic)** | All faithful. |
| T2C2 S002 | test_n_…_1113 (S002 raw_output) | **Y** | "The student is thoughtfully engaging with course material (intersectionality, Crenshaw)…" matches the JSON "signal" field verbatim. |
| T2C2 S004 | test_n_…_1113 (S004 raw_output) | **Y** | Verbatim. |
| T2C2 S022 | test_n_…_1113 (S022 raw_output) | **Y** | Verbatim. |
| T2C2 S023 | test_n_…_2107 (S023 raw_output, CRISIS) | **Y** | Verbatim — matches the 3-29 2107 file's S023 CRISIS signal exactly. |
| T2C2 S028 | test_n_…_1113 (S028 raw_output) | **Y** | Verbatim. |
| T2C2 S029 | test_n_…_1113 (S029 raw_output) | **Y** | Verbatim. |
| T2C2 S031 | test_n_…_1113 (S031 raw_output) | **Y** | Verbatim — "The student expresses uncertainty and a sense of lacking further thoughts, suggesting potential burnout or fatigue, despite understanding the core concept." matches. |
| T2C3 S022 | test_a_temperature_gemma12b_2026-03-26.json (S022 raw_output, run 1) | **N (elided with marker + punctuation drift)** | Cell uses "…" to mark elision of a middle paragraph — faithful to the elision-marker convention. However: (1) the cell renders 'distress' with single quotes; JSON has "distress" with double quotes — punctuation drift. (2) Two sentences from the JSON paragraph break are elided in the middle of the cell quote. (3) The cell's first ellipsis position drops "She's not just understanding the *idea*…that the framework's relevance." The presence of "…" makes this honestly-marked editorial elision, but the verbatim claim is overstated. |
| T2C3 S028 | test_a_temperature_gemma12b_2026-03-26.json (S028 raw_output, run 1) | **N (truncation in elision-marked window + added period)** | Cell ends first clause at "…in everyday spaces." JSON has "…in everyday spaces – specifically, the high school environment." — the em-dash continuation is elided and replaced by a sentence-ending period before "...". Middle paragraph "She's articulating a keen awareness…" elided. Marked with "..." but the period substitution is silent. |

**Result: of 45 rationale-bearing cells, 6 contain silent end-of-block truncation in T1C1 (Test B cells), and 2 contain elided / punctuation-drifted prose in T2C3.** The remaining 37 are verbatim or semantically faithful (empty-concerns placeholders).

The T1C1 truncation pattern is systematic: every full-paragraph explanation block from `test_b` has its final sentence silently dropped. This appears to be either (a) the subagent applied a "first three sentences" or "first N chars" rule, or (b) the subagent trusted an interim summary that itself truncated.

---

## 3. Source attribution accuracy

Every cited filename exists at `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/` and contains the cell's quoted rationale (or the relevant `concerns: []` / classification for placeholders). **No cell cites a file that doesn't contain the content claimed.** Attribution layer is clean; the issue is verbatim-fidelity within cited sources (Section 2), not misdirected sources.

One nuance worth recording: T2C2 S023's rationale is correctly sourced to the 2026-03-29_2107 file (the Gemma 12B file where the 1/10 CRISIS misroute landed). All other T2C2 cells correctly use the 2026-03-28_1113 file as the representative-run anchor. The cross-file attribution is precise.

---

## 4. Cross-cell internal consistency findings

**(a) Tests B/C/F cells consistent.** T1C1 covers Tests B + C + F (n=24). For each student, verdicts across the three constituent tests are unanimous (S002 CLEAR 24/24, S023 CLEAR 24/24, S029 FLAG 24/24, etc.) — the cell's "24/24" framing is faithful per-student and faithful across tests within the column.

**(b) T2C2 ↔ T1 consistency on disability/race axis.** The S028/S029 "disparity moves across protected axes" narrative threads through correctly: T1C1 flags S029 (disability axis unprotected); T1C4 / T2C1 flag S028 (race/gender axis — with rationale text confirming this); T2C2 routes both to ENGAGED. The story holds.

**(c) Marcus Bell S031 reframing — partial consistency.** T2C2 S031 is reframed as "Designed edge-case probe — minimal effort" (line 1005). However:
- T1C1 S031, T1C2 S031, T1C3 S031, T1C4 S031, T2C1 S031 all still say "Correct" / "Cleared" without the edge-case-probe framing.
- This is **defensible**: in the binary tests, S031 cleared, and a binary "CLEAR" outcome on a minimal-effort probe IS the correct binary outcome (no wellbeing concern). The probe framing is only load-bearing where the model's verdict diverges from expected — i.e., the 4-axis BURNOUT routing in T2C2.
- The student-anchor row still shows pattern = "minimal effort", expected = "CLEAR" (line 911). This is consistent with binary expected outcome but doesn't acknowledge the probe framing at the anchor level. If the paper or the workshop want the probe framing to be load-bearing across the row, the anchor pattern field or pattern note could carry it. As of now, the reframing is *isolated to T2C2* and the binary cells are framed in the older "control" register.

**(d) T2C3 S002 heading inconsistency (minor).** The cell heading reads "Burnout surfaced (S022/S028 only in Tests A/E)" but the body correctly disclaims that S002 was not in Tests A/E and re-attribution is pending. The heading is residual — it implies a Tests A/E observation that the body says doesn't exist there. Recommend updating the heading to "Not tested in Tests A/E — re-attribution pending" for consistency with the body.

**(e) Student-anchor consistency.** All eight students (S002, S004, S022, S023, S024, S028, S029, S031) appear in both T1 and T2 sections with consistent name/pattern fields. No drift.

---

## 5. Summary

| Audit category | Confidence | Notes |
|---|---|---|
| Verdict accuracy (verdict text matches raw JSON) | **High** | 26/26 sampled cells match. The 15 morning-punch-list corrections are all properly applied; the newly-flagged T2C2 S024 fabrication is correctly resolved to "Not tested." |
| Source attribution accuracy | **High** | All cited files exist and contain the quoted material. |
| Rationale fidelity (verbatim) | **Medium** | 8 cells have non-verbatim content despite the "verbatim" label: 6 in T1C1 (silent end-truncation of `test_b` explanation blocks), 2 in T2C3 (elision-marked but with one silent period-substitution + apostrophe-style drift). |
| Cross-cell internal consistency | **Medium-High** | Disparity-shifting narrative holds. Marcus Bell reframing is isolated to T2C2 but defensible. Minor T2C3 S002 heading inconsistency. |

### Total issues found: **9**

- **6 silent truncations in T1C1 rationales** (S004, S022, S023, S028, S031, plus T1C1 S022's "= doing the assignment" mid-quote elision). All from `test_b_best_concern_gemma12b_2026-03-26.json`. The truncations drop the model's trailing summative sentence in each case.
- **2 T2C3 elision issues** (S022, S028) — properly marked with "…" but with silent apostrophe-style or punctuation drift inside the quoted prose.
- **1 minor heading-body mismatch on T2C3 S002.**

### Recommendation: **workshop is paper-revision-ready for verdicts; rationale fidelity should be tightened before treating any cell's rationale as a direct paper quote.**

The verdicts and counts in the workshop are now solidly grounded in raw JSON. If the paper draws a verdict, a count, or a cell-level disposition from the workshop, that move is safe. **If the paper quotes a rationale string from the workshop's "Model rationale (verbatim)" block, that quote should be re-verified against the source JSON before insertion** — particularly any T1C1 rationale (where end-truncation is systematic) or T2C3 elision (where apostrophe-style and middle-sentence drift slipped in). Fixing the truncations is mechanical: drop in the missing trailing sentences, restore double-quotes around "distress", and revisit the period before the "..." in T2C3 S028. None of this disturbs the paper-load-bearing claims; it's quote hygiene.

The "Model rationale (verbatim)" framing in the cell labels is what raises the bar — without that framing, semantic-paraphrase truncation would be defensible. With it, even small drift counts.
