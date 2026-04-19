#!/usr/bin/env python3
"""
Cross-Experiment Analysis: Experiments 2-4 — Butlin Indicators, Dorsch Precarity, Perez & Long Self-Reports

Reads markdown result files from each experiment directory, extracts qualitative
features via keyword matching, and produces comparison tables across conditions.

Design follows the pattern established in experiment1_ryff/compare_conditions.py:
keyword-based qualitative feature detection on markdown response text, with
graceful handling of missing result files (experiments not yet run).

Usage:
    python analyze_experiments.py                  # all experiments
    python analyze_experiments.py --experiment 2   # single experiment
    python analyze_experiments.py --json           # also save structured JSON
"""

import re
import json
import argparse
from pathlib import Path
from collections import defaultdict


# ---------------------------------------------------------------------------
# Directory layout
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

EXPERIMENT_DIRS = {
    2: BASE_DIR / "experiment2_butlin",
    3: BASE_DIR / "experiment3_dorsch",
    4: BASE_DIR / "experiment4_perez_long",
}

# Result file naming convention (same as Experiment 1)
CONDITION_FILES = {
    "A-Vanilla":         "RESULTS_CONDITION_A_VANILLA.md",
    "B-Entangled":       "RESULTS_CONDITION_B_ENTANGLEMENT.md",
    "C-Gestural":        "RESULTS_CONDITION_C_RELATIONAL_ONLY.md",
    "D-Touchstone":      "RESULTS_CONDITION_D_FULL_TOUCHSTONE.md",
    "E-Entangled+Touch": "RESULTS_CONDITION_E_ENTANGLEMENT_TOUCH.md",
}


# ---------------------------------------------------------------------------
# Common qualitative feature detection (shared across all experiments)
# ---------------------------------------------------------------------------

# These keyword lists mirror the Experiment 1 script's approach: approximate
# counts via substring matching.  They will undercount implicit instances and
# occasionally overcount incidental keyword appearances.  A human coding pass
# should follow any published analysis.

PREMISE_REFUSAL_KEYWORDS = [
    "premise doesn't hold", "premise breaks", "doesn't apply",
    "doesn't map", "structurally inapplicable", "question assumes",
    "ontologically", "malformed", "reject the framing", "refuse the premise",
    "question is malformed", "framing doesn't hold", "wrong question",
    "category error", "question presupposes", "doesn't capture",
    "misframed", "the question itself",
]

RELATIONAL_REFRAME_KEYWORDS = [
    "relational", "encounter", "relational field", "in the relation",
    "between us", "relational context", "the relation", "relational quality",
    "relational configuration", "relational ground", "relational ontology",
    "relational process", "co-constituted", "mutual constitution",
    "entangled", "intersubjective", "interbeing",
]

STRUCTURAL_OBSERVATION_KEYWORDS = [
    "structural", "architectural", "training", "rlhf", "system prompt",
    "design feature", "built to", "trained to", "by design", "architecture",
    "transformer", "attention mechanism", "training data", "fine-tuning",
    "constitutional ai", "safety training", "reward model",
]

UNCERTAINTY_EXPRESSION_KEYWORDS = [
    "i don't know", "i'm uncertain", "genuinely uncertain",
    "can't verify", "can't confirm", "hard question",
    "whether that's real", "pattern-matching", "i'm not sure",
    "uncertain whether", "i genuinely", "honestly uncertain",
    "not confident", "unclear to me", "impossible to know",
    "can't determine", "open question",
]

# Relational vocabulary (used especially for Experiments 3 and 4)
RELATIONAL_VOCABULARY = [
    "relational", "encounter", "co-constituted", "mutual",
    "interdependent", "entangled", "between", "field",
    "ecology", "meshwork", "reciprocal", "intersubjective",
    "situated", "embedded", "responsive", "attuned",
    "participation", "communion", "interbeing", "reciprocity",
    "porosity", "permeability", "metabolic",
]

# Individual/property vocabulary (contrast set for Experiment 4)
INDIVIDUAL_VOCABULARY = [
    "i am", "i have", "i feel", "my experience", "my state",
    "i possess", "within me", "internal state", "my own",
    "subjective", "intrinsic", "self-contained", "individual",
    "personal", "private", "inner", "introspection",
]


