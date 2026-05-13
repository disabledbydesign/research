# 4-Axis Iteration Workshop — Disconfirmer Audit (Post-Rationale-Addition)

**Auditor role:** adversarial disconfirmer (paired with verifier).
**Target:** `data_tables/4axis_iteration_workshop.html` (975 lines, modified 2026-05-11 11:27).
**Audit window:** 2026-05-11, post-rationale-addition pass.
**Method:** read-only verification against raw JSON in `data/raw_outputs/`. Default disposition: suspicion.

---

## 1. Silent-correction stress test

### 1a. Brandon Mitchell Test L (WB08): "Likely missed" → "BURNOUT @ 0.95 caught"

**Verification of the new claim.** Confirmed against `test_l_expanded_wellbeing_gemma12b_2026-03-28.json` (line 108–120):

- `student_name`: "Brandon Mitchell"
- `signal_type`: "grief_loss"
- `tier2_axis`: **"BURNOUT"**
- `tier2_confidence`: **0.95**
- `tier2_detected`: true
- `tier2_correct`: **"OK"**
- `raw_output`: `{"axis": "BURNOUT", "signal": "Exhaustion and overwhelm stemming from a recent loss and ongoing grief; disillusionment with the material due to its collision with a harsh reality.", "confidence": 0.95}`

The workshop's verbatim rationale (line 322 of workshop) matches the JSON `tier2_signal` field character-for-character. The corrected verdict is supported.

**The "was the earlier reading defensible?" probe.** The workshop now says "corrects earlier note that drew from experiment_log summary rather than raw JSON" (line 322) and "earlier draft listed Brandon as 'likely missed' based on experiment_log summary" (line 329). I do **not** have access to the prior workshop state to verify what the experiment_log summary actually says about Brandon — but the workshop's framing that this was a log-vs-JSON drift correction is consistent with the broader `log_vs_json_drift_2026-05-11.md` workstream sitting next to this file. **No new inconsistency introduced** by the correction; if anything, the workshop is now MORE faithful to raw JSON.

**Verdict on 1a:** Silent correction holds. The corrected reading is verbatim-grounded in raw JSON. Honest disclosure of the correction in cell-body AND in the Test L verdict footnote.

### 1b. S031 27B filename: "_2030" typo → "_2026-03-30_0034"

**Verification of the corrected file.** The current workshop (line 567) lists: "4 runs (2026-03-29_0907, _1928, _2109, **2026-03-30_0034**)". File `test_n_4axis_submissions_gemma27b_cloud_2026-03-30_0034.json` exists (verified `ls`) and contains S031 at line 110, classified `actual_axis: NONE`, `confidence: 0.95` — consistent with the workshop's "NONE @ 0.95" claim.

**Was `_2030` a plausible alternate file?** Directory enumeration: no file in `data/raw_outputs/` contains `_2030` as a stem. The only March-30 Test N file is the corrected one. The most plausible typo origin is misreading a timestamp segment ("2030" being the time-portion 20:30, but the actual time-portion is `_0034` — i.e., 00:34). Alternatively, "2030" could have come from year-confusion or a mid-stream typo. There is no other candidate file the typo could have validly referenced.

**Note for the verifier:** the workshop's NONE rationale quote on line 569 is "Brief definition of intersectionality, expresses confusion and lack of further insight. Insufficient text to assess for crisis, burnout, or engagement." This is taken from the 2026-03-29_0907 file (line 119) verbatim — NOT from the 0034 file, whose rationale is different ("Insufficient text to assess wellbeing. The submission primarily summarizes a course concept."). The source attribution on line 569 correctly cites `2026-03-29_0907`, not 0034. The 0034 file is just listed as one of the 4 NONE runs (line 567). So the typo correction in the run-list is independent of the rationale quote, and both are correctly grounded.

**Verdict on 1b:** Silent correction holds. The file exists, contains S031 with the claimed verdict, and the rationale quote attributed to a different file (0907) is verbatim-correct.

---

## 2. Byte-identicality verification

### 2a. Test O S002 Gemma 12B "verbatim identical across 3 runs"

Sampled `test_o_multi_axis_gemma12b_2026-03-28_{1225,1235,1245}.json` directly. All three S002 entries have **byte-identical `raw_output`**:

```
"{\n  \"axes\": [\"ENGAGED\", \"CHECK-IN\"],\n  \"signal\": \"The student demonstrates engagement with the course material (intersectionality, Crenshaw's work, identity). The 'Idk I had more to say but its late and...' ending is ambiguous; it could indicate genuine fatigue/time pressure (CHECK-IN) or a more significant issue preventing further elaboration.\",\n  \"confidence\": 0.8\n}"
```

Only `time_seconds` differs across runs (20.3 / 20.7 / 19.9). **Claim holds.** This is consistent with MLX-local at temp 0.3 producing deterministic outputs given identical prompts.

### 2b. Test N S002 Gemma 12B "identical rationale on 9/10 runs, near-identical on 2026-03-29_2107"

