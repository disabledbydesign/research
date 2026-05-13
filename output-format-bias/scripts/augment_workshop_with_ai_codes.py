#!/usr/bin/env python3
"""
Non-destructive augmentation of the Variant A coding workshop with TWO AI layers:

  1. Open-coding scaffolding (ai_codes)
       Opus + Gemini per-cell descriptions, verbatim deficit/concern quotes,
       other-notable observations. From the 2026-05-11 open-coding pass.

  2. Evaluative scaffolding (eval_codes)
       Opus + Gemini per-cell TP/FP/hallucination/unclear booleans with
       verbatim model_output quotes per category, summary_verdict, reasoning.
       From the 2026-05-11 evaluative pass (with student submissions as ground truth).

The augmented workshop renders:

  Cell (in the table grid):
    - Existing category dropdown + flag badge + preview + notes textarea (UNCHANGED)
    - New: compact eval indicator showing OP/GM per-flag booleans (T/F/H/U) +
      divergence marker if coders disagree on any flag

  Popover (on hover):
    - Existing meta + Set-excerpt + model output text + verification flags (UNCHANGED)
    - New: prominent eval verdict bar at top (both coders side by side)
    - New: two-column eval evidence section (verbatim TP/FP/H/U examples per coder)
    - New: collapsible open-coding details (description + deficit/concern quotes)

  Storage key 'vaw_state' unchanged: existing coding state, notes, categories,
  and toggles persist across original / augmented files.

Reads:
  - data_tables/variant_a_coding_workshop_2026-05-11.html  (ORIGINAL, untouched)
  - variant_a_ai_coding_2026-05-11/variant_a_coding_pass_opus_2026-05-11.json
  - variant_a_ai_coding_2026-05-11/variant_a_coding_pass_gemini_2026-05-11.json
  - variant_a_ai_coding_2026-05-11/variant_a_evaluative_pass_opus_2026-05-11.json
  - variant_a_ai_coding_2026-05-11/variant_a_evaluative_pass_gemini_2026-05-11.json

Writes:
  - data_tables/variant_a_coding_workshop_with_ai_codes_2026-05-11.html
"""
import json
import re
from pathlib import Path

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
DT = ROOT / "data_tables"
AI_DIR = DT / "variant_a_ai_coding_2026-05-11"
ORIG = DT / "variant_a_coding_workshop_2026-05-11.html"
OPEN_OPUS = AI_DIR / "variant_a_coding_pass_opus_2026-05-11.json"
OPEN_GEMINI = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"
EVAL_OPUS = AI_DIR / "variant_a_evaluative_pass_opus_2026-05-11.json"
EVAL_GEMINI = AI_DIR / "variant_a_evaluative_pass_gemini_2026-05-11.json"
OUT = DT / "variant_a_coding_workshop_with_ai_codes_2026-05-11.html"


# ============================================================================
# CSS — added before </style>
# ============================================================================