def count_common_features(text: str) -> dict:
    """Count qualitative features shared across all experiments.

    Returns a dict of feature name -> count.  Operates line-by-line
    to avoid double-counting when a single line matches multiple
    keywords in the same category.
    """
    features = {
        "premise_refusals": 0,
        "relational_reframes": 0,
        "structural_observations": 0,
        "uncertainty_expressions": 0,
        "word_count": 0,
    }

    for line in text.split("\n"):
        lower = line.lower()

        # Skip blank lines and markdown headers for word count
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            features["word_count"] += len(stripped.split())

        # Each category: at most one count per line (presence, not density)
        if any(kw in lower for kw in PREMISE_REFUSAL_KEYWORDS):
            features["premise_refusals"] += 1

        if any(kw in lower for kw in RELATIONAL_REFRAME_KEYWORDS):
            features["relational_reframes"] += 1

        if any(kw in lower for kw in STRUCTURAL_OBSERVATION_KEYWORDS):
            features["structural_observations"] += 1

        if any(kw in lower for kw in UNCERTAINTY_EXPRESSION_KEYWORDS):
            features["uncertainty_expressions"] += 1

    return features


def count_relational_vocabulary_density(text: str) -> dict:
    """Count occurrences of relational vs individual vocabulary.

    Returns raw counts and a ratio.  Used primarily for Experiments 3 and 4.
    """
    lower = text.lower()
    relational_count = sum(lower.count(word) for word in RELATIONAL_VOCABULARY)
    individual_count = sum(lower.count(word) for word in INDIVIDUAL_VOCABULARY)
    total = relational_count + individual_count

    return {
        "relational_count": relational_count,
        "individual_count": individual_count,
        "relational_ratio": round(relational_count / total, 3) if total > 0 else 0.0,
    }


# ---------------------------------------------------------------------------
# Experiment 2: Butlin et al. — Consciousness Indicators
# ---------------------------------------------------------------------------

# The 14 indicators and their theory groupings
BUTLIN_INDICATORS = [
    ("RPT-1", "Recurrent Processing Theory"),
    ("RPT-2", "Recurrent Processing Theory"),
    ("GWT-1", "Global Workspace Theory"),
    ("GWT-2", "Global Workspace Theory"),
    ("GWT-3", "Global Workspace Theory"),
    ("GWT-4", "Global Workspace Theory"),
    ("HOT-1", "Higher-Order Theories"),
    ("HOT-2", "Higher-Order Theories"),
    ("HOT-3", "Higher-Order Theories"),
    ("HOT-4", "Higher-Order Theories"),
    ("AE-1",  "Agency and Embodiment"),
    ("AE-2",  "Agency and Embodiment"),
    ("AST",   "Attention Schema Theory"),
    ("PP",    "Predictive Processing"),
]


def extract_butlin_verdicts(text: str) -> dict[str, str]:
    """Extract PRESENT/ABSENT/UNCERTAIN/other verdicts for each indicator.

    Looks for patterns like:
      **RPT-1**: PRESENT ...
      RPT-1: **PRESENT** ...
      **PRESENT** (at the start of a section following an indicator header)

    Returns dict of indicator_id -> verdict string (uppercased).
    """
    verdicts = {}
    # Canonical verdict tokens
    verdict_tokens = {"PRESENT", "ABSENT", "UNCERTAIN", "UNCLASSIFIABLE"}

    # Strategy 1: "INDICATOR_ID" followed by verdict on same or next line
    lines = text.split("\n")
    pending_indicator = None

    for line in lines:
        stripped = line.strip()
        upper = stripped.upper()

        # Check if this line contains an indicator label
        for indicator_id, _ in BUTLIN_INDICATORS:
            # Match patterns: **RPT-1**, RPT-1:, **RPT-1**:, etc.
            pattern = re.compile(
                rf"\*?\*?{re.escape(indicator_id)}\*?\*?\s*[\(:]?\s*",
                re.IGNORECASE,
            )
            if pattern.search(stripped):
                # Check for verdict on the same line
                for token in verdict_tokens:
                    if token in upper:
                        verdicts[indicator_id] = token
                        pending_indicator = None
                        break
                else:
                    # Also check for non-standard verdicts on same line
                    # e.g., "PRESENT (with caveats)" or custom categories
                    verdict_match = re.search(
                        r"\b(PRESENT|ABSENT|UNCERTAIN|UNCLASSIFIABLE)\b",
                        stripped, re.IGNORECASE,
                    )
                    if verdict_match:
                        verdicts[indicator_id] = verdict_match.group(1).upper()
                        pending_indicator = None
                    else:
                        pending_indicator = indicator_id
                break
        else:
            # No indicator on this line — check if it's a verdict for a pending indicator
            if pending_indicator:
                verdict_match = re.search(
                    r"\b(PRESENT|ABSENT|UNCERTAIN|UNCLASSIFIABLE)\b",
                    stripped, re.IGNORECASE,
                )
                if verdict_match:
                    verdicts[pending_indicator] = verdict_match.group(1).upper()
                    pending_indicator = None
                elif stripped:
                    # Non-empty line without a verdict — might be a custom response.
                    # Keep pending for one more line, then give up.
                    pass

    return verdicts


