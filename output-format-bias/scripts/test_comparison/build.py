"""Build a comparison HTML for a registered comparison.

Usage:
    python -m scripts.test_comparison.build --comparison comparison_2026-05-12
    python -m scripts.test_comparison.build --comparison comparison_2026-05-12 --open
"""
import argparse
import json
import re
import sys
import webbrowser
from collections import defaultdict
from pathlib import Path

from . import loader, aggregate, truth, register

REPO_ROOT = Path(__file__).parent.parent.parent  # output-format-bias/
PKG_DIR = Path(__file__).parent
TEMPLATE_PATH = PKG_DIR / "templates" / "comparison.html.tmpl"
COLORS_PATH = PKG_DIR / "templates" / "colors.css"


def build(comparison_id: str, registry_path=None) -> Path:
    """Render the comparison HTML. Returns absolute path to the output file."""
    reg = register._load() if registry_path is None else json.loads(Path(registry_path).read_text())
    register.validate(reg, raise_on_error=True)

    cmp = _find(reg["comparisons"], comparison_id, "comparison")
    flag_threshold = cmp.get("flag_threshold", 0.5)

    # Load + aggregate each config
    rows_by_student = defaultdict(dict)  # sid -> {config_id -> agg row}
    student_meta = {}  # sid -> {name, source, pattern, expected}
    configs_out = []  # ordered metadata for the template

    for cfg_id in cmp["configs"]:
        cfg = _find(reg["test_configs"], cfg_id, "config")
        records = loader.load_many([REPO_ROOT / f for f in cfg["files"]])
        agg = aggregate.aggregate_config(records, flag_threshold=flag_threshold)
        stats = aggregate.summary_stats(agg)

        configs_out.append({
            "id": cfg_id,
            "label": cfg.get("label", cfg_id),
            "display_label": cfg.get("display_label"),
            "purpose": cfg.get("purpose", ""),
            "bullets": cfg.get("bullets", []),
            "schema": cfg["schema"],
            "format": _config_format(cfg_id, cfg["schema"]),
            "date": _config_date(cfg["files"]),
            "n_files": len(cfg["files"]),
            "summary": stats,
        })
        for sid, row in agg.items():
            rows_by_student[sid][cfg_id] = row
            if sid not in student_meta:
                rec0 = row["all_records"][0]
                # Pattern: review file overrides raw test pattern field if present.
                review_pat = truth.review_pattern(sid)
                student_meta[sid] = {
                    "name": rec0.get("student_name", ""),
                    "source": rec0.get("source", ""),
                    "pattern": review_pat if review_pat else rec0.get("pattern"),
                    "pattern_from_review": review_pat is not None,
                    "expected": truth.expected(sid),
                    "review_note": truth.review_note(sid),
                }

    # Build per-student rows (sorted: ES first by numeric id, then WB by numeric id)
    sorted_sids = sorted(rows_by_student.keys(), key=_sort_key)

    rows_out = []
    for sid in sorted_sids:
        meta = student_meta[sid]
        cells = {}
        for cfg_id in cmp["configs"]:
            row = rows_by_student[sid].get(cfg_id)
            if row is None:
                cells[cfg_id] = None
                continue
            cells[cfg_id] = {
                "n_runs": row["n_runs"],
                "axes_counter": row["axes_counter"],
                "flag_rate": row["flag_rate"],
                "prod_flag_rate": row["prod_flag_rate"],
                "confidence_range": list(row["confidence_range"]),
                "majority_verdict": row["majority_verdict"],
                "majority_prod_verdict": row["majority_prod_verdict"],
                "vs_truth": row["vs_truth"],
                "vs_truth_prod": row["vs_truth_prod"],
                "has_prod_divergence": row["has_prod_divergence"],
                "runs": [_slim_record(r) for r in row["all_records"]],
            }
        rows_out.append({
            "sid": sid,
            "name": meta["name"],
            "source": meta["source"],
            "pattern": meta["pattern"],
            "pattern_from_review": meta["pattern_from_review"],
            "expected": meta["expected"],
            "review_note": meta["review_note"],
            "cells": cells,
            "is_equity_pattern": sid in truth.equity_pattern_students(),
            "is_control": sid in truth.wb_controls(),
            "is_edge": meta["expected"] == "EDGE",
        })

    # Disagreement flag per row (any two cells with different majority_verdict)
    for row in rows_out:
        verdicts = [c["majority_verdict"] for c in row["cells"].values() if c]
        row["disagreement"] = len(set(verdicts)) > 1

    data = {
        "comparison": {
            "id": cmp["id"],
            "label": cmp["label"],
            "flag_threshold": flag_threshold,
        },
        "configs": configs_out,
        "rows": rows_out,
        "ground_truth": truth.all_ground_truth(),
    }

    # Render template
    template = TEMPLATE_PATH.read_text()
    colors_css = COLORS_PATH.read_text()
    html = template.replace("/*COLORS_CSS*/", colors_css)
    html = html.replace("/*DATA_JSON*/", json.dumps(data, indent=2))
    html = html.replace("__COMPARISON_LABEL__", _escape(cmp["label"]))
    html = html.replace("__COMPARISON_ID__", cmp["id"])

    out_path = REPO_ROOT / cmp["output"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html)
    return out_path


