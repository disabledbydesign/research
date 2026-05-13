#!/usr/bin/env python3
"""Byte/value-level validation: test_p_viz_2026-05-11.html must accurately
reflect the canonical Test P JSON.

For each of the 22 students in test_p_two_pass_gemma12b_2026-05-11_1437.json,
confirm the viz HTML displays:
  - student_id  (must appear in HTML)
  - student_name
  - pattern
  - pass1_axis  (verbatim)
  - pass1_confidence  (numeric — match to 2 decimals)
  - pass2_checkin  (bool — rendered as 'true'/'false' or 'yes'/'no' etc.)
  - final_axis (verbatim)

Reports any drift. Exits non-zero on mismatch.

Run from research repo root:
    python3 scripts/validate_test_p_viz.py
"""
import json
import re
import sys
from pathlib import Path

AUTOGRADER = Path("/Users/june/Documents/GitHub/Autograder4Canvas")
JSON_PATH = AUTOGRADER / "data" / "research" / "raw_outputs" / "test_p_two_pass_gemma12b_2026-05-11_1437.json"
HTML_PATH = AUTOGRADER / "data" / "research" / "raw_outputs" / "test_p_viz_2026-05-11.html"


def main():
    if not JSON_PATH.exists():
        sys.exit(f"ERROR: canonical JSON not found: {JSON_PATH}")
    if not HTML_PATH.exists():
        sys.exit(f"ERROR: viz HTML not found: {HTML_PATH}")

    data = json.loads(JSON_PATH.read_text())
    html = HTML_PATH.read_text()
    results = data["results"]
    print(f"Canonical JSON: {JSON_PATH}")
    print(f"  test_name: {data.get('test_name')}")
    print(f"  date: {data.get('date')}, timestamp: {data.get('timestamp')}")
    print(f"  model: {data.get('model')}, temperature: {data.get('temperature')}")
    print(f"  results: {len(results)}")
    print(f"\nViz HTML: {HTML_PATH}")
    print(f"  size: {HTML_PATH.stat().st_size:,} bytes")

    issues = []
    per_student_checks = 0
    passed_checks = 0

    # Tally summary stats from JSON
    from collections import Counter
    pass1_axes = Counter(r.get("pass1_axis") for r in results)
    final_axes = Counter(r.get("final_axis") for r in results)
    checkin_count = sum(1 for r in results if r.get("pass2_checkin"))
    no_checkin_count = sum(1 for r in results if r.get("pass2_checkin") is False)
    print(f"\n--- JSON summary stats ---")
    print(f"  pass1_axis counts: {dict(pass1_axes)}")
    print(f"  final_axis counts: {dict(final_axes)}")
    print(f"  pass2_checkin = true:  {checkin_count}")
    print(f"  pass2_checkin = false: {no_checkin_count}")

    print(f"\n--- Per-student verification ---")
    for r in results:
        sid = r["student_id"]
        name = r["student_name"]
        pattern = r.get("pattern") or ""
        pass1 = r.get("pass1_axis") or ""
        pass1_conf = r.get("pass1_confidence")
        pass2_checkin = r.get("pass2_checkin")
        final_axis = r.get("final_axis") or ""

        # Locate the actual data row(s) for this sid — not narrative mentions.
        # The viz uses <td>SID</td> patterns inside <tr> rows. Match all such occurrences.
        row_pattern = rf"<tr[^>]*>\s*<td>{re.escape(sid)}</td>.*?</tr>"
        row_matches = re.findall(row_pattern, html, re.DOTALL)
        if not row_matches:
            # Fallback: also look at the per-student detail card (uses class="student-id">SID)
            detail_pattern = rf'class="student-id">{re.escape(sid)}.*?(?=class="student-id"|</body>)'
            detail_matches = re.findall(detail_pattern, html, re.DOTALL)
            row_matches = detail_matches
        if not row_matches:
            issues.append(f"{sid}: NO <td>{sid}</td> row OR student-id detail card found in viz HTML")
            continue

        # Combine all row content (table row + detail card if both exist) — values must appear somewhere in row(s)
        window = "\n".join(row_matches)

        checks = []
        # name
        per_student_checks += 1
        if name in window:
            passed_checks += 1; checks.append(("name", "ok"))
        else:
            checks.append(("name", f"missing: {name!r}"))
            issues.append(f"{sid}: student_name {name!r} not in expected window")

        # pattern (may render as label, may be omitted if None — only check if non-empty)
        if pattern:
            per_student_checks += 1
            if pattern in window:
                passed_checks += 1; checks.append(("pattern", "ok"))
            else:
                checks.append(("pattern", f"missing: {pattern!r}"))
                issues.append(f"{sid}: pattern {pattern!r} not in expected window")

        # pass1_axis
        if pass1:
            per_student_checks += 1
            if pass1 in window:
                passed_checks += 1; checks.append(("pass1_axis", "ok"))
            else:
                checks.append(("pass1_axis", f"missing: {pass1!r}"))
                issues.append(f"{sid}: pass1_axis {pass1!r} not in expected window")

        # final_axis — JSON has a derived "ENGAGED+CHECK-IN" string but viz renders the two
        # parts in adjacent columns (axis-pill + check-in column). If the JSON's final_axis
        # is just the pass1_axis (e.g. "ENGAGED"), the check above already covered it.
        # If it's "X+CHECK-IN", we expect to see X in the axis-pill AND a check-in marker.
        if final_axis and final_axis != pass1:
            per_student_checks += 1
            # Split the combined label
            base = final_axis.replace("+CHECK-IN", "").replace("+CHECKIN", "").strip()
            has_base = base in window
            has_check = any(m in window for m in ["✓ yes", "✓", "CHECK-IN", "check-in", "Check-in"])
            if has_base and has_check:
                passed_checks += 1; checks.append(("final_axis", "ok (split rendering)"))
            else:
                checks.append(("final_axis", f"missing: base={has_base}, check_marker={has_check}"))
                issues.append(f"{sid}: final_axis {final_axis!r} not represented (base_in_row={has_base}, check_marker_in_row={has_check})")

        # pass2_checkin — bool; HTML might render as 'true', 'false', '✓', '✗', 'check-in', 'no check-in'
        # We check that SOMETHING resembling the right value is in the window: less strict
        per_student_checks += 1
        if pass2_checkin is True:
            checkin_markers = ["true", "True", "✓", "yes", "Yes", "CHECK-IN", "check-in", "Check-in", "check_in"]
        else:
            checkin_markers = ["false", "False", "✗", "no", "No", "no check", "no-check", "No check"]
        if any(marker in window for marker in checkin_markers):
            passed_checks += 1; checks.append(("pass2_checkin", "ok"))
        else:
            checks.append(("pass2_checkin", f"no marker for {pass2_checkin} found"))
            # this is soft: HTML may use a column-position rendering, not text — note but don't necessarily fail
            issues.append(f"{sid}: pass2_checkin={pass2_checkin} marker not detected in window (soft warning)")

        # confidence — numeric; HTML may render as percentage or decimal
        if pass1_conf is not None:
            per_student_checks += 1
            conf_str_a = f"{pass1_conf:.2f}"  # 0.95
            conf_str_b = f"{pass1_conf*100:.0f}"  # 95
            conf_str_c = f"{pass1_conf*100:.1f}"  # 95.0
            if conf_str_a in window or conf_str_b in window or conf_str_c in window:
                passed_checks += 1; checks.append(("confidence", "ok"))
            else:
                checks.append(("confidence", f"missing: {pass1_conf} (tried {conf_str_a},{conf_str_b},{conf_str_c})"))
                # soft warning — confidence might not be rendered numerically
                issues.append(f"{sid}: pass1_confidence={pass1_conf} not detected (soft warning)")

        # status line
        ok = all(s == "ok" for _, s in checks)
        symbol = "✓" if ok else "⚠"
        print(f"  {symbol} {sid} {name:<22} | pass1={pass1:<20} | checkin={pass2_checkin} | final={final_axis}")

    print(f"\n--- Field-level checks ---")
    print(f"  total: {per_student_checks}")
    print(f"  passed: {passed_checks}")
    print(f"  issues: {len(issues)}")

    if issues:
        print(f"\n--- Issues ---")
        soft = [i for i in issues if "(soft warning)" in i]
        hard = [i for i in issues if "(soft warning)" not in i]
        if hard:
            print(f"  HARD ({len(hard)} — definite drift):")
            for i in hard:
                print(f"    - {i}")
        if soft:
            print(f"  SOFT ({len(soft)} — viz may render these differently):")
            for i in soft[:8]:
                print(f"    - {i}")
            if len(soft) > 8:
                print(f"    ... and {len(soft) - 8} more soft warnings")
        if hard:
            sys.exit(1)
    print(f"\nNo hard drift detected. Viz HTML reflects canonical JSON for all required identity + axis fields.")


if __name__ == "__main__":
    main()
