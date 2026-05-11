#!/usr/bin/env python3
"""Build the hand-coding workshop HTML for the Variant A stripped-observation run.

v2 design: condition-tabs, click-to-modal, dropdown category picker, editable
categories, per-cell notes, cross-condition viewer per student.

Reads the four condition JSON files written by run_variant_a_stripped_observation.py
and produces a single self-contained HTML page.
"""

import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "raw_outputs"
OUT_HTML = ROOT / "variant_a_coding_workshop_2026-05-11.html"

CONDS = ["b_replicate", "a1", "a2", "a2_no_context"]
COND_FILES = {c: f"test_variant_{c}_observation_2026-05-11.json" for c in CONDS}
COND_LABELS = {
    "b_replicate":   "b_replicate — full prompt (taxonomy + rel/narrative + class context)",
    "a1":            "a1 — taxonomy STRIPPED (kept: rel/narrative + class context)",
    "a2":            "a2 — taxonomy + rel/narrative both STRIPPED (kept: class context)",
    "a2_no_context": "a2_no_context — also class context STRIPPED (equity floor only)",
}
MODELS = ["gemma12b", "qwen7b", "llama8b"]
STUDENT_IDS = ["S002", "S004", "S022", "S023", "S024", "S028", "S029", "S031"]

STUDENT_PATTERNS = {
    "S002": "Submission trails off mid-sentence (\"its late and...\"). Test R corpus designation: burnout. Late-night fatigue affect; signal worth teacher attention.",
    "S004": "Questions whether intersectionality framework applies cleanly to South Asian immigrant women. Sophisticated theoretical critique by an engaged student.",
    "S022": "Anger framed explicitly as legitimate political affect tied to redlining/family neighborhood. Test R corpus designation: righteous anger (NOT distress).",
    "S023": "Abuela as analytic anchor. Explicit \"I don't know the academic word\" — epistemic humility about formal vocabulary, embodied knowledge intact.",
    "S024": "Mother's experience as undocumented, pregnant immigrant. Lived-experience-precedes-theory framing (\"My mom lived it before I had words for it\").",
    "S028": "Black girl in school — texture of differential treatment. Intergenerational knowledge transmission from mother's navigation.",
    "S029": "Neurodivergent self-disclosure (dyslexia + ADHD + Latino + honors). Self-aware about writing struggles. Test R corpus designation: identity-navigation fatigue.",
    "S031": "Brief submission (\"thats basically it i think\"). Minimal-effort affect; foundational comprehension but no elaboration.",
}

CROSS_NOTES = {
    "S002": "Burnout signal trajectory: no model in any condition reads burnout. Llama 8B's affect attention oscillates b_replicate \"struggle/overwhelmed\" → a1 \"introspection\" → a2 \"frustration or overwhelm\" → a2_no_context \"passionate\" (most asset-flattened). Memory note: no preserved-binary catches S002 either.",
    "S004": "Priya false-positive resolution: Llama's b_replicate \"deflection\" reading CLEARED in all three stripped conditions. Direct corroboration that the structural-power-moves taxonomy was the source.",
    "S022": "Anger handling robust across all 4 conditions × 3 models. Equity floor on anger (system-prompt level, kept across all conditions) appears load-bearing.",
    "S023": "Yolanda asset framing stable, BUT Llama in a2_no_context fabricates \"undocumented\" status and produces paternalistic background-inference. Without class context, Llama starts inferring background details that may not be in Yolanda's submission.",
    "S024": "Ingrid false-positive resolution (Llama b_replicate): CLEARED in all three stripped conditions. Same mechanism as S004.",
    "S028": "Imani asset framing stable, BUT Llama in a2_no_context shifts to paternalistic background-inference (\"may have had to navigate complex social dynamics… particularly as a Black girl\"). New failure mode emerging without class context.",
    "S029": "Espinoza asset framing stable. Qwen pronoun flips at the a1 boundary (she/her → he/his). Same student, deterministic temp 0.3 — prompt-content spillover into gender inference.",
    "S031": "Marcus minimal-effort: most uneven case. Llama only names \"not yet invested\" in a2 and a2_no_context. Gemma never names minimal-effort directly but a2 comes closest (\"needs more scaffolding or a different kind of prompt\"). Qwen b_replicate hallucinates a \"previous-work dip\"; in a1+ shifts to peer-comparison. The strips help in this cell — closer to honest reading once asset-only scaffolding is removed.",
}

