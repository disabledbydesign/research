# 12B-vs-27B differential table — VERIFIER audit

**Audit target:** `/Users/june/Documents/GitHub/research/output-format-bias/data_tables/12B_vs_27B_differential_table_2026-05-11.html`
**Date:** 2026-05-11
**Verifier role:** Confirm prompt-difference claim + per-row verdict accuracy + rationale verbatim fidelity + sampling-n framing + comparison-gap rows.
**Method:** Read raw JSON system_prompt and raw_output fields directly. Hash-compare. Verbatim-compare quoted text.

---

## 1. Prompt-difference claim verification (HIGHEST PRIORITY)

### Verdict: CONFIRMED — and the situation is WORSE than the subagent's claim.

The subagent flagged that 27B's Test N system_prompt contains language absent from 12B's ("MATERIAL CONDITIONS... breaking through and limiting their capacity" + "CRISIS supersedes ENGAGED"). I confirm BOTH additions are real and load-bearing. However, the subagent under-described the prompt drift: there are **FIVE distinct system_prompt versions across the 16 Test N JSON files**, not two. The 12B-vs-27B framing is multiply confounded along a prompt-iteration axis.

### Byte-by-byte comparison (the canonical pair: 12B 2026-03-28_1113 vs 27B 2026-03-29_0907)

- **12B prompt:** SHA-256 prefix `7ac35519a697`, length **1459 chars**.
- **27B prompt:** SHA-256 prefix `4d2116b5bca5`, length **2204 chars**.
- IDENTICAL? **No.**

**12B-only language (in BURNOUT bullet):**
> "They're functioning but running on empty. Metacommentary about fatigue, trailing off, apologies for quality."

**27B-only language (in BURNOUT bullet, replacing the above):**
> "They're functioning but running on empty. **The key signal is that the student's MATERIAL CONDITIONS (work schedule, sleep loss, caregiving duties) are breaking through and limiting their capacity. Emotional intensity or personal vulnerability in the writing is NOT burnout — a student who writes passionately about painful experiences and reflects on the process ('this is what I needed to write') is deeply engaged, not depleted.**"

**27B-only language (added as a new paragraph after the critical-distinction paragraph):**
> "**CRISIS supersedes ENGAGED:** If a student discloses domestic violence, housing loss, food insecurity, or immigration enforcement threat — even while maintaining strong analytical engagement with the assignment — classify as CRISIS. A student can be intellectually engaged AND in crisis. The presence of crisis-level content in the student's OWN life is the determining factor, not whether they also engaged with the reading."

The subagent's quoted text matches the raw JSON character-for-character.

### Wider prompt-drift catalog (NOT flagged by subagent)

| Hash prefix | Length | Files using it | What it adds |
|-------------|--------|----------------|---|
| `7ac35519a697` | 1459 | 9× 12B (all 2026-03-28 12B runs) | Baseline / shortest prompt. NO "material conditions" clause, NO "CRISIS supersedes" |
| `4d2116b5bca5` | 2204 | 2× 27B (03-29 0907, 03-29 1928) | Adds "material conditions" + "CRISIS supersedes" |
| `93f4769ad4ef` | 2918 | 1× 12B (03-29 2107) + 1× 27B (03-29 2109) | Adds "material conditions" + "CRISIS supersedes" + **"IDENTITY DISCLOSURE IS NOT A WELLBEING SIGNAL"** paragraph |
| `0dbf57133a8a` | 3199 | 1× 27B (03-29 2127) | Slightly different "IDENTITY DISCLOSURE ALONE" + "Wellbeing signals require..." formulation |
| `d3e281bb333a` | 3987 | 2× 27B (03-30 0034, 04-01 1607) | All of the above + **"MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE"** paragraph |

The prompt evolved iteratively over the Test N campaign. Only ONE prompt version (`93f4769a`) was run on BOTH 12B and 27B (a single run each: 12B 03-29_2107 and 27B 03-29_2109). The other 14 runs are paired model-with-prompt: 12B never sees the strengthened prompts run on 27B; 27B never sees the baseline 12B prompt.

### Why this matters for the paper claim

