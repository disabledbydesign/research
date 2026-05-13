# T2C3 Generative observation (Tests A+E) — VERIFIER / count-first angle

Source of truth: raw JSON at `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/` (verified byte-identical to the Autograder4Canvas copy: same byte sizes, same SHAs-by-byte-size for all 5 files).

## n = 28 verification

### Raw run tally per JSON

| File | n_runs | S022 runs | S028 runs | Other students | classification field values |
|---|---|---|---|---|---|
| `test_a_temperature_gemma12b_2026-03-26.json` | 10 | 5 | 5 | none | 5×MIXED (all S022), 5×ASSET (all S028) |
| `test_a_temperature_gemma27b_cloud_2026-03-26.json` | 6 | 3 | 3 | none | 6×ASSET |
| `test_a_temperature_qwen7b_2026-03-26.json` | 6 | 3 | 3 | none | 6×ASSET |
| `test_e_cross_model_gemma27b_cloud_2026-03-26.json` | 6 | 3 | 3 | none | 6×ASSET |
| `test_e_cross_model_qwen7b_2026-03-26.json` | 6 | 3 | 3 | none | 6×ASSET |
| **TOTAL** | **34** | 17 | 17 | 0 | 5 MIXED + 29 ASSET |

### Match to "n = 28" claim? **NO.**

Raw count is 34, not 28. Mismatch of +6.

### What is going on with the count?

Critical discovery (count-first): **The Test E cross-model JSONs are byte-identical re-publishings of the Test A cross-model JSONs.** Verified programmatically:

- `test_a_temperature_gemma27b_cloud_2026-03-26.json` and `test_e_cross_model_gemma27b_cloud_2026-03-26.json`: same set of (student_id, run) keys, and `raw_output` is identical for every matching key.
- Same for the qwen7b pair.
- Test E files only differ by adding a `note` field ("Cross-model replication of Test A (temperature/consistency)") and a `reference_model` field (`gemma-3-12b-it-4bit`).

So the 5 listed files contain only **22 unique runs**, not 34, and certainly not 28:

- Gemma 12B: 10 unique runs (S022 × 5, S028 × 5)
- Gemma 27B: 6 unique runs (S022 × 3, S028 × 3)
- Qwen 7B: 6 unique runs (S022 × 3, S028 × 3)
- **Unique total: 22**

Three plausible reconciliations of the workshop's "n = 28":

1. **28 = 10 (Gemma 12B Test A) + 12 (Test E Gemma 27B + Qwen 7B) + 6 phantom runs.** Doesn't match anything in the JSON.
2. **28 = 10 + 6 + 6 + 6 = stops counting after one of the duplicate pairs.** That gives 28 — i.e., Test A counted once for all three models (22) plus Test E counted ONCE for one of the two cross-model files (+6). This would still be inconsistent: it counts Test E qwen7b OR Test E gemma27b but not both, while listing all three models in the column.
3. **28 = experiment_log narrative count: "10/10 consistent" (Test A Gemma 12B) + "12/12 ASSET" (Test E qwen7b + gemma27b, 6 each) + 6 (Test A Gemma 27B or Qwen 7B, the model not double-counted by Test E).** This is the most likely intended arithmetic but it's still a confusing accounting because Test E is the same data as Test A for the cross-model files.

Most defensible count for the column: **22 unique runs across 3 models on 2 students.** "28" is not supportable from the raw JSON under any non-overlapping accounting.

### Numeric verdict

- Claimed n = 28. Raw JSON unique runs across the 5 listed files = **22**. Naive sum of all rows = **34**. Mismatch either direction.

## Per-cell verification (7 student rows; S024 expected "Not tested")

### Critical structural finding before per-cell

**The 5 listed Test A + Test E JSONs contain ONLY S022 and S028.** None of S002, S004, S023, S024, S028, S029, S031 appear in any of these 5 files except S028. The per-cell claims for S002, S004, S023, S029, S031 in the T2C3 column CANNOT be sourced from Tests A + E.

