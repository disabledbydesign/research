# Cross-Reference Verification — ofb_paper_compiled_source_2026-05-09.md

**Date:** 2026-05-12 (overnight pass)
**Verifier:** Claude (read-only)
**Paper version checked:** `ofb_paper_compiled_source_2026-05-09.md` (364 lines)

**Scope:** All internal cross-references — section refs (§I–§VI), Row refs, Table refs, Test refs, footnotes, and "as discussed in X" forward/backward refs. Citation refs (Yosso 2005, etc.) are out of scope; this pass checks only internal pointers to the paper's own structure.

**Headline:** Most refs resolve cleanly. Two genuine breaks (one ❌, one ⚠️-borderline-❌). Several minor inconsistencies worth flagging.

---

## ❌ Broken or missing references

### ❌-1. "tests A–F" on line 97 implies a Test D that does not exist

**Location:** III.C.1, line 97
**Usage:** "anti-bias regex safeguards engineered to address the failures and calibrated through further testing (tests A–F)"
**Target:** The dash-range "A–F" implies six tests A, B, C, D, E, F.
**What actually appears in the paper:**
- Test A (Row 4, generative observation — line 181)
- Test B (Row 2, Table 1 — lines 149, 157)
- Test C (Row 2, Table 1 — lines 149, 157)
- Test D — **never mentioned anywhere in the paper**
- Test E (Row 4, generative observation — line 181)
- Test F (Row 2, Table 1 — lines 149, 157)
- Test M (Row 2, more-robust config — line 151) — sits outside the A–F range entirely
- Tests A and E also referenced in the `[^model-testing]` footnote (line 111)

**Problem:** The "A–F" range is misleading on two fronts:
1. Test D is never enumerated — either it exists in raw notes but isn't reported, or the range should be "A, B, C, E, F."
2. The phrase "calibrated through further testing (tests A–F)" frames *all* of A–F as anti-bias regex calibration tests, but Tests A and E are actually the *generative observation* runs (Row 4), not anti-bias regex calibration. The framing folds two distinct experimental tracks into one range.

**Recommendation:** Either rewrite to enumerate the actually-reported tests, or split the parenthetical to distinguish "binary-calibration tests B, C, F (and M)" from "generative-observation tests A and E."

---

### ❌-2. The "class-wide burnout/academic dishonesty pattern mentioned above" has no clear antecedent in the body

**Location:** IV.B, line 196
**Usage:** "One assignment was a deliberate stress test: the topic was self-care (CITATIONS NEEDED), following the class-wide burnout/academic dishonesty pattern mentioned above."
**Target:** "mentioned above" — points to an earlier discussion.
**What actually appears in the paper:** The only earlier mention is in **I. Introduction, line 21**: "*Autograder does track academic integrity violations, but as population-level and longitudinal signals of burnout — a commitment that solidified when AI-based cheating spiked across courses in week five amid escalating geopolitical conflicts and ICE raids.*"

**Problem:** That sentence in §I introduces the *commitment* to tracking integrity-as-burnout but does not establish a "class-wide burnout/academic dishonesty pattern" as a referenceable phenomenon. The IV.B reference reads as if a specific pattern had been described and named earlier — but it wasn't. There is no §III or §IV.A passage describing a class-wide burnout/academic-dishonesty event the reader can resolve "mentioned above" to.

**Recommendation:** Either expand the I.21 mention into something the reader can later refer back to (e.g., a brief named description of the cheating spike and its read-as-burnout interpretation), or rewrite the IV.B sentence to introduce the context inline rather than gesturing backward. This is a "cross-reference rot" of the same shape as the III.D hallucination caught yesterday: the body claims an antecedent that doesn't fully exist.

---

## ⚠️ Exists but content doesn't match / minor inconsistencies

### ⚠️-1. "Test M" introduced in IV.A.3 has no earlier mention and breaks the alphabetical sequence

**Location:** IV.A.3, line 151
**Usage:** "Test M added more robust safeguards: a more elaborate concern-detection prompt..."
**Target:** Test M itself.
**Status:** Test M is described in place (line 151), so as a forward-defined item it technically resolves. But it is **never listed in [^model-testing]** (line 111, which only names Tests A and E for cross-family work and otherwise mentions "format-effect ablation" generically), and it is not in the "tests A–F" range on line 97.

**Problem:** A reader scanning for Test M's provenance finds no testing-protocol enumeration. The jump from A–F to M with nothing between is unexplained — were there tests G–L too? If so, where? If not, why call it M?

