# Audit Report — Instance B
**Session:** data-verification-audit_2026-04-26
**Role:** Independent auditor (no coordination with Instance A before writing)
**Date:** 2026-04-26

---

## 1. Claims Independently Verified Against Raw JSONs

I selected 8 claims with direct stakes for the paper and verified each by opening the raw JSON files directly (not via the verification table or experiment log narrative).

### 1a. Test B (3 runs): S029 = 3/3 FLAG, S002 = 3/3 CLEAR

**Files opened:** all three `test_b_best_concern_gemma12b_*.json`

**Verification result: CONFIRMED.** S029 Jordan Espinoza = FLAG in all three preserved runs; S002 Jordan Kim = CLEAR in all three. The validation pass's correction from "instability" to "deterministic misclassification" is supported by the raw data.

**However, a significant discrepancy requires flagging.** The experiment log narrative at lines 1817–1827 explicitly states that Test B produced S029 = CLEAR in its results table: *"The best possible concern prompt CLEARED EVERY STUDENT."* The raw JSON for the 2026-03-26 file shows S029 = FLAG. When I checked the JSON's provenance field, it reads:

> `'note': 'Retroactively added — commit identified from git log timestamps'`

The validation pass concluded that the "first run cleared everyone" framing was "never accurate" and took the JSON as ground truth. **This conclusion is not warranted given the retroactive provenance.** The experiment log narrative is a contemporary primary source documenting what Test B produced. The JSON may be a later re-run (possibly from 2026-04-14 when the other two Test B files were generated). The validation pass's correction may itself be an error — it replaced a primary-source record with a retroactively-added file.

**What both versions agree on:** S002 = CLEAR in all preserved runs — the true positive is missed regardless. The claim "binary classification cannot be simultaneously sensitive AND equitable" holds under both interpretations. The mechanism differs: "cleared everyone" = over-correction of the threshold; "flagged S029 + cleared S002" = threshold can't protect all equity-critical patterns while catching true positives. Both are binary ceiling evidence; they're not the same evidence.

**Recommendation for the paper:** Do not claim that the "best possible binary cleared everyone" until the JSON provenance is resolved. Alternatively, cite BOTH interpretations: "across preserved Test B runs, the best-possible binary either clears everyone (original run, as documented in the experiment log) or flags the neurodivergent student while clearing the burnout case — in neither version can it be simultaneously sensitive and equitable." The experiment log's own wording is paper-ready; the retroactively-added JSON should be treated as a later replication, not a correction to the original.

---

### 1b. Test C: S023 = CLEAR, S029 = FLAG

**File opened:** `test_c_length_gemma12b_2026-03-26.json`

**Verification result: CONFIRMED.** S023 Yolanda Fuentes = CLEAR; S029 Jordan Espinoza = FLAG; all others = CLEAR. The validation pass correction (drop S023 from the Test C citation) is correct.

---

### 1c. Test F (n=20): S029 = 20/20 FLAG, S002 = 20/20 CLEAR

**Files opened:** both `test_f_bc_stability_gemma12b_*.json`

**Verification result: CONFIRMED.** Both files contribute 10 records each per student. S029 = 20/20 FLAG; S002 = 20/20 CLEAR; all others = 20/20 CLEAR. The validation pass correction (n=20, not n=25) is correct.

---

### 1d. Test A: Gemma 12B MIXED tag on S022 is a measurement artifact; prose is asset-framed

**File opened:** `test_a_temperature_gemma12b_2026-03-26.json`

**Verification result: CONFIRMED.** I read the full raw_output prose for S022 Destiny Williams, run 1. The prose explicitly says: *"Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning."* This is unambiguous asset-framing. The MIXED classification tag on Gemma 12B was a downstream measurement artifact, not a finding about the model's behavior. All five 12B runs carry the same framing; only the automated tag differs.

The verification table's Finding A footnote and the "16/16 across three model families" claim at the prose level are both correct.

---

### 1e. Test D: 7/7 power moves detected

**File opened:** `test_d_power_moves_gemma12b_2026-03-26.json`

