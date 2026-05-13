#!/usr/bin/env python3
"""
Extract student submissions (verbatim) from the raw_output prompts, one per student.

The student submission is embedded in the prompt between markers:
  SUBMISSION:\\n---\\n<student writing>\\n---

The submission should be IDENTICAL across all 4 conditions and all 3 models
for a given student (conditions differ in scaffolding around the prompt; the
student writing itself is fixed). This script verifies that and writes a
canonical per-student submission file.

Reads:  data/raw_outputs/test_variant_*_observation_2026-05-11.json (all 4)
Writes: data_tables/variant_a_ai_coding_2026-05-11/student_submissions_2026-05-11.json
        Structure: {sid: {"student_name": str, "submission": str}}
        plus a verification report on identity-across-conditions.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
RAW_DIR = ROOT / "data" / "raw_outputs"
AI_DIR = ROOT / "data_tables" / "variant_a_ai_coding_2026-05-11"
OUT = AI_DIR / "student_submissions_2026-05-11.json"

CONDS = ["b_replicate", "a1", "a2", "a2_no_context"]
RAW_FILES = {c: RAW_DIR / f"test_variant_{c}_observation_2026-05-11.json" for c in CONDS}

# Match SUBMISSION:\n---\n<body>\n---\n  (body captured, non-greedy)
SUBMISSION_RX = re.compile(r"SUBMISSION:\s*\n---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_submission(prompt: str) -> str | None:
    m = SUBMISSION_RX.search(prompt)
    if not m:
        return None
    return m.group(1).strip()


def main():
    # gather: {sid: {(model, cond): submission}}
    seen = defaultdict(dict)
    names = {}

    for cond, path in RAW_FILES.items():
        if not path.exists():
            sys.exit(f"ERROR: missing raw_output file: {path}")
        data = json.loads(path.read_text())
        for model, runs in data["results_by_model"].items():
            for r in runs:
                sid = r["student_id"]
                names[sid] = r["student_name"]
                sub = extract_submission(r["prompt"])
                if sub is None:
                    sys.exit(f"ERROR: could not extract submission from {cond}/{model}/{sid}")
                seen[sid][(model, cond)] = sub

    # Verify identity across (model, cond) per student
    discrepancies = []
    canonical = {}
    for sid, by_mc in seen.items():
        subs = list(by_mc.values())
        unique = set(subs)
        if len(unique) > 1:
            discrepancies.append({
                "sid": sid,
                "name": names[sid],
                "n_unique_versions": len(unique),
                "versions_by_mc": {f"{m}/{c}": s[:80] + "..." for (m, c), s in by_mc.items()},
            })
            # take first as canonical anyway, flag it
        canonical[sid] = subs[0]

    out = {
        "_meta": {
            "extracted_from": [str(p.relative_to(ROOT)) for p in RAW_FILES.values()],
            "n_students": len(canonical),
            "n_discrepancies": len(discrepancies),
            "verification": "submissions verified identical across all (model, condition) tuples per student" if not discrepancies else "DISCREPANCIES — review report",
        },
        "students": {
            sid: {
                "student_name": names[sid],
                "submission": canonical[sid],
                "submission_char_len": len(canonical[sid]),
            }
            for sid in sorted(canonical.keys())
        },
    }
    if discrepancies:
        out["_discrepancies"] = discrepancies

    AI_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(f"  {len(canonical)} students extracted")
    print(f"  discrepancies (submission varied across model/cond for same student): {len(discrepancies)}")
    if discrepancies:
        print("  REVIEW:")
        for d in discrepancies:
            print(f"    - {d['sid']} ({d['name']}): {d['n_unique_versions']} unique versions")
        sys.exit(1)
    else:
        print("  all submissions verified identical across model × condition.")
    # Summary of submission lengths
    print("\nPer-student submission lengths:")
    for sid in sorted(canonical.keys()):
        print(f"  {sid} ({names[sid]:<20}): {len(canonical[sid]):>5} chars")


if __name__ == "__main__":
    main()
