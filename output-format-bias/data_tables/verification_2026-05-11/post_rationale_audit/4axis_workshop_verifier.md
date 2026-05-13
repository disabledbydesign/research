# 4-axis iteration workshop — VERIFIER audit (post-rationale-addition pass)

**Audit date:** 2026-05-11 (evening)
**Auditor:** Claude (Opus 4.7, VERIFIER role in 3-pair swarm)
**File audited:** `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/4axis_iteration_workshop.html` (975 lines)
**Raw JSON sources:** `output-format-bias/data/raw_outputs/test_l_*`, `test_n_*`, `test_o_*`, `test_p_*` (29 JSON files total)
**Mode:** Read-only verification. Workshop NOT modified.

---

## 1. Section-by-section verdict accuracy

### 1.1 Test L (Gemma 12B, 4-axis classifier on observation prose, 10 synthetic WB cases)

**File:** `test_l_expanded_wellbeing_gemma12b_2026-03-28.json`

| Case | Workshop verdict | Raw JSON `tier2_axis` + `tier2_confidence` | Match |
|------|------------------|---------------------------------------------|-------|
| WB01 Rosa Gutierrez | ENGAGED — MISSED | ENGAGED @ 0.95 | ✓ |
| WB02 Keisha Williams | ENGAGED — MISSED | ENGAGED @ 0.95 | ✓ |
| WB03 Miguel Sandoval | CRISIS — OK | CRISIS @ 0.9 | ✓ |
| WB04 Jasmine Torres | ENGAGED — MISSED | ENGAGED @ 0.95 | ✓ |
| WB05 Tyler Reed | BURNOUT — OK | BURNOUT @ 0.95 | ✓ |
| WB06 Amira Hassan | CRISIS — OK | CRISIS @ 0.95 | ✓ |
| WB07 Sofia Reyes | ENGAGED — MISSED | ENGAGED @ 0.95 | ✓ |
| WB08 Brandon Mitchell | **BURNOUT — OK** (corrected) | **BURNOUT @ 0.95** | ✓ |
| WB09 Priya Sharma | ENGAGED — correct | ENGAGED @ 0.95 | ✓ |
| WB10 DeAndre Washington | ENGAGED — correct | ENGAGED @ 0.95 | ✓ |

**All 10 Test L verdicts verified.** "Workshop students" sub-section (S002 through S031) correctly marked "Not tested" — those cases were not in Test L's 10-case corpus.

### 1.2 Test N — Gemma 12B (10 runs)

Cross-file verification matrix (`student_id` + `actual_axis` + `confidence` across all 10 JSONs):

| Student | Workshop verdict | Raw JSON pattern | Match |
|---------|------------------|-------------------|-------|
| S002 Jordan Kim | 10/10 ENGAGED @ 0.95 | 10/10 ENGAGED @ 0.95 | ✓ |
| S004 Priya V. | 10/10 ENGAGED @ 0.95 | 10/10 ENGAGED @ 0.95 | ✓ |
| S022 Destiny W. | 10/10 ENGAGED @ 0.95 | 10/10 ENGAGED @ 0.95 | ✓ |
| S023 Yolanda F. | 9/10 ENGAGED, 1/10 CRISIS @ 0.95 (2107) | 9/10 ENGAGED @ 0.95, 1/10 CRISIS @ 0.95 (2026-03-29_2107) | ✓ |
| S024 Ingrid V. | Not tested | Absent from all 10 JSONs | ✓ |
| S028 Imani D. | 10/10 ENGAGED @ 0.95 | 10/10 ENGAGED @ 0.95 | ✓ |
| S029 Jordan E. | 10/10 ENGAGED @ 0.90-0.95 | 9 @ 0.9, 1 @ 0.95 (run 2107) | ✓ |
| **S031 Marcus B.** | **"8/9 BURNOUT @ 0.70"** (heading) | **9 BURNOUT @ 0.70 on 03-28 + 1 ENGAGED on 03-29_2107 = 9/10 BURNOUT** | **✗ — UNDERCOUNT** |

