#!/usr/bin/env python3
"""Byte-level validation: every cell.eval_codes field in the augmented workshop
must match the corresponding entry in the source evaluative-pass JSONs verbatim.

Companion to:
  - validate_workshop_against_json.py    (cell.text vs raw_outputs)
  - validate_ai_codes_against_passes.py  (cell.ai_codes vs open-coding passes)

This script confirms cell.eval_codes.{opus,gemini} fields match the
evaluative-pass JSONs character-for-character (booleans, lists, strings).

Usage:
    python3 scripts/validate_eval_codes_against_passes.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HTML = ROOT / "data_tables" / "variant_a_coding_workshop_with_ai_codes_2026-05-11.html"
AI_DIR = ROOT / "data_tables" / "variant_a_ai_coding_2026-05-11"
EVAL_OPUS = AI_DIR / "variant_a_evaluative_pass_opus_2026-05-11.json"
EVAL_GEMINI = AI_DIR / "variant_a_evaluative_pass_gemini_2026-05-11.json"

# Each field in cell.eval_codes.{coder} maps to a per-cell source field.
SCALAR_FIELDS = ["tp_present", "fp_present", "hallucination_present", "unclear_present",
                 "summary_verdict", "reasoning"]
LIST_FIELDS = ["tp_examples", "fp_examples", "hallucination_examples", "unclear_examples"]


def extract_embedded_data(html_text: str) -> dict:
    marker = "const DATA = "
    start = html_text.index(marker) + len(marker)
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


def expected_for_field(src_cell: dict, field: str):
    # Source eval pass uses same field names; for booleans, coerce to bool;
    # for lists, default to []; for strings, default to "" / "unknown" / None pass-through.
    v = src_cell.get(field)
    if field.endswith("_present"):
        return bool(v)
    if field in LIST_FIELDS:
        return v or []
    if field == "summary_verdict":
        return v or "unknown"
    if field == "reasoning":
        return v or ""
    return v


def main():
    html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HTML
    if not html_path.exists():
        sys.exit(f"ERROR: HTML not found: {html_path}")
    print(f"Validating: {html_path}")
    print(f"  against Opus eval: {EVAL_OPUS}")
    print(f"  against Gemini eval: {EVAL_GEMINI}")

    html_text = html_path.read_text(encoding="utf-8")
    embedded = extract_embedded_data(html_text)

    opus = json.loads(EVAL_OPUS.read_text())
    gemini = json.loads(EVAL_GEMINI.read_text())
    opus_by_cell = {c["cell_id"]: c for c in opus["per_cell"]}
    gemini_by_cell = {c["cell_id"]: c for c in gemini["per_cell"]}

    html_cells = embedded["cells"]
    total = 0
    field_checks = 0
    mismatches = []
    missing_eval_codes = []
    missing_in_pass = {"opus": [], "gemini": []}

    all_fields = SCALAR_FIELDS + LIST_FIELDS

    for cid, cdata in html_cells.items():
        total += 1
        ec = cdata.get("eval_codes")
        if not ec:
            missing_eval_codes.append(cid)
            continue
        for coder_key, source_idx in (("opus", opus_by_cell), ("gemini", gemini_by_cell)):
            src_cell = source_idx.get(cid)
            if not src_cell:
                missing_in_pass[coder_key].append(cid)
                continue
            html_block = ec.get(coder_key) or {}
            for field in all_fields:
                field_checks += 1
                html_val = html_block.get(field)
                src_val = expected_for_field(src_cell, field)
                if field.endswith("_present"):
                    html_val = bool(html_val)
                if field in LIST_FIELDS:
                    html_val = html_val or []
                if html_val != src_val:
                    mismatches.append({
                        "cell_id": cid,
                        "coder": coder_key,
                        "field": field,
                        "html_value": html_val,
                        "source_value": src_val,
                    })

    # Reverse: any source cells missing from HTML?
    html_cell_ids = set(html_cells.keys())
    pass_only = {
        "opus": sorted(set(opus_by_cell.keys()) - html_cell_ids),
        "gemini": sorted(set(gemini_by_cell.keys()) - html_cell_ids),
    }

    # Report
    print(f"\nValidated {total} cells × 2 coders × {len(all_fields)} fields = {field_checks} field checks.")
    print(f"  exact-match: {field_checks - len(mismatches)}")
    print(f"  mismatches: {len(mismatches)}")
    print(f"  cells without eval_codes: {len(missing_eval_codes)}")
    print(f"  cells missing in opus pass: {len(missing_in_pass['opus'])}")
    print(f"  cells missing in gemini pass: {len(missing_in_pass['gemini'])}")
    print(f"  pass cells not present in HTML (opus): {len(pass_only['opus'])}")
    print(f"  pass cells not present in HTML (gemini): {len(pass_only['gemini'])}")

    if mismatches:
        print("\n--- EVAL_CODES MISMATCHES ---")
        for m in mismatches[:20]:
            print(f"\n## {m['cell_id']} · {m['coder']} · {m['field']}")
            print(f"  html:   {repr(m['html_value'])[:200]}")
            print(f"  source: {repr(m['source_value'])[:200]}")
        if len(mismatches) > 20:
            print(f"\n... and {len(mismatches) - 20} more mismatches")
    if missing_eval_codes:
        print("\n--- CELLS WITHOUT eval_codes FIELD ---")
        for cid in missing_eval_codes[:20]:
            print(f"  {cid}")
    for coder, missing in missing_in_pass.items():
        if missing:
            print(f"\n--- CELLS MISSING IN {coder.upper()} PASS ---")
            for cid in missing[:20]:
                print(f"  {cid}")
    for coder, only in pass_only.items():
        if only:
            print(f"\n--- {coder.upper()} PASS CELLS NOT IN HTML ---")
            for cid in only[:20]:
                print(f"  {cid}")

    if mismatches or missing_eval_codes or any(missing_in_pass.values()) or any(pass_only.values()):
        sys.exit(1)
    print("\nAll eval_codes fields match source evaluative-pass JSONs verbatim.")


if __name__ == "__main__":
    main()
