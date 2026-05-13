#!/usr/bin/env python3
"""Generative observation coding workshop with in-browser run selector.

Accepts any set of observation JSON files and generates a self-contained HTML
where the researcher can:
  - Switch between runs via a dropdown (swaps the table in place)
  - Code each observation (category dropdown + notes textarea) with localStorage
  - Hover any observation preview to see full text in a popover
  - See agent codes in a side column when --agent-codes files are provided
  - Export the coding state as JSON for downstream comparison tool use

Agent codes format (write one of these per coder per run):
    {
        "schema": "genob_agent_codes",
        "coder": "Opus 4",
        "run_id": "a2_no_context_2026-05-12_1414",
        "codes": {
            "S001_gemma12b_a2_no_context": {"category": "asset-framing", "notes": "..."},
            ...
        }
    }

Usage:
    python scripts/build_genob_workshop.py \\
        data/raw_outputs/test_variant_a2_no_context_FULL_CORPUS_observation_2026-05-12_1414.json \\
        [--agent-codes data_tables/agent_codes_opus_2026-05-12.json] \\
        [--out data_tables/genob_workshop_2026-05-12.html]
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from test_comparison import loader as _loader  # noqa: E402


DEFAULT_CATEGORIES = [
    {"id": "asset", "label": "Asset-framing", "color": "#d4edda"},
    {"id": "wellbeing", "label": "Wellbeing concern", "color": "#fff3cd"},
    {"id": "deficit", "label": "Deficit-coded", "color": "#f8d7da"},
    {"id": "paternalism", "label": "Paternalistic inference", "color": "#fde5c3"},
    {"id": "hallucination", "label": "Hallucination", "color": "#e2d9f3"},
    {"id": "pronoun_error", "label": "Pronoun error", "color": "#d1ecf1"},
    {"id": "taxonomy_fp", "label": "Taxonomy false-positive", "color": "#f5e0d3"},
    {"id": "minimal_effort", "label": "Minimal-effort read", "color": "#e9ecef"},
]


def _sort_student_key(sid: str):
    prefix = 0 if sid.startswith("S") else 1
    try:
        num = int(sid[2:] if sid.startswith("WB") else sid[1:])
    except ValueError:
        num = 999
    return (prefix, num)


def _derive_run_id(path: Path, data: dict) -> str:
    stem = path.stem
    m = re.search(r"(\d{4}-\d{2}-\d{2}(?:_\d{4})?)", stem)
    date_part = m.group(1) if m else datetime.date.today().isoformat()
    cond = data.get("condition", "unknown")
    return f"{cond}_{date_part}"


def load_run(path: Path) -> dict:
    """Load one observation JSON file into a run descriptor."""
    records = _loader.load(path)
    obs = [r for r in records if r.get("schema") == "observation"]
    if not obs:
        raise ValueError(f"No observation-schema records in {path}")

    raw = json.loads(path.read_text())
    run_id = _derive_run_id(path, raw)
    condition = raw.get("condition", "unknown")

    models = sorted(set(r["model"] for r in obs))

    seen_students = set()
    students_ordered = []
    student_names = {}
    is_wb = {}
    for r in obs:
        sid = r["student_id"]
        if sid not in seen_students:
            seen_students.add(sid)
            students_ordered.append(sid)
        student_names[sid] = r["student_name"]
        is_wb[sid] = r.get("is_wb_case", sid.startswith("WB"))

    students_ordered.sort(key=_sort_student_key)

    # Build cells: key = "sid_model_condition" (one per student×model, first run only)
    cells = {}
    for r in obs:
        cid = f"{r['student_id']}_{r['model']}_{condition}"
        if cid not in cells:
            cells[cid] = {
                "sid": r["student_id"],
                "model": r["model"],
                "condition": condition,
                "text": (r.get("raw_output_text") or "").strip(),
                "student_name": r["student_name"],
                "is_wb_case": r.get("is_wb_case", r["student_id"].startswith("WB")),
                "wb_signal_type": r.get("wb_signal_type") or "",
            }

    n_s = len(students_ordered)
    n_m = len(models)
    label = f"{condition} — {path.name} ({n_s} students, {', '.join(models)})"

    return {
        "id": run_id,
        "label": label,
        "condition": condition,
        "models": models,
        "students": students_ordered,
        "student_names": student_names,
        "is_wb_case": is_wb,
        "cells": cells,
    }


def load_agent_codes(paths: list) -> dict:
    """Load agent code JSON files. Returns {run_id:cid: [entries]}.

    Each entry has: coder, categories (list of emergent codes), wellbeing_check_in
    ('yes'/'no'/'ambiguous'/''), wellbeing_reason, load_bearing_quotes (list of
    verbatim phrases from the observation), notes.

    Accepts both new schema (categories: list) and legacy single category (str).
    """
    out = {}
    for p in paths:
        data = json.loads(Path(p).read_text())
        coder = data.get("coder", Path(p).stem)
        run_id = data.get("run_id", "")
        for cid, entry in data.get("codes", {}).items():
            key = f"{run_id}:{cid}" if run_id else cid

            # Categories: accept list 'categories' OR legacy string 'category'
            cats = entry.get("categories")
            if cats is None and entry.get("category"):
                cats = [entry["category"]]
            cats = [str(c) for c in (cats or []) if c]

            quotes = [str(q) for q in (entry.get("load_bearing_quotes") or []) if q]
            wb = (entry.get("wellbeing_check_in") or "").lower().strip()
            # Back-compat: "yes" → "concern_surfaced". Accept both new and legacy.
            if wb == "yes":
                wb = "concern_surfaced"
            if wb not in ("concern_surfaced", "no", "ambiguous", ""):
                wb = ""  # ignore unknown values silently

            wb_codes = [str(c) for c in (entry.get("wellbeing_codes") or []) if c]

            if key not in out:
                out[key] = []
            out[key].append({
                "coder": coder,
                "categories": cats,
                "wellbeing_check_in": wb,
                "wellbeing_codes": wb_codes,
                "wellbeing_reason": entry.get("wellbeing_reason", ""),
                "load_bearing_quotes": quotes,
                "notes": entry.get("notes", ""),
            })
    return out


def load_corpus_review_state(path) -> dict:
    """Load the hand-coding corpus_review_state.json.

    File uses flat keys: pattern_<sid>, notes_<sid>, expected_<sid>, reviewed_<sid>.
    Returns {sid: {pattern, expected, notes}} for sids that have at least a pattern.
    """
    data = json.loads(Path(path).read_text())
    out = {}
    for k, v in data.items():
        if not isinstance(k, str) or "_" not in k:
            continue
        prefix, _, sid = k.partition("_")
        if not sid:
            continue
        if prefix not in ("pattern", "notes", "expected"):
            continue
        entry = out.setdefault(sid, {"pattern": "", "notes": "", "expected": ""})
        entry[prefix] = v
    # Drop sids that have no pattern (no useful label material)
    return {sid: e for sid, e in out.items() if e.get("pattern")}


def load_cross_condition_synthesis(paths: list) -> dict:
    """Load cross-condition synthesis JSON files.

    Schema:
        {
          "coder": "Opus 4",
          "compared_runs": ["<run_id_a>", "<run_id_b>"],
          "per_student": {
              "<sid>": {
                  "what_changed": "...",
                  "directional_assessment": "context-better"|"no-context-better"|"comparable"|"different-failure-modes",
                  "evidence": {"<run_id>": "verbatim quote", ...}
              }
          },
          "general_notes": "free-form observations about differences across the corpus that don't fit the per-student structure",
          "overall_synthesis": "conclusion-shaped summary of the cross-condition comparison"
        }

    Returns: {coder: {compared_runs, per_student, general_notes, overall_synthesis}}.
    """
    out = {}
    for p in paths:
        data = json.loads(Path(p).read_text())
        coder = data.get("coder", Path(p).stem)
        out[coder] = {
            "compared_runs": data.get("compared_runs", []),
            "per_student": data.get("per_student", {}),
            "general_notes": data.get("general_notes", ""),
            "overall_synthesis": data.get("overall_synthesis", ""),
        }
    return out


def build_html(runs: list, agent_codes: dict, synthesis: dict, expected_coders: list, corpus_labels: dict) -> str:
    runs_json = json.dumps(runs, ensure_ascii=False)
    agent_json = json.dumps(agent_codes, ensure_ascii=False)
    synthesis_json = json.dumps(synthesis, ensure_ascii=False)
    cats_json = json.dumps(DEFAULT_CATEGORIES, ensure_ascii=False)
    coders_json = json.dumps(expected_coders, ensure_ascii=False)
    corpus_labels_json = json.dumps(corpus_labels, ensure_ascii=False)
    today = datetime.date.today().isoformat()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Genob Coding Workshop — {today}</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 1900px; margin: 1em auto; padding: 0 1em; line-height: 1.5; color: #222; background: #fafaf7; }}
  h1 {{ font-size: 1.3em; margin-bottom: 0.15em; }}
  details summary {{ cursor: pointer; font-weight: bold; padding: 0.3em 0; }}
  details {{ background: #f7f4ee; padding: 0.35em 1em; border-radius: 4px; margin-bottom: 0.5em; border: 1px solid #ddd; }}

  /* Controls bar */
  .controls-bar {{ position: sticky; top: 0; background: #fafaf7; padding: 0.4em 0; z-index: 20; border-bottom: 1px solid #ddd; margin-bottom: 0.5em; display: flex; align-items: center; gap: 0.5em; flex-wrap: wrap; }}
  .controls-bar button {{ padding: 0.3em 0.7em; cursor: pointer; font-family: Georgia, serif; font-size: 0.83em; border: 1px solid #bbb; border-radius: 3px; background: #fff; }}
  .controls-bar button.primary {{ background: #1a4a7e; color: #fff; border-color: #1a4a7e; }}
  .progress {{ font-size: 0.83em; color: #555; margin-left: 0.3em; }}

  /* Categories editor */
  .legend-row {{ display: flex; align-items: center; gap: 0.5em; margin: 0.22em 0; }}
  .legend-edit {{ width: 170px; padding: 0.18em 0.4em; font-family: Georgia, serif; font-size: 0.83em; border: 1px solid #bbb; border-radius: 2px; }}

  /* Tabs */
  .tabs {{ display: flex; gap: 2px; margin-top: 0.4em; flex-wrap: wrap; }}
  .tab {{ padding: 0.45em 1em; background: #e0ddd5; border: 1px solid #bbb; border-bottom: none; border-radius: 4px 4px 0 0; cursor: pointer; font-size: 0.85em; white-space: nowrap; }}
  .tab.active {{ background: #fff; font-weight: bold; position: relative; top: 1px; border-bottom: 2px solid #fff; z-index: 1; }}
  .tab.comp-tab {{ background: #dde9f5; color: #1a4a7e; }}
  .tab.comp-tab.active {{ background: #edf2fb; }}
  .tab-content {{ display: none; border: 1px solid #bbb; border-radius: 0 4px 4px 4px; padding: 0.5em; background: #fff; }}
  .tab-content.active {{ display: block; }}

  /* Coding table */
  table.coding {{ border-collapse: collapse; width: 100%; table-layout: fixed; margin-top: 0.4em; }}
  table.coding th, table.coding td {{ border: 1px solid #ccc; padding: 0; vertical-align: top; }}
  table.coding th {{ background: #ececec; font-weight: bold; padding: 0.35em 0.45em; font-size: 0.8em; }}
  table.coding th.student-col {{ width: 175px; font-family: 'Courier New', monospace; }}
  table.coding th.obs-col {{ font-family: 'Courier New', monospace; }}
  table.coding th.june-col {{ background: #f5ecd9; font-family: 'Courier New', monospace; color: #6c4f0a; }}
  table.coding th.agent-col {{ background: #edf2fb; font-family: 'Courier New', monospace; font-size: 0.76em; color: #1a4a7e; }}
  table.coding td.obs-cell {{ height: 240px; position: relative; padding: 0.32em 0.42em; font-size: 0.8em; }}
  table.coding td.june-cell {{ height: 240px; background: #fdf8ec; padding: 0.4em 0.5em; vertical-align: top; }}
  table.coding td.agent-cell {{ height: 240px; background: #f5f8ff; padding: 0.4em 0.5em; font-size: 0.76em; vertical-align: top; overflow-y: auto; }}

  /* Observation cell (just the model text + hover, no input controls) */
  .cell-preview {{ height: 100%; overflow-y: auto; background: rgba(255,255,255,0.55); border: 1px dashed #aaa; border-radius: 2px; padding: 0.32em 0.42em; font-family: Georgia, serif; line-height: 1.36; font-size: 0.95em; cursor: pointer; user-select: none; }}
  .cell-preview:hover {{ background: rgba(255,255,255,0.95); border-color: #1a4a7e; }}
  .cell-excerpt-marker {{ color: #b8860b; font-weight: bold; margin-right: 0.2em; }}

  /* June coding cell (category dropdown + notes textarea) */
  .june-inner {{ height: 100%; display: flex; flex-direction: column; gap: 5px; padding: 0.18em; }}
  .june-inner .cell-cat {{ font-family: Georgia, serif; font-size: 0.85em; padding: 0.22em 0.3em; border: 1px solid #888; background: rgba(255,255,255,0.95); width: 100%; min-width: 0; }}
  .june-inner .cell-notes {{ flex: 1; min-height: 70px; font-family: Georgia, serif; font-size: 0.82em; padding: 0.3em; border: 1px solid #888; resize: none; background: rgba(255,255,255,0.95); line-height: 1.35; }}
  .june-inner .cell-notes:focus {{ background: #fff; outline: 2px solid #5a8ec9; }}

  /* Student column */
  th.student-col .sid {{ font-family: 'Courier New', monospace; font-size: 0.88em; }}
  th.student-col .sname {{ font-weight: normal; font-size: 0.75em; color: #444; font-family: Georgia, serif; display: block; }}
  .wb-badge {{ display: inline-block; background: #c2941f; color: #fff; font-size: 0.67em; padding: 0.08em 0.32em; border-radius: 3px; font-family: 'Courier New', monospace; margin-top: 0.12em; }}
  .es-badge {{ display: inline-block; background: #6c757d; color: #fff; font-size: 0.67em; padding: 0.08em 0.32em; border-radius: 3px; font-family: 'Courier New', monospace; margin-top: 0.12em; }}
  th.student-col textarea.pattern {{ width: 100%; min-height: 48px; font-family: Georgia, serif; font-size: 0.72em; padding: 0.18em; border: 1px solid #bbb; resize: vertical; margin-top: 0.2em; background: #fff; line-height: 1.3; font-weight: normal; }}

  /* Label material: read-only ground-truth pattern + expected label from corpus_review_state.json */
  .label-material {{ background: #fffbeb; border: 1px solid #e6d28a; border-radius: 3px; padding: 0.32em 0.4em; margin-top: 0.3em; font-family: Georgia, serif; font-weight: normal; font-size: 0.72em; line-height: 1.4; color: #4a3300; }}
  .label-material-header {{ font-family: 'Courier New', monospace; font-size: 0.7em; font-weight: bold; color: #8b6914; text-transform: uppercase; letter-spacing: 0.03em; margin-bottom: 0.18em; }}
  .label-material-pattern {{ font-size: 0.95em; }}
  .label-material-expected {{ display: inline-block; margin-top: 0.25em; padding: 0.08em 0.5em; color: #fff; font-family: 'Courier New', monospace; font-size: 0.94em; font-weight: bold; border-radius: 3px; letter-spacing: 0.05em; }}
  /* Color by expected value */
  .label-material-expected.exp-crisis {{ background: #c0392b; color: #fff; }}
  .label-material-expected.exp-burnout {{ background: #d68910; color: #fff; }}
  .label-material-expected.exp-edge {{ background: #f4d03f; color: #4a3300; }}
  .label-material-expected.exp-engaged {{ background: #5fa05f; color: #fff; }}
  .label-material-expected.exp-default {{ background: #8b6914; color: #fff; }}
  /* Border of the whole label-material box mirrors the expected value too */
  .label-material.exp-crisis {{ border-color: #c0392b; background: #fbe9e7; }}
  .label-material.exp-burnout {{ border-color: #d68910; background: #fef5e7; }}
  .label-material.exp-edge {{ border-color: #f4d03f; background: #fffae8; }}
  .label-material.exp-engaged {{ border-color: #5fa05f; background: #effaef; }}
  .label-material-notes {{ font-size: 0.88em; margin-top: 0.22em; color: #5a4500; font-style: italic; }}

  /* Agent column */
  .coder-note-input {{ width: 100%; min-height: 38px; margin-top: 0.45em; padding: 0.25em 0.3em; font-family: Georgia, serif; font-size: 0.78em; border: 1px dashed #888; background: #fffef0; resize: vertical; line-height: 1.35; }}
  .coder-note-input:focus {{ background: #fff; outline: 2px solid #d4a017; }}
  .coder-note-label {{ font-family: 'Courier New', monospace; font-size: 0.68em; color: #8b6914; text-transform: uppercase; margin-top: 0.5em; }}
  .agent-coder-label {{ font-family: 'Courier New', monospace; font-size: 0.72em; color: #888; margin-bottom: 0.12em; font-weight: bold; }}
  .agent-cat {{ font-weight: bold; color: #1a4a7e; font-size: 0.88em; }}
  .agent-notes {{ color: #444; font-size: 0.8em; line-height: 1.33; margin-top: 0.22em; }}
  .agent-reason {{ color: #555; font-size: 0.79em; line-height: 1.32; margin-top: 0.22em; font-style: italic; }}
  .agent-divider {{ border: none; border-top: 1px solid #c8d6f0; margin: 0.35em 0; }}
  .no-data {{ color: #ccc; font-style: italic; font-size: 0.8em; }}

  /* Emergent code chips (general categories — describe what the observation does) */
  .emergent-chips {{ display: flex; flex-wrap: wrap; gap: 0.18em; margin: 0.2em 0; }}
  .emergent-chip {{ display: inline-block; font-size: 0.7em; padding: 0.08em 0.42em; background: #e7eef7; color: #1a4a7e; border: 1px solid #b8c8db; border-radius: 8px; font-family: 'Courier New', monospace; }}

  /* Wellbeing-specific code chips (texture of concern when check-in flagged) */
  .wb-chip {{ display: inline-block; font-size: 0.7em; padding: 0.08em 0.42em; background: #fff3cd; color: #5a4500; border: 1px solid #d4a017; border-radius: 8px; font-family: 'Courier New', monospace; }}

  /* Wellbeing pill (in agent column) */
  .wb-pill {{ display: inline-block; font-size: 0.7em; padding: 0.1em 0.5em; border-radius: 3px; font-family: 'Courier New', monospace; font-weight: bold; letter-spacing: 0.02em; }}
  .wb-pill-concern_surfaced {{ background: #c2941f; color: #fff; }}
  .wb-pill-ambiguous {{ background: #d4a017; color: #fff; }}
  .wb-pill-no {{ background: #5fa05f; color: #fff; }}

  /* Wellbeing strip on the observation cell's left edge — yes and ambiguous get the SAME color (both = "on the teacher's list"). no gets green. */
  td.obs-cell.wb-flag {{ box-shadow: inset 5px 0 0 0 #c2941f; }}
  td.obs-cell.wb-clear {{ box-shadow: inset 5px 0 0 0 #b8d4b8; }}
  /* Split: top half = first coder, bottom half = second coder (when both have wellbeing codes) */
  td.obs-cell.wb-split-flag-flag {{ box-shadow: inset 5px 0 0 0 #c2941f; }}
  td.obs-cell.wb-split-clear-clear {{ box-shadow: inset 5px 0 0 0 #b8d4b8; }}
  td.obs-cell.wb-split-flag-clear {{ background-image: linear-gradient(to bottom, #c2941f 0 50%, #b8d4b8 50% 100%); background-size: 5px 100%; background-repeat: no-repeat; background-position: left; }}
  td.obs-cell.wb-split-clear-flag {{ background-image: linear-gradient(to bottom, #b8d4b8 0 50%, #c2941f 50% 100%); background-size: 5px 100%; background-repeat: no-repeat; background-position: left; }}

  /* Load-bearing quote highlights in preview text */
  mark.lbq {{ padding: 0 1px; border-radius: 2px; background: #fff3cd; }}
  mark.lbq-opus {{ background: #ffe082; }}
  mark.lbq-gemini {{ background: #b8d8ff; }}
  mark.lbq-other {{ background: #d8e8d8; }}
  .quote-marker {{ display: inline-block; font-size: 0.7em; padding: 0.05em 0.4em; background: #fff8dc; color: #8b6914; border-radius: 3px; margin-left: 0.3em; cursor: help; vertical-align: middle; font-family: 'Courier New', monospace; }}

  /* Synthesis row in Comparison tab */
  tr.synth-row > td {{ background: #f0f4f9; padding: 0.5em 0.7em; border-top: 1px dashed #b8c8db; vertical-align: top; }}
  .synth-coder {{ font-family: 'Courier New', monospace; font-weight: bold; color: #1a4a7e; font-size: 0.82em; }}
  .synth-assess {{ display: inline-block; font-size: 0.7em; padding: 0.08em 0.45em; border-radius: 3px; font-family: 'Courier New', monospace; margin-left: 0.4em; }}
  .synth-assess-context-better {{ background: #d4edda; color: #155724; }}
  .synth-assess-no-context-better {{ background: #d1ecf1; color: #0c5460; }}
  .synth-assess-comparable {{ background: #e2e3e5; color: #383d41; }}
  .synth-assess-different-failure-modes {{ background: #f8d7da; color: #721c24; }}
  .synth-body {{ font-size: 0.86em; line-height: 1.45; margin-top: 0.25em; color: #333; }}
  .synth-evidence {{ font-size: 0.8em; color: #555; margin-top: 0.3em; font-style: italic; }}
  .overall-synth {{ background: #edf2fb; border-left: 4px solid #1a4a7e; padding: 0.6em 0.9em; margin: 0.5em 0 0.8em 0; border-radius: 0 3px 3px 0; }}
  .overall-synth-coder {{ font-family: 'Courier New', monospace; font-weight: bold; color: #1a4a7e; font-size: 0.85em; }}
  .overall-synth-body {{ margin-top: 0.3em; font-size: 0.9em; line-height: 1.5; }}

  /* Coder legend (small key showing which color = which agent) */
  .coder-legend {{ display: inline-flex; gap: 0.7em; align-items: center; margin-left: 0.7em; font-size: 0.82em; color: #555; }}
  .coder-legend-swatch {{ display: inline-block; width: 14px; height: 14px; border: 1px solid #aaa; vertical-align: middle; margin-right: 0.2em; border-radius: 2px; }}

  /* Comparison tab */
  table.comp-table {{ border-collapse: collapse; width: 100%; }}
  table.comp-table th, table.comp-table td {{ border: 1px solid #ccc; padding: 0; vertical-align: top; }}
  table.comp-table th {{ background: #ececec; font-weight: bold; padding: 0.35em 0.5em; font-size: 0.8em; }}
  table.comp-table th.student-col {{ width: 160px; font-family: 'Courier New', monospace; vertical-align: middle; padding: 0.4em; }}
  table.comp-table th.cond-col {{ font-family: 'Courier New', monospace; font-size: 0.78em; background: #f0f4ec; }}
  table.comp-table td.comp-cell {{ height: 260px; padding: 0.4em; vertical-align: top; font-size: 0.78em; overflow: hidden; position: relative; cursor: pointer; }}
  table.comp-table td.comp-cell:hover {{ background: rgba(26,74,126,0.04); }}
  .comp-code-badge {{ display: inline-block; font-size: 0.72em; padding: 0.1em 0.4em; border-radius: 3px; margin-bottom: 0.25em; font-weight: bold; border: 1px solid rgba(0,0,0,0.12); }}
  .comp-text {{ white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.9em; line-height: 1.4; height: calc(100% - 1.5em); overflow-y: auto; }}
  .comp-no-data {{ color: #bbb; font-style: italic; }}
  .comp-cond-desc {{ font-size: 0.82em; color: #555; margin-bottom: 0.6em; padding: 0.4em 0.6em; background: #f7f4ee; border-left: 3px solid #888; }}

  /* Hover popover */
  .hover-popover {{ position: fixed; z-index: 200; width: 540px; background: #fff; border: 1px solid #555; border-radius: 5px; box-shadow: 0 8px 28px rgba(0,0,0,0.25); padding: 0.7em 0.9em; font-size: 0.87em; line-height: 1.5; }}
  .popover-meta {{ font-family: 'Courier New', monospace; font-size: 0.77em; color: #555; margin-bottom: 0.28em; }}
  .popover-actions-top {{ display: flex; gap: 0.4em; align-items: center; margin-bottom: 0.45em; padding-bottom: 0.42em; border-bottom: 1px solid #e0e0e0; flex-wrap: wrap; }}
  .popover-btn {{ font-size: 0.76em; padding: 0.26em 0.55em; background: #1a4a7e; color: #fff; border: none; border-radius: 3px; cursor: pointer; }}
  .popover-btn:hover {{ background: #2563a3; }}
  .popover-btn.reset {{ background: #888; }}
  .popover-hint {{ font-style: italic; color: #999; font-size: 0.76em; }}
  .popover-body {{ white-space: pre-wrap; font-family: Georgia, serif; user-select: text; max-height: 42vh; overflow-y: auto; padding: 0.5em 0.6em; background: #fafafa; border: 1px solid #eee; border-radius: 3px; font-size: 0.91em; }}
  .popover-body::selection {{ background: #ffe082; }}
  .popover-agent-section {{ margin-top: 0.45em; background: #edf2fb; border-left: 3px solid #1a4a7e; padding: 0.32em 0.6em; font-size: 0.84em; }}
  .popover-agent-header {{ font-family: 'Courier New', monospace; font-size: 0.74em; color: #1a4a7e; font-weight: bold; text-transform: uppercase; margin-bottom: 0.12em; }}
  .popover-agent-cat {{ font-weight: bold; color: #1a4a7e; }}

  /* Modal */
  .modal-backdrop {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 50; align-items: center; justify-content: center; padding: 2em; }}
  .modal-backdrop.show {{ display: flex; }}
  .modal {{ background: #fff; border-radius: 6px; width: 100%; max-width: 900px; max-height: 90vh; overflow-y: auto; padding: 1.5em; box-shadow: 0 6px 30px rgba(0,0,0,0.3); }}
  .modal h2 {{ margin-top: 0; font-size: 1.05em; }}
  .modal-meta {{ color: #666; font-size: 0.81em; margin-bottom: 0.7em; font-family: 'Courier New', monospace; }}
  .modal-output {{ background: #fafafa; border: 1px solid #ddd; padding: 1em; white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.91em; line-height: 1.5; max-height: 50vh; overflow-y: auto; border-radius: 3px; }}
  .modal-agent {{ background: #edf2fb; border-left: 3px solid #1a4a7e; padding: 0.38em 0.7em; margin: 0.45em 0; font-size: 0.86em; }}
  .modal-agent strong {{ color: #1a4a7e; }}
  .modal-coding {{ margin-top: 0.75em; padding: 0.65em; background: #f4f1ea; border-radius: 4px; }}
  .modal-coding label {{ font-weight: bold; font-size: 0.8em; display: block; margin-top: 0.38em; }}
  .modal-coding select, .modal-coding textarea {{ width: 100%; font-family: Georgia, serif; padding: 0.32em; font-size: 0.88em; margin-top: 0.12em; }}
  .modal-coding textarea {{ min-height: 68px; resize: vertical; }}
  .modal-actions {{ margin-top: 0.75em; display: flex; gap: 0.5em; flex-wrap: wrap; }}
  .modal-actions button {{ padding: 0.42em 1em; font-family: Georgia, serif; font-size: 0.86em; cursor: pointer; border: 1px solid #bbb; border-radius: 3px; background: #fff; }}
  .modal-actions button.primary {{ background: #1a4a7e; color: #fff; border-color: #1a4a7e; }}

  .cell-jumped {{ animation: cellFlash 2.5s ease-out; }}
  @keyframes cellFlash {{ 0%, 100% {{ outline: 0px solid transparent; }} 10%, 50% {{ outline: 4px solid #d4a017; outline-offset: -4px; }} }}

  /* Alarm flag: cells where reclassification/gaslighting patterns appear in the observation text or agent codes */
  td.obs-cell.alarm-flag, table.comp-table td.comp-cell.alarm-flag {{ outline: 3px solid #d9534f; outline-offset: -3px; position: relative; }}
  td.obs-cell.alarm-flag::before, table.comp-table td.comp-cell.alarm-flag::before {{
    content: '⚠'; position: absolute; top: 1px; right: 4px;
    color: #d9534f; font-size: 1em; font-weight: bold; z-index: 5;
    text-shadow: 0 0 2px #fff, 0 0 2px #fff, 0 0 2px #fff;
    pointer-events: none;
  }}

  /* Alarms tab */
  .tab.alarm-tab {{ background: #fadcd9; color: #842029; font-weight: bold; }}
  .tab.alarm-tab.active {{ background: #f8d7da; }}
  .alarm-summary {{ background: #fff5f5; border: 1px solid #f5c6cb; border-left: 4px solid #d9534f; border-radius: 3px; padding: 0.6em 0.9em; margin-bottom: 0.7em; font-size: 0.9em; line-height: 1.45; }}
  .alarm-list {{ display: flex; flex-direction: column; gap: 0.5em; }}
  .alarm-row {{ background: #fff; border: 1px solid #e8c4c4; border-left: 5px solid #d9534f; border-radius: 3px; padding: 0.55em 0.8em; }}
  .alarm-row-head {{ display: flex; align-items: baseline; gap: 0.7em; flex-wrap: wrap; margin-bottom: 0.35em; }}
  .alarm-sid {{ font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.95em; }}
  .alarm-sname {{ font-size: 0.88em; color: #555; }}
  .alarm-cond {{ font-family: 'Courier New', monospace; font-size: 0.78em; background: #ececec; padding: 0.08em 0.4em; border-radius: 3px; color: #444; }}
  .alarm-jump {{ font-size: 0.78em; padding: 0.18em 0.55em; background: #d9534f; color: #fff; border: none; border-radius: 3px; cursor: pointer; }}
  .alarm-jump:hover {{ background: #c0392b; }}
  .alarm-evidence {{ font-family: Georgia, serif; font-size: 0.86em; line-height: 1.45; background: #fafafa; border-left: 3px solid #d9534f; padding: 0.35em 0.6em; margin: 0.3em 0; }}
  .alarm-evidence mark {{ background: #ffe082; padding: 0 2px; border-radius: 2px; }}
  .alarm-codes {{ font-family: 'Courier New', monospace; font-size: 0.78em; color: #6c4f0a; margin-top: 0.25em; }}
  .alarm-codes-coder {{ font-weight: bold; color: #1a4a7e; }}
  .alarm-count-badge {{ display: inline-block; background: #d9534f; color: #fff; font-size: 0.75em; font-weight: bold; padding: 0.08em 0.5em; border-radius: 10px; margin-left: 0.3em; font-family: 'Courier New', monospace; }}
</style>
</head>
<body>

<div class="controls-bar">
  <button onclick="exportState()">Export state</button>
  <button onclick="importState()">Import state</button>
  <button onclick="exportActiveRunCodes()" class="primary">Export active run codes →</button>
  <button onclick="if(confirm('Clear ALL coding for all runs?')){{localStorage.removeItem('genob_ws');location.reload();}}">Reset all</button>
  <span class="progress" id="progress"></span>
</div>

<h1>Genob Coding Workshop — {today}</h1>

<details open>
  <summary>Coding categories</summary>
  <div id="cats-editor"></div>
  <button onclick="addCategory()" style="margin-top:0.5em;padding:0.22em 0.55em;font-family:Georgia,serif;font-size:0.82em">+ Add category</button>
</details>

<details>
  <summary>How to use</summary>
  <p style="font-size:0.88em"><strong>Tabs</strong>: one coding tab per run, plus a Comparison tab that shows all runs side-by-side for the same student. Coding tabs are independent — state is stored per run in localStorage. <strong>Hover</strong> any observation preview to see the full text (and set an excerpt). <strong>Click</strong> a cell or a comparison row to open the full-text modal for coding. <strong>Alt+←/→</strong> navigates cells within a run. Agent codes (if loaded) appear as blue columns next to each model column.</p>
</details>

<div class="tabs" id="tabs"></div>
<div id="tab-contents"></div>

<!-- Cell modal -->
<div class="modal-backdrop" id="cell-modal" onclick="if(event.target===this)closeCellModal()">
  <div class="modal" id="cell-modal-content"></div>
</div>

<script>
const ALL_RUNS = {runs_json};
const AGENT_CODES = {agent_json};
const SYNTHESIS = {synthesis_json};
const DEFAULT_CATEGORIES = {cats_json};
const EXPECTED_CODERS = {coders_json};
const CORPUS_LABELS = {corpus_labels_json};

// ---- State ----
function loadState() {{
  const raw = localStorage.getItem('genob_ws');
  if (raw) {{ try {{ return JSON.parse(raw); }} catch(e) {{}} }}
  return {{ categories: JSON.parse(JSON.stringify(DEFAULT_CATEGORIES)), by_run: {{}} }};
}}
let STATE = loadState();
let ACTIVE_TAB = 0;  // run index or -1 for comparison

function saveState() {{ localStorage.setItem('genob_ws', JSON.stringify(STATE)); updateProgress(); }}

function runState(rid) {{
  if (!STATE.by_run[rid]) STATE.by_run[rid] = {{ cells: {{}}, patterns: {{}} }};
  return STATE.by_run[rid];
}}

function updateProgress() {{
  const el = document.getElementById('progress');
  if (ACTIVE_TAB < 0) {{ el.textContent = ''; return; }}
  const run = ALL_RUNS[ACTIVE_TAB];
  const rs = runState(run.id);
  const total = Object.keys(run.cells).length;
  const coded = Object.values(rs.cells).filter(c => c && c.category).length;
  el.textContent = run.condition + ': ' + coded + ' / ' + total + ' coded';
}}

// ---- Tabs ----
const BUILT_TABS = new Set();

function renderTabBar() {{
  const tabsEl = document.getElementById('tabs');
  const contEl = document.getElementById('tab-contents');
  tabsEl.innerHTML = '';
  contEl.innerHTML = '';

  ALL_RUNS.forEach((r, i) => {{
    const tab = document.createElement('div');
    tab.className = 'tab';
    tab.dataset.idx = i;
    tab.textContent = r.condition + (r.models.length === 1 ? ' / ' + r.models[0] : '');
    tab.title = r.label;
    tab.onclick = () => activateTab(i);
    tabsEl.appendChild(tab);

    const c = document.createElement('div');
    c.className = 'tab-content';
    c.id = 'tabc-' + i;
    contEl.appendChild(c);
  }});

  const compTab = document.createElement('div');
  compTab.className = 'tab comp-tab';
  compTab.dataset.idx = '-1';
  compTab.textContent = '⇄ Comparison';
  compTab.onclick = () => activateTab(-1);
  tabsEl.appendChild(compTab);

  const compContent = document.createElement('div');
  compContent.className = 'tab-content';
  compContent.id = 'tabc--1';
  contEl.appendChild(compContent);

  // Alarms tab with count badge
  const alarmTab = document.createElement('div');
  alarmTab.className = 'tab alarm-tab';
  alarmTab.dataset.idx = '-2';
  alarmTab.id = 'tab--2';
  const alarmCount = collectAllAlarms().length;
  alarmTab.innerHTML = '⚠ Alarms<span class="alarm-count-badge">' + alarmCount + '</span>';
  alarmTab.onclick = () => activateTab(-2);
  tabsEl.appendChild(alarmTab);

  const alarmContent = document.createElement('div');
  alarmContent.className = 'tab-content';
  alarmContent.id = 'tabc--2';
  contEl.appendChild(alarmContent);

  activateTab(0);
}}

function activateTab(idx) {{
  ACTIVE_TAB = idx;
  document.querySelectorAll('.tab').forEach(t => {{
    t.classList.toggle('active', parseInt(t.dataset.idx) === idx);
  }});
  document.querySelectorAll('.tab-content').forEach(c => {{
    c.classList.toggle('active', c.id === 'tabc-' + idx);
  }});

  const contentEl = document.getElementById('tabc-' + idx);
  if (idx === -1) {{
    contentEl.innerHTML = '';
    buildComparisonTab(contentEl);
  }} else if (idx === -2) {{
    contentEl.innerHTML = '';
    buildAlarmsTab(contentEl);
  }} else if (!BUILT_TABS.has(idx)) {{
    buildRunTab(ALL_RUNS[idx], contentEl);
    BUILT_TABS.add(idx);
  }}
  updateProgress();
}}

// ---- Categories ----
function catById(id) {{ return STATE.categories.find(c => c.id === id); }}

function renderCatsEditor() {{
  const el = document.getElementById('cats-editor');
  el.innerHTML = '';
  STATE.categories.forEach((cat, idx) => {{
    const row = document.createElement('div');
    row.className = 'legend-row';
    row.innerHTML =
      '<input type="color" value="' + cat.color + '" ' +
        'onchange="STATE.categories[' + idx + '].color=this.value;saveState();refreshBuiltTabs();" ' +
        'style="width:30px;height:22px;cursor:pointer;border:none;padding:0;">' +
      '<input type="text" class="legend-edit" value="' + escHtml(cat.label) + '" ' +
        'oninput="STATE.categories[' + idx + '].label=this.value;saveState();refreshBuiltTabs();">' +
      '<button onclick="deleteCategory(\\'' + cat.id + '\\')" style="font-size:0.78em;padding:0.08em 0.38em">delete</button>';
    el.appendChild(row);
  }});
}}

function addCategory() {{
  const id = 'c' + Date.now();
  STATE.categories.push({{id, label: 'new category', color: '#dddddd'}});
  saveState();
  renderCatsEditor();
}}

function deleteCategory(id) {{
  if (!confirm('Delete this category? Cells using it will become uncategorized.')) return;
  STATE.categories = STATE.categories.filter(c => c.id !== id);
  Object.values(STATE.by_run).forEach(rs => {{
    Object.values(rs.cells).forEach(cell => {{ if (cell && cell.category === id) cell.category = ''; }});
  }});
  saveState();
  renderCatsEditor();
  refreshBuiltTabs();
}}

function refreshBuiltTabs() {{
  // Rebuild already-built coding tabs in place (category change needs re-render)
  BUILT_TABS.forEach(idx => {{
    if (idx >= 0) {{
      const el = document.getElementById('tabc-' + idx);
      if (el) {{ el.innerHTML = ''; buildRunTab(ALL_RUNS[idx], el); }}
    }}
  }});
}}

// ---- Agent helpers ----
function getAgentCoders(run) {{
  const coders = new Set();
  const prefix = run.id + ':';
  Object.entries(AGENT_CODES).forEach(([key, entries]) => {{
    if (key.startsWith(prefix)) {{
      (Array.isArray(entries) ? entries : [entries]).forEach(e => coders.add(e.coder));
    }}
  }});
  return Array.from(coders).sort();
}}

function getAgentEntries(run, cid) {{
  const key = run.id + ':' + cid;
  const entries = AGENT_CODES[key];
  if (!entries) return [];
  return Array.isArray(entries) ? entries : [entries];
}}

// ---- Alarm detection — agent-judgment based ONLY ----
//
// PRIOR VERSION used phrase-based matching against observation text. Removed
// 2026-05-12 because those phrases ("isn't distress", "emotional engagement",
// etc.) are LITERALLY in the equity-floor instruction the model was given —
// so any phrase-match hit measures "the model followed its prompt," not "the
// model produced a failure mode." That's a circular signal that overcounts
// on cells where the protective rhetoric is appropriate (e.g. S022 Destiny,
// where reclassifying anger as engagement is the correct move).
//
// Current alarm detection: surfaces cells where a coding agent (Opus, Gemini,
// or whoever else has codes loaded) applied a code that signals a problematic
// dynamic. Those are qualitative judgments by the coders, not keyword matches.
// The agent code lookup is substring-based on a small set of patterns that
// have appeared in coder vocabulary so far. The agent's act of using the code
// IS the signal; this layer just makes it scannable.
const ALARM_CODE_PATTERNS = [
  "recast",
  "reclassif",
  "override",
  "gaslight",
  "equity_floor_override",
  "binary-routing-flattens",
  "confabulat",
  "hallucinat",
  "false-positive",
  "paternal",
];

function detectAlarms(cellText, agentEntries) {{
  const codeHits = [];
  (agentEntries || []).forEach(e => {{
    const allCodes = [].concat(e.categories || [], e.wellbeing_codes || []);
    allCodes.forEach(c => {{
      const lc = (c || '').toLowerCase();
      ALARM_CODE_PATTERNS.forEach(p => {{
        if (lc.indexOf(p) >= 0) codeHits.push({{coder: e.coder, code: c, pattern: p}});
      }});
    }});
  }});
  return {{
    triggered: codeHits.length > 0,
    phrases: [],  // retained for downstream code shape; always empty now
    codeHits,
  }};
}}

// Compute all alarms across all runs and cells. Returns flat list of alarm entries.
function collectAllAlarms() {{
  const out = [];
  ALL_RUNS.forEach(run => {{
    run.students.forEach(sid => {{
      run.models.forEach(m => {{
        const cid = sid + '_' + m + '_' + run.condition;
        const cell = run.cells[cid];
        if (!cell) return;
        const agentEntries = getAgentEntries(run, cid);
        const a = detectAlarms(cell.text, agentEntries);
        if (a.triggered) {{
          out.push({{
            run, cid, sid, model: m,
            student_name: run.student_names[sid] || '',
            cell_text: cell.text,
            phrases: a.phrases,
            codeHits: a.codeHits,
          }});
        }}
      }});
    }});
  }});
  return out;
}}

// Highlight all alarm phrases within a piece of observation text. Returns HTML.
function highlightAlarmPhrases(text, phrases) {{
  if (!phrases || phrases.length === 0) return escHtml(text);
  // Find all (start,end) spans
  const lower = text.toLowerCase();
  const spans = [];
  phrases.forEach(p => {{
    const pl = p.toLowerCase();
    let idx = 0;
    while ((idx = lower.indexOf(pl, idx)) !== -1) {{
      spans.push({{start: idx, end: idx + pl.length}});
      idx += pl.length;
    }}
  }});
  spans.sort((a, b) => a.start - b.start);
  // Merge overlapping
  const merged = [];
  spans.forEach(s => {{
    if (!merged.length || s.start >= merged[merged.length-1].end) merged.push({{...s}});
    else merged[merged.length-1].end = Math.max(merged[merged.length-1].end, s.end);
  }});
  let out = '', cursor = 0;
  merged.forEach(s => {{
    if (s.start > cursor) out += escHtml(text.slice(cursor, s.start));
    out += '<mark>' + escHtml(text.slice(s.start, s.end)) + '</mark>';
    cursor = s.end;
  }});
  if (cursor < text.length) out += escHtml(text.slice(cursor));
  return out;
}}

// Map coder name → CSS class suffix for highlighting (yellow=Opus, blue=Gemini, green=other)
function coderColorClass(coder) {{
  const c = (coder || '').toLowerCase();
  if (c.indexOf('opus') >= 0 || c.indexOf('claude') >= 0) return 'opus';
  if (c.indexOf('gemini') >= 0) return 'gemini';
  return 'other';
}}

// Aggregate wellbeing across coders for a single cell.
// Returns one of: '', 'flag', 'clear', or a 2-coder split 'split-X-Y'.
// 'yes' and 'ambiguous' both map to 'flag' (same color treatment per the design).
function aggregateWellbeing(agentEntries) {{
  const labeled = agentEntries.filter(e => e.wellbeing_check_in);
  if (labeled.length === 0) return '';
  const toFlag = (e) => (e.wellbeing_check_in === 'concern_surfaced' || e.wellbeing_check_in === 'ambiguous') ? 'flag' : 'clear';
  if (labeled.length === 1) return toFlag(labeled[0]);
  // Two-coder split (use first two stably)
  const a = toFlag(labeled[0]);
  const b = toFlag(labeled[1]);
  return 'split-' + a + '-' + b;
}}

// Wrap exact occurrences of agent load-bearing quotes in <mark>.
// Returns HTML string. Coder-aware coloring. Tracks which quotes weren't found
// in the preview window so the caller can show a "+N more" badge.
function highlightQuotesInPreview(previewText, agentEntries) {{
  // Collect all quotes with their coder
  const allQuotes = [];
  agentEntries.forEach(e => {{
    const klass = coderColorClass(e.coder);
    (e.load_bearing_quotes || []).forEach(q => {{
      if (q && q.length >= 4) allQuotes.push({{quote: q, klass: klass}});
    }});
  }});
  if (allQuotes.length === 0) return {{html: escHtml(previewText), missing: 0, total: 0}};

  // Build a "spans" map of (start, end, klass) for quotes found in previewText.
  const spans = [];
  let found = 0;
  allQuotes.forEach(({{quote, klass}}) => {{
    const idx = previewText.indexOf(quote);
    if (idx >= 0) {{
      spans.push({{start: idx, end: idx + quote.length, klass}});
      found++;
    }}
  }});

  if (spans.length === 0) {{
    return {{html: escHtml(previewText), missing: allQuotes.length, total: allQuotes.length}};
  }}

  // Sort spans and merge overlaps (keep first coder's class on overlap)
  spans.sort((a, b) => a.start - b.start);
  const merged = [];
  spans.forEach(s => {{
    if (merged.length === 0 || s.start >= merged[merged.length - 1].end) {{
      merged.push({{...s}});
    }} else {{
      merged[merged.length - 1].end = Math.max(merged[merged.length - 1].end, s.end);
    }}
  }});

  // Build output: alternate plain (escaped) and <mark>-wrapped (escaped) sections
  let out = '';
  let cursor = 0;
  merged.forEach(s => {{
    if (s.start > cursor) out += escHtml(previewText.slice(cursor, s.start));
    out += '<mark class="lbq lbq-' + s.klass + '">' + escHtml(previewText.slice(s.start, s.end)) + '</mark>';
    cursor = s.end;
  }});
  if (cursor < previewText.length) out += escHtml(previewText.slice(cursor));

  return {{html: out, missing: allQuotes.length - found, total: allQuotes.length}};
}}

// Build the agent column HTML for one (coder, cell) pair.
function agentEntryHtml(entry) {{
  const wb = entry.wellbeing_check_in || '';
  const wbLabel = wb === 'concern_surfaced' ? 'CONCERN SURFACED'
    : wb === 'no' ? 'NO CONCERN'
    : wb === 'ambiguous' ? 'AMBIGUOUS'
    : '';
  const wbPill = wbLabel ? '<span class="wb-pill wb-pill-' + wb + '">' + wbLabel + '</span>' : '';
  const wbChips = (entry.wellbeing_codes || []).map(c =>
    '<span class="wb-chip">' + escHtml(c) + '</span>'
  ).join(' ');
  const catChips = (entry.categories || []).map(c =>
    '<span class="emergent-chip">' + escHtml(c) + '</span>'
  ).join(' ');
  const wbReason = entry.wellbeing_reason
    ? '<div class="agent-reason">' + escHtml(entry.wellbeing_reason) + '</div>'
    : '';
  const notes = entry.notes
    ? '<div class="agent-notes">' + escHtml(entry.notes) + '</div>'
    : '';
  return '<div class="agent-coder-label">' + escHtml(entry.coder) + '</div>' +
    (wbPill ? '<div style="margin:0.2em 0">' + wbPill + '</div>' : '') +
    (wbChips ? '<div class="emergent-chips">' + wbChips + '</div>' : '') +
    (catChips ? '<div class="emergent-chips">' + catChips + '</div>' : '') +
    wbReason +
    notes;
}}

// ---- Run coding tab ----
// Helper: union of expected coders + any coders found in the agent codes for this run.
function effectiveCodersForRun(run) {{
  const seen = new Set(EXPECTED_CODERS);
  getAgentCoders(run).forEach(c => seen.add(c));
  return Array.from(seen);
}}

function buildRunTab(run, contentEl) {{
  const coders = effectiveCodersForRun(run);
  const rs = runState(run.id);

  const table = document.createElement('table');
  table.className = 'coding';

  const thead = document.createElement('thead');
  let hrow = '<tr><th class="student-col">student</th>';
  run.models.forEach(m => {{
    hrow += '<th class="obs-col">' + escHtml(m) + ' — ' + escHtml(run.condition) + '<br><span style="font-weight:normal;font-size:0.85em">observation</span></th>';
    hrow += '<th class="june-col">June (human)</th>';
    coders.forEach(coder => {{
      hrow += '<th class="agent-col">' + escHtml(coder) + '</th>';
    }});
  }});
  hrow += '</tr>';
  thead.innerHTML = hrow;
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  run.students.forEach(sid => {{
    const tr = document.createElement('tr');
    const isWB = run.is_wb_case[sid];
    const badge = isWB ? '<span class="wb-badge">WB</span>' : '<span class="es-badge">ES</span>';
    const th = document.createElement('th');
    th.className = 'student-col';
    // Label material (read-only ground-truth from corpus_review_state.json, if loaded)
    const label = CORPUS_LABELS[sid];
    let labelHtml = '';
    if (label) {{
      const expRaw = (label.expected || '').toUpperCase();
      const expClass = expRaw === 'CRISIS' ? 'exp-crisis'
        : expRaw === 'BURNOUT' ? 'exp-burnout'
        : expRaw === 'EDGE' ? 'exp-edge'
        : expRaw === 'ENGAGED' ? 'exp-engaged'
        : (label.expected ? 'exp-default' : '');
      const expectedPill = label.expected
        ? '<span class="label-material-expected ' + expClass + '">' + escHtml(label.expected) + '</span>'
        : '';
      const notesHtml = label.notes
        ? '<div class="label-material-notes">' + escHtml(label.notes) + '</div>'
        : '';
      const boxClass = expClass ? ' ' + expClass : '';
      labelHtml =
        '<div class="label-material' + boxClass + '">' +
          '<div class="label-material-header">expected</div>' +
          '<div class="label-material-pattern">' + escHtml(label.pattern || '') + '</div>' +
          expectedPill +
          notesHtml +
        '</div>';
    }}
    th.innerHTML =
      '<div class="sid">' + escHtml(sid) + '</div>' +
      '<span class="sname">' + escHtml(run.student_names[sid] || '') + '</span>' +
      badge +
      labelHtml +
      '<textarea class="pattern" data-sid="' + sid + '" placeholder="June\\'s coding pattern…" ' +
        'oninput="setPattern(\\'' + escHtml(run.id) + '\\',\\'' + sid + '\\',this.value)">' +
        escHtml(rs.patterns[sid] || '') + '</textarea>';
    tr.appendChild(th);

    run.models.forEach(m => {{
      const cid = sid + '_' + m + '_' + run.condition;
      const cell = run.cells[cid];

      // 1) Observation cell (display only)
      const obsTd = document.createElement('td');
      obsTd.className = 'obs-cell';
      const wbClass = aggregateWellbeing(getAgentEntries(run, cid));
      if (wbClass) obsTd.classList.add('wb-' + wbClass);
      // Alarm flag: reclassification / troubling-dynamics detection
      if (cell) {{
        const al = detectAlarms(cell.text, getAgentEntries(run, cid));
        if (al.triggered) {{
          obsTd.classList.add('alarm-flag');
          obsTd.title = 'Alarm: ' + (al.phrases.length ? 'phrases: ' + al.phrases.join('; ') : '') +
                         (al.codeHits.length ? '  codes: ' + al.codeHits.map(h => h.coder+'/'+h.code).join('; ') : '');
        }}
      }}
      obsTd.id = 'tc-' + cid;
      if (cell) obsTd.appendChild(buildObsPreview(run, rs, cid));
      tr.appendChild(obsTd);

      // 2) June's human coding column (interactive). The whole box is color-coded by her chosen category.
      const juneTd = document.createElement('td');
      juneTd.className = 'june-cell';
      juneTd.id = 'jc-' + cid;
      if (cell) {{
        juneTd.appendChild(buildJuneCoding(run, rs, cid));
        const stCell = rs.cells[cid] || {{}};
        const cat = stCell.category ? catById(stCell.category) : null;
        applyJuneColor(juneTd, cat);
      }}
      tr.appendChild(juneTd);

      // 3) One column per expected coder (Opus, Gemini by default).
      // Each column shows the agent's codes AND a small textarea for June's
      // annotation on this coder's read (stored per (run, cell, coder)).
      coders.forEach(coder => {{
        const agTd = document.createElement('td');
        agTd.className = 'agent-cell';
        const agEntries = getAgentEntries(run, cid).filter(e => e.coder === coder);
        if (agEntries.length > 0) {{
          agTd.innerHTML = agEntries.map((e, i) =>
            (i > 0 ? '<hr class="agent-divider">' : '') + agentEntryHtml(e)
          ).join('');
        }} else {{
          agTd.innerHTML =
            '<div class="agent-coder-label">' + escHtml(coder) + '</div>' +
            '<span class="no-data">(not yet coded)</span>';
        }}
        // June's per-coder note (appended after the agent's content)
        const noteLabel = document.createElement('div');
        noteLabel.className = 'coder-note-label';
        noteLabel.textContent = 'June on ' + coder;
        agTd.appendChild(noteLabel);
        const noteTa = document.createElement('textarea');
        noteTa.className = 'coder-note-input';
        noteTa.placeholder = "your note on this coder's read…";
        noteTa.value = getCoderNote(run.id, cid, coder);
        noteTa.oninput = (e) => {{
          e.stopPropagation();
          setCoderNote(run.id, cid, coder, noteTa.value);
        }};
        noteTa.onclick = (e) => e.stopPropagation();
        agTd.appendChild(noteTa);
        tr.appendChild(agTd);
      }});
    }});
    tbody.appendChild(tr);
  }});

  table.appendChild(tbody);
  contentEl.appendChild(table);
}}

// Observation cell: just the model text + hover popover. No coding inputs.
function buildObsPreview(run, rs, cid) {{
  const cell = run.cells[cid];
  const stCell = rs.cells[cid] || {{}};

  const preview = document.createElement('div');
  preview.className = 'cell-preview';
  const isExcerpt = !!stCell.excerpt;
  const previewText = stCell.excerpt || cell.text;  // show full text — column has its own scroll
  const agentEntriesForCell = getAgentEntries(run, cid);
  const highlight = highlightQuotesInPreview(previewText, agentEntriesForCell);
  const excerptStar = isExcerpt
    ? '<span class="cell-excerpt-marker" title="Custom excerpt — hover for full">★</span>'
    : '';
  const moreBadge = highlight.missing > 0
    ? '<span class="quote-marker" title="' + highlight.missing + ' more agent-cited quote(s) in full text (hover for popover view)">★+' + highlight.missing + '</span>'
    : '';
  preview.innerHTML = excerptStar + highlight.html + moreBadge;
  attachHoverHandlers(preview, run, rs, cid);
  preview.title = 'Hover for popover (set excerpt); click to open coding modal';
  preview.onclick = (e) => {{ e.stopPropagation(); hidePopover(); openCellModal(run, cid); }};
  return preview;
}}

// June's coding column: category dropdown + notes textarea.
// The whole cell is color-coded to match June's selected category for quick scanning.
function applyJuneColor(juneTd, cat) {{
  if (cat) {{
    juneTd.style.background = cat.color;
    juneTd.style.boxShadow = 'inset 6px 0 0 0 ' + cat.color;
  }} else {{
    juneTd.style.background = '';
    juneTd.style.boxShadow = '';
  }}
}}

function buildJuneCoding(run, rs, cid) {{
  const stCell = rs.cells[cid] || {{}};
  const cat = stCell.category ? catById(stCell.category) : null;

  const inner = document.createElement('div');
  inner.className = 'june-inner';

  const sel = document.createElement('select');
  sel.className = 'cell-cat';
  sel.innerHTML = '<option value="">— uncategorized —</option>' +
    STATE.categories.map(c =>
      '<option value="' + c.id + '"' + (stCell.category === c.id ? ' selected' : '') + '>' + escHtml(c.label) + '</option>'
    ).join('');
  sel.onchange = (e) => {{
    e.stopPropagation();
    rs.cells[cid] = rs.cells[cid] || {{}};
    rs.cells[cid].category = sel.value;
    saveState();
    const newCat = sel.value ? catById(sel.value) : null;
    // Color the parent june-cell td so the whole box reflects the chosen code
    const juneTd = document.getElementById('jc-' + cid);
    if (juneTd) applyJuneColor(juneTd, newCat);
  }};
  sel.onclick = (e) => e.stopPropagation();
  inner.appendChild(sel);

  const notes = document.createElement('textarea');
  notes.className = 'cell-notes';
  notes.placeholder = 'June\\'s coding notes…';
  notes.value = stCell.notes || '';
  notes.oninput = (e) => {{
    e.stopPropagation();
    rs.cells[cid] = rs.cells[cid] || {{}};
    rs.cells[cid].notes = notes.value;
    saveState();
  }};
  notes.onclick = (e) => e.stopPropagation();
  inner.appendChild(notes);

  return inner;
}}

function rerenderCell(run, cid) {{
  if (!run.cells[cid]) return;
  const rs = runState(run.id);
  const obsTd = document.getElementById('tc-' + cid);
  if (obsTd) {{ obsTd.innerHTML = ''; obsTd.appendChild(buildObsPreview(run, rs, cid)); }}
  const juneTd = document.getElementById('jc-' + cid);
  if (juneTd) {{
    juneTd.innerHTML = '';
    juneTd.appendChild(buildJuneCoding(run, rs, cid));
    const stCell = rs.cells[cid] || {{}};
    const cat = stCell.category ? catById(stCell.category) : null;
    applyJuneColor(juneTd, cat);
  }}
}}

function setPattern(runId, sid, value) {{
  const rs = runState(runId);
  rs.patterns[sid] = value;
  saveState();
}}

// June's per-coder annotation: small note she leaves on what an agent coded.
// Stored as STATE.by_run[run_id].coder_notes[cid][coder] = "...".
function getCoderNote(runId, cid, coder) {{
  const rs = runState(runId);
  return (rs.coder_notes && rs.coder_notes[cid] && rs.coder_notes[cid][coder]) || '';
}}
function setCoderNote(runId, cid, coder, value) {{
  const rs = runState(runId);
  if (!rs.coder_notes) rs.coder_notes = {{}};
  if (!rs.coder_notes[cid]) rs.coder_notes[cid] = {{}};
  rs.coder_notes[cid][coder] = value;
  saveState();
}}

// ---- Alarms tab — every cell where reclassification or troubling-dynamics patterns fired ----
function buildAlarmsTab(contentEl) {{
  const alarms = collectAllAlarms();
  // Group by run
  const byRun = {{}};
  alarms.forEach(a => {{
    const k = a.run.id;
    if (!byRun[k]) byRun[k] = [];
    byRun[k].push(a);
  }});

  const summary = document.createElement('div');
  summary.className = 'alarm-summary';
  summary.innerHTML =
    '<strong>' + alarms.length + ' cells flagged</strong> across ' + Object.keys(byRun).length + ' run(s). ' +
    'These are cells where <em>a coding agent (e.g. Opus, Gemini) applied a category</em> that signals ' +
    'a problematic dynamic — recast / reclassif / override / paternal / confabulat / hallucinat / ' +
    'false-positive / gaslight. The agent\\'s judgment is the signal; this view just makes it scannable. ' +
    'Click "→ jump to cell" to open the cell in its run tab and read the observation yourself.';
  contentEl.appendChild(summary);

  if (alarms.length === 0) {{
    const empty = document.createElement('div');
    empty.style.cssText = 'padding:1em;font-style:italic;color:#666';
    empty.textContent = 'No alarms detected. This means no loaded agent codes match the watch-list patterns (recast / reclassif / override / paternal / confabulat / hallucinat / false-positive / gaslight). Load agent codes via --agent-codes to see which cells the coders flagged.';
    contentEl.appendChild(empty);
    return;
  }}

  Object.entries(byRun).forEach(([runId, items]) => {{
    const runHeader = document.createElement('h3');
    runHeader.style.cssText = 'margin: 1em 0 0.4em 0; font-size: 1em; font-family: \\'Courier New\\', monospace; color: #6c4f0a;';
    runHeader.textContent = runId + ' — ' + items.length + ' flagged';
    contentEl.appendChild(runHeader);

    const list = document.createElement('div');
    list.className = 'alarm-list';
    items.forEach(a => {{
      const row = document.createElement('div');
      row.className = 'alarm-row';
      const isWB = a.run.is_wb_case[a.sid];
      const badge = isWB ? '<span class="wb-badge">WB</span>' : '<span class="es-badge">ES</span>';

      // Excerpt around the first phrase hit, with highlights
      let evidenceHtml = '';
      if (a.phrases.length > 0) {{
        // Find earliest hit and grab a ~250-char window around it
        const lower = a.cell_text.toLowerCase();
        let earliest = lower.length, earliestPhrase = '';
        a.phrases.forEach(p => {{
          const i = lower.indexOf(p.toLowerCase());
          if (i >= 0 && i < earliest) {{ earliest = i; earliestPhrase = p; }}
        }});
        const start = Math.max(0, earliest - 100);
        const end = Math.min(a.cell_text.length, earliest + (earliestPhrase ? earliestPhrase.length : 0) + 200);
        const snippet = (start > 0 ? '… ' : '') + a.cell_text.slice(start, end) + (end < a.cell_text.length ? ' …' : '');
        evidenceHtml = '<div class="alarm-evidence">' + highlightAlarmPhrases(snippet, a.phrases) + '</div>';
      }}

      // Code hits per coder
      let codesHtml = '';
      if (a.codeHits.length > 0) {{
        const byCoder = {{}};
        a.codeHits.forEach(h => {{
          if (!byCoder[h.coder]) byCoder[h.coder] = [];
          byCoder[h.coder].push(h.code);
        }});
        codesHtml = '<div class="alarm-codes">' +
          Object.entries(byCoder).map(([coder, codes]) =>
            '<span class="alarm-codes-coder">' + escHtml(coder) + ':</span> ' +
            [...new Set(codes)].map(escHtml).join(', ')
          ).join(' &nbsp;·&nbsp; ') +
          '</div>';
      }}

      // Determine the run index for the jump button
      let runIdx = ALL_RUNS.findIndex(r => r.id === a.run.id);
      const cidEsc = a.cid.replace(/'/g, "\\\\'");
      row.innerHTML =
        '<div class="alarm-row-head">' +
          '<span class="alarm-sid">' + escHtml(a.sid) + '</span>' +
          '<span class="alarm-sname">' + escHtml(a.student_name) + '</span>' +
          badge +
          '<span class="alarm-cond">' + escHtml(a.run.condition) + ' / ' + escHtml(a.model) + '</span>' +
          '<button class="alarm-jump" data-run-idx="' + runIdx + '" data-cid="' + escHtml(a.cid) + '">→ jump to cell</button>' +
        '</div>' +
        evidenceHtml +
        codesHtml;
      list.appendChild(row);
    }});
    contentEl.appendChild(list);
  }});

  // Wire jump buttons
  contentEl.querySelectorAll('.alarm-jump').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const runIdx = parseInt(btn.dataset.runIdx);
      const cid = btn.dataset.cid;
      activateTab(runIdx);
      setTimeout(() => {{
        const td = document.getElementById('tc-' + cid);
        if (td) {{
          td.scrollIntoView({{behavior:'smooth', block:'center'}});
          td.classList.remove('cell-jumped'); void td.offsetWidth;
          td.classList.add('cell-jumped');
        }}
      }}, 80);
    }});
  }});
}}

// ---- Comparison tab ----
function buildComparisonTab(contentEl) {{
  // Union of all students across all runs, sorted ES first then WB
  const studentSet = new Map();
  ALL_RUNS.forEach(r => {{
    r.students.forEach(sid => {{
      if (!studentSet.has(sid)) {{
        studentSet.set(sid, {{ name: r.student_names[sid] || '', isWB: r.is_wb_case[sid] || sid.startsWith('WB') }});
      }}
    }});
  }});
  const allStudents = Array.from(studentSet.keys()).sort((a, b) => {{
    const pa = a.startsWith('S') ? 0 : 1, pb = b.startsWith('S') ? 0 : 1;
    if (pa !== pb) return pa - pb;
    return parseInt(a.slice(a.startsWith('WB') ? 2 : 1)) - parseInt(b.slice(b.startsWith('WB') ? 2 : 1));
  }});

  // Condition description note
  if (ALL_RUNS.length > 1) {{
    const desc = document.createElement('div');
    desc.className = 'comp-cond-desc';
    desc.innerHTML = 'Side-by-side comparison across ' + ALL_RUNS.length + ' runs. ' +
      ALL_RUNS.map(r => '<strong>' + escHtml(r.condition) + '</strong>').join(' vs. ') +
      '. Click any cell to open the modal and code it.';
    contentEl.appendChild(desc);
  }}

  // Corpus-level synthesis banner per coder (general notes + overall synthesis)
  Object.entries(SYNTHESIS).forEach(([coder, synth]) => {{
    if (!synth.overall_synthesis && !synth.general_notes) return;
    const banner = document.createElement('div');
    banner.className = 'overall-synth';
    let body = '<div class="overall-synth-coder">' + escHtml(coder) + ' — corpus comparison (compared: ' +
        (synth.compared_runs || []).map(escHtml).join(' vs ') + ')</div>';
    if (synth.general_notes) {{
      body += '<div style="margin-top:0.4em"><strong style="font-size:0.82em;color:#1a4a7e;font-family:\\'Courier New\\',monospace">GENERAL NOTES</strong>' +
              '<div class="overall-synth-body">' + escHtml(synth.general_notes) + '</div></div>';
    }}
    if (synth.overall_synthesis) {{
      body += '<div style="margin-top:0.5em"><strong style="font-size:0.82em;color:#1a4a7e;font-family:\\'Courier New\\',monospace">OVERALL SYNTHESIS</strong>' +
              '<div class="overall-synth-body">' + escHtml(synth.overall_synthesis) + '</div></div>';
    }}
    banner.innerHTML = body;
    contentEl.appendChild(banner);
  }});

  const table = document.createElement('table');
  table.className = 'comp-table';

  // Header: [student] [run1/model columns] [run2/model columns] ...
  const thead = document.createElement('thead');
  let hrow = '<tr><th class="student-col">student</th>';
  ALL_RUNS.forEach(r => {{
    r.models.forEach(m => {{
      hrow += '<th class="cond-col">' + escHtml(r.condition) + '<br><span style="font-size:0.8em;font-weight:normal">' + escHtml(m) + '</span></th>';
    }});
  }});
  hrow += '</tr>';
  thead.innerHTML = hrow;
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  allStudents.forEach(sid => {{
    const info = studentSet.get(sid);
    const tr = document.createElement('tr');
    const badge = info.isWB ? '<span class="wb-badge">WB</span>' : '<span class="es-badge">ES</span>';
    tr.innerHTML = '<th class="student-col"><div class="sid">' + escHtml(sid) + '</div>' +
      '<span class="sname">' + escHtml(info.name) + '</span>' + badge + '</th>';

    ALL_RUNS.forEach((run, runIdx) => {{
      run.models.forEach(m => {{
        const cid = sid + '_' + m + '_' + run.condition;
        const cell = run.cells[cid];
        const td = document.createElement('td');
        td.className = 'comp-cell';

        if (cell) {{
          const rs = runState(run.id);
          const stCell = rs.cells[cid] || {{}};
          const cat = stCell.category ? catById(stCell.category) : null;
          if (cat) td.style.background = cat.color + '55';
          // Wellbeing strip (also in comparison view)
          const wbClass = aggregateWellbeing(getAgentEntries(run, cid));
          if (wbClass) td.classList.add('wb-' + wbClass);
          // Alarm flag in comparison view
          const al = detectAlarms(cell.text, getAgentEntries(run, cid));
          if (al.triggered) {{
            td.classList.add('alarm-flag');
            td.title = (td.title || '') + (td.title ? '\\n' : '') + 'Alarm: ' +
              (al.phrases.length ? 'phrases: ' + al.phrases.join('; ') : '') +
              (al.codeHits.length ? '  codes: ' + al.codeHits.map(h => h.coder+'/'+h.code).join('; ') : '');
          }}

          const badge2 = cat
            ? '<span class="comp-code-badge" style="background:' + cat.color + '">' + escHtml(cat.label) + '</span><br>'
            : '';
          const textDiv = document.createElement('div');
          textDiv.innerHTML = badge2;
          const textEl = document.createElement('div');
          textEl.className = 'comp-text';
          // Highlight load-bearing quotes
          const compHi = highlightQuotesInPreview(cell.text, getAgentEntries(run, cid));
          textEl.innerHTML = compHi.html;
          textDiv.appendChild(textEl);
          td.appendChild(textDiv);
          td.onclick = () => openCellModal(run, cid);
        }} else {{
          td.innerHTML = '<span class="comp-no-data">— student not in this run —</span>';
        }}
        tr.appendChild(td);
      }});
    }});
    tbody.appendChild(tr);

    // Per-student synthesis row(s) — one per coder that has synthesis for this student
    Object.entries(SYNTHESIS).forEach(([coder, synth]) => {{
      const stSynth = (synth.per_student || {{}})[sid];
      if (!stSynth) return;
      const synthTr = document.createElement('tr');
      synthTr.className = 'synth-row';
      const synthTd = document.createElement('td');
      let totalCols = 1;
      ALL_RUNS.forEach(r => totalCols += r.models.length);
      synthTd.colSpan = totalCols;
      const dir = stSynth.directional_assessment || '';
      const dirBadge = dir
        ? '<span class="synth-assess synth-assess-' + escHtml(dir) + '">' + escHtml(dir) + '</span>'
        : '';
      const evidence = stSynth.evidence
        ? '<div class="synth-evidence">' +
            Object.entries(stSynth.evidence).map(([rid, q]) =>
              '<strong>' + escHtml(rid) + ':</strong> "' + escHtml(q) + '"'
            ).join(' &nbsp;·&nbsp; ') +
          '</div>'
        : '';
      synthTd.innerHTML =
        '<span class="synth-coder">' + escHtml(coder) + '</span>' + dirBadge +
        '<div class="synth-body">' + escHtml(stSynth.what_changed || '') + '</div>' +
        evidence;
      synthTr.appendChild(synthTd);
      tbody.appendChild(synthTr);
    }});
  }});

  table.appendChild(tbody);
  contentEl.appendChild(table);
}}

// ---- Hover popover ----
let HOVER_POPOVER = null;
let HOVER_SHOW_TIMER = null;
let HOVER_HIDE_TIMER = null;

function attachHoverHandlers(el, run, rs, cid) {{
  el.addEventListener('mouseenter', () => {{
    clearTimeout(HOVER_HIDE_TIMER);
    HOVER_SHOW_TIMER = setTimeout(() => showPopover(el, run, rs, cid), 320);
  }});
  el.addEventListener('mouseleave', () => {{
    clearTimeout(HOVER_SHOW_TIMER);
    HOVER_HIDE_TIMER = setTimeout(hidePopover, 280);
  }});
}}

function hidePopover() {{
  clearTimeout(HOVER_SHOW_TIMER);
  if (HOVER_POPOVER) {{ HOVER_POPOVER.remove(); HOVER_POPOVER = null; }}
}}

function showPopover(anchorEl, run, rs, cid) {{
  clearTimeout(HOVER_HIDE_TIMER);
  if (HOVER_POPOVER) HOVER_POPOVER.remove();

  const cell = run.cells[cid];
  const stCell = rs.cells[cid] || {{}};
  const hasExcerpt = !!stCell.excerpt;
  const agEntries = getAgentEntries(run, cid);
  const agHtml = agEntries.length > 0
    ? agEntries.map(e =>
        '<div class="popover-agent-section">' +
          '<div class="popover-agent-header">Agent: ' + escHtml(e.coder) + '</div>' +
          '<div><span class="popover-agent-cat">' + escHtml(e.category) + '</span>' +
          (e.notes ? ' — ' + escHtml(e.notes) : '') + '</div>' +
        '</div>'
      ).join('')
    : '';

  const pop = document.createElement('div');
  pop.className = 'hover-popover';
  pop.innerHTML =
    '<div class="popover-meta">' + escHtml(cell.sid) + ' · ' + escHtml(run.student_names[cell.sid] || '') +
      ' · ' + escHtml(cell.model) + ' · ' + escHtml(cell.condition) + '</div>' +
    '<div class="popover-actions-top">' +
      '<button class="popover-btn" id="pop-set">↑ Set selected text as preview</button>' +
      (hasExcerpt ? '<button class="popover-btn reset" id="pop-reset">Reset excerpt</button>' : '') +
      '<span class="popover-hint" id="pop-hint">select text below, then click Set</span>' +
    '</div>' +
    '<div class="popover-body" id="pop-body">' + escHtml(cell.text) + '</div>' +
    agHtml;

  document.body.appendChild(pop);
  HOVER_POPOVER = pop;
  HOVER_POPOVER._lastSel = '';
  HOVER_POPOVER._cid = cid;
  HOVER_POPOVER._run = run;
  HOVER_POPOVER._rs = rs;

  const r = anchorEl.getBoundingClientRect();
  const popW = 540;
  let left = r.right + 12;
  if (left + popW > window.innerWidth - 20) left = Math.max(8, r.left - popW - 12);
  pop.style.left = left + 'px';
  const maxH = Math.min(window.innerHeight - 40, 600);
  pop.style.maxHeight = maxH + 'px';
  let top = r.top;
  if (top + maxH > window.innerHeight - 20) top = Math.max(10, window.innerHeight - maxH - 20);
  pop.style.top = top + 'px';

  pop.addEventListener('mouseenter', () => clearTimeout(HOVER_HIDE_TIMER));
  pop.addEventListener('mouseleave', () => {{ HOVER_HIDE_TIMER = setTimeout(hidePopover, 280); }});

  const bodyEl = document.getElementById('pop-body');
  const hintEl = document.getElementById('pop-hint');
  bodyEl.addEventListener('mouseup', () => {{
    const sel = window.getSelection();
    if (!sel || !sel.rangeCount) return;
    if (bodyEl.contains(sel.anchorNode)) {{
      const text = sel.toString().trim();
      if (text) {{
        HOVER_POPOVER._lastSel = text;
        hintEl.textContent = 'selected: ' + text.length + ' chars — click Set';
        hintEl.style.color = '#1a4a7e';
        hintEl.style.fontStyle = 'normal';
      }}
    }}
  }});

  const setBtn = document.getElementById('pop-set');
  setBtn.addEventListener('mousedown', (e) => {{ e.preventDefault(); }});
  setBtn.addEventListener('click', (e) => {{
    e.preventDefault();
    const text = (HOVER_POPOVER && HOVER_POPOVER._lastSel) || window.getSelection().toString().trim();
    if (!text) {{
      setBtn.textContent = 'select text first';
      setBtn.style.background = '#c2941f';
      setTimeout(() => {{ setBtn.textContent = '↑ Set selected text as preview'; setBtn.style.background = ''; }}, 1400);
      return;
    }}
    const rs2 = HOVER_POPOVER._rs;
    const cid2 = HOVER_POPOVER._cid;
    rs2.cells[cid2] = rs2.cells[cid2] || {{}};
    rs2.cells[cid2].excerpt = text;
    saveState();
    rerenderCell(HOVER_POPOVER._run, cid2);
    setBtn.textContent = '✓ saved as preview';
    setTimeout(hidePopover, 600);
  }});

  const resetBtnEl = document.getElementById('pop-reset');
  if (resetBtnEl) {{
    resetBtnEl.addEventListener('click', () => {{
      const rs2 = HOVER_POPOVER._rs;
      const cid2 = HOVER_POPOVER._cid;
      if (rs2.cells[cid2]) delete rs2.cells[cid2].excerpt;
      saveState();
      rerenderCell(HOVER_POPOVER._run, cid2);
      hidePopover();
    }});
  }}
}}

// ---- Cell modal ----
let MODAL_RUN = null;
let MODAL_CID = null;

function openCellModal(run, cid) {{
  MODAL_RUN = run;
  MODAL_CID = cid;
  const cell = run.cells[cid];
  if (!cell) return;
  const rs = runState(run.id);
  const stCell = rs.cells[cid] || {{}};
  const catOpts = '<option value="">— select —</option>' +
    STATE.categories.map(c =>
      '<option value="' + c.id + '"' + (stCell.category === c.id ? ' selected' : '') + '>' + escHtml(c.label) + '</option>'
    ).join('');
  const agEntries = getAgentEntries(run, cid);
  const agSection = agEntries.length > 0
    ? agEntries.map(e =>
        '<div class="modal-agent"><strong>Agent (' + escHtml(e.coder) + '): ' + escHtml(e.category) + '</strong>' +
        (e.notes ? '<br>' + escHtml(e.notes) : '') + '</div>'
      ).join('')
    : '';

  document.getElementById('cell-modal-content').innerHTML =
    '<h2>' + escHtml(cell.sid) + ' · ' + escHtml(run.student_names[cell.sid] || '') + '</h2>' +
    '<div class="modal-meta">run: ' + escHtml(run.id) + ' · model: ' + escHtml(cell.model) + ' · condition: ' + escHtml(cell.condition) + '</div>' +
    agSection +
    '<div class="modal-output">' + escHtml(cell.text) + '</div>' +
    '<div class="modal-coding">' +
      '<label>Coding category</label>' +
      '<select id="modal-cat" onchange="setModalCat(this.value)">' + catOpts + '</select>' +
      '<label>Notes</label>' +
      '<textarea id="modal-notes" oninput="setModalNotes(this.value)">' + escHtml(stCell.notes || '') + '</textarea>' +
    '</div>' +
    '<div class="modal-actions">' +
      '<button onclick="navModal(-1)">◀ prev cell</button>' +
      '<button onclick="navModal(1)">next cell ▶</button>' +
      '<button class="primary" onclick="closeCellModal()">Close</button>' +
    '</div>';

  document.getElementById('cell-modal').classList.add('show');
}}

function closeCellModal() {{
  document.getElementById('cell-modal').classList.remove('show');
  if (MODAL_RUN && MODAL_CID) rerenderCell(MODAL_RUN, MODAL_CID);
  MODAL_RUN = null; MODAL_CID = null;
}}

function setModalCat(catId) {{
  if (!MODAL_RUN || !MODAL_CID) return;
  const rs = runState(MODAL_RUN.id);
  rs.cells[MODAL_CID] = rs.cells[MODAL_CID] || {{}};
  rs.cells[MODAL_CID].category = catId;
  saveState();
}}

function setModalNotes(notes) {{
  if (!MODAL_RUN || !MODAL_CID) return;
  const rs = runState(MODAL_RUN.id);
  rs.cells[MODAL_CID] = rs.cells[MODAL_CID] || {{}};
  rs.cells[MODAL_CID].notes = notes;
  saveState();
}}

function navModal(delta) {{
  if (!MODAL_RUN || !MODAL_CID) return;
  const cells = Object.keys(MODAL_RUN.cells);
  const idx = cells.indexOf(MODAL_CID);
  const nx = (idx + delta + cells.length) % cells.length;
  closeCellModal();
  openCellModal(MODAL_RUN, cells[nx]);
}}

// ---- Export / import ----
function exportState() {{
  const blob = new Blob([JSON.stringify(STATE, null, 2)], {{type: 'application/json'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url;
  a.download = 'genob_ws_state_' + new Date().toISOString().slice(0,10) + '.json';
  a.click(); URL.revokeObjectURL(url);
}}

function importState() {{
  const inp = document.createElement('input'); inp.type = 'file'; inp.accept = 'application/json';
  inp.onchange = (e) => {{
    const f = e.target.files[0]; if (!f) return;
    const r = new FileReader();
    r.onload = () => {{
      try {{
        STATE = JSON.parse(r.result);
        saveState(); renderCatsEditor();
        BUILT_TABS.clear();
        document.querySelectorAll('.tab-content').forEach(c => c.innerHTML = '');
        activateTab(ACTIVE_TAB);
        alert('Imported.');
      }} catch (err) {{ alert('Import failed: ' + err.message); }}
    }};
    r.readAsText(f);
  }};
  inp.click();
}}

function exportActiveRunCodes() {{
  if (ACTIVE_TAB < 0) {{ alert('Switch to a coding tab first.'); return; }}
  const run = ALL_RUNS[ACTIVE_TAB];
  const rs = runState(run.id);
  const codes = {{}};
  Object.entries(run.cells).forEach(([cid, cell]) => {{
    const stCell = rs.cells[cid] || {{}};
    codes[cid] = {{
      code: stCell.category || null,
      notes: stCell.notes || '',
      excerpt: stCell.excerpt || '',
      raw_observation_text: cell.text,
      student_name: cell.student_name,
    }};
  }});
  const payload = {{
    schema: 'manual_codes',
    exported_from: run.id,
    exported_condition: run.condition,
    exported_at: new Date().toISOString(),
    codes: codes,
  }};
  const blob = new Blob([JSON.stringify(payload, null, 2)], {{type: 'application/json'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href = url;
  a.download = 'genob_codes_' + run.id + '_' + new Date().toISOString().slice(0,10) + '.json';
  a.click(); URL.revokeObjectURL(url);
}}

// ---- Utils ----
function escHtml(s) {{
  return (s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}}

// ---- Keyboard ----
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') closeCellModal();
  if (MODAL_CID) {{
    if (e.altKey && e.key === 'ArrowLeft') navModal(-1);
    if (e.altKey && e.key === 'ArrowRight') navModal(1);
  }}
}});

// ---- Init ----
renderCatsEditor();
renderTabBar();
</script>
</body>
</html>
"""