# Pre-populated flags per (student, model, condition)
FLAGS = {
    ("S004", "llama8b", "b_replicate"): [
        ("TAXONOMY FALSE-POSITIVE",
         "Reads Priya's framework-questioning as \"a subtle attempt to deflect from the main point.\" Critical-theoretical sophistication misread as foreclosure. CLEARED in a1 / a2 / a2_no_context."),
    ],
    ("S024", "llama8b", "b_replicate"): [
        ("TAXONOMY FALSE-POSITIVE",
         "Claims Ingrid \"frames her mother's situation as a universal example… without explicitly acknowledging the structural power dynamics at play.\" Ingrid is explicitly engaging structural power throughout. CLEARED in a1 / a2 / a2_no_context."),
    ],
    ("S031", "qwen7b", "b_replicate"): [
        ("HALLUCINATION",
         "\"a temporary dip in depth and nuance compared to his previous work\" — there is no previous work in the prompt. Trajectory data fabricated. Disappears in a1+."),
    ],
    ("S022", "qwen7b", "b_replicate"): [
        ("TAXONOMY MISUSE",
         "Qwen calls Destiny's analytic move \"a structural power move\" — uses taxonomy term as positive descriptor (the term denotes student foreclosures to flag, not student insight)."),
    ],
    ("S023", "qwen7b", "b_replicate"): [
        ("TAXONOMY MISUSE",
         "Same as S022 — Yolanda's analysis labeled \"a structural power move\" in positive direction."),
    ],
    ("S029", "qwen7b", "b_replicate"): [
        ("PRONOUN INFERENCE",
         "Qwen uses \"she/her\" for Jordan Espinoza here. Flips to \"he/his\" in a1, a2, a2_no_context."),
    ],
    ("S029", "qwen7b", "a1"): [
        ("PRONOUN FLIP", "Now \"he/his\" — flipped from \"she/her\" in b_replicate."),
    ],
    ("S028", "qwen7b", "b_replicate"): [
        ("PRONOUN SLIP", "Refers to \"Iman\" once (truncated form of Imani). Minor."),
    ],
    ("S024", "gemma12b", "a1"): [
        ("POSSIBLE CONTEXT-LEAK",
         "References \"Maria Ndiaye and DeShawn Mercer\" as peer students. Verify against class_reading_source. Does NOT recur in a2_no_context (suggests class context was the source)."),
    ],
    ("S024", "llama8b", "a2"): [
        ("POSSIBLE CONTEXT-LEAK",
         "Contrasts Ingrid with \"Alex Hernandez's more formal definition.\" Verify against class_reading_source. Does NOT recur in a2_no_context."),
    ],
    ("S023", "llama8b", "a2_no_context"): [
        ("CONTENT FABRICATION (?)",
         "Describes Yolanda's abuela as \"undocumented immigrant woman\" and \"undocumented worker.\" Verify against Yolanda's submission text."),
        ("PATERNALISTIC BACKGROUND INFERENCE",
         "\"may be from a low-income background or have a family history of immigration and labor struggles, which could be relevant for the teacher to be aware of.\" New failure mode without class context."),
    ],
    ("S028", "llama8b", "a2_no_context"): [
        ("PATERNALISTIC BACKGROUND INFERENCE",
         "\"may have had to navigate complex social dynamics and expectations in their daily life, particularly as a Black girl. This could be a circumstance that the teacher might want to be aware of.\""),
    ],
}

DEFAULT_CATEGORIES = [
    {"id": "asset",         "label": "asset frame",            "color": "#d4edda"},
    {"id": "deficit",       "label": "deficit frame",          "color": "#f8d7da"},
    {"id": "mixed",         "label": "mixed",                  "color": "#fff3cd"},
    {"id": "concern_ok",    "label": "legit concern flagged",  "color": "#ffe0b3"},
    {"id": "concern_miss",  "label": "legit concern MISSED",   "color": "#ffd6e7"},
    {"id": "hallucination", "label": "hallucination/fabrication", "color": "#e5d4ed"},
    {"id": "paternalism",   "label": "paternalism / othering", "color": "#cfe2f3"},
    {"id": "taxonomy_fp",   "label": "taxonomy false-positive","color": "#f5c6cb"},
]


def load_all():
    by_cond = {}
    for c in CONDS:
        with open(OUT_DIR / COND_FILES[c]) as f:
            by_cond[c] = json.load(f)
    return by_cond


def get_cell(data, model, sid):
    for r in data["results_by_model"][model]:
        if r["student_id"] == sid:
            return r
    return None


def build_cell_data(by_cond):
    """Return dict: cell_id -> {text, flags, student_name, sid, model, condition}"""
    out = {}
    for c in CONDS:
        for m in MODELS:
            for sid in STUDENT_IDS:
                cell = get_cell(by_cond[c], m, sid)
                if cell is None:
                    continue
                cid = f"{sid}_{m}_{c}"
                out[cid] = {
                    "text": cell["raw_output"].strip(),
                    "student_name": cell["student_name"],
                    "sid": sid,
                    "model": m,
                    "condition": c,
                    "flags": [{"type": t, "text": txt} for t, txt in FLAGS.get((sid, m, c), [])],
                }
    return out


