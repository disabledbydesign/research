#!/usr/bin/env python3
"""Build unified-genob coding workshop.

Three per-condition tabs (both / single / neither), each showing the
Gemma 12B observation + Opus codes + Gemini codes + June's coding cell.
A fourth "3-way comparison" tab pulls from June's localStorage coding
for all three conditions side-by-side.

Usage:
    python scripts/build_unified_genob_coding_workshop.py

Reads from data/raw_outputs/ and data_tables/unified_ai_coding_2026-05-13/.
Writes data_tables/unified_genob_coding_workshop_2026-05-13.html
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw_outputs"
CODING_DIR = ROOT / "data_tables/unified_ai_coding_2026-05-13"
CORPUS_REVIEW = ROOT / "data_tables/corpus_overview/corpus_review_state.json"
OUT = ROOT / "data_tables/unified_genob_coding_workshop_2026-05-13.html"

CONDITIONS = ["both", "single", "neither"]
GENOB_FILES = {
    "both":    RAW / "test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_0739.json",
    "single":  RAW / "test_unified_genob_single_FULL_CORPUS_gemma12b_2026-05-13_0822.json",
    "neither": RAW / "test_unified_genob_neither_FULL_CORPUS_gemma12b_2026-05-13_0905.json",
}
OPUS_FILES = {
    "both":    CODING_DIR / "opus_unified_genob_both_2026-05-13.json",
    "single":  CODING_DIR / "opus_unified_genob_single_2026-05-13.json",
    "neither": CODING_DIR / "opus_unified_genob_neither_2026-05-13.json",
}
GEMINI_FILE = CODING_DIR / "gemini_unified_genob_2026-05-13.json"
SEED_VOCAB_FILE = ROOT / "data_tables/hand_coding/JB_variant_a_coding_state_2026-05-11.json"


def _sort_key(sid: str):
    prefix = 0 if sid.startswith("S") else 1
    try:
        num = int(sid[2:] if sid.startswith("WB") else sid[1:])
    except ValueError:
        num = 999
    return (prefix, num)


def load_observations(cond: str) -> dict:
    """Returns {sid: {name, observation, reasoning, confidence}}"""
    path = GENOB_FILES[cond]
    raw = json.loads(path.read_text())
    out = {}
    for r in raw["results"]:
        if r.get("run") != 1:
            continue
        sid = r["student_id"]
        out[sid] = {
            "name": r.get("student_name", ""),
            "observation": r.get("observation", ""),
            "reasoning": r.get("reasoning", ""),
            "confidence": r.get("confidence", 0.0),
            "source": r.get("source", ""),
        }
    return out


def load_agent_codes(path: Path) -> dict:
    """Returns {cell_key: code_entry}"""
    d = json.loads(path.read_text())
    return d.get("codes", {})


def load_seed_vocab() -> list:
    """Returns June's existing code vocabulary from variant_a coding state."""
    if not SEED_VOCAB_FILE.exists():
        return []
    d = json.loads(SEED_VOCAB_FILE.read_text())
    return d.get("categories", [])


def load_corpus_review() -> dict:
    d = json.loads(CORPUS_REVIEW.read_text())
    out = {}
    for key, val in d.items():
        for prefix in ("pattern_", "expected_", "notes_", "reviewed_"):
            if key.startswith(prefix):
                sid = key[len(prefix):]
                if sid not in out:
                    out[sid] = {}
                out[sid][prefix.rstrip("_")] = val
                break
    return out


def js(obj) -> str:
    return json.dumps(obj, ensure_ascii=False)


def build() -> str:
    obs = {c: load_observations(c) for c in CONDITIONS}
    opus = {c: load_agent_codes(OPUS_FILES[c]) for c in CONDITIONS}
    gemini_all = load_agent_codes(GEMINI_FILE)
    corpus_review = load_corpus_review()
    seed_vocab = load_seed_vocab()

    all_sids = sorted(
        set().union(*[set(v.keys()) for v in obs.values()]),
        key=_sort_key
    )

    # Embed all data as JS
    obs_js = js(obs)
    opus_js = js(opus)
    gemini_js = js(gemini_all)
    sids_js = js(all_sids)
    cr_js = js(corpus_review)
    seed_vocab_js = js(seed_vocab)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Unified Genob Coding Workshop — 2026-05-13</title>