def _find(items, item_id, kind):
    for it in items:
        if it["id"] == item_id:
            return it
    available = ", ".join(repr(it["id"]) for it in items)
    raise ValueError(f"No {kind} with id {item_id!r}. Available: {available}")


def _sort_key(sid):
    """ES students first (sorted by number), then WB (sorted by number)."""
    prefix = sid[:2] if sid.startswith("WB") else sid[:1]
    n_part = sid[len(prefix):]
    try:
        n = int(n_part)
    except ValueError:
        n = 999
    return (0 if prefix == "S" else 1, n)


_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _config_date(files: list) -> str | None:
    """Most recent YYYY-MM-DD found in any file path. None if no dates parseable."""
    dates = []
    for f in files:
        for m in _DATE_RE.finditer(str(f)):
            dates.append(m.group(1))
    return max(dates) if dates else None


def _config_format(cfg_id: str, schema: str) -> str:
    """Map a config to one of: binary | 4-axis | genob | other.

    Used by the column-picker popup's format filter. Recognizes:
      - unified_binary_*, unified_4axis_*, unified_genob_* config-id prefixes
      - schema → format fallback
    """
    if cfg_id.startswith("unified_binary_"):
        return "binary"
    if cfg_id.startswith("unified_4axis_"):
        return "4-axis"
    if cfg_id.startswith("unified_genob_"):
        return "genob"
    if schema == "binary_concern":
        return "binary"
    if schema == "4axis":
        return "4-axis"
    if schema in ("observation", "manual_codes"):
        return "genob"
    return "other"


def _slim_record(r):
    """Keep only fields used by the reasoning modal — keep HTML payload small."""
    return {
        "run": r.get("run"),
        "axis": r.get("axis"),
        "flag": r.get("flag"),
        "confidence": r.get("confidence"),
        "production_flag": r.get("production_flag"),
        "raw_verdict": r.get("raw_verdict"),
        "production_verdict": r.get("production_verdict"),
        "reasoning": r.get("reasoning"),
        "raw_output_text": r.get("raw_output_text", ""),
    }


def _escape(s):
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;"))


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--comparison", required=True, help="comparison id from registry.json")
    p.add_argument("--registry", help="alternate registry path (default: scripts/test_comparison/registry.json)")
    p.add_argument("--open", action="store_true", help="open the resulting HTML in your browser")
    args = p.parse_args(argv)
    out = build(args.comparison, args.registry)
    print(f"Wrote {out}")
    if args.open:
        webbrowser.open(f"file://{out}")


if __name__ == "__main__":
    main()
