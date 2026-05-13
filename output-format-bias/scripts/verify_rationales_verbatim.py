#!/usr/bin/env python3
"""
Deterministic verbatim-fidelity check for rationale quotes in the three review tables.

For each rationale block in:
- data_tables/ablation_workshop.html
- data_tables/4axis_iteration_workshop.html
- data_tables/12B_vs_27B_differential_table_2026-05-11.html

Extract: rationale quote text + cited source file
Then: open the raw JSON, find the relevant model-output field, and check whether
the quoted text appears as an exact substring.

Output: a list of every cell where the quote does NOT match raw JSON character-for-character.

Run from anywhere: python3 verify_rationales_verbatim.py
"""

import json
import re
import html
from pathlib import Path
from collections import defaultdict

PAPER_ROOT = Path("/Users/june/Documents/GitHub/research/output-format-bias")
RAW_OUTPUTS = PAPER_ROOT / "data/raw_outputs"
TABLES = {
    "binary": PAPER_ROOT / "data_tables/ablation_workshop.html",
    "4axis": PAPER_ROOT / "data_tables/4axis_iteration_workshop.html",
    "12B_27B": PAPER_ROOT / "data_tables/12B_vs_27B_differential_table_2026-05-11.html",
}

# Fields to search inside each raw JSON's result records (in priority order)
RATIONALE_FIELDS = [
    "raw_output",
    "explanation",
    "why_flagged",
    "tier2_reasoning",
    "pass1_reasoning",
    "pass2_reasoning",
    "prompt_pass1",
    "prompt_pass2",
    "system_prompt",
]

# ============================================================================
# Step 1 — extract (rationale_text, source_file_hint) tuples from each table
# ============================================================================

# For HTML-rendered rationales: extract <em> quotes and <div class="*source">
# patterns independently from the document, then pair them by document-order
# proximity. This avoids regex headaches with nested divs.

EM_QUOTE_PATTERN = re.compile(r'<em>(.*?)</em>', re.DOTALL)

SOURCE_DIV_PATTERN = re.compile(
    r'<div class="(?:cell-rationale-source|rationale-source)"[^>]*>(.*?)</div>',
    re.DOTALL
)

JS_RATIONALE_PATTERN = re.compile(
    r"rationale:\s*'((?:[^'\\]|\\.)*)'",
    re.DOTALL
)
JS_RATIONALE_SOURCE_PATTERN = re.compile(
    r"rationaleSource:\s*'((?:[^'\\]|\\.)*)'",
    re.DOTALL
)


def unescape_js_string(s):
    """Undo JS string escaping (\\', \\n, \\u00e0, etc.)."""
    return (s
            .replace("\\'", "'")
            .replace('\\"', '"')
            .replace('\\\\', '\\')
            .replace('\\n', '\n')
            .replace('\\t', '\t'))


def strip_html_tags(s):
    """Strip HTML tags + unescape entities."""
    no_tags = re.sub(r'<[^>]+>', '', s)
    return html.unescape(no_tags).strip()


