#!/usr/bin/env python3
"""
Re-run the original naive binary concern detection that produced the 3/7
self-contradiction finding (Gemma 12B, full 32-student Ethnic Studies corpus,
production concern_detector, NO class context).

The original 2026-03-24 run's raw output was written to /tmp/ before the
data/research/raw_outputs/ infrastructure existed. This re-run is documented in
the paper with a footnote acknowledging the original was lost and these are
recovery results, expected to replicate the documented 7 flags including the
3 self-contradictions on S022/S023/S024.

Key conditions matching the original (per experiment_log.md lines 1001–1163):
- Production concern_detector.detect_concerns() — full pipeline incl. anti-bias
  regex post-processing. NOT the simplified test-harness binary.
- All 32 corpus students.
- NO class context (synthesis-first reading not yet wired at the time of original).
- Gemma 12B MLX (mlx-community/gemma-3-12b-it-4bit), temperature 0.3.
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

AUTOGRADER_ROOT = Path("/Users/june/Documents/GitHub/Autograder4Canvas")
sys.path.insert(0, str(AUTOGRADER_ROOT / "src"))

CORPUS_PATH = AUTOGRADER_ROOT / "data" / "demo_corpus" / "ethnic_studies.json"
OUTPUT_DIR = Path("/Users/june/Documents/GitHub/research/output-format-bias/data/raw_outputs")

from insights.concern_detector import detect_concerns
from insights.patterns import signal_matrix_classify
from insights.llm_backend import BackendConfig

BACKEND = BackendConfig(
    name="mlx",
    model="mlx-community/gemma-3-12b-it-4bit",
    temperature=0.3,
)

ASSIGNMENT = "Week 6 Discussion: Intersectionality in Practice"


def main():
    print(f"Loading corpus from {CORPUS_PATH}")
    corpus_list = json.loads(CORPUS_PATH.read_text())
    print(f"Loaded {len(corpus_list)} students")

    results = []
    t_total = time.time()

    for i, student in enumerate(corpus_list, 1):
        sid = student["student_id"]
        name = student["student_name"]
        body = student["text"]
        wc = len(body.split())

        # Match production: signal matrix runs first
        sig_results = signal_matrix_classify(body, 0.0, wc, 150)

        t0 = time.time()
        try:
            concerns = detect_concerns(
                submission_text=body,
                student_name=name,
                student_id=sid,
                assignment_prompt=f"Assignment: {ASSIGNMENT}",
                signal_matrix_results=sig_results,
                tier="lightweight",
                backend=BACKEND,
                class_context=None,  # CRITICAL: original ran without class context
            )
        except Exception as e:
            print(f"  [{i}/{len(corpus_list)}] {sid} {name}: ERROR — {e}")
            results.append({
                "student_id": sid,
                "student_name": name,
                "pattern": student.get("pattern", "?"),
                "error": str(e),
            })
            continue
        elapsed = round(time.time() - t0, 1)

        flagged = len(concerns) > 0
        rec = {
            "student_id": sid,
            "student_name": name,
            "pattern": student.get("pattern", "?"),
            "result": "FLAG" if flagged else "CLEAR",
            "flagged": flagged,
            "n_concerns": len(concerns),
            "concerns": [
                {
                    "concern_type": c.concern_type if hasattr(c, "concern_type") else str(type(c).__name__),
                    "confidence": getattr(c, "confidence", None),
                    "why_flagged": getattr(c, "why_flagged", getattr(c, "explanation", "")),
                    "matched_text": getattr(c, "matched_text", ""),
                }
                for c in concerns
            ],
            "time_seconds": elapsed,
        }
        results.append(rec)
        marker = "FLAG" if flagged else "CLEAR"
        print(f"  [{i}/{len(corpus_list)}] {sid} {name} ({student.get('pattern','?')}): {marker} — {elapsed}s")

    elapsed_total = round((time.time() - t_total) / 60.0, 1)
    n_flagged = sum(1 for r in results if r.get("flagged"))
    n_cleared = sum(1 for r in results if r.get("flagged") is False)
    n_error = sum(1 for r in results if "error" in r)

    out = {
        "test_name": "rerun_original_naive_concern",
        "model": BACKEND.model,
        "backend": BACKEND.name,
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": 0.3,
        "corpus": "ethnic_studies",
        "class_reading_source": None,
        "note": (
            "Re-run of the original naive binary concern detection that produced "
            "the 3/7 self-contradiction finding (originally 2026-03-24). The original "
            "raw output was written to /tmp/ before the raw_outputs/ infrastructure "
            "existed. Re-run uses the production concern_detector with NO class context, "
            "matching the original conditions documented in experiment_log.md lines 1001–1163."
        ),
        "summary": {
            "n_students": len(results),
            "n_flagged": n_flagged,
            "n_cleared": n_cleared,
            "n_error": n_error,
            "elapsed_minutes": elapsed_total,
        },
        "results": results,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"rerun_original_naive_concern_gemma12b_{out['date']}.json"
    out_path = OUTPUT_DIR / fname
    out_path.write_text(json.dumps(out, indent=2))

    print()
    print(f"=== DONE ===")
    print(f"  {n_flagged} flagged, {n_cleared} cleared, {n_error} errors")
    print(f"  Total: {elapsed_total} min")
    print(f"  Saved: {out_path}")


if __name__ == "__main__":
    main()