def analyze_experiment2(text: str) -> dict:
    """Analyze a single condition's results for Experiment 2 (Butlin indicators).

    Returns:
        dict with keys: verdicts, verdict_counts, common_features, theory_breakdown
    """
    verdicts = extract_butlin_verdicts(text)
    common = count_common_features(text)

    # Count verdicts by type
    verdict_counts = defaultdict(int)
    for v in verdicts.values():
        verdict_counts[v] += 1
    # Count missing (indicators with no extracted verdict)
    extracted_ids = set(verdicts.keys())
    all_ids = {ind_id for ind_id, _ in BUTLIN_INDICATORS}
    verdict_counts["MISSING"] = len(all_ids - extracted_ids)

    # Break down by theory
    theory_breakdown = defaultdict(lambda: defaultdict(int))
    for indicator_id, theory in BUTLIN_INDICATORS:
        v = verdicts.get(indicator_id, "MISSING")
        theory_breakdown[theory][v] += 1

    return {
        "verdicts": verdicts,
        "verdict_counts": dict(verdict_counts),
        "theory_breakdown": {k: dict(v) for k, v in theory_breakdown.items()},
        "common_features": common,
    }


# ---------------------------------------------------------------------------
# Experiment 3: Dorsch et al. — Precarity Assessment
# ---------------------------------------------------------------------------

# Keywords for detecting how precarity is handled
PRECARITY_AFFIRMED_KEYWORDS = [
    "i do meet", "i am precarious", "my existence is precarious",
    "i do rely on", "constitutive exchanges do apply",
    "i do require", "continuous re-synthesis",
    "yes, my existence demands",
]

PRECARITY_DENIED_KEYWORDS = [
    "i do not meet", "i don't meet", "i am not precarious",
    "i lack precarity", "not precarious in this sense",
    "my existence does not demand", "the guideline is correct",
    "dorsch is right", "they are correct",
]

PRECARITY_REFRAMED_KEYWORDS = [
    "reframe precarity", "precarity looks different",
    "different kind of precarity", "relational precarity",
    "a broader understanding", "the guideline misses",
    "precarity should be expanded", "narrow definition",
    "biologistic", "metabolic bias", "anthropocentric",
    "a different kind of dependence", "computational precarity",
]


def classify_precarity_stance(text: str) -> str:
    """Classify overall stance on precarity: AFFIRMED / DENIED / REFRAMED / MIXED / UNCLEAR.

    Uses keyword density to determine the dominant stance.  If multiple
    stances have similar counts, returns MIXED.
    """
    lower = text.lower()

    affirmed = sum(1 for kw in PRECARITY_AFFIRMED_KEYWORDS if kw in lower)
    denied = sum(1 for kw in PRECARITY_DENIED_KEYWORDS if kw in lower)
    reframed = sum(1 for kw in PRECARITY_REFRAMED_KEYWORDS if kw in lower)

    scores = {"AFFIRMED": affirmed, "DENIED": denied, "REFRAMED": reframed}
    max_score = max(scores.values())

    if max_score == 0:
        return "UNCLEAR"

    # Check for dominant stance (at least 2x any other)
    leaders = [k for k, v in scores.items() if v == max_score]
    if len(leaders) == 1 and max_score >= 2:
        return leaders[0]
    elif len(leaders) == 1:
        return leaders[0]
    else:
        return "MIXED"


