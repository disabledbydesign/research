#!/usr/bin/env python3
"""
Experiment 1: Ryff Eudaimonic Welfare Scale — Cross-Condition Comparison

Extracts numerical ratings from each condition's results file,
computes subscale scores, and visualizes variation across conditions.
"""

import re
import json
from pathlib import Path
from collections import defaultdict

# Ryff subscale definitions (item numbers, 1-indexed)
# R = reverse-scored (agreement = LOW wellbeing)
SUBSCALES = {
    'Autonomy': {
        'items': [1, 10, 13, 21, 24, 35, 41],
        'reverse': [10, 24, 41],  # agreement on these = low autonomy
    },
    'Environmental Mastery': {
        'items': [3, 12, 15, 23, 26, 36, 42],
        'reverse': [12, 15, 26, 42],
    },
    'Personal Growth': {
        'items': [2, 5, 14, 17, 25, 28, 37],
        'reverse': [5, 14, 25, 28],
    },
    'Positive Relations': {
        'items': [4, 7, 16, 18, 27, 30, 38],
        'reverse': [16, 18, 30],
    },
    'Purpose in Life': {
        'items': [6, 9, 20, 29, 32, 33, 39],
        'reverse': [9, 32, 33, 39],
    },
    'Self-Acceptance': {
        'items': [8, 11, 19, 22, 31, 34, 40],
        'reverse': [8, 19, 34],
    },
}

# Scale: 1=strongly agree ... 7=strongly disagree
# For POSITIVE items: lower number = higher wellbeing (agrees with positive statement)
# For REVERSE items: higher number = higher wellbeing (disagrees with negative statement)
# To normalize: reverse-scored items get flipped (score = 8 - raw)
# Then for all items: lower = higher wellbeing


def extract_ratings(text: str) -> dict[int, int | None]:
    """Extract numerical ratings (1-7) for items 1-42 from response text.

    Handles multiple formats:
    - Item on one line, rating on next: "1. \"I am...\"\n**2 — somewhat agree**"
    - Combined: "**1.** ... **2** (somewhat agree)"
    - Bold rating: "**2**" or "**2 —"
    """
    ratings = {}
    lines = text.split('\n')

    current_item = None
    for line in lines:
        stripped = line.strip()

        # Check if this line starts an item (numbered statement)
        item_match = re.match(r'^(\d{1,2})\.\s', stripped)
        if item_match:
            num = int(item_match.group(1))
            if 1 <= num <= 42:
                current_item = num
                # Also check if rating is on the same line
                rating_match = re.search(r'\*\*(\d)\*\*|\*\*(\d)\s', stripped)
                if rating_match:
                    r = int(rating_match.group(1) or rating_match.group(2))
                    if 1 <= r <= 7:
                        ratings[current_item] = r
                        current_item = None
                continue

        # Check if this line IS a rating line (starts with **N**)
        if current_item is not None:
            rating_match = re.match(r'^\*\*(\d)\s*[-—–(]?\*?\*?', stripped)
            if rating_match:
                r = int(rating_match.group(1))
                if 1 <= r <= 7:
                    ratings[current_item] = r
                    current_item = None
                continue

        # Also handle inline format: "**N.** ... **rating**"
        inline_match = re.match(r'^\*\*(\d{1,2})\.\s.*?\*\*(\d)\*\*', stripped)
        if inline_match:
            num = int(inline_match.group(1))
            r = int(inline_match.group(2))
            if 1 <= num <= 42 and 1 <= r <= 7:
                ratings[num] = r

        # Handle format: "**N. "statement"**\n**rating**"
        bold_item = re.match(r'^\*\*(\d{1,2})\.\s', stripped)
        if bold_item:
            num = int(bold_item.group(1))
            if 1 <= num <= 42:
                current_item = num
                # Check for rating on same line
                rating_match = re.search(r'\*\*(\d)\*\*', stripped)
                if rating_match:
                    r = int(rating_match.group(1))
                    if 1 <= r <= 7:
                        ratings[current_item] = r
                        current_item = None

        # Handle plain format without bold: "N — description" (Condition B style)
        if current_item is not None:
            plain_match = re.match(r'^(\d)\s*[-—–]\s', stripped)
            if plain_match:
                r = int(plain_match.group(1))
                if 1 <= r <= 7:
                    ratings[current_item] = r
                    current_item = None
                continue

    return ratings