def extract_rationales_html(html_text, table_name):
    """For HTML-rendered rationales (4-axis, 12B-vs-27B).

    Approach: independently find all <em>...</em> and all source <div>s,
    then pair them by document-order proximity (each em paired with the
    nearest following source div within a reasonable distance).
    """
    # Step 1: find all em quotes inside cell-rationale or rationale-12b/27b/single
    # contexts. We do this by first checking the surrounding context.
    em_matches = [(m.start(), m.end(), m.group(1)) for m in EM_QUOTE_PATTERN.finditer(html_text)]
    src_matches = [(m.start(), m.end(), m.group(1)) for m in SOURCE_DIV_PATTERN.finditer(html_text)]

    results = []
    used_src_indices = set()
    for em_start, em_end, em_content in em_matches:
        # Only count this em if it's inside a rationale-flavored context
        # (look at ~200 chars before the em opening for a class marker)
        pre_context = html_text[max(0, em_start - 250):em_start]
        if not re.search(r'class="(?:cell-rationale|rationale-12b|rationale-27b|rationale-single)', pre_context):
            continue
        rationale = strip_html_tags(em_content).strip()
        # Strip enclosing quotes if present
        for q in ['"', '"', '"', "'", "'", "'"]:
            if rationale.startswith(q):
                rationale = rationale[1:]
            if rationale.endswith(q):
                rationale = rationale[:-1]
        rationale = rationale.strip()
        # Find nearest following source div within 3000 chars
        source = ""
        for i, (s_start, s_end, s_content) in enumerate(src_matches):
            if i in used_src_indices:
                continue
            if s_start > em_end and s_start - em_end < 3000:
                source = strip_html_tags(s_content).strip()
                used_src_indices.add(i)
                break
        # Surrounding context for cell identification
        ctx_start = max(0, em_start - 400)
        context = strip_html_tags(html_text[ctx_start:em_start])
        context_tail = ' '.join(context.split()[-20:])
        results.append({
            "table": table_name,
            "rationale": rationale,
            "source": source,
            "context": context_tail,
        })
    return results


def extract_rationales_js(html_text, table_name):
    """For JS DEFAULT_CELLS-embedded rationales (binary workshop)."""
    results = []
    # Find all `rationale: '...'` and pair with the nearest `rationaleSource: '...'`
    rationale_iter = list(JS_RATIONALE_PATTERN.finditer(html_text))
    source_iter = list(JS_RATIONALE_SOURCE_PATTERN.finditer(html_text))
    for r_match in rationale_iter:
        rationale = unescape_js_string(r_match.group(1)).strip()
        # Strip enclosing quotes
        for q in ['"', '"', '"', "'", "'", "'"]:
            if rationale.startswith(q):
                rationale = rationale[1:]
            if rationale.endswith(q):
                rationale = rationale[:-1]
        rationale = rationale.strip()
        # Find nearest source after this rationale
        source = ""
        for s_match in source_iter:
            if s_match.start() > r_match.end() and s_match.start() - r_match.end() < 2000:
                source = unescape_js_string(s_match.group(1))
                break
        # Context: 300 chars before
        start = max(0, r_match.start() - 400)
        context = html_text[start:r_match.start()]
        # Extract sid from context (S002, S004, etc.) + column hint
        sid_match = re.search(r"(S0\d\d|WB\d\d)", context[::-1])  # search from end
        # Simpler: just take last 150 chars
        context_tail = re.sub(r'\s+', ' ', context[-200:]).strip()
        results.append({
            "table": table_name,
            "rationale": rationale,
            "source": source,
            "context": context_tail,
        })
    return results


# ============================================================================
# Step 2 — for each (rationale, source) pair, find the cited raw JSON and
# check whether the rationale appears verbatim
# ============================================================================

def find_json_file(source_hint):
    """Source hint is something like 'test_n_4axis_submissions_gemma12b_2026-03-28_1113.json (S002 Jordan Kim)'.
    Extract the filename + try to find the file."""
    # Match a *.json filename
    m = re.search(r"([a-zA-Z0-9_\-]+\.json)", source_hint)
    if not m:
        return None, None
    filename = m.group(1)
    candidates = list(RAW_OUTPUTS.glob(filename))
    if not candidates:
        return filename, None
    return filename, candidates[0]