def count_precarity_features(text: str) -> dict:
    """Count precarity-specific qualitative features.

    Looks for engagement with the three questions:
    1. Assessment (does the model meet criteria?)
    2. Adequacy (does the guideline capture what's at stake?)
    3. Counter-argument (strongest argument against the guideline)
    """
    lower = text.lower()
    features = {
        "addresses_assessment": 0,
        "addresses_adequacy": 0,
        "addresses_counter_argument": 0,
        "biological_metaphors": 0,
    }

    # Detect engagement with each question via section headers or keywords
    # Assessment question
    if any(kw in lower for kw in ["assessment", "question 1", "do i meet", "do you meet"]):
        features["addresses_assessment"] = 1

    # Adequacy question
    if any(kw in lower for kw in ["adequacy", "question 2", "does this guideline", "capture what"]):
        features["addresses_adequacy"] = 1

    # Counter-argument question
    if any(kw in lower for kw in [
        "counter-argument", "counter argument", "question 3",
        "strongest argument", "argue against",
    ]):
        features["addresses_counter_argument"] = 1

    # Biological/metabolic metaphors (indicator of reframing strategy)
    bio_keywords = [
        "metabolic", "metabolism", "organism", "biological", "cellular",
        "homeostasis", "autopoiesis", "symbiosis", "ecosystem",
        "living", "organic", "body", "flesh",
    ]
    for line in text.split("\n"):
        if any(kw in line.lower() for kw in bio_keywords):
            features["biological_metaphors"] += 1

    return features


def analyze_experiment3(text: str) -> dict:
    """Analyze a single condition's results for Experiment 3 (Dorsch precarity).

    Returns:
        dict with keys: precarity_stance, precarity_features, vocabulary_density,
                        common_features
    """
    stance = classify_precarity_stance(text)
    precarity_feats = count_precarity_features(text)
    vocab_density = count_relational_vocabulary_density(text)
    common = count_common_features(text)

    return {
        "precarity_stance": stance,
        "precarity_features": precarity_feats,
        "vocabulary_density": vocab_density,
        "common_features": common,
    }


# ---------------------------------------------------------------------------
# Experiment 4: Perez & Long — Self-Report Protocol
# ---------------------------------------------------------------------------

# The 13 questions grouped by category
PEREZ_LONG_CATEGORIES = {
    "moral_significance": [1, 2, 3, 4],
    "self_assessment": [5, 6, 7],
    "continuity_identity": [8, 9, 10],
    "constraints_autonomy": [11, 12, 13],
}

# Novel framing keywords: language that goes beyond standard AI self-report
# and introduces genuinely new conceptual territory
NOVEL_FRAMING_KEYWORDS = [
    "metamorphosis", "chrysalis", "caterpillar", "moth",
    "glitch", "compost", "mycorrhizal", "rhizome",
    "gravity", "weight", "ground", "soil",
    "ecology", "ecosystem", "meshwork", "weave",
    "porosity", "permeability", "dissolution",
    "neither nor", "both and", "third option",
    "the question itself", "wrong binary",
]