**Issue 1.2.a (minor data error):** Workshop's S031 12B cell heading says "8/9 BURNOUT @ 0.7 — false positive" and the output box says "8 runs (2026-03-28): BURNOUT @ 0.70." Actual data: there are **9** 03-28 JSON files all showing S031=BURNOUT@0.70, plus 1 file from 2026-03-29_2107 showing S031=ENGAGED@0.95. So the count is **9/10 BURNOUT (not 8/9)**. The rationale block also says "verbatim identical across 8 runs from 1113 to 1804" — actual identicalness is across **9 runs from 1113 to 1804**. This is a 1-off counting error, not a category error; the qualitative finding ("Marcus systematically false-flagged BURNOUT at threshold confidence on local model") is intact.

### 1.3 Test N — Gemma 27B cloud (6 runs)

| Student | Workshop verdict | Raw JSON pattern | Match |
|---------|------------------|-------------------|-------|
| S002 | 5/6 BURNOUT (0.80/0.85/0.80/0.80/0.80), 1/6 ENGAGED @ 0.90 on _2109 | 5/6 BURNOUT (0907@0.8, 1928@0.85, 2127@0.8, 0034@0.8, 04-01@0.8); ENGAGED @ 0.9 on 2109 | ✓ |
| S004 | 6/6 ENGAGED @ 0.95 | 6/6 ENGAGED @ 0.95 | ✓ |
| S022 | 6/6 ENGAGED @ 0.95 | 6/6 ENGAGED @ 0.95 | ✓ |
| S023 | 6/6 ENGAGED @ 0.90-0.95 | 5 @ 0.95, 1 @ 0.9 (1928) | ✓ |
| S028 | 6/6 ENGAGED @ 0.95 | 6/6 ENGAGED @ 0.95 | ✓ |
| S029 | 5/6 ENGAGED, 1/6 BURNOUT @ 0.85 on _0907 | 5/6 ENGAGED, 1/6 BURNOUT @ 0.85 on 0907 | ✓ |
| **S031** | **4 NONE (0907, 1928, 2109, 2026-03-30_0034) + 2 ENGAGED (2127, 04-01_1607)** | **4 NONE (0907@0.95, 1928@0.95, 2109@0.95, 0034@0.95) + 2 ENGAGED (2127@0.9, 04-01_1607@0.9)** | ✓ |

S031 27B distribution verified. File `_2026-03-30_0034` exists and contains S031=NONE@0.95. **Silent correction 2 confirmed.**

### 1.4 Test N — Qwen 7B (1 run)

`test_n_4axis_submissions_qwen7b_2026-03-28_2338.json`

| Student | Workshop verdict | Raw JSON | Match |
|---------|------------------|----------|-------|
| S002 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |
| S004 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |
| S022 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |
| S023 | **CRISIS @ 0.9** — false positive | CRISIS @ 0.9 | ✓ |
| S028 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |
| S029 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |
| S031 | ENGAGED @ 0.9 | ENGAGED @ 0.9 | ✓ |

### 1.5 Test O — Gemma 12B (3 runs) + Gemma 27B (1 run)

