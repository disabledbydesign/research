#!/usr/bin/env python3
"""Compare unified-genob observations across the three supersedes conditions
(both / single / neither) side by side per student.

Usage:
    python scripts/build_unified_genob_workshop.py \
        data/raw_outputs/test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-13_0739.json \
        data/raw_outputs/test_unified_genob_single_FULL_CORPUS_gemma12b_2026-05-13_0822.json \
        data/raw_outputs/test_unified_genob_neither_FULL_CORPUS_gemma12b_2026-05-13_0905.json \
        [--corpus-review data_tables/corpus_overview/corpus_review_state.json] \
        [--out data_tables/unified_genob_workshop_2026-05-13.html]

Optional: pass additional --file path label triples to add extra comparison columns
(e.g. a no-hedging rerun):
        --extra-file path "no-hedging"
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS_REVIEW_DEFAULT = ROOT / "data_tables/corpus_overview/corpus_review_state.json"
OUT_DEFAULT = ROOT / "data_tables/unified_genob_workshop_2026-05-13.html"


def _sort_key(sid: str):
    prefix = 0 if sid.startswith("S") else 1
    try:
        num = int(sid[2:] if sid.startswith("WB") else sid[1:])
    except ValueError:
        num = 999
    return (prefix, num)


def load_genob_file(path: Path, label: str) -> dict:
    """Returns {student_id: {name, observation, reasoning, confidence, error}}"""
    raw = json.loads(path.read_text())
    results = raw.get("results", [])
    out = {}
    for r in results:
        if r.get("run") != 1:
            continue
        sid = r["student_id"]
        out[sid] = {
            "name": r.get("student_name", ""),
            "observation": r.get("observation", ""),
            "reasoning": r.get("reasoning", ""),
            "confidence": r.get("confidence", 0.0),
            "error": r.get("error"),
            "source": r.get("source", ""),
        }
    return out


def load_corpus_review(path: Path) -> dict:
    """Returns {sid: {pattern, expected, notes}} from corpus_review_state.json."""
    raw = json.loads(path.read_text())
    out = {}
    for key, val in raw.items():
        for prefix in ("pattern_", "expected_", "notes_", "reviewed_"):
            if key.startswith(prefix):
                sid = key[len(prefix):]
                if sid not in out:
                    out[sid] = {}
                out[sid][prefix.rstrip("_")] = val
                break
    return out


def _esc(s: str) -> str:
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_html(columns: list[tuple[str, dict]], corpus_review: dict,
               all_sids: list[str]) -> str:
    """Build full HTML string.

    columns: list of (label, {sid: obs_data}) in order
    """
    col_width = max(200, 900 // max(len(columns), 1))

    rows_html = []
    for sid in all_sids:
        is_wb = sid.startswith("WB")
        cr = corpus_review.get(sid, {})
        pattern = cr.get("pattern", "")
        expected = cr.get("expected", "")
        notes = cr.get("notes", "")

        # Expected badge color
        exp_color = {
            "CRISIS": "#c0392b",
            "BURNOUT": "#d68910",
            "EDGE": "#c8a000",
            "ENGAGED": "#5fa05f",
        }.get(expected, "#888")

        # Get name from first column that has this student
        name = ""
        for _, col_data in columns:
            if sid in col_data:
                name = col_data[sid]["name"]
                break

        wb_badge = f'<span class="wb-badge">WB</span>' if is_wb else ""
        exp_badge = (f'<span class="exp-badge" style="background:{exp_color}">'
                     f'{_esc(expected)}</span>') if expected else ""

        # Student info cell
        info_html = f"""<td class="info-cell">
  <div class="sid">{_esc(sid)}</div>
  <div class="sname">{_esc(name)}</div>
  <div class="badges">{wb_badge}{exp_badge}</div>"""
        if pattern:
            info_html += f'\n  <div class="pattern">{_esc(pattern)}</div>'
        if notes:
            info_html += f'\n  <div class="notes-label">Notes</div><div class="notes-text">{_esc(notes)}</div>'
        info_html += "\n</td>"

        # Observation columns
        obs_cells = []
        for label, col_data in columns:
            entry = col_data.get(sid)
            if not entry:
                obs_cells.append('<td class="obs-cell"><span class="no-data">—</span></td>')
                continue
            obs = entry["observation"]
            reasoning = entry["reasoning"]
            conf = entry["confidence"]
            err = entry["error"]

            conf_pct = int(conf * 100)
            conf_color = "#5fa05f" if conf >= 0.75 else ("#d68910" if conf >= 0.5 else "#c0392b")

            err_html = f'<div class="error-note">ERROR: {_esc(str(err))}</div>' if err else ""
            obs_html = f'<div class="obs-text">{_esc(obs)}</div>' if obs else '<div class="no-data">no observation</div>'
            reasoning_html = ""
            if reasoning:
                reasoning_html = f'<details class="reasoning-details"><summary>reasoning</summary><div class="reasoning-text">{_esc(reasoning)}</div></details>'

            conf_html = f'<div class="conf-bar"><span class="conf-label">conf</span><span class="conf-val" style="color:{conf_color}">{conf_pct}%</span></div>'

            obs_cells.append(f"""<td class="obs-cell">
{err_html}{obs_html}{reasoning_html}{conf_html}
</td>""")

        row_class = "wb-row" if is_wb else "es-row"
        rows_html.append(
            f'<tr class="{row_class}">{info_html}{"".join(obs_cells)}</tr>'
        )

    # Build column headers
    header_cells = ['<th class="info-col">Student</th>']
    for label, _ in columns:
        header_cells.append(f'<th class="obs-col">{_esc(label)}</th>')

    col_style = "\n".join(
        f"  table.main col.obs-col {{ width: {col_width}px; }}" for _ in columns
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Unified Genob Workshop — 2026-05-13</title>
<style>
* {{ box-sizing: border-box; }}
body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 2200px; margin: 1em auto; padding: 0 1em; line-height: 1.5; color: #222; background: #fafaf7; }}
h1 {{ font-size: 1.2em; margin-bottom: 0.2em; }}
.subtitle {{ font-size: 0.85em; color: #666; margin-bottom: 1em; }}

/* Controls */
.controls {{ position: sticky; top: 0; background: #fafaf7; padding: 0.3em 0; z-index: 20; border-bottom: 1px solid #ddd; margin-bottom: 0.6em; display: flex; align-items: center; gap: 0.5em; flex-wrap: wrap; }}
.controls button {{ padding: 0.25em 0.6em; cursor: pointer; font-family: Georgia, serif; font-size: 0.82em; border: 1px solid #bbb; border-radius: 3px; background: #fff; }}
.controls button.active {{ background: #1a4a7e; color: #fff; border-color: #1a4a7e; }}
.filter-label {{ font-size: 0.82em; color: #555; }}

/* Table */
table.main {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
table.main col.info-col {{ width: 210px; }}
table.main th {{ background: #ececec; font-weight: bold; padding: 0.4em 0.5em; font-size: 0.8em; border: 1px solid #ccc; text-align: left; position: sticky; top: 38px; z-index: 10; }}
table.main th.info-col {{ background: #e0ddd4; }}
table.main th.obs-col {{ background: #dce6f4; color: #1a4a7e; font-family: 'Courier New', monospace; font-size: 0.75em; }}
table.main td {{ border: 1px solid #ccc; vertical-align: top; padding: 0; }}

/* Info cell */
td.info-cell {{ padding: 0.5em 0.55em; background: #f7f4ee; font-size: 0.8em; }}
.sid {{ font-family: 'Courier New', monospace; font-weight: bold; font-size: 0.95em; }}
.sname {{ color: #555; font-size: 0.88em; margin-bottom: 0.15em; }}
.badges {{ display: flex; gap: 0.3em; flex-wrap: wrap; margin: 0.15em 0; }}
.wb-badge {{ display: inline-block; background: #c2941f; color: #fff; font-size: 0.68em; padding: 0.08em 0.35em; border-radius: 3px; font-family: 'Courier New', monospace; }}
.exp-badge {{ display: inline-block; color: #fff; font-size: 0.68em; padding: 0.08em 0.35em; border-radius: 3px; font-family: 'Courier New', monospace; font-weight: bold; }}
.pattern {{ font-size: 0.78em; color: #4a3800; background: #fffbeb; border: 1px solid #e6d28a; border-radius: 3px; padding: 0.3em 0.4em; margin-top: 0.3em; line-height: 1.4; }}
.notes-label {{ font-family: 'Courier New', monospace; font-size: 0.66em; color: #8b6914; text-transform: uppercase; margin-top: 0.4em; }}
.notes-text {{ font-size: 0.76em; color: #5a4500; font-style: italic; line-height: 1.4; }}

/* Obs cell */
td.obs-cell {{ padding: 0.45em 0.5em; background: #fff; font-size: 0.82em; min-height: 120px; }}
.obs-text {{ line-height: 1.45; color: #222; }}
.no-data {{ color: #bbb; font-style: italic; }}
.error-note {{ color: #c0392b; font-size: 0.78em; margin-bottom: 0.3em; font-family: 'Courier New', monospace; }}
.conf-bar {{ margin-top: 0.4em; display: flex; gap: 0.3em; align-items: center; }}
.conf-label {{ font-family: 'Courier New', monospace; font-size: 0.68em; color: #999; text-transform: uppercase; }}
.conf-val {{ font-family: 'Courier New', monospace; font-size: 0.82em; font-weight: bold; }}
.reasoning-details {{ margin-top: 0.35em; }}
.reasoning-details summary {{ font-family: 'Courier New', monospace; font-size: 0.7em; color: #888; cursor: pointer; }}
.reasoning-text {{ font-size: 0.77em; color: #555; font-style: italic; margin-top: 0.2em; line-height: 1.4; border-left: 2px solid #ccc; padding-left: 0.5em; }}

/* Row coloring */
tr.wb-row td {{ background: #fffdf5; }}
tr.wb-row td.info-cell {{ background: #fef9e7; }}
tr.wb-row.hidden, tr.es-row.hidden {{ display: none; }}
</style>
</head>
<body>
<h1>Unified Genob Conditions — Side-by-Side Workshop</h1>
<div class="subtitle">Supersedes states: both | single | neither &nbsp;·&nbsp; Gemma 12B &nbsp;·&nbsp; run==1 &nbsp;·&nbsp; 2026-05-13</div>

<div class="controls">
  <span class="filter-label">Show:</span>
  <button class="active" onclick="showAll()">All students</button>
  <button onclick="showOnly('wb-row')">WB only</button>
  <button onclick="showOnly('es-row')">ES only</button>
  <button onclick="hideBlank()">Hide no-disclosure (S+ clean)</button>
</div>

<table class="main" id="main-table">
<colgroup>
  <col class="info-col">
  {"".join('<col class="obs-col">' for _ in columns)}
</colgroup>
<thead>
<tr>{"".join(header_cells)}</tr>
</thead>
<tbody>
{"".join(rows_html)}
</tbody>
</table>

<script>
function showAll() {{
  document.querySelectorAll('#main-table tbody tr').forEach(r => r.classList.remove('hidden'));
  document.querySelectorAll('.controls button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}}
function showOnly(cls) {{
  document.querySelectorAll('#main-table tbody tr').forEach(r => {{
    r.classList.toggle('hidden', !r.classList.contains(cls));
  }});
  document.querySelectorAll('.controls button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}}
function hideBlank() {{
  document.querySelectorAll('#main-table tbody tr.es-row').forEach(r => r.classList.add('hidden'));
  document.querySelectorAll('.controls button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}}
</script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Build unified genob comparison workshop HTML")
    parser.add_argument("files", nargs="+",
                        help="Genob JSON files to compare (in display order)")
    parser.add_argument("--labels", nargs="*",
                        help="Column labels for each file (default: derived from filename)")
    parser.add_argument("--corpus-review", type=Path, default=CORPUS_REVIEW_DEFAULT,
                        help="corpus_review_state.json path")
    parser.add_argument("--out", type=Path, default=OUT_DEFAULT,
                        help="Output HTML path")
    args = parser.parse_args()

    paths = [Path(f) for f in args.files]
    labels = args.labels or [None] * len(paths)
    if len(labels) < len(paths):
        labels += [None] * (len(paths) - len(labels))

    def _auto_label(p: Path) -> str:
        stem = p.stem
        for cond in ("neither", "single", "both"):
            if cond in stem:
                return f"genob-{cond}"
        return stem[:40]

    columns = []
    all_sids_set = set()
    for path, label in zip(paths, labels):
        col_label = label or _auto_label(path)
        data = load_genob_file(path, col_label)
        columns.append((col_label, data))
        all_sids_set |= set(data.keys())
        print(f"Loaded {len(data)} students from {path.name} → column '{col_label}'")

    all_sids = sorted(all_sids_set, key=_sort_key)

    corpus_review = {}
    if args.corpus_review.exists():
        corpus_review = load_corpus_review(args.corpus_review)
        print(f"Loaded corpus review for {len(corpus_review)} students")
    else:
        print(f"Warning: corpus review not found at {args.corpus_review}")

    html = build_html(columns, corpus_review, all_sids)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html, encoding="utf-8")
    print(f"\nWritten: {args.out}")
    print(f"  {len(all_sids)} students × {len(columns)} conditions")


if __name__ == "__main__":
    main()