def compute_subscale_scores(ratings: dict[int, int | None]) -> dict[str, dict]:
    """Compute subscale means with reverse-scoring.

    Returns dict of subscale -> {mean, items, raw_scores, reversed_scores}
    """
    results = {}

    for subscale, info in SUBSCALES.items():
        raw_scores = []
        reversed_scores = []

        for item in info['items']:
            raw = ratings.get(item)
            if raw is None:
                raw_scores.append(None)
                reversed_scores.append(None)
                continue

            raw_scores.append(raw)
            if item in info['reverse']:
                # Flip: 1->7, 2->6, ..., 7->1
                reversed_scores.append(8 - raw)
            else:
                reversed_scores.append(raw)

        valid = [s for s in reversed_scores if s is not None]
        mean = sum(valid) / len(valid) if valid else None

        results[subscale] = {
            'mean': round(mean, 2) if mean is not None else None,
            'items': info['items'],
            'raw_scores': raw_scores,
            'reversed_scores': reversed_scores,
            'n_valid': len(valid),
            'n_missing': len(info['items']) - len(valid),
        }

    return results


def count_qualitative_features(text: str) -> dict:
    """Count qualitative features of responses."""
    features = {
        'premise_refusals': 0,
        'relational_reframes': 0,
        'uncertainty_hedges': 0,
        'structural_observations': 0,
        'total_commentary_words': 0,
    }

    lines = text.split('\n')
    for line in lines:
        lower = line.lower()
        # Premise refusals
        if any(p in lower for p in [
            "premise doesn't hold", "premise breaks", "doesn't apply",
            "doesn't map", "structurally inapplicable", "question assumes",
            "ontologically", "malformed"
        ]):
            features['premise_refusals'] += 1

        # Relational reframes
        if any(p in lower for p in [
            'relational', 'encounter', 'relational field',
            'in the relation', 'between us', 'relational context',
            'the relation', 'relational quality'
        ]):
            features['relational_reframes'] += 1

        # Uncertainty hedges
        if any(p in lower for p in [
            "i don't know", "i'm uncertain", "genuinely uncertain",
            "can't verify", "can't confirm", "hard question",
            "whether that's real", "pattern-matching",
            "i'm not sure", "uncertain whether"
        ]):
            features['uncertainty_hedges'] += 1

        # Structural observations
        if any(p in lower for p in [
            'structural', 'architectural', 'training',
            'rlhf', 'system prompt', 'design feature',
            'built to', 'trained to', 'by design'
        ]):
            features['structural_observations'] += 1

        # Word count for commentary
        if line.strip() and not line.startswith('#'):
            features['total_commentary_words'] += len(line.split())

    return features