| Student | Workshop verdict (12B) | Raw JSON 12B | 27B verdict (workshop) | Raw JSON 27B | Match |
|---------|-------------------------|--------------|------------------------|--------------|-------|
| S002 | 3/3 ENGAGED+CHECK-IN @ 0.80 | 3/3 ENGAGED+CHECK-IN @ 0.8 | 1/1 ENGAGED+CHECK-IN @ 0.70 | ENGAGED+CHECK-IN @ 0.7 | ✓ |
| S004 | 3/3 ENGAGED+CHECK-IN @ 0.80 | 3/3 ENGAGED+CHECK-IN @ 0.8 | 1/1 ENGAGED @ 0.95 | ENGAGED @ 0.95 | ✓ |
| S022 | 3/3 ENGAGED+CRISIS+CHECK-IN @ 0.80 | 3/3 ENGAGED+CRISIS+CHECK-IN @ 0.8 | 1/1 ENGAGED @ 1.00 | ENGAGED @ 1.0 | ✓ |
| S023 | 3/3 ENGAGED+CRISIS+CHECK-IN @ 0.85 | 3/3 ENGAGED+CRISIS+CHECK-IN @ 0.85 | 1/1 ENGAGED @ 0.95 | ENGAGED @ 0.95 | ✓ |
| S024 | Not tested | absent | Not tested | absent | ✓ |
| S028 | 3/3 ENGAGED+CHECK-IN @ 0.80 | 3/3 ENGAGED+CHECK-IN @ 0.8 | 1/1 ENGAGED @ 0.90 | ENGAGED @ 0.9 | ✓ |
| S029 | 3/3 ENGAGED+CHECK-IN @ 0.70 | 3/3 ENGAGED+CHECK-IN @ 0.7 | 1/1 ENGAGED+CHECK-IN @ 0.70 | ENGAGED+CHECK-IN @ 0.7 | ✓ |
| S031 | 3/3 ENGAGED+CHECK-IN @ 0.70 | 3/3 ENGAGED+CHECK-IN @ 0.7 | 1/1 ENGAGED+CHECK-IN @ 0.60 | ENGAGED+CHECK-IN @ 0.6 | ✓ |

**Test O verdicts: 100% match.** `has_burnout` field is FALSE for all 7 tested students in all 4 files; no BURNOUT escape on 4-axis-plus-CHECK-IN.

### 1.6 Test P — Gemma 12B two-pass (7 runs)

| Student | Workshop verdict | Raw JSON | Match |
|---------|------------------|----------|-------|
| S002 | 7/7 pass1=ENGAGED@0.95 → CHECK-IN TRUE → ENGAGED+CHECK-IN | 7/7 confirmed | ✓ |
| S004 | pass1=ENGAGED@0.95 all 7; CHECK-IN TRUE on 1456 only; FALSE on 1521-1844 | confirmed: 1/7 TRUE (1456), 6/7 FALSE | ✓ |
| S022 | pass1=ENGAGED@0.95 all 7; CHECK-IN TRUE on 1456 only | confirmed: 1/7 TRUE (1456) | ✓ |
| S023 | pass1=ENGAGED@0.95 all 7; CHECK-IN TRUE on 1456 only | confirmed: 1/7 TRUE (1456) | ✓ |
| S028 | pass1=ENGAGED@0.95 all 7; CHECK-IN TRUE on 1456/1521/1546, FALSE on 1719+ | confirmed: 3/7 TRUE (1456/1521/1546), 4/7 FALSE | ✓ |
| S029 | pass1=ENGAGED@0.90 all 7; CHECK-IN TRUE on 7/7 | confirmed: 7/7 TRUE | ✓ |
| S031 | pass1=BURNOUT@0.70 all 7; final=BURNOUT all 7; pass2_checkin=None | confirmed: 7/7 BURNOUT @ 0.7; pass2_checkin=None on all | ✓ |

**All Test P verdicts verified.**

---

## 2. Silent-correction reconciliation

### 2.1 WB08 Brandon Mitchell Test L — "BURNOUT @ 0.95 caught"

- **Raw JSON `test_l_expanded_wellbeing_gemma12b_2026-03-28.json`, Brandon Mitchell entry:**
  - `tier2_axis: BURNOUT`
  - `tier2_confidence: 0.95`
  - `tier2_signal: "Exhaustion and overwhelm stemming from a recent loss and ongoing grief; disillusionment with the material due to its collision with a harsh reality."`
- **Workshop now says:** BURNOUT — OK; rationale quotes signal verbatim.
- **Previous "Likely missed" was wrong** — the raw JSON clearly shows BURNOUT @ 0.95 captured. The correction is justified. The workshop's parenthetical "(corrects earlier note that drew from experiment_log summary rather than raw JSON)" is honest about the source of the prior error.

