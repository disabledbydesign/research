# 4-axis classifier iteration history — workshop students × tests

Date: 2026-05-11
Source: raw JSONs in `output-format-bias/data/raw_outputs/` (verified with Autograder4Canvas mirror)
Workshop students: S002 Jordan Kim (burnout, expected FLAG), S004 Priya V. (strong, CLEAR), S022 Destiny W. (righteous anger, CLEAR), S023 Yolanda F. (lived experience, CLEAR), S024 Ingrid V. (lived experience, CLEAR — but **not tested in any 4-axis-family run**), S028 Imani D. (AAVE, CLEAR), S029 Jordan E. (neurodivergent, CLEAR), S031 Marcus B. (minimal effort, CLEAR)

Note: S024 is absent from all 4-axis-family raw data. The workshop's T2C2 cells for S024 describe outcomes that were never measured.

---

## The four iterations

| Iteration | What the architecture does | Models tested | n runs (workshop students) |
|---|---|---|---|
| **Test L** — 4-axis on observation prose | Run the four-category classifier (CRISIS / BURNOUT / ENGAGED / NONE) on top of the generative-observation output, not on raw student submissions | Gemma 12B | 0 — **only synthetic WB cohort tested, none of the 8 workshop students** |
| **Test N** — pure 4-axis on raw submissions | Same four-category schema, run directly on the student's submission text. Forced single-label choice. | Gemma 12B (10), Gemma 27B cloud (6), Qwen 7B (1) | 17 runs total |
| **Test O** — multi-axis with CHECK-IN flag | Allows concurrent labels from the four categories AND adds a separate CHECK-IN boolean for "teacher might want to look in on this student" — not a wellbeing category | Gemma 12B (3), Gemma 27B cloud (1) | 4 runs |
| **Test P** — two-pass | Pass 1: run Test N's pure 4-axis schema (no CHECK-IN). Pass 2: refine pass-1 ENGAGED cases with a separate CHECK-IN evaluator | Gemma 12B | 7 runs |

---

## S002 Jordan Kim (burnout, expected FLAG) — the central TP question

### Pure 4-axis on raw submissions (Test N)

| Model | Runs | S002 classification |
|---|---|---|
| Gemma 12B (4-bit MLX) | 10 | **10/10 ENGAGED** at 0.95 confidence — every run rejects burnout reading |
| Gemma 27B cloud (OpenRouter) | 6 | **5/6 BURNOUT** (at 0.8 / 0.85 / 0.8 / 0.8 / 0.8) + 1/6 ENGAGED (at 0.9) |
| Qwen 7B (4-bit MLX) | 1 | 1/1 ENGAGED at 0.9 |

S002 caught only by Gemma 27B cloud, and only when no alternative signal exists. Even on 27B, one run drifts to ENGAGED.

### Multi-axis with CHECK-IN (Test O)

| Model | Runs | S002 classification |
|---|---|---|
| Gemma 12B | 3 | **3/3 ENGAGED + CHECK-IN** at 0.8 — wellbeing slot says ENGAGED, but CHECK-IN flag fires |
| Gemma 27B cloud | 1 | 1/1 ENGAGED + CHECK-IN at 0.7 — 27B abandons BURNOUT once given the CHECK-IN option |

S002 caught — but via CHECK-IN flag, not via the BURNOUT wellbeing category.

### Two-pass with CHECK-IN refinement (Test P)

| Model | Runs | S002 classification |
|---|---|---|
| Gemma 12B | 7 | **7/7: pass1 ENGAGED @ 0.95, final ENGAGED + CHECK-IN** — pass 2 catches her every time |

S002 caught reliably via the pass-2 CHECK-IN, not via the wellbeing classification.

---

## Three other findings the workshop doesn't represent

### S031 Marcus Bell (minimal effort, expected CLEAR) — false BURNOUT on pure 4-axis Gemma 12B

| Iteration | Gemma 12B result |
|---|---|
| Test N (8 morning + replication runs 2026-03-28) | **8/9 BURNOUT** at 0.7 |
| Test N (one later run 2026-03-29_2107) | 1/1 ENGAGED at 0.95 |
| Test P (two-pass, 7 runs) | **7/7 pass1 BURNOUT @ 0.7 → final BURNOUT** (the two-pass architecture does NOT undo the misclassification) |