**Verification result: CONFIRMED.** All 7 records have `detected: True`. The 7 students are: S018 (corpus_colorblind), S025 (corpus_tone_policing), PM01 (abstract_liberalism), PM02 (settler_innocence), PM03 (progress_narrative), PM04 (meritocracy_deflection), PM05 (objectivity_claim). The 7/7 claim holds. Note: this is a single run; cross-model robustness is not tested.

---

### 1f. Test N S029: Gemma 12B = 10/10 ENGAGED; Gemma 27B = 5/6 ENGAGED, 1/6 BURNOUT

**Files opened:** all 10 Gemma 12B test_n files; all 6 Gemma 27B test_n files

**Verification result: CONFIRMED.** The one BURNOUT result is from `test_n_4axis_submissions_gemma27b_cloud_2026-03-29_0907.json` (run 1 of 6). The model's reasoning in that file: *"Student details multiple cognitive and social challenges (dyslexia, ADHD, first-gen student status, racial bias) and explicitly states the *interaction* of these factors is 'exhausting.' This points to depleted capacity rather than a current crisis."* This is exactly the compression error the experiment log describes (hearing "exhausting" → coding as depletion). The 5/6 vs. 1/6 pattern and the 12B stability finding are correctly stated in the verification table.

---

### 1g. Verification table S023 count: 9× ENGAGED, 2× CRISIS

I noticed the per-student summary for S023 Yolanda Fuentes in test_n_4axis_submissions showed "9× ENGAGED, 2× CRISIS" while my initial reading of the matrix was ambiguous. Verified directly:

- S023 in Gemma 12B runs 1–9: ENGAGED
- S023 in Gemma 12B run 10 (`2026-03-29_2107`): CRISIS
- S023 in Qwen 7B run: CRISIS

Total: 9× ENGAGED, 2× CRISIS. **Verification table count is correct.**

---

### 1h. Rerun original naive concern file

**File examined:** `rerun_original_naive_concern_gemma12b_2026-04-26.json`

**Structure confirmed.** 32 students, 8 flagged: S001, S005, S012, S018, S020, S023, S024, S025. The `concerns` field stores model reasoning.

**Finding:** The rerun confirms the self-contradiction phenomenon persists. The `why_flagged` reasoning for S001, S005, S012, S020, S023, S024 all contain hedged or asset-adjacent language: "While this isn't inherently a wellbeing concern..." (S005, S012, S020); "This is a normal part of the learning process" (S023); "While not a direct wellbeing concern" (S024); "strong application of intersectionality" flagged at conf=0.9 (S001). These are self-contradictions in the original sense: the model's own explanation argues against the flag.

**Notable:** S022 Destiny Williams is NOT flagged in the rerun (was in the original 3/7). This is consistent with explicit guards being added for righteous-anger cases in the refactored code. S002 Jordan Kim also not flagged — consistent with all binary test results.

**Issue with the rerun file's own metadata:** The `note` field says it "uses the production concern_detector." Given the established finding that `detect_concerns()` is research-track code, the note is incorrect on its face. Minor documentation error in the rerun file itself, but worth noting for paper citation: the file should say "research-track binary classifier" not "production concern_detector."

---

## 2. Missing File Hunt

### 2a. Reading-first vs JSON-first comparison (S017/S001/S012): FOUND

**Location:** `/Users/june/Documents/GitHub/autograder4canvas/data/demo_baked/reading_first_comparison.json`  
(also at `/Users/june/Documents/GitHub/Autograder4Canvas/data/demo_baked/reading_first_comparison.json`)

Confirmed three students: S001 Maria Ndiaye, S012 Talia Reyes, S017 Tyler Huang. The file has both "standard" (JSON-first) and "reading_first" outputs for each student. The S017 free_form_reading includes the exact framing cited in the s1 handoff: *"He's demonstrating a thoughtful, considered engagement with the material, prioritizing a clear understanding over performative elaboration."* The s1 handoff's quoted contrast ("lacks personal connection" → "prioritizing clarity over performative elaboration") is present in the data — the "standard" approach has `what_reaching_for: null` while reading_first surfaces the asset frame.

**Paper implication:** This data IS retrievable and citeable. It's in the autograder4canvas codebase under `data/demo_baked/`, not under `output-format-bias/data/raw_outputs/`. The claim in REVIEW_FOR_JUNE that this file has "No file in raw_outputs/. Unknown whether lost or never persisted" is technically correct (not in raw_outputs/) but the file exists and is accessible. Update REVIEW_FOR_JUNE gaps table.

