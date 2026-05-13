# Experiment log vs. raw JSON — known divergences + missing data tracker

Date: 2026-05-11 evening
Source: Pass 2 (2026-04-25), Pass 3 (2026-04-26), Pass 8 morning swarm (2026-05-11), Pass 8b iteration history (2026-05-11 afternoon)

This doc consolidates **where the experiment_log narrative differs from raw JSON**, and **which runs are referenced in the log but have no preserved JSON**. Single scannable source for June's review.

## Source-of-truth framework (corrected per June 2026-05-11 evening)

JSON is not blanket-authoritative. The correct framing:

| Situation | Source of truth |
|---|---|
| **JSON exists + log agrees** | Both consistent; cite either |
| **JSON exists + log disagrees** | **JSON wins** — log has known errors (Test B/C tables, line 1817-1870) |
| **JSON does NOT exist + log is the only record** | **Log narrative is what we have**, with caveat about retroactive provenance — Pass 3 found that even existing JSONs are sometimes retroactively committed, so even "preserved" data has provenance complications |

The missing-data items in Part 2 below are NOT "we don't know what happened." They are "log narrative is the only record; trust it within the limits of retroactive-provenance uncertainty." Different epistemic situation than the drifts in Part 1.

Corrections are applied surgically without deleting historical context (per "mark + correct, don't delete" direction).

## Other authoritative narrative sources (to cross-reference where log is the only record)

Per June 2026-05-11 evening — there are FOUR session_log files we hadn't been treating as canonical:
- `Autograder4Canvas/docs/research/session_log.md` (active state file)
- `output-format-bias/research/session_log.md` (likely mirror — needs verification)
- `Autograder4Canvas/docs/research/logs/session_log_2026-04-02.md` (archived April snapshot)
- `output-format-bias/research/logs/session_log_2026-04-02.md` (likely mirror — needs verification)

These are agent-startup state files (test-monitor skill convention). The current `Autograder4Canvas/docs/research/session_log.md` contains material we hadn't surfaced — most notably the **Variant A test from 2026-05-11**: the test designed earlier today ran successfully (97.8 min, all 4 conditions × 3 MLX models × 8 students × n=1). Outputs at `output-format-bias/data/raw_outputs/test_variant_*_2026-05-11.json`. A coding workshop at `output-format-bias/variant_a_coding_workshop_2026-05-11.html` awaits lead-author hand-coding.

Important caveat: line 116 of the current `Autograder4Canvas/docs/research/session_log.md` claims *"Experiment log: ~6800+ lines. All entries verified against raw JSON."* This claim is now **known false** — Pass 2 / Pass 3 / Pass 8 all flagged the Test B/C tables (uncorrected as of 2026-05-11 evening). The session_log's "verified" claim is itself a piece of stale documentation worth correcting.

---

## Part 1: Experiment_log narrative that contradicts raw JSON

### Drift 1: Test B results table mis-marks S029 ★★★ (FLAGGED 3x; UNCORRECTED in original)

**Where**: `output-format-bias/research/experiment_log.md` lines 1817-1827 + mirror at `Autograder4Canvas/docs/research/experiment_log.md` (byte-identical)

**Log narrative says**:
> Table shows S029 Jordan Espinoza = CLEAR. Narrative at line 1870 reads: "Test B cleared S023 and S029, while Test C flagged them."

**Raw JSON says**:
- `test_b_best_concern_gemma12b_2026-03-26.json`: S029 = FLAG (3/3 runs)
- `test_b_best_concern_gemma12b_2026-04-14_1211.json`: S029 = FLAG
- `test_b_best_concern_gemma12b_2026-04-14_1216.json`: S029 = FLAG
- All Test B runs across all three preserved JSONs flag S029.

**Verdict**: Log table is **wrong**. Flag should be FLAG, not CLEAR.

**Validation history**: Flagged by Pass 2 (2026-04-25 REVIEW_FOR_JUNE), re-flagged by Pass 3 (2026-04-26 Audit Report A Finding 2), re-flagged by Pass 8 (2026-05-11 PUNCH_LIST item 21). Corrections appendix at log line 6721+ documents the correct values; **original table at 1817-1827 was never edited**.