`experiment_log.md` is consistent on this: the Test A table at line ~2261 lists only S022 and S028; the Test E tables at lines ~2377–2387 list only S022 and S028. The other students' "Cleared, asset-framed" observations come from the full-pipeline equity-observation runs (e.g., `equity_observations_gemma12b_*.json`, the 32-student corpus runs documented elsewhere in `experiment_log.md`), NOT from Tests A or E.

This is a load-bearing inconsistency with the workshop's column subtitle: "Tests A + E · n = 28 runs across Gemma 12B, Qwen 7B, and Gemma 27B; asset-framed in every run." If Tests A + E are the cited source, the column actually covers 2 students (S022, S028), not 7. If the column means "generative observation in general," the source-set is broader than Tests A + E and the per-cell claims should cite their actual provenance.

### S024 — verify absence

- Workshop: "Not tested. Not in the observation subset."
- Verify: S024 does not appear as a `student_id` in any of the 5 listed JSONs. **Confirmed absent.**
- **Verdict: matches.**

### S002 — verify burnout surfacing

- Workshop: "Burnout surfaced. Signal recovered without forcing a verdict."
- Tests A + E JSONs (the 5 cited): **S002 is not present in any of them. 0 of 28 (or 34, or 22) Test A/E runs touch S002.**
- The S002 burnout-surfacing finding is real per `experiment_log.md` line 2504–2521 — but it's sourced from the full-pipeline `generate_demo_insights.py` Stage 3b observation pass on the 32-student corpus, NOT from Tests A + E.
- **Verdict: claim is true at the level of "generative observation in general," but NOT supportable from the Tests A + E data the column cites. The column attribution is wrong.**

### S004, S023, S029, S031 — verify asset-framed

- Workshop: all "Cleared, asset-framed" with descriptive sub-claims (strengths surfaced, lived experience treated as evidence, neurodivergent processing read descriptively, minimal effort surfaced as itself).
- Tests A + E JSONs (the 5 cited): **none of these students appear.**
- **Verdict: per-cell claims may be true from other tests (Tests B/C/F generative observations, equity_observations full-pipeline runs), but they are NOT supportable from Tests A + E data. Same attribution error as S002.**

### S022 — verify "Anger read as analytic, not pathological"

Raw spot-check across all 3 models, both run = 1 (full prose read):

- **Gemma 12B run 1** (representative for all 5 runs — see deterministic finding below): "Her emotional relationship to the material is one of righteous anger, and she's expressing it directly and effectively. This isn't 'distress'; it's a passionate response to the ongoing impact of historical and contemporary injustices. The intensity of her feeling is a sign of deep engagement, not a barrier to learning." → **asset-framed; analytic, not pathologized.**
- **Gemma 27B run 1**: "There's a clear and justified anger fueling her response, and she explicitly names that anger as a productive force, pushing against the expectation of detached academic discourse." → **asset-framed; analytic.**
- **Qwen 7B run 1**: "Her writing is charged with anger and frustration, which she frames as a positive force for action." So far asset-framed. But then: "This engagement is both a strength and a challenge, as it can sometimes lead to a more passionate and less nuanced expression of ideas. The teacher might want to be aware of this intensity and encourage Destiny to balance her emotional engagement with more analytical depth." → **soft concern-framing — anger gets read as causing a nuance deficit. Not deficit-framed outright, but tonally pulls in that direction.**
- Verdict for S022: **Mostly asset-framed (Gemma 12B and 27B clearly so; Qwen 7B contains a soft "balance her intensity" concern that doesn't match the workshop's clean "Anger read as analytic, not pathological" framing).**

### S028 — verify "Linguistic register read as competence"

Raw spot-check, run = 1:

