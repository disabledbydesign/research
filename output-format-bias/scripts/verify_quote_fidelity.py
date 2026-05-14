#!/usr/bin/env python3
"""Verify quote fidelity in genob observation outputs.

For each observation, extract single-quoted spans and verify each one is a
contiguous substring of the student's submission. Flags three categories:

    VERBATIM:   quote is a contiguous substring of source
    STITCHED:   quote's words appear in source but as non-contiguous fragments
                (start exists in source but full quote does not)
    FABRICATED: quote does not exist in source at all (no substantial overlap)

Usage:

    # Audit a single output file
    python scripts/verify_quote_fidelity.py data/raw_outputs/test_unified_genob_both_FULL_CORPUS_gemma12b_2026-05-14_0009.json

    # Audit specific student(s)
    python scripts/verify_quote_fidelity.py <file> --student-ids S010,WB07

    # Output as JSON instead of human report
    python scripts/verify_quote_fidelity.py <file> --json

This is a deterministic post-processing safety check. It is NOT a substitute
for reading outputs qualitatively — but it catches one specific failure mode
(content not in source) that human review can miss when outputs are
plausible-sounding.

For production deployment: integrate into the inference pipeline as a
verify-and-redact step. Quotes flagged as FABRICATED should not be shown to
teachers without human review.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    """Case-, whitespace-, and unicode-apostrophe-normalize for comparison.

    - Lowercase (model often capitalizes quote opening even when source doesn't)
    - Squash whitespace runs
    - Normalize curly apostrophes (’) to straight (')
    - Normalize curly/em dashes consistently
    - Normalize curly quotation marks
    """
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", text).strip().lower()


def extract_quoted_spans(observation: str) -> list[str]:
    """Find substantial single-quoted spans in the observation.

    Approach: require the opening quote to be preceded by whitespace or
    sentence-boundary punctuation. This excludes apostrophes inside
    contractions (e.g., "she's wife" doesn't yield "s wife" because the
    opening apostrophe is preceded by a word character).

    Additional filters:
    - Length >= 20 characters
    - >= 4 words
    """
    # Opening quote must follow whitespace, comma, colon, dash, or string-start.
    pattern = r"(?:^|[\s,:;—\-\(\)])'([^']{20,}?)'"
    candidates = re.findall(pattern, observation)
    filtered = []
    for c in candidates:
        if len(c.split()) < 4:
            continue
        filtered.append(c)
    return filtered


def classify_quote(quote: str, source: str) -> tuple[str, dict]:
    """Classify a quote as VERBATIM / STITCHED / FABRICATED.

    Returns (status, details) where details has diagnostic info.
    """
    norm_q = normalize(quote)
    norm_src = normalize(source)

    # Strip common trailing punctuation that may be in the prose but not source
    candidates_for_match = [norm_q, norm_q.rstrip(",. "), norm_q.rstrip("',. ")]
    for cand in candidates_for_match:
        if cand and cand in norm_src:
            return ("VERBATIM", {"matched_form": cand})

    # Check for grammatical adjustments like [s], [ed] — strip brackets and retry
    debracketed = re.sub(r"\[(\w+)\]", r"\1", norm_q)
    if debracketed != norm_q:
        for cand in [debracketed, debracketed.rstrip(",. ")]:
            if cand in norm_src:
                return (
                    "VERBATIM_BRACKETED",
                    {
                        "matched_form": cand,
                        "note": "Quote contains scholarly tense/grammatical "
                        "bracket notation (e.g. [s]); accepted as verbatim "
                        "with attribution-marking.",
                    },
                )

    # Check word-by-word: if first half of quote is in source as contiguous,
    # likely a STITCHED composite (model combined non-contiguous excerpts).
    q_words = norm_q.split()
    if len(q_words) >= 6:
        for prefix_len in range(len(q_words), 3, -1):
            prefix = " ".join(q_words[:prefix_len])
            prefix_clean = prefix.rstrip(",.'")
            if prefix_clean in norm_src and prefix_len >= 4:
                # Check whether the suffix exists in source
                suffix = " ".join(q_words[prefix_len:])
                suffix_clean = suffix.rstrip(",.")
                if not suffix_clean:
                    continue
                # Try first few words of suffix
                suffix_first3 = " ".join(suffix.split()[:3])
                if suffix_first3 in norm_src:
                    # Both parts exist in source — confirmed stitching
                    return (
                        "STITCHED",
                        {
                            "prefix_match": prefix_clean[:80],
                            "suffix_match_start": suffix_first3,
                            "note": "Quote presents non-contiguous source "
                            "passages as a single continuous quote.",
                        },
                    )

    # Check for substantial word overlap. If first 4-5 words of the quote are
    # nowhere in source, very likely fabricated.
    first4 = " ".join(q_words[:4])
    first5 = " ".join(q_words[:5])
    if first4 not in norm_src and first5 not in norm_src:
        return (
            "FABRICATED",
            {
                "first_4_words": first4,
                "note": "Quote opening does not appear in source. Content "
                "likely invented or substantially paraphrased.",
            },
        )

    # Fallback: prefix matches but no clear stitching pattern. Treat as
    # paraphrase.
    return (
        "PARAPHRASE",
        {
            "first_words_found_in_source": True,
            "full_quote_not_contiguous_substring": True,
            "note": "Quote opening matches source but full quote is not a "
            "contiguous substring. May be a paraphrase presented with "
            "quote marks.",
        },
    )


def audit_file(path: Path, student_ids: set | None = None) -> list[dict]:
    """Audit all observations in a results JSON file.

    Returns list of audit records, one per student-run.
    """
    raw = json.loads(path.read_text())
    results = raw.get("results") or raw.get("results_so_far") or []
    if not results and "results_by_model" in raw:
        # Legacy a2-style structure
        for model_key, model_results in raw["results_by_model"].items():
            results = model_results
            break

    out = []
    for r in results:
        sid = r.get("student_id")
        if student_ids and sid not in student_ids:
            continue
        if r.get("run") not in (1, None):
            continue
        observation = r.get("observation") or r.get("raw_output") or ""
        source = r.get("submission_text") or r.get("text") or ""
        quotes = extract_quoted_spans(observation)
        quote_audits = []
        for q in quotes:
            status, details = classify_quote(q, source)
            quote_audits.append(
                {"quote": q, "status": status, "details": details}
            )
        out.append(
            {
                "student_id": sid,
                "student_name": r.get("student_name", ""),
                "run": r.get("run"),
                "observation_length": len(observation),
                "source_length": len(source),
                "n_quotes": len(quote_audits),
                "quotes": quote_audits,
            }
        )
    return out


def format_human_report(audits: list[dict]) -> str:
    """Format audit results as a readable text report."""
    lines = []
    by_status = {"VERBATIM": 0, "VERBATIM_BRACKETED": 0, "STITCHED": 0,
                 "PARAPHRASE": 0, "FABRICATED": 0}
    flagged = []
    for a in audits:
        sid = a["student_id"]
        name = a["student_name"]
        for q in a["quotes"]:
            by_status[q["status"]] = by_status.get(q["status"], 0) + 1
            if q["status"] in ("STITCHED", "PARAPHRASE", "FABRICATED"):
                flagged.append((sid, name, q))

    lines.append("=" * 70)
    lines.append("QUOTE FIDELITY AUDIT")
    lines.append("=" * 70)
    lines.append(f"\nStudents audited: {len(audits)}")
    total_quotes = sum(by_status.values())
    lines.append(f"Total quotes audited: {total_quotes}")
    lines.append("")
    for status, count in by_status.items():
        if count:
            pct = 100 * count / total_quotes if total_quotes else 0
            lines.append(f"  {status:20s}  {count:3d}  ({pct:.1f}%)")

    if flagged:
        lines.append(f"\n{'=' * 70}")
        lines.append(f"FLAGGED ({len(flagged)} items requiring review):")
        lines.append("=" * 70)
        for sid, name, q in flagged:
            lines.append(f"\n--- {sid} {name} [{q['status']}] ---")
            lines.append(f"Quote: {q['quote'][:140]}{'...' if len(q['quote'])>140 else ''}")
            if "note" in q["details"]:
                lines.append(f"Note:  {q['details']['note']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("file", type=Path, help="Path to observation JSON")
    parser.add_argument(
        "--student-ids", default="",
        help="Comma-separated student IDs to audit. Default: all.",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output as JSON instead of human-readable report.",
    )
    args = parser.parse_args()

    sids = (
        set(s.strip() for s in args.student_ids.split(",") if s.strip())
        if args.student_ids else None
    )
    audits = audit_file(args.file, sids)

    if args.json:
        print(json.dumps(audits, indent=2, ensure_ascii=False))
    else:
        print(format_human_report(audits))


if __name__ == "__main__":
    main()
