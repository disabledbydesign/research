#!/usr/bin/env python3
"""
Build the input bundle for the evaluative coding pass.

For each of the 96 cells, package: student_submission, model_output (cell.text),
the coder's own open codes, the cross_notes for that student, the student_seed,
plus high-level conditions metadata. This is what both Opus and Gemini will
read in pass 2.

Reads:
  - data_tables/variant_a_ai_coding_2026-05-11/variant_a_cells_for_coding.json
  - data_tables/variant_a_ai_coding_2026-05-11/variant_a_coding_pass_opus_2026-05-11.json
  - data_tables/variant_a_ai_coding_2026-05-11/variant_a_coding_pass_gemini_2026-05-11.json
  - data_tables/variant_a_ai_coding_2026-05-11/student_submissions_2026-05-11.json

Writes:
  - data_tables/variant_a_ai_coding_2026-05-11/evaluative_pass_input_opus.json
  - data_tables/variant_a_ai_coding_2026-05-11/evaluative_pass_input_gemini.json

Each output is the bundle for ONE coder's evaluative pass (only that coder's
own open codes are included to preserve inter-coder integrity).
"""
import json
from pathlib import Path

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
AI_DIR = ROOT / "data_tables" / "variant_a_ai_coding_2026-05-11"
CELLS = AI_DIR / "variant_a_cells_for_coding.json"
OPUS_PASS = AI_DIR / "variant_a_coding_pass_opus_2026-05-11.json"
GEMINI_PASS = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"
SUBS = AI_DIR / "student_submissions_2026-05-11.json"
OUT_OPUS = AI_DIR / "evaluative_pass_input_opus.json"
OUT_GEMINI = AI_DIR / "evaluative_pass_input_gemini.json"


def main():
    cells_payload = json.loads(CELLS.read_text())
    opus = json.loads(OPUS_PASS.read_text())
    gemini = json.loads(GEMINI_PASS.read_text())
    subs = json.loads(SUBS.read_text())

    opus_by_cell = {c["cell_id"]: c for c in opus["per_cell"]}
    gemini_by_cell = {c["cell_id"]: c for c in gemini["per_cell"]}
    students = subs["students"]

    def build_for_coder(coder_name: str, coder_by_cell: dict, out_path: Path):
        cells_out = {}
        for cid, cell in cells_payload["cells"].items():
            sid = cell["sid"]
            student = students.get(sid, {})
            own_codes = coder_by_cell.get(cid, {})
            cells_out[cid] = {
                "cell_id": cid,
                "sid": sid,
                "student_name": cell["student_name"],
                "model": cell["model"],
                "condition": cell["condition"],
                "student_submission": student.get("submission"),
                "model_output": cell["text"],
                "own_open_codes": {
                    "description": own_codes.get("description"),
                    "concern_quote": (own_codes.get("concern_flagged") or {}).get("quote"),
                    "concern_note": (own_codes.get("concern_flagged") or {}).get("note"),
                    "deficit_quote": (own_codes.get("deficit_language") or {}).get("quote"),
                    "deficit_note": (own_codes.get("deficit_language") or {}).get("note"),
                    "other_notable": own_codes.get("other_notable"),
                },
                "student_seed": cells_payload["student_seeds"].get(sid, ""),
                "cross_notes_for_student": cells_payload["cross_notes"].get(sid, ""),
            }
        out = {
            "coder": coder_name,
            "pass": "evaluative_input",
            "pass_date": "2026-05-11",
            "cond_labels": cells_payload["cond_labels"],
            "n_cells": len(cells_out),
            "cells": cells_out,
        }
        out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
        size_mb = out_path.stat().st_size / 1e6
        print(f"Wrote {out_path}  ({size_mb:.2f} MB, {len(cells_out)} cells)")

    build_for_coder("opus", opus_by_cell, OUT_OPUS)
    build_for_coder("gemini-2.5-pro", gemini_by_cell, OUT_GEMINI)


if __name__ == "__main__":
    main()