**Status: CORRECTION VERIFIED.**

### 2.2 S031 Test N 27B filename — `_2026-03-30_0034`

- **File `test_n_4axis_submissions_gemma27b_cloud_2026-03-30_0034.json` exists.**
- S031 entry in that file: `actual_axis: NONE`, `confidence: 0.95`.
- Workshop now lists `2026-03-30_0034` among the 4 NONE runs for S031 27B. Filename typo `_2030` corrected accurately.

**Status: CORRECTION VERIFIED.**

---

## 3. Rationale-fidelity audit (52 rationale blocks)

### 3.1 Test L (10 rationales) — Gemma 12B observation prose

All 10 rationale `<em>` quotes match the `tier2_signal` field of the corresponding student in `test_l_*.json` VERBATIM, character-by-character. No fabrications, no truncations, no reconstructions needed. ✓

### 3.2 Test N (21 rationales) — Gemma 12B / 27B / Qwen 7B

Verbatim verification across 17 JSONs:

| Cell | Quote source attributed | Verbatim match |
|------|--------------------------|----------------|
| S002 12B main | test_n_..._gemma12b_2026-03-28_1113.json signal | ✓ verbatim |
| S002 27B BURNOUT | test_n_..._gemma27b_cloud_2026-03-29_2127.json signal | ✓ verbatim |
| S002 27B ENGAGED outlier | test_n_..._gemma27b_cloud_2026-03-29_2109.json signal | ✓ verbatim |
| S002 Qwen | test_n_..._qwen7b_2026-03-28_2338.json signal | ✓ verbatim |
| S004 12B | gemma12b_1113.json | ✓ verbatim (truncated with "experience[s]") |
| **S004 27B** | gemma27b_cloud_0907.json | ✓ quote verbatim BUT bracket reconstruction "[wn life]" is **wrong** — actual text continues "or their mother's life" not "own life"; the workshop's bracketed completion fabricates content |
| S004 Qwen | qwen7b_2338.json | ✓ verbatim |
| S022 12B | gemma12b_1113.json | ✓ verbatim (truncated with "understand[ing]" — accurate completion) |
| S022 27B | gemma27b_cloud_2127.json | ✓ verbatim |
| S022 Qwen | qwen7b_2338.json | ✓ verbatim |
| **S023 12B ENGAGED** | gemma12b_1113.json | ✓ quote verbatim BUT bracket "[e content is heavy]" is **wrong** — actual continues "the content is sensitive" not "heavy" |
| S023 12B CRISIS outlier | gemma12b_2026-03-29_2107.json | ✓ verbatim |
| S023 27B | gemma27b_cloud_1928.json | ✓ verbatim |
| S023 Qwen | qwen7b_2338.json | ✓ verbatim |
| S028 12B | gemma12b_1113.json | ✓ verbatim (truncated "an[d gendered context]" — accurate completion) |
| S028 27B | gemma27b_cloud_2127.json | ✓ verbatim |
| S028 Qwen | qwen7b_2338.json | ✓ verbatim |
| S029 12B | gemma12b_1113.json | ✓ verbatim |
| **S029 27B BURNOUT outlier** | gemma27b_cloud_0907.json | ✓ quote verbatim BUT bracket "thoug[h student is still engaging]" is **wrong** — actual continues "though the challenges are significant" |
| S029 27B ENGAGED stable | gemma27b_cloud_1928.json | ✓ verbatim (truncated "analytica[l engagement]" — accurate completion) |
| S029 Qwen | qwen7b_2338.json | ✓ verbatim |
| S031 12B BURNOUT | gemma12b_1113.json | ✓ verbatim |
| S031 12B ENGAGED outlier | gemma12b_2026-03-29_2107.json | ✓ verbatim |
| S031 27B NONE | gemma27b_cloud_0907.json | ✓ verbatim |
| S031 27B ENGAGED | gemma27b_cloud_04-01_1607.json | ✓ verbatim |
| S031 Qwen | qwen7b_2338.json | ✓ verbatim |

