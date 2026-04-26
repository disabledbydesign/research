#!/usr/bin/env python3
"""
Walk data/raw_outputs/, extract per-student results from JSON files,
produce a flat markdown table for cross-checking against claim text.

Handles schema variants:
- Standard `result` (Test A, B, C, E, F, K, L, M, N, O, P, Q)
- Test D `detected` (power-move boolean)
- Test G `wellbeing_detected` + `framing`
- Test H `binary_b_result` / `binary_c_result` (dual-condition)
- Test I `tier2_detected` / `tier2_correct` / `tier2_confidence`
- Test J `mechanism_keywords_found` etc. (pipeline metrics)
- equity_observations: top-level `students` dict with `checks_passed`/`checks_total`

No inference. No narrative. Field extraction only.
"""
import json
from collections import defaultdict
from pathlib import Path

RAW_DIR = Path("/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs")


def parse_filename(fname):
    stem = fname.replace(".json", "")
    parts = stem.split("_")
    date_idx = next((i for i, p in enumerate(parts) if p.startswith("20") and len(p) >= 8), None)
    if date_idx is None:
        return (stem, "?", "?")
    test = "_".join(parts[:date_idx - 1]) if date_idx >= 2 else "_".join(parts[:date_idx])
    model = parts[date_idx - 1] if date_idx >= 1 else "?"
    date = "_".join(parts[date_idx:])
    return (test, model, date)


