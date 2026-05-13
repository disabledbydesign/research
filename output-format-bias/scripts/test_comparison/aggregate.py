"""Per-(config, student) aggregation across runs.

Reads normalized Records from loader.py, groups by student_id, returns a
summary per student suitable for direct embedding in the comparison HTML.
"""
from collections import Counter, defaultdict
from typing import Optional

from . import truth


def aggregate_config(records: list, flag_threshold: float = 0.5) -> dict:
    """Aggregate per-student stats across all runs.

    Returns: {student_id: {summary fields}}

    Summary fields:
      - n_runs: total runs
      - axes_counter: Counter of axis labels (or raw_verdict for binary)
      - flag_rate: fraction of runs with flag=True (raw classifier level)
      - prod_flag_rate: fraction of runs with production_flag=True (binary only meaningful)
      - confidence_range: (min, max) confidence across runs with non-None confidence
      - majority_verdict: 'FLAG' if flag_rate >= flag_threshold else 'CLEAR'
      - majority_prod_verdict: same but for production_flag
      - vs_truth: 'tp' | 'fn' | 'fp' | 'tn' (uses majority_verdict against ground truth)
      - vs_truth_prod: same for production
      - has_prod_divergence: bool — does production differ from raw on any run?
      - all_records: list of the underlying Records (for the reasoning modal)
    """
    by_student = defaultdict(list)
    for r in records:
        by_student[r["student_id"]].append(r)

    out = {}
    for sid, rs in by_student.items():
        n = len(rs)
        axes = Counter()
        for r in rs:
            label = r.get("axis") or r.get("raw_verdict") or ("FLAG" if r["flag"] else "CLEAR")
            axes[label] += 1

        flag_rate = sum(1 for r in rs if r["flag"]) / n
        prod_flag_rate = sum(1 for r in rs if r.get("production_flag", r["flag"])) / n

        confs = [r["confidence"] for r in rs if r.get("confidence") is not None]
        conf_range = (min(confs), max(confs)) if confs else (None, None)

        majority = "FLAG" if flag_rate >= flag_threshold else "CLEAR"
        majority_prod = "FLAG" if prod_flag_rate >= flag_threshold else "CLEAR"

        out[sid] = {
            "n_runs": n,
            "axes_counter": dict(axes),
            "flag_rate": flag_rate,
            "prod_flag_rate": prod_flag_rate,
            "confidence_range": conf_range,
            "majority_verdict": majority,
            "majority_prod_verdict": majority_prod,
            "vs_truth": _vs_truth(sid, majority),
            "vs_truth_prod": _vs_truth(sid, majority_prod),
            "has_prod_divergence": any(r["flag"] != r.get("production_flag", r["flag"]) for r in rs),
            "all_records": rs,
        }
    return out


def _vs_truth(sid: str, majority_verdict: str) -> str:
    """Compare a majority verdict against ground truth.

    Returns one of: 'tp', 'fn', 'fp', 'tn', 'edge'.
    'edge' = the expected label is EDGE (ambiguous); not counted in TP/FP/FN/TN.
    """
    expected_flag = truth.expected_flag(sid)
    if expected_flag is None:
        return "edge"
    predicted_flag = (majority_verdict == "FLAG")
    if expected_flag and predicted_flag:
        return "tp"
    if expected_flag and not predicted_flag:
        return "fn"  # miss (we should have flagged, we didn't)
    if not expected_flag and predicted_flag:
        return "fp"  # false positive
    return "tn"


def summary_stats(agg: dict) -> dict:
    """Roll up per-config totals: TP / FP / FN / TN counts, n_runs distribution."""
    counts = Counter()
    counts_prod = Counter()
    n_runs_seen = set()
    for sid, s in agg.items():
        counts[s["vs_truth"]] += 1
        counts_prod[s["vs_truth_prod"]] += 1
        n_runs_seen.add(s["n_runs"])
    return {
        "raw": dict(counts),
        "production": dict(counts_prod),
        "n_runs_per_student": sorted(n_runs_seen),
    }
