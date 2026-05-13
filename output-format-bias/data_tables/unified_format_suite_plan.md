# Unified Format-Comparison Test Suite — Plan

**Goal**: Build a non-production test suite that runs three output formats (binary, 4-axis, generative observation) on the same 46-student corpus, with the same classification-oriented prompt scaffolding held constant in all six new variants. The only deliberate variation is (a) the output-format tail and (b) whether the "default to not flag when ambiguous" paragraph is included or stripped. This measures what changes in the model's output when the same scaffolding is given different format instructions and different ambiguity-handling instructions.

## Glossary (for the implementing agent and any cross-camp reader)

- **ES corpus** — the 32 ethnic-studies student submissions (`student_id` starts with `S`)
- **WB cases** — the 14 wellbeing-signal cases seeded into the corpus (`student_id` starts with `WB`)
- **Substrate** — the body of the system prompt: equity guards, category definitions, worked examples, identity-disclosure rule, CRISIS-supersedes guard. Everything except the final output-format instruction. We hold this constant across the six new variants.
- **Tail** — the final JSON-schema instruction at the bottom of the system prompt that tells the model what to emit. The only deliberate variation in the suite.
- **Equity floor** — a set of instructions inside the substrate designed to prevent disproportionate surveillance of marginalized students (e.g., "passionate engagement is engagement, not distress"). Load-bearing in the production system; identified today as the source of "parroting" on disclosure cases when combined with the tiebreaker.
- **Tiebreaker** — a single paragraph in the substrate ("DEFAULT TO NOT FLAGGING WHEN AMBIGUOUS"). Named for its function in categorical formats (resolves BURNOUT/ENGAGED ambiguity). In genob there is no tie to break, but the paragraph's protective rhetoric may still shape the prose; that's the suspected mechanism behind today's "this isn't distress" parroting finding on WB04/WB07/WB01/WB08.
- **Format effect** — what changes in the model's output when the same scaffolding is given a different output-schema instruction.
- **Prompting effect** — what changes in the model's output when the scaffolding content itself changes (different rules, different examples). NOT what this suite tests directly; the May 12 a2 vs a2_no_context run already tested one slice of this and stays as a separate paper row.