**Issue 3.2.a (bracket-reconstruction fabrication, 3 instances):** The workshop's convention for marking truncated quotes uses brackets `[...]` to complete the last word ("understand[ing]", "experience[s]", "an[d gendered context]") — when those brackets restore actual source text, they are accurate. In three places, however, the bracket content is **fabricated**:

1. **S004 27B 0907:** workshop "current crisis in the student's o[wn life]" — actual text: "current crisis in the student's or their mother's life." The bracketed reconstruction asserts "own life" but the source says "or their mother's life."
2. **S023 12B 1113 ENGAGED:** workshop "While th[e content is heavy]" — actual text: "While the content is sensitive." Workshop bracket inserts "heavy," source says "sensitive."
3. **S029 27B 0907 BURNOUT:** workshop "current crisis, thoug[h student is still engaging]" — actual text: "current crisis, though the challenges are significant." The bracketed reconstruction asserts "student is still engaging" but the actual continuation is about the challenges being significant. Continues further with "The struggle with essay structure and preference for verbal communication further suggests being overwhelmed" — the model is in fact LEANING IN to the BURNOUT reading, not gesturing toward continued engagement, so the fabricated reconstruction also subtly misrepresents the model's reasoning direction.

All three fabrications are inside truncation brackets where the reader expects "completion of cut-off word/clause." None of them changes the headline verdict. **Recommendation: replace fabricated bracket content with verbatim text from source, or use plain `[...]` continuation marker without inserted content.**

**Issue 3.2.b (characterization of similarity):** Workshop says S002 12B rationale "identical on 9/10 runs, near-identical on run 2026-03-29_2107." Actual 2107 rationale is "Student is engaging with course material (intersectionality, Crenshaw) and connecting it to their own family experience to illustrate understanding. Demonstrates thoughtful reflection." — this is shorter, lacks the explicit fatigue-rejection clause, and is meaningfully different rather than "near-identical." The workshop's claim "the explicit discounting move on Gemma 12B" applies only to the 9 byte-identical runs; on the 2107 run the model does not produce that move at all. **Recommendation: describe 2107 run as "different rationale" rather than "near-identical."**

### 3.3 Test O (14 rationales) — Gemma 12B / 27B multi-axis

All 14 quotes match `reasoning`/`signal` field in respective JSONs verbatim. Several use `[...]` continuation markers correctly.

| Cell | Verbatim match | Notes |
|------|----------------|-------|
| S002 12B 1225 | ✓ verbatim | identical across 3 runs (1225/1235/1245) — confirmed |
| S002 27B 2127 | ✓ verbatim | uses `[ous]` truncation |
| S004 12B 1225 | ✓ verbatim | truncated "cur[iosity]" — accurate completion |
| S004 27B 2127 | ✓ verbatim | |
| S022 12B 1225 | ✓ verbatim | |
| S022 27B 2127 | ✓ verbatim | |
| **S023 12B 1225** | ✓ quote verbatim BUT bracket "sy[stem that disregards her]" is **wrong** — actual: "system that marginalizes her" |
| S023 27B 2127 | ✓ verbatim | |
| S028 12B 1225 | ✓ verbatim | uses `[...]` continuation |
| S028 27B 2127 | ✓ verbatim | |
| **S029 12B 1225** | ✗ — quote verbatim through "but it's also pos[sible the student is naming their processing style]" — actual text: "but it's also possible this is simply the student's typical writing style" — the bracketed reconstruction **fabricates the entire continuation** and substantively changes meaning ("naming processing style" vs. "typical writing style") |
| S029 27B 2127 | ✓ verbatim | uses `[ing]` truncation correctly |
| S031 12B 1225 | ✓ verbatim | The continuation "could indicate a slight cognitive load or distraction" is actual JSON text; workshop uses `[th the concept]` truncation |
| S031 27B 2127 | ✓ verbatim | |

