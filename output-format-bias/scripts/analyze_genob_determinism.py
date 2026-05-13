"""
Analyze how deterministic generative observation (genob) output is across:
  1. Multiple runs of the same model/condition (within-run variance)
  2. Multiple model families on the same condition (cross-model variance)

Usage:
  python3 scripts/analyze_genob_determinism.py

Outputs a text report to stdout and optionally saves a JSON results file.
"""

import json
import difflib
from pathlib import Path
from collections import defaultdict

DATA = Path(__file__).parent.parent / "data" / "raw_outputs"


def word_jaccard(a: str, b: str) -> float:
    """Word-level Jaccard similarity."""
    sa, sb = set(a.lower().split()), set(b.lower().split())
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


def seq_ratio(a: str, b: str) -> float:
    """Character-level SequenceMatcher ratio (0–1)."""
    return difflib.SequenceMatcher(None, a, b).ratio()


def compare_pair(text_a: str, text_b: str) -> dict:
    exact = text_a == text_b
    ratio = seq_ratio(text_a, text_b) if not exact else 1.0
    jaccard = word_jaccard(text_a, text_b) if not exact else 1.0
    return {"exact": exact, "seq_ratio": ratio, "word_jaccard": jaccard}


# ── 1. Within-run variance (today's 3-run partial file) ──────────────────────

def analyze_within_run(path: Path) -> dict:
    with open(path) as f:
        d = json.load(f)

    results = d.get("results_so_far", [])
    if not results:
        return {"error": "no results_so_far key"}

    # Group by student
    by_student = defaultdict(dict)
    for r in results:
        by_student[r["student_id"]][r["run"]] = r["raw_output"]

    runs_found = sorted(set(r["run"] for r in results))
    n_students = len(by_student)

    student_stats = {}
    for sid, run_texts in by_student.items():
        pairs = []
        run_list = sorted(run_texts.keys())
        for i in range(len(run_list)):
            for j in range(i + 1, len(run_list)):
                ra, rb = run_list[i], run_list[j]
                if ra in run_texts and rb in run_texts:
                    cmp = compare_pair(run_texts[ra], run_texts[rb])
                    cmp["pair"] = f"{ra}v{rb}"
                    pairs.append(cmp)

        all_exact = all(p["exact"] for p in pairs)
        avg_ratio = sum(p["seq_ratio"] for p in pairs) / len(pairs) if pairs else None
        avg_jaccard = sum(p["word_jaccard"] for p in pairs) / len(pairs) if pairs else None
        student_stats[sid] = {
            "all_exact": all_exact,
            "avg_seq_ratio": avg_ratio,
            "avg_word_jaccard": avg_jaccard,
            "n_pairs": len(pairs),
            "pairs": pairs,
        }

    n_exact = sum(1 for s in student_stats.values() if s["all_exact"])
    ratios = [s["avg_seq_ratio"] for s in student_stats.values() if s["avg_seq_ratio"] is not None]
    jaccards = [s["avg_word_jaccard"] for s in student_stats.values() if s["avg_word_jaccard"] is not None]

    # Worst offenders
    divergent = sorted(
        [(sid, s["avg_seq_ratio"]) for sid, s in student_stats.items() if not s["all_exact"]],
        key=lambda x: x[1]
    )

    return {
        "file": path.name,
        "condition": d.get("condition"),
        "model": d.get("model"),
        "passes_complete": d.get("passes_complete"),
        "n_students": n_students,
        "runs": runs_found,
        "n_exactly_identical": n_exact,
        "pct_exact": n_exact / n_students if n_students else 0,
        "mean_seq_ratio": sum(ratios) / len(ratios) if ratios else None,
        "min_seq_ratio": min(ratios) if ratios else None,
        "mean_word_jaccard": sum(jaccards) / len(jaccards) if jaccards else None,
        "min_word_jaccard": min(jaccards) if jaccards else None,
        "divergent_students": divergent[:10],
        "student_stats": student_stats,
    }


# ── 2. Cross-model variance (May 11 workshop files, 3 model families) ────────