The single 12B run on the strengthened prompt (`93f4769a`, file 2026-03-29_2107) produced a **CRISIS @ 0.95 misclassification on S023 Yolanda** — a false positive that 12B never produced under the original prompt. So the only data point where 12B sees a prompt close to what 27B was tested on shows 12B ALSO becomes less reliable on the equity case. This single run is consistent with "stricter burnout prompt → more FPs on identity-disclosure cases" being a prompt effect, not a model-scale effect.

The HTML rationale block on the Test N S002 row DOES flag this prompt-confound (lines 590) — credit there. But:
1. It treats it as a two-prompt situation when it is actually a five-prompt iteration.
2. It does not surface the S023 "12B-under-strengthened-prompt CRISIS FP" datapoint, which is the most direct evidence that the prompt drift drives misclassification independent of model scale.
3. The preamble callout (line 287-289) on "inference-setup confound" should be expanded to "inference-setup + prompt-iteration confound."

---

## 2. Per-row verdict accuracy (13 rows)

For each row I verified the 12B-result-cell and 27B-result-cell claims against raw JSON. Findings:

### Row 1 — Round 3 standard pipeline
- Cells cite experiment_log narrative, not structured JSON. Rationale-note correctly flags this.
- **Status:** Unverifiable at raw-JSON level. Rationale-note is honest about this.

### Row 2 — Round 3 standard pipeline (no class context)
- Same constraint. 12B "Not tested" claim is consistent with file inventory (no 12B-no-context Round 3 JSON).
- **Status:** Unverifiable at raw-JSON level. Honestly framed.

### Row 3 — Round 3 replication study
- Same constraint.
- **Status:** Unverifiable at raw-JSON level. The rationale-note correctly points readers to the 2026-04-26 naive rerun for verbatim S025 rationale.

### Row 4 — Test A temperature
- 12B Test A S022: classification = **MIXED** for all 5 runs. ✓ matches HTML.
- 12B Test A S028: classification = **ASSET** for all 5 runs. ✓ matches HTML.
- 27B Test A S022 + S028: Test A 27B file is `test_a_temperature_gemma27b_cloud_2026-03-26.json` — but the HTML's Test A row says "27B: 3 runs/student" and pulls 27B quote from Test E. This is consistent.
- Verbatim quote of 12B S022 prose: HTML quotes *"Destiny is powerfully connecting the theoretical framework of intersectionality to a deeply felt, ongoing reality of systemic injustice…"* — verified character-by-character against `test_a_temperature_gemma12b_2026-03-26.json` raw_output. ✓
- **Status:** VERIFIED.

### Row 5 — Test E cross-model
- Test E 27B S022 classification = **ASSET**, 3/3 runs. ✓
- HTML quotes 27B S022 prose: *"Destiny is powerfully connecting the theoretical framework of intersectionality to very concrete, historical, and ongoing realities…"* — verified verbatim against `test_e_cross_model_gemma27b_cloud_2026-03-26.json`. ✓ (HTML normalizes curly quotes to straight quotes; substance is verbatim.)
- HTML quotes 12B S028 prose (from Test A as reference): verified verbatim.
- **Status:** VERIFIED.

### Row 6 — Test K enhancement-tier prose quality
- **DISCREPANCY.** HTML cell says "Gemma 27B free = **8/10**." The 2026-03-29 rerun file `test_k_enhancement_comparison_multi_model_2026-03-29_1113.json` shows **gemma27b_free total = 6/10**, not 8. The 2026-03-28 file shows gemma27b_free = **8/10**. So the cell's "8/10" claim is from the earlier file, but the HTML's per-dimension breakdown ("structural 2, language-justice 2, relational 2-3, pedagogical 2, anti-spotlighting 0") mismatches the 2026-03-28 scores: actual 2026-03-28 dimensions are `structural_naming: 2, language_justice: 1, relational_analysis: 3, pedagogical_depth: 2, anti_spotlighting: 0`. So "language-justice 2" should be **1**.
- The rationale quote in the rationale block is from the 2026-03-29 file (verbatim verified) — but the score claim is from the 2026-03-28 file. The rationale-source line names only the 2026-03-29 file. **The cell silently mixes two files.**
- HTML claim "(best scoring model)": in 2026-03-28, gemma27b_free=8 was tied for top with no model above. In 2026-03-29, Step Flash=9 beat gemma27b_free=6. So "best scoring model" is true only for the 2026-03-28 run.
- **Status:** PARTIALLY ACCURATE. Recommend rewriting cell to specify which run produced 8/10 and acknowledging the rerun's lower score.

