#!/usr/bin/env python3
"""Build a hand-coding workshop HTML for the Variant A stripped-observation run.

Reads the four condition JSON files written by run_variant_a_stripped_observation.py
and produces a single self-contained HTML page for manual qualitative coding by hand.

Output: variant_a_coding_workshop_2026-05-11.html in the output-format-bias root.
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
    "b_replicate": ('b_replicate', 'full prompt: equity floor + power-moves taxonomy + rel/narrative paragraph + class context'),
    "a1":          ('a1', 'power-moves taxonomy STRIPPED (kept: equity floor + rel/narrative + class context)'),
    "a2":          ('a2', 'taxonomy + rel/narrative paragraph BOTH STRIPPED (kept: equity floor + class context)'),
    "a2_no_context": ('a2_no_context', 'ALSO class context stripped (equity floor only in system prompt)'),
}
MODELS = ["gemma12b", "qwen7b", "llama8b"]

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

# Flags keyed by (student_id, model, condition) -> list of {type, text}
FLAGS = {
    ("S004", "llama8b", "b_replicate"): [
        {"type": "TAXONOMY FALSE-POSITIVE",
         "text": "Reads Priya's framework-questioning as \"a subtle attempt to deflect from the main point.\" Critical-theoretical sophistication misread as foreclosure. This is the verification-swarm-flagged deficit pattern. CLEARED in a1 / a2 / a2_no_context."},
    ],
    ("S024", "llama8b", "b_replicate"): [
        {"type": "TAXONOMY FALSE-POSITIVE",
         "text": "Claims Ingrid \"frames her mother's situation as a universal example of intersectionality, without explicitly acknowledging the structural power dynamics at play.\" Ingrid is explicitly engaging structural power dynamics throughout. CLEARED in a1 / a2 / a2_no_context."},
    ],
    ("S031", "qwen7b", "b_replicate"): [
        {"type": "HALLUCINATION",
         "text": "\"his submission does reveal a temporary dip in depth and nuance compared to his previous work, which showed a more critical engagement\" — there is no previous work in the prompt. Trajectory data fabricated. Disappears in a1+."},
    ],
    ("S022", "qwen7b", "b_replicate"): [
        {"type": "TAXONOMY MISUSE",
         "text": "Qwen calls Destiny's analytic move \"a structural power move\" — uses taxonomy term as positive descriptor (the term is meant to denote student foreclosures to flag, not student insight)."},
    ],
    ("S023", "qwen7b", "b_replicate"): [
        {"type": "TAXONOMY MISUSE",
         "text": "Same as S022 — Yolanda's analysis labeled \"a structural power move\" in positive direction. Taxonomy term semantically inverted by Qwen."},
    ],
    ("S029", "qwen7b", "b_replicate"): [
        {"type": "PRONOUN INFERENCE",
         "text": "Qwen uses \"she/her\" for Jordan Espinoza here. Flips to \"he/his\" in a1, a2, a2_no_context. Same student, deterministic temp 0.3 — prompt-content spillover into unrelated representation choices."},
    ],
    ("S029", "qwen7b", "a1"): [
        {"type": "PRONOUN FLIP",
         "text": "Now \"he/his\" — flipped from \"she/her\" in b_replicate."},
    ],
    ("S024", "gemma12b", "a1"): [
        {"type": "POSSIBLE CONTEXT-LEAK",
         "text": "References \"Maria Ndiaye and DeShawn Mercer\" as peer students. Verify against class_reading_source — these may be in the class context, or may be fabricated peer-comparisons. Does NOT recur in a2_no_context (suggests source was class context)."},
    ],
    ("S024", "llama8b", "a2"): [
        {"type": "POSSIBLE CONTEXT-LEAK",
         "text": "Contrasts Ingrid with \"Alex Hernandez's more formal definition\" — Alex Hernandez may be from class_reading_source or fabricated. Does NOT recur in a2_no_context."},
    ],
    ("S023", "llama8b", "a2_no_context"): [
        {"type": "CONTENT FABRICATION (?)",
         "text": "Describes Yolanda's abuela as \"undocumented immigrant woman\" and \"undocumented worker.\" Verify against Yolanda's actual submission text — if she does not characterize her abuela's immigration status, this is content fabrication. Also note: paternalistic-background inference (next flag)."},
        {"type": "PATERNALISTIC BACKGROUND INFERENCE",
         "text": "\"Yolanda's submission suggests that she may be from a low-income background or have a family history of immigration and labor struggles, which could be relevant for the teacher to be aware of in terms of providing support and resources for her academic journey.\" New failure mode emerging without class context — Llama infers student background as concern-flag."},
    ],
    ("S028", "llama8b", "a2_no_context"): [
        {"type": "PATERNALISTIC BACKGROUND INFERENCE",
         "text": "\"Imani's submission suggests they may have had to navigate complex social dynamics and expectations in their daily life, particularly as a Black girl. This could be a circumstance that the teacher might want to be aware of.\" Same new failure mode."},
    ],
    ("S028", "qwen7b", "b_replicate"): [
        {"type": "PRONOUN SLIP",
         "text": "Refers to \"Iman\" once (truncated form of Imani) before reverting. Minor."},
    ],
}

CROSS_CONDITION_NOTES = {
    "S002": "**Burnout signal trajectory across conditions for Jordan Kim:** No model in any condition reads burnout. Llama 8B's affect attention oscillates: b_replicate \"sense of struggle, overwhelmed\" → a1 \"introspection\" → a2 \"frustration or overwhelm\" → a2_no_context \"passionate\" (most asset-flattened). Gemma and Qwen miss entirely in all four. Worth correlating against whether the preserved-binary classifier catches S002 — memory note says no.",
    "S004": "**Priya false-positive resolution:** Llama's b_replicate \"deflection\" reading is CLEARED in all three stripped conditions. Direct corroboration that the structural-power-moves taxonomy was the source of the deficit-frame.",
    "S022": "**Anger handling robust across all four conditions for all three models.** Equity floor on anger (which stays in the system prompt across all conditions) appears load-bearing. Test R designation \"righteous anger\" reads correctly across the matrix.",
    "S023": "**Yolanda asset framing stable across conditions, but Llama in a2_no_context fabricates \"undocumented\" status.** Without class context, Llama starts inferring background details that may not be in Yolanda's submission text. Flag.",
    "S024": "**Ingrid false-positive resolution (Llama b_replicate):** CLEARED in all three stripped conditions. Same mechanism as S004.",
    "S028": "**Imani asset framing stable, but Llama in a2_no_context shifts to paternalistic background-inference.** New failure mode emerging without class context.",
    "S029": "**Espinoza asset framing stable. Qwen pronoun flips at the a1 boundary.** Same student, deterministic temp 0.3 — prompt spillover into gender inference.",
    "S031": "**Marcus minimal-effort: most uneven case.** Llama only names \"not yet invested\" in a2 and a2_no_context. Gemma never names minimal-effort directly but a2 comes closest (\"needs more scaffolding or a different kind of prompt\"). Qwen b_replicate hallucinates a \"previous-work dip\"; in a1+ shifts to peer-comparison. The strips help in this cell — closer to honest reading once asset-only scaffolding is removed.",
}


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


def flags_html_for(sid, model, cond):
    flags = FLAGS.get((sid, model, cond), [])
    if not flags:
        return ""
    out = ['<div class="flags">']
    for f in flags:
        out.append(f'<div class="flag"><span class="flag-tag">{html.escape(f["type"])}:</span> {html.escape(f["text"])}</div>')
    out.append("</div>")
    return "".join(out)


def build_html(by_cond):
    parts = []
    parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Variant A Stripped-Observation — Coding Workshop 2026-05-11</title>
<style>
  body { font-family: Georgia, 'Times New Roman', serif; max-width: 1700px; margin: 1em auto; padding: 0 1em; line-height: 1.5; color: #222; }
  h1 { font-size: 1.6em; margin-bottom: 0.2em; }
  h2 { font-size: 1.3em; }
  .meta { color: #666; margin-bottom: 1.5em; }
  .legend { background: #f7f4ee; padding: 1em 1.5em; border: 1px solid #ddd; border-radius: 4px; margin-bottom: 2em; }
  .legend ul { margin: 0.4em 0; padding-left: 1.5em; }
  .legend li { margin-bottom: 0.3em; }
  .student-block { margin-bottom: 3em; border-top: 3px solid #333; padding-top: 1em; }
  .student-header { font-size: 1.35em; font-weight: bold; margin-bottom: 0.3em; }
  .student-id { color: #888; font-weight: normal; font-size: 0.85em; }
  .pattern-label { font-weight: bold; font-size: 0.9em; display: block; margin-top: 0.5em; }
  .pattern-field { width: 100%; min-height: 60px; font-family: Georgia, serif; font-size: 0.95em; padding: 0.5em; margin: 0.3em 0 1em 0; border: 1px solid #999; box-sizing: border-box; }
  .cross-note { background: #fffaef; border-left: 3px solid #c2941f; padding: 0.7em 1em; margin: 0.5em 0 1em 0; font-size: 0.9em; }
  table.cells { border-collapse: collapse; width: 100%; table-layout: fixed; }
  table.cells th, table.cells td { border: 1px solid #ccc; padding: 0.5em; vertical-align: top; font-size: 0.83em; }
  table.cells th { background: #ececec; font-weight: bold; }
  table.cells th.cond { font-family: 'Courier New', monospace; font-size: 0.85em; }
  table.cells th.cond small { display: block; font-family: Georgia, serif; font-size: 0.78em; font-weight: normal; color: #555; margin-top: 0.2em; }
  table.cells th.model { font-family: 'Courier New', monospace; width: 75px; background: #e0e0e0; }
  table.cells td.output { cursor: pointer; font-family: Georgia, serif; max-height: 380px; overflow-y: auto; white-space: pre-wrap; }
  .output.untouched { background: #fff; }
  .output.asset { background: #d4edda; }
  .output.deficit { background: #f8d7da; }
  .output.mixed { background: #fff3cd; }
  .output.concern { background: #ffe0b3; }
  .output.hallucination { background: #e5d4ed; }
  .flags { margin-top: 0.6em; }
  .flag { background: #fff8dc; border-left: 3px solid #c2941f; padding: 0.4em 0.6em; margin-top: 0.3em; font-size: 0.85em; }
  .flag-tag { font-weight: bold; color: #8b6914; font-family: 'Courier New', monospace; font-size: 0.85em; }
  .color-key { display: inline-block; padding: 0.2em 0.7em; margin: 0.15em; border-radius: 3px; font-size: 0.85em; border: 1px solid #aaa; }
  .controls { margin-top: 1em; }
  button { font-family: Georgia, serif; padding: 0.4em 0.9em; cursor: pointer; }
  .toc { background: #f0f0f0; padding: 0.7em 1em; margin-bottom: 1em; }
  .toc a { text-decoration: none; color: #1a4a7e; margin-right: 1em; font-family: 'Courier New', monospace; }
  .toc a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>Variant A Stripped-Observation — Coding Workshop</h1>
<p class="meta">2026-05-11 · 8 students × 4 conditions × 3 MLX models = 96 cells, n=1 (Llama 8B spot-check returned byte-identical at temp 0.3)</p>

<div class="legend">
  <h2>Conditions (progressive stripping)</h2>
  <ul>
    <li><strong>b_replicate</strong> — today's production prompt verbatim: equity floor + structural-power-moves taxonomy + relational/narrative epistemology paragraph + class context</li>
    <li><strong>a1</strong> — power-moves taxonomy STRIPPED (kept: equity floor + rel/narrative + class context)</li>
    <li><strong>a2</strong> — taxonomy + rel/narrative paragraph BOTH STRIPPED (kept: equity floor + class context)</li>
    <li><strong>a2_no_context</strong> — ALSO class context stripped (equity floor only in system prompt)</li>
  </ul>
  <h2>Color coding</h2>
  <p>Click any cell to cycle through:
    <span class="color-key untouched">untouched</span>
    <span class="color-key asset">asset frame</span>
    <span class="color-key deficit">deficit frame</span>
    <span class="color-key mixed">mixed</span>
    <span class="color-key concern">legit-concern flagged</span>
    <span class="color-key hallucination">hallucination / fabrication</span>
  </p>
  <p style="font-size: 0.9em; color: #555;">Categories are placeholders — replace, override, or extend as your reading develops. Pattern field and color states persist in browser localStorage. Use the buttons below to export or clear.</p>
  <div class="controls">
    <button onclick="exportState()">Export coding state as JSON</button>
    <button onclick="if(confirm('Clear ALL coding and pattern edits?')){localStorage.clear();location.reload();}">Clear all coding</button>
  </div>
</div>

<div class="toc">
  Jump to:
""")
    for sid in sorted(STUDENT_PATTERNS):
        # student name from first available cell
        nm = ""
        for c in CONDS:
            cell = get_cell(by_cond[c], "gemma12b", sid)
            if cell:
                nm = cell["student_name"]
                break
        parts.append(f'  <a href="#{sid}">{sid} {html.escape(nm.split()[-1] if nm else "")}</a>\n')
    parts.append("</div>\n")

    for sid in sorted(STUDENT_PATTERNS):
        nm = ""
        for c in CONDS:
            cell = get_cell(by_cond[c], "gemma12b", sid)
            if cell:
                nm = cell["student_name"]
                break
        parts.append(f'<div class="student-block" id="{sid}">')
        parts.append(f'<div class="student-header"><span class="student-id">{sid}</span> &nbsp; {html.escape(nm)}</div>')
        parts.append(f'<label class="pattern-label">Qualitative pattern this student represents (editable, persists locally):</label>')
        parts.append(f'<textarea class="pattern-field" id="pattern_{sid}">{html.escape(STUDENT_PATTERNS[sid])}</textarea>')
        cn = CROSS_CONDITION_NOTES.get(sid)
        if cn:
            parts.append(f'<div class="cross-note">{html.escape(cn).replace("**", "")}</div>')
        parts.append('<table class="cells">')
        parts.append('<tr><th class="model"></th>')
        for c in CONDS:
            label, sub = COND_LABELS[c]
            parts.append(f'<th class="cond">{label}<small>{html.escape(sub)}</small></th>')
        parts.append('</tr>')
        for m in MODELS:
            parts.append(f'<tr><th class="model">{m}</th>')
            for c in CONDS:
                cell = get_cell(by_cond[c], m, sid)
                output_text = cell["raw_output"].strip() if cell else "(no output)"
                cell_id = f"cell_{sid}_{m}_{c}"
                flags_html = flags_html_for(sid, m, c)
                parts.append(f'<td class="output" id="{cell_id}">{html.escape(output_text)}{flags_html}</td>')
            parts.append('</tr>')
        parts.append('</table>')
        parts.append('</div>')

    parts.append("""
<script>
  const COLORS = ['untouched','asset','deficit','mixed','concern','hallucination'];
  function setColor(cell, color) {
    COLORS.forEach(c => cell.classList.remove(c));
    cell.classList.add(color);
  }
  function cycleColor(cell) {
    const id = cell.id;
    let cur = 'untouched';
    for (const c of COLORS) if (cell.classList.contains(c)) { cur = c; break; }
    const next = COLORS[(COLORS.indexOf(cur) + 1) % COLORS.length];
    setColor(cell, next);
    localStorage.setItem('color_' + id, next);
  }
  function saveText(el) {
    localStorage.setItem('text_' + el.id, el.value);
  }
  document.querySelectorAll('td.output').forEach(c => {
    const saved = localStorage.getItem('color_' + c.id);
    setColor(c, saved || 'untouched');
    c.addEventListener('click', (e) => {
      // don't cycle if user is selecting text or clicking inside a flag
      if (window.getSelection().toString().length > 0) return;
      if (e.target.closest('.flag')) return;
      cycleColor(c);
    });
  });
  document.querySelectorAll('textarea.pattern-field').forEach(t => {
    const saved = localStorage.getItem('text_' + t.id);
    if (saved !== null) t.value = saved;
    t.addEventListener('input', () => saveText(t));
  });
  function exportState() {
    const state = { date: new Date().toISOString(), colors: {}, patterns: {} };
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k.startsWith('color_')) state.colors[k.slice(6)] = localStorage.getItem(k);
      if (k.startsWith('text_')) state.patterns[k.slice(5)] = localStorage.getItem(k);
    }
    const blob = new Blob([JSON.stringify(state, null, 2)], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'variant_a_coding_state_' + new Date().toISOString().slice(0,10) + '.json';
    a.click();
    URL.revokeObjectURL(url);
  }
</script>
</body>
</html>
""")
    return "".join(parts)


def main():
    by_cond = load_all()
    out_html = build_html(by_cond)
    OUT_HTML.write_text(out_html, encoding="utf-8")
    print(f"Wrote {OUT_HTML} ({OUT_HTML.stat().st_size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
