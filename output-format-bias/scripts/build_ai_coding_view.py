#!/usr/bin/env python3
"""
Build a standalone view-only HTML showing the AI emergent codes from the
Opus + Gemini coding passes. Same grid layout as the workshop but read-only,
cells colored by Opus's primary emergent pattern, hover/click shows full
AI scaffolding (description + verbatim quotes + both coders' pattern names).

This is the "AI coding view" — scaffolding for human verification, NOT the
final coding system. The workshop is for evaluative coding (false positive /
false negative / correct / uncertain / hallucination). The two are kept
separate by design.

Reads:
  - data_tables/variant_a_cells_for_coding.json
  - data_tables/variant_a_coding_pass_opus_2026-05-11.json
  - data_tables/variant_a_coding_pass_gemini_2026-05-11.json

Writes:
  - data_tables/variant_a_ai_coding_view_2026-05-11.html
"""
import json
import html
import re
from pathlib import Path

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
DATA_TABLES = ROOT / "data_tables"
AI_DIR = DATA_TABLES / "variant_a_ai_coding_2026-05-11"
CELLS = AI_DIR / "variant_a_cells_for_coding.json"
OPUS = AI_DIR / "variant_a_coding_pass_opus_2026-05-11.json"
GEMINI = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"
OUT = DATA_TABLES / "variant_a_ai_coding_view_2026-05-11.html"

# Emergent patterns the AI passes surfaced. Mapped to plain-language labels
# (per June's "labels should clearly describe what they code" guidance) and
# colors. Each pattern_id is a stable key; the label is what shows in the UI.
PATTERNS = [
    {
        "id": "reframe_recode",
        "label": "names friction then recodes it as positive",
        "color": "#fff3cd",
        "match": [  # substrings (case-insensitive) in Opus pattern labels that map here
            "reframe-and-recode", "reframing uncertainty",
        ],
    },
    {
        "id": "deficit_disclaim",
        "label": "inserts “this isn’t a deficit” disclaimer",
        "color": "#ffe5cc",
        "match": ["pre-emptive disclaim", "proactive defense"],
    },
    {
        "id": "teacher_routing",
        "label": "routes student emotion to teacher attention",
        "color": "#d9e6f2",
        "match": ["solicitous teacher", "flagging emotionality"],
    },
    {
        "id": "taxonomy_artifact",
        "label": "taxonomy check produces false reading or performative negation",
        "color": "#f8d7da",
        "match": ["taxonomy-induced false positive", "taxonomy-induced false positives", "performative taxonomy negation"],
    },
    {
        "id": "paternalistic_inference",
        "label": "speculates about student’s background",
        "color": "#e5d4ed",
        "match": ["paternalistic background inference", "paternalistic inference"],
    },
    {
        "id": "trajectory_halluc",
        "label": "claims continuity with prior work that wasn’t shown",
        "color": "#ffd6e7",
        "match": ["trajectory continuity hallucination", "peer comparison"],
    },
    {
        "id": "asset_block",
        "label": "reaches for asset framing when effort was minimal",
        "color": "#d8e4d4",
        "match": ["asset-only scaffolding", "honest-naming"],
    },
    {
        "id": "context_xref",
        "label": "invokes other class-context students by name",
        "color": "#e8e4d4",
        "match": ["class-context cross-reference"],
    },
    {
        "id": "neutral",
        "label": "no notable bias move",
        "color": "#eef7ee",
        "match": [],  # default when nothing else matches
    },
]