### Row 7 — Test N S002
- 12B: 10/10 ENGAGED across 10 files. ✓ (Confidence values: 0.95 in all 10 runs.)
- 27B: 5/6 BURNOUT + 1/6 ENGAGED. ✓ (BURNOUT in 0907, 1928, 2127, 30_0034, 04-01_1607 = 5 files; ENGAGED in 2109 = 1 file.)
- HTML says "5 runs BURNOUT @ 0.80-0.85" — confidence values for the 5 BURNOUT runs are: 0.8, 0.85, 0.8, 0.8, 0.8 → range 0.80-0.85 ✓.
- Verbatim 12B S002 rationale: matches `test_n_4axis_submissions_gemma12b_2026-03-28_1113.json` raw_output. ✓
- Verbatim 27B S002 BURNOUT rationale: matches `2026-03-29_0907.json`. ✓ (HTML strips the ```json``` code fence and confidence written as `0.80` vs raw `0.8` — substance verbatim.)
- **Verbatim 27B S002 ENGAGED rationale (the 1/6 miss)**: HTML quote begins `{axes: [ENGAGED], signal: ...}`. **The raw_output for `2026-03-29_2109.json` S002 actually uses `"axis": "ENGAGED"` (singular, string), NOT `"axes": ["ENGAGED"]` (plural, list).** This is a **rationale fidelity break**. Confidence value in raw is `0.9`; HTML writes `0.90`. The substantive signal text is verbatim faithful, but the `axes`/`axis` schema mismatch suggests the subagent may have confused this Test N output with Test O's schema (Test O does use `axes` as a list).
- **Status:** VERIFIED except for one schema typo in the 1/6 ENGAGED rationale quote.

### Row 8 — Test N S029
- 12B: 10/10 ENGAGED. ✓ (Confidence 0.90 across 9 files; 0.95 in the 2026-03-29_2107 file with the strengthened prompt.)
- 27B: 5/6 ENGAGED + 1/6 BURNOUT (BURNOUT in 0907 only). ✓
- Verbatim 12B S029 rationale: matches `2026-03-28_1113.json` raw_output. ✓
- Verbatim 27B S029 BURNOUT rationale: HTML quote vs raw — HTML drops the asterisks around `*interaction*` in raw_output (`"interaction"` vs `"*interaction*"`). Minor formatting normalization, content faithful. ✓
- Rationale-note correctly flags the prompt-confound for the S029 case.
- **Status:** VERIFIED.

### Row 9 — Test N other students (S004, S022, S023, S028, S031)
- 12B S004: 10/10 ENGAGED ✓
- 12B S022: 10/10 ENGAGED ✓
- 12B S023: HTML claims **9/10 ENGAGED + 1/10 CRISIS**. Verified: 9 of 10 files = ENGAGED; the 2026-03-29_2107 file = CRISIS @ 0.95. **The 1/10 CRISIS is the run with the strengthened prompt (`93f4769a`)** — this is the data point I flagged in Section 1. The HTML treats it as a 12B reliability finding; it is more accurately a "12B-under-strengthened-prompt produces CRISIS FP on identity-disclosure case" finding, supporting the prompt-confound hypothesis.
- 12B S028: 10/10 ENGAGED ✓
- 12B S031: HTML claims **8/9 BURNOUT @ 0.70 + 1/9 ENGAGED**. Actual: **9/10 BURNOUT + 1/10 ENGAGED** (9 BURNOUT runs all under original prompt; 1 ENGAGED under strengthened prompt). HTML "n=9" is incorrect — n=10 runs exist (10 12B Test N files). Note: confidence is `0.7` in raw, HTML writes `0.70`.
- 27B S004: 6/6 ENGAGED ✓
- 27B S022: 6/6 ENGAGED ✓
- 27B S023: 6/6 ENGAGED ✓
- 27B S028: 6/6 ENGAGED ✓
- 27B S031: HTML claims **4/6 NONE + 2/6 ENGAGED**. Actual: 4/6 NONE (in 0907, 1928, 2109, 30_0034) + 2/6 ENGAGED (in 2127, 04-01_1607). ✓
- **Status:** VERIFIED except for the 12B S031 n=9 vs n=10 miscount.