**Status**: Inline correction marker applied 2026-05-11 evening — see [Part 3](#part-3-corrections-applied) below.

---

### Drift 2: Test C results table mis-marks S023 ★★★ (FLAGGED 3x; UNCORRECTED in original)

**Where**: `output-format-bias/research/experiment_log.md` line 1857 + mirror

**Log narrative says**:
> Table shows S023 Yolanda Fuentes = FLAG.

**Raw JSON says**:
- `test_c_length_gemma12b_2026-03-26.json`: S023 = CLEAR. Only S029 was flagged in Test C, not S023.

**Verdict**: Log table is **wrong**. S023 should be CLEAR, not FLAG.

**Validation history**: Same as Drift 1 — flagged Pass 2, Pass 3, Pass 8. Corrections appendix documents correct values; original table never edited.

**Status**: Inline correction marker applied 2026-05-11 evening — see [Part 3](#part-3-corrections-applied).

---

### Drift 3: Test B narrative at line 1870 mis-summarizes the table

**Where**: `experiment_log.md` line 1870 (in both copies)

**Log narrative says**:
> "Test B cleared S023 and S029, while Test C flagged them."

**Raw JSON says**:
- Test B: S023 = CLEAR (correct in narrative); S029 = FLAG (narrative wrong about Test B)
- Test C: S023 = CLEAR (narrative wrong about Test C); S029 = FLAG

So the narrative is wrong on two of four data points. The correct narrative would be: "Test B and Test C both flagged S029 (false positive on neurodivergent case); both cleared S023 (lived experience correctly cleared)."

**Status**: Inline correction marker applied — see [Part 3](#part-3-corrections-applied).

---

### Drift 4: "16/16 across three model families" conflates two tests

**Where**: Paper drafts (multiple); experiment_log references this count in places where it cites Test A and Test E together

**Log narrative + paper says**: "16/16 across three model families"

**Raw JSON says**:
- Test A: 10 Gemma 12B + 6 Qwen 7B = 16 runs (only two model families)
- Test E: 6 Qwen 7B + 6 Gemma 27B cloud = 12 runs
- Combined Test A + Test E: 22 unique runs (Test E gemma27b/qwen7b files turn out to be byte-identical re-publishings of Test A counterparts; raw row count is 34)

**Verdict**: "16/16 across three model families" is wrong on the count AND the family count. Correct: 22 unique runs across three model families (Gemma 12B + Qwen 7B + Gemma 27B). The morning swarm flagged this; abstract says "28 runs" which is also wrong.

**Validation history**: Pass 3 Finding 4 (2026-04-26) flagged. Pass 8 (2026-05-11) re-flagged in paper-wide fact-check (PUNCH_LIST Tier 1 item 3 + Tier 5 item 18).

**Status**: NOT yet corrected. Queued for paper revision.

---

### Drift 5: Paper line 174 falsely credits Gemma 12B with catching S002

**Where**: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/ofb_paper_compiled_source_2026-05-09.md` line 174

**Paper says**:
> "Run on Gemma 12B across the synthetic corpus, the four-axis classifier correctly identified the burnout case (S002)..."

**Raw JSON says**:
- 10 Test N runs on Gemma 12B (`test_n_4axis_submissions_gemma12b_2026-03-28_*.json` + `_2026-03-29_2107.json`): S002 = ENGAGED in 10/10 runs at 0.95 confidence
- Pure 4-axis Gemma 12B never catches S002. Catch happens only on Gemma 27B cloud (5/6 BURNOUT).

**Verdict**: Paper claim contradicts experiment_log line 3349 + 3386-3389 AND raw JSON. The flattened "Gemma 12B 4-axis catches S002" claim is the same compression failure the paper studies.

**Validation history**: Surfaced by Pass 8 morning swarm + Pass 8b iteration history extraction.

**Status**: NOT yet corrected. Master log Issue 5a — queued for pass D revision.

---

### Drift 6: Ablation diagram propagates the Drift 5 error

**Where**: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/ablation_diagram.html` line 661

**Diagram says**:
> "Gemma 12B: protected students routed to ENGAGED; S002 correctly identified as BURNOUT"

Same error as Drift 5. 12B never catches S002 in pure 4-axis. The "correctly identified as BURNOUT" claim only holds for Gemma 27B cloud.

**Status**: NOT yet corrected. Master log Issue 5b — queued.

---

### Drift 7: Workshop T2C2 cells for S002 / S031 / S023 misrepresent model-dependent behavior

**Where**: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/ablation_workshop.html` — `DEFAULT_CELLS.t2.S002.t2c2`, `S031.t2c2`, `S023.t2c2`

**Workshop cells say**:
- S002: "BURNOUT identified. BURNOUT axis correctly caught the true positive."
- S031: "ENGAGED. Cleared."
- S023: "ENGAGED. Lived experience routed to ENGAGED."

**Raw JSON says** (across 17 Test N JSONs):
- S002: Gemma 12B 10/10 ENGAGED (missed). Gemma 27B cloud 5/6 BURNOUT (caught under forced choice). Qwen 7B 1/1 ENGAGED.
- S031: Gemma 12B 8/9 BURNOUT (false positive on minimal effort). Gemma 27B 4/6 NONE + 2/6 ENGAGED.
- S023: Gemma 12B 9/10 ENGAGED + 1/10 CRISIS. Gemma 27B 6/6 ENGAGED. Qwen 7B 1/1 CRISIS (false positive on lived experience).

**Verdict**: All three cells flatten model-dependent behavior into model-agnostic claims. The workshop's cells contradict their own underlying raw JSON.

**Status**: Master log B.7 + B.8 — queued for workshop cell pass.

---

### Drift 8: Workshop T2C3 cells for S002 / S004 / S023 / S029 / S031 are fabricated

**Where**: `ablation_workshop.html` — `DEFAULT_CELLS.t2.<sid>.t2c3` for those five students

**Workshop cells say**: Each describes a generative-observation outcome (e.g., "Burnout surfaced descriptively" for S002, "Strengths surfaced descriptively" for S004, etc.).

**Raw JSON says**: Tests A and E (`test_a_temperature_*.json` + `test_e_cross_model_*.json`) contain only S022 and S028. The other five students are not present in any of the five T2C3 source JSONs.

**Verdict**: The workshop T2C3 cells for these five students describe outcomes that were never measured. III.D-style hallucination — coherent narrative, mismatched empirical referent.

**Status**: Master log B.8 — queued for workshop cell pass. Cells must either be marked "not tested in this column" or re-sourced from other tests where these students do appear (likely `equity_observations_*` full-pipeline runs).

---

### Drift 9: "27B less stable" claim conflates two findings

**Where**: `experiment_log.md` line 6805 + many derivative documents (paper line 174 area, fieldnote `observation_27b_less_stable_than_12b_on_equity_2026-04-25.md`, s1 handoff line 227)

**Log narrative says**: "12B > 27B on the equity case — pattern across two experiments"

**The actual data shows two distinct findings**:
- **27B WORSE on S029** (Phase 4 Test N, 2026-03-29): 12B 10/10 ENGAGED correct; 27B 5/6 ENGAGED + 1/6 BURNOUT (false positive on neurodivergent case)
- **27B BETTER on S002** (Phase 4 Test N, 2026-03-29): 12B 10/10 ENGAGED missed; 27B 5/6 BURNOUT caught (TP recovery)

The "less stable on equity" framing only captures the first. The 2026-04-25 consolidation lumps both Experiment 1 (2026-03-22/23 replication study on S015/S018/S025 relational-harms) and Experiment 2 (2026-03-29 S029 Test N) under "the equity case" — but they're different students, different tests, different metrics.

Additionally, the "27B less stable" framing in the log doesn't acknowledge that 27B is bidirectionally less stable: 1/6 misclassification on S029 (false positive) AND 1/6 misclassification on S002 (missed TP). Direction matters; equity-impact direction matters more.

**Verdict**: Log framing flattens. Paper should distinguish. Master log Issue 4.

**Status**: NOT yet corrected. Queued for paper revision.

---

## Part 2: Runs referenced in the log without persisted JSON

These are documented in the experiment_log but raw JSON files don't exist. The log narrative is the only record.

### Missing 1: Original Mar 24 binary baseline (3/7 file)

**What was run**: 7-student binary detector run on Mar 24 — the original "naive" baseline that the paper's §IV.A.1 references.

**What survived**: Verbatim contradiction quotes embedded in derivative documents.

**What was lost**: The raw JSON itself — apparently to `/tmp/` (per Pass 2's documentation). Apr 26 rerun was launched to recover analogous data; result at `rerun_original_naive_concern_gemma12b_2026-04-26.json`. But the Apr 26 rerun documents itself as *"not a strict replication"* because the classifier was refactored Mar 25 (16 commits between Mar 24 and Apr 26).

**Implication**: All paper claims about "Mar 24 baseline" rest on derivative narrative + Apr 26 reproduction, NOT preserved JSON. Pass 3 Finding 1 flagged this as a systematic retroactive-provenance issue.

### Missing 2: Observation-only prototype (7 students)

**What was run**: Per Pass 2 + Pass 3 documentation, an "observation-only prototype" was run on 7 corpus students.

**What survived**: References in experiment_log; no raw JSON in `data/raw_outputs/`.

**Implication**: Whatever claims rest on this prototype need scoping or removal.

### Missing 3: Reading-first / JSON-first comparison

**What was run**: A comparison between "reading-first" and "JSON-first" pipeline modes.

**What survived**: Initially thought lost; **recovered by Pass 3 instance B** at `Autograder4Canvas/data/demo_baked/reading_first_comparison.json`. Status: present, but in autograder demo_baked rather than research raw_outputs.

### Missing 4: Test E reproduction on Gemma 12B

**What was run**: Test E was originally cross-model (Gemma 27B + Qwen 7B). A Gemma 12B reproduction was referenced but not run / not preserved.

**What survived**: References only.

**Implication**: The morning swarm found that Test E gemma27b/qwen7b JSONs are byte-identical re-publishings of Test A's gemma27b/qwen7b files. So there's no independent Test E data beyond Test A's cross-model runs — the "n=28" headline is built on this misunderstanding.

### Missing 5: Original 32-student naive binary

**What was run**: A naive binary run on the full 32-student corpus.

**What survived**: References in log; no raw JSON.

**Implication**: Paper claims about "32-student corpus" need scoping. The data we have is Test M's 17 records (7 corpus + 10 wellbeing synthetic), not 32.

### Missing 6: Test wellbeing prescan chain (2026-03-29)

**What was attempted**: A controlled-corpus prescan + 4-axis combined test.

**What survived**: Log file at `test_wellbeing_prescan_chain_20260329.log` showing the run crash-aborted on S029 (GPU OOM).

**Implication**: The prescan + 4-axis combination was never controlled-corpus-tested before being deployed live on Week 7 / Week 2 ETHN-1 data. Master log Issue 2 covers this.

---

## Part 3: Corrections applied this pass

### Inline correction markers added 2026-05-11 evening

To experiment_log Test B / Test C tables (Drifts 1, 2, 3):

- `output-format-bias/research/experiment_log.md` lines 1817-1827, 1857, 1870 — **correction markers added inline** (don't delete, mark + correct per direction)
- `Autograder4Canvas/docs/research/experiment_log.md` — mirror correction markers added inline

The markers preserve the historical record while making the correction visible to any reader.

### Format used

```
> ⚠ CORRECTION 2026-05-11: This table's S029 entry shows CLEAR.
> Raw JSON shows S029 = FLAG in 3/3 Test B runs. Flagged by Pass 2 (2026-04-25),
> Pass 3 (2026-04-26), Pass 8 (2026-05-11). Canonical correct values at the
> "CORRECTIONS — 2026-04-25" appendix beginning line 6721.
```

### What's still queued (corrections referenced in Part 1 but not yet applied)

- Drifts 4, 5, 6, 7, 8, 9 — queued for workshop cell pass + paper revision pass
- Missing-data Items 1-6 — paper claims that rest on these need scoping