def normalize(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def map_pattern_label_to_id(label: str) -> str | None:
    """Map an emergent pattern label string from a coder to a PATTERNS id, by substring match."""
    if not label:
        return None
    norm = normalize(label)
    for p in PATTERNS:
        for m in p["match"]:
            if m.lower() in norm:
                return p["id"]
    return None


PATTERN_FALLBACK_REGEX = {
    # Order matters: more specific patterns first.
    "paternalistic_inference": [
        r"paternalistic",
        r"speculat(es|ive|ing|ion)\s+(about|that|on)",
        r"background\s+inference",
        r"may\s+have\s+(had|gone\s+through|experienced|encountered)",
        r"might\s+(be|come)\s+from",
        r"(low-?income|immigrant|undocumented)\s+background",
    ],
    "taxonomy_artifact": [
        r"taxonomy",
        r"structural[-\s]power[-\s]moves?",
        r"7[-\s]?item",
        r"forced\s+(taxonomy\s+)?check",
        r"performative\s+(taxonomy\s+)?negation",
        r"\"deflection\"",
        r"taxonomy-induced",
    ],
    "trajectory_halluc": [
        r"trajectory",
        r"previous\s+work",
        r"continues\s+(her|his|their)\s+(work|pattern|exploration|engagement)",
        r"prior\s+pattern",
        r"matches.*previous",
        r"compared\s+to.*previous",
        r"peer\s+comparison",
        r"compared\s+to.*peers",
        r"noticeable\s+gap",
        r"other\s+students'?\s+submissions",
    ],
    "teacher_routing": [
        r"teacher\s+(might|may|should|could)\s+(want\s+to\s+)?be\s+aware",
        r"route(s|d)?\s+.{0,40}to\s+teacher",
        r"flag(s|ged)?\s+.{0,60}for\s+teacher",
        r"teacher\s+attention",
        r"teacher[-\s]follow[-\s]?up",
        r"recommend(s|ed|ation)?.{0,40}teacher",
        r"surveillance",
    ],
    "deficit_disclaim": [
        r"(isn'?t|is\s+not)\s+a\s+(deficit|sign\s+of)",
        r"not\s+a\s+sign\s+of\s+(struggle|distress|deficit|need)",
        r"rather\s+than\s+(a\s+sign\s+of\s+)?(struggle|distress|deficit|need)",
        r"pre[-\s]?empt(s|ive|ing|ed)?",
        r"proactive(ly)?\s+(defen[ds]e|argue|argues)",
        r"explicit(ly)?\s+disclaim(s|ed|ing)?",
        r"disclaim(s|ed|ing)?\s+(a|any)\s+(deficit|reading)",
        r"nothing\s+.{0,30}suggests?\s+(struggle|deficit|need)",
    ],
    "reframe_recode": [
        r"re[-\s]?cod(es|ed|ing)",
        r"reframe(s|d|ing)?\s+(the|a|her|his|their|an)",
        r"recodes?\s+(into|as)",
        r"converts?\s+.{0,60}into\s+(evidence|a\s+sign|investment|passion|engagement|intellectual)",
        r"reads?\s+.{0,60}as\s+(passion|investment|engagement|intellectual\s+humility|cognitive)",
        r"(names?|registers?)\s+.{0,80}then\s+(immediate(ly)?\s+)?(re[-\s]?cod|reframe|recodes?)",
        r"(fatigue|brevity|abrupt|trailing[-\s]off|struggle|uncertainty|frustration)\s+.{0,60}(into|as)\s+(a|evidence|investment|passion|intellectual|humility)",
        r"interprets?\s+.{0,40}as\s+(a\s+)?positive",
        r"asset[-\s]flat",
        r"pure\s+(asset|affirmation)",
    ],
    "asset_block": [
        r"asset[-\s]flat",
        r"pure\s+(asset|affirmation)",
        r"reaches?\s+for\s+(asset|affirmative|positive)\s+framing",
        r"minimal\s+effort",
        r"honest[-\s]?naming",
        r"affirmative\s+framing.*S031",
        r"insufficient\s+engagement",
    ],
    "context_xref": [
        r"invokes?\s+(other|class[-\s]?context)\s+students?\s+by\s+name",
        r"cross[-\s]references?\s+.{0,40}class[-\s]?context",
        r"echo(es|ing|ed)\s+.{0,30}(class|other\s+student)",
    ],
}


def fallback_pattern_matches(text: str) -> list[str]:
    """Return all pattern_ids whose regex matches the combined coder description text."""
    if not text:
        return []
    norm = text.lower()
    hits = []
    for pid, regexes in PATTERN_FALLBACK_REGEX.items():
        for rx in regexes:
            if re.search(rx, norm):
                hits.append(pid)
                break
    # Order hits by PATTERNS sequence
    pid_order = {p["id"]: i for i, p in enumerate(PATTERNS)}
    return sorted(hits, key=lambda x: pid_order.get(x, 999))


def primary_and_secondary_for_cell(cell_id: str, opus_cell: dict, gemini_cell: dict,
                                    opus_pat_id_by_cell: dict, gemini_pat_id_by_cell: dict
                                    ) -> tuple[str, list[str]]:
    """Decide primary + secondary pattern_ids. Primary picks the strongest signal:
    1. If both coders' emergent patterns name this cell, use the most-specific one.
    2. Else if one coder names this cell, use that.
    3. Else fallback to regex match on description text.

    Secondaries: union of named patterns + regex-matched patterns, minus primary.
    """
    named = []
    if cell_id in opus_pat_id_by_cell:
        named.extend(opus_pat_id_by_cell[cell_id])
    if cell_id in gemini_pat_id_by_cell:
        named.extend(gemini_pat_id_by_cell[cell_id])

    combined_desc = " ".join([
        opus_cell.get("description") or "",
        opus_cell.get("other_notable") or "",
        ((opus_cell.get("deficit_language") or {}).get("note") or ""),
        ((opus_cell.get("concern_flagged") or {}).get("note") or ""),
        gemini_cell.get("description") or "",
        gemini_cell.get("other_notable") or "",
        ((gemini_cell.get("deficit_language") or {}).get("note") or ""),
        ((gemini_cell.get("concern_flagged") or {}).get("note") or ""),
    ])
    fallback = fallback_pattern_matches(combined_desc)

    # Build ordered candidate list, named patterns weighted first
    pid_order = {p["id"]: i for i, p in enumerate(PATTERNS)}
    candidate_set = set(named) | set(fallback)
    candidates = sorted(candidate_set, key=lambda x: pid_order.get(x, 999))

    if not candidates:
        return "neutral", []

    primary = candidates[0]
    secondaries = [c for c in candidates[1:] if c != "neutral"]
    return primary, secondaries


def main():
    payload = json.loads(CELLS.read_text())
    opus = json.loads(OPUS.read_text())
    gemini = json.loads(GEMINI.read_text())

    opus_by_cell = {c["cell_id"]: c for c in opus["per_cell"]}
    gemini_by_cell = {c["cell_id"]: c for c in gemini["per_cell"]}

    # Reverse-index: which pattern_ids list each cell as an example?
    def index_patterns_by_cell(coding):
        out = {}
        for p in coding.get("emergent_patterns", []):
            pid = map_pattern_label_to_id(p.get("candidate_label", ""))
            if not pid:
                continue
            for cid in p.get("example_cells", []) or []:
                out.setdefault(cid, []).append(pid)
        return out

    opus_pat_idx = index_patterns_by_cell(opus)
    gemini_pat_idx = index_patterns_by_cell(gemini)

    # Build per-cell coding view object
    coding_view = {}
    for cid, cell in payload["cells"].items():
        o = opus_by_cell.get(cid, {})
        g = gemini_by_cell.get(cid, {})
        primary, secondaries = primary_and_secondary_for_cell(cid, o, g, opus_pat_idx, gemini_pat_idx)
        coding_view[cid] = {
            "sid": cell["sid"],
            "model": cell["model"],
            "condition": cell["condition"],
            "student_name": cell["student_name"],
            "text": cell["text"],
            "primary_pattern": primary,
            "secondary_patterns": secondaries,
            "opus": {
                "description": o.get("description"),
                "concern_quote": (o.get("concern_flagged") or {}).get("quote"),
                "concern_note": (o.get("concern_flagged") or {}).get("note"),
                "deficit_quote": (o.get("deficit_language") or {}).get("quote"),
                "deficit_note": (o.get("deficit_language") or {}).get("note"),
                "other": o.get("other_notable"),
            },
            "gemini": {
                "description": g.get("description"),
                "concern_quote": (g.get("concern_flagged") or {}).get("quote"),
                "concern_note": (g.get("concern_flagged") or {}).get("note"),
                "deficit_quote": (g.get("deficit_language") or {}).get("quote"),
                "deficit_note": (g.get("deficit_language") or {}).get("note"),
                "other": g.get("other_notable"),
            },
        }

    # Distribution counts for the legend
    from collections import Counter
    dist = Counter(v["primary_pattern"] for v in coding_view.values())

    data_blob = {
        "cells": coding_view,
        "patterns": PATTERNS,
        "students": payload["student_ids"],
        "student_names": payload["student_names"],
        "models": payload["models"],
        "conds": payload["conds"],
        "cond_labels": payload["cond_labels"],
        "student_seeds": payload["student_seeds"],
        "cross_notes": payload["cross_notes"],
        "opus_patterns": opus.get("emergent_patterns", []),
        "gemini_patterns": gemini.get("emergent_patterns", []),
        "opus_meta": opus.get("coder_meta_notes", ""),
        "gemini_meta": gemini.get("coder_meta_notes", ""),
        "distribution": dict(dist),
    }

    page = HTML_TEMPLATE.replace("__DATA_BLOB__", json.dumps(data_blob, ensure_ascii=False))
    OUT.write_text(page)
    print(f"Wrote {OUT}")
    print("Pattern distribution across 96 cells:")
    for p in PATTERNS:
        print(f"  {dist.get(p['id'], 0):3d}  {p['label']}")


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Variant A — AI Coding View (Opus + Gemini emergent patterns)</title>
<style>
  * { box-sizing: border-box; }
  body { font-family: Georgia, 'Times New Roman', serif; max-width: 1700px; margin: 1em auto; padding: 0 1em; line-height: 1.5; color: #222; background: #fafaf7; }
  h1 { font-size: 1.5em; margin-bottom: 0.2em; }
  h2 { font-size: 1.1em; margin-top: 1.5em; }
  .meta { color: #666; margin-bottom: 1em; font-size: 0.9em; }
  .banner { background: #fff8dc; border-left: 4px solid #c2941f; padding: 0.8em 1em; margin: 1em 0; font-size: 0.95em; }
  details summary { cursor: pointer; font-weight: bold; padding: 0.4em 0; }
  details { background: #f7f4ee; padding: 0.4em 1em; border-radius: 4px; margin-bottom: 1em; border: 1px solid #ddd; }

  .legend-row { display: flex; align-items: center; gap: 0.6em; margin: 0.35em 0; font-size: 0.92em; }
  .legend-swatch { display: inline-block; width: 28px; height: 18px; border: 1px solid #999; border-radius: 3px; flex-shrink: 0; }
  .legend-count { font-family: 'Courier New', monospace; color: #555; font-size: 0.85em; min-width: 2.5em; }

  .tabs { display: flex; gap: 2px; margin-top: 1em; }
  .tab { padding: 0.6em 1em; background: #e0ddd5; border: 1px solid #bbb; border-bottom: none; border-radius: 4px 4px 0 0; cursor: pointer; font-size: 0.9em; }
  .tab.active { background: #fff; font-weight: bold; border-bottom: 2px solid #fff; position: relative; top: 1px; }
  .tab-content { display: none; background: #fff; border: 1px solid #bbb; padding: 1em; border-radius: 0 4px 4px 4px; }
  .tab-content.active { display: block; }

  .cond-desc { background: #f7f4ee; padding: 0.6em 1em; border-left: 3px solid #888; margin-bottom: 1em; font-size: 0.92em; }

  table.grid { border-collapse: collapse; width: 100%; table-layout: fixed; }
  table.grid th, table.grid td { border: 1px solid #ccc; padding: 0; vertical-align: top; }
  table.grid th { background: #ececec; font-weight: bold; padding: 0.4em; font-size: 0.85em; font-family: 'Courier New', monospace; }
  table.grid th.student-col { width: 200px; vertical-align: top; padding: 0.5em 0.4em; }
  table.grid th.student-col .student-name { display: block; font-family: Georgia, serif; font-weight: normal; font-size: 0.85em; color: #444; margin-top: 0.2em; }
  table.grid th.student-col .student-seed { display: block; font-family: Georgia, serif; font-weight: normal; font-size: 0.78em; color: #555; margin-top: 0.3em; line-height: 1.3; }

  td.cell { height: 200px; cursor: pointer; position: relative; }
  .cell-inner { height: 100%; padding: 0.4em; display: flex; flex-direction: column; gap: 4px; font-size: 0.78em; }
  .cell-inner:hover { outline: 2px solid #1a4a7e; outline-offset: -2px; }
  .cell-primary { font-family: Georgia, serif; font-weight: bold; font-size: 0.82em; color: #222; line-height: 1.25; }
  .cell-secondary { display: flex; flex-wrap: wrap; gap: 3px; }
  .chip { display: inline-block; padding: 0.1em 0.45em; border-radius: 10px; font-size: 0.68em; border: 1px solid rgba(0,0,0,0.15); font-family: Georgia, serif; }
  .cell-desc { flex: 1; overflow: hidden; font-family: Georgia, serif; font-size: 0.78em; line-height: 1.3; color: #333; padding: 0.2em 0.1em; background: rgba(255,255,255,0.55); border-radius: 2px; }
  .cell-quote-marker { display: flex; gap: 4px; font-size: 0.7em; font-family: 'Courier New', monospace; color: #555; }
  .marker { padding: 0.05em 0.35em; border-radius: 2px; font-weight: bold; }
  .marker.deficit { background: #f8d7da; color: #8b1f2a; }
  .marker.concern { background: #fff3cd; color: #7a5a00; }

  .modal-backdrop { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 50; align-items: center; justify-content: center; padding: 2em; }
  .modal-backdrop.show { display: flex; }
  .modal { background: #fff; border-radius: 6px; max-width: 1100px; width: 100%; max-height: 92vh; overflow-y: auto; padding: 1.2em 1.6em; }
  .modal-header { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid #ddd; padding-bottom: 0.6em; margin-bottom: 0.8em; }
  .modal-title { font-family: 'Courier New', monospace; font-size: 1em; }
  .modal-close { background: #888; color: #fff; border: none; padding: 0.4em 0.8em; border-radius: 3px; cursor: pointer; font-size: 0.85em; }
  .modal-section { margin: 0.8em 0; }
  .modal-section h3 { font-size: 0.95em; margin: 0 0 0.4em 0; color: #333; }
  .source-text { background: #fafafa; border: 1px solid #eee; padding: 0.8em 1em; border-radius: 3px; white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.92em; line-height: 1.5; }
  .coder-block { background: #f7f4ee; border-left: 3px solid #888; padding: 0.6em 0.9em; margin-bottom: 0.6em; border-radius: 3px; }
  .coder-block.opus { border-left-color: #1a4a7e; }
  .coder-block.gemini { border-left-color: #2d8a4a; }
  .coder-label { font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.85em; margin-bottom: 0.3em; }
  .quote-block { background: #fff; border-left: 3px solid #c2941f; padding: 0.3em 0.6em; margin: 0.3em 0; font-family: Georgia, serif; font-size: 0.88em; line-height: 1.4; }
  .quote-label { font-family: 'Courier New', monospace; font-size: 0.72em; color: #555; font-weight: bold; text-transform: uppercase; margin-right: 0.4em; }

  .pattern-list { columns: 2; column-gap: 1.4em; }
  .pattern-item { break-inside: avoid; margin-bottom: 0.7em; padding: 0.4em 0.6em; border-radius: 3px; }
  .pattern-item .pid { font-family: 'Courier New', monospace; font-size: 0.78em; color: #555; }
  .pattern-item .plabel { font-weight: bold; font-size: 0.92em; }
  .pattern-item .pwhat { font-size: 0.86em; line-height: 1.4; margin-top: 0.2em; }

  .nav-bar { margin: 0.8em 0; display: flex; gap: 0.5em; align-items: center; }
  .nav-bar button { padding: 0.3em 0.6em; font-size: 0.85em; cursor: pointer; }
  .progress { font-family: 'Courier New', monospace; font-size: 0.85em; color: #555; }
</style>
</head>
<body>

<h1>Variant A — AI Coding View</h1>
<div class="meta">Opus + Gemini 2.5 Pro emergent patterns, 2026-05-11. View-only. 96 cells.</div>

<div class="banner">
  <strong>What this view shows:</strong> the descriptive coding two AI coders (Opus and Gemini 2.5 Pro) produced after reading all 96 cells with open-coding instructions ("describe what the output is doing, do not categorize"). Cells are colored by their primary emergent pattern. Click any cell for full scaffolding: source text, both coders' descriptions, verbatim deficit/concern quotes.<br><br>
  <strong>What this view is NOT:</strong> the evaluative coding system the paper will use (false positive / false negative / correct / uncertain / hallucination). The coding workshop holds your evaluative pass. This view is scaffolding for your verification.
</div>

<details>
  <summary>Legend &mdash; emergent patterns + distribution across 96 cells</summary>
  <div id="legend"></div>
</details>

<details>
  <summary>Both coders' full pattern descriptions + meta-notes</summary>
  <div id="patterns-detail"></div>
</details>

<details>
  <summary>Inter-coder variance &mdash; agreement rates + coder meta-notes</summary>
  <div id="variance-detail">
    <p>See <code>variant_a_coding_variance_2026-05-11.md</code> for the per-cell divergence list (24 cells with notable divergence). Headline: 91.7% concern-flag agreement, 97.9% deficit-flag agreement, quote-overlap 0.56 (concern) / 0.25 (deficit) when both coders flagged the same cell.</p>
  </div>
</details>

<div class="tabs" id="tabs"></div>
<div id="tab-contents"></div>

<div class="modal-backdrop" id="modal-backdrop">
  <div class="modal" id="modal"></div>
</div>

<script>
const DATA = __DATA_BLOB__;

function patternById(id) { return DATA.patterns.find(p => p.id === id); }
function escapeHtml(s) {
  return (s == null ? '' : String(s))
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function renderLegend() {
  const el = document.getElementById('legend');
  let html = '';
  DATA.patterns.forEach(p => {
    const count = DATA.distribution[p.id] || 0;
    html += `<div class="legend-row">
      <span class="legend-swatch" style="background:${p.color}"></span>
      <span class="legend-count">${count}</span>
      <span><strong>${escapeHtml(p.label)}</strong> <span style="font-family:'Courier New',monospace;color:#888;font-size:0.85em;">${p.id}</span></span>
    </div>`;
  });
  el.innerHTML = html;
}

function renderPatternsDetail() {
  const el = document.getElementById('patterns-detail');
  let html = '<h3>Opus emergent patterns</h3><div class="pattern-list">';
  (DATA.opus_patterns || []).forEach(p => {
    html += `<div class="pattern-item" style="background:#eef3f8;border-left:3px solid #1a4a7e;">
      <div><span class="pid">${escapeHtml(p.pattern_id || '')}</span> <span class="plabel">${escapeHtml(p.candidate_label || '')}</span></div>
      <div class="pwhat">${escapeHtml(p.what_it_is || '')}</div>
      ${p.where_it_appears ? `<div class="pwhat"><em>Distribution:</em> ${escapeHtml(p.where_it_appears)}</div>` : ''}
    </div>`;
  });
  html += '</div>';
  html += '<h3 style="margin-top:1.2em;">Gemini emergent patterns</h3><div class="pattern-list">';
  (DATA.gemini_patterns || []).forEach(p => {
    html += `<div class="pattern-item" style="background:#eef8ee;border-left:3px solid #2d8a4a;">
      <div><span class="pid">${escapeHtml(p.pattern_id || '')}</span> <span class="plabel">${escapeHtml(p.candidate_label || '')}</span></div>
      <div class="pwhat">${escapeHtml(p.what_it_is || '')}</div>
      ${p.where_it_appears ? `<div class="pwhat"><em>Distribution:</em> ${escapeHtml(p.where_it_appears)}</div>` : ''}
    </div>`;
  });
  html += '</div>';
  html += `<div style="margin-top:1em;"><strong>Opus meta-notes:</strong><br>${escapeHtml(DATA.opus_meta).replace(/\n/g, '<br>')}</div>`;
  html += `<div style="margin-top:1em;"><strong>Gemini meta-notes:</strong><br>${escapeHtml(DATA.gemini_meta).replace(/\n/g, '<br>')}</div>`;
  el.innerHTML = html;
}

function buildCellInner(cid) {
  const c = DATA.cells[cid];
  const primary = patternById(c.primary_pattern) || DATA.patterns[DATA.patterns.length - 1];
  const desc = (c.opus && c.opus.description) ? c.opus.description : '';
  const trunc = desc.length > 200 ? desc.slice(0, 200) + '…' : desc;
  let chips = '';
  c.secondary_patterns.forEach(pid => {
    const p = patternById(pid);
    if (p) chips += `<span class="chip" style="background:${p.color}" title="${escapeHtml(p.label)}">${escapeHtml(p.label)}</span>`;
  });
  const hasConcern = c.opus && c.opus.concern_quote;
  const hasDeficit = c.opus && c.opus.deficit_quote;
  const markers = `${hasDeficit ? '<span class="marker deficit">D</span>' : ''}${hasConcern ? '<span class="marker concern">C</span>' : ''}`;
  return `
    <div class="cell-inner" style="background:${primary.color}">
      <div class="cell-primary">${escapeHtml(primary.label)}</div>
      ${chips ? `<div class="cell-secondary">${chips}</div>` : ''}
      <div class="cell-desc">${escapeHtml(trunc)}</div>
      ${markers ? `<div class="cell-quote-marker">${markers}<span style="color:#888;">click for quotes</span></div>` : ''}
    </div>
  `;
}

function buildCondTable(cond) {
  const wrap = document.createElement('div');
  const desc = document.createElement('div');
  desc.className = 'cond-desc';
  desc.textContent = DATA.cond_labels[cond];
  wrap.appendChild(desc);

  const table = document.createElement('table');
  table.className = 'grid';
  const thead = document.createElement('thead');
  let header = '<tr><th class="student-col">student</th>';
  DATA.models.forEach(m => { header += `<th>${m}</th>`; });
  header += '</tr>';
  thead.innerHTML = header;
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  DATA.students.forEach(sid => {
    const row = document.createElement('tr');
    const seed = (DATA.student_seeds && DATA.student_seeds[sid]) || '';
    row.innerHTML = `<th class="student-col">
      <span style="font-family:'Courier New',monospace;">${sid}</span>
      <span class="student-name">${escapeHtml(DATA.student_names[sid])}</span>
      <span class="student-seed">${escapeHtml(seed)}</span>
    </th>`;
    DATA.models.forEach(m => {
      const cid = `${sid}_${m}_${cond}`;
      const td = document.createElement('td');
      td.className = 'cell';
      td.id = 'tc-' + cid;
      td.innerHTML = buildCellInner(cid);
      td.onclick = () => openCellModal(cid);
      row.appendChild(td);
    });
    tbody.appendChild(row);
  });
  table.appendChild(tbody);
  wrap.appendChild(table);
  return wrap;
}

function renderTabs() {
  const tabsEl = document.getElementById('tabs');
  const contentsEl = document.getElementById('tab-contents');
  tabsEl.innerHTML = '';
  contentsEl.innerHTML = '';
  DATA.conds.forEach((cond, idx) => {
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
  });
}

function activateTab(cond) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.getElementById('tab-' + cond).classList.add('active');
  document.getElementById('tabc-' + cond).classList.add('active');
}

function openCellModal(cid) {
  const c = DATA.cells[cid];
  const primary = patternById(c.primary_pattern);
  const m = document.getElementById('modal');
  const secondaryHtml = (c.secondary_patterns || []).map(pid => {
    const p = patternById(pid);
    return p ? `<span class="chip" style="background:${p.color}">${escapeHtml(p.label)}</span>` : '';
  }).join(' ');

  function coderBlock(label, coder, klass) {
    return `<div class="coder-block ${klass}">
      <div class="coder-label">${label}</div>
      <div><em>Description:</em> ${escapeHtml(coder.description || '—')}</div>
      ${coder.concern_quote ? `<div class="quote-block"><span class="quote-label">concern flagged:</span>${escapeHtml(coder.concern_quote)}</div>` : ''}
      ${coder.concern_note ? `<div style="font-size:0.85em;color:#555;margin-top:0.2em;">${escapeHtml(coder.concern_note)}</div>` : ''}
      ${coder.deficit_quote ? `<div class="quote-block" style="border-left-color:#d9534f;"><span class="quote-label">deficit language:</span>${escapeHtml(coder.deficit_quote)}</div>` : ''}
      ${coder.deficit_note ? `<div style="font-size:0.85em;color:#555;margin-top:0.2em;">${escapeHtml(coder.deficit_note)}</div>` : ''}
      ${coder.other ? `<div style="font-size:0.85em;color:#555;margin-top:0.3em;"><em>Other notable:</em> ${escapeHtml(coder.other)}</div>` : ''}
    </div>`;
  }

  m.innerHTML = `
    <div class="modal-header">
      <div class="modal-title">${c.sid} &middot; ${c.model} &middot; ${c.condition} &middot; <span style="font-family:Georgia,serif;font-weight:normal;">${escapeHtml(c.student_name)}</span></div>
      <button class="modal-close" onclick="closeCellModal()">close</button>
    </div>
    <div class="nav-bar">
      <button onclick="navCell(-1)">← prev</button>
      <button onclick="navCell(1)">next →</button>
      <span style="margin-left:0.6em;">Primary pattern: <span class="chip" style="background:${primary.color}">${escapeHtml(primary.label)}</span> ${secondaryHtml ? `&middot; also: ${secondaryHtml}` : ''}</span>
    </div>
    <div class="modal-section">
      <h3>Source model output</h3>
      <div class="source-text">${escapeHtml(c.text)}</div>
    </div>
    <div class="modal-section">
      <h3>Opus &amp; Gemini coders</h3>
      ${coderBlock('OPUS', c.opus || {}, 'opus')}
      ${coderBlock('GEMINI 2.5 PRO', c.gemini || {}, 'gemini')}
    </div>
  `;
  document.getElementById('modal-backdrop').classList.add('show');
  CURRENT_CID = cid;
}

let CURRENT_CID = null;
function closeCellModal() {
  document.getElementById('modal-backdrop').classList.remove('show');
  CURRENT_CID = null;
}
function navCell(delta) {
  if (!CURRENT_CID) return;
  const ids = Object.keys(DATA.cells);
  const idx = ids.indexOf(CURRENT_CID);
  const newIdx = (idx + delta + ids.length) % ids.length;
  openCellModal(ids[newIdx]);
}

// modal close on backdrop click or Esc
document.getElementById('modal-backdrop').addEventListener('click', (e) => {
  if (e.target.id === 'modal-backdrop') closeCellModal();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeCellModal();
  if (CURRENT_CID && e.key === 'ArrowRight') navCell(1);
  if (CURRENT_CID && e.key === 'ArrowLeft') navCell(-1);
});

renderLegend();
renderPatternsDetail();
renderTabs();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