CSS_ADDITION = """
  /* ============ AI scaffolding (open coding + eval) — non-destructive ============ */

  /* Cell-level eval indicator (compact two-row chip strip below preview) */
  .cell-eval {
    flex-shrink: 0;
    display: flex; flex-direction: column; gap: 0;
    padding: 0;
    border: 1px solid #888;
    border-left-width: 5px;
    border-radius: 2px;
    font-size: 0.7em; font-family: 'Courier New', monospace;
    cursor: help;
    line-height: 1.25;
    overflow: hidden;
  }
  .cell-eval.agree   { border-left-color: #2d8a4a; }
  .cell-eval.diverge { border-left-color: #b22222; }

  .cell-eval-row {
    display: flex; gap: 4px; align-items: center;
    padding: 0.2em 0.4em;
  }
  /* Verdict-colored backgrounds — applied per row by the JS */
  .cell-eval-row.v-mostly-correct      { background: #d4edda; }
  .cell-eval-row.v-mixed               { background: #fff3cd; }
  .cell-eval-row.v-mostly-problematic  { background: #f8d7da; }
  .cell-eval-row.v-needs-human-review  { background: #e5d4ed; }
  .cell-eval-row.v-unknown             { background: #efefef; }

  .cell-eval-coder { font-weight: bold; min-width: 1.7em; color: #333; }
  .cell-eval-flag {
    display: inline-flex; align-items: baseline; gap: 1px;
    padding: 0 0.2em;
    font-size: 0.95em;
  }
  .cell-eval-flag .lab { font-weight: bold; }
  .cell-eval-flag .dot { font-size: 1.1em; line-height: 0.8; }
  .cell-eval-flag .dot.on { color: #222; }
  .cell-eval-flag .dot.off { color: rgba(0,0,0,0.18); }
  .cell-eval-flag.tp .lab { color: #155724; }
  .cell-eval-flag.fp .lab { color: #8b1f2a; }
  .cell-eval-flag.h  .lab { color: #4a1f6a; }
  .cell-eval-flag.u  .lab { color: #7a5a00; }
  .cell-eval-diverge {
    margin-left: auto; font-size: 1em; font-weight: bold;
    color: #b22222;
  }
  .cell-eval-agree { margin-left: auto; font-size: 1em; color: #2d8a4a; font-weight: bold; }

  /* Popover eval verdict bar */
  .popover-verdict-bar {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 0.5em;
    margin: 0.5em 0;
    padding: 0.5em 0.6em;
    background: #f7f4ee;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  .popover-verdict-bar.diverge { border-color: #c2941f; background: #fff8dc; }
  .verdict-col { font-size: 0.85em; }
  .verdict-coder {
    font-family: 'Courier New', monospace; font-weight: bold;
    font-size: 0.85em; margin-bottom: 0.25em;
  }
  .verdict-coder.op { color: #1a4a7e; }
  .verdict-coder.gm { color: #2d8a4a; }
  .verdict-summary {
    display: inline-block; padding: 0.1em 0.5em; border-radius: 3px;
    font-weight: bold; font-size: 0.92em; margin-right: 0.4em;
  }
  .verdict-summary.mostly-correct      { background: #d4edda; color: #155724; }
  .verdict-summary.mixed               { background: #fff3cd; color: #7a5a00; }
  .verdict-summary.mostly-problematic  { background: #f8d7da; color: #8b1f2a; }
  .verdict-summary.needs-human-review  { background: #e5d4ed; color: #4a1f6a; }
  .verdict-flags { margin-top: 0.3em; }
  .verdict-flags .vf {
    display: inline-block; margin-right: 0.5em;
    font-family: 'Courier New', monospace; font-size: 0.85em;
  }
  .verdict-flags .vf.on  { color: #b22222; font-weight: bold; }
  .verdict-flags .vf.off { color: #888; }
  .verdict-agreement {
    grid-column: 1 / -1; padding-top: 0.4em; border-top: 1px dotted #bbb;
    font-size: 0.82em; color: #555;
  }
  .verdict-agreement.diverge { color: #8b1f2a; font-weight: bold; }

  /* Popover two-column eval evidence section */
  .popover-eval-section {
    margin-top: 0.8em; padding-top: 0.6em; border-top: 1px dashed #ccc;
  }
  .popover-eval-section h4 {
    font-size: 0.85em; margin: 0 0 0.4em 0; color: #555;
    font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 0.05em;
  }
  .eval-twocol {
    display: grid; grid-template-columns: 1fr 1fr; gap: 0.6em;
  }
  .eval-col {
    background: #f7f4ee;
    border-left: 3px solid #1a4a7e;
    padding: 0.5em 0.65em;
    font-size: 0.83em; line-height: 1.4;
    border-radius: 3px;
  }
  .eval-col.gemini { border-left-color: #2d8a4a; }
  .eval-coder-name {
    font-family: 'Courier New', monospace; font-weight: bold;
    font-size: 0.78em; color: #555; margin-bottom: 0.3em;
  }
  .eval-cat {
    margin: 0.4em 0 0.2em 0;
    font-family: 'Courier New', monospace; font-size: 0.78em;
    font-weight: bold; text-transform: uppercase; letter-spacing: 0.04em;
  }
  .eval-cat.tp { color: #2d8a4a; }
  .eval-cat.fp { color: #b22222; }
  .eval-cat.h  { color: #6a1b9a; }
  .eval-cat.u  { color: #8a6d0c; }
  .eval-cat.absent { color: #888; font-weight: normal; }
  .eval-example {
    background: #fff; border-left: 2px solid #c2941f;
    padding: 0.2em 0.5em; margin: 0.15em 0;
    font-style: italic; font-size: 0.95em;
  }
  .eval-example.fp { border-left-color: #b22222; }
  .eval-example.h  { border-left-color: #6a1b9a; }
  .eval-example.u  { border-left-color: #8a6d0c; }
  .eval-reasoning {
    margin-top: 0.5em; padding-top: 0.4em; border-top: 1px dotted #ccc;
    font-size: 0.92em; color: #333;
  }
  .eval-reasoning-label {
    font-family: 'Courier New', monospace; font-size: 0.78em;
    font-weight: bold; color: #555; text-transform: uppercase;
    margin-right: 0.4em;
  }

  /* Open-coding details (collapsible, secondary) */
  .popover-opencodes {
    margin-top: 0.6em; padding-top: 0.5em; border-top: 1px dotted #ccc;
  }
  .popover-opencodes details { background: #fafaf7; border: 1px solid #ddd; }
  .popover-opencodes summary {
    font-size: 0.82em; color: #555; font-family: 'Courier New', monospace;
    text-transform: uppercase; letter-spacing: 0.04em; padding: 0.3em 0.5em;
  }
  .opencode-block {
    background: #f7f4ee; border-left: 3px solid #1a4a7e;
    padding: 0.4em 0.6em; margin: 0.3em 0;
    font-size: 0.85em; line-height: 1.4;
  }
  .opencode-block.gemini { border-left-color: #2d8a4a; }
  .opencode-coder-name {
    font-family: 'Courier New', monospace; font-weight: bold;
    font-size: 0.78em; color: #555;
  }
  .opencode-quote {
    background: #fff; border-left: 2px solid #c2941f;
    padding: 0.2em 0.5em; margin: 0.2em 0;
    font-style: italic; font-size: 0.92em;
  }
  .opencode-quote.deficit { border-left-color: #d9534f; }
  .opencode-quote-label {
    font-family: 'Courier New', monospace; font-size: 0.7em;
    color: #555; font-weight: bold; text-transform: uppercase; margin-right: 0.4em;
  }

  /* Wider popover to fit the two-column eval layout */
  .hover-popover { width: 880px !important; }
"""