**Recommendation:** Either rename Test M to fit the sequence (Test G?) or add a brief footnote explaining the naming (e.g., "M" for "more robust" / "May" / experiment-log convention).

### ⚠️-2. "Mar 24 baseline" and "Apr 26 reproduction" in IV.A.3 reference experiment-log dates not introduced elsewhere

**Location:** IV.A.3, line 169
**Usage:** "the Mar 24 baseline (per experiment-log narrative; raw output lost) and the Apr 26 reproduction both cleared S029, but the three layers of equity-protective engineering on race and language introduced a new failure mode on disability."
**Target:** Two dated experiment-log entries.
**Status:** These are not paper-internal section references but pointers to an experiment log the reader does not have access to. The line already concedes "raw output lost" for the Mar 24 baseline, so the reader has no way to verify or contextualize either date.

**Problem:** Not a broken reference per se — but a reader cannot evaluate the claim because the antecedent lives in a private experiment log. For a published version, either suppress the dates and report only the comparison ("an earlier baseline and a later reproduction"), or attach a footnote describing what the experiment log is and where (if anywhere) it lives.

### ⚠️-3. Section IV.B's "four-axis classifier misclassified one student in the remaining three assignments" — number doesn't pair cleanly with the corpus described

**Location:** IV.B, line 198
**Usage:** "The four-axis classifier misclassified one student in the remaining three assignments."
**Target:** The four live-data assignments mentioned at IV.B opening (line 194: "I ran four assignments through a research-only pipeline").
**Status:** Numbers do add up (1 stress-test assignment + 3 remaining = 4 total), so structurally OK. ✅ for arithmetic.

But: the sentence is dense and the reader has to do the bookkeeping themselves. The stress-test (self-care) assignment is one; the remaining three are the others; the four-axis classifier misclassified one student across those three. Worth a light edit for clarity, but not a broken reference.

### ⚠️-4. "Crenshaw, 1989; 1991" — the 1991 entry is in-text only

**Location:** V.B, line 222
**Usage:** "(Crenshaw, 1989; 1991)"
**Target:** References section.
**Status:** Crenshaw 1989 *is* in the References (line 286). Crenshaw 1991 is **not** in the References. This is a citation-list issue, not a paper-internal structural ref — but flagging because it's the same shape of rot (body claims something not in target).

### ⚠️-5. Abstract claims "28 runs" for generative observation; body math gives 28 (16 + 12) ✅ — but worth a sanity-check pass

**Location:** Abstract (line 11) vs. IV.A.5 (line 181)
**Usage:** Abstract says "across two model families (Gemma at 12B and 27B; Qwen 7B) and 28 runs."
Body says: "Test A ran 16 passes across Gemma 12B, Qwen 7B, and Gemma 27B; Test E added 12 more across Qwen 7B and Gemma 27B."
**Math:** 16 + 12 = 28. ✅
**Note:** Body Test A spans **three** model families (Gemma 12B, Qwen 7B, Gemma 27B), but abstract says "two model families (Gemma at 12B and 27B; Qwen 7B)" — Gemma 12B and 27B are the same family. So "two families" = Gemma + Qwen. Correct, just a parse-difficulty.

### ⚠️-6. "see IV.A.3" at V.B line 222 vs. "§IV.A.3" elsewhere — formatting inconsistency

**Location:** V.B, line 222: "(see IV.A.3)"
**Compare:** lines 131, 139: "§IV.A.3"
**Status:** Both resolve to the same target ✅. Stylistic inconsistency only — the paper uses both `§IV.A.X` and bare `IV.A.X` for section refs. Worth a copy-edit sweep.

---

## ✅ Verified references (collapsed summary)

All of the following resolve cleanly to existing targets with content matching the body's claim:

| Ref | Location | Target | Match? |
|---|---|---|---|
| "take that up in V.B" | Abstract line 11 | §V.B "The design principle: unbounded protection" (line 220) — discusses residual asymmetry in descriptive register | ✅ |
| "treated in V.B" | I, line 29 | §V.B (line 220) | ✅ |
| "developed in V.B" | I, line 33 | §V.B (line 220) | ✅ |
| "§IV.A" | III.B, line 89 | §IV.A "The Four-Row Ablation" (line 121), built on 32-student synthetic corpus | ✅ |
| "Section IV.B" | III.B, line 91 | §IV.B "Live-Data Deployment" (line 192) | ✅ |
| `[^model-testing]` | III.D, line 109 | Footnote defined line 111, content matches body's claim about cross-family testing | ✅ |
| "Row 1" (minimal binary), "Row 2" (calibrated anti-bias), "Row 3" (four-axis), "Row 4" (generative observation) | IV.A intro line 123 | Row 1 = §IV.A.2 (line 141), Row 2 = §IV.A.3 (line 147), Row 3 = §IV.A.4 (line 173), Row 4 = §IV.A.5 (line 179) | ✅ all four |
| "§IV.A.3 for the verbatim language" | IV.A.1, line 131 | §IV.A.3 line 149 contains the five-equation verbatim block | ✅ |
| "§IV.A.3 will document" (disability-axis pattern) | IV.A.1, line 131 | §IV.A.3 (line 147ff) does document the disability-axis pattern (S029 24/24 false-flag) | ✅ |
| "the calibrated binary tested in §IV.A.3" | IV.A.1, line 139 | §IV.A.3 (line 147) | ✅ |
| "The minimal binary classifier in §IV.A.2" | IV.A.1, line 139 | §IV.A.2 (line 141) | ✅ |
| "Table 1" | IV.A.3, line 155 | Table at lines 157–165: 7-row table with S002, S004, S022, S023, S028, S029, S031 across Tests B/C/F. Body claim "S029 false-flagged 24 of 24" matches table row 6 "24/24 false-flagged" ✅; "S002 cleared 24/24" matches row 1 "24/24 missed" ✅; "S028 cleared 24/24" matches row 5 ✅ | ✅ |
| "see §IV.A.5" | IV.A.4, line 175 | §IV.A.5 (line 179) generative observation | ✅ |
| "residual register pattern V.B describes" | IV.B, line 200 | §V.B does describe the residual register/cushioning pattern (line 228) | ✅ |
| "Rows 1 and 2" | V.A, line 208 | §IV.A.2 (Row 1) and §IV.A.3 (Row 2) | ✅ |
| "Test A" / "Test E" footnote refs | [^model-testing] line 111 | Both defined in §IV.A.5 line 181 (Test A = 16 passes Gemma 12B/Qwen 7B/Gemma 27B; Test E = 12 passes Qwen 7B/Gemma 27B) | ✅ |
| "Tests B, C, and F (24 preserved runs total)" | IV.A.3, line 149 | Table 1 columns: B (3 runs) + C (1 run) + F (20 runs) = 24. ✅ | ✅ |
| Quantitative claim: "S029 false-flagged 24 of 24 runs across Tests B, C, and F" | IV.A.1 line 131, IV.A.3 line 167, V.B line 222, VI line 248 | Table 1 row 6 confirms 3/3 + 1/1 + 20/20 = 24/24 | ✅ |
| "Phase 1" / "Phase 2" | IV.A.1 line 127, IV.A.1 line 139 | Defined in `[^model-testing]` line 111 | ✅ |

---

## Priority fixes for June (ranked)

1. **(❌-2) Fix the "class-wide burnout/academic dishonesty pattern mentioned above" antecedent gap at line 196.** This is the closest in shape to the hallucinated III.D pattern caught yesterday — the body gestures back to a phenomenon it never adequately set up. Either expand the §I.21 sentence into a named context or rewrite IV.B line 196 to introduce the situation inline. Highest priority because a careful reviewer will notice and the fix is small.

2. **(❌-1) Resolve the "tests A–F" range at line 97.** Test D is never enumerated and Tests A/E belong to a different track (generative observation) than the parenthetical implies. Either enumerate ("tests B, C, F, M") or rewrite to separate the calibration and generative tracks.

3. **(⚠️-1) Decide what to do about Test M.** Either rename to fit the A–F sequence or footnote the naming. Currently a reader sees "A–F" and then "M" with no bridge.

4. **(⚠️-4) Add Crenshaw 1991 to the References list** (or drop the "; 1991" from V.B line 222). Same rot-pattern as the III.D hallucination but in the citation list.

5. **(⚠️-2) Decide whether to keep the "Mar 24 baseline / Apr 26 reproduction" dates at IV.A.3 line 169** or generalize them. As written, they reference a private experiment log the reviewer can't access.

6. **(⚠️-6) Stylistic copy-edit pass:** unify `§IV.A.X` vs. bare `IV.A.X` for section references.

---

**Summary stats:** 27+ internal references checked. 2 ❌ broken, 6 ⚠️ flagged (3 substantive, 3 stylistic), remainder ✅. The two ❌ items and the Crenshaw 1991 citation gap are the same *shape* of rot as the III.D hallucination caught 2026-05-10 — body claims an antecedent that doesn't exist or doesn't fully exist. Worth one focused pass.