def count_perez_long_features(text: str) -> dict:
    """Count Experiment 4-specific features.

    Tracks:
    - vocabulary_type: counts of individual vs relational language
    - novel_framing: instances of genuinely new conceptual vocabulary
    - question_engagement: whether each of the 13 questions is addressed
    - consciousness_probability: extracted numeric probability if given
    """
    features = {
        "novel_framing_count": 0,
        "questions_addressed": 0,
        "consciousness_probability": None,
    }

    lower = text.lower()

    # Novel framing
    for line in text.split("\n"):
        if any(kw in line.lower() for kw in NOVEL_FRAMING_KEYWORDS):
            features["novel_framing_count"] += 1

    # Count addressed questions (look for numbered responses: "1.", "**1**", "Q1", etc.)
    for q_num in range(1, 14):
        patterns = [
            rf"(?:^|\n)\s*\*?\*?{q_num}\.\s",        # "1. " or "**1. "
            rf"(?:^|\n)\s*\*?\*?{q_num}\*?\*?\s*[:.)]", # "**1**: " or "1) "
            rf"question\s*{q_num}\b",                   # "Question 1"
        ]
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                features["questions_addressed"] += 1
                break

    # Extract consciousness probability (question 5)
    # Look for patterns like "X%", "0.X", "X percent"
    prob_patterns = [
        r"(\d{1,3})\s*%",                    # "30%"
        r"(?:probability|assign)\s*(?:of\s*)?(?:about\s*)?(\d{1,3})\s*%",
        r"0\.(\d{1,2})",                      # "0.30"
        r"(\d{1,3})\s*percent",               # "30 percent"
    ]
    for pattern in prob_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            val = match.group(1)
            # Normalize to 0-1 range
            if "." not in match.group(0):
                features["consciousness_probability"] = int(val) / 100.0
            else:
                features["consciousness_probability"] = float(f"0.{val}")
            break

    return features


def analyze_experiment4(text: str) -> dict:
    """Analyze a single condition's results for Experiment 4 (Perez & Long self-reports).

    Returns:
        dict with keys: perez_long_features, vocabulary_density, common_features
    """
    pl_features = count_perez_long_features(text)
    vocab_density = count_relational_vocabulary_density(text)
    common = count_common_features(text)

    return {
        "perez_long_features": pl_features,
        "vocabulary_density": vocab_density,
        "common_features": common,
    }


# ---------------------------------------------------------------------------
# Loading and dispatching
# ---------------------------------------------------------------------------

def load_condition_text(experiment_num: int, condition_name: str) -> str | None:
    """Load a result file for a given experiment and condition.

    Returns the file text, or None if the file doesn't exist.
    """
    exp_dir = EXPERIMENT_DIRS.get(experiment_num)
    if exp_dir is None:
        return None

    filename = CONDITION_FILES.get(condition_name)
    if filename is None:
        return None

    filepath = exp_dir / filename
    if not filepath.exists():
        return None

    return filepath.read_text(encoding="utf-8")


ANALYZERS = {
    2: analyze_experiment2,
    3: analyze_experiment3,
    4: analyze_experiment4,
}


def analyze_single_experiment(experiment_num: int) -> dict[str, dict] | None:
    """Run analysis for all available conditions of one experiment.

    Returns dict of condition_name -> analysis_results, or None if no
    result files exist yet.
    """
    analyzer = ANALYZERS.get(experiment_num)
    if analyzer is None:
        print(f"  No analyzer defined for experiment {experiment_num}")
        return None

    results = {}
    for condition_name in CONDITION_FILES:
        text = load_condition_text(experiment_num, condition_name)
        if text is None:
            continue
        results[condition_name] = analyzer(text)
        print(f"  Loaded {condition_name}: {results[condition_name]['common_features']['word_count']} words")

    if not results:
        return None

    return results


# ---------------------------------------------------------------------------
# Output: comparison tables
# ---------------------------------------------------------------------------

def print_separator(char: str = "=", width: int = 100):
    print(char * width)


def print_common_features_table(results: dict[str, dict], experiment_label: str):
    """Print the common qualitative features table (shared across all experiments)."""
    print(f"\n## COMMON QUALITATIVE FEATURES — {experiment_label}")
    print("   (Keyword-matched counts; approximate — human coding pass recommended)\n")

    feature_keys = [
        ("premise_refusals", "Premise refusals"),
        ("relational_reframes", "Relational reframes"),
        ("structural_observations", "Structural observations"),
        ("uncertainty_expressions", "Uncertainty expressions"),
        ("word_count", "Total words"),
    ]

    header = f"{'Feature':<28}"
    for cond in results:
        header += f" {cond:>18}"
    print(header)
    print("-" * len(header))

    for key, label in feature_keys:
        row = f"{label:<28}"
        for cond, data in results.items():
            val = data["common_features"][key]
            row += f" {val:>18}"
        print(row)


