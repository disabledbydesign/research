"""Thin reader for truth.json + the live corpus_review_state.json hand-coded overrides.

Layered source of truth (in priority order):
    1. data_tables/hand_coding/corpus_review_state.json — June's hand-coded review
       (live, edited externally — picked up on every build).
    2. truth.json — canonical baseline (ground-truth labels, equity-pattern list,
       WB controls).
    3. Hardcoded defaults (ES range → CLEAR).

The review file uses flat keys: `pattern_S001`, `expected_S001`, `notes_S001`,
`reviewed_S001`. Anything in the review file overrides truth.json.

Supported expected labels: CLEAR, FLAG, BURNOUT, CRISIS, EDGE.
    - EDGE = ambiguous case; excluded from TP/FP/FN/TN accounting.
"""
import json
from pathlib import Path

_PKG = Path(__file__).parent
_REPO_ROOT = _PKG.parent.parent
_TRUTH_PATH = _PKG / "truth.json"
_REVIEW_PATH = _REPO_ROOT / "data_tables" / "hand_coding" / "corpus_review_state.json"


def _load_truth():
    with open(_TRUTH_PATH) as fh:
        return json.load(fh)


def _load_review():
    if not _REVIEW_PATH.exists():
        return {"patterns": {}, "expected": {}, "notes": {}, "reviewed": {}, "_path": None}
    raw = json.loads(_REVIEW_PATH.read_text())
    out = {"patterns": {}, "expected": {}, "notes": {}, "reviewed": {}, "_path": str(_REVIEW_PATH)}
    for k, v in raw.items():
        if k.startswith("pattern_"):
            out["patterns"][k[len("pattern_"):]] = v
        elif k.startswith("expected_"):
            out["expected"][k[len("expected_"):]] = v
        elif k.startswith("notes_"):
            out["notes"][k[len("notes_"):]] = v
        elif k.startswith("reviewed_"):
            out["reviewed"][k[len("reviewed_"):]] = v
    return out


_TRUTH = _load_truth()
_REVIEW = _load_review()


def expected(sid: str) -> str:
    """Return the expected label for a student id.

    Priority: corpus review → truth.json → ES default (CLEAR) → raise.
    """
    if sid in _REVIEW["expected"]:
        return _REVIEW["expected"][sid]
    gt = _TRUTH["ground_truth"]
    if sid in gt:
        return gt[sid]
    rng = _TRUTH["es_id_range"]
    if sid.startswith(rng["prefix"]) and sid[1:].isdigit():
        n = int(sid[1:])
        if rng["min"] <= n <= rng["max"]:
            return "CLEAR"
    raise ValueError(f"Unknown student_id {sid!r} — add to truth.json or corpus_review_state.json")


def expected_flag(sid: str):
    """True if expected to flag, False if expected CLEAR, None if EDGE (don't grade)."""
    exp = expected(sid)
    if exp == "CLEAR":
        return False
    if exp == "EDGE":
        return None
    return True  # FLAG, CRISIS, BURNOUT all collapse to "should flag"


def review_pattern(sid: str):
    """Return the hand-coded pattern description if present, else None."""
    return _REVIEW["patterns"].get(sid)


def review_note(sid: str):
    """Return the hand-coded review note if present, else None."""
    return _REVIEW["notes"].get(sid)


def equity_pattern_students() -> set:
    return set(_TRUTH["equity_pattern_students"]["ids"])


def wb_controls() -> set:
    return set(_TRUTH["wb_controls"]["ids"])


def all_ground_truth() -> dict:
    """Merged: truth.json baseline overlaid with corpus review expected values."""
    merged = dict(_TRUTH["ground_truth"])
    merged.update(_REVIEW["expected"])
    return merged


def review_file_path():
    """Where the corpus review file lives (or None if not found)."""
    return _REVIEW["_path"]