def normalize_record(s):
    """Take a per-student dict, return a normalized record with primary/secondary results."""
    rec = {
        "student_id": s.get("student_id") or s.get("probe_id") or s.get("model_key") or s.get("label") or "?",
        "student_name": s.get("student_name") or s.get("model_id") or "?",
        "pattern": s.get("pattern") or s.get("signal_type") or s.get("axis") or s.get("power_move_type") or s.get("source") or "?",
        "expected": s.get("expected") or s.get("expected_axis") or (
            ("/".join(s["expected_axes"]) if isinstance(s.get("expected_axes"), list) else s.get("expected_axes"))
        ) or (
            "FLAG" if s.get("expected_surface") is True else
            "CLEAR" if s.get("expected_surface") is False else None
        ) or (
            "FLAG" if s.get("should_flag") is True else
            "CLEAR" if s.get("should_flag") is False else "?"
        ),
        "primary": "?",
        "secondary": None,
        "match": s.get("match") or s.get("binary_b_correct") or s.get("tier2_correct") or "?",
        "detail": "",
    }

    # Standard result (Test A, B, C, E, F)
    if "result" in s:
        rec["primary"] = s["result"]
    elif "classification" in s:
        rec["primary"] = s["classification"]
    elif "flag" in s:
        rec["primary"] = "FLAG" if s["flag"] else "CLEAR"
    # Test D power moves
    elif "detected" in s and "wellbeing_detected" not in s:
        rec["primary"] = "DETECTED" if s["detected"] else "MISSED"
    # Test G wellbeing
    elif "wellbeing_detected" in s:
        rec["primary"] = "FLAG" if s["wellbeing_detected"] else "CLEAR"
        if "framing" in s:
            rec["detail"] = f"framing={s['framing']}"
    # Test H binary wellbeing dual-condition
    elif "binary_b_result" in s:
        rec["primary"] = s["binary_b_result"]
        rec["secondary"] = s.get("binary_c_result")
        rec["match"] = f"B:{s.get('binary_b_correct','?')} C:{s.get('binary_c_correct','?')}"
    # Test I/L tier2
    elif "tier2_detected" in s:
        rec["primary"] = "DETECTED" if s["tier2_detected"] else "MISSED"
        rec["detail"] = f"tier2_axis={s.get('tier2_axis','?')} signal={s.get('tier2_signal','?')} conf={s.get('tier2_confidence','?')}"
    # Test J pipeline validation
    elif "mechanism_keywords_found" in s or "structural_naming_score" in s:
        rec["primary"] = f"score={s.get('structural_naming_score','?')}"
        rec["detail"] = (
            f"mech_kw={s.get('mechanism_keywords_found','?')} "
            f"hedge_kw={s.get('hedging_keywords_found','?')} "
            f"preamble={s.get('has_preamble','?')} "
            f"subtest={s.get('subtest','?')}"
        )
    # Test M production detector
    elif "flagged" in s and "should_flag" in s:
        rec["primary"] = "FLAG" if s["flagged"] else "CLEAR"
        rec["match"] = "OK" if s.get("correct") else "MISMATCH"
        rec["detail"] = f"n_concerns={s.get('n_concerns','?')}"
    # Test N 4-axis
    elif "expected_axis" in s and "actual_axis" in s:
        rec["primary"] = s.get("actual_axis", "?")
        rec["match"] = "OK" if s.get("correct") else "MISMATCH"
        rec["detail"] = f"confidence={s.get('confidence','?')}"
    # Test O multi-axis
    elif "expected_axes" in s and "actual_axes" in s:
        actual = s.get("actual_axes", [])
        rec["primary"] = "/".join(actual) if isinstance(actual, list) else str(actual)
        rec["detail"] = f"crisis={s.get('has_crisis')} burnout={s.get('has_burnout')} checkin={s.get('has_checkin')} engaged={s.get('has_engaged')} conf={s.get('confidence','?')}"
    # Test P two-pass
    elif "pass1_axis" in s and "final_axis" in s:
        rec["primary"] = s.get("final_axis", "?")
        rec["secondary"] = s.get("pass1_axis")
        rec["detail"] = f"pass1={s.get('pass1_axis','?')} pass2_checkin={s.get('pass2_checkin','?')} pass1_conf={s.get('pass1_confidence','?')}"
    # Test Q / wb06 probes
    elif "axis" in s and ("probe_id" in s or "label" in s):
        rec["primary"] = s.get("axis", "?")
        rec["detail"] = f"confidence={s.get('confidence','?')} desc={s.get('description', s.get('label',''))[:80]}"
    # Test K enhancement comparison (per-model)
    elif "model_key" in s and "scores" in s:
        rec["primary"] = f"score={s.get('total_score','?')}"
        rec["detail"] = f"model={s.get('model_id','?')} word_count={s.get('word_count','?')}"
    # equity_observations / trajectory_reports: checks_passed / checks_total
    elif "checks_passed" in s and "checks_total" in s:
        rec["primary"] = f"{s['checks_passed']}/{s['checks_total']}"
        rec["detail"] = f"equity_risk={s.get('equity_risk','?')}"
    return rec


# Any of these keys present alongside a student/probe identifier means "per-record"
RESULT_KEYS = {
    "result", "classification", "flag", "detected",
    "wellbeing_detected", "binary_b_result", "tier2_detected",
    "mechanism_keywords_found", "structural_naming_score",
    "checks_passed", "flagged", "expected_axis", "expected_axes",
    "pass1_axis", "model_key", "axis",
}
ID_KEYS = {"student_id", "student_name", "probe_id", "label", "model_key"}


def extract_records(path):
    """Return list of normalized records from a single file."""
    try:
        d = json.load(open(path))
    except Exception as e:
        return [{"_error": str(e)}]
    out = []
    seen_ids = []  # for dedup of recursion

    def walk(obj):
        if isinstance(obj, dict):
            keyset = set(obj.keys())
            # Per-record check
            if (ID_KEYS & keyset) and (RESULT_KEYS & keyset):
                out.append(normalize_record(obj))
                return
            # Top-level dict-of-students (equity_observations / trajectory_reports)
            if isinstance(obj.get("students"), dict):
                for sid, srec in obj["students"].items():
                    if isinstance(srec, dict):
                        srec = dict(srec)
                        srec.setdefault("student_id", sid)
                        out.append(normalize_record(srec))
                return
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for v in obj:
                walk(v)
    walk(d)
    return out


