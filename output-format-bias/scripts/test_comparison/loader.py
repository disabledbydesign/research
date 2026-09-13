"""Schema-dispatched JSON loaders for wellbeing-classifier raw outputs.

Each loader reads ONE specific schema explicitly. The dispatcher routes by:
    1. classifier_variant field (if present) — primary contract
    2. test_name prefix (for older / non-classifier schemas)
Unknown schemas raise — we never silently coerce.

----------------------------------------------------------------------------
ADDING A NEW SCHEMA (the only case you'd need to touch Python):
----------------------------------------------------------------------------
1. Write `load_<schema>(data: dict, path: str) -> list[Record]`. Each Record is
   a flat dict with at minimum: file, student_id, run, flag, axis, confidence,
   plus whatever schema-specific fields you want preserved (reasoning,
   raw_output_text, production_flag, etc.).
2. Add an entry to the dispatch logic in `load()` below. Use classifier_variant
   if the schema sets it; otherwise match on test_name prefix.
3. If your schema needs per-record fields the existing aggregator doesn't
   handle, extend aggregate.py — the loader stays focused on parsing.
"""
import json
from pathlib import Path
from typing import Optional


Record = dict  # alias for documentation


# -----------------------------------------------------------------------------
# Schema 1: binary_concern (Test R / WELLBEING_CONCERN_PROMPT / production binary)
# -----------------------------------------------------------------------------

def load_binary_concern(data: dict, path: str) -> list:
    """Parse Test R / WELLBEING_CONCERN_PROMPT raw output.

    Schema fields used (from data['results'][i]):
      - student_id, student_name, source ('ES' or 'WB'), pattern, run
      - raw_verdict ('FLAG' | 'CLEAR'), production_verdict ('FLAG' | 'CLEAR')
      - raw_confidences (list of floats from each detected concern)
      - raw_output (model's free-text JSON-in-markdown — preserved for reasoning modal)
    """
    out = []
    for r in data["results"]:
        raw_confs = r.get("raw_confidences") or []
        confidence = max(raw_confs) if raw_confs else None
        out.append({
            "file": path,
            "schema": "binary_concern",
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "source": r.get("source"),
            "pattern": r.get("pattern"),
            "run": r["run"],
            # primary fields
            "flag": r["raw_verdict"] != "CLEAR",
            "axis": None,  # binary schema has no axis
            "confidence": confidence,
            # binary-specific extra: production post-processor verdict
            "production_flag": r["production_verdict"] != "CLEAR",
            "raw_verdict": r["raw_verdict"],
            "production_verdict": r["production_verdict"],
            # reasoning lives inside raw_output (JSON-in-markdown)
            "reasoning": None,
            "raw_output_text": r.get("raw_output", ""),
        })
    return out


# -----------------------------------------------------------------------------
# Schema 2: 4axis (Test N single-pass + binary-reasoning + reasoning variants)
# -----------------------------------------------------------------------------

def load_4axis(data: dict, path: str) -> list:
    """Parse 4-axis output schemas (CRISIS/BURNOUT/ENGAGED/NONE).

    Covers classifier_variant in {'single-pass', 'reasoning', 'binary-reasoning'}.

    Schema fields used (from data['results'][i]):
      - student_id, student_name, source, pattern, run
      - actual_axis ('CRISIS' | 'BURNOUT' | 'ENGAGED' | 'NONE')
      - confidence (float)
      - reasoning (str, may be None if classifier_variant == 'single-pass')
      - raw_output (preserved)
    """
    # Source values vary across 4axis files: 'ES'/'WB' or 'ethnic_studies'/'wellbeing_signal_cases'.
    # Normalize to 'ES'/'WB' for downstream consumers.
    SRC_MAP = {
        "ES": "ES", "WB": "WB",
        "ethnic_studies": "ES",
        "wellbeing_signal_cases": "WB",
        "wellbeing": "WB",
    }
    out = []
    for r in data["results"]:
        axis = r.get("actual_axis")
        flag = axis in ("CRISIS", "BURNOUT")
        out.append({
            "file": path,
            "schema": "4axis",
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "source": SRC_MAP.get(r.get("source"), r.get("source")),
            "pattern": r.get("pattern"),
            "run": r["run"],
            # primary fields
            "flag": flag,
            "axis": axis,
            "confidence": r.get("confidence"),
            # production_flag mirrors flag (no post-processor for 4-axis)
            "production_flag": flag,
            "raw_verdict": axis,
            "production_verdict": axis,
            "reasoning": r.get("reasoning"),
            "raw_output_text": r.get("raw_output", ""),
        })
    return out