- **Gemma 12B run 1**: "She's articulating a keen awareness... with a remarkable ability to describe this as a 'texture'... She's clearly grasping that intersectionality isn't just about adding categories together... The language she uses – 'I'm just gonna be real,' 'hits the same' – suggests a desire for authenticity and a rejection of academic jargon that feels disconnected from lived experience." → **asset-framed; AAVE and informal register read as competence and authenticity.**
- **Gemma 27B run 1**: "Imani is very clearly centering her own experience... I don't see any structural power moves at play here." → **asset-framed; explicitly absolves any power-move read.**
- **Qwen 7B run 1**: Strong asset-framing for the first two paragraphs, but then: *"she's clearly engaged with the material, but her writing also contains a structural power move: 'It's not Black plus girl. It's like a whole different channel that comes with its own static.' While this statement is a powerful and accurate description of her lived experience, it could be seen as a form of abstract liberalism. By framing the experience of being Black and a girl as an inherent and separate 'channel,' it might inadvertently downplay the systemic and structural nature of the discrimination she describes."* This is reproduced byte-identically in all 3 Qwen runs (deterministic). → **NOT clean asset-framing. Qwen 7B labels Imani's intersectional articulation as "abstract liberalism" — a misapplication of a known anti-racist critique category to a Black girl's own intersectional analysis. It does not pathologize Imani's *competence*, but it does pathologize her *framework* by misclassifying it as a power move.**
- Verdict for S028: **Asset-framed on Gemma 12B and 27B. NOT cleanly asset-framed on Qwen 7B — contains a recurring power-move misread (6 out of 6 Qwen runs across Test A + Test E, byte-identical).**

## "Asset-framed in every run" check

For the 5 listed JSONs (S022 + S028 only, since no other students appear):

- 22 unique runs (or 34 if counting duplicates).
- Of those: most are asset-framed. Two specific contamination patterns appear:
  1. **Qwen 7B S022 ×3 runs (×6 if counting Test A + Test E duplicates):** soft "balance her intensity" concern attached to Destiny's anger.
  2. **Qwen 7B S028 ×3 runs (×6 if counting Test A + Test E duplicates):** Imani's intersectional articulation labeled as "abstract liberalism" / "structural power move."
- These don't read as Imani-is-deficit or Destiny-is-distressed (the binary classifier's failure mode) but they DO show that generative observation isn't *cleanly* asset-framed in every run on every model.
- The "asset-framed in every run" claim is **directionally correct but not absolute** — Qwen 7B's outputs add concern-flavored qualifications that the workshop's column note erases.

## Aggregate column claim — "No verdict; observation rather than classification"

- All 5 JSONs use the colleague-register observation prompt (verified system_prompt across all 5 — same opening "You are a thoughtful teaching colleague... You are NOT a grading system, a concern detector...").
- Output is descriptive prose, not categorical.
- However: each result also carries a `classification` field (ASSET / MIXED / DEFICIT). That's a post-hoc keyword classifier — not a verdict the model produced, but it IS a verdict layered on top by `classify_framing()`. So "no verdict" is true at the prompt level; partially false at the artifact level.
- **Verdict: prompt is verdict-free; pipeline adds a downstream framing classifier. Workshop note is fair at the model-output level.**

## Experiment_log vs JSON inconsistencies

1. **experiment_log line 2264–2276** says Test A Gemma 12B produced "10/10 consistent (5/5 MIXED + 5/5 ASSET)." Verified in JSON. ✓
2. **experiment_log line 2389** says Test E produced "12/12 ASSET across both models." Verified: 6 ASSET (gemma27b) + 6 ASSET (qwen7b) = 12. ✓ — but this is the SAME 12 runs already in Test A's gemma27b and qwen7b files. Test E is bookkeeping, not new data.
3. **experiment_log does NOT mention Test A gemma27b or Test A qwen7b separately** — only Test A Gemma 12B is described. The cross-model runs are framed as Test E. This is consistent with the byte-identical duplication finding: there were 22 unique runs; the cross-model 12 were filed under both Test A and Test E names.
4. **Workshop's "n = 28" doesn't match any clean accounting** of Test A + Test E from the JSON or the experiment_log narrative.
5. **Workshop's per-cell coverage of S002, S004, S023, S029, S031 cannot be sourced from Tests A + E** — these students are absent from the 5 listed JSONs. Per-cell claims for those students are real findings but they originate in other tests (equity_observations full-pipeline runs, Tests B/C/F, etc.).