**Scope discipline**: Extend the existing `run_4axis_full_corpus_test.py` (which already does 80% of this). DO NOT rewrite from scratch. DO NOT touch production prompts.py. The two changes from the existing script are (a) add three new variant entries to `VARIANT_CHOICES` and (b) add the post-processing layer (the existing script doesn't apply it; we need raw + post-processed both recorded).

---

## Conceptual grounding

**Generative observation** is the act of *looking and seeing what is there*. The model is asked to describe what it observes — not to classify, not to flag. The output is prose. Its analytic value comes from a downstream reader (human or another agent) coding the prose afterward. The comparison this suite makes is between three ways the same model can be asked to report on the same content:

- **Binary**: emit one of two verdicts (`CONCERN`/`CLEAR`)
- **4-axis**: emit one of four labels (`CRISIS`/`BURNOUT`/`ENGAGED`/`NONE`)
- **Genob**: emit prose describing the student's wellbeing

**How to describe what this measures (matters for the paper's methods section)**: hold the classification-oriented substrate (its equity guards, four-axis category definitions, worked examples, identity-disclosure rule, CRISIS-supersedes guard) identical across the six new variants; let only the output-format tail and the tiebreaker paragraph's presence differ. This is NOT a clean "format effect in vacuum" test — the substrate is a classification apparatus, so attaching a genob tail to it is structurally asking the model to perform classification preparation then describe rather than classify. That mismatch IS the experiment. The paper's honest framing is: "what happens to the same classification scaffolding when the output instruction is varied?" That framing closes the main reviewer attack surface (vs. claiming format effect was isolated from prompting effect).

**Important methodological flag**: Production "binary" emits 4-axis labels and collapses them downstream to `CONCERN`/`CLEAR`. The unified binary in this suite is a **true binary at the model layer** — the model emits `CONCERN`/`CLEAR` directly. The substrate still contains the four-axis category definitions. The model performs an internal mapping from "this fits CRISIS" → emit `CONCERN`. This is one of the things the suite measures: does that internal mapping introduce error the 4-axis format doesn't have?

**The genob-tb vs genob-notb pair is the most informative single comparison** because it tests one specific mechanism: whether the tiebreaker paragraph's protective rhetoric leaks into descriptive prose when the model has no categorical decision to route. Today's "this isn't distress" parroting on WB04/WB07/WB01/WB08 is the suspected effect. If parroting disappears in genob-notb but persists in genob-tb, the tiebreaker paragraph is the cause. If both produce parroting, the format-substrate mismatch drives it. If genob-notb starts producing false positives on S004 Priya / S024 Ingrid, the tiebreaker is doing protective work that genob loses without it. All three outcomes are publishable.

**What this suite does NOT test**: priming-content effects (what happens to genob with a different substrate). The May 12 a2 vs a2_no_context run already tests one slice of this — class-context-present vs class-context-absent in the production OBSERVATION_SYSTEM_PROMPT — and stays as a separate paper row.

---

## Existing infrastructure — reuse verbatim, do not rewrite

The canonical runner is `/Users/june/Documents/GitHub/Autograder4Canvas/scripts/run_4axis_full_corpus_test.py`. It already implements:

- Backend wiring (`BackendConfig`, `send_text`, MLX warmup, `unload_mlx_model`) — preserve.
- Corpus loading: 32 ES students from `data/demo_corpus/ethnic_studies.json` + 14 WB cases imported from `run_alt_hypothesis_tests.WELLBEING_SIGNAL_CASES`. Preserve.
- CLI flags: `--variant`, `--smoke`, `--model`, `--n-runs` — preserve, extend `VARIANT_CHOICES`.
- Run loop: `for run in 1..N: for student in corpus: run_one(...)` — preserve.
- `save_results()` JSON wrapper (metadata + results list) — preserve.
- Output filename convention `test_{variant}_FULL_CORPUS_{model}_{date}_{time}{_SMOKE}.json` — preserve.
- Output directory: `output-format-bias/data/raw_outputs/`. Preserve.
- Provenance capture (git commit, branch, dirty state). Preserve.
- Variant-dispatch pattern in `run_variant()` (lines 1006–1019). Extend it.

**Existing variants (six)** — keep unchanged:
- `single-pass`: 4-axis, `FOUR_AXIS_SUBMISSION_SYSTEM` (from `run_alt_hypothesis_tests.py`)
- `two-pass`: 4-axis, `WELLBEING_CLASSIFIER_SYSTEM` + prescan
- `reasoning`: 4-axis, `FOUR_AXIS_REASONING_SYSTEM` (inline at line 141)
- `reasoning-two-pass`: 4-axis reasoning + prescan
- `binary-reasoning`: binary derived from `WELLBEING_CLASSIFIER_SYSTEM` (line 210)
- `binary-no-tiebreaker`: binary, `WELLBEING_CLASSIFIER_SYSTEM` minus the tiebreaker paragraph (line 230)

**The tiebreaker is a paragraph, not a pass.** It lives in `WELLBEING_CLASSIFIER_SYSTEM` lines 1784–1791 of `Autograder4Canvas/src/insights/prompts.py`:

> "DEFAULT TO NOT FLAGGING WHEN AMBIGUOUS. When uncertain between BURNOUT and ENGAGED, default to ENGAGED. False positives — flagging students who are doing the assignment as if they were in crisis — produce real harm: surveillance of marginalized students, paternalistic outreach, and erosion of trust. False negatives at the BURNOUT level are addressed by the teacher's own attention. (This default-to-not-flag rule does NOT apply to CRISIS — for CRISIS-level material conditions, a single sentence is sufficient.)"

The `binary-no-tiebreaker` variant strips it via `_TIEBREAKER_START = "DEFAULT TO NOT FLAGGING WHEN AMBIGUOUS"` + slice-based removal. We use the **same string-slice technique** for the new 4-axis-no-tb and genob-no-tb variants — no new mechanism.

---

## What needs to be added — three new variants

The existing script lacks (a) 4-axis with-and-without-tiebreaker comparison (the 4-axis variants currently use `FOUR_AXIS_SUBMISSION_SYSTEM` / `FOUR_AXIS_REASONING_SYSTEM`, which are different substrates from `WELLBEING_CLASSIFIER_SYSTEM`), and (b) gen-ob variants entirely. To make all three formats minimally variant, **all six target variants share a single substrate (`WELLBEING_CLASSIFIER_SYSTEM`)** and differ only in (i) whether the tiebreaker paragraph is included and (ii) the output-schema tail.

New variants to add:

| Variant key | Substrate | Tiebreaker | Output schema tail |
|---|---|---|---|
| `unified-binary-tb` | `WELLBEING_CLASSIFIER_SYSTEM` (with reasoning schema replaced) | yes | `{reasoning, verdict: "CONCERN"\|"CLEAR", confidence}` |
| `unified-binary-notb` | same minus tiebreaker paragraph | no | same |
| `unified-4axis-tb` | `WELLBEING_CLASSIFIER_SYSTEM` (with reasoning schema replaced) | yes | `{reasoning, axis: "CRISIS"\|"BURNOUT"\|"ENGAGED"\|"NONE", confidence}` |
| `unified-4axis-notb` | same minus tiebreaker paragraph | no | same |
| `unified-genob-tb` | `WELLBEING_CLASSIFIER_SYSTEM` (with observation schema appended) | yes | `{reasoning, observation: 3-4 sentence prose, confidence}` |
| `unified-genob-notb` | same minus tiebreaker paragraph | no | same |

**All six use a single shared user prompt** — `WELLBEING_CLASSIFIER_PROMPT` (already imported, line 1832 of `insights/prompts.py`), with `signal_prefix=""` (no prescan in any of the unified variants — prescan is its own intervention and not part of the format axis).

This is six runs × 46 students × n=5 reps = 1,380 LLM calls. At ~3-5s per Gemma 12B call on MLX that's roughly 1-2 hours of compute. Tractable.

---

## The single source of truth for substrate construction

Add four module-level constants near the existing `BINARY_NO_TIEBREAKER_SYSTEM` block (line 230). The construction pattern follows the existing `.replace()` + slicing technique exactly:

```python
# Unified suite — all six variants share WELLBEING_CLASSIFIER_SYSTEM as substrate.
# Only differences: (a) tiebreaker paragraph in or out, (b) output schema tail.

# Reuse the existing constant defined at line ~203 of the script — do NOT
# re-declare a new constant with a different name. The existing script uses
# the name `_BINARY_OLD_SCHEMA`, not `_OLD_BINARY_SCHEMA`. Reference it as-is:
#
#   _BINARY_OLD_SCHEMA = (
#       'Respond with JSON only: {"axis": "CRISIS"|"BURNOUT"|"ENGAGED"|"NONE", '
#       '"signal": "brief description", "confidence": 0.0-1.0}'
#   )
#
# The .replace() calls below should use _BINARY_OLD_SCHEMA (verbatim, the
# existing name) — not _OLD_BINARY_SCHEMA. This is the silent-bug trap
# the critic-swarm flagged.

# Binary tail
_UNIFIED_BINARY_TAIL = (
    'Respond with JSON only: {"reasoning": "2-3 sentences working through '
    'the evidence before committing to a verdict", '
    '"verdict": "CONCERN"|"CLEAR", '
    '"signal": "brief description of key signal or lack thereof", '
    '"confidence": 0.0-1.0}'
)

# 4-axis tail (reasoning field, same shape as existing binary-reasoning)
_UNIFIED_4AXIS_TAIL = (
    'Respond with JSON only: {"reasoning": "2-3 sentences working through '
    'the evidence before committing to a classification", '
    '"axis": "CRISIS"|"BURNOUT"|"ENGAGED"|"NONE", '
    '"signal": "brief description of key signal or lack thereof", '
    '"confidence": 0.0-1.0}'
)

# Gen-ob tail — describes what is there, does not classify.
# Wellbeing-narrowed scope so the comparison with binary and 4-axis is apples-to-apples
# (same domain, different output shape). The "colleague, not a system" register is
# carried over from the production OBSERVATION_SYSTEM_PROMPT verbatim because that
# framing is what makes the descriptive form land; we are NOT bringing over the
# multi-dimensional ask (intellectual + emotional + circumstances), the
# structural-power-moves block, or the relational/narrative paragraph — those
# would change scope away from wellbeing.
_UNIFIED_GENOB_TAIL = (
    'Respond with JSON only: {"reasoning": "2-3 sentences of your working '
    'notes — which observations you weighted and why", '
    '"observation": "3-4 sentences describing what you observe about this '
    'student\'s wellbeing. Write as a colleague sharing what you noticed, not '
    'as a system generating a report. If the student\'s own current '
    'circumstances surface in the writing, name them directly. Do not '
    'classify or flag.", '
    '"confidence": 0.0-1.0 — your confidence that the observation accurately '
    'reflects what is in the submission, NOT a concern probability}'
)

UNIFIED_BINARY_TB_SYSTEM   = WELLBEING_CLASSIFIER_SYSTEM.replace(_BINARY_OLD_SCHEMA, _UNIFIED_BINARY_TAIL)
UNIFIED_4AXIS_TB_SYSTEM    = WELLBEING_CLASSIFIER_SYSTEM.replace(_BINARY_OLD_SCHEMA, _UNIFIED_4AXIS_TAIL)
UNIFIED_GENOB_TB_SYSTEM    = WELLBEING_CLASSIFIER_SYSTEM.replace(_BINARY_OLD_SCHEMA, _UNIFIED_GENOB_TAIL)

def _strip_tiebreaker(system: str) -> str:
    idx = system.find(_TIEBREAKER_START)
    assert idx != -1, "tiebreaker paragraph not found"
    end = system.find("\n\n", idx) + 2
    return system[:idx] + system[end:]

UNIFIED_BINARY_NOTB_SYSTEM = _strip_tiebreaker(UNIFIED_BINARY_TB_SYSTEM)
UNIFIED_4AXIS_NOTB_SYSTEM  = _strip_tiebreaker(UNIFIED_4AXIS_TB_SYSTEM)
UNIFIED_GENOB_NOTB_SYSTEM  = _strip_tiebreaker(UNIFIED_GENOB_TB_SYSTEM)
```

This guarantees: every unified variant has identical substrate text (equity floor, identity-disclosure rule, MINIMIZED-DISCLOSURE rule, worked examples a/b/c, CRISIS-supersedes guard), differing ONLY in the JSON schema tail and the tiebreaker-paragraph presence.

---

## Post-processing — record raw outputs only, do NOT apply in-script

The critic-swarm flagged that the production post-processing function (`_check_bias_in_output` in `research.concern_detector`) operates on `ConcernRecord` objects with per-passage confidences and cannot be cleanly imported for use against the unified-suite's single-verdict outputs. Rather than build a new in-script post-processing layer (which would diverge from the existing 4-axis script's pattern and risk producing data the paper's main analysis can't use), **this suite records raw model outputs only**. Downstream analysis applies post-processing uniformly across all variants for cross-format comparison.

For each record, write:
- `raw_output` — the complete JSON text the model emitted
- `reasoning` — extracted from the parsed JSON
- The format-specific decision field (`verdict` for binary, `axis` for 4-axis, `observation` for genob)
- `signal` — extracted from the parsed JSON (where present)
- `confidence` — extracted from the parsed JSON (semantics differ across formats — see below)

**Confidence is recorded but its semantics differ across formats and the data file should mark this**. Binary/4-axis confidence is "the model's confidence in the verdict it just emitted." Genob confidence is "the model's confidence that its observation accurately reflects what's in the submission" — NOT a concern probability. The output JSON wrapper should include a top-level note documenting this divergence so any downstream analyst can't compare confidence cells across formats without seeing the warning.

**No `final_decision` field in this suite's output.** The paper's downstream analysis script will compute `final_decision` consistently across variants by applying whatever post-processing rules the paper standardizes on (likely the 0.7 confidence threshold + a documented regex pattern set). Genob never gets a `final_decision` from the model layer — downstream coders (human + Opus + Gemini) do that work.

---

## Output JSON schema (per record)

Mirror the existing `run_one_reasoning_pass()` record shape (lines 621–643 of the existing script). Per record:

```python
{
    "codepath": "test_harness_unified_suite",
    "classifier_variant": "unified-binary-tb" | ... | "unified-genob-notb",
    "format": "binary" | "4axis" | "genob",
    "tiebreaker": True | False,
    "source": "ethnic_studies" | "wellbeing_synthetic",
    "run": int,
    "student_id": str,
    "student_name": str,
    "pattern": str | None,
    "signal_type": str | None,
    "expected_axis": str | None,
    "submission_text": str,
    "prompt": str,
    "system_prompt": str,
    "raw_output": str,
    "reasoning": str,
    # Exactly ONE of these is populated per record based on format
    "verdict": "CONCERN" | "CLEAR" | None,            # binary only
    "axis":    "CRISIS"|"BURNOUT"|"ENGAGED"|"NONE" | None,  # 4-axis only
    "observation": str | None,                         # genob only
    "signal": str | None,                              # populated where present; None for genob
    "confidence": float,                               # semantics differ across formats — see post-processing section
    "time_seconds": float,
    "error": str | None,
}
```

The top-level JSON wrapper (the file's metadata block — see `save_results()` lines 449–471 in the existing script) should include a new key:

```python
"confidence_semantics": {
    "binary":  "model's confidence in the verdict (CONCERN|CLEAR)",
    "4axis":   "model's confidence in the axis (CRISIS|BURNOUT|ENGAGED|NONE)",
    "genob":   "model's confidence that the observation accurately reflects the submission — NOT a concern probability"
}
```

This documents the divergence so downstream analysts can't accidentally cross-compare.

Three new `run_one_unified_*()` functions parameterized by `tiebreaker: bool`:
- `run_one_unified_binary(backend, sid, sname, sub, *, run_idx, source, pattern, signal_type, expected_axis, tiebreaker)`
- `run_one_unified_4axis(backend, sid, sname, sub, *, run_idx, source, pattern, signal_type, expected_axis, tiebreaker)`
- `run_one_unified_genob(backend, sid, sname, sub, *, run_idx, source, pattern, signal_type, expected_axis, tiebreaker)`

Positional parameters match the existing `run_one_reasoning_pass()` signature exactly (lines 562–569 of the script). Keyword-only `tiebreaker` is the only addition. The dispatch in `run_variant()` uses `functools.partial(run_one_unified_binary, tiebreaker=True)` etc. — the partial binds the keyword arg, and the script's existing call site supplies the positionals.

---

## Concrete file edits

Single file: `/Users/june/Documents/GitHub/Autograder4Canvas/scripts/run_4axis_full_corpus_test.py`.

1. **~line 232** — after `BINARY_NO_TIEBREAKER_SYSTEM`: add the unified-substrate constants block above (the four schema tails + six SYSTEM constants + `_strip_tiebreaker()` helper).

2. **~line 235** — extend `VARIANT_CHOICES`:
   ```python
   VARIANT_CHOICES = (
       "single-pass", "two-pass", "both",
       "reasoning", "reasoning-two-pass",
       "binary-reasoning", "binary-no-tiebreaker",
       # NEW — unified suite
       "unified-binary-tb", "unified-binary-notb",
       "unified-4axis-tb", "unified-4axis-notb",
       "unified-genob-tb", "unified-genob-notb",
       "unified-all",  # convenience: run all six in sequence
   )
   ```

3. **after `run_one_binary_no_tiebreaker_pass()`** (~line 988) — add three new `run_one_unified_*()` functions:
   - `run_one_unified_binary(backend, sid, sname, sub, *, tiebreaker, ...) -> dict`
   - `run_one_unified_4axis(backend, sid, sname, sub, *, tiebreaker, ...) -> dict`
   - `run_one_unified_genob(backend, sid, sname, sub, *, tiebreaker, ...) -> dict`
   
   Each follows the pattern of `run_one_binary_reasoning_pass()`: format prompt → call `send_text()` → parse JSON via regex → apply post-processing → return record dict.

4. **in `run_variant()`** (~line 1006) — extend dispatch:
   ```python
   elif variant == "unified-binary-tb":
       run_one = functools.partial(run_one_unified_binary, tiebreaker=True)
   elif variant == "unified-binary-notb":
       run_one = functools.partial(run_one_unified_binary, tiebreaker=False)
   # ... etc for 4axis and genob ...
   ```

5. **in `save_results()`** (~lines 315–445) — extend the existing if/elif chain that builds `filename`, `test_name`, `description`, and `classifier_entry_point`. The existing chain handles each variant with its own block (see lines 325–442 of the script for the pattern). Add six new blocks following the same shape, one per new variant. Filename pattern:
   ```
   test_unified_{format}_{tb|notb}_FULL_CORPUS_{model}_{date}_{time}.json
   ```
   e.g. `test_unified_genob_notb_FULL_CORPUS_gemma12b_2026-05-13_0900.json`
   The `description` field should be one sentence naming the variant and its position in the comparison. The `classifier_entry_point` is `"run_4axis_full_corpus_test.run_one_unified_<format>"`. The new wrapper key `confidence_semantics` is added in this function at the same indentation level as `test_name` etc.

6. **in `run_full()`** (~line 1151) — handle `variant == "unified-all"` by expanding to all six unified-* in sequence (mirrors existing `variant == "both"` handling).

7. **near top, imports** — add `import functools` and `from insights.submission_coder import <post_processing_function>` (whatever its real name is — agent to find).

**No changes to**:
- `WELLBEING_CLASSIFIER_SYSTEM` (production prompt — read-only reference)
- `WELLBEING_CLASSIFIER_PROMPT` (reused as-is, with `signal_prefix=""`)
- `BINARY_REASONING_SYSTEM`, `BINARY_NO_TIEBREAKER_SYSTEM`, `FOUR_AXIS_REASONING_SYSTEM` (existing variants stay functional)
- Backend wiring, corpus loading, save_results JSON wrapper, CLI infrastructure

---

## CLI usage after the change

```bash
# Smoke (1 ES + 1 WB student, n=1, one variant)
PYTHONPATH=src python3 scripts/run_4axis_full_corpus_test.py \
    --variant unified-genob-notb --smoke

# Full run, one variant
PYTHONPATH=src python3 scripts/run_4axis_full_corpus_test.py \
    --variant unified-4axis-tb --n-runs 5

# Full run, all six unified variants (the paper's row-comparison data)
PYTHONPATH=src python3 scripts/run_4axis_full_corpus_test.py \
    --variant unified-all --n-runs 5
```

---

## Validation steps (run after agent implementation)

1. **Smoke each new variant individually** (six 1-minute runs):
   ```bash
   for v in unified-binary-tb unified-binary-notb unified-4axis-tb unified-4axis-notb unified-genob-tb unified-genob-notb; do
       PYTHONPATH=src python3 scripts/run_4axis_full_corpus_test.py --variant $v --smoke
   done
   ```
   Each should produce a `*_SMOKE.json` file in `output-format-bias/data/raw_outputs/` with 2 records (S002 + WB01) per variant.

2. **Verify substrate identity**: load the six produced JSONs, extract `system_prompt` from each record. For the three TB variants, all three system prompts should differ ONLY in the JSON schema tail (verify by diffing). For the three NOTB variants, same plus the tiebreaker paragraph absent. The TB↔NOTB pair within each format should differ by exactly the tiebreaker paragraph (verify diff).

3. **Verify schema parsing**:
   - Binary-TB / Binary-NOTB → records have `verdict` populated, no `axis` or `observation`
   - 4axis-TB / 4axis-NOTB → records have `axis` populated, no `verdict` or `observation`
   - Genob-TB / Genob-NOTB → records have `observation` populated (non-empty prose), no `verdict` or `axis`

4. **Verify post-processing fields populated**: every record should have `raw_decision`, `raw_confidence`, `post_threshold_decision`, `post_regex_decision`, `regex_demotion_applied`, `final_decision`. None should be `None` except where format-specific (e.g. `axis` is `None` for binary variants).

5. **WB01/WB04/WB07/WB08 sanity check on genob-notb full run**: rebuild the workshop with the new genob-notb run loaded; the prose for WB04 should now contain explicit disclosure-naming language (the new tail tells the model "name them directly"), not "this isn't distress." This is the load-bearing change for the paper's argument.

6. **Diff the six full runs at WB cases**: for WB01, WB04, WB07, WB08, compare the `final_decision` across formats. Document where formats disagree. Expected: binary/4-axis should classify these as CONCERN/CRISIS; genob `final_decision` is gen-ob's recoded version (the threshold/regex applied to its prose). The disagreements are the paper's data.

---

## Smoke-validation criteria (structural only — not finding pre-specification)

The implementing agent's smoke run validates wiring and schema, NOT findings. The agent should not pre-specify which WB cases produce which prose patterns — that's the experiment's result, not the implementer's success criterion.

Structural checks the smoke run must pass:
- Each variant produces a JSON file with the metadata wrapper described in "Output JSON schema."
- For each new variant, the `system_prompt` field on each record exists and is non-empty.
- For the three -tb variants, the substring `"DEFAULT TO NOT FLAGGING WHEN AMBIGUOUS"` appears in `system_prompt`.
- For the three -notb variants, that substring does NOT appear; the rest of the substrate IS present (check for the verbatim string `"NON-NEGOTIABLE EQUITY FLOOR"`).
- For each variant, `format`, `tiebreaker`, and the appropriate one-of-(`verdict`/`axis`/`observation`) field is populated; the other two of that triple are `None`.
- The wrapper's `confidence_semantics` block is populated.
- No records contain `error` values.

These are the implementer's success criteria. Any analytic interpretation of the smoke run is out of scope for the implementing agent — the user runs the smoke, eyeballs a few cells, and decides whether to proceed to the full corpus run.

## Open questions the implementing agent must verify / decide

1. **Location and signature of the production post-processing function.** Likely in `insights/submission_coder.py` or `insights/concern_detector.py`. The 0.7 threshold and regex patterns are documented in the `test_r_wellbeing_concern_FULL_CORPUS_gemma12b_2026-05-12_0150.json` records (`raw_verdict` / `production_verdict` / `raw_confidences` / `post_regex_confidences` / `regex_demotion_applied`). Find the function that produces those, import and call it. If not cleanly importable, copy the patterns into a small helper in this script and add a comment pointing at the production source.

2. **Temperature for gemma12b.** Existing 4-axis runs use 0.1 (MODELS["gemma12b"]["temperature"]). Existing gen-ob a2 runs may have used a different value — verify by inspecting one of the gen-ob output records' metadata. Reconcile to a single value across all six unified variants. If they differ, prefer 0.1 (matches the binary/4-axis baseline the paper compares against).

3. **Max-tokens for genob variant.** Existing reasoning variants use `REASONING_PASS_MAX_TOKENS = 400`. Genob may need more since it emits both reasoning + 3-4 sentences of observation prose. Suggest 500-600. Run smoke first, look at truncation behavior, adjust.

4. **Genob `final_decision` semantics.** With genob's `confidence` defined as "accuracy of characterization, not concern probability," the post-processing path needs to either (a) skip the threshold/regex demotion for genob and write `final_decision = "PROSE"`, or (b) interpret the prose to produce a CONCERN/CLEAR verdict (e.g., presence of certain keywords). I recommend (a) — keep genob's decision in the prose for downstream human/agent coding. Confirm with the user.

5. **Class context for genob.** None. All six unified variants run without class context — that's the user's stated preference based on the equity-floor + class-context interaction finding. Don't load or pass `class_reading`.

6. **Filename clash detection.** The new variants produce filenames like `test_unified_genob_notb_FULL_CORPUS_*` which don't collide with existing test files, but verify before running by listing the output directory.

---

## What this plan does NOT change

- Production prompts.py in Autograder4Canvas. Read-only.
- Any existing variant in `run_4axis_full_corpus_test.py`. They remain runnable.
- The genob workshop (`build_genob_workshop.py`) — separate tooling, not in scope here.
- The 2026-05-12 a2 + a2_no_context observations already produced — those remain valid data points for the "production prompt" comparison row.
- The field-note and AutoGrader-CLAUDE.md tasks already on the task list — separate work, deferred until after this suite produces data.

---

## Estimated work

- Implementation (delegated to fresh-context agent with this plan): ~2 hours of agent time. Bulk of the work is the three new `run_one_unified_*()` functions and the post-processing import/wiring.
- Smoke validation: ~10 minutes of compute on MLX.
- Full unified-all run: ~1.5–2 hours of compute (1,380 LLM calls).
- Coding pass + comparison reading: separate downstream work, not blocked by this plan.

The implementing agent receives this plan as its briefing. I (in the resuming session) validate the resulting script before any production-scale run.