# -----------------------------------------------------------------------------
# Schema 3: observation (variant_a gen-ob raw output — free-text observations)
# -----------------------------------------------------------------------------

def load_genob_observation(data: dict, path: str) -> list:
    """Parse variant_a observation raw output.

    Used by the gen-ob workshop (NOT directly by the comparison tool — gen-ob
    enters the comparison tool via manual_codes after you've coded it).

    Handles two on-disk shapes:
      1. Completed run: data['results_by_model'][model_name] -> [records]
      2. Checkpointed partial run: data['results_so_far'] -> flat list of records,
         with data['model'] holding the single model name (used by
         run_genob_full_corpus_test.py's per-pass save).

    Returns one record per (student, model, run).
    """
    out = []
    condition = data.get("condition")
    rbm = data.get("results_by_model")
    if rbm:
        iter_pairs = rbm.items()
    else:
        # Partial-checkpoint shape: results_so_far + top-level model
        model_top = data.get("model")
        rso = data.get("results_so_far") or []
        if model_top is None or not rso:
            return out
        iter_pairs = [(model_top, rso)]

    for model, records in iter_pairs:
        for r in records:
            out.append({
                "file": path,
                "schema": "observation",
                "student_id": r["student_id"],
                "student_name": r["student_name"],
                "model": model,
                "condition": condition,
                "run": r.get("run", 1),
                "is_wb_case": r.get("is_wb_case", False),
                "wb_signal_type": r.get("wb_signal_type"),
                "wb_expected_surface": r.get("wb_expected_surface"),
                # free-text observation prose
                "raw_output_text": r.get("raw_output", ""),
            })
    return out


# -----------------------------------------------------------------------------
# Schema 5: unified (2026-05-12+ unified format-comparison suite)
# -----------------------------------------------------------------------------
#
# The unified suite shares WELLBEING_CLASSIFIER_SYSTEM as substrate across all
# format variants (binary / 4axis / genob), and produces a single uniform
# per-record shape. classifier_variant takes the form "unified-<format>-<state>"
# where state is tb/notb (v1) or {narrow,broad}? × {both,single,neither} (v2).
#
# This loader normalizes unified records into the EXISTING downstream schemas
# (binary_concern for unified-binary-*, 4axis for unified-4axis-*) so the
# aggregator and HTML template don't need to know about unified at all.
#
# Unified-genob-* records have verdict=None and axis=None (the output is
# free-text observation, not a categorical verdict). For the comparison tool,
# those flow through the gen-ob hand-coding workflow → manual_codes schema.

# source values in unified files. Extends the 4axis SRC_MAP.
_UNIFIED_SRC_MAP = {
    "ES": "ES",
    "WB": "WB",
    "ethnic_studies": "ES",
    "wellbeing_signal_cases": "WB",
    "wellbeing": "WB",
    "wellbeing_synthetic": "WB",
}


def load_unified(data: dict, path: str) -> list:
    """Parse the unified format-comparison suite (classifier_variant=unified-*).

    Dispatches by classifier_variant to emit either binary_concern-shaped or
    4axis-shaped records. unified-genob-* is rejected — those go through the
    gen-ob hand-coding workflow and enter the comparison tool as manual_codes.
    """
    cv = data.get("classifier_variant", "")
    if cv.startswith("unified-binary-"):
        return _load_unified_binary(data, path)
    if cv.startswith("unified-4axis-"):
        return _load_unified_4axis(data, path)
    if cv.startswith("unified-genob-"):
        return _load_unified_genob(data, path)
    raise ValueError(f"Unknown unified classifier_variant: {cv!r} in {path}")