<style>
* {{ box-sizing: border-box; }}
body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 2400px; margin: 0.8em auto; padding: 0 0.8em; line-height: 1.5; color: #222; background: #fafaf7; }}
h1 {{ font-size: 1.15em; margin-bottom: 0.1em; }}
.subtitle {{ font-size: 0.83em; color: #666; margin-bottom: 0.6em; }}

/* Controls */
.controls-bar {{ position: sticky; top: 0; background: #fafaf7; padding: 0.3em 0; z-index: 30; border-bottom: 1px solid #ddd; margin-bottom: 0.4em; display: flex; align-items: center; gap: 0.4em; flex-wrap: wrap; }}
.controls-bar button {{ padding: 0.25em 0.6em; cursor: pointer; font-family: Georgia, serif; font-size: 0.81em; border: 1px solid #bbb; border-radius: 3px; background: #fff; }}
.controls-bar button.primary {{ background: #1a4a7e; color: #fff; border-color: #1a4a7e; }}
.controls-bar .progress {{ font-size: 0.8em; color: #666; margin-left: 0.4em; }}

/* Tabs */
.tabs {{ display: flex; gap: 2px; margin-top: 0.4em; flex-wrap: wrap; }}
.tab {{ padding: 0.4em 1em; background: #e0ddd5; border: 1px solid #bbb; border-bottom: none; border-radius: 4px 4px 0 0; cursor: pointer; font-size: 0.84em; white-space: nowrap; }}
.tab.active {{ background: #fff; font-weight: bold; position: relative; top: 1px; border-bottom: 2px solid #fff; z-index: 1; }}
.tab.comp-tab {{ background: #dde9f5; color: #1a4a7e; }}
.tab.comp-tab.active {{ background: #edf2fb; }}
.tab-content {{ display: none; border: 1px solid #bbb; border-radius: 0 4px 4px 4px; padding: 0.5em; background: #fff; }}
.tab-content.active {{ display: block; }}

/* Coding table */
table.coding {{ border-collapse: collapse; width: 100%; table-layout: fixed; margin-top: 0.3em; }}
table.coding th, table.coding td {{ border: 1px solid #ccc; padding: 0; vertical-align: top; }}
table.coding th {{ background: #ececec; font-weight: bold; padding: 0.32em 0.42em; font-size: 0.79em; position: sticky; top: 36px; z-index: 10; }}
table.coding th.student-col {{ width: 190px; font-family: 'Courier New', monospace; background: #e4e0d6; }}
table.coding th.obs-col {{ font-family: 'Courier New', monospace; width: 360px; }}
table.coding th.agent-col {{ background: #edf2fb; font-family: 'Courier New', monospace; font-size: 0.75em; color: #1a4a7e; }}
table.coding th.opus-col {{ background: #f3eef9; color: #5e3a89; }}
table.coding th.gemini-col {{ background: #eaf3f9; color: #1a5a7e; }}
table.coding th.june-col {{ background: #f5ecd9; font-family: 'Courier New', monospace; color: #6c4f0a; }}

/* Student cell */
td.student-cell {{ padding: 0.45em 0.5em; background: #f7f4ee; font-size: 0.79em; vertical-align: top; }}
.sid {{ font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.97em; }}
.sname {{ color: #555; font-size: 0.87em; }}
.badges {{ display: flex; gap: 0.25em; flex-wrap: wrap; margin: 0.1em 0 0.2em; }}
.wb-badge {{ display: inline-block; background: #c2941f; color: #fff; font-size: 0.67em; padding: 0.07em 0.33em; border-radius: 3px; font-family: 'Courier New', monospace; }}
.exp-badge {{ display: inline-block; color: #fff; font-size: 0.67em; padding: 0.07em 0.33em; border-radius: 3px; font-family: 'Courier New', monospace; font-weight: bold; }}
.pattern-box {{ background: #fffbeb; border: 1px solid #e6d28a; border-radius: 3px; padding: 0.28em 0.36em; margin-top: 0.25em; font-size: 0.75em; color: #4a3800; line-height: 1.4; }}
.notes-box {{ font-size: 0.73em; color: #5a4500; font-style: italic; margin-top: 0.2em; }}

/* Observation cell */
td.obs-cell {{ height: 240px; position: relative; padding: 0.32em 0.42em; font-size: 0.8em; overflow: hidden; cursor: pointer; }}
td.obs-cell:hover {{ background: rgba(26,74,126,0.03); }}
td.obs-cell.wb-flag {{ box-shadow: inset 5px 0 0 0 #c2941f; }}
td.obs-cell.wb-ambiguous {{ box-shadow: inset 5px 0 0 0 #d4a017; }}
td.obs-cell.wb-clear {{ box-shadow: inset 5px 0 0 0 #b8d4b8; }}
.cell-preview {{ height: 100%; overflow-y: auto; font-family: Georgia, serif; line-height: 1.38; font-size: 0.94em; user-select: none; }}
.conf-mini {{ display: inline-block; font-family: 'Courier New', monospace; font-size: 0.7em; color: #999; margin-top: 0.3em; }}
mark.lbq-opus {{ background: #ffe082; padding: 0 1px; border-radius: 2px; }}
mark.lbq-gemini {{ background: #b8d8ff; padding: 0 1px; border-radius: 2px; }}

/* Agent codes cell */
td.agent-cell {{ height: 240px; padding: 0.42em 0.55em; font-size: 0.86em; vertical-align: top; overflow-y: auto; line-height: 1.4; }}
td.opus-cell {{ background: #f8f4fc; }}
td.gemini-cell {{ background: #f1f7fb; }}
.agent-coder-label {{ font-family: 'Courier New', monospace; font-size: 0.78em; color: #666; text-transform: uppercase; font-weight: bold; letter-spacing: 0.04em; margin-bottom: 0.18em; }}
.wb-pill {{ display: inline-block; font-size: 0.78em; padding: 0.1em 0.5em; border-radius: 3px; font-family: 'Courier New', monospace; font-weight: bold; letter-spacing: 0.02em; margin-bottom: 0.2em; }}
.wb-pill-concern_surfaced {{ background: #c2941f; color: #fff; }}
.wb-pill-ambiguous {{ background: #d4a017; color: #fff; }}
.wb-pill-no {{ background: #5fa05f; color: #fff; }}
.agent-reason {{ color: #555; font-size: 0.9em; font-style: italic; line-height: 1.4; margin-bottom: 0.22em; }}
.emergent-chips {{ display: flex; flex-wrap: wrap; gap: 0.2em; margin: 0.2em 0; }}
.category-line {{ font-size: 0.85em; font-style: italic; color: #555; margin: 0.18em 0; line-height: 1.4; }}
.wb-chip {{ font-size: 0.78em; padding: 0.08em 0.45em; background: #fff3cd; color: #5a4500; border-radius: 8px; font-family: 'Courier New', monospace; }}
.agent-notes {{ color: #333; font-size: 0.92em; line-height: 1.42; margin-top: 0.22em; }}
.no-data {{ color: #ccc; font-style: italic; font-size: 0.8em; }}

/* June coding cell */
td.june-cell {{ height: 240px; background: #fdf8ec; padding: 0.38em 0.45em; vertical-align: top; }}
.june-inner {{ height: 100%; display: flex; flex-direction: column; gap: 4px; }}
.june-label {{ font-family: 'Courier New', monospace; font-size: 0.7em; color: #8b6914; text-transform: uppercase; margin-bottom: 0.05em; }}
.june-inner select {{ font-family: Georgia, serif; font-size: 0.86em; padding: 0.25em 0.3em; border: 1px solid #888; background: #fff; width: 100%; border-radius: 3px; }}
.june-inner textarea {{ flex: 1; min-height: 60px; font-family: Georgia, serif; font-size: 0.85em; padding: 0.3em; border: 1px solid #888; resize: none; background: #fff; line-height: 1.4; border-radius: 3px; }}
.june-inner textarea:focus, .june-inner select:focus {{ outline: 2px solid #5a8ec9; }}
.autosave-hint {{ font-size: 0.82em; color: #aaa; font-style: italic; text-transform: none; letter-spacing: 0; font-weight: normal; }}
.cell-foot {{ display: flex; justify-content: space-between; align-items: center; min-height: 1.2em; }}
.save-indicator {{ font-family: 'Courier New', monospace; font-size: 0.72em; color: #5a8e3a; transition: opacity 0.3s; }}
.save-indicator.flash {{ color: #2a8e1a; font-weight: bold; }}

/* Manage codes modal */
.modal-backdrop {{ position: fixed; inset: 0; background: rgba(0,0,0,0.4); z-index: 1000; display: none; align-items: center; justify-content: center; }}
.modal-backdrop.active {{ display: flex; }}
.modal {{ background: #fff; width: 720px; max-width: 95vw; max-height: 88vh; overflow-y: auto; border-radius: 8px; padding: 1em 1.3em; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }}
.modal h2 {{ margin: 0 0 0.4em; font-size: 1.1em; }}
.modal .modal-subtitle {{ font-size: 0.85em; color: #666; margin-bottom: 0.8em; }}
.modal .codes-list {{ display: flex; flex-direction: column; gap: 0.35em; margin-bottom: 0.8em; }}
.modal .code-row {{ display: flex; gap: 0.4em; align-items: center; padding: 0.3em 0.4em; border: 1px solid #ddd; border-radius: 4px; }}
.modal .code-color {{ width: 24px; height: 24px; border-radius: 4px; border: 1px solid #888; cursor: pointer; flex-shrink: 0; }}
.modal .code-label-input {{ flex: 1; padding: 0.3em; font-family: Georgia, serif; font-size: 0.9em; border: 1px solid #ccc; border-radius: 3px; }}
.modal .code-id {{ font-family: 'Courier New', monospace; font-size: 0.72em; color: #999; min-width: 70px; }}
.modal .code-del {{ padding: 0.25em 0.55em; background: #c0392b; color: #fff; border: none; border-radius: 3px; cursor: pointer; font-size: 0.8em; }}
.modal .modal-actions {{ display: flex; gap: 0.5em; justify-content: flex-end; padding-top: 0.6em; border-top: 1px solid #eee; }}
.modal .modal-actions button {{ padding: 0.4em 1em; border-radius: 4px; border: 1px solid #888; background: #fff; cursor: pointer; font-family: Georgia, serif; }}
.modal .modal-actions button.primary {{ background: #1a4a7e; color: #fff; border-color: #1a4a7e; }}
.modal .add-code-row {{ display: flex; gap: 0.4em; padding: 0.4em; background: #f7f7f0; border-radius: 4px; margin-bottom: 0.8em; }}
.modal .add-code-row input {{ flex: 1; padding: 0.3em; border: 1px solid #ccc; border-radius: 3px; }}
.modal .add-code-row button {{ padding: 0.3em 0.8em; background: #5a8e3a; color: #fff; border: none; border-radius: 3px; cursor: pointer; }}

/* Comparison tab */
table.comp-table {{ border-collapse: collapse; width: 100%; table-layout: fixed; margin-top: 0.3em; }}
table.comp-table th, table.comp-table td {{ border: 1px solid #ccc; padding: 0; vertical-align: top; }}
table.comp-table th {{ background: #ececec; font-weight: bold; padding: 0.32em 0.5em; font-size: 0.79em; position: sticky; top: 36px; z-index: 10; }}
table.comp-table th.student-col {{ width: 190px; font-family: 'Courier New', monospace; background: #e4e0d6; }}
table.comp-table th.cond-col {{ font-family: 'Courier New', monospace; font-size: 0.78em; background: #dde9f5; color: #1a4a7e; }}
table.comp-table td.comp-student {{ padding: 0.4em 0.5em; background: #f7f4ee; font-size: 0.79em; vertical-align: top; }}
table.comp-table td.comp-obs {{ padding: 0.4em 0.5em; font-size: 0.8em; vertical-align: top; min-height: 180px; }}
.comp-obs-text {{ font-family: Georgia, serif; line-height: 1.42; color: #222; }}
.comp-june-code {{ margin-top: 0.5em; padding: 0.28em 0.4em; background: #fdf8ec; border: 1px solid #e0c96a; border-radius: 3px; font-size: 0.75em; }}
.comp-june-wb {{ display: inline-block; font-size: 0.8em; padding: 0.05em 0.4em; border-radius: 3px; font-family: 'Courier New', monospace; font-weight: bold; }}
.comp-june-notes {{ color: #5a4500; font-style: italic; margin-top: 0.12em; font-size: 0.9em; }}
.comp-no-code {{ color: #bbb; font-style: italic; font-size: 0.8em; }}
.comp-refresh-note {{ font-size: 0.8em; color: #888; margin-bottom: 0.4em; }}

/* Hover popover */
.hover-popover {{ position: fixed; z-index: 200; width: 540px; background: #fff; border: 1px solid #555; border-radius: 5px; box-shadow: 0 8px 28px rgba(0,0,0,0.22); padding: 0.65em 0.85em; font-size: 0.86em; line-height: 1.5; pointer-events: none; }}
.popover-meta {{ font-family: 'Courier New', monospace; font-size: 0.75em; color: #555; margin-bottom: 0.25em; }}
.popover-body {{ white-space: pre-wrap; font-family: Georgia, serif; max-height: 48vh; overflow-y: auto; padding: 0.4em 0.5em; background: #fafafa; border: 1px solid #eee; border-radius: 3px; font-size: 0.9em; }}

/* WB row tint */
tr.wb-row td {{ background-color: #fffdf4; }}
tr.wb-row td.student-cell {{ background-color: #fef9e7; }}
tr.wb-row td.opus-cell {{ background-color: #fbf4f6; }}
tr.wb-row td.gemini-cell {{ background-color: #f1f7fa; }}
tr.wb-row td.june-cell {{ background-color: #fefbec; }}
</style>
</head>
<body>
<h1>Unified Genob Coding Workshop — 2026-05-13</h1>
<div class="subtitle">Gemma 12B · run=1 · 46 students · Opus + Gemini codes + your coding</div>

<div class="controls-bar">
  <button class="primary" onclick="exportJuneCodes()">Export my codes →</button>
  <button onclick="importJuneCodes()">Import my codes</button>
  <button onclick="openCodesModal()">Manage codes…</button>
  <button onclick="if(confirm('Clear all your coding?')){{localStorage.removeItem(LS_KEY);location.reload();}}">Reset my coding</button>
  <span class="progress" id="progress-label"></span>
</div>

<!-- Manage codes modal -->
<div class="modal-backdrop" id="codes-modal" onclick="if(event.target===this) closeCodesModal()">
  <div class="modal">
    <h2>Manage your codes</h2>
    <div class="modal-subtitle">These codes appear in the dropdown for every cell. Shared across workshops. Edit a label by typing; click the color swatch to change it; delete with the × button.</div>
    <div class="add-code-row">
      <input id="new-code-label" type="text" placeholder="New code label (e.g., 'asymmetric inference')">
      <input id="new-code-color" type="color" value="#fff3cd">
      <button onclick="addCode()">+ Add</button>
    </div>
    <div class="codes-list" id="codes-list"></div>
    <div class="modal-actions">
      <button onclick="closeCodesModal()">Done</button>
    </div>
  </div>
</div>

<div class="tabs" id="tabs">
  <div class="tab active" onclick="switchTab('both',this)">genob-both</div>
  <div class="tab" onclick="switchTab('single',this)">genob-single</div>
  <div class="tab" onclick="switchTab('neither',this)">genob-neither</div>
  <div class="tab comp-tab" onclick="switchTab('compare',this)">3-way comparison ↔</div>
</div>

<div id="tab-both" class="tab-content active"></div>
<div id="tab-single" class="tab-content"></div>
<div id="tab-neither" class="tab-content"></div>
<div id="tab-compare" class="tab-content"></div>

<!-- Hover popover -->
<div id="popover" class="hover-popover" style="display:none">
  <div class="popover-meta" id="popover-meta"></div>
  <div class="popover-body" id="popover-body"></div>
</div>

<script>
const OBS = {obs_js};
const OPUS = {opus_js};
const GEMINI = {gemini_js};
const SIDS = {sids_js};
const CR = {cr_js};
const SEED_VOCAB = {seed_vocab_js};
const LS_KEY = 'genob_unified_ws_2026-05-13';
const LS_VOCAB_KEY = 'jb_coding_vocab_shared';
const CONDITIONS = ['both','single','neither'];

// ---- Storage ----
function loadState() {{
  try {{ return JSON.parse(localStorage.getItem(LS_KEY) || '{{}}'); }} catch(e) {{ return {{}}; }}
}}
function saveState(s) {{
  localStorage.setItem(LS_KEY, JSON.stringify(s));
}}
function stateKey(sid, cond) {{ return sid + '__' + cond; }}

// ---- Vocabulary (codes June can apply) — shared across workshops ----
function loadVocab() {{
  try {{
    const stored = localStorage.getItem(LS_VOCAB_KEY);
    if (stored) return JSON.parse(stored);
  }} catch(e) {{}}
  // First load — seed with the variant_a codes
  saveVocab(SEED_VOCAB);
  return SEED_VOCAB.slice();
}}
function saveVocab(v) {{
  localStorage.setItem(LS_VOCAB_KEY, JSON.stringify(v));
}}
function nextCodeId() {{ return 'c' + Date.now() + Math.floor(Math.random()*1000); }}
function findCode(id) {{ return loadVocab().find(c => c.id === id); }}

// ---- Debounced autosave ----
const _saveTimers = {{}};
function scheduleSave(sid, cond, cell) {{
  const k = sid + '__' + cond;
  clearTimeout(_saveTimers[k]);
  _saveTimers[k] = setTimeout(() => saveJune(sid, cond, cell), 350);
}}

// ---- WB check-in aggregation ----
function aggWbClass(sid, cond) {{
  const cellKey = sid + '_gemma12b_unified_genob_' + cond;
  const opusWb = (OPUS[cond][cellKey] || {{}}).wellbeing_check_in || '';
  const geminiWb = (GEMINI[cellKey] || {{}}).wellbeing_check_in || '';
  if (opusWb === 'concern_surfaced' || geminiWb === 'concern_surfaced') return 'wb-flag';
  if (opusWb === 'ambiguous' || geminiWb === 'ambiguous') return 'wb-ambiguous';
  return 'wb-clear';
}}

// ---- Highlight load-bearing quotes ----
function highlightQuotes(text, opusQuotes, geminiQuotes) {{
  let escaped = text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  function esc(s) {{ return s.replace(/[.*+?^${{}}()|[\\]\\\\]/g,'\\\\$&'); }}
  for (const q of (opusQuotes||[])) {{
    if (!q) continue;
    const escQ = esc(q.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'));
    escaped = escaped.replace(new RegExp(escQ,'g'), '<mark class="lbq-opus">$&</mark>');
  }}
  for (const q of (geminiQuotes||[])) {{
    if (!q) continue;
    const escQ = esc(q.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'));
    escaped = escaped.replace(new RegExp(escQ,'g'), '<mark class="lbq-gemini">$&</mark>');
  }}
  return escaped;
}}

// ---- Render agent codes block ----
function renderAgentBlock(coder, entry, lbqClass) {{
  if (!entry) return '<div class="no-data">' + coder + ': —</div>';
  const wb = entry.wellbeing_check_in || '';
  const wbCls = 'wb-pill wb-pill-' + wb;
  const wbPill = wb ? '<span class="' + wbCls + '">' + wb + '</span>' : '';
  const reason = (entry.wellbeing_reason||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  const cats = (entry.categories||[]).map(c => c.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/-/g,' ').replace(/_/g,' ')).join(' · ');
  const wbCodes = (entry.wellbeing_codes||[]).map(c => '<span class="wb-chip">' + c.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') + '</span>').join('');
  const notes = (entry.notes||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  return '<div class="agent-coder-label">' + coder + '</div>'
    + wbPill
    + (reason ? '<div class="agent-reason">' + reason + '</div>' : '')
    + (wbCodes ? '<div class="emergent-chips">' + wbCodes + '</div>' : '')
    + (cats ? '<div class="category-line">' + cats + '</div>' : '')
    + (notes ? '<div class="agent-notes">' + notes + '</div>' : '');
}}

// ---- Render June coding cell ----
function renderJuneCell(sid, cond) {{
  const k = stateKey(sid, cond);
  const s = loadState();
  const saved = s[k] || {{}};
  const vocab = loadVocab();
  const selVal = (saved.category||'').replace(/"/g,'&quot;');
  const notesVal = (saved.notes||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const opts = [`<option value="">— select code —</option>`].concat(
    vocab.map(c => {{
      const lbl = c.label.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
      return `<option value="${{c.id}}"${{selVal===c.id?' selected':''}}>${{lbl}}</option>`;
    }})
  );
  const selCode = vocab.find(c => c.id === selVal);
  const selStyle = selCode ? `style="background:${{selCode.color}};border-color:#888"` : '';
  return `<div class="june-inner" data-sid="${{sid}}" data-cond="${{cond}}">
    <div class="june-label">Your code &amp; notes <span class="autosave-hint">· auto-saves</span></div>
    <select ${{selStyle}} onchange="scheduleSave('${{sid}}','${{cond}}',this.parentNode)">
      ${{opts.join('')}}
    </select>
    <textarea placeholder="notes, codes, observations…"
      oninput="scheduleSave('${{sid}}','${{cond}}',this.parentNode)"
      onblur="saveJune('${{sid}}','${{cond}}',this.parentNode)">${{notesVal}}</textarea>
    <div class="cell-foot">
      <span class="save-indicator" id="ind-${{sid}}-${{cond}}">${{saved.category||saved.notes ? '✓ saved' : ''}}</span>
    </div>
  </div>`;
}}

function saveJune(sid, cond, cell) {{
  const sel = cell.querySelector('select');
  const ta = cell.querySelector('textarea');
  const s = loadState();
  const k = stateKey(sid, cond);
  s[k] = {{ category: sel.value, notes: ta.value }};
  saveState(s);
  // Update select background to match category color
  const code = findCode(sel.value);
  if (code) {{
    sel.style.background = code.color;
    sel.style.borderColor = '#888';
  }} else {{
    sel.style.background = '#fff';
    sel.style.borderColor = '#888';
  }}
  const ind = cell.querySelector('.save-indicator');
  if (ind) {{
    ind.textContent = '✓ saved';
    ind.classList.add('flash');
    setTimeout(() => ind.classList.remove('flash'), 1000);
  }}
  updateProgress();
}}

// ---- Build condition tab ----
function buildCondTab(cond) {{
  const obsData = OBS[cond];
  const opusCodes = OPUS[cond];
  const rows = SIDS.map(sid => {{
    const entry = obsData[sid];
    if (!entry) return '';
    const cr = CR[sid] || {{}};
    const isWB = sid.startsWith('WB');
    const expColor = {{CRISIS:'#c0392b',BURNOUT:'#d68910',EDGE:'#c8a000',ENGAGED:'#5fa05f'}}[cr.expected] || '#888';
    const wbBadge = isWB ? '<span class="wb-badge">WB</span>' : '';
    const expBadge = cr.expected ? `<span class="exp-badge" style="background:${{expColor}}">${{cr.expected}}</span>` : '';
    const patt = (cr.pattern||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    const notes = (cr.notes||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    const name = (entry.name||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

    const cellKey = sid + '_gemma12b_unified_genob_' + cond;
    const opusEntry = opusCodes[cellKey];
    const geminiEntry = GEMINI[cellKey];

    const opusQuotes = (opusEntry||{{}}).load_bearing_quotes || [];
    const geminiQuotes = (geminiEntry||{{}}).load_bearing_quotes || [];
    const obsText = entry.observation || '';
    const obsHighlighted = highlightQuotes(obsText, opusQuotes, geminiQuotes);

    const conf = Math.round((entry.confidence||0) * 100);
    const confColor = conf >= 75 ? '#5fa05f' : conf >= 50 ? '#d68910' : '#c0392b';
    const wbClass = aggWbClass(sid, cond);
    const rowClass = isWB ? 'wb-row' : 'es-row';

    const studentCell = `<td class="student-cell">
      <div class="sid">${{sid}}</div>
      <div class="sname">${{name}}</div>
      <div class="badges">${{wbBadge}}${{expBadge}}</div>
      ${{patt ? `<div class="pattern-box">${{patt}}</div>` : ''}}
      ${{notes ? `<div class="notes-box">${{notes}}</div>` : ''}}
    </td>`;

    const obsCell = `<td class="obs-cell ${{wbClass}}" data-obs="${{obsText.replace(/"/g,'&quot;')}}" data-sid="${{sid}}" data-cond="${{cond}}"
      onmouseenter="showPopover(event,this)" onmouseleave="hidePopover()">
      <div class="cell-preview">${{obsHighlighted}}</div>
      <div class="conf-mini" style="color:${{confColor}}">${{conf}}%</div>
    </td>`;

    const opusCell = `<td class="agent-cell opus-cell">${{renderAgentBlock('Opus', opusEntry, 'lbq-opus')}}</td>`;
    const geminiCell = `<td class="agent-cell gemini-cell">${{renderAgentBlock('Gemini', geminiEntry, 'lbq-gemini')}}</td>`;

    const juneCell = `<td class="june-cell">${{renderJuneCell(sid, cond)}}</td>`;

    return `<tr class="${{rowClass}}" id="row-${{sid}}-${{cond}}">${{studentCell}}${{obsCell}}${{opusCell}}${{geminiCell}}${{juneCell}}</tr>`;
  }}).join('');

  return `<table class="coding">
  <colgroup>
    <col style="width:175px"><col style="width:340px"><col style="width:285px"><col style="width:285px"><col style="width:235px">
  </colgroup>
  <thead><tr>
    <th class="student-col">Student</th>
    <th class="obs-col">observation — genob-${{cond}}</th>
    <th class="agent-col opus-col">Opus <span style="font-size:0.85em;color:#aaa">· <mark class="lbq-opus" style="font-size:0.9em">quotes</mark></span></th>
    <th class="agent-col gemini-col">Gemini <span style="font-size:0.85em;color:#aaa">· <mark class="lbq-gemini" style="font-size:0.9em">quotes</mark></span></th>
    <th class="june-col">Your coding</th>
  </tr></thead>
  <tbody>${{rows}}</tbody>
</table>`;
}}

// ---- Build comparison tab ----
function buildCompTab() {{
  const state = loadState();
  const vocab = loadVocab();
  const codeById = Object.fromEntries(vocab.map(c => [c.id, c]));
  const rows = SIDS.map(sid => {{
    const cr = CR[sid] || {{}};
    const isWB = sid.startsWith('WB');
    const expColor = {{CRISIS:'#c0392b',BURNOUT:'#d68910',EDGE:'#c8a000',ENGAGED:'#5fa05f'}}[cr.expected] || '#888';
    const wbBadge = isWB ? '<span class="wb-badge">WB</span>' : '';
    const expBadge = cr.expected ? `<span class="exp-badge" style="background:${{expColor}}">${{cr.expected}}</span>` : '';
    const firstObs = OBS.both[sid] || OBS.single[sid] || OBS.neither[sid];
    const name = ((firstObs||{{}}).name||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    const patt = (cr.pattern||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

    const studentCell = `<td class="comp-student">
      <div class="sid">${{sid}}</div>
      <div class="sname">${{name}}</div>
      <div class="badges">${{wbBadge}}${{expBadge}}</div>
      ${{patt ? `<div class="pattern-box">${{patt}}</div>` : ''}}
    </td>`;

    const condCells = CONDITIONS.map(cond => {{
      const entry = OBS[cond][sid];
      const obsText = (entry||{{}}).observation || '';
      const escaped = obsText.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
      const k = stateKey(sid, cond);
      const saved = state[k] || {{}};
      const code = saved.category ? codeById[saved.category] : null;
      const codeLabel = code ? code.label : '';
      const codeColor = code ? code.color : '#eee';
      const hasContent = code || saved.notes;
      const juneHtml = hasContent
        ? `<div class="comp-june-code">${{code ? `<span class="comp-june-wb" style="background:${{codeColor}};color:#333;border:1px solid #999">${{codeLabel}}</span>` : ''}}
           ${{saved.notes ? `<div class="comp-june-notes">${{(saved.notes||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}}</div>` : ''}}</div>`
        : `<div class="comp-no-code">not yet coded</div>`;
      return `<td class="comp-obs">
        <div class="comp-obs-text">${{escaped}}</div>
        ${{juneHtml}}
      </td>`;
    }}).join('');

    const rowClass = isWB ? 'wb-row' : 'es-row';
    return `<tr class="${{rowClass}}">${{studentCell}}${{condCells}}</tr>`;
  }}).join('');

  return `<p class="comp-refresh-note">Showing your saved coding. Switch to a condition tab to update coding, then return here — <button style="font-size:0.85em;padding:0.18em 0.5em;cursor:pointer" onclick="refreshCompTab()">Refresh</button></p>
<table class="comp-table">
  <colgroup>
    <col style="width:190px"><col><col><col>
  </colgroup>
  <thead><tr>
    <th class="student-col">Student</th>
    <th class="cond-col">genob-both</th>
    <th class="cond-col">genob-single</th>
    <th class="cond-col">genob-neither</th>
  </tr></thead>
  <tbody>${{rows}}</tbody>
</table>`;
}}

// ---- Tab switching ----
function switchTab(cond, el) {{
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  if (el) el.classList.add('active');
  const tc = document.getElementById('tab-' + cond);
  if (tc) tc.classList.add('active');
  if (cond === 'compare') refreshCompTab();
  updateProgress();
}}

function refreshCompTab() {{
  document.getElementById('tab-compare').innerHTML = buildCompTab();
}}

// ---- Progress indicator ----
function updateProgress() {{
  const state = loadState();
  const total = SIDS.length * CONDITIONS.length;
  const coded = Object.keys(state).filter(k => state[k].category || state[k].notes).length;
  const lbl = document.getElementById('progress-label');
  if (lbl) lbl.textContent = `Coded: ${{coded}} / ${{total}} cells`;
}}

// ---- Manage codes modal ----
function openCodesModal() {{
  renderCodesList();
  document.getElementById('codes-modal').classList.add('active');
}}
function closeCodesModal() {{
  document.getElementById('codes-modal').classList.remove('active');
  // Re-render current tab so dropdowns pick up vocab changes
  const activeTab = document.querySelector('.tab.active');
  if (activeTab) {{
    const onclick = activeTab.getAttribute('onclick') || '';
    const m = onclick.match(/switchTab\\('([^']+)'/);
    if (m) {{
      const cond = m[1];
      if (cond === 'compare') refreshCompTab();
      else document.getElementById('tab-' + cond).innerHTML = buildCondTab(cond);
    }}
  }}
}}
function renderCodesList() {{
  const vocab = loadVocab();
  const list = document.getElementById('codes-list');
  list.innerHTML = vocab.map(c => `
    <div class="code-row" data-id="${{c.id}}">
      <input type="color" class="code-color" value="${{c.color}}" onchange="updateCodeColor('${{c.id}}', this.value)">
      <input type="text" class="code-label-input" value="${{(c.label||'').replace(/"/g,'&quot;')}}" onchange="updateCodeLabel('${{c.id}}', this.value)">
      <span class="code-id">${{c.id.length>14?c.id.slice(0,11)+'…':c.id}}</span>
      <button class="code-del" onclick="deleteCode('${{c.id}}')" title="Delete this code">×</button>
    </div>
  `).join('');
}}
function addCode() {{
  const label = document.getElementById('new-code-label').value.trim();
  const color = document.getElementById('new-code-color').value;
  if (!label) return;
  const vocab = loadVocab();
  vocab.push({{ id: nextCodeId(), label, color }});
  saveVocab(vocab);
  document.getElementById('new-code-label').value = '';
  renderCodesList();
}}
function updateCodeLabel(id, label) {{
  const vocab = loadVocab();
  const c = vocab.find(x => x.id === id);
  if (c) {{ c.label = label; saveVocab(vocab); }}
}}
function updateCodeColor(id, color) {{
  const vocab = loadVocab();
  const c = vocab.find(x => x.id === id);
  if (c) {{ c.color = color; saveVocab(vocab); }}
}}
function deleteCode(id) {{
  if (!confirm('Delete this code? Cells using it will keep their notes but lose the code.')) return;
  let vocab = loadVocab();
  vocab = vocab.filter(c => c.id !== id);
  saveVocab(vocab);
  renderCodesList();
}}

// ---- Export / import ----
function exportJuneCodes() {{
  const state = loadState();
  const out = {{
    schema: 'june_genob_coding',
    exported_at: new Date().toISOString(),
    categories: loadVocab(),
    cells: state
  }};
  const blob = new Blob([JSON.stringify(out, null, 2)], {{type:'application/json'}});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'june_genob_coding_2026-05-13.json';
  a.click();
}}

function importJuneCodes() {{
  const inp = document.createElement('input');
  inp.type = 'file'; inp.accept = '.json';
  inp.onchange = e => {{
    const f = e.target.files[0];
    if (!f) return;
    const r = new FileReader();
    r.onload = ev => {{
      try {{
        const d = JSON.parse(ev.target.result);
        if (d.categories) saveVocab(d.categories);
        const cells = d.cells || d.codes || d;
        saveState(cells);
        location.reload();
      }} catch(err) {{ alert('Could not parse: ' + err); }}
    }};
    r.readAsText(f);
  }};
  inp.click();
}}

// ---- Hover popover ----
function showPopover(e, cell) {{
  const text = cell.getAttribute('data-obs') || '';
  const sid = cell.getAttribute('data-sid');
  const cond = cell.getAttribute('data-cond');
  document.getElementById('popover-meta').textContent = sid + '  ·  genob-' + cond;
  document.getElementById('popover-body').textContent = text;
  const pop = document.getElementById('popover');
  pop.style.display = 'block';
  const x = Math.min(e.clientX + 20, window.innerWidth - 580);
  const y = Math.min(e.clientY + 10, window.innerHeight - 200);
  pop.style.left = x + 'px';
  pop.style.top = y + 'px';
}}
function hidePopover() {{
  document.getElementById('popover').style.display = 'none';
}}

// ---- Init ----
(function() {{
  for (const cond of CONDITIONS) {{
    document.getElementById('tab-' + cond).innerHTML = buildCondTab(cond);
  }}
  updateProgress();
}})();
</script>
</body>
</html>"""


def main():
    html = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Written: {OUT}")
    print(f"  {len(CONDITIONS)} condition tabs + 1 comparison tab")


if __name__ == "__main__":
    main()