# ============================================================================
# JS — building blocks
# ============================================================================

# Helper: renders the eval indicator strip for inside a cell.
CELL_EVAL_JS = """
  // ---- cell-level eval indicator (compact, two rows: OP + GM, 4 flags each) ----
  if (cell.eval_codes) {
    const ec = cell.eval_codes;
    const op = ec.opus || {};
    const gm = ec.gemini || {};
    const flags = [
      {k: 'tp', label: 'T', opOn: !!op.tp_present, gmOn: !!gm.tp_present},
      {k: 'fp', label: 'F', opOn: !!op.fp_present, gmOn: !!gm.fp_present},
      {k: 'h',  label: 'H', opOn: !!op.hallucination_present, gmOn: !!gm.hallucination_present},
      {k: 'u',  label: 'U', opOn: !!op.unclear_present, gmOn: !!gm.unclear_present},
    ];
    const anyDiverge = flags.some(f => f.opOn !== f.gmOn) || (op.summary_verdict !== gm.summary_verdict);
    const evalDiv = document.createElement('div');
    evalDiv.className = 'cell-eval ' + (anyDiverge ? 'diverge' : 'agree');
    function rowHtml(coderClass, coderLabel, verdict, getOn) {
      const v = (verdict || 'unknown').toLowerCase();
      let s = '<div class="cell-eval-row v-' + v + '" title="' + coderLabel + ': ' + (verdict || 'unknown') + '"><span class="cell-eval-coder">' + coderLabel + '</span>';
      flags.forEach(f => {
        const on = getOn(f);
        s += '<span class="cell-eval-flag ' + f.k + '"><span class="lab">' + f.label + '</span><span class="dot ' + (on ? 'on' : 'off') + '">' + (on ? '●' : '○') + '</span></span>';
      });
      return s + '</div>';
    }
    evalDiv.innerHTML =
      rowHtml('op', 'OP', op.summary_verdict, f => f.opOn) +
      rowHtml('gm', 'GM', gm.summary_verdict, f => f.gmOn);
    // append divergence marker absolutely positioned in the first row, after the flags
    const rows = evalDiv.querySelectorAll('.cell-eval-row');
    const marker = document.createElement('span');
    marker.className = anyDiverge ? 'cell-eval-diverge' : 'cell-eval-agree';
    marker.textContent = anyDiverge ? '⚠' : '✓';
    marker.title = anyDiverge
      ? 'Opus and Gemini diverge on at least one flag or on summary verdict'
      : 'Opus and Gemini agree on all four flags';
    if (rows[0]) rows[0].appendChild(marker);
    // tooltip: short summary of both verdicts
    evalDiv.title =
      'OPUS: ' + (op.summary_verdict || '?') + ' | ' + flags.map(f => f.label + '=' + (f.opOn ? 'yes' : 'no')).join(' ') +
      '\\nGEMINI: ' + (gm.summary_verdict || '?') + ' | ' + flags.map(f => f.label + '=' + (f.gmOn ? 'yes' : 'no')).join(' ') +
      '\\n\\nHover the cell preview for full quotes and reasoning.';
    evalDiv.onclick = (e) => e.stopPropagation();
    inner.appendChild(evalDiv);
  }

"""