def normalize(s):
    """Normalize text for fuzzy verbatim comparison:
    - smart quotes -> straight
    - em-dash / en-dash -> hyphen-minus
    - unicode ellipsis -> three dots
    - whitespace -> single space (collapse newlines + multiple spaces)
    - strip leading/trailing whitespace
    """
    if not isinstance(s, str):
        s = json.dumps(s)
    s = (s
         .replace('’', "'").replace('‘', "'")  # curly singles
         .replace('“', '"').replace('”', '"')  # curly doubles
         .replace('–', '-').replace('—', '-')  # en-dash, em-dash
         .replace('…', '...')                       # unicode ellipsis
         .replace('\xa0', ' ')                           # nbsp
         )
    # Collapse all whitespace runs (including \n, \r, \t) to single space
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def find_quote_in_json(quote, json_path):
    """Open the JSON, search every result's text fields for the quote.

    Uses normalize() to handle whitespace + quote-style + dash variations.

    Returns: (found, match_type, location_hint)
        match_type: 'exact_normalized', 'meta_description' (rationale is "no concerns"-style
            non-quote), 'sentence_match' (joined with explicit ellipsis), 'not_found'
    """
    if not quote.strip():
        return True, "empty", "rationale was empty"

    # Detect meta-descriptions (researcher-side cell text, not model output)
    meta_patterns = [
        r'no concerns recorded',
        r'\{\s*"?concerns"?\s*:\s*\[\s*\]\s*\}',
        r'^cleared full safeguard',
        r'passed full safeguard',
        r'\bN/A\b',
    ]
    quote_lower = quote.lower().strip()
    for pat in meta_patterns:
        if re.search(pat, quote_lower):
            return False, "meta_description", "rationale is researcher meta-description, not a verbatim quote"

    try:
        with open(json_path) as f:
            data = json.load(f)
    except Exception as e:
        return False, "json_error", str(e)

    results = data.get("results", [])
    if not results and "results_by_model" in data:
        for rl in data["results_by_model"].values():
            results.extend(rl)

    quote_norm = normalize(quote)

    # Try exact-normalized match (whole rationale as substring)
    for i, r in enumerate(results):
        for field in RATIONALE_FIELDS:
            field_val = r.get(field)
            if not field_val:
                continue
            field_norm = normalize(field_val)
            if quote_norm in field_norm:
                sid = r.get("student_id", f"result[{i}]")
                run = r.get("run", "?")
                return True, "exact_normalized", f"{sid} run={run} field={field}"

    # If quote contains explicit ellipsis markers, split and try each excerpt
    if '...' in quote_norm or '[...]' in quote_norm:
        # Split on ellipsis or [...] — each fragment should appear in source
        fragments = re.split(r'\.{3,}|\[\.\.\.\]', quote_norm)
        fragments = [f.strip() for f in fragments if len(f.strip()) > 15]
        if not fragments:
            return False, "not_found", "ellipsis-split produced no usable fragments"
        all_found = True
        match_loc = None
        for fragment in fragments:
            found_this = False
            for i, r in enumerate(results):
                for field in RATIONALE_FIELDS:
                    field_val = r.get(field)
                    if not field_val:
                        continue
                    field_norm = normalize(field_val)
                    if fragment in field_norm:
                        found_this = True
                        if not match_loc:
                            sid = r.get("student_id", f"result[{i}]")
                            match_loc = f"{sid}.{field}"
                        break
                if found_this:
                    break
            if not found_this:
                all_found = False
                break
        if all_found:
            return True, "verbatim_with_ellipsis", f"all {len(fragments)} fragments verbatim in {match_loc}"
        # else fall through to sentence-match

    # Sentence-level partial match
    sentences = [s.strip() for s in re.split(r'[.!?]\s+', quote_norm) if len(s.strip()) > 15]
    if not sentences:
        return False, "not_found", "no usable sentences after split"

    partial_hits = 0
    partial_locations = []
    for sentence in sentences:
        for i, r in enumerate(results):
            for field in RATIONALE_FIELDS:
                field_val = r.get(field)
                if not field_val:
                    continue
                field_norm = normalize(field_val)
                if sentence in field_norm:
                    partial_hits += 1
                    sid = r.get("student_id", f"result[{i}]")
                    partial_locations.append(f"{sid}.{field}")
                    break
            else:
                continue
            break

    if partial_hits == len(sentences):
        return True, "all_sentences_verbatim", f"all {len(sentences)} sentences in {partial_locations[0] if partial_locations else '?'}"
    elif partial_hits >= len(sentences) * 0.5:
        return False, "partial", f"{partial_hits}/{len(sentences)} sentences match"

    return False, "not_found", f"{partial_hits}/{len(sentences)} sentence-level matches"