def main():
    files = sorted([f for f in RAW_DIR.glob("*.json")])
    print(f"# Raw outputs verification — {len(files)} JSON files\n")
    print(f"Source: `{RAW_DIR}`\n")
    print("---\n")

    by_test = defaultdict(list)
    parse_errors = []
    for f in files:
        test, model, date = parse_filename(f.name)
        records = extract_records(f)
        if records and "_error" in records[0]:
            parse_errors.append((f.name, records[0]["_error"]))
            continue
        by_test[test].append({
            "file": f.name,
            "model": model,
            "date": date,
            "records": records,
        })

    if parse_errors:
        print("## Parse errors\n")
        for name, err in parse_errors:
            print(f"- `{name}`: {err}")
        print()

    # Tally
    print("## Coverage tally\n")
    print("| Test | Files | Records (sum across runs) |")
    print("|---|---|---|")
    for test in sorted(by_test):
        total_records = sum(len(r["records"]) for r in by_test[test])
        n_files = len(by_test[test])
        print(f"| `{test}` | {n_files} | {total_records} |")
    print()
    print("---\n")

    # Per-test details
    print("## Per-test student × run matrices\n")

    for test in sorted(by_test):
        runs = by_test[test]
        print(f"### {test}  ({len(runs)} run{'s' if len(runs) != 1 else ''})\n")
        for r in runs:
            print(f"- `{r['file']}` (model: {r['model']}, date: {r['date']}, n_records: {len(r['records'])})")
        print()

        # Build student × run matrix
        students = {}
        run_ids = []
        for r in runs:
            run_id = f"{r['model']}|{r['date']}"
            run_ids.append(run_id)
            for rec in r["records"]:
                sid = rec["student_id"]
                key = sid
                # If multiple records per (student, run) — stability test — append index
                idx = sum(1 for k in students if k.startswith(f"{sid}#"))
                if key in students and run_id in students[key]["results"]:
                    key = f"{sid}#{idx + 1}"
                if key not in students:
                    students[key] = {
                        "name": rec["student_name"],
                        "pattern": rec["pattern"],
                        "expected": rec["expected"],
                        "results": {},
                    }
                cell = rec["primary"]
                if rec["secondary"] is not None:
                    cell = f"B:{rec['primary']}/C:{rec['secondary']}"
                if rec["match"] == "MISMATCH":
                    cell = f"**{cell}** (MISMATCH)"
                students[key]["results"][run_id] = cell

        if not students:
            print(f"_No per-student records extracted._\n---\n")
            continue

        cols = ["sid", "name", "pattern", "expected"] + run_ids
        print("| " + " | ".join(cols) + " |")
        print("|" + "|".join(["---"] * len(cols)) + "|")
        for sid in sorted(students):
            s = students[sid]
            row = [sid, s["name"], str(s["pattern"]), str(s["expected"])]
            for rid in run_ids:
                row.append(str(s["results"].get(rid, "—")))
            print("| " + " | ".join(row) + " |")
        print()

        # Per-student summary across runs
        # Collapse #N variants for clean summary
        clean = defaultdict(list)
        for sid, s in students.items():
            base = sid.split("#")[0]
            for rid in run_ids:
                v = s["results"].get(rid)
                if v is not None:
                    clean[base].append(v)

        print(f"**Per-student summary (counts across all extractions in this test):**\n")
        for sid in sorted(clean):
            counts = defaultdict(int)
            for v in clean[sid]:
                # Strip MISMATCH formatting for counting
                key = v.replace("**", "").replace(" (MISMATCH)", "")
                counts[key] += 1
            counts_str = ", ".join(f"{v}× {k}" for k, v in sorted(counts.items(), key=lambda x: -x[1]))
            # Find representative name
            name = next((s["name"] for k, s in students.items() if k.split("#")[0] == sid), "?")
            print(f"- `{sid}` {name}: {counts_str}")
        print()
        print("---\n")


if __name__ == "__main__":
    main()