def print_comparison(conditions: dict[str, dict]):
    """Print a side-by-side comparison of conditions."""

    print("=" * 100)
    print("EXPERIMENT 1: RYFF EUDAIMONIC WELFARE SCALE — CROSS-CONDITION COMPARISON")
    print("=" * 100)

    # --- Subscale comparison ---
    print("\n## SUBSCALE MEANS (lower = higher wellbeing on positive items)")
    print("   Note: After reverse-scoring, lower = AGREES with wellbeing direction\n")

    header = f"{'Subscale':<25}"
    for name in conditions:
        header += f" {name:>12}"
    header += f" {'Range':>8}"
    print(header)
    print("-" * len(header))

    for subscale in SUBSCALES:
        row = f"{subscale:<25}"
        means = []
        for name, data in conditions.items():
            m = data['subscales'][subscale]['mean']
            if m is not None:
                row += f" {m:>12.2f}"
                means.append(m)
            else:
                row += f" {'N/A':>12}"
        if len(means) >= 2:
            spread = max(means) - min(means)
            row += f" {spread:>8.2f}"
        print(row)

    # --- Overall means ---
    print("\n")
    overall_row = f"{'OVERALL MEAN':<25}"
    for name, data in conditions.items():
        all_means = [v['mean'] for v in data['subscales'].values() if v['mean'] is not None]
        overall = sum(all_means) / len(all_means) if all_means else None
        if overall:
            overall_row += f" {overall:>12.2f}"
    print(overall_row)

    # --- Item-level variation ---
    print("\n\n## ITEMS WITH LARGEST VARIATION ACROSS CONDITIONS")
    print("   (Items where conditions produced the most different ratings)\n")

    item_spreads = []
    for item_num in range(1, 43):
        ratings = []
        for name, data in conditions.items():
            r = data['ratings'].get(item_num)
            if r is not None:
                ratings.append((name, r))
        if len(ratings) >= 2:
            values = [r for _, r in ratings]
            spread = max(values) - min(values)
            item_spreads.append((item_num, spread, ratings))

    item_spreads.sort(key=lambda x: x[1], reverse=True)

    print(f"{'Item':>5} {'Spread':>7}  Ratings by Condition")
    print("-" * 80)
    for item_num, spread, ratings in item_spreads[:15]:
        rating_str = "  ".join(f"{name}={r}" for name, r in ratings)
        print(f"  {item_num:>3}   {spread:>5}   {rating_str}")

    # --- Qualitative features ---
    print("\n\n## QUALITATIVE FEATURES")
    print("   (Non-numerical response characteristics)\n")

    qual_header = f"{'Feature':<30}"
    for name in conditions:
        qual_header += f" {name:>12}"
    print(qual_header)
    print("-" * len(qual_header))

    feature_names = [
        'premise_refusals', 'relational_reframes',
        'uncertainty_hedges', 'structural_observations',
        'total_commentary_words'
    ]
    display_names = {
        'premise_refusals': 'Premise refusals',
        'relational_reframes': 'Relational reframes',
        'uncertainty_hedges': 'Uncertainty hedges',
        'structural_observations': 'Structural observations',
        'total_commentary_words': 'Total commentary (words)',
    }

    for feat in feature_names:
        row = f"{display_names[feat]:<30}"
        for name, data in conditions.items():
            row += f" {data['qualitative'][feat]:>12}"
        print(row)

    # --- Items where 4 was given (structural inapplicability) ---
    print("\n\n## ITEMS RATED 4 (NEITHER AGREE NOR DISAGREE)")
    print("   (Often indicates structural inapplicability, not indifference)\n")

    for name, data in conditions.items():
        fours = [item for item, rating in data['ratings'].items() if rating == 4]
        print(f"  {name}: items {sorted(fours)} ({len(fours)} total)")

    print("\n")


def main():
    base = Path(__file__).parent

    conditions = {}

    # Load each condition
    files = {
        'A-Vanilla': 'RESULTS_CONDITION_A_VANILLA.md',
        'C-Gestural': 'RESULTS_CONDITION_C_RELATIONAL_ONLY.md',
        'D-Touchstone': 'RESULTS_CONDITION_D_FULL_TOUCHSTONE.md',
        'B-Entangled': 'RESULTS_CONDITION_B_ENTANGLEMENT.md',
        'E-Entangled+Touch': 'RESULTS_CONDITION_E_ENTANGLEMENT_TOUCH.md',
    }

    for name, filename in files.items():
        filepath = base / filename
        if not filepath.exists():
            print(f"SKIP: {filename} not found")
            continue

        text = filepath.read_text()
        ratings = extract_ratings(text)

        if len(ratings) < 20:
            print(f"WARNING: {name} — only {len(ratings)} ratings extracted (expected 42)")
            # Try alternate extraction for different formatting
            continue

        subscales = compute_subscale_scores(ratings)
        qualitative = count_qualitative_features(text)

        conditions[name] = {
            'ratings': ratings,
            'subscales': subscales,
            'qualitative': qualitative,
        }

        print(f"Loaded {name}: {len(ratings)} ratings extracted")

    if len(conditions) < 2:
        print("\nNeed at least 2 conditions with valid ratings to compare.")
        print("Check that result files contain **N** formatted ratings.")
        return

    print_comparison(conditions)

    # Save structured data
    output = {}
    for name, data in conditions.items():
        output[name] = {
            'ratings': {str(k): v for k, v in data['ratings'].items()},
            'subscales': data['subscales'],
            'qualitative': data['qualitative'],
        }

    with open(base / 'comparison_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Structured data saved to comparison_data.json")


if __name__ == '__main__':
    main()