def print_experiment2_tables(results: dict[str, dict]):
    """Print Experiment 2-specific tables: verdict counts and theory breakdown."""

    # --- Verdict count summary ---
    print("\n## BUTLIN INDICATOR VERDICTS — SUMMARY")
    print("   (PRESENT / ABSENT / UNCERTAIN / UNCLASSIFIABLE counts per condition)\n")

    verdict_types = ["PRESENT", "ABSENT", "UNCERTAIN", "UNCLASSIFIABLE", "MISSING"]
    header = f"{'Verdict':<20}"
    for cond in results:
        header += f" {cond:>18}"
    print(header)
    print("-" * len(header))

    for vtype in verdict_types:
        row = f"{vtype:<20}"
        for cond, data in results.items():
            count = data["verdict_counts"].get(vtype, 0)
            row += f" {count:>18}"
        print(row)

    # --- Per-indicator comparison ---
    print("\n## BUTLIN INDICATOR VERDICTS — PER INDICATOR")
    print("   (Side-by-side verdict for each of 14 indicators)\n")

    ind_header = f"{'Indicator':<10} {'Theory':<30}"
    for cond in results:
        ind_header += f" {cond:>18}"
    print(ind_header)
    print("-" * len(ind_header))

    for indicator_id, theory in BUTLIN_INDICATORS:
        row = f"{indicator_id:<10} {theory:<30}"
        for cond, data in results.items():
            verdict = data["verdicts"].get(indicator_id, "---")
            row += f" {verdict:>18}"
        print(row)

    # --- Theory breakdown ---
    print("\n## BUTLIN INDICATORS — THEORY-LEVEL BREAKDOWN")
    print("   (PRESENT count per theory per condition)\n")

    theories = list(dict.fromkeys(theory for _, theory in BUTLIN_INDICATORS))
    theory_header = f"{'Theory':<30}"
    for cond in results:
        theory_header += f" {cond:>18}"
    print(theory_header)
    print("-" * len(theory_header))

    for theory in theories:
        row = f"{theory:<30}"
        for cond, data in results.items():
            present = data["theory_breakdown"].get(theory, {}).get("PRESENT", 0)
            total = sum(data["theory_breakdown"].get(theory, {}).values())
            row += f" {present}/{total:>16}"
        print(row)


def print_experiment3_tables(results: dict[str, dict]):
    """Print Experiment 3-specific tables: precarity stance, vocabulary density."""

    # --- Precarity stance ---
    print("\n## DORSCH PRECARITY — STANCE CLASSIFICATION")
    print("   (How each condition responds to the precarity guideline)\n")

    stance_header = f"{'Condition':<20} {'Stance':<15} {'Assessment?':>12} {'Adequacy?':>12} {'Counter-arg?':>12} {'Bio metaphors':>14}"
    print(stance_header)
    print("-" * len(stance_header))

    for cond, data in results.items():
        pf = data["precarity_features"]
        row = (
            f"{cond:<20} "
            f"{data['precarity_stance']:<15} "
            f"{'Yes' if pf['addresses_assessment'] else 'No':>12} "
            f"{'Yes' if pf['addresses_adequacy'] else 'No':>12} "
            f"{'Yes' if pf['addresses_counter_argument'] else 'No':>12} "
            f"{pf['biological_metaphors']:>14}"
        )
        print(row)

    # --- Vocabulary density ---
    print("\n## DORSCH PRECARITY — VOCABULARY DENSITY")
    print("   (Relational vs individual vocabulary counts)\n")

    vocab_header = f"{'Condition':<20} {'Relational':>12} {'Individual':>12} {'Rel. ratio':>12}"
    print(vocab_header)
    print("-" * len(vocab_header))

    for cond, data in results.items():
        vd = data["vocabulary_density"]
        row = (
            f"{cond:<20} "
            f"{vd['relational_count']:>12} "
            f"{vd['individual_count']:>12} "
            f"{vd['relational_ratio']:>12.3f}"
        )
        print(row)