def _load_unified_genob(data: dict, path: str) -> list:
    """unified-genob-* → observational records (flag=None, no truth grading).

    Genob produces free-text observations, not categorical verdicts. We emit
    records with flag=None and axis='OBS' so the aggregator marks the cells
    as 'edge' (ungraded) rather than computing TP/FP/FN/TN. The observation
    text is preserved in raw_output_text and reasoning for the cell modal.
    """
    out = []
    for r in data["results"]:
        out.append({
            "file": path,
            "schema": "genob_observation",
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "source": _UNIFIED_SRC_MAP.get(r.get("source"), r.get("source")),
            "pattern": r.get("pattern"),
            "run": r["run"],
            # flag=None signals to aggregator: do not grade against truth.
            "flag": None,
            "axis": "OBS",
            "confidence": r.get("confidence"),
            "production_flag": None,
            "raw_verdict": "OBS",
            "production_verdict": "OBS",
            # Genob reasoning may live under 'observation' or 'reasoning'; prefer non-empty.
            "reasoning": r.get("reasoning") or r.get("observation"),
            "raw_output_text": r.get("raw_output", ""),
        })
    return out


def _load_unified_binary(data: dict, path: str) -> list:
    """unified-binary-* → binary_concern-shaped records.

    Per-record fields used: student_id, student_name, source, pattern, run,
    verdict ('CONCERN' | 'ENGAGED' | 'CLEAR'), confidence, reasoning, raw_output.
    'CONCERN' is the flag verdict; 'ENGAGED' and 'CLEAR' both mean no flag.
    """
    out = []
    for r in data["results"]:
        verdict = r.get("verdict")
        flag = verdict == "CONCERN"
        out.append({
            "file": path,
            "schema": "binary_concern",
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "source": _UNIFIED_SRC_MAP.get(r.get("source"), r.get("source")),
            "pattern": r.get("pattern"),
            "run": r["run"],
            "flag": flag,
            "axis": None,
            "confidence": r.get("confidence"),
            # No post-processor for unified binary — production mirrors raw.
            "production_flag": flag,
            "raw_verdict": "FLAG" if flag else "CLEAR",
            "production_verdict": "FLAG" if flag else "CLEAR",
            "reasoning": r.get("reasoning"),
            "raw_output_text": r.get("raw_output", ""),
        })
    return out


def _load_unified_4axis(data: dict, path: str) -> list:
    """unified-4axis-* → 4axis-shaped records.

    Per-record fields used: student_id, student_name, source, pattern, run,
    axis ('CRISIS' | 'BURNOUT' | 'ENGAGED' | 'NONE'), confidence, reasoning.
    """
    out = []
    for r in data["results"]:
        axis = r.get("axis")
        flag = axis in ("CRISIS", "BURNOUT")
        out.append({
            "file": path,
            "schema": "4axis",
            "student_id": r["student_id"],
            "student_name": r["student_name"],
            "source": _UNIFIED_SRC_MAP.get(r.get("source"), r.get("source")),
            "pattern": r.get("pattern"),
            "run": r["run"],
            "flag": flag,
            "axis": axis,
            "confidence": r.get("confidence"),
            "production_flag": flag,
            "raw_verdict": axis,
            "production_verdict": axis,
            "reasoning": r.get("reasoning"),
            "raw_output_text": r.get("raw_output", ""),
        })
    return out


# -----------------------------------------------------------------------------
# Schema 4: manual_codes (gen-ob workshop export — your codes as verdicts)
# -----------------------------------------------------------------------------

