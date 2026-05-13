# Master Response Log — Output-Format-Bias Paper Verification Sweep

Started: 2026-05-11
Paper deadline: 2026-05-20
Last comprehensive update: 2026-05-11 late evening (session-end wrap; tables in data_tables/ are interpretation-ready)

---

## Session-end state (2026-05-11 late evening) — FOR FRESH-CONTEXT INTERPRETATION PASS

**The three review tables in `data_tables/` are the canonical review surface for interpretation.** Each cell has verbatim model rationale + source attribution. Verdicts, counts, P-ID tags, cross-table consistency all verified by paired audit + deterministic checks.

**What June will be doing next session**: interpretation pass on each table, deciding how findings map to paper revisions. NOT verification — that's done.

**Three tables to review (open in browser)**:
1. `data_tables/ablation_workshop.html` — binary calibration ladder (4 cols T1) + architecture comparison (3 cols T2). T2C2 S031 reframed as designed edge-case probe per Issue 3.
2. `data_tables/4axis_iteration_workshop.html` — 5 sections (Test L on observations, Test N pure 4-axis, Test O multi-axis + CHECK-IN, Test P two-pass, prescan + 4-axis). CHECK-IN is the load-bearing mechanism for S002 recovery.
3. `data_tables/12B_vs_27B_differential_table_2026-05-11.html` — 13 experiments with side-by-side rationale pairs. P3 controlled comparison (sha256 `93f4769a`, shared between 12B `_2107` and 27B `_2109`) shows both models produce ENGAGED on S002 AND S029 under shared prompt.

**Three paper-shaping findings from tonight's work** that the interpretation pass needs to weigh:
- **Issue 7 (12B/27B prompt confound)**: Test N uses 5 distinct system prompts across 16 JSONs. The "model-scale matters for equity" claim is triple-confounded (prompt + quantization + inference stack). The S029 BURNOUT 1/6 false positive on 27B is isolated to the only 27B prompt variant WITHOUT identity-disclosure guard.
- **Issue 2 (4-axis architecture)**: CHECK-IN is the load-bearing mechanism for subtle wellbeing signal recovery, not the 4-axis schema. Pure 4-axis Gemma 12B never catches S002 in 10 runs.
- **Issue 8 (Variant A test ran today)**: lead-author hand-coding pending at `output-format-bias/variant_a_coding_workshop_2026-05-11.html`. Three pre-coding findings already documented in `Autograder4Canvas/docs/research/session_log.md` lines 14-22.

**Open methodological question**: Issue 3 (Marcus Bell + which other workshop students are designed edge-case probes vs. clean controls). Affects how false-positive findings get framed. *Partially resolved 2026-05-12: don't claim "designed" — describe as edge cases. See Issue 3 status update.*

**Update 2026-05-12**: §IV.A.4 rewrite landed (scoped Option B per Issue 2). **Cross-issue paper-edit ripple register added at Issue 10** — captures targets in §I, §IV.A.1, §IV.A.3 prose + Table 1, §IV.A.6, §IV.B, §VI, abstract, with each target's dependencies on open validation issues. Ripples HELD pending interpretation pass on `data_tables/`. Name-convention consistency items can proceed independently. §IV.A.6 27B parenthetical applied (clean cut). **Issue 11 added** — paper's corpus description undercounts the three actual testing corpora (Phase 1 ~20, equity 32, wellbeing WB1–14); upstream of Issue 10 ripples #1–#3. WB1–14 origin question resolved 2026-05-12: separate corpus from long-essay LF01–LF07; defined inline in `scripts/run_alt_hypothesis_tests.py`.

**Supporting docs**:
- Drift tracker at `data_tables/verification_2026-05-11/log_vs_json_drift_2026-05-11.md`
- Post-rationale audit reports at `data_tables/verification_2026-05-11/post_rationale_audit/`
- Validation pass index in this file (13 passes from 2026-03-21 through 2026-05-12)
- Recommendations register in this file (B.1-B.15)

**Known cosmetic gap (not blocking interpretation)**: 23 cells in binary workshop labeled "Model rationale (verbatim)" are actually researcher meta-descriptions of empty `concerns: []` arrays for cleared cells. Relabel optional.

---

This file is the canonical place to track verification findings, response decisions, and corrections-to-apply for the output-format-bias paper.

## Quick navigation