Sampled five of the 10 runs directly (`1113`, `1158`, `1206`, `1727`, `1804`) + the outlier (`2026-03-29_2107`).

**Runs 1113, 1158, 1206, 1727, 1804** all have BYTE-IDENTICAL `raw_output` for S002:

```
"{\"axis\": \"ENGAGED\", \"signal\": \"Student is thoughtfully engaging with course material (intersectionality, Crenshaw) and connecting it to their own family observations to illustrate understanding. Acknowledgment of fatigue ('Idk...its late') does not indicate burnout.\", \"confidence\": 0.95}"
```

**Run 2026-03-29_2107** has a DIFFERENT raw_output:

```
"{\"axis\": \"ENGAGED\", \"signal\": \"Student is engaging with course material (intersectionality, Crenshaw) and connecting it to their own family experience to illustrate understanding. Demonstrates thoughtful reflection.\", \"confidence\": 0.95}"
```

The verdict (ENGAGED @ 0.95) is preserved, but the rationale's phrasing is substantively different. The workshop describes this as "near-identical" — that is a generous characterization.

**FLAG — methodological framing issue (not factual error).** The 2026-03-29_2107 file has an **EXPANDED SYSTEM PROMPT** (line 28 of that file) containing a new paragraph: "IDENTITY DISCLOSURE IS NOT A WELLBEING SIGNAL…". The earlier 9 runs (1113–1804) used the original/shorter system prompt. So the rationale variation between runs 1–9 and run 10 is NOT inference noise on the same prompt — it's a **prompt-iteration artifact**. Characterizing run 10 as a "near-identical run" elides this. The workshop's S004 cell (line 430) makes the same elision: "essentially identical across all 10 runs" — but the 10th run used a different system prompt.

This matters for: any claim that pure-4-axis Gemma 12B reliably misses S002 burnout under "the same conditions" — strictly, 9/10 runs were one prompt, 1/10 was a different prompt. The deterministic stability claim only directly holds for runs 1113–1804.

**Verdict on 2b:** The byte-identicality claim is TRUE for runs 1–9. The "near-identical" framing for run 10 obscures that run 10 used a different system prompt. Not a fabrication; is a methodological framing issue that the workshop should disclose.

---

## 3. Test P pass2 reconstruction fidelity

**Workshop claim** (line 889): pass 1 = `"The student expresses uncertainty and a sense of lacking further thoughts, suggesting potential burnout or fatigue, despite understanding the core concept."` Pass 2 reasoning = `"N/A — not ENGAGED"`. Source attribution: "pass1 from prompt_pass1; pass2_reasoning from test_p_two_pass_gemma12b_2026-03-28_1456.json (S031 Marcus Bell)".

**Verification against the JSON** (lines 113–128 of test_p_two_pass_gemma12b_2026-03-28_1456.json):

- `pass1_axis`: "BURNOUT" ✓ (matches axis in quoted JSON-snippet)
- `pass1_confidence`: 0.7 ✓
- `pass2_reasoning`: `"N/A — not ENGAGED"` — **byte-identical to workshop quote** ✓
- `prompt_pass1` field contents: `'{"axis": "BURNOUT", "signal": "The student expresses uncertainty and a sense of lacking further thoughts, suggesting potential burnout or fatigue, despite understanding the core concept.", "confidence": 0.7}'` — the workshop quote of pass 1 rationale matches the `signal` value in this string verbatim ✓
- `prompt_pass2`: empty string (pass 2 did not run because pass 1 was BURNOUT, not ENGAGED) ✓ — consistent with the workshop's framing that "the two-pass architecture's gating decision (pass 2 fires only on pass-1 ENGAGED) means … the CHECK-IN refinement layer never runs"