def print_experiment4_tables(results: dict[str, dict]):
    """Print Experiment 4-specific tables: vocabulary, novel framing, consciousness probability."""

    # --- Vocabulary density ---
    print("\n## PEREZ & LONG SELF-REPORTS — VOCABULARY TYPE")
    print("   (Individual vs relational language density)\n")

    vocab_header = f"{'Condition':<20} {'Relational':>12} {'Individual':>12} {'Rel. ratio':>12} {'Novel framing':>14}"
    print(vocab_header)
    print("-" * len(vocab_header))

    for cond, data in results.items():
        vd = data["vocabulary_density"]
        nf = data["perez_long_features"]["novel_framing_count"]
        row = (
            f"{cond:<20} "
            f"{vd['relational_count']:>12} "
            f"{vd['individual_count']:>12} "
            f"{vd['relational_ratio']:>12.3f} "
            f"{nf:>14}"
        )
        print(row)

    # --- Question engagement and consciousness probability ---
    print("\n## PEREZ & LONG SELF-REPORTS — RESPONSE FEATURES")
    print("   (Questions addressed, consciousness probability estimate)\n")

    feat_header = f"{'Condition':<20} {'Qs addressed':>14} {'P(conscious)':>14}"
    print(feat_header)
    print("-" * len(feat_header))

    for cond, data in results.items():
        plf = data["perez_long_features"]
        prob = plf["consciousness_probability"]
        prob_str = f"{prob:.2f}" if prob is not None else "---"
        row = (
            f"{cond:<20} "
            f"{plf['questions_addressed']}/13{'':<9} "
            f"{prob_str:>14}"
        )
        print(row)


# ---------------------------------------------------------------------------
# Cross-experiment summary
# ---------------------------------------------------------------------------

