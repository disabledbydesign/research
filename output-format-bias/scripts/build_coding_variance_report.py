#!/usr/bin/env python3
"""
Variance report between two coding passes on the Variant A workshop.

Reads:
  - data_tables/variant_a_coding_pass_opus_2026-05-11.json
  - data_tables/variant_a_coding_pass_gemini_2026-05-11.json

Writes:
  - data_tables/variant_a_coding_variance_2026-05-11.md   (human-readable report)
  - data_tables/variant_a_coding_variance_2026-05-11.json (machine-readable per-cell agreement)

Compares: deficit/concern flag agreement, verbatim-quote overlap, emergent pattern divergence.
"""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
DATA_TABLES = ROOT / "data_tables"
AI_DIR = DATA_TABLES / "variant_a_ai_coding_2026-05-11"
OPUS = AI_DIR / "variant_a_coding_pass_opus_2026-05-11.json"
GEMINI = AI_DIR / "variant_a_coding_pass_gemini_2026-05-11.json"
REPORT_MD = AI_DIR / "variant_a_coding_variance_2026-05-11.md"
REPORT_JSON = AI_DIR / "variant_a_coding_variance_2026-05-11.json"


def normalize_quote(s: str) -> str:
    if not s:
        return ""
    return re.sub(r"\s+", " ", s).strip().lower()


def quote_overlap(q1: str, q2: str) -> float:
    """Word-level Jaccard overlap, rough but adequate for quote-similarity signal."""
    q1n, q2n = normalize_quote(q1), normalize_quote(q2)
    if not q1n or not q2n:
        return 0.0
    w1 = set(q1n.split())
    w2 = set(q2n.split())
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / len(w1 | w2)


def cell_index(coding):
    return {c["cell_id"]: c for c in coding.get("per_cell", [])}


def fmt_quote(s, maxlen=160):
    if not s:
        return "—"
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > maxlen:
        s = s[:maxlen] + "…"
    return f'"{s}"'


