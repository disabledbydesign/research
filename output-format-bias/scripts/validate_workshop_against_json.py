#!/usr/bin/env python3
"""Byte-level validation: every cell in the workshop HTML must match the
corresponding raw_output in the source JSON files, verbatim (after .strip()).

Extracts the embedded DATA JS object from the HTML, parses it, and diffs
each cell against the canonical JSON output. Reports any mismatch in detail.
"""

import json
import sys
import difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "variant_a_coding_workshop_2026-05-11.html"
OUT_DIR = ROOT / "data" / "raw_outputs"

CONDS = ["b_replicate", "a1", "a2", "a2_no_context"]
COND_FILES = {c: f"test_variant_{c}_observation_2026-05-11.json" for c in CONDS}


def extract_embedded_data(html_text: str) -> dict:
    marker = "const DATA = "
    start = html_text.index(marker) + len(marker)
    # brace counter, skipping strings
    i = start
    depth = 0
    in_string = False
    escape = False
    while i < len(html_text):
        c = html_text[i]
        if escape:
            escape = False
        elif in_string:
            if c == "\\":
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return json.loads(html_text[start : i + 1])
        i += 1
    raise ValueError("Did not find closing brace for DATA")


def main():
    html_text = HTML.read_text(encoding="utf-8")
    embedded = extract_embedded_data(html_text)

    sources = {}
    for c in CONDS:
        with open(OUT_DIR / COND_FILES[c]) as f:
            sources[c] = json.load(f)

    total = 0
    mismatches = []
    missing_in_html = []
    missing_in_source = []
    metadata_issues = []

    # Build expected map: (sid, model, cond) -> raw_output
    expected = {}
    for c, src in sources.items():
        for m, runs in src["results_by_model"].items():
            for r in runs:
                expected[(r["student_id"], m, c)] = r["raw_output"].strip()
                # also pin student_name for cross-check
                expected[("__name__", r["student_id"])] = r["student_name"]

    html_cells = embedded["cells"]
    for cid, cdata in html_cells.items():
        total += 1
        sid = cdata["sid"]
        m = cdata["model"]
        c = cdata["condition"]
        key = (sid, m, c)
        if key not in expected:
            missing_in_source.append(cid)
            continue
        src_text = expected[key]
        html_text_cell = cdata["text"]
        if src_text != html_text_cell:
            d = list(
                difflib.unified_diff(
                    src_text.splitlines(),
                    html_text_cell.splitlines(),
                    fromfile=f"source[{c}/{m}/{sid}]",
                    tofile=f"html[{cid}]",
                    lineterm="",
                    n=1,
                )
            )
            mismatches.append((cid, d, len(src_text), len(html_text_cell)))
        # student name check
        src_name = expected.get(("__name__", sid))
        if cdata.get("student_name") != src_name:
            metadata_issues.append(
                f"{cid}: student_name mismatch: html={cdata.get('student_name')!r} vs source={src_name!r}"
            )

    # Reverse: any source cell missing from HTML?
    expected_keys = {k for k in expected.keys() if isinstance(k, tuple) and len(k) == 3}
    html_keys = {(cdata["sid"], cdata["model"], cdata["condition"]) for cdata in html_cells.values()}
    for k in expected_keys - html_keys:
        missing_in_html.append(k)

    # Top-level metadata cross-checks
    if set(embedded["conds"]) != set(CONDS):
        metadata_issues.append(f"conds mismatch: {embedded['conds']} vs {CONDS}")
    src_student_ids = sorted({sid for (sid, _, _) in expected_keys})
    if sorted(embedded["student_ids"]) != src_student_ids:
        metadata_issues.append(
            f"student_ids mismatch: {sorted(embedded['student_ids'])} vs {src_student_ids}"
        )
    src_models = sorted({m for (_, m, _) in expected_keys})
    if sorted(embedded["models"]) != src_models:
        metadata_issues.append(f"models mismatch: {sorted(embedded['models'])} vs {src_models}")

    # Report
    print(f"Validated {total} cells in HTML against source JSONs.")
    print(f"  exact-match: {total - len(mismatches)}")
    print(f"  mismatches: {len(mismatches)}")
    print(f"  missing in HTML (in source but not HTML): {len(missing_in_html)}")
    print(f"  missing in source (in HTML but not source): {len(missing_in_source)}")
    print(f"  metadata issues: {len(metadata_issues)}")

    if mismatches:
        print("\n--- MISMATCHES ---")
        for cid, diff_lines, src_len, html_len in mismatches:
            print(f"\n## {cid}  (source: {src_len} chars, html: {html_len} chars)")
            print("\n".join(diff_lines[:40]))
            if len(diff_lines) > 40:
                print(f"... {len(diff_lines) - 40} more diff lines")
    if missing_in_html:
        print("\n--- MISSING IN HTML ---")
        for k in missing_in_html:
            print(f"  {k}")
    if missing_in_source:
        print("\n--- MISSING IN SOURCE ---")
        for cid in missing_in_source:
            print(f"  {cid}")
    if metadata_issues:
        print("\n--- METADATA ISSUES ---")
        for m in metadata_issues:
            print(f"  {m}")

    if mismatches or missing_in_html or missing_in_source or metadata_issues:
        sys.exit(1)
    print("\nAll cells match source verbatim.")


if __name__ == "__main__":
    main()