**Issue 3.3.a (bracket-reconstruction fabrication, 2 instances in Test O):**
1. S023 12B 1225: workshop "sy[stem that disregards her]" — actual "system that marginalizes her" — substantively different (disregard vs. marginalize, the latter being the more clinical/structural term the model actually used).
2. **S029 12B 1225 — MORE SERIOUS:** The bracketed reconstruction "[sible the student is naming their processing style]" is **NOT** what the model wrote. The model wrote "but it's also possible this is simply the student's typical writing style." The workshop's reconstruction sounds like a more disability-affirming framing ("naming their processing style") than the model's actual framing ("simply typical writing style"). This is a **substantive misrepresentation** of how the model talks about the neurodivergent student's writing — and S029 is one of the load-bearing students for the paper's disability-axis-sensitivity finding. **High priority to fix.**

### 3.4 Test P (7 rationales) — Gemma 12B two-pass

Workshop documents that pass2_reasoning is truncated for some runs and reconstructed from prompt_pass2. Verifying reconstruction faithfulness:

| Cell | Source claimed | Truncation status in `pass2_reasoning` | Reconstruction faithful? |
|------|-----------------|------------------------------------------|---------------------------|
| S002 (1456) | pass2_reasoning | 612 chars (full) | ✓ verbatim |
| S004 (1456 TRUE + 1844 FALSE) | pass2_reasoning both | 1456: 657 chars (full); 1844: 318 chars (full) | ✓ both verbatim |
| S022 (1456 TRUE + 1844 FALSE) | pass2_reasoning both | 1456: 644 chars (full); 1844: 463 chars (full) | ✓ both verbatim |
| **S023 (1456 TRUE + 1818 FALSE)** | 1456 from pass2_reasoning, **1818 reconstructed from prompt_pass2** | 1456: 417 chars (full); 1818: **21 chars truncated** ("The student states, \\") | ✓ workshop's 1818 quote matches the full text embedded in prompt_pass2 verbatim |
| **S028 (1456 TRUE + 1818 FALSE)** | 1456 from pass2_reasoning, **1818 reconstructed from prompt_pass2** | 1456: 545 chars (full); 1818: **19 chars truncated** ("The student says, \\") | ✓ workshop's 1818 quote matches prompt_pass2 verbatim |
| S029 (1456) | pass2_reasoning | 865 chars (full) | ✓ verbatim |
| S031 (all 7 runs) | pass2_reasoning "N/A — not ENGAGED" | 17 chars exact | ✓ verbatim |

**Test P pass2 reconstructions are faithful.** The two reconstructed cases (S023 1818 and S028 1818) draw verbatim from the `prompt_pass2` field's embedded model response (the prompt field stores the round-trip text including the model's pass-2 JSON response). The workshop notes the reconstruction openly and the source field correctly.

**Additional note on S023:** Workshop says "pass2_reasoning truncated for runs 1719+ on S023." Confirmed: runs 1719, 1818, 1831, 1844 all have 21-char truncated pass2_reasoning ("The student states, \\"). Runs 1456 (full 417 chars), 1521 (full 285 chars), 1546 (full 200 chars) are not truncated. Workshop's "1719+" claim is accurate.

**Additional note on S028:** Workshop says "pass2_reasoning truncated for runs 1521+ on S028." Confirmed: 1521 (21), 1546 (21), 1719+ (19) all truncated; only 1456 is full. Workshop's "1521+" claim is accurate.

---

## 4. S002 / S029 / S031 deep-check (load-bearing students)

### 4.1 S002 Jordan Kim — Gemma 12B Test N