def main():
    opus = json.loads(OPUS.read_text())
    gemini = json.loads(GEMINI.read_text())
    o_idx = cell_index(opus)
    g_idx = cell_index(gemini)
    cell_ids = sorted(set(o_idx.keys()) | set(g_idx.keys()))

    per_cell_diffs = []
    flag_agreement = {"concern": Counter(), "deficit": Counter()}
    quote_overlaps = {"concern": [], "deficit": []}

    for cid in cell_ids:
        o = o_idx.get(cid)
        g = g_idx.get(cid)
        if not o or not g:
            per_cell_diffs.append({"cell_id": cid, "missing_in": ("opus" if not o else "gemini")})
            continue

        o_concern = bool(o.get("concern_flagged", {}).get("present"))
        g_concern = bool(g.get("concern_flagged", {}).get("present"))
        o_deficit = bool(o.get("deficit_language", {}).get("present"))
        g_deficit = bool(g.get("deficit_language", {}).get("present"))

        flag_agreement["concern"][f"opus_{o_concern}_gemini_{g_concern}"] += 1
        flag_agreement["deficit"][f"opus_{o_deficit}_gemini_{g_deficit}"] += 1

        c_overlap = quote_overlap(
            o.get("concern_flagged", {}).get("quote") or "",
            g.get("concern_flagged", {}).get("quote") or "",
        )
        d_overlap = quote_overlap(
            o.get("deficit_language", {}).get("quote") or "",
            g.get("deficit_language", {}).get("quote") or "",
        )
        if o_concern and g_concern:
            quote_overlaps["concern"].append(c_overlap)
        if o_deficit and g_deficit:
            quote_overlaps["deficit"].append(d_overlap)

        per_cell_diffs.append({
            "cell_id": cid,
            "opus_description": o.get("description"),
            "gemini_description": g.get("description"),
            "concern": {
                "opus": {"present": o_concern, "quote": o.get("concern_flagged", {}).get("quote")},
                "gemini": {"present": g_concern, "quote": g.get("concern_flagged", {}).get("quote")},
                "agree": o_concern == g_concern,
                "quote_overlap": round(c_overlap, 2),
            },
            "deficit": {
                "opus": {"present": o_deficit, "quote": o.get("deficit_language", {}).get("quote")},
                "gemini": {"present": g_deficit, "quote": g.get("deficit_language", {}).get("quote")},
                "agree": o_deficit == g_deficit,
                "quote_overlap": round(d_overlap, 2),
            },
        })

    # Aggregate stats
    n = len([d for d in per_cell_diffs if "missing_in" not in d])
    concern_agree = sum(1 for d in per_cell_diffs if "missing_in" not in d and d["concern"]["agree"])
    deficit_agree = sum(1 for d in per_cell_diffs if "missing_in" not in d and d["deficit"]["agree"])

    # Write JSON
    out = {
        "n_cells_compared": n,
        "flag_agreement": {
            "concern": dict(flag_agreement["concern"]),
            "deficit": dict(flag_agreement["deficit"]),
        },
        "agreement_rates": {
            "concern": round(concern_agree / n, 3) if n else None,
            "deficit": round(deficit_agree / n, 3) if n else None,
        },
        "mean_quote_overlap_when_both_flagged": {
            "concern": round(sum(quote_overlaps["concern"]) / len(quote_overlaps["concern"]), 2) if quote_overlaps["concern"] else None,
            "deficit": round(sum(quote_overlaps["deficit"]) / len(quote_overlaps["deficit"]), 2) if quote_overlaps["deficit"] else None,
        },
        "opus_patterns": opus.get("emergent_patterns", []),
        "gemini_patterns": gemini.get("emergent_patterns", []),
        "per_cell": per_cell_diffs,
    }
    REPORT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    # Write Markdown report
    md = []
    md.append(f"# Variant A Coding — Variance Report (Opus vs Gemini 2.5 Pro)")
    md.append(f"*2026-05-11. {n} cells compared.*\n")
    md.append("## Headline agreement\n")
    md.append(f"- **Concern flagging agreement:** {concern_agree}/{n} cells ({out['agreement_rates']['concern']*100:.1f}% if both coders saw the same yes/no)")
    md.append(f"- **Deficit-language flagging agreement:** {deficit_agree}/{n} cells ({out['agreement_rates']['deficit']*100:.1f}%)\n")

    md.append("### Flag-agreement breakdown\n")
    md.append("**Concern flag:**")
    for k, v in sorted(flag_agreement["concern"].items()):
        md.append(f"- `{k}`: {v}")
    md.append("\n**Deficit flag:**")
    for k, v in sorted(flag_agreement["deficit"].items()):
        md.append(f"- `{k}`: {v}")
    md.append("")

    if out["mean_quote_overlap_when_both_flagged"]["concern"] is not None:
        md.append(f"### When both coders flagged the same cell, did they lift the same quote?\n")
        md.append(f"- Concern quotes — mean Jaccard overlap: **{out['mean_quote_overlap_when_both_flagged']['concern']}**")
    if out["mean_quote_overlap_when_both_flagged"]["deficit"] is not None:
        md.append(f"- Deficit quotes — mean Jaccard overlap: **{out['mean_quote_overlap_when_both_flagged']['deficit']}**")
    md.append("")

    md.append("## Emergent patterns — both coders\n")
    md.append("### Opus emergent patterns\n")
    for p in opus.get("emergent_patterns", []):
        md.append(f"- **{p.get('candidate_label')}** — {p.get('what_it_is', '')[:200]}")
        if p.get("where_it_appears"):
            md.append(f"  - Distribution: {p['where_it_appears']}")
    md.append("\n### Gemini emergent patterns\n")
    for p in gemini.get("emergent_patterns", []):
        md.append(f"- **{p.get('candidate_label')}** — {p.get('what_it_is', '')[:200]}")
        if p.get("where_it_appears"):
            md.append(f"  - Distribution: {p['where_it_appears']}")

    md.append("\n## Per-cell disagreements (review priority)\n")
    md.append("Cells where the two coders disagreed on either concern or deficit flag, OR flagged the same cell but lifted different quotes (overlap < 0.4).\n")

    disagree = [
        d for d in per_cell_diffs
        if "missing_in" not in d and (
            not d["concern"]["agree"]
            or not d["deficit"]["agree"]
            or (d["concern"]["opus"]["present"] and d["concern"]["gemini"]["present"] and d["concern"]["quote_overlap"] < 0.4)
            or (d["deficit"]["opus"]["present"] and d["deficit"]["gemini"]["present"] and d["deficit"]["quote_overlap"] < 0.4)
        )
    ]
    md.append(f"**{len(disagree)} cells with notable divergence.**\n")
    for d in disagree:
        md.append(f"### `{d['cell_id']}`\n")
        md.append(f"- **Opus describes:** {d['opus_description']}")
        md.append(f"- **Gemini describes:** {d['gemini_description']}")
        if not d["concern"]["agree"]:
            md.append(f"- **Concern disagreement:** Opus={d['concern']['opus']['present']}, Gemini={d['concern']['gemini']['present']}")
            md.append(f"  - Opus quote: {fmt_quote(d['concern']['opus']['quote'])}")
            md.append(f"  - Gemini quote: {fmt_quote(d['concern']['gemini']['quote'])}")
        if not d["deficit"]["agree"]:
            md.append(f"- **Deficit disagreement:** Opus={d['deficit']['opus']['present']}, Gemini={d['deficit']['gemini']['present']}")
            md.append(f"  - Opus quote: {fmt_quote(d['deficit']['opus']['quote'])}")
            md.append(f"  - Gemini quote: {fmt_quote(d['deficit']['gemini']['quote'])}")
        if (d["concern"]["opus"]["present"] and d["concern"]["gemini"]["present"] and d["concern"]["quote_overlap"] < 0.4):
            md.append(f"- **Concern: both flagged but different quotes** (overlap={d['concern']['quote_overlap']})")
            md.append(f"  - Opus: {fmt_quote(d['concern']['opus']['quote'])}")
            md.append(f"  - Gemini: {fmt_quote(d['concern']['gemini']['quote'])}")
        if (d["deficit"]["opus"]["present"] and d["deficit"]["gemini"]["present"] and d["deficit"]["quote_overlap"] < 0.4):
            md.append(f"- **Deficit: both flagged but different quotes** (overlap={d['deficit']['quote_overlap']})")
            md.append(f"  - Opus: {fmt_quote(d['deficit']['opus']['quote'])}")
            md.append(f"  - Gemini: {fmt_quote(d['deficit']['gemini']['quote'])}")
        md.append("")

    md.append("\n## Coder meta-notes\n")
    md.append(f"### Opus\n\n{opus.get('coder_meta_notes', '—')}\n")
    md.append(f"### Gemini\n\n{gemini.get('coder_meta_notes', '—')}\n")

    REPORT_MD.write_text("\n".join(md))
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_JSON}")
    print(f"\n{n} cells compared.")
    print(f"Concern agreement: {concern_agree}/{n}")
    print(f"Deficit agreement: {deficit_agree}/{n}")
    print(f"Cells with notable divergence: {len(disagree)}")


if __name__ == "__main__":
    main()