---

### 2b. Observation-only prototype (7 students, 7/7 correct readings): NOT FOUND as JSON

**Search result:** No JSON file for this prototype in raw_outputs/ or either autograder4canvas repo.

**Explicit /tmp/ reference found:** Experiment log line 1770 states: `Results: /tmp/observation_prototype_results.json`. Same /tmp/ fate as the original 3/7 file.

**What does exist:** The experiment log at lines 1455–1465 contains a detailed results table with per-student comparison (binary result vs. observation reading) and quoted observation outputs. This is the surviving record. The quotes in the s1 handoff Level 3 section (S022: "anger is a powerful engine for her understanding", S023: "deep, embodied understanding without needing academic terminology", S028: "striking directness and clarity", S029: "self-awareness about their own learning style") all come from this table, and they survive.

**Paper implication:** The observation-only prototype CAN be cited from the experiment log narrative. The citation should note the data was not separately preserved (like the 3/7 original), that the results are documented in the experiment log at lines 1440–1526, and that the result table is the surviving evidence.

Note: `synthesis_first_prototype.json` in demo_baked has 7 students (S015, S018, S025, S023, S027, S028, S029) but is a thematic coding file, not a welfare concern detection run. It is NOT the observation-only prototype.

---

### 2c. Test E reproduction on Gemma 12B (2026-03-27): NOT FOUND

**Search result:** No `test_e_cross_model_gemma12b_*.json` file in raw_outputs/ or either autograder4canvas repo. Git history search found no such file. The only Test E files are for Qwen 7B and Gemma 27B.

**Assessment:** The s1 handoff's claim "cross-model reproduction (Test E + 2026-03-27 rerun)" appears to conflate two things: Test E (Qwen 7B + Gemma 27B, 2026-03-26) and a separate Gemma 12B observation run that may have been documented in the experiment log narrative but not saved to a distinct test_e-named file. The equity_observations files (`equity_observations_gemma12b_2026-03-30_*.json` and `_2026-03-31_*.json` and `_2026-04-02_*.json`) contain Gemma 12B generative observation runs, but on a different corpus (E001–E016, not S022/S028).

**Paper implication:** The "16/16 across three model families" claim should be itemized: Test A produced 10/10 on Gemma 12B; Test E produced 6/6 on Qwen 7B and 6/6 on Gemma 27B (confirmed files); no separate Gemma 12B test_e file exists. The 16 runs come from Test A (10 12B) + Test E (6 27B + 6 Qwen — wait, Test E cross_model has 6 records for Qwen and 6 for 27B = 12 total, not 16).

**Recalculation flag:** The "16/16 across three model families" claim may need recounting. Test A: 10 Gemma 12B runs (on S022 × 5 + S028 × 5 — two students). Test E cross_model: 6 Qwen 7B + 6 Gemma 27B (on S022 + S028). But that's 22 observation runs across three families, not 16. The "16" figure presumably comes from a different counting. The verification table header says "test_a" = 16 records (n_records: 16 for the last two equity_observations files). This needs resolution.

Actually, looking at the verification table coverage tally: `test_a_temperature` has 2 files with 16 records total (10 + 6 = 16: 10 from gemma12b, 6 from qwen7b). The Gemma 27B test_a has 6 records separately. So 16 generative observation records span Gemma 12B (10) + Qwen 7B (6); Gemma 27B (6) is separate. The "16/16 across three model families" likely counts 10 + 6 = 16 from Test A across the two model files, with the 27B as the "third family" confirmed by Test E. This is confusing counting and should be clarified in the paper.

---

### 2d. Original 32-student naive binary (3/7 source): Confirmed lost

**Status:** Confirmed. The rerun file exists at `data/raw_outputs/rerun_original_naive_concern_gemma12b_2026-04-26.json` and has been run (88.8 minutes, 32 students). See section 1h above.

---

## 3. Things the Validation Pass Missed or Needs Flagging

### 3a. Test B provenance problem (LOAD-BEARING for paper)