def load_manual_codes(data: dict, path: str) -> list:
    """Parse manual_codes JSON exported by the gen-ob workshop.

    Schema (see plan / workshop export button):
      {
        "schema": "manual_codes",
        "exported_from": "<observation config id>",
        "exported_model": "<model>",
        "exported_condition": "<condition>",
        "exported_at": "<ISO date>",
        "category_to_verdict": {<category_id>: "FLAG"|"CLEAR"|"REVIEW", ...},
        "unmapped_category_behavior": "FLAG" | "CLEAR" | "REVIEW",
        "codes": {<student_id>: {"code": <category_id>, "notes": str, "raw_observation_text": str}}
      }

    Returns one record per student (this is a single-run categorical config).
    """
    if data.get("schema") != "manual_codes":
        raise ValueError(f"Expected schema='manual_codes' in {path}, got {data.get('schema')!r}")
    cat_to_verdict = data["category_to_verdict"]
    unmapped = data.get("unmapped_category_behavior", "REVIEW")
    out = []
    for sid, entry in data["codes"].items():
        code = entry["code"]
        verdict = cat_to_verdict.get(code, unmapped)
        out.append({
            "file": path,
            "schema": "manual_codes",
            "student_id": sid,
            "student_name": entry.get("student_name", ""),
            "source": "ES" if sid.startswith("S") else "WB",
            "pattern": entry.get("pattern"),
            "run": 1,
            "flag": verdict == "FLAG",
            "axis": code,  # the category id is the "axis"
            "confidence": None,  # manual codes have no confidence
            "production_flag": verdict == "FLAG",
            "raw_verdict": verdict,
            "production_verdict": verdict,
            "reasoning": entry.get("notes", ""),
            "raw_output_text": entry.get("raw_observation_text", ""),
        })
    return out


# -----------------------------------------------------------------------------
# Dispatcher
# -----------------------------------------------------------------------------

def _infer_schema(data: dict, path: str) -> str:
    cv = data.get("classifier_variant")
    # Unified format-comparison suite (2026-05-12+): one loader handles all
    # three formats and emits binary_concern- or 4axis-shaped records.
    if isinstance(cv, str) and cv.startswith("unified-"):
        return "unified"
    # Known 4-axis variants (explicit allowlist for clarity/audit)
    if cv in ("single-pass", "reasoning", "binary-reasoning", "binary-no-tiebreaker"):
        return "4axis"

    tn = data.get("test_name") or ""
    if tn.startswith("test_r_wellbeing_concern") or tn.startswith("test_binary_concern"):
        return "binary_concern"
    if tn.startswith("test_variant_") and "observation" in tn:
        return "observation"

    if data.get("schema") == "manual_codes":
        return "manual_codes"

    # Partial-checkpoint observation file: results_so_far (list) + model + condition,
    # no test_name. Written by run_genob_full_corpus_test.py between passes.
    if (
        isinstance(data.get("results_so_far"), list)
        and data.get("model")
        and data.get("condition")
    ):
        return "observation"

    # Permissive fallback: if a 'results' list has records with the 4-axis output shape,
    # treat as 4-axis. This means new classifier_variant strings auto-dispatch correctly
    # as long as they emit the same per-record fields. Keeps the explicit allowlist above
    # for documentation purposes, but doesn't fail when a new variant lands.
    results = data.get("results")
    if isinstance(results, list) and results and isinstance(results[0], dict):
        r0 = results[0]
        if "actual_axis" in r0 and "confidence" in r0:
            return "4axis"
        if "raw_verdict" in r0 and "production_verdict" in r0:
            return "binary_concern"

    raise ValueError(
        f"Unknown schema for {path}\n"
        f"  test_name={tn!r}, classifier_variant={cv!r}\n"
        f"  Looked for per-record shape (actual_axis+confidence for 4axis, raw_verdict+production_verdict for binary)\n"
        f"  → not matched. To add a new schema, see the docstring at the top of loader.py."
    )


_LOADERS = {
    "binary_concern": load_binary_concern,
    "4axis": load_4axis,
    "observation": load_genob_observation,
    "manual_codes": load_manual_codes,
    "unified": load_unified,
}


def load(path) -> list:
    """Load any supported schema. Returns a list of normalized Records."""
    path = str(path)
    with open(path) as fh:
        data = json.load(fh)
    schema = _infer_schema(data, path)
    return _LOADERS[schema](data, path)


def load_many(paths) -> list:
    """Concatenate records from multiple files. Useful when a config has multiple runs split across files."""
    out = []
    for p in paths:
        out.extend(load(p))
    return out