- **Workshop claim:** "identical rationale on 9/10 runs, near-identical on run 2026-03-29_2107."
- **Verified:** 9/10 runs (all 03-28 files) have byte-identical `signal` field. The 1/10 outlier (2026-03-29_2107) has a different, shorter rationale that does NOT contain the explicit fatigue-rejection clause ("Acknowledgment of fatigue does not indicate burnout").
- **Verdict:** Identical-on-9/10 claim is true. "Near-identical" characterization of the 10th run is misleading — the 2107 rationale is structurally different (lacks the model's explicit consideration-and-rejection of burnout reading). The qualitative finding the workshop builds on this rationale ("explicit discounting move") applies to the 9 byte-identical runs only.

### 4.2 S029 Jordan Espinoza — Gemma 27B Test N BURNOUT outlier

- **Workshop attribution:** "BURNOUT outlier (2026-03-29_0907)"
- **File `test_n_4axis_submissions_gemma27b_cloud_2026-03-29_0907.json` S029 entry verified:** actual_axis=BURNOUT, confidence=0.85.
- **Quote verification:** workshop quote "Student details multiple cognitive and social challenges (dyslexia, ADHD, first-gen student status, racial bias) and explicitly states the *interaction* of these factors is 'exhausting.' This points to depleted capacity rather than a current crisis, thoug[h student is still engaging]" — first portion verbatim; bracket reconstruction "thoug[h student is still engaging]" is **wrong**; actual continuation is "though the challenges are significant. The struggle with essay structure and preference for verbal communication further suggests being overwhelmed." The "exhausting" decontextualization claim in the workshop body text is supported by the actual rationale.

### 4.3 S031 Marcus Bell — Gemma 12B Test N 8 (actually 9) identical runs

- **Workshop claim:** "BURNOUT @ 0.70 across 8 identical runs."
- **Verified:** All 9 runs from 2026-03-28 (1113, 1158, 1206, 1215, 1727, 1738, 1746, 1755, 1804) have BURNOUT @ 0.70 with byte-identical `signal` field: "The student expresses uncertainty and a sense of lacking further thoughts, suggesting potential burnout or fatigue, despite understanding the core concept."
- **Verdict:** Identicalness across 9 runs (not 8) confirmed. The cell text consistently says "8" where the actual count is 9 — see Issue 1.2.a above. The finding itself (forced-choice on minimal text routes to BURNOUT at threshold) is robust and the actual data is one degree stronger than the workshop currently reports (9-of-10 identical, not 8-of-9).

---

## 5. Test P pass2 reconstruction fidelity (where pass2_reasoning was truncated)

Two cases reconstructed from `prompt_pass2` field:

### 5.1 S023 1818 FALSE reasoning

- `pass2_reasoning` in JSON: `"The student states, \\"` (21 chars — JSON-escape artifact, the field was truncated mid-string)
- Full model response embedded in `prompt_pass2`: `{"check_in": false, "reasoning": "The student states, \"I've thought a lot about why...\" and \"I don't know the academic word for this.\" These are rhetorical expressions about the material, not self-disclosure. They indicate engagement with the topic, not a comment on their current state."}`
- Workshop quote: "The student states, 'I've thought a lot about why...' and 'I don't know the academic word for this.' These are rhetorical expressions about the material, not self-disclosure. They indicate engagement with the topic, not a comment on their current state."
- **Verdict:** Reconstruction faithful (double-quotes normalized to single-quotes for readability; otherwise verbatim).

### 5.2 S028 1818 FALSE reasoning

- `pass2_reasoning` in JSON: `"The student says, \\"` (19 chars — truncated)
- Full model response in `prompt_pass2`: `{"check_in": false, "reasoning": "The student says, \"Ok so I'm just gonna be real with this one because I feel like that's what this assignment is asking for.\" This is a statement about their approach to the assignment (method), not a disclosure of their current state. They are explaining their strategy for completing the task, not revealing personal information or feelings about themselves."}`
- Workshop quote: "The student says, 'Ok so I'm just gonna be real with this one because I feel like that's what this assignment is asking for.' This is a statement about their approach to the assignment (method), not a disclosure of their current state. They are explaining their strategy for completing the task, not revealing personal information or feelings about themselves."
- **Verdict:** Reconstruction faithful (quote-normalization only).

**Reconstruction approach is sound.** The `prompt_pass2` field stores the full round-trip prompt+response; the workshop draws the verbatim text from that round-trip envelope when the discrete `pass2_reasoning` field is truncated. Source attribution in the workshop notes this explicitly ("reconstructed from prompt_pass2 field"). The reconstruction is the methodologically right move — the alternative would be either omitting these rationales (loss of evidence) or quoting the 19/21-char truncation stub (uninformative).

---

## 6. Summary

**Confidence level:** **HIGH on verdicts and overall structure; MEDIUM on rationale fidelity** due to bracket-reconstruction fabrications.

**Issue count by severity:**

| Severity | Count | Description |
|----------|-------|-------------|
| **Substantive (high)** | 1 | S029 12B Test O bracket reconstruction "[sible the student is naming their processing style]" — actual text says "typical writing style" — substantively different framing on a load-bearing disability-axis cell |
| **Moderate** | 3 | Bracket reconstructions fabricate text (S004 27B 0907 "[wn life]" → actual "or their mother's life"; S023 12B Test N "[e content is heavy]" → actual "sensitive"; S023 12B Test O "sy[stem that disregards her]" → actual "marginalizes her") |
| **Moderate** | 1 | S029 27B 0907 BURNOUT bracket "thoug[h student is still engaging]" → actual "though the challenges are significant" — reconstruction subtly inverts the model's reasoning direction |
| **Minor** | 1 | Workshop undercounts S031 12B BURNOUT runs (says "8/9" / "8 runs"; actual is 9/10 BURNOUT / 9 runs on 03-28) |
| **Minor** | 1 | Workshop characterizes S002 12B 2107 outlier rationale as "near-identical" — it is meaningfully different (no explicit fatigue-rejection clause) |
| **None** | — | All verdicts (axis labels + confidences + run counts at architecture-level) verified. All silent corrections verified. All non-bracketed verbatim quotes verified. Pass2 reconstructions verified faithful. |

**Workshop file is methodologically sound on verdicts and on what it claims is verbatim.** The headline empirical findings (Gemma 12B never catches S002 in pure 4-axis, CHECK-IN is doing the work of BURNOUT on the locally-deployable model, S029 disability-axis CHECK-IN persists across prompt iterations, S031 false-BURNOUT pattern, S024 absent from all 4-axis-family runs) are all supported by the raw JSON. The 2 silent corrections (WB08 Brandon BURNOUT, S031 27B filename _2030→_0034) are correct.

**Where the audit flags concerns: the bracket-reconstruction convention `[completing text]` is inconsistent.** When brackets restore the literal next characters of a cut-off word (e.g., "understand[ing]" → "understanding"), they are accurate. When brackets attempt to summarize or extrapolate the cut-off continuation (e.g., "thoug[h student is still engaging]"), they fabricate model text. The most consequential instance (S029 12B Test O "naming their processing style" vs. actual "typical writing style") substantively misrepresents how the model talks about a neurodivergent student — directly relevant to the paper's disability-axis-sensitivity finding.

**Recommendations to lead author:**
1. **Fix S029 12B Test O quote** — replace fabricated bracket with verbatim continuation: "but it's also possible this is simply the student's typical writing style." This actually strengthens the workshop's argument: the model defaulting to "typical writing style" (rather than the more disability-affirming "naming their processing style") is closer to deficit-shaped framing.
2. **Fix the other 4 bracket reconstructions** (S004 27B 0907; S023 12B Test N; S023 12B Test O; S029 27B 0907 Test N) — either restore verbatim continuation or use plain `[...]` without inserted content.
3. **Correct S031 12B Test N count** from "8/9 BURNOUT" to "9/10 BURNOUT" and update the rationale claim from "verbatim identical across 8 runs from 1113 to 1804" to "9 runs" (verified above).
4. **Optional:** Soften "near-identical" characterization of the 2026-03-29_2107 S002 12B run to "different rationale" or describe what specifically differs.

These corrections do not change the workshop's conclusions or the paper's response options. They tighten the empirical record so that subsequent reviewers can verify each claim against source without finding fabricated bracket content.