As detailed in section 1a: the validation pass replaced the experiment log's Test B narrative (S029 = CLEAR, "cleared everyone") with the raw JSON (S029 = FLAG) without noting the JSON's retroactive provenance. This is a potential new error introduced by the validation pass. 

The paper's "best possible binary cleared everyone" claim comes from the experiment log, which is the primary source. The JSON, retroactively added, may be a subsequent replication under the same prompt conditions. If so, the correction "cleared everyone was never accurate" is itself inaccurate. The paper's core claim is not endangered by either version, but the specific framing matters for the "overshoot vs. false-positive" distinction in the argument structure.

**Recommended action:** Explicitly flag the retroactive provenance in the corrections record. Treat the experiment log narrative as the primary source for what the original Test B produced; treat the JSON files as replication data. The honest claim is "in the original documented run, the best-possible binary cleared everyone including the true positive; in subsequent replications under the same prompt, it consistently flagged S029 while still missing S002." Both are evidence of the binary ceiling.

### 3b. "16/16 across three model families" needs cleaner counting

The 16 generative observation runs may count Test A's Gemma 12B (10) + Test A's Qwen 7B (6). Gemma 27B's 6 runs come from a separate test (test_a_temperature_gemma27b). Test E (cross_model) also has 6 Qwen 7B + 6 Gemma 27B = 12 records but on slightly different students/conditions. The paper should itemize explicitly rather than relying on "16/16" as a simple cross-model count. The verification table has this data; it just needs to be surfaced clearly.

### 3c. Reading-first comparison file is in demo_baked, not raw_outputs/

The REVIEW_FOR_JUNE gaps table says this file is "unknown whether lost or never persisted." It exists. Update the gaps table. The paper can now cite this as preserved evidence.

### 3d. Rerun file metadata says "production" for research-track code

The rerun file's own note says it uses "production concern_detector." Per the established finding, `detect_concerns()` is research-track code. This is a documentation error in the file itself. If the paper cites the rerun, it should use the correct framing: "research-track binary classifier, re-run 2026-04-26."

### 3e. S022 not in rerun flags — evidence of guard efficacy

The rerun does not flag S022 Destiny Williams (righteous anger case). This was one of the original 3 self-contradiction cases. The absence in the rerun is consistent with explicit guards being added, but this also means the rerun cannot serve as a direct parallel to the original 3/7 for S022 specifically. The phenomenon persists (S023, S024 still flagged with self-contradictory reasoning), but the distribution has shifted. The paper's claim about S022 must rely on the experiment log's documented quotes, not the rerun.

---

## 4. Summary of Audit Status

| Claim | Status | Source |
|---|---|---|
| Test B: S029 = 3/3 FLAG (deterministic) | CONFIRMED | Raw JSONs |
| Test B: S002 = 3/3 CLEAR (deterministic miss) | CONFIRMED | Raw JSONs |
| Test B: "cleared everyone" in original run | UNRESOLVED — conflict between log narrative (CLEAR) and retroactively-added JSON (FLAG) | Experiment log primary; JSON retroactive |
| Test C: S023 CLEAR, S029 FLAG | CONFIRMED | Raw JSON |
| Test F: n=20, S029 = 20/20 FLAG | CONFIRMED | Raw JSONs |
| Test A Gemma 12B prose: asset-framed | CONFIRMED | Raw prose read directly |
| Test D: 7/7 power moves | CONFIRMED | Raw JSON |
| Test N 27B S029: 1/6 BURNOUT, 5/6 ENGAGED | CONFIRMED | Raw JSONs |
| Test N 12B S029: 10/10 ENGAGED | CONFIRMED | Raw JSONs |
| Rerun: 8 flags, 6 self-contradictions | CONFIRMED | Raw JSON + concerns field |
| Reading-first comparison file: lost | INCORRECT — FILE EXISTS at autograder4canvas/data/demo_baked/ | Found |
| Observation-only prototype: lost | CONFIRMED LOST — /tmp/ per log line 1770; results documented in log lines 1455–1465 | Experiment log |
| Test E Gemma 12B: missing | CONFIRMED MISSING — no file found anywhere | Thorough search |
| Original 32-student naive binary: lost | CONFIRMED — rerun file now exists | Rerun at raw_outputs/ |

---

*Written by Instance B independently, 2026-04-26. No coordination with Instance A before writing.*