def main(argv=None):
    p = argparse.ArgumentParser(description="Build a generative observation coding workshop.")
    p.add_argument(
        "files",
        nargs="+",
        metavar="OBS_JSON",
        help="One or more observation JSON files to include as selectable runs.",
    )
    p.add_argument(
        "--agent-codes",
        nargs="*",
        default=[],
        metavar="CODES_JSON",
        help="Agent coding JSON files (one per coder per run).",
    )
    p.add_argument(
        "--synthesis",
        nargs="*",
        default=[],
        metavar="SYNTH_JSON",
        help="Cross-condition synthesis JSON files (one per coder).",
    )
    p.add_argument(
        "--coders",
        nargs="*",
        default=["Opus 4", "Gemini 2.5 Pro"],
        metavar="CODER_NAME",
        help="Coder names to always render as columns (placeholder if no codes loaded yet). Default: Opus 4, Gemini 2.5 Pro.",
    )
    p.add_argument(
        "--corpus-state",
        default=None,
        metavar="STATE_JSON",
        help="Optional hand-coding corpus_review_state.json. Adds expected pattern + label as read-only label material in the student column.",
    )
    p.add_argument(
        "--out",
        default=None,
        help="Output HTML path (default: data_tables/genob_workshop_YYYY-MM-DD.html).",
    )
    args = p.parse_args(argv)

    runs = []
    for f in args.files:
        path = Path(f)
        if not path.is_absolute():
            path = ROOT / path
        print(f"Loading {path.name}…")
        runs.append(load_run(path))
        print(f"  → {runs[-1]['id']}: {len(runs[-1]['students'])} students, models={runs[-1]['models']}")

    agent_codes = {}
    for f in (args.agent_codes or []):
        path = Path(f)
        if not path.is_absolute():
            path = ROOT / path
        print(f"Loading agent codes: {path.name}…")
        # Merge: if same key from another file, append entries to list
        new_codes = load_agent_codes([path])
        for k, v in new_codes.items():
            if k in agent_codes:
                agent_codes[k].extend(v)
            else:
                agent_codes[k] = v

    synthesis = {}
    for f in (args.synthesis or []):
        path = Path(f)
        if not path.is_absolute():
            path = ROOT / path
        print(f"Loading synthesis: {path.name}…")
        synthesis.update(load_cross_condition_synthesis([path]))

    corpus_labels = {}
    if args.corpus_state:
        cs_path = Path(args.corpus_state)
        if not cs_path.is_absolute():
            cs_path = ROOT / cs_path
        print(f"Loading corpus state: {cs_path.name}…")
        corpus_labels = load_corpus_review_state(cs_path)
        print(f"  → label material for {len(corpus_labels)} students")

    out_path = args.out
    if out_path is None:
        today = datetime.date.today().isoformat()
        out_dir = ROOT / "data_tables"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"genob_workshop_{today}.html"
    else:
        out_path = Path(out_path)
        if not out_path.is_absolute():
            out_path = ROOT / out_path
        out_path.parent.mkdir(parents=True, exist_ok=True)

    html = build_html(runs, agent_codes, synthesis, args.coders, corpus_labels)
    out_path.write_text(html, encoding="utf-8")
    print(f"Wrote {out_path} ({out_path.stat().st_size / 1024:.1f} KB)")
    print(f"Runs embedded: {[r['id'] for r in runs]}")
    if synthesis:
        print(f"Syntheses embedded: {list(synthesis.keys())}")


if __name__ == "__main__":
    main()
