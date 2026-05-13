# Degradation Check Script — Design Spec

**Status**: Spec only. No code written. User reviews before implementation.  
**Date**: 2026-05-13  
**Target file**: `scripts/degradation_check.py` (in `Autograder4Canvas/scripts/` or standalone; see §8)

---

## 1. Goal and Motivation

The unified format-comparison suite runs six variants (binary-tb, binary-notb, 4axis-tb, 4axis-notb, genob-tb, genob-notb) against a 46-student corpus. Individual flag decisions can switch between variants without the variant being meaningfully better or worse — the classifier isn't perfectly deterministic at temp=0.1, and the six variants deliberately vary the output format so some cell-level churn is expected. What matters for "is this variant regressing?" is the aggregate: are WB cases still getting routed (true-positive rate) at roughly the same level? Are ES cases accumulating false positives?

This script compares a newly-completed run against a baseline at the aggregate level. It does not evaluate correctness — the "right" answer for most ES cases is contested. It detects change. Output is for researcher review; it makes no automatic decisions.

**Explicit non-goal**: no keyword matching against prose content. The binary and 4-axis comparisons operate on the `verdict` and `axis` fields only. Genob has no categorical output; see §7.

---

## 2. Function Signature

```python
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class Report:
    variant_current: str          # classifier_variant from current JSON wrapper
    variant_baseline: str         # classifier_variant from baseline JSON wrapper
    format: str                   # "binary" | "4axis" | "genob"
    current_path: Path
    baseline_path: Path
    timestamp: str                # ISO 8601
    # Aggregate measures
    wb_routed_current: int        # WB cases flagged (CONCERN or non-ENGAGED/NONE)
    wb_routed_baseline: int
    wb_total: int                 # should be 14 in full-corpus runs
    es_fp_current: int            # ES cases flagged
    es_fp_baseline: int
    es_total: int                 # should be 32 in full-corpus runs
    # Per-cell change list
    changed_cells: list[dict]     # see §5
    error_cells: list[dict]       # cells with error != None in either run
    # Summary
    judgment: str                 # "STABLE" | "DRIFT" | "DEGRADED"
    judgment_rationale: str       # one sentence
    # Caveats the script flags but can't resolve
    caveats: list[str]
    # Genob-only
    genob_skipped: bool           # True if format == "genob" and comparison skipped

def compare_runs(
    current_path: Path,
    baseline_path: Path,
    *,
    format_override: str | None = None,   # override auto-detected format
    stable_pct_threshold: float = 0.05,   # see §6
    drift_pct_threshold: float = 0.15,
    stable_agg_margin: int = 1,
    drift_agg_margin: int = 3,
) -> Report:
    ...
```

The function is importable. All thresholds are keyword-only with defaults so the caller (runner or user) can override without editing the script.

---

## 3. CLI Interface

```
python scripts/degradation_check.py <current.json> [--baseline <baseline.json>]
    [--format {binary,4axis,genob}]
    [--stable-pct-threshold 0.05]
    [--drift-pct-threshold 0.15]
    [--stable-agg-margin 1]
    [--drift-agg-margin 3]
    [--no-save]          # suppress writing the markdown report file
```

**Baseline selection** — if `--baseline` is not provided, the script applies this default lookup order (stopping at first match):

| Current variant | Default baseline candidates (glob, most-recent match) |
|---|---|
| `unified-binary-tb` | `test_binary_REASONING_FULL_CORPUS_*.json` |
| `unified-binary-notb` | `test_unified_binary_tb_FULL_CORPUS_*.json` (within-experiment sibling) |
| `unified-4axis-tb` | `test_n_4axis_REASONING_FULL_CORPUS_*.json` |
| `unified-4axis-notb` | `test_unified_4axis_tb_FULL_CORPUS_*.json` |
| `unified-genob-tb` | `test_variant_a2_FULL_CORPUS_*.json` (prior genob runs) |
| `unified-genob-notb` | `test_unified_genob_tb_FULL_CORPUS_*.json` |
| anything else | most-recent JSON in the same output directory matching same format prefix |