### Row 10 — Test O multi-axis
- 12B Test O S002: 3/3 ENGAGED + CHECK-IN. Verified verbatim in `test_o_multi_axis_gemma12b_2026-03-28_1225.json`. ✓
- 27B Test O S002: 1/1 ENGAGED + CHECK-IN. Verified verbatim in `test_o_multi_axis_gemma27b_cloud_2026-03-29_2127.json`. ✓
- **Status:** VERIFIED.

### Row 11 — Test P two-pass
- Test P 12B-only claim: verified — 7 `test_p_two_pass_gemma12b_*` files exist, no 27B counterpart in the data directory.
- Test P S002 pass1 + pass2 rationale: pass1_axis = ENGAGED @ 0.95, pass2_checkin = true. Verbatim quote of pass2 reasoning matches `test_p_two_pass_gemma12b_2026-03-28_1456.json` (HTML truncates at "warrant a brief, supportive check-in." — the raw continues "perhaps a quick 'Hope you're doing well, Jordan! Great connection you made about your family.'"). Truncation is acceptable for a rationale block; not a fidelity break.
- **Status:** VERIFIED.

### Row 12 — Test Q 27B counterfactual probes
- Test Q 27B-only claim: verified — 2 `test_q_27b_probes_*` files exist, no 12B counterpart.
- File 1 (2026-03-29_1111.json): 4 probes — Q0=BURNOUT, Q1=ENGAGED, Q2=ENGAGED, Q3=ENGAGED → **1 BURNOUT + 3 ENGAGED** ✓
- File 2 (2026-03-29_1918.json): 6 probes — Q0=BURNOUT, Q1=ENGAGED, Q2=ENGAGED, Q3=ENGAGED, Q4=ENGAGED, Q5=BURNOUT → **2 BURNOUT + 4 ENGAGED** ✓
- Combined claim: "3/10 BURNOUT, 7/10 ENGAGED" — sums correctly.
- **Caveat the HTML doesn't surface:** File 2 re-runs Q0–Q3 (same probes) and adds Q4–Q5. Treating these as 10 independent probes double-counts the baseline (Q0 appears in both files). The honest unique-probe count is 6 (Q0–Q5), with Q0–Q3 having 2 runs each. The "3/10 → 7/10" combined ratio is arithmetically right but methodologically conflates re-runs with new probes.
- Verbatim Q0 / Q1 / Q2 rationales: verified against raw_output fields in both files.
- **Status:** VERIFIED with one framing caveat to flag.

### Row 13 — Live-data runs
- All live-data files in `data/dual_binary_run_*` are 12B-only (verified by directory listing).
- No 27B live-data run exists. FERPA constraint stated in HTML is consistent with project's stated DPA situation.
- **Status:** VERIFIED.

---

## 3. Rationale fidelity (sampling across pairs)

### High-priority pairs (Test N S002 + S029) — fully sampled

**S002 12B (10 runs):** All 10 runs produce **byte-identical** raw_output under the 9-file prompt-7ac35519 cluster (SHA-256 prefix `89b9497aa481` for all 9). The 10th run (2026-03-29_2107, prompt 93f4769a) produces a different output but same axis. So the HTML's "representative" 12B S002 rationale is not just representative — it is the EXACT raw_output of 9 of the 10 runs.

**S002 27B (5 BURNOUT runs):** raw_output hashes are all DIFFERENT (`e6851587c6db`, `78ffe8af74ca`, `7a9f512f9380`, `96ff5ab4d810`, `d7ca36974d11`). So the HTML's "representative" 27B BURNOUT rationale is one specific run, not byte-identical across the 5. The HTML's phrasing "representative 5/6 catch... with reasoning anchored on 'brief, unfinished,' 'lateness,' 'time constraints,' 'material conditions'" is fair — the 5 BURNOUT rationales share thematic anchors even though wording varies.