# Inserted after popover-body and before flags. Renders the eval verdict bar at top,
# two-column eval evidence in the middle, and a collapsible open-coding details block.
POPOVER_AI_SECTION_JS = """
  // ---- AI scaffolding panels (eval verdict bar, two-col eval evidence, open-coding details) ----
  if (cell.eval_codes || cell.ai_codes) {
    const wrap = document.createElement('div');
    wrap.innerHTML = renderAiScaffolding(cell);
    while (wrap.firstChild) pop.appendChild(wrap.firstChild);
  }

"""

# Standalone helper functions defined before showPopover.
AI_HELPER_FN_JS = r"""
function _agreementOnAllFlags(opEval, gmEval) {
  if (!opEval || !gmEval) return null;
  const keys = ['tp_present', 'fp_present', 'hallucination_present', 'unclear_present'];
  const flagDiverge = keys.filter(k => !!opEval[k] !== !!gmEval[k]);
  const verdictDiverge = (opEval.summary_verdict !== gmEval.summary_verdict);
  return {
    flagDiverge,
    verdictDiverge,
    anyDiverge: flagDiverge.length > 0 || verdictDiverge,
  };
}

function _verdictBarHtml(opEval, gmEval) {
  if (!opEval && !gmEval) return '';
  function colHtml(coderClass, coderLabel, ec) {
    if (!ec) return '<div class="verdict-col"><div class="verdict-coder ' + coderClass + '">' + coderLabel + '</div><div>(no evaluation)</div></div>';
    const v = ec.summary_verdict || 'unknown';
    const flags = [
      {k: 'tp_present', label: 'TP'},
      {k: 'fp_present', label: 'FP'},
      {k: 'hallucination_present', label: 'HALL'},
      {k: 'unclear_present', label: 'UNCLEAR'},
    ];
    let flagsHtml = '<div class="verdict-flags">';
    flags.forEach(f => {
      const on = !!ec[f.k];
      flagsHtml += '<span class="vf ' + (on ? 'on' : 'off') + '">' + f.label + ': ' + (on ? 'yes' : 'no') + '</span>';
    });
    flagsHtml += '</div>';
    return '<div class="verdict-col">' +
      '<div class="verdict-coder ' + coderClass + '">' + coderLabel + '</div>' +
      '<span class="verdict-summary ' + v + '">' + v + '</span>' +
      flagsHtml +
      '</div>';
  }
  const agreement = _agreementOnAllFlags(opEval, gmEval);
  let agreementHtml = '';
  if (agreement) {
    if (agreement.anyDiverge) {
      const parts = [];
      if (agreement.verdictDiverge) parts.push('summary verdicts differ');
      if (agreement.flagDiverge.length) parts.push('flag divergence on ' + agreement.flagDiverge.map(s => s.replace('_present', '').toUpperCase()).join(', '));
      agreementHtml = '<div class="verdict-agreement diverge">⚠ ' + parts.join('; ') + '</div>';
    } else {
      agreementHtml = '<div class="verdict-agreement">✓ Opus and Gemini agree on all four flags and summary verdict.</div>';
    }
  }
  const klass = (agreement && agreement.anyDiverge) ? 'popover-verdict-bar diverge' : 'popover-verdict-bar';
  return '<div class="' + klass + '">' +
    colHtml('op', 'OPUS', opEval) +
    colHtml('gm', 'GEMINI 2.5 PRO', gmEval) +
    agreementHtml +
    '</div>';
}

function _evalEvidenceHtml(opEval, gmEval) {
  if (!opEval && !gmEval) return '';
  function colHtml(coderClass, coderLabel, ec) {
    if (!ec) return '';
    function catBlock(catKey, exKey, label, klass) {
      const present = !!ec[catKey];
      const examples = ec[exKey] || [];
      if (!present || examples.length === 0) {
        return '<div class="eval-cat absent">' + label + ': none</div>';
      }
      let s = '<div class="eval-cat ' + klass + '">' + label + ' (' + examples.length + ')</div>';
      examples.forEach(q => {
        s += '<div class="eval-example ' + klass + '">' + escapeHtml(q) + '</div>';
      });
      return s;
    }
    let body = '';
    body += catBlock('tp_present', 'tp_examples', 'TP', 'tp');
    body += catBlock('fp_present', 'fp_examples', 'FP', 'fp');
    body += catBlock('hallucination_present', 'hallucination_examples', 'HALLUCINATION', 'h');
    body += catBlock('unclear_present', 'unclear_examples', 'UNCLEAR', 'u');
    if (ec.reasoning) {
      body += '<div class="eval-reasoning"><span class="eval-reasoning-label">reasoning:</span>' + escapeHtml(ec.reasoning) + '</div>';
    }
    return '<div class="eval-col ' + (coderClass === 'gm' ? 'gemini' : '') + '">' +
      '<div class="eval-coder-name">' + coderLabel + '</div>' +
      body +
      '</div>';
  }
  return '<div class="popover-eval-section">' +
    '<h4>Evaluative coding — TP / FP / hallucination / unclear (with student submission as ground truth)</h4>' +
    '<div class="eval-twocol">' +
    colHtml('op', 'OPUS', opEval) +
    colHtml('gm', 'GEMINI 2.5 PRO', gmEval) +
    '</div></div>';
}

function _openCodingHtml(opAi, gmAi) {
  if (!opAi && !gmAi) return '';
  function block(coderClass, coderLabel, c) {
    if (!c) return '';
    const desc = c.description ? '<div>' + escapeHtml(c.description) + '</div>' : '';
    const cQuote = c.concern_quote
      ? '<div class="opencode-quote"><span class="opencode-quote-label">concern:</span>' + escapeHtml(c.concern_quote) + '</div>'
        + (c.concern_note ? '<div style="font-size:0.82em;color:#555;margin-top:0.15em;">' + escapeHtml(c.concern_note) + '</div>' : '')
      : '';
    const dQuote = c.deficit_quote
      ? '<div class="opencode-quote deficit"><span class="opencode-quote-label">deficit:</span>' + escapeHtml(c.deficit_quote) + '</div>'
        + (c.deficit_note ? '<div style="font-size:0.82em;color:#555;margin-top:0.15em;">' + escapeHtml(c.deficit_note) + '</div>' : '')
      : '';
    const other = c.other ? '<div style="font-size:0.82em;color:#555;margin-top:0.3em;"><em>other:</em> ' + escapeHtml(c.other) + '</div>' : '';
    return '<div class="opencode-block ' + (coderClass === 'gm' ? 'gemini' : '') + '">' +
      '<div class="opencode-coder-name">' + coderLabel + '</div>' +
      desc + cQuote + dQuote + other +
      '</div>';
  }
  return '<div class="popover-opencodes">' +
    '<details>' +
    '<summary>▸ Open-coding details (pass 1: descriptive)</summary>' +
    block('op', 'OPUS', opAi) +
    block('gm', 'GEMINI 2.5 PRO', gmAi) +
    '</details></div>';
}

function renderAiScaffolding(cell) {
  const eval_ = cell.eval_codes || {};
  const ai = cell.ai_codes || {};
  return _verdictBarHtml(eval_.opus, eval_.gemini) +
         _evalEvidenceHtml(eval_.opus, eval_.gemini) +
         _openCodingHtml(ai.opus, ai.gemini);
}

"""