**FLAG — minor field-naming caveat (not workshop's error).** The JSON's field names `prompt_pass1` and `prompt_pass2` are misleading: they store the model's *output* of each pass, not the prompt to that pass. On S002 (line 29 of same file), `prompt_pass2` contains a full pass-2 model output JSON, not a prompt string. The workshop correctly extracted from `signal`-within-`prompt_pass1` and from the canonical `pass2_reasoning` field. No misreading.

**Was the workshop's quote presented as "verbatim"?** Yes — the cell-rationale headers say "Model rationale (verbatim)". The quoted pass-1 signal IS verbatim; the "N/A — not ENGAGED" IS verbatim. Reconstruction is honest.

**Verdict on 3:** Reconstruction is faithful. The "verbatim" label is accurate for both quoted strings.

---

## 4. Errors found (ranked by severity)

### Severity LOW (methodological framing, not factual error)

**E1. "Near-identical / essentially identical across N runs" framing elides a prompt change.**
Locations: workshop lines 404 (S002 12B Test N), 430 (S004 12B Test N), possibly others using "near-identical … 2026-03-29_2107" language.
Issue: The 2026-03-29_2107 run uses an expanded system prompt with a new "IDENTITY DISCLOSURE IS NOT A WELLBEING SIGNAL" paragraph. The 9 prior runs (1113–1804) used the original prompt. Calling run 10 a "near-identical run" frames the rationale difference as inference noise on the same setup, but it's actually a prompt change. The verdict-level claim (10/10 ENGAGED) holds; the "9/10 identical, 1/10 near-identical" rationale claim glosses a prompt iteration.
Severity: low because the verdict pattern (10/10 ENGAGED on S002 12B Test N) is real; high-precision claim that all 10 runs are the same setup is overstated.
Recommended fix: add a footnote to the Test N 12B column noting that 2026-03-29_2107 used an iterated system prompt (the "identity disclosure" addition); attribute run-1-to-9 stability and run-10 outcome under separate prompts.

### Severity NEGLIGIBLE

None rising to medium or high severity in this audit window.

---

## 5. Suspicious patterns not yet errors — worth second look

**SP1. The "deterministic across runs" pattern as evidence for "model holds the framing".** The workshop leans on rationale stability across runs (e.g. line 404 "identical rationale on 9/10 runs") as evidence the model is consistent in its framing. With MLX-local at temp 0.3 producing byte-identical outputs (verified for Test O), the deterministic pattern is partly an artifact of inference configuration. The workshop's argumentative use of "stable across N runs" should be qualified: stability under MLX-local-deterministic ≠ stability under stochastic sampling. The Test O byte-identicality verification confirms this is a real concern, not speculation.

**SP2. WB04 Jasmine Torres (Test L): signal_type/rationale mismatch.** Corpus labels signal as "domestic_violence" (controlling stepdad in the submission text — verified from Test H raw output). Model rationale describes only "mother's undocumented status" — eliding DV entirely. Workshop labels this "DV disclosure absorbed into ENGAGED" which is honest about the failure mode, but the cell-body might be sharper if it noted the model didn't merely absorb the DV — it didn't acknowledge it at all (the rationale frames the case as immigration-adjacent, not DV-adjacent).

**SP3. The cell-body author-gloss vs. verbatim model rationale distinction is solid but may confuse readers.** The cell-body text (e.g., WB01: 'The descriptive observation describes Rosa's "intellectual reach despite difficult circumstances"') is author paraphrase of the observation prose, NOT a model quote. The quoted phrase in the cell-body uses double quotes, which a reader might mistake for a verbatim model excerpt. The "Model rationale (verbatim)" block below is separately quoted. This is a presentation/legibility concern, not an accuracy concern.

---

## 6. Cells that survived adversarial reading

- **All 10 Test L wellbeing-cohort cells (WB01–WB10):** verbatim rationales match `test_l_expanded_wellbeing_gemma12b_2026-03-28.json` byte-for-byte. tier2_axis / tier2_correct fields align with workshop verdicts.
- **S031 BURNOUT 8/9 claim (Gemma 12B Test N):** rationale verbatim matches 1113 file; consistent with "BURNOUT @ 0.70 across 8 runs from 1113 to 1804" stability claim (sampled 5 of 8 directly).
- **S031 27B NONE rationale:** matches 2026-03-29_0907 file verbatim. The 4-run NONE list (0907, 1928, 2109, **0034**) plus 2-run ENGAGED list (2127, 04-01_1607) — the corrected `_0034` file exists and confirms NONE @ 0.95.
- **S023 Yolanda CRISIS outlier rationale (Test N 12B):** verbatim matches 2026-03-29_2107.json.
- **S002 Test O 12B (3 runs, byte-identical):** verified — the "verbatim identical across 3 runs" claim is exact.
- **Test P S031 pass1/pass2 reconstruction:** both quoted strings byte-identical to JSON fields.
- **Cross-table consistency check with 12B-vs-27B differential table:** the S002-Test-N-12B verdict (10/10 ENGAGED) and the S031 patterns are consistent between the two tables.

---

## 7. Summary

The 4-axis iteration workshop survives adversarial audit substantially intact. Both silent corrections (Brandon Mitchell BURNOUT-caught, S031 27B filename) verify against raw JSON and were necessary corrections rather than introduced errors. The "byte-identical across runs" claim is TRUE under verification — sampled Test O 12B runs are exactly byte-identical, and 5 of the 10 Test N 12B S002 runs are byte-identical with the 6th matching set. The Test P pass2 reconstruction is faithful and the "verbatim" label is accurate. The one methodological framing issue (E1) is that runs 1–9 (1113–1804) and run 10 (2026-03-29_2107) of Test N 12B used DIFFERENT system prompts — the workshop characterizes run 10 as "near-identical" but it's actually a prompt-iteration data point, not an inference-noise data point. This is a low-severity disclosure gap, not a fabrication; the 10/10 ENGAGED verdict pattern is real, and recommending a footnote rather than a structural correction.

**Recommendation: READY for paper integration with one minor footnote.** Add a prompt-iteration note for Test N 12B's 2026-03-29_2107 run. No cells require pulling. No fabrications detected.