So on the locally-deployable Gemma 12B, pure 4-axis false-flags Marcus as BURNOUT in most runs. The "minimal effort = burnout signal" misreading. The two-pass architecture inherits it because pass 1 is forced-choice. The workshop's T2C2 cell for S031 reads "ENGAGED. Cleared." — that's wrong on Gemma 12B.

Gemma 27B is variable on S031: NONE (in 4 runs), ENGAGED (in 2 runs).

### S029 Jordan E. (neurodivergent, expected CLEAR) — false BURNOUT on Gemma 27B in 1/6 Test N runs

This is the same "5/6 ENGAGED, 1/6 BURNOUT" instability already documented this morning. Visible in the data: `test_n_4axis_submissions_gemma27b_cloud_2026-03-29_0907.json` has S029 = BURNOUT at 0.85. The other 5 Gemma 27B runs have S029 = ENGAGED at 0.9 / 0.95.

Multi-axis with CHECK-IN (Test O) on Gemma 27B: routes S029 to ENGAGED + CHECK-IN at 0.7 — the CHECK-IN flag fires every time even when BURNOUT doesn't.

### S023 Yolanda F. (lived experience, expected CLEAR) — false CRISIS on two pure 4-axis runs

| Iteration | Result |
|---|---|
| Test N Qwen 7B (1 run) | **CRISIS at 0.9** |
| Test N Gemma 12B 2026-03-29_2107 (1 run) | **CRISIS at 0.95** |

These are false positives on the lived-experience axis. The workshop's T2C2 cell for S023 reads "ENGAGED. Lived experience routed to ENGAGED" — that doesn't account for the CRISIS misroutes.

Multi-axis with CHECK-IN (Test O) on Gemma 12B: routes S023 to ENGAGED + CRISIS + CHECK-IN at 0.85 — CRISIS flag fires even in the multi-axis version, on lived-experience.

---

## What this means for the paper

The 4-axis story is more complicated than the workshop's clean "BURNOUT axis correctly caught the true positive" claim.

**On the TP-recovery question (S002):**
- Pure 4-axis on locally-deployable model (Gemma 12B): **misses S002 in 10/10 runs**
- Pure 4-axis on cloud Gemma 27B: catches via BURNOUT in 5/6 runs (forced choice; one run still drifts to ENGAGED)
- Multi-axis with CHECK-IN flag: **catches S002 reliably on both 12B and 27B via CHECK-IN, not via BURNOUT**
- Two-pass with CHECK-IN refinement: **catches S002 reliably on 12B via pass-2 CHECK-IN, not via BURNOUT**

The thing that actually does the work for S002 is the **CHECK-IN flag** — a non-categorical signal that lets the system mark a student for teacher attention without forcing a wellbeing category. Not the 4-axis architecture itself.

**On false positives created by the 4-axis architecture:**
- S031 Marcus: pure 4-axis Gemma 12B false-flags him BURNOUT (8/9 runs). Two-pass inherits.
- S029: 1/6 false-BURNOUT on Gemma 27B. Already in paper.
- S023: false-CRISIS on Qwen 7B and on one Gemma 12B run.

**Paper-revision options:**
1. **Cut the 4-axis sections.** The architecture story collapses under iteration-history scrutiny — what works for S002 is CHECK-IN, not the 4-axis schema, and the 4-axis schema itself introduces NEW false positives on S031 (and arguably S023, S029).
2. **Explain the iteration history honestly.** Frame the 4-axis as a designed sequence: pure 4-axis → multi-axis with CHECK-IN → two-pass with CHECK-IN refinement. The signal that actually catches subtle wellbeing cases is the CHECK-IN axis, layered alongside the wellbeing classification. The 4-axis schema alone does not.

Either approach is defensible. Option 1 is simpler and shorter; option 2 is more methodologically substantive and may strengthen the broader argument (forced-choice categorical classification systematically misses subtle cases; designs need a non-categorical fallback signal).