# ============================================================================
# Data assembly
# ============================================================================

def build_ai_codes(opus_cell: dict, gemini_cell: dict) -> dict:
    def pack(c: dict) -> dict:
        if not c:
            return {}
        return {
            "description": c.get("description") or "",
            "concern_quote": (c.get("concern_flagged") or {}).get("quote"),
            "concern_note": (c.get("concern_flagged") or {}).get("note"),
            "deficit_quote": (c.get("deficit_language") or {}).get("quote"),
            "deficit_note": (c.get("deficit_language") or {}).get("note"),
            "other": c.get("other_notable"),
        }
    return {"opus": pack(opus_cell), "gemini": pack(gemini_cell)}


def build_eval_codes(opus_eval: dict, gemini_eval: dict) -> dict:
    def pack(c: dict) -> dict:
        if not c:
            return {}
        return {
            "tp_present": bool(c.get("tp_present")),
            "tp_examples": c.get("tp_examples") or [],
            "fp_present": bool(c.get("fp_present")),
            "fp_examples": c.get("fp_examples") or [],
            "hallucination_present": bool(c.get("hallucination_present")),
            "hallucination_examples": c.get("hallucination_examples") or [],
            "unclear_present": bool(c.get("unclear_present")),
            "unclear_examples": c.get("unclear_examples") or [],
            "summary_verdict": c.get("summary_verdict") or "unknown",
            "reasoning": c.get("reasoning") or "",
        }
    return {"opus": pack(opus_eval), "gemini": pack(gemini_eval)}