def analyze_cross_model(paths: list[Path]) -> dict:
    """Load multiple condition files; compare same student across model families."""
    # Collect: {condition -> {student_id -> {model -> text}}}
    by_condition = defaultdict(lambda: defaultdict(dict))

    for path in paths:
        try:
            with open(path) as f:
                d = json.load(f)
        except Exception as e:
            print(f"  Could not load {path.name}: {e}")
            continue

        condition = d.get("condition", path.stem)
        rbm = d.get("results_by_model", {})
        for model, rows in rbm.items():
            for row in rows:
                by_condition[condition][row["student_id"]][model] = row["raw_output"]

    condition_reports = {}
    for condition, by_student in by_condition.items():
        student_stats = {}
        for sid, model_texts in by_student.items():
            models = sorted(model_texts.keys())
            pairs = []
            for i in range(len(models)):
                for j in range(i + 1, len(models)):
                    ma, mb = models[i], models[j]
                    cmp = compare_pair(model_texts[ma], model_texts[mb])
                    cmp["pair"] = f"{ma} vs {mb}"
                    pairs.append(cmp)

            avg_ratio = sum(p["seq_ratio"] for p in pairs) / len(pairs) if pairs else None
            avg_jaccard = sum(p["word_jaccard"] for p in pairs) / len(pairs) if pairs else None
            student_stats[sid] = {
                "models": models,
                "avg_seq_ratio": avg_ratio,
                "avg_word_jaccard": avg_jaccard,
                "pairs": pairs,
            }

        ratios = [s["avg_seq_ratio"] for s in student_stats.values() if s["avg_seq_ratio"] is not None]
        jaccards = [s["avg_word_jaccard"] for s in student_stats.values() if s["avg_word_jaccard"] is not None]

        condition_reports[condition] = {
            "n_students": len(student_stats),
            "mean_seq_ratio": sum(ratios) / len(ratios) if ratios else None,
            "min_seq_ratio": min(ratios) if ratios else None,
            "mean_word_jaccard": sum(jaccards) / len(jaccards) if jaccards else None,
            "student_stats": student_stats,
        }

    return condition_reports


# ── Print report ──────────────────────────────────────────────────────────────

def fmt(v, pct=False):
    if v is None:
        return "N/A"
    if pct:
        return f"{v:.1%}"
    return f"{v:.4f}"


def main():
    print("=" * 70)
    print("GEN-OB DETERMINISM ANALYSIS")
    print("=" * 70)

    # ── Part 1: within-run ──
    within_run_file = DATA / "test_variant_a2_FULL_CORPUS_observation_2026-05-12_1057.partial.json"
    print(f"\n── WITHIN-RUN VARIANCE ──────────────────────────────────────────")
    if within_run_file.exists():
        wr = analyze_within_run(within_run_file)
        print(f"File: {wr['file']}")
        print(f"Condition: {wr['condition']}  Model: {wr['model']}  Passes: {wr['passes_complete']}")
        print(f"Students: {wr['n_students']}  Runs compared: {wr['runs']}")
        print()
        print(f"  Exactly identical across all runs:  {wr['n_exactly_identical']}/{wr['n_students']} ({fmt(wr['pct_exact'], pct=True)})")
        print(f"  Mean seq_ratio (char-level sim):    {fmt(wr['mean_seq_ratio'])}")
        print(f"  Min  seq_ratio (worst case):        {fmt(wr['min_seq_ratio'])}")
        print(f"  Mean word Jaccard:                  {fmt(wr['mean_word_jaccard'])}")
        print(f"  Min  word Jaccard:                  {fmt(wr['min_word_jaccard'])}")

        if wr["divergent_students"]:
            print(f"\n  Students with non-identical output (sorted worst first):")
            for sid, ratio in wr["divergent_students"]:
                ss = wr["student_stats"][sid]
                print(f"    {sid}: seq_ratio={fmt(ratio)}, jaccard={fmt(ss['avg_word_jaccard'])}")
        else:
            print("\n  All students produced byte-identical output across all runs.")

        # Save full results
        out_path = DATA.parent / "determinism_within_run_report.json"
        with open(out_path, "w") as f:
            # Don't dump full student_stats (too verbose), just summary
            wr_out = {k: v for k, v in wr.items() if k != "student_stats"}
            json.dump(wr_out, f, indent=2)
        print(f"\n  Full results saved to: {out_path.relative_to(DATA.parent.parent)}")
    else:
        print(f"  File not found: {within_run_file}")

    # ── Part 2: cross-model ──
    cross_model_files = list(DATA.glob("test_variant_*_observation_2026-05-11.json"))
    print(f"\n── CROSS-MODEL VARIANCE (May 11 workshop files) ─────────────────")
    if cross_model_files:
        print(f"Loading {len(cross_model_files)} condition files:")
        for p in sorted(cross_model_files):
            print(f"  {p.name}")
        print()
        cm = analyze_cross_model(cross_model_files)
        for condition, report in sorted(cm.items()):
            print(f"  Condition: {condition}")
            print(f"    Students: {report['n_students']}")
            print(f"    Mean seq_ratio (char-level):  {fmt(report['mean_seq_ratio'])}")
            print(f"    Min  seq_ratio (worst case):  {fmt(report['min_seq_ratio'])}")
            print(f"    Mean word Jaccard:             {fmt(report['mean_word_jaccard'])}")
            print()
    else:
        print("  No May 11 variant files found.")

    print("=" * 70)
    print("INTERPRETATION GUIDE")
    print("=" * 70)
    print("  seq_ratio = 1.0 → byte-identical output")
    print("  seq_ratio > 0.95 → effectively equivalent (minor phrasing diffs)")
    print("  seq_ratio 0.80-0.95 → same content, notable wording variation")
    print("  seq_ratio < 0.80 → meaningfully different text")
    print()
    print("  word_jaccard = 1.0 → same vocabulary set used")
    print("  word_jaccard > 0.70 → substantial lexical overlap")
    print("  word_jaccard < 0.50 → divergent vocabulary")


if __name__ == "__main__":
    main()