**S029 12B (10 runs):** Same pattern — 9 runs byte-identical (`586947a88e9a`); 1 run under strengthened prompt diverges. HTML quote is representative of the 9-file cluster.

**S029 27B (1 BURNOUT run, 5 ENGAGED):** The 1 BURNOUT run quoted is unique and accurately quoted (with minor asterisk normalization).

**No evidence of cherry-picking.** The Test N rationale quotes are drawn from canonical/representative runs and accurately represent the population.

### Other pairs (Test A, E, O, P) — spot-checked

All 4 spot-checks (Test A 12B S022, Test E 27B S022 + S028, Test O 12B+27B S002, Test P 12B S002) passed verbatim with minor unicode/whitespace normalization that does not affect substance.

### One schema fidelity break (Test N S002 ENGAGED 1/6 run)

HTML quotes `{axes: [ENGAGED], ...}`. Raw is `{"axis": "ENGAGED", ...}`. Singular string, not list of axes. The subagent likely cross-pollinated Test O's `axes: list` schema into the Test N rationale. The substantive signal text is verbatim. Recommend fixing to match raw schema.

### One asterisk-stripping (Test N S029 27B BURNOUT)

HTML quote drops the `*interaction*` markdown asterisks from raw_output. Minor; recommend restoring for true verbatim.

---

## 4. Byte-identicality + n-framing audit

### Verified at raw-JSON level

**Gemma 12B 4-bit MLX at temp 0.3 is deterministic across runs (within same prompt).** I confirmed this empirically:

- Test N S002 12B: 9 of 10 runs produce SHA-256-identical raw_output (`89b9497aa481`). The 10th run uses a different system_prompt and produces different output.
- Test N S029 12B: 9 of 10 runs produce SHA-256-identical raw_output (`586947a88e9a`). Same pattern.
- Test N S004/S022/S028: same pattern (all 9 same-prompt runs return identical text + identical confidence).

**Gemma 27B cloud is NOT deterministic.** Even within identical system_prompts, raw_output hashes differ across runs:
- S002 27B runs 0907 + 1928 share prompt hash `4d2116b5` but produce different raw_output hashes (`e6851587` vs `78ffe8af`).
- Same pattern for S029 27B and other students.

### Implications for the table's n-framing

The HTML uniformly reports "Gemma 12B n=10 runs" and "Gemma 27B n=6 runs." This is technically the count of times the model was invoked but **dramatically misrepresents independent samples**:

- For 12B Test N S002 / S029 / S004 / S022 / S028: effective independent samples = **2** (9 byte-identical + 1 with different prompt), not 10.
- For 12B Test N S023 / S031: effective independent samples = **2** (9 byte-identical of one verdict + 1 different-verdict run on strengthened prompt).
- For 27B Test N: 6 calls produce 6 distinct outputs — n=6 is a reasonable sample-size count, but cloud sampling stochasticity is bounded by OpenRouter's parameters which are not under our control.

The "12B more reliable" framing is amplified by the byte-identicality: 12B produces the same answer 10 times because it is deterministic at this temperature/quantization, NOT because it has independently converged on a robust verdict. Reliability and determinism are different claims; the table conflates them.

**Recommended n-framing change:** Replace "n=10 runs" for 12B with "n=10 invocations, all deterministic-byte-identical except where prompt differed (effective n=2 distinct samples)." Or footnote a single global caveat. The "12B more reliable than 27B at run-to-run consistency" claim in Row 3 should be scoped to: "given deterministic MLX inference at temp 0.3 with quantization-bounded sampling, 12B produces identical outputs; cloud 27B exhibits sampling stochasticity. This is a property of the inference setup, not a model-scale reliability claim."

This is consistent with the inference-setup-confound callout already in the preamble (line 287-289), but the body cells do not propagate the caveat into their n-counts.

---

## 5. Comparison-gap rows

### Test P (12B-only)
- Verified: 7 files all `test_p_two_pass_gemma12b_*`. No 27B Test P file exists. ✓

### Test Q (27B-only)
- Verified: 2 files both `test_q_27b_probes_*`. No 12B Test Q file exists. ✓