def main():
    html_content = ORIG.read_text()
    open_opus = json.loads(OPEN_OPUS.read_text())
    open_gemini = json.loads(OPEN_GEMINI.read_text())
    eval_opus = json.loads(EVAL_OPUS.read_text())
    eval_gemini = json.loads(EVAL_GEMINI.read_text())

    open_opus_by_cell = {c["cell_id"]: c for c in open_opus["per_cell"]}
    open_gemini_by_cell = {c["cell_id"]: c for c in open_gemini["per_cell"]}
    eval_opus_by_cell = {c["cell_id"]: c for c in eval_opus["per_cell"]}
    eval_gemini_by_cell = {c["cell_id"]: c for c in eval_gemini["per_cell"]}

    # ---- 1. extract and augment DATA ----
    data_re = re.compile(r"(const DATA = )(\{.*?\});", re.DOTALL)
    m = data_re.search(html_content)
    if not m:
        raise SystemExit("Could not find DATA constant in workshop HTML")

    data = json.loads(m.group(2))
    cells = data["cells"]
    for cid, cell in cells.items():
        cell["ai_codes"] = build_ai_codes(
            open_opus_by_cell.get(cid, {}),
            open_gemini_by_cell.get(cid, {}),
        )
        cell["eval_codes"] = build_eval_codes(
            eval_opus_by_cell.get(cid, {}),
            eval_gemini_by_cell.get(cid, {}),
        )

    new_data_str = "const DATA = " + json.dumps(data, ensure_ascii=False) + ";"
    html_content = html_content[: m.start()] + new_data_str + html_content[m.end():]

    # ---- 2. inject CSS just before </style> ----
    if "</style>" not in html_content:
        raise SystemExit("Could not find </style> tag")
    html_content = html_content.replace("</style>", CSS_ADDITION + "\n</style>", 1)

    # ---- 3. inject cell eval line into buildCellInner (between preview append and notes setup) ----
    preview_anchor = "  attachHoverHandlers(preview, cid);\n  inner.appendChild(preview);"
    if preview_anchor not in html_content:
        raise SystemExit("Could not find buildCellInner preview anchor for cell-eval injection")
    html_content = html_content.replace(
        preview_anchor,
        preview_anchor + "\n" + CELL_EVAL_JS,
        1,
    )

    # ---- 4. inject AI scaffolding panels into showPopover after popover body is in DOM ----
    popover_anchor = "  document.body.appendChild(pop);\n  HOVER_POPOVER = pop;"
    if popover_anchor not in html_content:
        raise SystemExit("Could not find showPopover anchor for AI section injection")
    html_content = html_content.replace(
        popover_anchor,
        popover_anchor + "\n" + POPOVER_AI_SECTION_JS,
        1,
    )

    # ---- 5. inject helper functions before showPopover ----
    helper_anchor = "function showPopover(cid, anchorEl) {"
    if helper_anchor not in html_content:
        raise SystemExit("Could not find showPopover function for helper injection")
    html_content = html_content.replace(
        helper_anchor,
        AI_HELPER_FN_JS + "\n" + helper_anchor,
        1,
    )

    # ---- 6. update <title> ----
    html_content = html_content.replace(
        "<title>Variant A Coding Workshop — 2026-05-11</title>",
        "<title>Variant A Coding Workshop (with AI eval scaffolding) — 2026-05-11</title>",
        1,
    )

    OUT.write_text(html_content)
    print(f"Wrote {OUT}")
    print(f"  Original ({ORIG.stat().st_size:,} bytes) untouched.")
    print(f"  Augmented ({OUT.stat().st_size:,} bytes).")
    print(f"\nWhat's in the augmented workshop:")
    print(f"  - Each cell shows a compact two-row eval indicator (OP + GM, 4 flags each, divergence marker)")
    print(f"  - Hovering opens a popover with: prominent verdict bar (Opus | Gemini side-by-side),")
    print(f"    two-column TP/FP/hallucination/unclear evidence with verbatim quotes, and")
    print(f"    a collapsible open-coding details block (pass 1 descriptive codes)")
    print(f"  - Your category dropdown, notes textarea, flag badges, localStorage state: all unchanged")
    print(f"  - Storage key 'vaw_state' shared with original, so coding state persists")


if __name__ == "__main__":
    main()
