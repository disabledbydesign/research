#!/usr/bin/env python3
"""Byte-level validation: every cell.ai_codes field in the augmented workshop HTML
must match the corresponding entry in the source Opus / Gemini coding-pass JSONs
verbatim.

Confirms the augmentation step injected the AI scaffolding without corrupting
any field (description, deficit quote/note, concern quote/note, other notable).

Companion to validate_workshop_against_json.py — that script confirms cell.text
matches raw_outputs/; this one confirms cell.ai_codes.{opus,gemini} matches the
coding-pass JSONs.

Usage:
    python3 scripts/validate_ai_codes_against_passes.py
    python3 scripts/validate_ai_codes_against_passes.py path/to/workshop.html
"""

import json
import sys
import difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HTML = ROOT / "data_tables" / "variant_a_coding_workshop_with_ai_codes_2026-05-11.html"
AI_DIR = ROOT / "data_tables" / "variant_a_ai_coding_2026-05-11"
OPUS_JSON = AI_DIR / "variant_a_coding_pass_opus_2026-05-11.json"
GEMINI_JSON = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"

# Fields in ai_codes.{coder} mapped to their path inside the coding-pass per_cell entry.
# Each value is a function that extracts the equivalent from the source coder cell.
FIELD_MAP = {
    "description": lambda c: c.get("description"),
    "concern_quote": lambda c: (c.get("concern_flagged") or {}).get("quote"),
    "concern_note": lambda c: (c.get("concern_flagged") or {}).get("note"),
    "deficit_quote": lambda c: (c.get("deficit_language") or {}).get("quote"),
    "deficit_note": lambda c: (c.get("deficit_language") or {}).get("note"),
    "other": lambda c: c.get("other_notable"),
}


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


def norm(v):
    """Normalize for comparison: None and empty string are equivalent (the augmenter
    stores empty descriptions as empty string for legibility; coders may emit either)."""
    if v is None:
        return ""
    return v


def main():
    html_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HTML
    if not html_path.exists():
        sys.exit(f"ERROR: HTML not found: {html_path}")
    print(f"Validating: {html_path}")
    print(f"  against Opus: {OPUS_JSON}")
    print(f"  against Gemini: {GEMINI_JSON}")

    html_text = html_path.read_text(encoding="utf-8")
    embedded = extract_embedded_data(html_text)

    opus = json.loads(OPUS_JSON.read_text())
    gemini = json.loads(GEMINI_JSON.read_text())
    opus_by_cell = {c["cell_id"]: c for c in opus["per_cell"]}
    gemini_by_cell = {c["cell_id"]: c for c in gemini["per_cell"]}

    html_cells = embedded["cells"]
    total = 0
    field_checks = 0
    mismatches = []
    missing_ai_codes = []
    missing_in_pass = {"opus": [], "gemini": []}

    for cid, cdata in html_cells.items():
        total += 1
        ai = cdata.get("ai_codes")
        if not ai:
            missing_ai_codes.append(cid)
            continue

        for coder_key, source_idx in (("opus", opus_by_cell), ("gemini", gemini_by_cell)):
            src_cell = source_idx.get(cid)
            if not src_cell:
                missing_in_pass[coder_key].append(cid)
                continue
            html_block = ai.get(coder_key) or {}
            for field, extractor in FIELD_MAP.items():
                field_checks += 1
                html_val = norm(html_block.get(field))
                src_val = norm(extractor(src_cell))
                if html_val != src_val:
                    diff_lines = list(
                        difflib.unified_diff(
                            (src_val or "").splitlines() or [""],
                            (html_val or "").splitlines() or [""],
                            fromfile=f"source[{coder_key}/{cid}/{field}]",
                            tofile=f"html.ai_codes[{coder_key}/{cid}/{field}]",
                            lineterm="",
                            n=1,
                        )
                    )
                    mismatches.append((cid, coder_key, field, diff_lines, len(src_val), len(html_val)))

    # Reverse: pass cells missing from HTML?
    html_cell_ids = set(html_cells.keys())
    pass_only = {
        "opus": sorted(set(opus_by_cell.keys()) - html_cell_ids),
        "gemini": sorted(set(gemini_by_cell.keys()) - html_cell_ids),
    }

    # Report
    print(f"\nValidated {total} cells × 2 coders × {len(FIELD_MAP)} fields = {field_checks} field checks.")
    print(f"  exact-match: {field_checks - len(mismatches)}")
    print(f"  mismatches: {len(mismatches)}")
    print(f"  cells without ai_codes: {len(missing_ai_codes)}")
    print(f"  cells missing in opus pass: {len(missing_in_pass['opus'])}")
    print(f"  cells missing in gemini pass: {len(missing_in_pass['gemini'])}")
    print(f"  pass cells not present in HTML (opus): {len(pass_only['opus'])}")
    print(f"  pass cells not present in HTML (gemini): {len(pass_only['gemini'])}")

    if mismatches:
        print("\n--- AI_CODES MISMATCHES ---")
        for cid, coder, field, diff_lines, src_len, html_len in mismatches:
            print(f"\n## {cid} · {coder} · {field}  (source: {src_len} chars, html: {html_len} chars)")
            print("\n".join(diff_lines[:30]))
            if len(diff_lines) > 30:
                print(f"... {len(diff_lines) - 30} more diff lines")
    if missing_ai_codes:
        print("\n--- CELLS WITHOUT ai_codes FIELD ---")
        for cid in missing_ai_codes[:20]:
            print(f"  {cid}")
        if len(missing_ai_codes) > 20:
            print(f"  ... and {len(missing_ai_codes) - 20} more")
    for coder, missing in missing_in_pass.items():
        if missing:
            print(f"\n--- CELLS MISSING IN {coder.upper()} PASS ---")
            for cid in missing[:20]:
                print(f"  {cid}")
            if len(missing) > 20:
                print(f"  ... and {len(missing) - 20} more")
    for coder, only in pass_only.items():
        if only:
            print(f"\n--- {coder.upper()} PASS CELLS NOT IN HTML ---")
            for cid in only[:20]:
                print(f"  {cid}")

    if mismatches or missing_ai_codes or any(missing_in_pass.values()) or any(pass_only.values()):
        sys.exit(1)
    print("\nAll ai_codes fields match source coding-pass JSONs verbatim.")


if __name__ == "__main__":
    main()