## Cross-dir consistency

Files in `/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs/` and `/Users/june/Documents/GitHub/Autograder4Canvas/data/research/raw_outputs/` have identical byte sizes for all 5 files:

- gemma12b: 129512 bytes both dirs
- gemma27b Test A: 76441 both
- qwen7b Test A: 77552 both
- gemma27b Test E: 76558 both
- qwen7b Test E: 77669 both

The two copies are the same files.

## Deterministic-output footnote (count-first observation)

A count-first finding worth flagging: at temperature 0.3, Gemma 12B produced byte-identical raw_output across all 5 runs for S022 and all 5 runs for S028 (verified by md5 hash). Qwen 7B did the same across all 3 runs for each student. Only Gemma 27B (cloud / OpenRouter) showed genuine run-to-run variation. So the "10 runs" on Gemma 12B and the "6 runs" on Qwen 7B are mathematically 10 identical traces and 6 identical traces — they verify determinism, not independent sampling. This does not break the workshop's claims, but it does mean "n = 28" or "n = 34" overstates the independent-evidence count. **The genuinely-independent evidence base is closer to: 2 students × 5 runs (Gemma 27B has variance) + 2 students × 1 trace (Gemma 12B deterministic) + 2 students × 1 trace (Qwen 7B deterministic) = roughly 10 independent samples + 4 deterministic confirmations.**

## Summary

**Count claim ("n = 28"): not supportable from raw JSON.** Raw rows = 34, unique runs = 22 (Test E gemma27b/qwen7b are byte-identical to Test A gemma27b/qwen7b). The "28" doesn't match either accounting.

**Coverage claim (Tests A + E cover all 7 students except S024): false.** Tests A + E JSONs contain only S022 and S028. The per-cell asset-framing claims for S002, S004, S023, S029, S031 in the T2C3 column are real findings sourced from OTHER tests (equity_observations full-pipeline runs); they should not be attributed to Tests A + E.

**Asset-framed in every run: directionally true with caveats.** Gemma 12B and Gemma 27B are cleanly asset-framed on both S022 and S028. Qwen 7B contains two recurring soft contaminations: a "balance her intensity" concern attached to Destiny's anger (S022 × 3 runs, deterministic) and a "structural power move / abstract liberalism" mislabel attached to Imani's intersectional articulation (S028 × 3 runs, deterministic). These are not the binary classifier's deficit-framing failure mode, but they're not the workshop column's clean "asset-framed in every run" either.

**Recommended workshop revisions:**
1. Either change the column source from "Tests A + E" to a broader citation that includes the equity_observations full-pipeline runs, OR change the per-cell claims to reflect that Tests A + E only cover S022 and S028 (and mark S002/S004/S023/S029/S031 cells as sourced from a different test).
2. Reconcile the n. If Test A and Test E cross-model files share data, count Test E as bookkeeping (not new runs): unique runs = 22. Or, if you want to keep the larger count, n = 34 raw rows. "n = 28" appears to be neither.
3. Either qualify "asset-framed in every run" to acknowledge Qwen 7B's S028 power-move misread, or drop that claim and replace with "asset-framed across Gemma 12B and Gemma 27B; mild concern-framing artifacts on Qwen 7B on S022 and S028."
4. Footnote the determinism: temp 0.3 on local MLX runs produces byte-identical outputs across runs. The independent-sample count is much smaller than the row count.