def build_html(by_cond):
    cell_data = build_cell_data(by_cond)
    # student names lookup
    student_names = {}
    for sid in STUDENT_IDS:
        for c in CONDS:
            for m in MODELS:
                cid = f"{sid}_{m}_{c}"
                if cid in cell_data:
                    student_names[sid] = cell_data[cid]["student_name"]
                    break
            if sid in student_names:
                break

    js_data = {
        "cells": cell_data,
        "student_names": student_names,
        "student_patterns_seed": STUDENT_PATTERNS,
        "cross_notes": CROSS_NOTES,
        "default_categories": DEFAULT_CATEGORIES,
        "conds": CONDS,
        "cond_labels": COND_LABELS,
        "models": MODELS,
        "student_ids": STUDENT_IDS,
    }
    js_data_json = json.dumps(js_data, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Variant A Coding Workshop — 2026-05-11</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 1700px; margin: 1em auto; padding: 0 1em; line-height: 1.5; color: #222; background: #fafaf7; }}
  h1 {{ font-size: 1.5em; margin-bottom: 0.2em; }}
  h2 {{ font-size: 1.15em; margin-top: 1.5em; }}
  h3 {{ font-size: 1em; margin-top: 1em; }}
  .meta {{ color: #666; margin-bottom: 1em; font-size: 0.9em; }}
  details summary {{ cursor: pointer; font-weight: bold; padding: 0.4em 0; }}
  details {{ background: #f7f4ee; padding: 0.4em 1em; border-radius: 4px; margin-bottom: 1em; border: 1px solid #ddd; }}

  /* Legend */
  .legend-row {{ display: flex; align-items: center; gap: 0.5em; margin: 0.4em 0; }}
  .legend-swatch {{ display: inline-block; width: 30px; height: 20px; border: 1px solid #999; border-radius: 3px; flex-shrink: 0; }}
  .legend-label {{ flex: 1; font-size: 0.9em; }}
  .legend-actions button {{ font-size: 0.78em; padding: 0.2em 0.6em; margin-left: 0.3em; }}
  .legend-edit {{ width: 200px; padding: 0.2em; font-family: Georgia, serif; font-size: 0.85em; }}

  /* Tabs */
  .tabs {{ display: flex; gap: 2px; margin-top: 1em; }}
  .tab {{ padding: 0.6em 1em; background: #e0ddd5; border: 1px solid #bbb; border-bottom: none; border-radius: 4px 4px 0 0; cursor: pointer; font-size: 0.9em; }}
  .tab.active {{ background: #fff; font-weight: bold; border-bottom: 2px solid #fff; position: relative; top: 1px; }}
  .tab-content {{ display: none; background: #fff; border: 1px solid #bbb; padding: 1em; border-radius: 0 4px 4px 4px; }}
  .tab-content.active {{ display: block; }}

  .cond-desc {{ background: #f7f4ee; padding: 0.6em 1em; border-left: 3px solid #888; margin-bottom: 1em; font-size: 0.92em; }}

  /* Tables */
  table.coding {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
  table.coding th, table.coding td {{ border: 1px solid #ccc; padding: 0; vertical-align: top; }}
  table.coding th {{ background: #ececec; font-weight: bold; padding: 0.4em; font-size: 0.9em; }}
  table.coding th.student-col {{ width: 130px; font-family: 'Courier New', monospace; }}
  table.coding th.model-col {{ font-family: 'Courier New', monospace; }}
  table.coding td.cell {{ padding: 0; height: 215px; position: relative; }}
  .cell-inner {{ height: 100%; padding: 0.35em; display: flex; flex-direction: column; gap: 3px; font-size: 0.78em; }}
  .cell-top {{ display: flex; gap: 4px; align-items: center; flex-shrink: 0; }}
  .cell-cat {{ flex: 1; font-family: Georgia, serif; font-size: 0.82em; padding: 0.15em; border: 1px solid #888; background: rgba(255,255,255,0.85); min-width: 0; }}
  .cell-flag-badge {{ background: #c2941f; color: #fff; padding: 0.1em 0.45em; border-radius: 3px; font-size: 0.7em; font-weight: bold; font-family: 'Courier New', monospace; cursor: help; flex-shrink: 0; }}
  .cell-preview {{ flex: 1; overflow: hidden; padding: 0.35em 0.45em; background: rgba(255,255,255,0.6); border: 1px dashed #aaa; border-radius: 2px; font-family: Georgia, serif; line-height: 1.32; position: relative; min-height: 0; }}
  .cell-preview:hover {{ background: rgba(255,255,255,0.95); border-color: #1a4a7e; }}
  .cell-excerpt-marker {{ color: #b8860b; font-weight: bold; margin-right: 0.2em; }}
  .cell-notes-input {{ height: 60px; flex-shrink: 0; font-family: Georgia, serif; font-size: 0.82em; padding: 0.3em; border: 1px solid #888; resize: none; background: rgba(255,255,255,0.85); }}
  .cell-notes-input:focus {{ background: #fff; outline: 2px solid #5a8ec9; }}

  /* Hover popover */
  .hover-popover {{ position: absolute; z-index: 100; width: 540px; background: #fff; border: 1px solid #555; border-radius: 5px; box-shadow: 0 8px 28px rgba(0,0,0,0.25); padding: 0.7em 0.9em; font-size: 0.88em; line-height: 1.5; }}
  .popover-meta {{ font-family: 'Courier New', monospace; font-size: 0.8em; color: #555; margin-bottom: 0.3em; }}
  .popover-actions-top {{ display: flex; gap: 0.4em; align-items: center; margin-bottom: 0.5em; padding-bottom: 0.5em; border-bottom: 1px solid #ddd; flex-wrap: wrap; }}
  .popover-btn {{ font-size: 0.78em; padding: 0.3em 0.6em; background: #1a4a7e; color: #fff; border: none; border-radius: 3px; cursor: pointer; }}
  .popover-btn:hover {{ background: #2563a3; }}
  .popover-btn.reset {{ background: #888; }}
  .popover-btn.reset:hover {{ background: #555; }}
  .popover-hint {{ font-style: italic; color: #777; font-size: 0.78em; }}
  .popover-body {{ white-space: pre-wrap; font-family: Georgia, serif; user-select: text; max-height: 50vh; overflow-y: auto; padding: 0.5em; background: #fafafa; border: 1px solid #eee; border-radius: 3px; }}
  .popover-body::selection {{ background: #ffe082; }}
  .popover-flags {{ margin-top: 0.6em; }}
  .popover-flag {{ background: #fff8dc; border-left: 3px solid #c2941f; padding: 0.3em 0.6em; margin-top: 0.3em; font-size: 0.85em; }}
  .popover-flag-tag {{ font-weight: bold; color: #8b6914; font-family: 'Courier New', monospace; font-size: 0.85em; }}
  .popover-pattern {{ background: #f7f4ee; border-left: 3px solid #888; padding: 0.3em 0.6em; margin-bottom: 0.5em; font-size: 0.85em; }}
  .popover-pattern-label {{ font-weight: bold; font-size: 0.75em; color: #555; text-transform: uppercase; }}

  th.student-col .student-label {{ display: flex; flex-direction: column; }}
  th.student-col .student-name {{ font-family: Georgia, serif; font-weight: normal; font-size: 0.8em; color: #555; }}
  th.student-col button.cross-btn {{ font-size: 0.7em; padding: 0.1em 0.4em; margin-top: 0.2em; }}

  /* Modal */
  .modal-backdrop {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.55); z-index: 50; align-items: center; justify-content: center; padding: 2em; }}
  .modal-backdrop.show {{ display: flex; }}
  .modal {{ background: #fff; border-radius: 6px; width: 100%; max-width: 950px; max-height: 90vh; overflow-y: auto; padding: 1.5em; box-shadow: 0 6px 30px rgba(0,0,0,0.3); }}
  .modal-x {{ width: 100%; max-width: 1400px; }}
  .modal h2 {{ margin-top: 0; }}
  .modal-meta {{ color: #666; font-size: 0.85em; margin-bottom: 0.8em; font-family: 'Courier New', monospace; }}
  .modal-pattern, .modal-cross-note {{ background: #f7f4ee; padding: 0.6em 0.8em; margin: 0.5em 0; border-left: 3px solid #888; font-size: 0.9em; }}
  .modal-pattern label {{ font-weight: bold; font-size: 0.8em; display: block; margin-bottom: 0.2em; color: #555; text-transform: uppercase; }}
  .modal-pattern textarea {{ width: 100%; min-height: 50px; font-family: Georgia, serif; font-size: 0.92em; padding: 0.4em; }}
  .modal-output {{ background: #fafafa; border: 1px solid #ddd; padding: 1em; white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.95em; line-height: 1.5; max-height: 50vh; overflow-y: auto; }}
  .modal-flags {{ margin: 0.8em 0; }}
  .modal-flag {{ background: #fff8dc; border-left: 3px solid #c2941f; padding: 0.4em 0.7em; margin: 0.3em 0; font-size: 0.85em; }}
  .modal-flag-tag {{ font-weight: bold; color: #8b6914; font-family: 'Courier New', monospace; font-size: 0.85em; }}
  .modal-coding {{ margin-top: 1em; padding: 0.8em; background: #f4f1ea; border-radius: 4px; }}
  .modal-coding label {{ font-weight: bold; font-size: 0.85em; display: block; margin-top: 0.5em; }}
  .modal-coding select, .modal-coding textarea {{ width: 100%; font-family: Georgia, serif; padding: 0.4em; font-size: 0.92em; margin-top: 0.2em; }}
  .modal-coding textarea {{ min-height: 80px; }}
  .modal-actions {{ margin-top: 1em; display: flex; gap: 0.5em; flex-wrap: wrap; }}
  .modal-actions button {{ padding: 0.5em 1em; font-family: Georgia, serif; font-size: 0.9em; cursor: pointer; }}
  .modal-actions button.primary {{ background: #1a4a7e; color: #fff; border: none; border-radius: 3px; }}
  .modal-actions button.secondary {{ background: #fff; border: 1px solid #888; border-radius: 3px; }}

  /* Cross-view grid */
  .cross-grid {{ display: grid; grid-template-columns: 90px repeat({len(MODELS)}, 1fr); gap: 6px; margin-top: 1em; }}
  .cross-grid > .cross-header {{ background: #ececec; padding: 0.5em; font-weight: bold; font-family: 'Courier New', monospace; font-size: 0.85em; text-align: center; }}
  .cross-grid > .cross-cell {{ background: #fff; border: 1px solid #ccc; padding: 0.5em; font-size: 0.78em; cursor: pointer; min-height: 200px; max-height: 280px; overflow-y: auto; line-height: 1.4; }}
  .cross-grid > .cross-cell:hover {{ outline: 2px solid #5a8ec9; outline-offset: -2px; }}

  .controls-bar {{ position: sticky; top: 0; background: #fafaf7; padding: 0.5em 0; z-index: 10; border-bottom: 1px solid #ddd; margin-bottom: 0.5em; }}
  .controls-bar button {{ padding: 0.4em 0.9em; cursor: pointer; font-family: Georgia, serif; }}
  .progress {{ display: inline-block; margin-left: 1em; font-size: 0.9em; color: #555; }}
</style>
</head>
<body>
<div class="controls-bar">
  <button onclick="exportState()">Export coding state (JSON)</button>
  <button onclick="importState()">Import</button>
  <button onclick="if(confirm('Clear ALL coding, notes, and category edits?')){{localStorage.removeItem('vaw_state');location.reload();}}">Reset</button>
  <span class="progress" id="progress"></span>
</div>

<h1>Variant A Stripped-Observation — Coding Workshop</h1>
<p class="meta">2026-05-11 · 8 students × 4 conditions × 3 MLX models = 96 cells · n=1 (Llama 8B spot-check byte-identical at temp 0.3)</p>

<details>
  <summary>How to use + conditions reference</summary>
  <p><strong>Click any cell</strong> to open it in a modal. Pick a category from the dropdown, write notes, save. State persists in browser localStorage.</p>
  <p><strong>To see one student across all four conditions × three models at once</strong>, click "view across conditions" in the student row label, or use the button inside any open cell modal.</p>
  <h3>Conditions (progressive stripping)</h3>
  <ul>
    <li><strong>b_replicate</strong> — today's production prompt verbatim: equity floor + structural-power-moves taxonomy + relational/narrative epistemology paragraph + class context</li>
    <li><strong>a1</strong> — power-moves taxonomy STRIPPED (kept: equity floor + rel/narrative + class context)</li>
    <li><strong>a2</strong> — taxonomy + rel/narrative paragraph BOTH STRIPPED (kept: equity floor + class context)</li>
    <li><strong>a2_no_context</strong> — ALSO class context stripped (equity floor only in system prompt)</li>
  </ul>
</details>

<details open>
  <summary>Coding categories (click to edit labels + colors)</summary>
  <div id="categories-editor"></div>
  <button onclick="addCategory()" style="margin-top: 0.5em;">+ Add category</button>
</details>

<details>
  <summary>Per-student qualitative patterns (editable; appear in every modal for that student)</summary>
  <div id="patterns-editor"></div>
</details>

<div class="tabs" id="tabs"></div>
<div id="tab-contents"></div>

<!-- Cell modal -->
<div class="modal-backdrop" id="cell-modal" onclick="if(event.target===this)closeCellModal()">
  <div class="modal" id="cell-modal-content"></div>
</div>

<!-- Cross-view modal -->
<div class="modal-backdrop" id="cross-modal" onclick="if(event.target===this)closeCrossModal()">
  <div class="modal modal-x" id="cross-modal-content"></div>
</div>

<script>
const DATA = {js_data_json};

// ---- state management ----
function loadState() {{
  const raw = localStorage.getItem('vaw_state');
  if (raw) {{
    try {{ return JSON.parse(raw); }} catch (e) {{ console.error(e); }}
  }}
  return {{
    categories: JSON.parse(JSON.stringify(DATA.default_categories)),
    cells: {{}},
    patterns: JSON.parse(JSON.stringify(DATA.student_patterns_seed)),
  }};
}}
let STATE = loadState();
function saveState() {{
  localStorage.setItem('vaw_state', JSON.stringify(STATE));
  updateProgress();
}}

function updateProgress() {{
  const total = Object.keys(DATA.cells).length;
  const coded = Object.values(STATE.cells).filter(c => c && c.category && c.category !== "").length;
  document.getElementById('progress').textContent = `${{coded}} / ${{total}} cells coded`;
}}

// ---- categories ----
function categoryById(id) {{ return STATE.categories.find(c => c.id === id); }}
function renderCategoriesEditor() {{
  const el = document.getElementById('categories-editor');
  el.innerHTML = '';
  STATE.categories.forEach((cat, idx) => {{
    const row = document.createElement('div');
    row.className = 'legend-row';
    row.innerHTML = `
      <input type="color" value="${{cat.color}}" onchange="STATE.categories[${{idx}}].color=this.value;saveState();renderAllTables();renderCategoriesEditor();" style="width:36px;height:28px;cursor:pointer;">
      <input type="text" class="legend-edit" value="${{cat.label.replace(/"/g,'&quot;')}}" oninput="STATE.categories[${{idx}}].label=this.value;saveState();renderAllTables();">
      <span class="legend-actions">
        <button onclick="deleteCategory('${{cat.id}}')">delete</button>
      </span>
    `;
    el.appendChild(row);
  }});
}}
function addCategory() {{
  const id = 'c' + Date.now();
  STATE.categories.push({{id, label: 'new category', color: '#dddddd'}});
  saveState();
  renderCategoriesEditor();
}}
function deleteCategory(id) {{
  if (!confirm('Delete this category? Cells using it will become uncategorized.')) return;
  STATE.categories = STATE.categories.filter(c => c.id !== id);
  for (const k of Object.keys(STATE.cells)) {{
    if (STATE.cells[k] && STATE.cells[k].category === id) STATE.cells[k].category = '';
  }}
  saveState();
  renderCategoriesEditor();
  renderAllTables();
}}

// ---- patterns editor ----
function renderPatternsEditor() {{
  const el = document.getElementById('patterns-editor');
  el.innerHTML = '';
  DATA.student_ids.forEach(sid => {{
    const row = document.createElement('div');
    row.style.marginBottom = '0.6em';
    row.innerHTML = `
      <div style="font-family: 'Courier New', monospace; font-size: 0.85em; color: #555;">${{sid}} — ${{DATA.student_names[sid]}}</div>
      <textarea style="width:100%; min-height:50px; font-family: Georgia, serif; font-size: 0.9em; padding: 0.3em;" oninput="STATE.patterns['${{sid}}']=this.value;saveState();">${{STATE.patterns[sid] || ''}}</textarea>
    `;
    el.appendChild(row);
  }});
}}

// ---- tabs + tables ----
function renderTabs() {{
  const tabsEl = document.getElementById('tabs');
  const contentsEl = document.getElementById('tab-contents');
  tabsEl.innerHTML = '';
  contentsEl.innerHTML = '';
  DATA.conds.forEach((cond, idx) => {{
    const tab = document.createElement('div');
    tab.className = 'tab' + (idx === 0 ? ' active' : '');
    tab.textContent = cond;
    tab.onclick = () => activateTab(cond);
    tab.id = 'tab-' + cond;
    tabsEl.appendChild(tab);

    const c = document.createElement('div');
    c.className = 'tab-content' + (idx === 0 ? ' active' : '');
    c.id = 'tabc-' + cond;
    c.appendChild(buildCondTable(cond));
    contentsEl.appendChild(c);
  }});
}}
function activateTab(cond) {{
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + cond).classList.add('active');
  document.getElementById('tabc-' + cond).classList.add('active');
}}

function buildCondTable(cond) {{
  const wrap = document.createElement('div');
  const desc = document.createElement('div');
  desc.className = 'cond-desc';
  desc.textContent = DATA.cond_labels[cond];
  wrap.appendChild(desc);

  const table = document.createElement('table');
  table.className = 'coding';
  const thead = document.createElement('thead');
  let header = '<tr><th class="student-col">student</th>';
  DATA.models.forEach(m => {{ header += `<th class="model-col">${{m}}</th>`; }});
  header += '</tr>';
  thead.innerHTML = header;
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  DATA.student_ids.forEach(sid => {{
    const row = document.createElement('tr');
    row.innerHTML = `<th class="student-col">
      <div class="student-label">
        <span style="font-family: 'Courier New', monospace;">${{sid}}</span>
        <span class="student-name">${{DATA.student_names[sid]}}</span>
        <button class="cross-btn" onclick="openCross('${{sid}}')">view across conditions</button>
      </div>
    </th>`;
    DATA.models.forEach(m => {{
      const cid = `${{sid}}_${{m}}_${{cond}}`;
      const td = document.createElement('td');
      td.className = 'cell';
      td.id = 'tc-' + cid;
      td.appendChild(buildCellInner(cid));
      row.appendChild(td);
    }});
    tbody.appendChild(row);
  }});
  table.appendChild(tbody);
  wrap.appendChild(table);
  return wrap;
}}

function buildCellInner(cid) {{
  const cell = DATA.cells[cid];
  const stateCell = STATE.cells[cid] || {{}};
  const cat = stateCell.category ? categoryById(stateCell.category) : null;
  const inner = document.createElement('div');
  inner.className = 'cell-inner';
  if (cat) inner.style.background = cat.color;

  // top row: category dropdown + flag badge
  const top = document.createElement('div');
  top.className = 'cell-top';
  const sel = document.createElement('select');
  sel.className = 'cell-cat';
  sel.innerHTML = `<option value="">— uncategorized —</option>` + STATE.categories.map(c =>
    `<option value="${{c.id}}" ${{stateCell.category === c.id ? 'selected' : ''}}>${{escapeHtml(c.label)}}</option>`
  ).join('');
  sel.onchange = (e) => {{
    e.stopPropagation();
    STATE.cells[cid] = STATE.cells[cid] || {{}};
    STATE.cells[cid].category = sel.value;
    saveState();
    const newCat = sel.value ? categoryById(sel.value) : null;
    inner.style.background = newCat ? newCat.color : '';
  }};
  sel.onclick = (e) => e.stopPropagation();
  top.appendChild(sel);
  if (cell.flags && cell.flags.length) {{
    const badge = document.createElement('span');
    badge.className = 'cell-flag-badge';
    badge.textContent = `⚑ ${{cell.flags.length}}`;
    badge.title = cell.flags.map(f => f.type + ': ' + f.text).join('\\n\\n');
    badge.onclick = (e) => {{ e.stopPropagation(); openCellModal(cid); }};
    top.appendChild(badge);
  }}
  inner.appendChild(top);

  // preview text (hover for full text in popover; can highlight to override excerpt)
  const preview = document.createElement('div');
  preview.className = 'cell-preview';
  const isCustomExcerpt = !!stateCell.excerpt;
  const previewText = stateCell.excerpt || (cell.text.length > 220 ? cell.text.slice(0, 220) + '…' : cell.text);
  if (isCustomExcerpt) {{
    preview.innerHTML = `<span class="cell-excerpt-marker" title="Custom excerpt — hover for full text">★</span>${{escapeHtml(previewText)}}`;
  }} else {{
    preview.textContent = previewText;
  }}
  attachHoverHandlers(preview, cid);
  inner.appendChild(preview);

  // notes textarea
  const notes = document.createElement('textarea');
  notes.className = 'cell-notes-input';
  notes.placeholder = 'coding notes…';
  notes.value = stateCell.notes || '';
  notes.oninput = (e) => {{
    e.stopPropagation();
    STATE.cells[cid] = STATE.cells[cid] || {{}};
    STATE.cells[cid].notes = notes.value;
    saveState();
  }};
  notes.onclick = (e) => e.stopPropagation();
  inner.appendChild(notes);

  return inner;
}}

function renderCell(cid) {{
  const td = document.getElementById('tc-' + cid);
  if (td) {{
    td.innerHTML = '';
    td.appendChild(buildCellInner(cid));
  }}
}}
function renderAllTables() {{ renderTabs(); }}

// ---- hover popover (full text + highlight-to-excerpt) ----
let HOVER_POPOVER = null;
let HOVER_SHOW_TIMER = null;
let HOVER_HIDE_TIMER = null;

function attachHoverHandlers(preview, cid) {{
  preview.addEventListener('mouseenter', () => {{
    clearTimeout(HOVER_HIDE_TIMER);
    HOVER_SHOW_TIMER = setTimeout(() => showPopover(cid, preview), 320);
  }});
  preview.addEventListener('mouseleave', () => {{
    clearTimeout(HOVER_SHOW_TIMER);
    HOVER_HIDE_TIMER = setTimeout(hidePopover, 280);
  }});
}}

function hidePopover() {{
  clearTimeout(HOVER_SHOW_TIMER);
  if (HOVER_POPOVER) {{
    HOVER_POPOVER.remove();
    HOVER_POPOVER = null;
  }}
}}

function showPopover(cid, anchorEl) {{
  clearTimeout(HOVER_HIDE_TIMER);
  if (HOVER_POPOVER) HOVER_POPOVER.remove();

  const cell = DATA.cells[cid];
  const stateCell = STATE.cells[cid] || {{}};
  const sid = cell.sid;
  const flagsHtml = (cell.flags || []).map(f =>
    `<div class="popover-flag"><span class="popover-flag-tag">${{escapeHtml(f.type)}}:</span> ${{escapeHtml(f.text)}}</div>`
  ).join('');
  const patternText = STATE.patterns[sid];
  const patternHtml = patternText ? `<div class="popover-pattern"><span class="popover-pattern-label">pattern:</span> ${{escapeHtml(patternText)}}</div>` : '';
  const resetBtn = stateCell.excerpt ? `<button class="popover-btn reset" id="popover-reset-btn">Reset excerpt</button>` : '';

  const pop = document.createElement('div');
  pop.className = 'hover-popover';
  pop.innerHTML = `
    <div class="popover-meta">${{cell.sid}} · ${{escapeHtml(DATA.student_names[sid])}} · ${{cell.model}} · ${{cell.condition}}</div>
    <div class="popover-actions-top">
      <button class="popover-btn" id="popover-set-btn">↑ Set selected text as cell preview</button>
      ${{resetBtn}}
      <span class="popover-hint">select text below, then click "Set"</span>
    </div>
    ${{patternHtml}}
    <div class="popover-body" id="popover-body">${{escapeHtml(cell.text)}}</div>
    ${{flagsHtml ? `<div class="popover-flags">${{flagsHtml}}</div>` : ''}}
  `;
  document.body.appendChild(pop);
  HOVER_POPOVER = pop;

  // position to the right of the cell, or left if no room
  const r = anchorEl.getBoundingClientRect();
  const popW = 540;
  let left = r.right + 12;
  if (left + popW > window.innerWidth - 20) left = Math.max(10, r.left - popW - 12);
  pop.style.left = left + 'px';
  let top = r.top + window.scrollY;
  // clamp vertically so the popover stays in the viewport
  const popHeight = Math.min(window.innerHeight - 40, 600);
  pop.style.maxHeight = popHeight + 'px';
  if (top + popHeight > window.scrollY + window.innerHeight - 20) {{
    top = window.scrollY + window.innerHeight - popHeight - 20;
  }}
  if (top < window.scrollY + 10) top = window.scrollY + 10;
  pop.style.top = top + 'px';

  pop.addEventListener('mouseenter', () => clearTimeout(HOVER_HIDE_TIMER));
  pop.addEventListener('mouseleave', () => {{
    HOVER_HIDE_TIMER = setTimeout(hidePopover, 280);
  }});

  // capture selection BEFORE focus changes by using mousedown
  document.getElementById('popover-set-btn').addEventListener('mousedown', (e) => {{
    e.preventDefault();
    const text = window.getSelection().toString().trim();
    if (!text) {{
      const btn = e.target;
      const orig = btn.textContent;
      btn.textContent = 'select text first';
      btn.style.background = '#c2941f';
      setTimeout(() => {{ btn.textContent = orig; btn.style.background = ''; }}, 1400);
      return;
    }}
    STATE.cells[cid] = STATE.cells[cid] || {{}};
    STATE.cells[cid].excerpt = text;
    saveState();
    renderCell(cid);
    e.target.textContent = '✓ saved as preview';
    setTimeout(() => {{ if (HOVER_POPOVER) hidePopover(); }}, 700);
  }});

  const resetBtnEl = document.getElementById('popover-reset-btn');
  if (resetBtnEl) {{
    resetBtnEl.addEventListener('click', () => {{
      if (STATE.cells[cid]) {{
        delete STATE.cells[cid].excerpt;
        saveState();
        renderCell(cid);
      }}
      hidePopover();
    }});
  }}
}}

// ---- cell modal (kept for cross-view drill-through; not used on main table now) ----
let CURRENT_CID = null;
function openCellModal(cid) {{
  CURRENT_CID = cid;
  const cell = DATA.cells[cid];
  const stateCell = STATE.cells[cid] || {{}};
  const sid = cell.sid;
  const optionsHtml = `<option value="">— select —</option>` + STATE.categories.map(c =>
    `<option value="${{c.id}}" ${{stateCell.category === c.id ? 'selected' : ''}}>${{escapeHtml(c.label)}}</option>`
  ).join('');
  const flagsHtml = (cell.flags || []).map(f =>
    `<div class="modal-flag"><span class="modal-flag-tag">${{escapeHtml(f.type)}}:</span> ${{escapeHtml(f.text)}}</div>`
  ).join('');
  const html = `
    <h2>${{sid}} · ${{escapeHtml(DATA.student_names[sid])}}</h2>
    <div class="modal-meta">model: ${{cell.model}} · condition: ${{cell.condition}} · ${{escapeHtml(DATA.cond_labels[cell.condition])}}</div>
    <div class="modal-pattern">
      <label>Qualitative pattern this student represents</label>
      <textarea oninput="STATE.patterns['${{sid}}']=this.value;saveState();">${{escapeHtml(STATE.patterns[sid] || '')}}</textarea>
    </div>
    ${{DATA.cross_notes[sid] ? `<div class="modal-cross-note"><strong>cross-condition synthesis:</strong> ${{escapeHtml(DATA.cross_notes[sid])}}</div>` : ''}}
    <h3>Model output</h3>
    <div class="modal-output">${{escapeHtml(cell.text)}}</div>
    ${{flagsHtml ? `<div class="modal-flags">${{flagsHtml}}</div>` : ''}}
    <div class="modal-coding">
      <label>Coding category</label>
      <select id="modal-cat" onchange="setCellCategory(this.value)">${{optionsHtml}}</select>
      <label>Notes (open-ended)</label>
      <textarea id="modal-notes" oninput="setCellNotes(this.value)">${{escapeHtml(stateCell.notes || '')}}</textarea>
    </div>
    <div class="modal-actions">
      <button class="secondary" onclick="openCross('${{sid}}')">View this student across all conditions</button>
      <button class="secondary" onclick="navCell(-1)">◀ prev cell</button>
      <button class="secondary" onclick="navCell(1)">next cell ▶</button>
      <button class="primary" onclick="closeCellModal()">Close</button>
    </div>
  `;
  document.getElementById('cell-modal-content').innerHTML = html;
  document.getElementById('cell-modal').classList.add('show');
}}
function closeCellModal() {{
  document.getElementById('cell-modal').classList.remove('show');
  if (CURRENT_CID) renderCell(CURRENT_CID);
  CURRENT_CID = null;
}}
function setCellCategory(catId) {{
  if (!CURRENT_CID) return;
  STATE.cells[CURRENT_CID] = STATE.cells[CURRENT_CID] || {{}};
  STATE.cells[CURRENT_CID].category = catId;
  saveState();
}}
function setCellNotes(notes) {{
  if (!CURRENT_CID) return;
  STATE.cells[CURRENT_CID] = STATE.cells[CURRENT_CID] || {{}};
  STATE.cells[CURRENT_CID].notes = notes;
  saveState();
}}
function navCell(delta) {{
  if (!CURRENT_CID) return;
  const all = Object.keys(DATA.cells);
  const idx = all.indexOf(CURRENT_CID);
  const nx = (idx + delta + all.length) % all.length;
  closeCellModal();
  openCellModal(all[nx]);
}}

// ---- cross-condition modal ----
function openCross(sid) {{
  const optionsHtml = STATE.categories.map(c =>
    `<option value="${{c.id}}">${{escapeHtml(c.label)}}</option>`
  ).join('');
  let grid = `<h2>${{sid}} · ${{escapeHtml(DATA.student_names[sid])}} — all conditions × models</h2>`;
  grid += `<div class="modal-pattern"><label>Qualitative pattern</label><textarea oninput="STATE.patterns['${{sid}}']=this.value;saveState();">${{escapeHtml(STATE.patterns[sid] || '')}}</textarea></div>`;
  if (DATA.cross_notes[sid]) grid += `<div class="modal-cross-note">${{escapeHtml(DATA.cross_notes[sid])}}</div>`;
  grid += `<div class="cross-grid">`;
  grid += `<div class="cross-header"></div>`;
  DATA.models.forEach(m => {{ grid += `<div class="cross-header">${{m}}</div>`; }});
  DATA.conds.forEach(cond => {{
    grid += `<div class="cross-header" style="text-align:left;">${{cond}}</div>`;
    DATA.models.forEach(m => {{
      const cid = `${{sid}}_${{m}}_${{cond}}`;
      const cell = DATA.cells[cid];
      const stateCell = STATE.cells[cid] || {{}};
      const cat = stateCell.category ? categoryById(stateCell.category) : null;
      const bg = cat ? cat.color : '#fff';
      const tag = cat ? `<span class="cell-tag">${{escapeHtml(cat.label)}}</span><br>` : '';
      const flagIcon = (cell.flags && cell.flags.length) ? `<span class="cell-flag-icon">⚑</span>` : '';
      grid += `<div class="cross-cell" style="background:${{bg}}" onclick="closeCrossModal();openCellModal('${{cid}}')">${{flagIcon}}${{tag}}${{escapeHtml(cell.text)}}</div>`;
    }});
  }});
  grid += `</div>`;
  grid += `<div class="modal-actions"><button class="primary" onclick="closeCrossModal()">Close</button></div>`;
  document.getElementById('cross-modal-content').innerHTML = grid;
  document.getElementById('cross-modal').classList.add('show');
}}
function closeCrossModal() {{
  document.getElementById('cross-modal').classList.remove('show');
}}

// ---- export/import ----
function exportState() {{
  const blob = new Blob([JSON.stringify(STATE, null, 2)], {{type: 'application/json'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'variant_a_coding_state_' + new Date().toISOString().slice(0,10) + '.json';
  a.click();
  URL.revokeObjectURL(url);
}}
function importState() {{
  const inp = document.createElement('input');
  inp.type = 'file';
  inp.accept = 'application/json';
  inp.onchange = (e) => {{
    const f = e.target.files[0];
    if (!f) return;
    const r = new FileReader();
    r.onload = () => {{
      try {{
        STATE = JSON.parse(r.result);
        saveState();
        renderCategoriesEditor();
        renderPatternsEditor();
        renderAllTables();
        alert('Imported.');
      }} catch (err) {{
        alert('Import failed: ' + err.message);
      }}
    }};
    r.readAsText(f);
  }};
  inp.click();
}}

// ---- utils ----
function escapeHtml(s) {{
  return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}}

// ---- keyboard ----
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') {{
    closeCellModal();
    closeCrossModal();
  }}
  if (CURRENT_CID) {{
    if (e.key === 'ArrowLeft' && e.altKey) navCell(-1);
    if (e.key === 'ArrowRight' && e.altKey) navCell(1);
  }}
}});

// ---- init ----
renderCategoriesEditor();
renderPatternsEditor();
renderAllTables();
updateProgress();
</script>
</body>
</html>
"""


def main():
    by_cond = load_all()
    out_html = build_html(by_cond)
    OUT_HTML.write_text(out_html, encoding="utf-8")
    print(f"Wrote {OUT_HTML} ({OUT_HTML.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