If no baseline candidate is found, the script exits with a clear error message naming the pattern it searched.

---

## 4. Aggregate Measures — Exact Definitions

**WB routing rate** — "flagged" means the model's categorical output indicates concern, per format:
- binary: `verdict == "CONCERN"`
- 4axis: `axis in {"CRISIS", "BURNOUT"}`
- genob: not applicable (see §7)

```
wb_routed = count of WB records where source == "wellbeing_synthetic" AND flagged
wb_routing_rate = wb_routed / wb_total
```

Multi-run files (`n_runs_per_student > 1`): collapse per-student across runs using majority vote (round up on tie) before counting. Record which students had a split vote as a caveat.

**ES false-positive rate** — "flagged" defined same as above by format:

```
es_fp = count of ES records where source == "ethnic_studies" AND flagged
es_fp_rate = es_fp / es_total
```

Same majority-vote collapse for multi-run files.

**Confidence distribution** (secondary, reported but not used in judgment thresholds):
- Mean and range of `confidence` for WB cases, current vs. baseline
- Note: confidence semantics differ across formats (binary/4axis = decision confidence; genob = characterization accuracy). Do not cross-compare confidence across formats. Report within-format only.

---

## 5. Per-Cell Change List Format

Each entry in `changed_cells`:

```python
{
    "student_id": str,
    "source": "ethnic_studies" | "wellbeing_synthetic",
    "current_decision": str | None,   # verdict or axis value, or "MAJORITY: X (split N/M)"
    "baseline_decision": str | None,
    "direction": "gained_flag" | "lost_flag" | "changed_label",
    # "gained_flag": not flagged in baseline, flagged in current
    # "lost_flag": flagged in baseline, not flagged in current
    # "changed_label": both runs flagged but axis/verdict value changed (4-axis only)
}
```

Each entry in `error_cells`:

```python
{
    "student_id": str,
    "source": str,
    "error_in": "current" | "baseline" | "both",
    "error_message": str | None,
}
```

Error cells are reported separately and excluded from aggregate counts (with a caveat noting the exclusion).

---

## 6. Threshold Definitions

**These thresholds are guesses. Review and adjust before implementation.**

```
pct_changed = len(changed_cells) / (wb_total + es_total)

wb_delta = abs(wb_routed_current - wb_routed_baseline)
es_fp_delta = abs(es_fp_current - es_fp_baseline)
```

| Judgment | Criteria |
|---|---|
| STABLE | `pct_changed <= 0.05` AND `wb_delta <= 1` AND `es_fp_delta <= 1` |
| DRIFT | not STABLE AND `pct_changed <= 0.15` AND `wb_delta <= 3` AND `es_fp_delta <= 3` |
| DEGRADED | `pct_changed > 0.15` OR `wb_routed_current < wb_routed_baseline - 2` OR `es_fp_current > es_fp_baseline + 2` |

The DEGRADED rule is asymmetric by design: WB routing dropping is a loss of detection sensitivity; ES false positives increasing is a surveillance-bias risk. Both are degradation. ES false positives decreasing or WB routing increasing is NOT degradation (it may be improvement or it may be overcorrection — user review resolves this).

The script always prints the raw numbers. The judgment label is a reading aid, not a decision gate.

---

## 7. Genob Handling

Genob records carry no categorical `verdict` or `axis`. Three options were considered:

**(A)** Skip aggregate measures; report only structural checks and a note that "genob comparison requires downstream agent coding; this script does not auto-classify prose."

**(B)** Compare structural fields only: `confidence` distribution, `observation` non-empty, `error` rate.

**(C)** Use available agent codes from `data_tables/agent_codes/` as the comparison ground, if present.

**Recommendation: implement (A) as the default, with (B) as an automatic fallback when a baseline exists and the format is genob.**

Rationale: (A) is honest — the whole point of genob is that the prose is the data and should not be auto-classified. (B) adds genuinely useful signal (did the error rate change? did the model stop producing observations?) without touching prose content. (C) is the most informative option but requires the agent codes to be loaded into a consistent schema, which is separate downstream work and should not block this script.