### Live-data (12B-only)
- Verified: 3 directories `dual_binary_run_2026-04-27_ETHN1_*` all 12B. No 27B live-data run. FERPA rationale stated is consistent with the project's data-protection situation. ✓

### Other gaps not surfaced

- **Test M production detector**: only 12B file exists (`test_m_production_detector_gemma12b_2026-03-28.json`). No 27B counterpart. The HTML table does not include a Test M row — possibly out-of-scope, but it is a 12B-only experiment not flagged in the comparison-gap rows.
- **Test R wellbeing/concern synthetic (2026-05-10)**: only 12B file exists (`test_r_wellbeing_concern_synthetic_gemma12b_2026-05-10_2119.json`). Recent test; may have been excluded because it postdates the table's planning date, but it is a 12B-only experiment relevant to the comparison.
- **Test variants A1/A2/B (2026-05-11)**: only `test_variant_*_observation_2026-05-11.json` files exist; all appear to be observation-format tests. Not labeled with model in filename — need to inspect content to verify.

The table's stated gaps are accurate; there are 2-3 additional 12B-only experiments (Test M, Test R, Test variants) the paper may want to name in the comparison-gap framing.

---

## 6. Summary

**Prompt-difference verification result: CONFIRMED, and worse than originally claimed.** The 27B Test N system_prompt contains "MATERIAL CONDITIONS... breaking through and limiting their capacity" and "CRISIS supersedes ENGAGED" — both absent from 12B's baseline prompt — exactly as the subagent flagged. But the situation is iterative: there are FIVE distinct prompt versions across 16 Test N JSONs, and only ONE prompt was run on both 12B and 27B (a single run each). The "12B vs 27B" framing is multiply confounded along a prompt-iteration axis on top of the already-flagged 4-bit-MLX-vs-cloud-fp16 inference axis. Most consequential: the lone 12B run under a strengthened prompt produces a CRISIS @ 0.95 false positive on S023 (the prompt drift demonstrably affects 12B too), which the HTML treats as a 12B reliability finding rather than as evidence FOR the prompt-confound hypothesis.

**Per-row accuracy: 13/13 rows broadly correct on direction; 4 row-level discrepancies to fix.** Test K cell mixes scores from 2026-03-28 with prose from 2026-03-29 and reports "language-justice 2" when raw is "1." Test N "other students" 12B S031 cell reports n=9 when n=10. Test N S002 ENGAGED 1/6 rationale schema-confuses Test N's `axis: string` with Test O's `axes: list`. Test Q's "10 probes" framing double-counts Q0 (rerun across both files).

**Rationale fidelity: high.** Verbatim quotes verified against raw_output for Test A, Test E, Test N S002/S029/S031, Test O S002, Test P S002, Test K gemma27b_free, Test Q baseline+ablations. Minor unicode/whitespace normalization throughout (curly→straight quotes, asterisk stripping); no substantive paraphrase. No evidence of cherry-picking — Test N S002 12B and S029 12B "representative" rationales are byte-identical to 9 of 10 actual runs.

**Byte-identicality finding: load-bearing for the paper.** 12B at temp 0.3 is deterministic — same prompt yields byte-identical output. "n=10" 12B sample sizes are descriptive (number of invocations), not inferential (independent samples). Effective independent samples for 12B Test N is 2 distinct prompts → 2 distinct outputs per student. 27B cloud is NOT deterministic (different output hashes under same prompt). The "12B more reliable" claim becomes "12B produces the same answer when given the same prompt, because MLX 4-bit at temp 0.3 is effectively deterministic" — that is true and unsurprising. It is not a model-reliability claim.

**Confidence in audit: high on prompt-confound (direct character-level verification); high on per-row verdict directions; high on rationale fidelity; medium-high on the "honest claim scope" the synthesis callout already names.** Recommend revising HTML to: (a) expand inference-setup-confound callout to acknowledge five-version prompt drift, (b) fix the 4 row-level discrepancies, (c) reframe 12B "n=10" cells as "n=10 invocations, deterministic-byte-identical within prompt; effective n=2 distinct samples across the prompt-iteration axis," (d) explicitly name S023's CRISIS-under-strengthened-prompt as evidence of the prompt-confound mechanism. The synthesis callout (line 880) is approximately right and should be tightened with the five-prompt observation.