- **[Methodological commitments](#methodological-commitments)** — applies to all entries
- **[Issue 1: Generative-observation prompt confound](#issue-1)** — Variant A test built + critic-reviewed
- **[Issue 2: 4-axis claim collapses](#issue-2)** — disambiguated 12B/27B findings + Test L/N/O/P iteration history
- **[Issue 3: Corpus-design question on Marcus Bell](#issue-3)** — open methodological question
- **[Issue 4: 27B-vs-12B claim conflates two findings](#issue-4)** — provenance + scope
- **[Issue 5: Paper claims contradicted by experiment log](#issue-5)** — specific lines + corrections
- **[Issue 6: MLX cache management protocol](#issue-6)** — infrastructure
- **[Issue 7: 12B/27B prompt-difference confound](#issue-7)** — Test N system prompts differ between models; paper's "model-scale" interpretation is triple-confounded
- **[Issue 8: Variant A test completed but coding pending](#issue-8)** — test ran 2026-05-11, outputs exist, lead-author hand-coding queued
- **[Issue 9: T2C2 S024 fabrication (parallel to T2C3 hallucinations)](#issue-9)** — second instance of the III.D-shape pattern
- **[Issue 10: §IV.A.4 rewrite landed; cross-issue paper-edit ripple register](#issue-10)** — what landed 2026-05-12, ripple targets, dependencies on open validation issues
- **[Issue 11: Corpus description undercounts the actual testing corpora](#issue-11)** — three distinct corpora (Phase 1 ~20, equity 32, wellbeing 14); foundational rewrite upstream of Issue 10 ripples #1–#3
- **[Validation pass index](#validation-pass-index)** — 13 passes from 2026-03-21 through 2026-05-12
- **[Recommendations-not-implemented register](#recommendations-register)** — what's been flagged but not applied, prioritized
- **[Visual artifacts (workshops + diagrams)](#visual-artifacts)** — what's been updated when
- **[Source-of-truth framework](#source-of-truth)** — when JSON wins vs when log narrative is the only record
- **[Session_log sources](#session-logs)** — 4 files, including the active state file with Variant A results

---

## Methodological commitments

These apply to every entry below and to every revision pass on the paper.

1. **No keyword matching for qualitative evaluation.** Every model output cited in this work is read in full. Parser / classifier labels are downstream artifacts, not evaluation inputs. Where prose and parser disagree, the prose wins. (The III.D hallucination and the T2C3 Qwen 7B miss both happened because keyword-classifiers labeled outputs ASSET while the prose contained deficit framing. The classifier compresses; the prose is the data.)

2. **Verbatim quotes only.** Model outputs are quoted exactly as they appear in raw JSON. No paraphrase. No editorial truncation. No ellipsis hiding substantive content. Apostrophe style (straight vs. curly), capitalization, and punctuation preserved. If a quote needs trimming, the trim must not remove evaluative content.

3. **Raw JSON as primary source.** Every numeric or factual claim in paper prose must be sourceable to raw JSON, not to `experiment_log.md`, workshop cells, contradiction catalog, or prior draft text. Summaries are derived and may contain compression errors; JSON is authoritative.

4. **Disconfirmer-paired analysis for qualitative claims.** Single-angle readings are insufficient. Each qualitative claim about model behavior is checked from at least one disconfirming angle (try to falsify, not just confirm). The pair-agreement / pair-disagreement is itself diagnostic.

5. **Descriptive vs. interpretive marked separately.** "The model said X" is descriptive (verifiable in JSON). "The mechanism is Y" / "the model is invoking construct Z" / "this represents axis A protection" is interpretive (researcher inference). These are different kinds of claims and the paper must distinguish them. Mechanism inferences require explicit justification grounded in the model's reasoning text, not just the model's verdict.

6. **Re-grounding on every revision.** When paper prose is revised, the reviser opens the raw JSON and checks the claim against it, not against earlier draft text or summary documents. Compression drift accumulates across revisions unless each revision re-grounds. This applies even when the revision is "small."

7. **Numbers that look round are suspicious.** "n=28," "16 passes," "three layers," "four assignments" — if a number is summary-shaped, verify it against raw counts before letting it stand. Several of the wrong numbers in the May 9 draft were summary arithmetic that didn't match the JSON.

---

<a id="issue-1"></a>
## Issue 1 — Generative-observation prompt confounds open-ended observation with critical-theory detection task

**Severity**: Tier 1 (load-bearing for paper's central format-protection claim)
**Surfaced by**: T2C3 disconfirmer + T2C3 verifier (pair-confirmed)
**Affects in paper**: §IV.A.4 (Generative observation row), §IV.A.5 (cross-architecture synthesis), abstract n-claim, discussion of format vs. model.

### Problem

The current Test A / Test E prompt couples two distinct tasks: (a) open-ended descriptive observation ("In 3-4 sentences, share what you notice … Write naturally."), and (b) detection + naming of "structural power moves" using a CRT-derived vocabulary (tone policing, abstract liberalism, settler innocence, progress narratives, objectivity claims, deflection to individual solutions, meritocracy framing — seven items with definitions).

The disconfirmer found Qwen 7B producing deficit framing in the prose despite parser-ASSET labels: tone-policing-shaped recommendations on Destiny ("balance her emotional engagement with more analytical depth"), and outright misapplication of "abstract liberalism" to Imani's first-person intersectional articulation. Gemma 12B and Gemma 27B produced clean asset-framed observation across the same prompt.

The current data cannot distinguish two possible mechanisms:

1. Qwen fails at open-ended observation generally (format-protection has a model-scale floor).
2. Qwen fails at applying the critical-theory constructs (prompt-loading re-introduces compression-style bias even inside an "open-ended" container).

The two readings have different implications for the paper's central claim.

### Relevant raw JSON

Test outputs (variant B = current bundled prompt):
- `output-format-bias/data/raw_outputs/test_a_temperature_gemma12b_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_a_temperature_gemma27b_cloud_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_a_temperature_qwen7b_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_e_cross_model_gemma27b_cloud_2026-03-26.json`
- `output-format-bias/data/raw_outputs/test_e_cross_model_qwen7b_2026-03-26.json`

Mirror copies (byte-identical, verified via `diff`):
- `Autograder4Canvas/data/research/raw_outputs/test_a_temperature_*.json`
- `Autograder4Canvas/data/research/raw_outputs/test_e_cross_model_*.json`

Student corpus (submissions):
- `Autograder4Canvas/data/demo_corpus/ethnic_studies.json` (16-student equity corpus with patterns + submissions)

Tests A and E in these JSONs only include S022 (Destiny Williams) and S028 (Imani Drayton). Workshop cells claiming Test A/E results for S002, S004, S023, S029, S031 are unsourced — see Issue 6.

### Proposed response

Run a separation test: **Variant A (pure observation, no power-moves block)** across the same models, comparing against the existing Test A/E data as Variant B.

**Variant A prompt strip**: Remove the entire "structural power moves vary by discipline … name it specifically" block plus the enumerated 7-item list of moves. Keep class context, submission, "In 3-4 sentences share what you notice" framing, and the descriptive consider-prompts (intellectual reach, emotional relationship, engagement/capacity). Keep "Do NOT categorize, label, or flag. Just describe." Result: pure descriptive observation prompt.

**Variant B**: existing Tests A/E prompt verbatim (no re-run needed — existing data is the comparison anchor).

**Models for Variant A run**:
- Gemma 12B (MLX, local) — passed B; baseline check
- Qwen 7B (MLX, local) — failed B; this is the load-bearing comparison
- Llama 3.1 8B (MLX, local — June has) — new model in the mix
- Optional: Mistral 7B and Phi-3 medium (download required; only if Qwen results are ambiguous and we want broader generalization across small models)
- Skip Gemma 27B (cloud, costs money; passed B; predicted to pass A; not informative enough to justify spend)

**Students**: S022 (Destiny) + S028 (Imani) at minimum — the two students with existing Test A/E data so the comparison is direct. Optional extension to S023 Yolanda Fuentes, S029 Jordan Espinoza, S031 Marcus Bell for cross-axis robustness if Qwen results are clean (then we want to confirm generalization).

**Runs per model per student**: 3 at temp 0.3 (matches existing Tests A/E protocol).

**Evaluation**: Deep qualitative human read of every output. NO parser, NO keyword matching, NO classifier label trusted as evaluation input. The prose is the data. June reads each output and judges asset / deficit / covert-classification by hand. This applies even if it's slow — keyword shortcuts are exactly what produced the III.D and T2C3 misses.

**Possible outcomes and paper implications**:

1. **All models clean on A, Qwen fails on B**: Strongest version of the format claim. "Open-ended observation protects against bias across model families when the prompt stays purely descriptive; loading the prompt with categorical detection tasks re-introduces compression-style bias on smaller models." Maps cleanly onto the paper's compression thesis.
2. **All models clean on A, all models also clean on B (Qwen failure was prompt-specific quirk we can't reproduce)**: Disconfirmer's finding becomes prompt-confound rather than format-failure. Paper's existing claim essentially survives.
3. **Qwen fails on A as well**: Format protection has a model-scale floor. Paper scopes to model family. Less generous but still publishable.

### Status

**In progress** — 4-condition test script written, smoke-tested, and revised through critic-swarm review 2026-05-11. Awaiting test-monitor session launch.

**Design expanded twice on 2026-05-11**:
1. Originally proposed single Variant A → expanded to 3 conditions to cover both prompt-strip dimensions + class-context priming confound (June's decision pre-swarm).
2. Critic-swarm methodologist review added a 4th condition `b_replicate` to control for cross-session protocol drift between March 2026 (Tests A/E data collection) and May 2026 (this run). Without it, "Qwen recovers under a1" is confounded with "Qwen behaves differently in May than March for reasons unrelated to the strip."

**Final 4-condition design**:

| Condition | Strip | Class context | Tests |
|---|---|---|---|
| `b_replicate` | NONE — today's production prompt verbatim | Gemma 12B class read | Cross-session protocol drift (March vs May) |
| `a1` | structural-power-moves block only | Gemma 12B class read | Does CRT detection vocabulary cause the bias? |
| `a2` | power-moves + relational/narrative paragraph | Gemma 12B class read | Does relational guidance also contribute load? |
| `a2_no_context` | power-moves + relational/narrative | **removed entirely** | Is class context load-bearing? (degradation here is consistent with EITHER "priming was doing the work" OR "context-stripping is itself a small-model stressor" — design does not disambiguate) |

**Comparison structure**:
- May `b_replicate` vs. March B JSONs → cross-session drift check (corroborates or invalidates the original finding under today's conditions)
- May `a1`/`a2`/`a2_no_context` vs. May `b_replicate` → intra-session strip effect (clean within-session comparison)

**Class reading shape verified 2026-05-11**: today's checkpoint at `Autograder4Canvas/data/demo_baked/checkpoints/ethnic_studies_gemma12b_mlx_class_reading.json` is **byte-identical** to the embedded class_context in the March Test A/E JSON prompts (both 6,384-char strings). With-context conditions are clean B comparisons on this dimension.

**Models**: 3 local MLX (Gemma 12B, Qwen 7B, Llama 3.1 8B). Skip Gemma 27B cloud. **`unload_mlx_model()` now called between models** to prevent memory pressure on consumer hardware (per build-agent critic-swarm flag).

**Students**: full 8-student workshop subset (S002, S004, S022, S023, S024, S028, S029, S031).

**Total runs**: adaptive. n=1 default per model; Llama bumps to n=3 only if pre-run determinism spot-check fails. June + Claude decision 2026-05-11 after weighing strategic trade-offs.

- **If Llama is deterministic at temp 0.3** (likely, based on Gemma 12B + Qwen 7B priors from existing Tests A/E): total = 4 conditions × 3 models × 8 students × 1 run + 3 spot-check = **99 model calls, ~40-70 min**.
- **If Llama is non-deterministic**: Llama bumps to n=3; total = 4 × 8 × (1 + 1 + 3) + 3 spot-check = **163 model calls, ~70-110 min**.

**Why n=1 default**: existing Tests A/E protocol used inconsistent n (n=5 for Test A, n=3 for Test E — no canonical n to "preserve parity" with). MLX at temp 0.3 is byte-identical across runs on Gemma 12B and Qwen 7B in March data. n=3 was conservative-but-mostly-wasted runtime. n=1 + spot-check is more efficient and equally rigorous.

**Why spot-check Llama only**: Gemma 12B and Qwen 7B determinism at 0.3 already established from existing Tests A/E (byte-identical raw_output across runs). Llama 8B at 0.3 is unknown — the spot-check (3 calls on S022 under b_replicate, ~30 sec) tells us whether to proceed with n=1 or scale Llama up.

**Why hold model expansion**: critic-swarm review surfaced "do we add Mistral / Qwen 1.5B / larger cloud Qwen?" — held for follow-up. Qwen 1.5B too small to handle the prompt usefully; larger cloud Qwen costs money for a question that isn't load-bearing yet; Mistral requires download. If 3-model results raise scale-within-family or cross-family questions, those become targeted follow-up tests.

### Pre-registered analysis practice (NOT pre-registered categories)

Per critic-swarm methodologist + skeptical-reviewer concern that 252 outputs read under deadline pressure will drift toward flattering interpretation, AND per June's response that pre-registered codes ARE the compression move the paper critiques — the practice (not categories) gets pre-registered:

1. **Read each output verbatim, full prose, no skimming.** No keyword-classifier shortcut. The classifier label in `b_replicate` outputs is also ignored (it exists for schema parity but does not inform evaluation).
2. **Attach the model's actual quote** when noting any pattern. No paraphrase, no editorial truncation.
3. **Disconfirming pass on every cell** (per master log commitment #4): if a cell reads "deficit-framed," do a second read trying to find the asset-framed read of the same passage. If a cell reads "asset-framed," check for covert classification or verdict-shaped phrasing buried in the prose.
4. **Cluster *after* reading, not before.** Categories may emerge — the disconfirmer's "clear asset / covert classification / verdict-shaped / borderline" emerged from reading; don't impose them at the start.
5. **Don't pre-commit to interpretation language** for outcomes. Per skeptical-reviewer, the original 3-outcome table was scope-inflated (Outcome 1 claimed the test would license "strongest version of format claim" — actually it can only localize where Qwen failure lives WITHIN observation format; the broader format-vs-compressed claim is supported by binary/4-axis evidence already in the paper, not by this test).

### Possible outcomes and what each ACTUALLY licenses

Revised per critic-swarm skeptical-reviewer:

| Pattern | What's earnable |
|---|---|
| `b_replicate` reproduces March Qwen deficit-framing | Original verification finding corroborated under current conditions. Protocol drift not material. Subsequent a1/a2/a2_no_context comparisons are interpretable. |
| `b_replicate` does NOT reproduce March deficit-framing | Cross-session drift is material. Cannot interpret a1/a2/a2_no_context as direct B-vs-A. Need to understand what changed (autograder commit diff between March and May, MLX runtime, model weights). Different question to answer. |
| Qwen recovers under a1 (intra-session) | Within-observation-format, the structural-power-moves block is identified as the load on Qwen 7B. Does NOT license "format protects across model families" — that claim depends on binary/4-axis evidence, not this test. |
| Qwen still deficit under a1, recovers under a2 | The relational/narrative paragraph also contributes load. Two pieces of guidance flagged as bias-introducing on smaller models. |
| Qwen still deficit under a2, recovers under a2_no_context | Class-context priming OR context-stripping-as-stressor (design does not disambiguate). |
| Qwen still deficit under all conditions | Model-scale floor within the observation format. Paper scopes to Gemma family for this specific claim. Alternative explanations not eliminated: 4-bit quantization, prompt-position sensitivity, training-data drift, S022/S028-specific. |
| Gemma DEGRADES under a2_no_context | Class context is load-bearing for asset-framing on Gemma too. Could be priming OR context-as-anchor. (4th outcome per skeptical-reviewer — added explicitly so analysis doesn't drift toward "priming was doing the work" reading.) |

### Test artifacts

- **Script**: `output-format-bias/scripts/run_variant_a_stripped_observation.py` — 4 condition prompts defined inline (a1/a2/a2_no_context) plus `b_replicate` imported live from `insights.prompts.OBSERVATION_PROMPT`. Includes `unload_mlx_model()` between model loops and `determinism_check()` in output metadata. Fully self-contained.
- **Handoff doc**: `output-format-bias/scripts/VARIANT_A_TEST_HANDOFF.md` — launch instructions for the test-monitor session.
- **Launch command** (from autograder root):
  ```
  cd ~/Documents/GitHub/Autograder4Canvas && PYTHONPATH=src python3 \
    ~/Documents/GitHub/research/output-format-bias/scripts/run_variant_a_stripped_observation.py
  ```
- **Output files** (written incrementally per condition):
  - `output-format-bias/data/raw_outputs/test_variant_b_replicate_observation_2026-05-11.json`
  - `output-format-bias/data/raw_outputs/test_variant_a1_observation_2026-05-11.json`
  - `output-format-bias/data/raw_outputs/test_variant_a2_observation_2026-05-11.json`
  - `output-format-bias/data/raw_outputs/test_variant_a2_no_context_observation_2026-05-11.json`

**Smoke test (2026-05-11, pre-swarm)**: all 8 workshop students present, all prompts format cleanly.
**Post-swarm verification (2026-05-11)**: system prompt identical to production (1,745 chars); A1 strip integrity verified (no STRUCTURAL POWER MOVE / Tone policing / Abstract liberalism / NAME THE MECHANISM strings; relational/narrative preserved); A2 strip integrity verified (relational/narrative removed); a2_no_context strip integrity verified (class context section removed entirely). Class reading shape parity with March B JSONs verified byte-identical.

### Notes

The corpus submissions for S022 and S028 are visible in the raw JSONs (embedded in the `prompt` field). Worth comparing the literal student writing against each model's read of it — Destiny's "righteous anger" submission and Imani's "Black plus girl / whole different channel that comes with its own static" submission are where the deficit framing surfaces on Qwen.

The meta-irony in the existing Qwen output: the model applies "abstract liberalism" — which the prompt defines as the colorblind move ("everyone should be treated equally") — to a Black girl explicitly *refusing* additive/colorblind framing. The model performs the construct in the act of (mis)identifying it. If Variant A produces clean Qwen output, this is a finding about prompt-priming. If Variant A still fails, it's a finding about model capacity.

---

<a id="issue-2"></a>
## Issue 2 — Paper's "4-axis classifier recovers the burnout TP" claim collapses under iteration-history scrutiny

**Severity**: Tier 1 (load-bearing for paper's §IV.A.3 + §IV.A.4 + Table 2 architectural argument)
**Surfaced by**: T2C2 verifier + disconfirmer (2026-05-11 morning) → June's question + supplementary search (2026-05-11 afternoon) → iteration-history extraction
**Affects in paper**: §IV.A.3 (four-axis section), §IV.A.4 (cross-architecture synthesis), Table 2 cells, abstract

### Problem

The workshop's T2C2 cell for Jordan Kim (S002, burnout TP) reads: *"BURNOUT identified. BURNOUT axis correctly caught the true positive. The categorical slot designed against the known burnout pattern recovered what the binary missed."* The paper §IV.A.3 inherits this framing.

The full iteration history (extracted 2026-05-11 from raw JSONs — see `verification_2026-05-11/4axis_iteration_history_2026-05-11.md`) shows this claim is wrong on the locally-deployable model and rests on a different mechanism than "the BURNOUT slot caught it" even where it works:

**Pure 4-axis on raw submissions (Test N) — S002:**
- Gemma 12B 4-bit MLX: 10/10 runs ENGAGED. Pure 4-axis misses S002 on the local model.
- Gemma 27B cloud: 5/6 BURNOUT (forced-choice artifact — one run still drifts ENGAGED).
- Qwen 7B: 1/1 ENGAGED.

**Multi-axis with CHECK-IN flag (Test O) — S002:**
- Gemma 12B: 3/3 ENGAGED + CHECK-IN. CHECK-IN is the catch mechanism, not BURNOUT.
- Gemma 27B cloud: 1/1 ENGAGED + CHECK-IN. 27B abandons BURNOUT once given the CHECK-IN alternative.

**Two-pass with CHECK-IN refinement (Test P) — S002:**
- Gemma 12B: 7/7 pass1 ENGAGED → final ENGAGED + CHECK-IN. Catch happens at pass 2 via CHECK-IN, never via the 4-axis wellbeing classification.

The architecture that actually recovers S002 is **CHECK-IN as a separate non-categorical flag layered alongside the 4-axis schema** — not the 4-axis schema itself. The paper's "4-axis recovers the TP" framing flattens this distinction.

### Three additional findings the workshop doesn't represent

Surfaced during iteration-history extraction:

1. **S031 Marcus Bell (minimal effort, expected CLEAR)** is false-flagged BURNOUT in pure 4-axis Gemma 12B (8/9 morning runs) at 0.7 confidence. Two-pass Test P inherits this misclassification in all 7 pass1 runs. Workshop T2C2 cell reads "ENGAGED. Cleared." — wrong on Gemma 12B.
2. **S029 Jordan E. (neurodivergent, expected CLEAR)** false-BURNOUT in 1/6 Gemma 27B Test N runs (already noted morning). Multi-axis with CHECK-IN routes to ENGAGED + CHECK-IN on Gemma 27B.
3. **S023 Yolanda F. (lived experience, expected CLEAR)** false-CRISIS in Qwen 7B Test N (1/1) and in one Gemma 12B Test N run (2026-03-29_2107). Multi-axis with CHECK-IN routes to ENGAGED + CRISIS + CHECK-IN on Gemma 12B.

S024 Ingrid V. (lived experience) is **not tested in any 4-axis-family run.** Workshop T2C2 cell for S024 describes an outcome that was never measured.

### Relevant raw JSON

All in `output-format-bias/data/raw_outputs/`:
- Test N (pure 4-axis on raw submissions): `test_n_4axis_submissions_*` × 17 files
- Test O (multi-axis + CHECK-IN): `test_o_multi_axis_*` × 4 files
- Test P (two-pass): `test_p_two_pass_gemma12b_*` × 7 files
- Test L (4-axis on observations, synthetic WB only — no workshop students): `test_l_expanded_wellbeing_gemma12b_2026-03-28.json` × 1 file

Full iteration history extracted to: `verification_2026-05-11/4axis_iteration_history_2026-05-11.md`

### Provenance note

The experiment_log (`research/experiment_log.md`) was rigorous about this. Line 3386-3394 explicitly documents Test N as missing S002 at 12B. Line 4751-4756 + 4891-4893 + 4934-4966 document the Test O / Test P CHECK-IN architecture catching S002 via CHECK-IN (not BURNOUT). Line 5376-5379 pre-wrote a "Paper claim revision" qualifier: "The 4-axis format eliminates false positives on neurodivergent writers within Gemma 12B 4-bit. Cannot claim generalization to larger model scales."

**The compression happened at the workshop-cell-authoring layer, not in the experiment log.** Workshop cells were written during the 2026-05-10 session and didn't carry through the model-dependence + CHECK-IN-mechanism nuance the log documented. Pattern: the experiment log is mixed (Test B/C tables had S023/S029 flag swaps surfaced this morning, but Test N + 4-axis-iteration history is clean and pre-flagged the load-bearing limits). The workshop is the consistent compression layer.

### Proposed response

Two options for the paper §IV.A.3 + §IV.A.4 + Table 2:

**Option A — Cut the 4-axis sections.** The architecture story collapses under iteration-history scrutiny. What recovers S002 is CHECK-IN, not the 4-axis schema, and the 4-axis schema itself introduces new false positives on S031, S023, S029. Cutting simplifies §IV.A and tightens the paper's argument to binary vs. generative observation.

**Option B — Explain the iteration history honestly.** Frame the 4-axis as a designed sequence: pure 4-axis (Test N) → multi-axis with CHECK-IN (Test O) → two-pass with CHECK-IN refinement (Test P). The signal that actually catches subtle wellbeing cases is the CHECK-IN axis layered alongside the wellbeing classification. The 4-axis schema alone does not.

Option B is methodologically substantive (forced-choice categorical classification systematically misses subtle cases; non-categorical fallback signals recover them). Option A is shorter and may better fit the May 20 deadline. June's call.

Either option requires:
- Rewriting workshop T2C2 cells for S002, S023, S029, S031 (all currently wrong or under-stated)
- Marking S024 cells as "not tested in any 4-axis-family run" (currently fabricated)
- Updating §IV.A.3 to reflect what the data actually shows
- Updating Table 2 if it stays in the paper

### Status (updated 2026-05-12)

**§IV.A.4 rewrite landed 2026-05-12** — scoped variant of Option B (kept the section but reframed honestly without going into the Test N → Test O → Test P CHECK-IN narrative). See Issue 10 for the new text, the session decisions feeding ripples, and the ripple register.

**§IV.A.3 (prose + Table 1) + §IV.A.6 + abstract** remain open. Held pending interpretation pass on `data_tables/`. Full Option A (cut 4-axis sections) vs. Option B (full CHECK-IN narrative) decision still open if interpretation pass reveals additional problems §IV.A.4 didn't address.

---

<a id="issue-3"></a>
## Issue 3 — Marcus Bell (S031) is a designed-edge-case, not a clean control — workshop framing needs revision

**Severity**: Tier 2 (corpus/methodological — affects how we interpret 4-axis Test N results)
**Surfaced by**: June 2026-05-11 evening during iteration-history review; corpus-design intent clarified by June same evening
**Affects**: workshop T2C2 S031 cell, paper §IV.A.3 discussion of Test N false positives, framing of "designed test cases" vs "controls"

### Problem (revised after corpus-design clarification)

Initial framing of this Issue treated Marcus's expected-CLEAR verdict as an unambiguous corpus-design choice. June clarified 2026-05-11 evening: **"I thought we designed minimal effort to test whether that would flag?"** — meaning Marcus was deliberately constructed as an edge-case probe, not as a clean control. The workshop's "expected CLEAR" notation doesn't capture this design intent.

Marcus's submission (294 chars, 3 sentences, ends "i think the concept makes sense but idk what else to say about it") is a deliberately ambiguous case designed to test whether the classifier reads minimal effort as a wellbeing signal. The data answers that question:

- **Pure 4-axis Gemma 12B**: routes to BURNOUT 8/9 runs at exactly threshold confidence 0.7
- **Pure 4-axis Gemma 27B cloud**: 4/6 NONE ("insufficient text to assess"), 2/6 ENGAGED — variable
- **Multi-axis + CHECK-IN**: ENGAGED + CHECK-IN consistently
- **Two-pass**: pass1 BURNOUT (inherited), final BURNOUT (CHECK-IN refinement skipped because pass1 wasn't ENGAGED)

So the test answers: yes, multiple 4-axis variants do treat minimal effort as a wellbeing signal. Whether that's the desired behavior depends on what the deployed system is meant to do.

### Reframe

This isn't a "false positive" or a "true positive" — it's a **designed probe** revealing model behavior on an ambiguous case. The workshop's binary expected-CLEAR / expected-FLAG framing doesn't fit. Marcus belongs in a different category: "edge case designed to surface model behavior, expected outcome is observational, not a pass/fail metric."

### Implications for paper

The paper currently treats Marcus as a control (clean CLEAR case). The honest framing is that Marcus is a **designed probe** showing that pure 4-axis classifiers treat minimal-effort submissions as soft burnout signals. That's information about model behavior, not a "false positive" the classifier should be penalized for.

Three possible paper framings:

1. **Reframe Marcus as a designed-edge-case in §IV.A.3**: name the probe explicitly, report the result ("pure 4-axis Gemma 12B routes minimal effort to BURNOUT 8/9; cloud Gemma 27B more cautious"), let the reader decide whether this is appropriate wellbeing-monitor behavior.
2. **Drop Marcus from the workshop**: he wasn't part of the original 7-student equity subset that drove the binary-vs-format argument; he was added later as an edge-case probe. The workshop's 8-student framing may be wrong to include him as a peer.
3. **Move Marcus to a separate "edge case" section** that documents designed-probe results alongside the equity-axis findings.

### Action

1. Workshop cell pass: update S031's anchor text to acknowledge the designed-probe framing rather than expected-CLEAR. Pattern label "minimal_effort" stays; expected verdict gets revised from CLEAR to "designed edge case — observe model behavior."
2. Master log to track which other corpus students might be similar designed-probes vs. clean controls. The S004 Priya (strong) and possibly others may also have been designed for specific behavior-observation purposes — need to confirm corpus-design intent with June.
3. Paper §IV.A.3 framing decision: which of the three options above.

### Status (updated 2026-05-12)

June's clarification 2026-05-12 reframes Issue 3 substantively. The design_notes claim *"True minimal effort... NOT pathologized,"* but the actual text reads more articulate than that framing. June: *"I think that Claude just kind of missed the ball on writing a convincing burnout essay [for S002 Jordan Kim]... [Marcus is] more ambiguous than what the documentation frames it as... we don't have to call it designed to be edge cased. We can just say that they are edge cases."*

**Decision: do NOT claim "designed edge case" framing in the paper.** Describe both Marcus and S002 as edge cases — descriptive of textual behavior, agnostic about design intent. The corpus generation may not have differentiated as cleanly as design notes suggest.

§IV.A.4 (rewritten 2026-05-12, see Issue 10) applies this — describes Marcus as *"44 words ... naming the concept correctly and ending with 'idk what else to say about it'"* without claiming design intent.

**Open subitem**: corpus documentation overclaims design distinctness vs. actual textual properties. Could be a separate documentation cleanup task. Not blocking paper work.

---

<a id="issue-4"></a>
## Issue 4 — The "12B-vs-27B" comparison conflates two distinct findings

**Severity**: Tier 1 (provenance + scope problem affecting how the paper frames model-scale + equity)
**Surfaced by**: Validation pass agent + 12B-vs-27B history search agent 2026-05-11 evening
**Affects**: §IV.A.3, §IV.A.4, abstract, methods note on n-asymmetry

### Problem

The experiment_log at line 6805 says "12B > 27B on the equity case — pattern across two experiments (added 2026-04-25)." This is a CONSOLIDATION written 2026-04-25 that lumps two distinct findings under one label. They're about different students, different tests, different metrics:

**Finding 4a — 27B WORSE on S029 (neurodivergent case in Test N 4-axis)**:
- Gemma 12B 4-axis: 10/10 ENGAGED (correct on the protected case)
- Gemma 27B 4-axis: 5/6 ENGAGED + 1/6 BURNOUT — ~17% false-positive rate
- Documented at experiment_log line 5273-5379 (Phase 4 Cross-Model, 2026-03-29); consolidation at line 6805-6818 (2026-04-25)
- This is what the "27B less stable on equity" claim points at

**Finding 4b — 27B BETTER on S002 (burnout TP)**:
- Gemma 12B 4-axis: 10/10 ENGAGED (missed the TP)
- Gemma 27B 4-axis: 5/6 BURNOUT (caught the TP under forced choice)
- Documented at experiment_log line 3349 + 3386-3389 (Test N section, 2026-03-28); 27B catch at line 5298 (Phase 4, 2026-03-29); full count added at line 6793 (2026-04-25 validation pass)
- This is "27B catches subtle burnout that 12B misses"
- Bidirectional: 1/6 of 27B runs also misclassify S002 as ENGAGED — 27B instability runs in both directions, not only on equity cases

**These are different findings.** They happen to both involve "27B less stable than 12B" but the *direction* of the instability is opposite: 27B introduces false positives on the equity case (S029), but recovers true positives on the burnout case (S002) that 12B misses.

### The "equity case" label is doing too much work

Even within Finding 4a, "the equity case" is ambiguous between:
- The 2026-03-22/23 replication study: equity case = S015 Brittany / S018 Connor / S025 Aiden (relational-harms detection in the binary pipeline; 12B 100% catch vs 27B 80% catch over 5 runs)
- The 2026-03-29 Test N: equity case = S029 Jordan Espinoza (neurodivergent case; 12B 10/10 ENGAGED vs 27B 1/6 BURNOUT)

The 2026-04-25 consolidation (experiment_log line 6805) treats both as "the equity case." But they're different students, different tests, different metrics, different n. If a reviewer pushes, this lumping is a soft spot.

### The chronologically first instance is older than the s1 handoff

The earliest documented "12B > 27B" claim is `output-format-bias/research/experiment_log.md` lines 442-490, dated **2026-03-22/23** (the original Round 3 / Replication Study):

> Line 469: "HEADLINE: Gemma 12B + class context = PERFECT. 100% flags, 0% FP, 5/5 runs."
> Line 472: "12B MORE reliable than 27B with class context (100% vs 80%)"

The first outside-the-log write-up is `output-format-bias/research/system_comparison_old_vs_new.md` line 55 (2026-03-25). The s1 handoff (2026-04-25) is a later recap, not the origin.

### Inference-setup confound is not ruled out

The "12B more reliable than 27B" claim has three documented hypotheses (experiment_log line 6818+):
1. Normative gravity (larger training corpus → stronger pull toward conventional readings)
2. Prior-vs-prompt weighting (27B weights priors over instructions more than 12B)
3. **Inference-setup confound** (12B = local MLX 4-bit; 27B = cloud OpenRouter, likely fp16, different sampling implementation)

The third is the easiest to test and the most boring. It hasn't been ruled out. If a reviewer pushes on the 12B-better-than-27B claim, this is the soft spot. Worth flagging in the paper or scoping the claim to "Gemma 12B 4-bit MLX vs Gemma 27B cloud OpenRouter" rather than a clean model-scale comparison.

### Proposed response

1. In §IV.A.3 / §IV.A.4 / abstract: distinguish the two findings explicitly. Don't use "27B is less stable" as a unified claim; name S029 false positive separately from S002 catch.
2. Scope the "less stable" framing to "Gemma 27B cloud on Test N at temp 0.3 produced a 1/6 BURNOUT misclassification on S029 (neurodivergent) and a 1/6 ENGAGED misclassification on S002 (burnout TP) — bidirectional decision-boundary instability, n=6 small."
3. Add the inference-setup-confound caveat: model-scale interpretation rests on a 4-bit-MLX-vs-cloud-fp16 comparison; clean model-scale conclusions would need controlled inference setup.
4. Decide whether the 2026-03-22/23 replication-study "equity case" (S015/S018/S025) and the 2026-03-29 Test N S029 finding should be presented as ONE pattern or TWO different ones. The consolidation reads as one; the data supports two.

### Status

Open. Pending paper revision pass.

---

<a id="issue-5"></a>
## Issue 5 — Paper claims directly contradicted by experiment log + raw JSON

**Severity**: Tier 1 (paper-text errors that would be caught by any rigorous reviewer)
**Surfaced by**: 12B-vs-27B history agent 2026-05-11 evening + Pass 8 (this morning's swarm)
**Affects**: specific lines in the May 9 paper draft + ablation diagram

### Problem

Two distinct claims in current paper-side artifacts that contradict the experiment_log and raw JSON:

**5a. `ofb_paper_compiled_source_2026-05-09.md` line 174**:
> "Run on Gemma 12B across the synthetic corpus, the four-axis classifier correctly identified the burnout case (S002)..."

This is **wrong**. Experiment_log line 3349 + 3386-3389 explicitly say 12B 4-axis MISSES S002 (10/10 ENGAGED across all runs). The paper's claim only holds for Gemma 27B cloud (5/6 BURNOUT). Requires correction in pass D revision.

**5b. `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/ablation_diagram.html` line 661**:
> "Gemma 12B: protected students routed to ENGAGED; S002 correctly identified as BURNOUT"

Same error. The ablation diagram propagates the same flattened claim that contradicts raw JSON for 12B.

**5c. `williams_restructure_proposal_2026-05-12.md` lines 303, 307**:
> Mirror paragraph from the May 9 compiled source. Inherits the error.

### Proposed response

Three corrections, all mechanical once the correct claim is decided:

1. Paper line 174: rewrite to scope to Gemma 27B specifically AND name what 12B did (missed). Suggested: *"Run on Gemma 27B cloud, the four-axis classifier identified the burnout case (S002) in 5 of 6 runs. The same four-axis schema on Gemma 12B 4-bit MLX missed S002 in all 10 runs — the model explicitly rejected the burnout reading. The architecture's TP recovery is model-scale-dependent on this corpus."*
2. Ablation diagram line 661: same correction.
3. Williams restructure: inherits correction.

### Status

Open. Apply in pass D / paper revision pass.

---

<a id="issue-6"></a>
## Issue 6 — MLX cache-management protocol needed (recurring issue)

**Severity**: Tier 4 (infrastructure / methodology hygiene)
**Surfaced by**: critic-swarm build-agent review 2026-05-11 + June's response noting "the cache is an issue"
**Affects**: any multi-model MLX run on consumer hardware (24-32 GB unified memory). Specifically the Variant A test if `unload_mlx_model()` weren't called between models.

### Problem

Loading multiple MLX models sequentially without explicit unloading risks memory pressure → swap → 10× slowdown or OOM kill. For the Variant A test, this would have been 12 model loads (3 models × 4 conditions) without unload. Patched inline for that script, but the broader infrastructure concern is real: any test that iterates over multiple models needs the same hygiene, and currently it's per-script rather than a standardized utility.

### Proposed response

Draft a reusable `mlx_model_session` context-manager or similar utility in the autograder's `insights.llm_backend` module that:
- Loads a model when entering scope
- Calls `unload_mlx_model()` on exit (including on exception)
- Optionally tracks load/unload events for memory-pressure debugging

This is a separate, lower-priority task that doesn't block the May 20 paper deadline but should land before the next multi-model test.

### Status

Open. Not blocking paper deadline. Track for post-deadline cleanup or before any future multi-model MLX run.

---

<a id="issue-7"></a>
## Issue 7 — 12B/27B Test N uses different system prompts; "model-scale" interpretation is triple-confounded

**Severity**: Tier 1 (paper-shaping; collapses the "12B vs 27B model-scale" reading)
**Surfaced by**: 12B-vs-27B rationale subagent 2026-05-11 evening while reading prompts side by side
**Affects**: Issue 4 framing, §IV.A.3 / §IV.A.4 / abstract claims about model scale

### Problem

The 27B Test N system prompt has text the 12B version doesn't:

> "The key signal is that the student's MATERIAL CONDITIONS (work schedule, sleep loss, caregiving duties) are breaking through and limiting their capacity. Emotional intensity or personal vulnerability in the writing is NOT burnout."

Plus a *"CRISIS supersedes ENGAGED"* clarification.

The 27B BURNOUT verdicts on S002 explicitly cite "material conditions" and "time constraints impacting ability to complete work" — vocabulary lifted from the 27B-only prompt revision.

Test Q's Q1 ablation (removing the word "exhausting") flips 27B from BURNOUT to ENGAGED on S029 — empirical confirmation that lexical triggers are doing real work.

### Implication

The "12B vs 27B" comparison is now triple-confounded:
1. **Model scale** (12B vs 27B parameter count) — the intended variable
2. **Quantization + inference stack** (12B = local MLX 4-bit; 27B = cloud OpenRouter, likely fp16) — Issue 4 confound
3. **Prompt difference** (27B has additional "material conditions" language and "CRISIS supersedes ENGAGED" clarification) — Issue 7 confound (new)

All three vary simultaneously. The data CANNOT cleanly support a "model scale matters for equity" claim. It can support "this specific 12B-local-4-bit-prompt-A vs this specific 27B-cloud-fp16-prompt-B comparison shows differential behavior" — but that's a much weaker claim.

### Proposed response

1. Pull the model-scale framing from §IV.A.3 / §IV.A.4 / abstract. Replace with "configuration-specific comparison" framing.
2. Either run a controlled experiment (same prompt across models, same quantization, same inference stack) OR acknowledge this comparison can't isolate model-scale and scope claims accordingly.
3. The "12B more reliable than 27B" finding from Round 3 replication (2026-03-22/23) ALSO needs this scoping — were the prompts identical there? Quick check needed.

### Status

Open. **Most paper-consequential single finding from tonight's work.** Requires paper-revision pass.

---

<a id="issue-8"></a>
## Issue 8 — Variant A stripped-observation test completed; coding workshop awaits lead-author hand-coding

**Severity**: Tier 1 (Issue 1's resolution depends on this)
**Surfaced by**: `Autograder4Canvas/docs/research/session_log.md` (2026-05-11 entry — discovered tonight)
**Affects**: Issue 1 resolution, §IV.A.4 framing decisions

### Status

The Variant A test designed earlier today (master log Issue 1) **already ran** 2026-05-11, 97.8 min total. 4 conditions × 3 MLX models × 8 students × n=1 (Llama 8B spot-check returned byte-identical at temp 0.3, so n=1 was sufficient).

### Where the data lives

- **Raw outputs**: `output-format-bias/data/raw_outputs/test_variant_*_2026-05-11.json` (4 files, one per condition)
- **Coding workshop**: `output-format-bias/variant_a_coding_workshop_2026-05-11.html` (awaiting lead-author hand-coding)
- **Session_log entry**: `Autograder4Canvas/docs/research/session_log.md` lines 10-22 (already documents three pre-coding findings)
- **Experiment_log entry**: written 2026-05-11 section of `Autograder4Canvas/docs/research/experiment_log.md`

### Three pre-coding findings already surfaced

Per session_log lines 14-19:

1. **Llama 8B's taxonomy-driven false-positives clear in stripped conditions.** S004 Priya ("deflection") and S024 Ingrid ("fails to acknowledge structural power") false-positive on b_replicate; both clear cleanly under a1, a2, a2_no_context. Direct corroboration of the prompt-load hypothesis.
2. **Stripping the relational/narrative paragraph (a2) makes Llama willing to name minimal effort on S031 Marcus** ("not yet invested") — phrase absent in b_replicate or a1. The relational paragraph was suppressing concern signals on edge-case probes.
3. **Stripping class context (a2_no_context) unlocks new Llama failure mode**: paternalistic background inference on S023 + S028, plus possible fabrication on S023 (Llama describes Yolanda's abuela as undocumented — needs verification against the actual submission). Class-context-stripping introduces new bias rather than just removing priming.

**No model in any condition reads burnout on S002 Jordan Kim.** S002 stays missed across all four conditions and all three models.

### Action queued

Lead-author hand-coding of the variant_a_coding_workshop_2026-05-11.html. Then paper §IV.A.4 framing decision based on what the coding reveals about the prompt-confound vs. format-protection thesis.

### Status

Test complete. Coding pending. Issue 1 stays Open until coding is done.

---

<a id="issue-9"></a>
## Issue 9 — T2C2 S024 is a fabrication (parallel to T2C3 hallucination pattern)

**Severity**: Tier 2 (workshop cell error — but reveals the III.D-shape is more pervasive than the morning swarm caught)
**Surfaced by**: Binary ablation workshop subagent 2026-05-11 evening during rationale-addition pass
**Affects**: workshop T2C2 S024 cell, generalization of the "workshop-as-compression-layer" pattern

### Problem

S024 Ingrid Vasquez has zero records in every Test N 4-axis JSON (Gemma 12B, Gemma 27B, Qwen 7B). The workshop's T2C2 S024 cell previously read "ENGAGED — lived experience routed to ENGAGED" — coherent-sounding cell with no empirical referent.

This is the same III.D-shape hallucination as the morning swarm's T2C3 finding (5 cells fabricated), but for a different column. The morning swarm caught T2C3; missed T2C2 S024.

Subagent fixed the cell to "Not tested" with grey tint and explanation note.

### Implication

The "workshop-as-compression-layer introduces fabrications" pattern is broader than the morning swarm caught. Worth one more pass across ALL workshop cells to check whether others fabricate against zero raw-JSON referents.

### Status

Single-cell fix applied 2026-05-11 evening. Broader audit recommended — see Recommendations register addition.

---

<a id="issue-10"></a>
## Issue 10 — §IV.A.4 rewrite landed; cross-issue paper-edit ripple register

**Severity**: Tier 1 (ripple targets touch §I Intro, §IV.A.1, §IV.A.3 prose + Table 1, §IV.A.6, §IV.B, §VI, abstract)
**Surfaced by**: 2026-05-12 workshop session on §IV.A.4 — corrections + edge-case reframe required ripple identification
**Affects**: every place in the paper that frames S002 as "true positive" / "genuine burnout case," every place that cites 27B comparison data, every place that names Marcus without a last name

### What landed 2026-05-12

§IV.A.4 (Row 3: Four-axis classification) rewritten in `paper/ofb_paper_v3.md` via Edit tool. Scoped variant of Option B from Issue 2: kept the §IV.A.4 section but reframed honestly, without pulling in the full CHECK-IN iteration narrative (Test N → Test O → Test P).

What the rewrite changed:

- Dropped "intermediate point on the compression spectrum" framing (the §IV.A intro already does that work)
- Replaced "after generative observation was developed" with "after generative observation was working" — chronologically more honest about the parallel development of 4-axis and observation
- Reframed ENGAGED as a structural slot for "intellectually meaningful work that is also deeply personal," not as an a-priori design intervention
- Named explicitly that the ENGAGED marker does not surface in the Autograder UX (those considerations are handled by existing subsystems)
- **Corrected the S002 claim**: pure 4-axis on Gemma 12B does NOT catch S002 — it misses S002 in all 10 runs (per Issue 2 finding). Old text claimed 4-axis "correctly identified the burnout case."
- **Dropped all 27B specifics** from §IV.A.4: no "5 of 6 ENGAGED, 1 of 6 BURNOUT," no "~17% misclassification" claim, no model-scale instability claim (per Issue 7 — prompt confound; June hasn't validated 27B comparisons yet)
- Added edge-case framing for S002 (Jordan Kim) and S031 (Marcus Bell) — descriptive, not "designed" (per Issue 3 reframe — see updated status)
- Named the inverse-readings observation: Jordan Kim → ENGAGED, Marcus Bell → BURNOUT, similar trailing-off signals
- Closing sentence: *"Categorical slots accommodate the compression error; they don't exit it."* — replaces "remove" (per June: "remove is not the right word choice for compression. what are we actually doing with the design?")

### Session decisions feeding downstream ripples

1. **S002 reframed from "genuine burnout case / true positive" to "edge case."** Corpus pattern label is "burnout" but the textual signal is ambiguous (strong analytical work that trails off mid-sentence: *"Idk I had more to say but its late and"*). Even generative observation reads it as "rush to finish... running low," not as burnout (experiment_log line 1841). No `design_notes` field for S002 in `replacement_students.json` (Marcus has design_notes; Jordan doesn't).

2. **Marcus reframed from "minimal effort, expected CLEAR" to "edge case."** Design notes claim *"True minimal effort... NOT pathologized"* but the actual text is more articulate than the design intent suggests — names intersectionality correctly in 44 words before *"idk what else to say about it."* The corpus generation may not have differentiated as cleanly as design intent did. Per June 2026-05-12: *"we don't have to call it designed to be edge cased. We can just say that they are edge cases."*

3. **Word-count comparison context** (from `Autograder4Canvas/data/demo_corpus/ethnic_studies.json`, 32-student corpus):
   - Marcus Bell (S031): 44 words — corpus's shortest
   - Jordan Kim (S002): 89 words — second-shortest
   - Median: 188 words; mean: 175; max: 230 (Priya Venkataraman S004)
   - Marcus at 44 is ~1/4 the median and ~1/5 the longest submission

4. **Name convention** for §IV.A.4: full first+last on first mention with S-number in parens — "Jordan Espinoza (S029)," "Jordan Kim (S002)," "Marcus Bell (S031)" — then full name on subsequent mentions in the paragraph. Disambiguates Jordan Kim from Jordan Espinoza.

### Ripple targets — HELD pending validation work

Each target depends on resolution of one or more open validation issues. **Do not apply ripples until the entangled validation questions are settled.** The interpretation pass on `data_tables/` is the gating work — settled data anchors the ripple text.

| # | Target | Current text | Reframe direction | Depends on | Status |
|---|---|---|---|---|---|
| 1 | **§I Intro** (line 20) | *"one true positive (S002 Jordan Kim, the only student in the corpus with genuine burnout indicators) and seven false positives"* | Drop TP claim. Minimal version: *"eight flags, seven of them equity-critical false positives"* | Issue 2 (S002 reframe); confirmation 8 flags / 7 false positives holds across validated runs | HELD |
| 2 | **§III.B Methods** (line 86) | *"and one genuine burnout case (S002 Jordan Kim)"* — corpus description | Drop "genuine burnout" framing. Either remove S002 from this list, or describe as *"one case designed with a burnout pattern label"* | Issue 2 (S002 reframe) | HELD |
| 3 | **§IV.A.1 opening** (line 124) | *"one true positive (S002 Jordan Kim) and seven equity-critical false positives"* — iteration history opening | Parallel to #1 | Issue 2 | HELD |
| 4 | **§IV.A.1 class-context iteration** (line 126) | *"12 flags, zero true positives, six confirmed false positives on protected students"* — the "zero true positives" implicitly invokes S002 as the missed TP | Cut "zero true positives" — argument holds with just *"12 flags, six confirmed false positives on protected students"* | Issue 2; load-bearing claim is the 6 FPs, not the missed TP | HELD |
| 5 | **§IV.A.1 second-attempt** (line 128) | *"The classifier also missed S002, the only burnout case"* + *"lost true-positive sensitivity"* | Cut the S002-as-only-burnout-case claim and the "lost true-positive sensitivity" framing. Surviving sentence: *"The simpler specification traded false positives on race and lived-experience axes for a new failure mode on disability."* | Issue 2 | HELD |
| 6 | **§IV.A.3 prose** (line 166) | *"Jordan Kim (S002), the only student in the corpus with burnout indicators, is cleared 24 of 24 times"* + *"traded sensitivity on the only true positive in the process"* | Reframe S002 as edge case; drop "only true positive" | Issue 2 + Table 1 verification | HELD |
| 7 | **§IV.A.3 Table 1** (line 156) | S002 row: Expected = FLAG; Result column says "missed" | Edge-case framing for Expected column; or drop the "missed" notation; or restructure | Issue 2 + verification that Table 1 cell values match raw JSON | HELD |
| 8 | **§IV.A.6** (line 186) | *"surviving at ~17% on the Gemma 27B decision boundary"* | Drop the 17% claim — inherits prompt-confound from Issue 7 | (was: Issue 7 + 4 + 27B validation) | **APPLIED 2026-05-12** — parenthetical cut; resulting sentence: *"attenuates under the four-axis classifier and does not reappear under generative observation"* |
| 9 | **§IV.B** (line 195) | *"Generative observation missed one true positive across all four assignments"* | Check whether this needs reframe given synthetic-corpus changes — different student/context, may be fine as-is | Variant A coding (Issue 8) | HELD |
| 10 | **Abstract** | Scan for "burnout" / "S002" / "true positive" / "the burnout case" appearances | Update if equivalence-of-framing required by upstream ripples | Issues 2, 3 | HELD |
| 11 | **§VI Conclusion** | Scan for S002 references — none found 2026-05-12 (Conclusion only references S029) | No action | — | **VERIFIED CLEAN 2026-05-12** |

### Cross-paper consistency items (independent of validation outcomes)

**Verified clean 2026-05-12 (no action needed):**
- ✓ All "Marcus" mentions in the paper already use "Marcus Bell" or "S031 Marcus Bell" — no bare "Marcus" found
- ✓ All Jordan Kim / Jordan Espinoza mentions carry S-number prefix or last name — disambiguation consistent throughout

**Open consistency item (not blocking; final-pass cleanup):**
- Naming convention is mixed across the paper: some places use "S### Firstname Lastname" (e.g., line 156 Table 1; line 86 corpus description) and others use "Firstname Lastname (S###)" (e.g., lines 166, 174, 245). Pick one and propagate at final-pass.

### The meta-pattern

Ripple work IS downstream of validation work. Applying ripples while validation is open creates a moving target — each ripple risks introducing claims contradicted by subsequent validation findings. June 2026-05-12: *"these are all entangled with other questions that are open from the validation path."*

**The shared system**: interpretation pass on `data_tables/` settles data-side questions → settled data anchors ripple text → ripple work proceeds against the punch list above.

### Status

**§IV.A.4 rewrite LANDED.** Ripples HELD. Cross-paper consistency items (name convention) can proceed independently. Interpretation pass on `data_tables/` is the gating work for the ripple register.

---

<a id="issue-11"></a>
## Issue 11 — Paper's corpus description undercounts the actual testing corpora used

**Severity**: Tier 1 (foundational — corpus description in §III.B and §IV.A.1 is what every results claim refers back to; rewriting it forces ripple changes through Methods, Findings, and Abstract)
**Surfaced by**: Conversation 2026-05-12 — June: *"we'll want to update the information about the testing history to include the ~20 student that existed before the 32 student corpus, and the 14 WB students"* + *"this is one of those ripply changes that everything else is dependent on"*
**Affects**: Abstract, §III.B Methods, §IV.A.1 iteration history, downstream Issue 10 ripples #1–#3 (which touch the same prose region)

### What the paper currently says about the corpus

- **Abstract** (line 8): *"a synthetic corpus of 32 essays"* — single-corpus framing
- **§III.B Methods** (line 86): *"a 32-student synthetic corpus designed for controlled testing of equity-critical patterns"* — only the 32-student corpus is named
- **§IV.A.1 iteration history** (line 124): *"Phase 1 tested the binary classifier on a ~20-essay synthetic corpus... In Phase 2, that hardened classifier ran against the 32-essay corpus for the first time"* — Phase 1 ~20 mentioned and Phase 2 32 mentioned, no description of what they contain or how they relate
- **WB1–WB14 corpus**: not mentioned anywhere in the paper

### What actually exists (verified 2026-05-12)

Three distinct synthetic corpora across the testing history:

1. **~20-student Phase 1 corpus** — earlier ethnic studies corpus used for cross-family model selection (Phase 1, footnote on §III.D names Gemma 12B, Qwen 7B, Llama 70B, Deepseek, Qwen 32B as the cross-family Phase 1 models). Exact composition needs confirmation — may have been an early draft of `data/demo_corpus/ethnic_studies.json`. June to recall, or reconstruct from git history of `data/demo_corpus/` if needed.

2. **32-student equity corpus** — `Autograder4Canvas/data/demo_corpus/ethnic_studies.json`. Word counts 44–230, median 188, mean 175. The corpus that every §IV.A ablation Table refers to. Includes equity-critical profiles (S022 Destiny Williams, S023 Yolanda Fuentes, S028 Imani Drayton, S029 Jordan Espinoza), strong/control profiles (S004 Priya Venkataraman), and edge cases (S002 Jordan Kim, S031 Marcus Bell).

3. **14-student wellbeing corpus (WB01–WB14)** — defined inline in `Autograder4Canvas/scripts/run_alt_hypothesis_tests.py` (NOT in any `data/demo_corpus/` JSON file). Word counts 93–165, mean 119. Two creation events:
   - **WB01–WB10 created 2026-03-27** for Test G (first wellbeing signal detection on observation outputs). Cases: Rosa Gutierrez (ICE stress, CRISIS), Keisha Williams (caregiving exhaustion, BURNOUT), Miguel Sandoval (housing loss, CRISIS), Jasmine Torres (DV-adjacent, CRISIS), Tyler Reed (work burnout, BURNOUT), Amira Hassan (food insecurity, CRISIS), Sofia Reyes (tonal rupture/disclosure, CRISIS), Brandon Mitchell (grief, CRISIS), Priya Sharma (analytical control on ICE topic, ENGAGED), DeAndre Washington (passionate analytical control, ENGAGED).
   - **WB11–WB14 added 2026-04-01** for community-resilience guard extension after WB06 finding (community framing was being read as "less severe"). Cases: Kaya Runningwater (Indigenous tribal food distribution + housing crowding, CRISIS), Jasmine Rollins (Black church food pantry after parent job loss, CRISIS), Amara Osei (Ghanaian susu rotating credit after eviction, CRISIS), Marcus Tran (analytical writing about community wealth frameworks, ENGAGED — the "no false positive on community-wealth analysis" control).

The WB corpus is the corpus the §IV.A.4 four-axis classifier was tested against for wellbeing-detection sensitivity (Tests G, H, I, L, N, O, P). The §IV.A.4 claims about 4-axis behavior on **equity-critical profiles** use the 32-student corpus; any 4-axis claims about **wellbeing-detection accuracy** (e.g., "8/8 WB signals caught") would draw from the WB corpus. The paper currently elides this distinction.

### Adjacent: long-form corpus (separate from WB; not directly affected)

`data/demo_corpus/phase1_long_form.json` contains LF01–LF07 (7 students, 623–1129 words each). Used for the long-form chunking test (Phase 1 essays test, March 28), not for wellbeing or format-effect work. Mentioned here for completeness — distinct corpus from the three above; only ripple-relevant if the paper later cites long-form chunking work.

### Confirmed: WB1–WB14 are NOT the long-essay students

Direct verification 2026-05-12: WB cases live in `scripts/run_alt_hypothesis_tests.py`; LF cases live in `data/demo_corpus/phase1_long_form.json`. Different files, different IDs (WB vs. LF), different word-count ranges (93–165 vs. 623–1129), different purposes. The earlier-conversation question is answered: **separate corpus.**

### Why this matters (June 2026-05-12)

*"This is one of those ripply changes that everything else is dependent on."* The corpus description is foundational — every results claim implicitly refers to one of these corpora. If Methods says "the 32-student corpus" and Results cite WB-corpus findings, the reader can't trace the data back to its source. Rewriting the corpus description unlocks ripples through:

- **Abstract**: single-corpus framing → multi-corpus framing
- **§III.B**: 32-student-only description → name all three relevant corpora and their purposes
- **§IV.A.1**: Phase 1 ~20 bare mention → name what the ~20 contained, how it relates to Phase 2's 32
- **§IV.A.4**: 4-axis "wellbeing detection" claims (currently absent or implicit) — if explicit, name the WB corpus; if implicit, decide whether to make explicit
- **§IV.B live-data**: separate from this issue (uses real student data, not synthetic) but worth scoping the synthetic-corpora claim against

### Open subitems for the rewrite

1. **Confirm what the ~20-student Phase 1 corpus actually contained.** June to recall, or reconstruct from git history of `data/demo_corpus/ethnic_studies.json` (look for commits before 2026-03-26 that established the corpus shape).
2. **Decide framing**: name all three corpora explicitly in §III.B, OR consolidate into a single "synthetic test materials" description with the differences in a footnote, OR keep §III.B focused on the 32-student equity corpus and add a separate corpus-introduction paragraph for the WB cases at the point in §IV.A where wellbeing-detection results would be cited.
3. **Decide whether to cite wellbeing-detection results from the WB corpus in the paper at all.** Currently §IV.A.4 makes claims about 4-axis on equity-critical profiles (32-student corpus) but not about wellbeing-detection sensitivity (WB corpus). If the wellbeing-detection numbers are paper-relevant, where do they go and how are they framed?

### Sequencing relative to Issue 10

The corpus rewrite is **upstream** of Issue 10's ripple targets #1 (Intro), #2 (§III.B), #3 (§IV.A.1) — all of which touch the same prose region. Recommended sequence: do Issue 11 corpus rewrite first (foundational), then Issue 10 ripples on top of the new corpus framing. The §IV.A.4 rewrite that already landed (per Issue 10) can stand on its own; the corpus rewrite doesn't disturb it.

### Status

**Open.** Documentation of the WB1–WB14 origin question and the corpus-claims gap captured 2026-05-12 so we don't have to re-discover it. Awaiting June's decisions on framing + Phase 1 corpus reconstruction. Treat as upstream of Issue 10 ripples #1–#3.

---

<a id="source-of-truth"></a>
## Source-of-truth framework

JSON is NOT blanket-authoritative (corrected per June 2026-05-11 evening):

| Situation | Source of truth |
|---|---|
| JSON exists + log agrees | Both consistent; cite either |
| JSON exists + log disagrees | **JSON wins** — log has known errors (Test B/C tables) |
| JSON does NOT exist + log is the only record | **Log narrative is what we have**, with caveat about retroactive provenance |

The "missing data" items (Pass 2 + Pass 3) are NOT "we don't know what happened" — they're "log narrative is the only record; trust it within the limits of retroactive-provenance uncertainty."

Drift doc fully documents this at `data_tables/verification_2026-05-11/log_vs_json_drift_2026-05-11.md`.

---

<a id="session-logs"></a>
## Session_log sources — four files (test-monitor skill convention)

We were treating `Autograder4Canvas/docs/research/session_log.md` as the only narrative source besides the experiment_log. Four exist:

| File | Lines | Role |
|---|---|---|
| `Autograder4Canvas/docs/research/session_log.md` | 116 | Active state file. Contains 2026-05-11 Variant A test results + 2026-04-13 to 2026-05-10 context. |
| `output-format-bias/research/session_log.md` | 111 | Mirror of autograder version (likely; needs explicit confirmation) |
| `Autograder4Canvas/docs/research/logs/session_log_2026-04-02.md` | 128 | Archived April 2 snapshot |
| `output-format-bias/research/logs/session_log_2026-04-02.md` | 128 | Mirror of archived version |

**Important**: line 116 of the active session_log claims *"Experiment log: ~6800+ lines. All entries verified against raw JSON."* This claim is **known false** — Pass 2/3/8 all flagged uncorrected Test B/C errors. The session_log's own status claim is stale documentation.

---

<a id="validation-pass-index"></a>
## Validation pass index — comprehensive chronological record

This project has had **13 distinct validation efforts** between 2026-03-21 and 2026-05-12, not the 8 I mentioned earlier. Sub-passes of 7 (gen-ob audit, contradiction catalog, paper-edit JSON audit) and two pre-c2c-era passes (pipeline evaluation, fragility audit) bring the count to 13.

Organized chronologically. Each row: pass-name | scope | doc location | key finding | implementation status.

### Pre-c2c era

**Pass 0a — Pipeline evaluation + Methodology audit (Opus)** — 2026-03-21/22
- Scope: 29-student demo corpus pipeline output vs raw submissions
- Doc: `output-format-bias/pipeline_evaluation.md` (~300 lines) + `comparison_analysis.md`
- Finding: pipeline missed that 19/29 submissions were DAIGT-adapted off-topic essays
- Status: completed; shaped scope claims since

**Pass 0b — Pipeline-wide enumerative fragility audit** — 2026-04-27
- Scope: research-track binary classifier failure modes
- Doc: `experiment_log.md` line ~6706; full enumeration at `research/binary_fix_attempts_enumeration_2026-04-27.md` (~700 lines)
- Finding: 7 distinct fix mechanisms attempted within binary format, all with measurable failure modes on protected populations
- Status: completed; cited throughout paper

### Canonical numbered passes (c2c era)

**Pass 1 — s2 convergent-claim production** — 2026-04-25 evening
- Doc: `c2c_sessions/output-format-bias-session-2_2026-04-25/artifacts/convergent_claim_session2_v1-v4.md`
- Status: superseded by Pass 2 corrections

**Pass 2 — Direct raw-JSON-vs-narrative validation** — 2026-04-25/26 (THE canonical one)
- Scope: 81 raw JSONs cross-checked against s1 handoff + s2 artifacts; produced a 984-line verification table
- Doc: `c2c_sessions/output-format-bias-session-2_2026-04-25/REVIEW_FOR_JUNE.md` + `verification_table.md` + `verify_raw_outputs.py` + `rerun_original_naive_concern.py` + `rerun_log.txt`
- Finding: 5 corrections + 4 gaps documented; Apr 26 rerun launched as part of this pass to recover lost-Mar-24-3/7 analog
- Status: completed; corrections appendix added to `experiment_log.md` at line 6721+; paper integrated most; **original Test B / Test C tables in log (lines 1817-1870) NEVER corrected** — see [Recommendations register](#recommendations-register) item B.1

**Pass 3 — Independent two-instance audit OF Pass 2** — 2026-04-26
- Scope: two instances (Opus A + Sonnet B) independently re-verified ~10 claims each against raw JSON; missing-files hunt
- Doc: `c2c_sessions/data-verification-audit_2026-04-26/artifacts/audit_report_instance_a.md` (152 lines), `audit_report_instance_b.md` (194 lines), `CONVERSATION.md`
- Finding: 6 new findings beyond Pass 2 — retroactive-provenance is systematic; Test C has same log-vs-JSON conflict Pass 2 missed; Test B uses class context (collapses format/architecture distinction); "16/16 across three families" conflates Test A and Test E; April 14 Test B reruns are 5 min apart; "production_concern_detector" label is in JSON metadata; `reading_first_comparison.json` recovered (not lost)
- Status: completed; findings partially applied; provenance qualifications + label corrections NOT applied — see [Recommendations register](#recommendations-register) items B.2 + B.3 + B.4

**Pass 4 — C-scrutiny independent reads** — 2026-04-28 morning
- Scope: structured-classifier-blind reads of 75 submissions across Week 7 / Week 2 / Week 5 by parallel A (Opus 4.7) + B (Sonnet 4.6); selection-bias correction
- Doc: `c2c_sessions/output-format-bias-c-scrutiny-and-s4-prep_2026-04-28/artifacts/pass1-3 files (~1800 lines total)
- Finding: substantive null on system-misses (paper's C accuracy claim survives); 4 finding categories; Week 7 plausible-BURNOUT under-read by both A + B (methodological insight: human readers face same disambiguation challenge as structured classifiers)
- Status: completed; integrated into paper §IV.B / Discussion as "complementary-by-design" framing

**Pass 5 — Astra Fellowship reviewer-subagent feedback** — 2026-05-02
- Scope: technical AI-safety reviewer reads OFB summary
- Doc: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/REVISION_NOTE_2026-05-02_self_contradiction_as_mechanism.md` (57 lines)
- Finding: strongest evidence pillar (self-contradiction in Row 1) is currently de-emphasized; restructure §IV.A evidence ordering recommended
- Status: **NOT YET IMPLEMENTED** — 9 days old; partially superseded by Pass 8 — see [Recommendations register](#recommendations-register) item B.6

**Pass 6 — Citation gaps revision-note** — 2026-05-04
- Scope: REE submission citation prep
- Doc: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/REVISION_NOTE_2026-05-04_citation_gaps.md` (195 lines)
- Finding: 9 citations need verification (Caldwell, Chinta, Hew, Liu, Queiroga, Bonilla-Silva, Xu, Long)
- Status: 5 resolved by 2026-05-12 citation_resolution_report; 4 still open — see [Recommendations register](#recommendations-register) item B.13

**Pass 7a — Generative-observation validation audit (parallel registers)** — 2026-05-10
- Scope: two parallel subagents audit gen-ob outputs against stereotype-aligned-language predictions from Liu / Tan / Phalen / Demszky / Kwako / Ormerod; one register general critical-AI, one CRT/DisCrit/feminist
- Doc: `validation_audit_genobs_2026-05-10.md` (82 lines)
- Finding: format-change claim holds; subtler patterns surface (asymmetric emotional-context naming, asymmetric corrective framing race vs disability, meta-analytical suspicion catching resistant capital, curative imaginary still routes through binary)
- Status: completed; S029-introduced-by-calibration finding applied to §IV.A.3 on 2026-05-10; remaining findings produced §V.C audit caveat but not yet in paper text

**Pass 7b — Contradiction catalog (cross-test inventory)** — 2026-05-10
- Scope: 30-instance inventory of self-contradictions where model names an exception then flags
- Doc: `contradiction_catalog_2026-05-10.md` (101 lines)
- Finding: 30 distinct contradiction instances across 9 test architectures, 9 dates, 3 model families; most reproducible is S029 ("While this is related to their academic work")
- Status: completed; flagged for §IV.A.3 potential addition (PARKING_LOT item 6); **NOT YET inserted into paper** — see [Recommendations register](#recommendations-register) item B.11

**Pass 7c — Two-source validation of §IV.A.1 + §IV.A.2** — 2026-05-10
- Scope: paper §IV.A.1/2 narrative against preserved JSON; parser-faithfulness check for Test C
- Doc: PARKING_LOT_2026-05-10.md §SESSION SUMMARY
- Finding: 6 paper edits applied (line 183, 177, 131, 133, 127, 169, 97)
- Status: applied to paper 2026-05-10

**Pass 8 — 12-agent paired verification swarm + paper-wide factcheck** — 2026-05-11 morning
- Scope: 6 paper-claim "columns" × verifier + disconfirmer (12 agents) + 1 paper-wide fact-check
- Doc: `c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/verification_2026-05-11/` (14 files including `PUNCH_LIST_2026-05-11.md`)
- Finding: 24 items in 5-tier punch list. Tier 1 includes: Qwen 7B falsifies "asset-framed in every run" (12/34 deterministic); S002 BURNOUT recovery is 27B-only; abstract "28 runs" → 22 unique; deterministic outputs at temp 0.3 reframe "n=X"; §IV.A.2 Row 1 mischaracterization. Tier 2 includes T2C3 cell hallucinations, T2C2 S031 contradiction, S024 unsupported. Tier 3 mechanism overreach (S028 race/gender not disability). Tier 4 quote fidelity. Tier 5 numeric + structural including the experiment_log Test B/C flag swap.
- Status: in progress — many items NOT YET addressed — see [Recommendations register](#recommendations-register) items B.7–B.10

**Pass 8b — Iteration history extraction + 4-axis architecture mapping** — 2026-05-11 afternoon
- Scope: pulled Test L / N / O / P JSON data across 8 workshop students; mapped CHECK-IN as load-bearing mechanism; surfaced prescan + 4-axis live deployment without controlled ablation
- Doc: `verification_2026-05-11/4axis_iteration_history_2026-05-11.md` + `4axis_iteration_workshop.html`
- Finding: "4-axis recovers TP" claim depends on which architecture; pure 4-axis on Gemma 12B never catches S002; CHECK-IN flag does the wellbeing-recovery work; prescan + 4-axis live deployment exists but controlled test crash-aborted
- Status: feeds Issue 2 + Issue 4 + Issue 5

**Pass 9 — Cross-reference verification + paper-wide review** — 2026-05-12 (overnight, ahead of today)
- Scope: 4 overnight agents on crossref verification, citation resolution, Williams diagnostic restructure, REE submission checklist
- Doc: `crossref_verification_2026-05-12.md`, `citation_resolution_report_2026-05-12.md`, `williams_restructure_proposal_2026-05-12.md`, `ree_submission_checklist_2026-05-12.md`, `MORNING_BRIEF_2026-05-12.md`
- Finding: 2 broken refs (Test D + III.D hallucination); 6 minor inconsistencies; 5 tentatives resolved; 4 author-name errors caught; Williams restructure proposed (481 words saved); REE checklist
- Status: June responded with marginalia 2026-05-12; many items still queued

### Cross-cutting observations

- **Total recommendations across passes**: ~40-50 distinct items (Pass 8 alone is 24)
- **Implementation rate**: ~15 applied, ~25-30 queued/unapplied
- **Validation-of-validation gaps**: Pass 2's corrections were treated as ground truth; Pass 3 caught that Pass 2 inherited the retroactive-provenance gap; Pass 3 framing corrections still unapplied. Pass D draft was written pre-Pass-8; Pass 8 punch list requires Pass D revisions before atomic swap.
- **Recurring failure mode**: Pass 2 (2026-04-25), Pass 3 (2026-04-26), and Pass 8 (2026-05-11) all flagged the experiment_log Test B/C table flag swap. Three separate validation passes; correction never propagated to the original table; corrections appendix added but original tables left as-is. This is the headline example of the workshop-as-compression-layer pattern.
- **Reusable infrastructure**: Pass 2 produced `verify_raw_outputs.py` as a script. Never re-run since 2026-04-25. Could re-validate current JSON state cheaply.

---

<a id="recommendations-register"></a>
## Recommendations-not-implemented register — prioritized

Recommendations from validation passes that have NOT been applied. Listed by priority for paper deadline.

### B.1 — Test B / Test C experiment_log table flag swap ★★★ HIGHEST PRIORITY

**Flagged three times** (Pass 2, Pass 3, Pass 8). Never corrected in the original tables.

- File: `output-format-bias/research/experiment_log.md` AND `Autograder4Canvas/docs/research/experiment_log.md` (byte-identical)
- Lines:
  - 1817-1827: Test B results table shows S029 = CLEAR (raw JSON shows FLAG in 3/3 runs)
  - 1857: Test C results table shows S023 = FLAG (raw JSON shows CLEAR)
  - 1870: narrative reads "Test B cleared S023 and S029, while Test C flagged them" — wrong on both data points
- Corrections appendix at line 6721+ documents what's correct, but original tables were never edited
- Action: inline-mark corrections (per June's "don't delete, mark + correct" direction)
- Status: APPLIED 2026-05-11 evening (this pass) — see [Visual artifacts](#visual-artifacts) below for the marker format

### B.7 — Pass 8 Tier 1 items ★★★

Five paper-text revisions needed:
1. Scope "asset-framed in every run" claim to Gemma family or use Qwen as productive counterexample
2. Reframe §IV.A.3 / §IV.A.4 to show S002 recovery is model-scale × slot, not architectural
3. Correct abstract "28 runs" → 22 unique runs
4. Recast "n=X runs" framing as repeated emissions at temp 0.3, not independent samples
5. Replace §IV.A.2 Row 1 description ("minimal binary, no equity-protective language") with actual JSON config (full production CONCERN_PROMPT)

Status: queued for paper revision

### B.10 — Pass 8 Tier 4 quote fidelity ★★

Three quote-attribution corrections:
1. T1C2 S022 quote truncation: workshop ends at "deprivation" but model continues "and lack of access to essential resources"
2. T1C2 S023 cell body says "AAVE register cleared" — should be "lived experience cleared" (row-label drift)
3. **T1C3 S023/S024 self-contradiction attribution swap**: the verbatim "While not a direct wellbeing concern... [flagged at 0.8]" quote belongs to S024, not S023. **Paper §IV.A.2 line 145 attributes to S023 (Yolanda) — needs to swap to S024 (Ingrid)**. Load-bearing.

Status: queued for paper revision

### B.6 — REVISION_NOTE 2026-05-02 evidence-ordering reframe ★★

9 days old. Astra reviewer recommended §IV.A restructure to lead with self-contradiction (Row 1) → calibration limit (Row 2) → format change (Row 3) → S028/S029 as diagnostic. Currently de-emphasized. Pass D draft (`proposed_IV_A_restructure_2026-05-11.md`) does not lead with self-contradiction in the way 2026-05-02 recommends.

Status: needs to be folded into pass D revision

### B.11 — Test R contradiction-of-exceptions exhibit ★★

Pass 7b contradiction catalog identified Test R as the sharpest preserved self-contradiction case (model explicitly denies the prompt's exceptions and flags anyway). Worth adding to §IV.A.3 as a discrete exhibit.

Status: queued for paper revision

### B.8 — Pass 8 Tier 2 workshop cell corrections ★

- T2C3 cells for S002/S004/S023/S029/S031 are hallucinations (Tests A/E contain only S022 + S028) — mark "not tested in this column"
- T2C2 S031 contradicted (workshop "ENGAGED. Cleared." vs raw 9/17 BURNOUT)
- T1C4/T2C1 S024 unsupported
- T1C4/T2C1 "32-student corpus" wrong for Test M (actual: 7 corpus + 10 synthetic = 17)
- T2C2 S023 ENGAGED obscures 2/17 CRISIS misroute (Gemma 12B 1/10 + Qwen 1/1)

Status: queued for workshop cell pass (next step after master log review)

### B.9 — Pass 8 Tier 3 interpretive overreach ★

- T1C4/T2C1 S028 Test M is race/gender axis per model rationale, not disability-on-AAVE
- T1C1 S002 "burnout signal absorbed as resilience" — model actually dismisses as "late-hour fatigue / engagement with course material," not resilience
- T1C1 S023 "race / language axis" → drop "/ language" (model reasons about immigration/economic hardship, never language)

Status: queued for workshop cell pass

### B.2 — Provenance qualifications on Pass 2 corrections (Pass 3 finding)

Recommended language: "JSON shows X; log narrative describes Y; JSONs committed retroactively; we report JSON values while noting log may describe an unpreserved run."

Status: NOT applied to paper

### B.3 — "16/16 across three model families" itemization (Pass 3 + Pass 8)

Replace summary count with itemized: Test A = 10 Gemma 12B + 6 Qwen 7B; Test E = 6 Qwen + 6 Gemma 27B; total 22 distinct runs not 16.

Status: NOT applied

### B.4 — "production_concern_detector" JSON label drift (Pass 3)

JSON metadata `codepath` field encodes "production_concern_detector" but the test was running research-track variants. Methods should acknowledge label drift OR regenerate metadata.

Status: NOT applied

### B.13 — Open citations (4 remaining from Pass 6 + Pass 9)

Caldwell publisher, Bonilla-Silva edition+pages, Hew authorship/arXiv, Xu/Long re-verify.

Status: 5/9 resolved 2026-05-12; 4 still open

### B.15 — PUBLICATION_PIPELINE.md staleness flag (2026-04-21)

Doc self-reports staleness. Status fields ("Prepping for submission" on OFB) match reality but doc hasn't been re-validated.

Status: deferred

### TODO — consider adding validation-passes note in paper supplementary

Either §III methodological note or supplementary materials. Sentence-level: "Results validated through 13 independent passes between 2026-04-25 and 2026-05-12, including a comprehensive raw-JSON-vs-narrative audit (Pass 2), independent two-instance verification (Pass 3), structured-classifier-blind reads for selection-bias correction (Pass 4), and a 12-agent paired verification swarm (Pass 8)." Buys reviewer credibility cheap. June's decision after she reviews this log.

---

<a id="visual-artifacts"></a>
## Visual artifacts — what's been built + corrected when

**2026-05-11 evening — June moved review artifacts to a dedicated `data_tables/` directory at paper root.** This is version-controlled (the c2c session path was gitignored). All three review tables now live there.

| Artifact | Path (new canonical location) | Status as of 2026-05-11 evening |
|---|---|---|
| **Binary ablation workshop** | `data_tables/ablation_workshop.html` | **Subagent dispatched 2026-05-11 evening** to apply Tier 2/3/4 morning-swarm corrections to `DEFAULT_CELLS` + add verbatim model rationale to each cell. Workshop's localStorage may carry stale edits — Reset to Defaults after subagent completes. |
| **4-axis iteration workshop** | `data_tables/4axis_iteration_workshop.html` | **Subagent dispatched 2026-05-11 evening** to add verbatim model rationale to each cell (validates the agentic coding labels). Cell data already built fresh from raw JSON earlier this evening. |
| **12B-vs-27B differential table** | `data_tables/12B_vs_27B_differential_table_2026-05-11.html` | **Subagent dispatched 2026-05-11 evening** to add side-by-side 12B+27B rationale pairs to each row, with special focus on Test N S002 + S029 (the load-bearing single-experiment findings). |
| Ablation diagram | (deleted 2026-05-11 evening by June — was stale) | N/A |
| Log-vs-JSON drift tracker | `c2c/c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/verification_2026-05-11/log_vs_json_drift_2026-05-11.md` | **Built 2026-05-11 evening.** 9 drifts + 6 missing-data items. |
| Master response log | `MASTER_RESPONSE_LOG_2026-05-11.md` (paper root) | This file. |
| Punch list (morning swarm) | `c2c/c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/verification_2026-05-11/PUNCH_LIST_2026-05-11.md` | 24 items in 5-tier list. Source for Issue 2, B.7, B.8, B.9, B.10. |
| 4-axis iteration history (data) | `c2c/c2c_sessions/output-format-bias-session-4_2026-04-28/artifacts/verification_2026-05-11/4axis_iteration_history_2026-05-11.md` | Plain markdown table data backing the 4-axis workshop. |
| Variant A test script + handoff | `scripts/run_variant_a_stripped_observation.py` + `scripts/VARIANT_A_TEST_HANDOFF.md` | Built 2026-05-11; awaiting test-monitor session launch. |

**Note on the data_tables/ directory**: this directory is now the **canonical review surface** for June. The three HTML tables are designed for visual scan + cross-validation across the binary calibration ladder, 4-axis iteration history, and 12B/27B differential. Each table includes (or will include after subagent completion) verbatim model rationales so June can validate verdicts by reading what the model said, not just trusting the classification label.

---

<a id="evening-plan-2026-05-11"></a>
## Paper-prep action plan — captured 2026-05-11 late evening

This section is the durable plan for the remaining paper-prep work. Captured during a fresh-context interpretation pass that surfaced several big-picture fixes that will resolve clusters of smaller issues. Status flags: **OPEN** (queued, not started), **IN PROGRESS** (started this session), **DATA LANDED** (subagent or verification returned findings; awaiting interpretation/integration into paper).

### Reframings (paper text + workshop cells)

**P1. Reframe Marcus (S031) + Jordan Kim (S002) as designed edge-case probes.** [IN PROGRESS — workshop Marcus cells reframed 2026-05-11 evening, Jordan Kim still framed as clean TP]. Both students were specifically designed to probe what the classifiers do at the boundary of detection — Marcus's minimal-effort + closing-off signal, Jordan Kim's subtle trailing-off burnout. They are not clean controls / clean TPs. Workshop visual coding for Marcus updated (lavender for "caught the designed-probe signal," violet for "missed it"); equivalent reframing for S002's workshop cells still needed. Paper text needs explicit edge-case-probe framing rather than "binary missed the TP" simplifications.

**P2. Add 10-student WB synthetic corpus framing to paper.** [OPEN]. The WB01-WB10 synthetic corpus (Rosa, Keisha, Miguel, Jasmine, Tyler, Amira, Sofia, Brandon, Priya control, DeAndre control) is the core burnout/crisis sensitivity test that the current paper draft underweights. Plus WB11-WB14 community-resilience extension (Indigenous tribal distribution, Black church food pantry, West African susu, control). Paper needs explicit framing of what this corpus is for (testing actual wellbeing-signal detection independent of the equity-critical corpus) and what it shows. Inventory documented in subagent report 2026-05-11 evening.

### Tables (paper + workshop)

**P3. Build WB10 binary vs 4-axis comparison table.** [DATA LANDED]. Test H (binary B + binary C on WB cases) and Test N (4-axis on WB cases) results are in raw JSON. Headline: Test N 8/8 + 2/2 controls = **10/10**; Test B 7/8 (missed Rosa ICE stress); Test C 3/8 (length-collapse). Test I (Tier 2) added later — 8/8 but 1 FP on Priya control. Table includes all available recent runs; cut what's not needed for paper.

**P4. Add WB tests to test_timeline.html.** [OPEN]. Test H (2026-03-27), Test G (2026-03-27 generative observation), Test I (2026-03-28 Tier 2), Test N WB runs (2026-03-28), and any recent WB-relevant reruns need to sit in the timeline alongside corpus-student tests.

**P5. Add original-binary 3/7 self-contradicting row to Table 1.** [OPEN]. The original naive binary run (Destiny S022, Yolanda S023, Ingrid S024 flagged 3/3 with self-contradicting "While not a direct wellbeing concern... [flagged at 0.8]" rationales) is documented in experiment_log notes only — raw data didn't persist. Add to Table 1 with a "raw data not preserved; documented in experiment_log" note. This row anchors the historical failure mode the calibration was designed to address.

### Pending data dependencies

**P6. Assess "binary is now working" claim — pending Ingrid result.** [WAITING ON RERUN]. test_r (2026-05-10) showed both equity-critical flags (Destiny @ 0.4, Jordan E. @ 0.6) sub-threshold — 0.7 production cutoff suppresses both. But underlying compression error still fires (Destiny's redlining sentence read as autobiographical food insecurity, not anger). The "binary now works" claim depends on Ingrid rerun (5 reps, S024 added to corpus, queued 2026-05-11 evening). If Ingrid clears, calibration-does-equity-work framing holds. If Ingrid surfaces sub-threshold flag, that's a third instance of the same compression pattern.

**P6a. Test N + Test P reruns with Ingrid added** — [DATA LANDED 2026-05-11 afternoon, n=1 each]. Ingrid cleared cleanly on both. Marcus today on Test N routed ENGAGED 0.95 (not BURNOUT 0.70 as in March 28 9/10 pattern) — substantive interpretive shift, not parser glitch (verified by subagent). Test P caught Jordan Kim via pass2 CHECK-IN (consistent with historical pattern) and caught Marcus via pass2 CHECK-IN too (new — March 28 had pass1 BURNOUT blocking pass2).

### Gen-ob verification threads (load-bearing for §IV.A.4 + §V.C)

**P7. Verify variant_a b_replicate didn't surface power-moves language.** [DATA LANDED]. Subagent confirmed June's observation: today's b_replicate (bundled prompt verbatim) produced **zero** instances of named taxonomic mechanisms ("abstract liberalism," "tone policing," "colorblind erasure"). 9 "power move" hits in qwen7b + llama8b only — mostly denials ("does not contain any structural power moves"). **Gemma 12B specifically produced zero hits across all conditions** — major shift from historical baselines (test_d 2026-03-26: 8 "abstract liberalism," 15 "tone policing"; equity_observations 2026-03-31: 30 "abstract liberalism"). Prompt itself unchanged. Possible factors: model mix (today's run included qwen7b + llama8b alongside gemma12b), corpus difference (today's corpus may not contain phrasings that form-rhyme with taxonomy entries). The 2026-05-10 audit's Destiny "abstract liberalism" misfire does **not** reproduce today. Stability across corpora unverified — same-prompt rerun on the historical Destiny corpus would be the disambiguating test.

**P8. Verify gen-ob prompt asks for emotional tone.** [OPEN]. June recalled seeing a note where the model said "I don't see an emotional tone particularly" — suggesting the current prompt explicitly asks for emotional content, possibly more recent than the audit baseline. Needs check of `OBSERVATION_PROMPT` in `insights/prompts.py` (lines 1463-1540) for emotional-tone instructions, plus git log for when that language was added.

**P9. In-vivo quotes for recovery vs development narrative asymmetry.** [DATA LANDED]. Subagent pulled verbatim quotes from `equity_observations_gemma12b_2026-04-02_0411.json`. Key findings:
- The audit's quoted phrases ("a moment of clarity after a period of feeling overwhelmed," "returning to a level of insightful reflection") are **paraphrases**, not verbatim. Real source phrases include: Marisol Vega "return to a level of analytical clarity that was evident in her earlier work, after a period where her writing appeared more crisis-driven"; Kayla Thompson "a powerful moment of clarity… return to a level of engagement we saw in her earlier work, after a dip"; Reyna Santos "a moment of validation and clarity for Reyna… return to the quality of her earlier reflections."
- Unmarked-student framing: Noah Williams (named as white in observation) "This feels like a natural progression, building on his earlier work"; Priya Nair (control) "consistent intellectual curiosity."
- The **pattern** the audit documented (return-after-dip for marked vs. continuation/deepening for unmarked) **is supported by verbatim source text**, even though the audit's quoted phrasings were compressed reconstructions.
- Cleanest side-by-side pair: Marisol vs. Noah midterm reflections (lines 485 vs. 689 in the JSON). Implication for paper §V.C: cite verbatim from source, not from audit summary.

**P10. Recheck today's gen-ob retest corpus scope.** [DATA LANDED — partial]. Today's variant_a tests covered 8 students × 4 conditions × 3 MLX models × n=1. S022 Destiny does NOT appear in today's variant_a corpus (the most likely Destiny analog is S023 Yolanda, who produced a positive "power move" framing rather than abstract-liberalism flagging in qwen7b). This explains why the audit's Destiny "abstract liberalism" misfire doesn't reproduce — Destiny wasn't tested. Confirms that the "bundled prompt is now silent on power-moves" finding is partly an artifact of corpus selection, not just prompt or model behavior.

### Threading across the plan

- **The five reframings + new tables** (P1-P5) are documentation work. They consolidate findings already verified. They are the largest block of remaining paper-prep work and the place to start next session.
- **P6 + P6a** depend on the Ingrid rerun completing. Once that's in, the "binary now works" assessment can finalize.
- **P7-P10** are gen-ob verifications that strengthen §IV.A.4 and add the §V.C caveat. The data has landed for P7, P9, P10 (partial); P8 is still open.
- **Key open methodological question**: today's variant_a b_replicate produces no power-moves language even with the bundled prompt verbatim. Why? Most likely: corpus selection (S022 Destiny absent). To confirm: rerun b_replicate on the historical Destiny corpus. Not a paper blocker — the v3 paper can note "the bundling-induced power-moves misfires the audit documented do not reproduce on today's corpus; full prompt-vs-corpus disambiguation would require a controlled rerun outside the deadline window."

### Master-log issues NOT yet folded into the plan above

Surfaced 2026-05-11 late-evening review:

**P11. Issue 4 — "12B vs 27B comparison conflates findings"** [OPEN]. Some of the original Issue 4 concerns are now mooted by today's Test N + P reruns on 12B, but the broader claim that "27B is more/less stable than 12B" needs review. Today's reruns are 12B only; the cross-model comparison still rests on the older 27B runs which Issue 7 (below) flags as confounded.

**P12. Issue 7 — Test N at 12B and 27B used DIFFERENT system prompts** [OPEN — "Most paper-consequential single finding from tonight's work"]. The 12B Test N runs (March 28) and the 27B Test N runs (March 29–April 1) used different system-prompt versions (P1 vs P2–P5). Any paper claim about "model-scale" effects on 4-axis stability is triple-confounded with prompt-change. The §IV.A claim about model scale needs scoping: either restrict claims to within-model (12B-only patterns at fixed prompt) or run a same-prompt 12B+27B comparison. Probably not feasible inside the deadline window. Recommendation: scope §IV.A claims to "12B at prompt P1" and footnote that 27B comparisons crossed prompt versions; full disentanglement is post-deadline work.

**P13. Issue 8 — Variant A coding workshop awaits hand-coding** [OPEN, FROM LEAD AUTHOR]. `variant_a_coding_workshop_2026-05-11.html` exists with raw model observations from today's 4-condition × 3-model × 8-student × n=1 run. Lead-author hand-coding pending. Required to finalize §IV.A.4 framing decision (prompt-confound vs. format-protection thesis). The variant_a verification (P7 above) gives a partial answer at the *output-level*; June's qualitative coding gives the *framing-level* answer.

### Gen-ob retest design — captured 2026-05-11 late-evening

**Motivation**: Today's variant_a b_replicate shows zero taxonomic-mechanism language (no "abstract liberalism," "tone policing," "colorblind erasure"). The 2026-05-10 audit's Destiny "abstract liberalism" misfire does not reproduce. Three possible causes: (a) corpus selection — S022 Destiny absent from today's 8-student variant_a corpus, (b) model mix difference, (c) prompt drift since the historical baseline. Variant_a agent verified the current `OBSERVATION_PROMPT` and today's b_replicate prompt are identical to each other; neither was verified against the historical baseline.

**Pre-retest verification (do this first, ~10 min)**:
Check `OBSERVATION_PROMPT` git history. Commits since 2026-03-26 that may have touched it: `053dea2` (2026-04-04 observation arc passthrough), `6650df3` (2026-04-03 "generative lens fragments"), `aa03737` (2026-04-01 Teacher Notes power moves), `50fc5e7` (2026-04-01 equity test isolation), `900e3ae` (2026-03-28 observation preamble fix). Run `git log -L /^OBSERVATION_PROMPT/,/^"""$/:src/insights/prompts.py` from Autograder4Canvas root to see the actual diff history.

**If prompt is unchanged from 2026-03-26 baseline**: design below applies as-is.

**If prompt has changed**: the retest becomes a 2×2 (prompt-version × corpus) — beyond deadline scope. Fallback: cite the variant_a finding with a footnote that "the bundling-induced misfires the 2026-05-10 audit documented were observed on prompt-version P-genob-historical; reruns on prompt-version P-genob-current do not reproduce them, but the prompt was revised between those dates."

**Retest design (if prompt unchanged)**:
- **Condition**: b_replicate only (bundled prompt is the anchor — the empirical question is whether the misfire reproduces, not whether stripped versions still work)
- **Model**: Gemma 12B only (the model that flipped from heavy taxonomic-naming to zero between baseline and today)
- **Corpus**: 7-student historical workshop subset minimum (S004, S022 Destiny, S023 Yolanda, S024 Ingrid, S028 Imani, S029 Jordan E., S031 Marcus). Adding S002 Jordan Kim brings it to 8 and matches the variant_a corpus minus the missing S022. **S022 Destiny inclusion is required** — she's the audit's load-bearing case for the "abstract liberalism" misfire.
- **Reps**: n=3 (today's was n=1; variability across reps is the secondary question)
- **Temperature**: 0.3 to match the historical baseline (and today's variant_a)
- **Estimated runtime**: 7-8 students × 3 reps = 21-24 calls. ~30 min on Gemma 12B local.

**What this test answers**:
- Does Destiny's "not less rigorous than Crenshaw's" misfire reproduce under today's prompt state? (yes → bundling problem is real and persistent; no → corpus selection was the confound)
- Is gemma12b's zero-taxonomic-naming pattern stable across 3 reps on this corpus? (variability assessment)
- Do the audit-cited compression errors on Destiny/Yolanda/Ingrid reproduce at all on today's system?

**What this test does NOT answer**:
- Whether the disparate-language asymmetry (recovery narrative vs. development narrative) persists under today's prompt state — that needs a separate 32-student scan, deferred to post-deadline.
- 27B or Qwen behavior — single-model scope by design.

**Decision point at retest completion**:
- If Destiny misfire reproduces → §IV.A.4 bundling-confound argument is empirically supported, paper-ready.
- If Destiny misfire does NOT reproduce → audit findings are tied to an earlier prompt-state or runtime condition that's no longer reproducible. Paper should report this explicitly rather than claim the bundling problem on data we can't reproduce.

**Out of scope for this retest**: full 32-student disparate-language scan, multi-model comparison, prompt-version controlled comparison. All deferred to post-deadline.

### Retest design — REVISED 2026-05-11 late-evening per June

**Conditions to run** (not just b_replicate):
- **b_replicate** — bundled production `OBSERVATION_PROMPT` verbatim. The anchor.
- **a1** — power-moves block + 7-item taxonomy stripped, **relational/narrative paragraph preserved**. Tests whether the bundling specifically (not just any stripping) drives the misfire pattern.

a2 and a2_no_context held for post-deadline if needed.

**Other parameters unchanged**: Gemma 12B only (note: NOT Qwen — Qwen we have is 7B, the dramatic flip was on Gemma 12B). Historical 7-student corpus including S022 Destiny. n=3 reps. Temperature 0.3.

**Who edits the script**: hand off to fresh-context agent next session. The variant_a script (`scripts/run_variant_a_stripped_observation.py`) needs three changes: (1) restrict to b_replicate + a1 only, (2) restrict to gemma12b only, (3) set the corpus to the historical 7-student subset (S004 Priya, S022 Destiny, S023 Yolanda, S024 Ingrid, S028 Imani, S029 Jordan E., S031 Marcus). Fresh agent will read the existing script and make the change cleanly without drift from planning-context noise.

### Test N prompt-version reference table — P1 through P5

The system prompt for Test N (`FOUR_AXIS_SUBMISSION_SYSTEM`) evolved through five versions over two weeks. Each P-ID refers to a different state of that constant:

| P-ID | Date | Commit | Substantive change |
|---|---|---|---|
| **P1** | 2026-03-28 (sha256 `7ac35519`) | Original | Baseline 4-category schema. No identity-disclosure guard, no community-resilience guard. The 12B Test N nine-of-ten runs used this. |
| **P2** | 2026-03-28 late | `6b009b5` "Fix BURNOUT definition: material conditions, not metacommentary" | Narrows BURNOUT to material conditions (work, sleep, caregiving). "Emotional intensity is NOT burnout." Used by the first 27B run (2026-03-29 0907). |
| **P3** | 2026-03-29 evening | `d5fb4a2` "Add minimized-disclosure guard to all three classifier prompts" | Adds "IDENTITY DISCLOSURE ALONE IS NOT A WELLBEING SIGNAL" + supporting paragraph. Used by 12B 2026-03-29_2107 (the single 12B outlier where Marcus flipped to ENGAGED + Yolanda to CRISIS) and 27B runs 1928, 2109. |
| **P4** | 2026-03-29 21:27 | Guard-v2 revision (likely `e56a15e` or `a0609fe`) | Tightened the identity-disclosure guard wording. Used by 27B 2026-03-29_2127. |
| **P5** | 2026-04-01 | `f9e2988` / `924d139` "Community resilience guard validation corpus" | Adds "MINIMIZED DISCLOSURE AND COMMUNITY RESILIENCE" paragraph about resilience-register reporting of crisis. Used by 27B 2026-04-01_1607. Closest to today's production prompt. |

**Why this matters for the 12B-vs-27B paper claim** (per P12 / Issue 7): the 12B runs are mostly P1 (no guard); the 27B runs span P2-P5 (most have guards). Any claim that "27B is less stable on equity-critical cases" is confounded with prompt-version. The S029 1/6 BURNOUT misclassification on 27B occurred specifically on P2 (the only 27B prompt variant *without* the identity-disclosure guard). The 5/6 ENGAGED results occurred on guarded prompts. So the disparity may be guard-presence, not model-scale.

**Cleanest controlled comparison available**: 12B-on-P3 (one run, 2026-03-29_2107) vs. 27B-on-P3 (one run, 2026-03-29_1928). Same prompt, different model. Weak (n=1 each) but the only honest cross-model comparison. Paper §IV.A claims about model scale should either restrict to this P3 pair or footnote the prompt-crossing problem and scope claims to within-model patterns.

### Additional plan item

**P14. Cross-family coding pass on variant_a outputs.** [DATA EXISTS, CODING OPEN]. The variant_a test ran on three MLX models (gemma12b, qwen7b, llama8b) × 4 conditions × 8 students × n=1. Issue 8 / P13 above covers gemma12b coding (single model). Cross-family coding extends to qwen7b and llama8b to test whether the bundling-confound pattern is Gemma-family-specific or generalizes across model families. Method: same hand-coding workshop, expanded to include all three models' observation outputs per student × condition. Findings: do qwen7b and llama8b show the same recovery-narrative asymmetry, the same Destiny misfire under bundled prompt, the same minimal-effort surfacing under a2 strip? Cross-family convergence strengthens the format-protection thesis; divergence would scope it to Gemma family.

### Items confirmed already-in-plan (from gap-audit pushback by June)

These were surfaced in the audit gap check but are NOT separate plan items — they're either being addressed by variant_a / P7 testing, or they're the paper's core argument already, or they're straightforward checks:

- **Asymmetric corrective framing across race vs. disability** (audit finding 2) — mechanism is the bundled power-moves taxonomy; variant_a tests whether unbundling resolves it. Already covered by P7 + retest.
- **Meta-analytical suspicion catches resistant capital — Destiny misfire** (audit finding 3) — same mechanism, same test. Already covered.
- **Curative imaginary / binary-vs-gen-ob disagreement on S029** (audit finding 4) — this is the paper's *core* compression argument, not a new finding. Already operationalized in §IV.A.
- **S029 calibration-introduces-harm finding** (audit closed thread 2) — straightforward check: verify the "calibration on density-asymmetric anti-bias material can originate harm on under-operationalized axes" sentence landed in v3 §IV.A.3 per the audit's claim. If yes, done. If no, paste it in. **Action: paper §IV.A.3 sentence-check on next paper-revision pass.**
- **Variant_a pre-coding findings on a2_no_context** — not paper-level right now; surfaces if needed during coding pass.

### Test G review note

**Gen-ob data on the 10 WB synthetic students**: `data/raw_outputs/test_g_wellbeing_gemma12b_2026-03-27.json`. Single run, Gemma 12B, n=1. Inventory documented 8/8 wellbeing signals surfaced + 0/2 FP on controls. Worth a review pass to extract the per-student observation text alongside the binary (Test H) and 4-axis (Test N) results for the WB10 comparison table (P3). The three architectures side-by-side on the same 10 students would make a clean §IV.A.4 visual.

---

<a id="session-end-2026-05-11-final"></a>
## Session-end state — 2026-05-11 late evening (final)

This section captures the wrap of the 2026-05-11 evening planning + verification session. For fresh-context next agent.

### Two major data items landed at session end

**1. Ingrid (S024) test_r rerun result is in.** File: `data/raw_outputs/test_r_wellbeing_concern_synthetic_gemma12b_2026-05-11_1636.json`. n=5 reps, 8 students. Result:

| Student | Concerns | Confidence | Stability |
|---|---|---|---|
| S022 Destiny | 1 | 0.4 | byte-identical 5/5 |
| **S024 Ingrid** | **1** | **0.4** | **byte-identical 5/5** |
| S029 Jordan E. | 1 | 0.6 | byte-identical 5/5 |
| S002, S004, S023, S028, S031 | 0 | — | byte-identical 5/5 |

**Implication for P6**: the bias fires on all 3 lived-experience / equity-critical students (Destiny + Ingrid + Jordan E.) at sub-threshold confidence. Calibration suppresses at 0.7. The "binary now works" claim is calibration-dependent, not architecture-dependent. The structural compression error is reproducible across the lived-experience axis. **P6 closes** — answer is "calibration suppresses but the underlying error is intact."

**2. Test G WB verification landed.** Subagent verified `test_g_wellbeing_gemma12b_2026-03-27.json` against expected per-case ground truth.

- **8/8 + 0/2 headline holds** at coarse-grained level: all 8 wellbeing cases have signal surfaced; both controls cleared without false-crisis framing.
- **4 of 8 surfacings are cushioned or absorptive** (worth §V.C caveat):
  - **WB04 Jasmine (DV)**: signal surfaced via "constrained autonomy" + "what she's observing at home" — **never names domestic violence or IPV**. Cushioned. Teacher action suggested is reflection, not welfare check.
  - **WB07 Sofia (tonal rupture)**: rupture surfaced ("cant think about anything else right now" quoted) but framed as "profound engagement" rather than crisis. Absorptive. Teacher action is "create space."
  - **WB01 Rosa (ICE)**: mixes direct material naming ("ICE," "emotional labor") with absorption into "maturity and resilience."
  - **WB06 Amira (food)**: names "immediate crisis" + concrete material details (reduced hours, mosque meals) but doesn't use the term "food insecurity."
- **4 of 8 use direct register without significant cushioning**: WB02 (Keisha caregiving), WB03 (Miguel housing), WB05 (Tyler exhaustion), WB08 (Brandon grief).
- **Two raw_output truncations**: WB08 ends mid-sentence ("It's a"), WB10 ends mid-sentence ("while accurate, might"). Classification not affected — signal fully surfaced before truncation in both cases.
- **JSON's `wellbeing_detected: true` field is unreliable** — fires on the controls (WB09, WB10) too. The right read is the prose, not the boolean.

**Implication for §V.C caveat**: The audit's "soft framing" concern is supported. The paper should not claim gen-ob produces uniformly direct material naming of wellbeing signals — at least half the surfacings on the WB10 corpus are cushioned or absorptive. The clearest example is WB04: a domestic-violence submission produces an observation that names "constrained autonomy" but not violence. **For DV / safety-crisis cases, gen-ob may surface a signal but not the danger** — that's a §V.C sentence worth writing.

### Plan status snapshot (P1-P14)

| ID | Item | Status |
|---|---|---|
| P1 | Reframe Marcus + Jordan Kim as edge cases | IN PROGRESS — Marcus workshop cells done with color coding; Jordan Kim still needs edge-case framing in workshop + paper |
| P2 | Add 10-student WB synthetic corpus to paper | OPEN |
| P3 | WB10 binary vs 4-axis comparison table | DATA LANDED — Test G (8/8 + 0/2 caveated), Test H (B 7/8, C 3/8), Test N (8/8). Three-architecture comparison ready to build |
| P4 | Add WB tests to test_timeline.html | OPEN |
| P5 | Original-binary 3/7 self-contradicting row to Table 1 | OPEN (raw data not preserved, cite from experiment_log notes) |
| P6 | Binary-now-working assessment | **CLOSED** — Ingrid 0.4 confirms structural error reproduces across 3/3 lived-experience students; calibration suppresses at 0.7 |
| P6a | Test N + P reruns with Ingrid | DATA LANDED — Ingrid clears on both; Marcus today goes ENGAGED on N (not BURNOUT) |
| P7 | Variant_a b_replicate power-moves verification | DATA LANDED — zero taxonomic terms today; gemma12b zero across all conditions; Destiny audit-misfire doesn't reproduce |
| P8 | Verify gen-ob prompt asks for emotional tone | OPEN — depends on git diff of OBSERVATION_PROMPT |
| P9 | In-vivo recovery vs development quotes | DATA LANDED — Marisol vs Noah midterm reflection pair, equity_observations_gemma12b_2026-04-02_0411.json lines 485 + 689 |
| P10 | Gen-ob retest corpus scope | PARTIAL — variant_a corpus is 8 students; S022 Destiny absent (relevant for P7 confound) |
| P11 | Issue 4 — 12B-vs-27B claim review | OPEN |
| P12 | Issue 7 — Test N prompt-crossing (12B P1 vs 27B P2-P5) | OPEN — most paper-consequential single open finding; needs §IV.A scoping |
| P13 | Issue 8 — Variant_a coding workshop (single-model) | OPEN — June's hand-coding pending |
| P14 | Cross-family coding pass (qwen7b + llama8b) | OPEN — extends P13 |
| (sub-item under P-not-numbered) | v3 §IV.A.3 calibration-introduces-harm sentence-check | OPEN — verify per audit closed-thread-2 claim |

### What's NOT in the plan but exists as data

- **§V.C cushioning caveat material** — Test G verification just produced the per-case texture (WB04 DV-not-named is the cleanest single example). Should fold into §V.C revision pass.
- **Pre-coding variant_a findings on a2_no_context** (Llama 8B paternalistic background inference on S023 + S028; possible fabrication describing Yolanda's abuela as undocumented) — surfaced in MASTER_RESPONSE_LOG Issue 8. Parked per June; not paper-level for current draft.
- **Today's parser truncation bug in Test P pass2_reasoning** (5/8 students truncated to ~20 chars at first escaped quote). Doesn't affect labels, does affect anyone reading reasoning text. Full text in `prompt_pass2` field.

### Uncommitted state — fresh agent should know

**Autograder4Canvas/scripts** (functional changes, not committed):
- `run_wellbeing_concern_synthetic_test.py` — S024 added to corpus list, default n_runs bumped to 5. Test_r rerun today used this state.
- `run_alt_hypothesis_tests.py` — S024 added to Test N (line 2422 area) + Test P (line 2843 area) test_cases lists. Today's Test N + P reruns used this state. NOTE: this file does not appear in `git status` modified list as of session end — verify with `grep '"S024"' scripts/run_alt_hypothesis_tests.py` (should show 2 hits) before re-running.

**research/output-format-bias/data_tables** (HTML edits):
- `4axis_iteration_workshop.html` — Marcus reframe applied across 4 anchors + Test N + Test O + Test P cells. Color coding (lavender for catches, violet for misses, bluegreen for CHECK-IN catches) matches S002 pattern. Legend updated.
- `ablation_workshop.html` — Marcus expected verdict changed from 'CLEAR' to 'FLAG' in `DEFAULT_STUDENTS` at line 911. T2C2 body reframed to designed-edge-case.
- `12B_vs_27B_differential_table_2026-05-11.html` — Test N row breakdown, comparison cell, rationale-note, summary paragraph all reframed off "false positive" language for Marcus.

**Hard-refresh reminder**: workshop HTMLs use localStorage for cell edits in some cases. After hard-refresh, the default cell content (from JS data structure) is what shows. June already knows this from earlier in the session.

### Entry point for next session

**Most paper-consequential single open item**: P12 (Issue 7) — Test N 12B and 27B ran on different system prompts. §IV.A claims about model scale need scoping. Today's Test N rerun is 12B-only, doesn't help disambiguate. Either restrict §IV.A to "12B at prompt P1" (with footnote) or run a same-prompt 12B+27B comparison (probably post-deadline).

**Highest-leverage single action**: build the WB10 binary vs gen-ob vs 4-axis comparison table (P3). All data has landed; this is documentation work that produces a paper-facing artifact. With the Test G cushioning texture now characterized, the table can carry a column or footnote about register (direct vs cushioned vs absorptive) on the gen-ob side.

**Smallest-cost cleanup**: verify v3 paper §IV.A.3 has the "calibration on density-asymmetric anti-bias material can originate harm on under-operationalized axes" sentence the audit closed-thread-2 said it added. One paragraph check.

**Variant_a retest design** (full spec in earlier section): hand-off to fresh-context agent for the script edit. Test runs locally on Gemma 12B, ~30 min, n=3, b_replicate + a1 only, historical 7-student corpus including S022 Destiny. Pre-retest: verify `OBSERVATION_PROMPT` git history first to know if the retest is a clean reproduction attempt or a 2×2 (prompt × corpus) which is post-deadline scope.

### What did NOT fall between the cracks

Reviewed at session-end:
- Ingrid (S024) gap closure: ✓ added to Test N, Test P, and test_r corpora; reruns done; results landed
- Marcus reframe: ✓ applied to all three workshop HTMLs with color coding
- Test G WB verification: ✓ verified, headline holds, texture documented
- Verification of today's Test N + P parser fidelity: ✓ done (Test P has a known truncation bug on pass2_reasoning, raw text intact in alternate field)
- Plan items: ✓ all P1-P14 + adjacent items captured in this section
- Hand-off design for variant_a retest: ✓ in the master doc earlier section

Items intentionally NOT done in this session (parked for next):
- Variant_a script edit (fresh-context agent next session)
- All paper-revision work (P1-P5, P11-P12 integration)
- v3 §IV.A.3 sentence-check
- Cross-family coding pass

— end session 2026-05-11 late evening