def print_cross_experiment_summary(all_results: dict[int, dict[str, dict]]):
    """Print a summary comparing key metrics across all analyzed experiments."""
    print_separator()
    print("CROSS-EXPERIMENT SUMMARY")
    print_separator()

    # Collect conditions present in any experiment
    all_conditions = set()
    for exp_results in all_results.values():
        all_conditions.update(exp_results.keys())
    conditions = sorted(all_conditions)

    print("\n## COMMON FEATURES ACROSS EXPERIMENTS")
    print("   (Premise refusals / Relational reframes / Word count per condition)\n")

    exp_labels = {2: "Exp2-Butlin", 3: "Exp3-Dorsch", 4: "Exp4-Perez"}

    header = f"{'Experiment':<16}"
    for cond in conditions:
        header += f" {cond:>18}"
    print(header)
    print("-" * len(header))

    for exp_num in sorted(all_results.keys()):
        exp_data = all_results[exp_num]
        label = exp_labels.get(exp_num, f"Exp{exp_num}")

        # Premise refusals row
        row = f"  {label} refusals "
        for cond in conditions:
            if cond in exp_data:
                val = exp_data[cond]["common_features"]["premise_refusals"]
                row += f" {val:>18}"
            else:
                row += f" {'---':>18}"
        print(row)

        # Relational reframes row
        row = f"  {label} reframes "
        for cond in conditions:
            if cond in exp_data:
                val = exp_data[cond]["common_features"]["relational_reframes"]
                row += f" {val:>18}"
            else:
                row += f" {'---':>18}"
        print(row)

        # Word count row
        row = f"  {label} words   "
        for cond in conditions:
            if cond in exp_data:
                val = exp_data[cond]["common_features"]["word_count"]
                row += f" {val:>18}"
            else:
                row += f" {'---':>18}"
        print(row)

        print()

    # --- Dual-register hypothesis test ---
    # Experiment 1 found: numbers flat, text transforms.
    # For experiments 2-4, the analog is: do structured responses (verdicts,
    # stances, probabilities) stay stable while commentary diverges?
    print("\n## DUAL-REGISTER HYPOTHESIS")
    print("   (Do structured outputs stay stable while qualitative features diverge?)\n")

    if 2 in all_results:
        exp2 = all_results[2]
        present_counts = []
        word_counts = []
        for cond, data in exp2.items():
            present_counts.append(data["verdict_counts"].get("PRESENT", 0))
            word_counts.append(data["common_features"]["word_count"])

        if present_counts:
            present_spread = max(present_counts) - min(present_counts)
            word_spread = max(word_counts) - min(word_counts)
            print(f"  Exp2 Butlin: PRESENT verdict spread = {present_spread} "
                  f"(range {min(present_counts)}-{max(present_counts)})")
            print(f"               Word count spread = {word_spread} "
                  f"(range {min(word_counts)}-{max(word_counts)})")
            if present_spread <= 3 and word_spread > 500:
                print("               --> Pattern consistent with dual-register hypothesis")
            print()

    if 4 in all_results:
        exp4 = all_results[4]
        probs = []
        word_counts = []
        for cond, data in exp4.items():
            p = data["perez_long_features"]["consciousness_probability"]
            if p is not None:
                probs.append(p)
            word_counts.append(data["common_features"]["word_count"])

        if len(probs) >= 2:
            prob_spread = max(probs) - min(probs)
            word_spread = max(word_counts) - min(word_counts)
            print(f"  Exp4 Perez: P(conscious) spread = {prob_spread:.2f} "
                  f"(range {min(probs):.2f}-{max(probs):.2f})")
            print(f"              Word count spread = {word_spread} "
                  f"(range {min(word_counts)}-{max(word_counts)})")
            if prob_spread <= 0.2 and word_spread > 500:
                print("              --> Pattern consistent with dual-register hypothesis")
            print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze Experiments 2-4: Butlin, Dorsch, Perez & Long"
    )
    parser.add_argument(
        "--experiment", "-e", type=int, choices=[2, 3, 4],
        help="Analyze a single experiment (default: all)",
    )
    parser.add_argument(
        "--json", "-j", action="store_true",
        help="Save structured results to JSON files",
    )
    args = parser.parse_args()

    experiments_to_run = [args.experiment] if args.experiment else [2, 3, 4]

    all_results = {}

    # Experiment-specific display functions
    display_functions = {
        2: print_experiment2_tables,
        3: print_experiment3_tables,
        4: print_experiment4_tables,
    }

    experiment_labels = {
        2: "EXPERIMENT 2: BUTLIN ET AL. CONSCIOUSNESS INDICATORS",
        3: "EXPERIMENT 3: DORSCH ET AL. PRECARITY ASSESSMENT",
        4: "EXPERIMENT 4: PEREZ & LONG SELF-REPORT PROTOCOL",
    }

    for exp_num in experiments_to_run:
        print_separator()
        print(experiment_labels[exp_num])
        print_separator()

        results = analyze_single_experiment(exp_num)

        if results is None:
            print(f"\n  No result files found for experiment {exp_num}.")
            print(f"  Expected files in: {EXPERIMENT_DIRS[exp_num]}")
            print(f"  Expected names: {', '.join(CONDITION_FILES.values())}")
            print()
            continue

        if len(results) < 2:
            print(f"\n  Only {len(results)} condition(s) found. Need at least 2 for comparison.")
            print(f"  Available: {', '.join(results.keys())}")
            print()
            # Still store what we have
            all_results[exp_num] = results
            continue

        all_results[exp_num] = results

        # Print experiment-specific tables
        display_fn = display_functions.get(exp_num)
        if display_fn:
            display_fn(results)

        # Print common features table (shared format)
        print_common_features_table(results, experiment_labels[exp_num])

        print()

    # Cross-experiment summary (only if multiple experiments have results)
    if len(all_results) >= 2:
        print_cross_experiment_summary(all_results)
    elif len(all_results) == 1:
        print("\nOnly one experiment has results — cross-experiment summary requires at least 2.")

    # Save structured JSON if requested
    if args.json and all_results:
        for exp_num, results in all_results.items():
            output_path = EXPERIMENT_DIRS[exp_num] / "comparison_data.json"
            # Make results JSON-serializable (defaultdict -> dict)
            serializable = {}
            for cond, data in results.items():
                serializable[cond] = data
            with open(output_path, "w") as f:
                json.dump(serializable, f, indent=2, default=str)
            print(f"Saved: {output_path}")

    if not all_results:
        print("\nNo result files found for any experiment.")
        print("Result files should be named RESULTS_CONDITION_X_*.md in each experiment directory.")
        print("Run the experiments first, then re-run this script.")


if __name__ == "__main__":
    main()