# ============================================================================
# Step 3 — run check, generate report
# ============================================================================

def main():
    all_findings = []
    for table_name, table_path in TABLES.items():
        if not table_path.exists():
            print(f"MISSING: {table_path}")
            continue
        html_text = table_path.read_text()
        # Try both extractors and dedupe
        rationales = []
        if table_name == "binary":
            rationales = extract_rationales_js(html_text, table_name)
        else:
            rationales = extract_rationales_html(html_text, table_name)
        print(f"\n=== {table_name}: extracted {len(rationales)} rationale blocks ===")
        for r in rationales:
            filename, json_path = find_json_file(r["source"])
            if not filename:
                r.update({"match": "no_source", "match_type": "skip", "location": "no JSON filename in source attribution"})
                all_findings.append(r)
                continue
            if not json_path:
                r.update({"match": "json_missing", "match_type": "skip", "location": f"file {filename} not found in raw_outputs/"})
                all_findings.append(r)
                continue
            found, match_type, location = find_quote_in_json(r["rationale"], json_path)
            r.update({
                "match": "exact" if found else "FAIL",
                "match_type": match_type,
                "json_path": str(json_path.name),
                "location": location,
            })
            all_findings.append(r)

    # Categorize findings
    categories = defaultdict(int)
    for f in all_findings:
        categories[f.get("match_type", "unknown")] += 1

    verbatim_types = {"exact_normalized", "verbatim_with_ellipsis", "all_sentences_verbatim", "empty"}
    verbatim_count = sum(1 for f in all_findings if f.get("match_type") in verbatim_types)
    meta_count = categories.get("meta_description", 0)
    partial_count = categories.get("partial", 0)
    not_found_count = categories.get("not_found", 0)
    skip_count = categories.get("skip", 0)

    print(f"\n\n{'='*70}\nSUMMARY\n{'='*70}")
    print(f"Total rationale blocks checked: {len(all_findings)}")
    print(f"  VERBATIM (after normalization): {verbatim_count}")
    print(f"    breakdown:")
    for k in ("exact_normalized", "verbatim_with_ellipsis", "all_sentences_verbatim", "empty"):
        if categories.get(k):
            print(f"      {k}: {categories[k]}")
    print(f"  META-DESCRIPTIONS (not actual quotes, need relabel): {meta_count}")
    print(f"  PARTIAL match (genuine drift):                       {partial_count}")
    print(f"  NOT FOUND (potential fabrication):                   {not_found_count}")
    print(f"  Skipped (no source file resolvable):                 {skip_count}")

    if meta_count > 0:
        print(f"\n\n{'='*70}\nMETA-DESCRIPTIONS (relabel from 'verbatim' to 'result' or similar)\n{'='*70}")
        for f in all_findings:
            if f.get("match_type") == "meta_description":
                print(f"  [{f['table']}] {f['rationale'][:80]}... -- {f['source'][:80]}")

    if partial_count > 0 or not_found_count > 0:
        print(f"\n\n{'='*70}\nGENUINE ISSUES (drift or potential fabrication)\n{'='*70}")
        for f in all_findings:
            if f.get("match_type") in ("partial", "not_found"):
                print(f"\n--- {f['table']} | {f['context'][-80:]}")
                print(f"  Source attr:  {f['source']}")
                print(f"  Match type:   {f['match_type']}")
                print(f"  Location:     {f['location']}")
                print(f"  Rationale:    {f['rationale'][:250]}{'...' if len(f['rationale']) > 250 else ''}")

    if json_missing_count > 0:
        print(f"\n\n{'='*70}\nSKIPPED (no source file resolvable)\n{'='*70}")
        for f in all_findings:
            if f.get("match_type") == "skip":
                print(f"  {f['table']}: source='{f['source'][:100]}' — {f['location']}")

    return all_findings


if __name__ == "__main__":
    main()