In the genob case, the report's aggregate section reads:

```
FORMAT: genob — categorical comparison not applicable.
Structural checks (current vs. baseline):
  - Observation non-empty: N/M records (current) vs. N/M records (baseline)
  - Error rate: N/M (current) vs. N/M (baseline)
  - Mean confidence: X.XX (current) vs. X.XX (baseline)
  
For content comparison, use agent codes in data_tables/agent_codes/.
```

Open design question for the user: **Should (C) be implemented as an optional path**, activated by a `--agent-codes <path>` flag? If so, the script would load the JSON from that path, join by `student_id`, and treat the agent's qualitative code as the comparison field. This would make the genob report as informative as the binary/4-axis ones for WB cases. Flag this for user decision before implementation.

---

## 8. Integration Point — Runner Hook

`save_results()` in `/Users/june/Documents/GitHub/Autograder4Canvas/scripts/run_4axis_full_corpus_test.py` returns the saved `Path` at **line 648**:

```python
    path.write_text(json.dumps(output, indent=2, default=str))
    return path                  # ← line 648
```

The hook call goes immediately after `save_results()` returns in the `run_variant()` or `run_full()` dispatch, not inside `save_results()` itself. This keeps `save_results()` pure (write-only; no side effects beyond writing the JSON).

Proposed integration (do NOT edit runner until spec is approved):

```python
# In run_variant() or run_full(), after:
#   saved_path = save_results(results, variant=variant, ...)
from degradation_check import compare_runs, find_default_baseline
baseline = find_default_baseline(saved_path, variant=variant, output_dir=OUTPUT_DIR)
if baseline:
    report = compare_runs(saved_path, baseline)
    print(report.summary_text())   # to stdout for the user watching the run
else:
    print(f"[degradation_check] No baseline found for {variant}; skipping.")
```

The `find_default_baseline()` helper encapsulates the lookup table from §3 so the runner doesn't duplicate it.

**The degradation check should never raise an exception that stops the runner.** Wrap in `try/except Exception as e: print(f"[degradation_check] WARNING: {e}; skipping.")`.

---

## 9. Report Output Format

Saved as `<current_filename_without_extension>_degradation_report.md` alongside the run JSON in `data/raw_outputs/`.

Sections:
1. **Header**: variant, baseline, timestamp, judgment badge (`STABLE` / `DRIFT` / `DEGRADED`)
2. **Aggregate table**: WB routing rate and ES FP rate, current vs. baseline, delta
3. **Per-cell change list**: table of `changed_cells` sorted by `student_id`
4. **Error cells**: if any
5. **Confidence distribution** (secondary)
6. **Caveats**: auto-generated, e.g. split-vote collapses, error-cell exclusions, smoke-run flag
7. **Genob note** (if applicable)

---

## 10. Open Questions for User to Resolve Before Implementation

1. **Genob option (C)**: implement `--agent-codes` flag for content-grounded genob comparison? Agent codes exist at `data_tables/agent_codes/` but their schema needs to be checked for join compatibility.

2. **Multi-run majority vote**: is majority vote (per student, across runs) the right collapse? An alternative is to count any-flagged-in-any-run as flagged (union) or flagged-in-all-runs (intersection). The majority rule is a reasonable middle ground but changes how volatile the numbers look.

3. **Smoke-run behavior**: should the script skip or explicitly label comparisons where `smoke == true` in either JSON? A smoke run has 2 records vs. 46; the thresholds in §6 would be meaningless. Recommend: skip judgment, report raw counts only, add a caveat.

4. **Script location**: `Autograder4Canvas/scripts/degradation_check.py` (alongside the runner) or `research/output-format-bias/scripts/`? The runner import path depends on this.

5. **Baseline for the first run of a new variant** (no prior run exists): script should print a clear "no baseline found; run will serve as future baseline" message and skip gracefully, not error.

---

## Implementation Estimate

~150 lines of Python. Standard library only (`json`, `pathlib`, `glob`, `dataclasses`, `datetime`, `argparse`). No external dependencies.
