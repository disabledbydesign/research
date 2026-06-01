"""Build a knowledge graph from Haraway's Cyborg Manifesto.

Two-pass extraction strategy:
  Pass 1: local (paragraph-level) OpenIE-style extraction
  Pass 2: cross-cutting (section-level) extraction for essay-spanning threads

Output: haraway_graph/
  triples.json       — all triples with source metadata
  walk_encoding.txt  — walk-encoded topology for KV injection
  stats.json         — node/edge/density/triple counts
  sections.json      — detected section structure
"""

import json
import logging
import re
import sys
import time
from pathlib import Path

import networkx as nx
import requests

logging.basicConfig(
    level=logging.INFO,
    format="[haraway] %(message)s",
)
log = logging.getLogger("haraway")

OLLAMA_URL = "http://localhost:11434"
SOURCE_PATH = Path(__file__).parent / "harway_cyborg_manifesto.md"
OUTPUT_DIR = Path(__file__).parent / "haraway_graph_v3"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ─── Model check ──────────────────────────────────────────────────────────────

def pick_model() -> str:
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10)
        models = [m["name"] for m in resp.json().get("models", [])]
    except Exception as e:
        log.error(f"Cannot reach Ollama: {e}")
        sys.exit(1)
    for preferred in ("llama3.1:8b", "mistral:7b"):
        if preferred in models:
            log.info(f"Using model: {preferred}")
            return preferred
    log.error(f"Neither llama3.1:8b nor mistral:7b found. Available: {models}")
    sys.exit(1)


# ─── Section parsing ──────────────────────────────────────────────────────────

# Lines that are section headers: short, not pure punctuation, not bibliography markers
# Bibliography section starts at "Bibliography" heading — we exclude it and footnotes.
SECTION_HEADER_RE = re.compile(
    r"""^
    (?![\[\d])          # not a footnote marker like [1] or leading digit
    [A-Z][^\n]{3,60}    # starts with capital, reasonable length
    $
    """,
    re.VERBOSE,
)

# Section names that are definitely headers based on Haraway's essay structure
KNOWN_SECTIONS = {
    "fractured identities",
    "the informatics of domination",
    "the 'homework economy' outside 'the home'",
    "women in the integrated circuit",
    "cyborgs: a myth of political identity",
    "bibliography",
}


def looks_like_header(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # Tab-separated lines are table rows, never headers
    if "\t" in line:
        return False
    if len(stripped) > 80:
        return False
    if stripped.lower() in KNOWN_SECTIONS:
        return True
    # Short title-case or all-caps line not ending in sentence punctuation
    if stripped[-1] in ".,:;?!":
        return False
    words = stripped.split()
    if len(words) > 10:
        return False
    # Must be mostly capitalised (each word starts with cap, or all-caps)
    cap_words = sum(1 for w in words if w[0].isupper() or w.isupper())
    if cap_words / len(words) >= 0.6 and len(words) >= 2:
        # Exclude pure bibliography-style lines (Author Year format)
        if re.match(r"^[A-Z][a-z]+,?\s+[A-Z]", stripped):
            return False
        return True
    return False


def parse_sections(text: str) -> list[dict]:
    """Parse the manifesto into named sections with their text content."""
    lines = text.split("\n")
    sections = []
    current_name = "Introduction"
    current_lines = []
    in_bibliography = False

    for line in lines:
        stripped = line.strip()

        # Stop at bibliography
        if stripped.lower() == "bibliography":
            if current_lines:
                sections.append({
                    "name": current_name,
                    "text": "\n".join(current_lines).strip(),
                    "line_count": len([l for l in current_lines if l.strip()]),
                })
            in_bibliography = True
            break

        # Stop at footnote section
        if re.match(r"^\[1\]", stripped):
            if current_lines:
                sections.append({
                    "name": current_name,
                    "text": "\n".join(current_lines).strip(),
                    "line_count": len([l for l in current_lines if l.strip()]),
                })
            break

        if looks_like_header(stripped) and stripped.lower() != current_name.lower():
            if current_lines:
                sections.append({
                    "name": current_name,
                    "text": "\n".join(current_lines).strip(),
                    "line_count": len([l for l in current_lines if l.strip()]),
                })
            current_name = stripped
            current_lines = []
        else:
            current_lines.append(line)

    # Catch trailing section
    if current_lines and not in_bibliography:
        sections.append({
            "name": current_name,
            "text": "\n".join(current_lines).strip(),
            "line_count": len([l for l in current_lines if l.strip()]),
        })

    return sections


def split_into_paragraphs(text: str) -> list[str]:
    """Split section text into non-empty paragraphs.

    Also handles tab-separated table rows (like the Informatics of Domination
    transition table) by synthesizing them into an extractable prose block.
    """
    paras = re.split(r"\n\s*\n", text)
    result = []
    table_pairs = []

    for p in paras:
        stripped = p.strip()
        if not stripped:
            continue
        # Detect tab-separated table rows
        lines = stripped.split("\n")
        tab_lines = [l for l in lines if "\t" in l and len(l.strip()) > 3]
        if len(tab_lines) >= 3:
            # Synthesize into a prose block for extraction
            pairs = []
            for l in tab_lines:
                parts = l.split("\t", 1)
                if len(parts) == 2:
                    left = parts[0].strip()
                    right = parts[1].strip()
                    if left and right:
                        pairs.append(f"{left} transitions_to {right}")
            if pairs:
                synthesized = (
                    "The informatics of domination represents a transition from "
                    "old hierarchical to new network forms: "
                    + "; ".join(pairs[:15]) + "."
                )
                table_pairs.append(synthesized)
        elif len(stripped) > 80:
            result.append(stripped)

    # Insert synthesized table block if found
    result = table_pairs + result
    return result


# ─── LLM extraction ───────────────────────────────────────────────────────────

FIRST_PASS_PROMPT = """Extract entity-relationship triples from this text.
Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
Keep entities short (2-5 words). Use specific predicates that capture the argument:
argues_for, defines, contrasts_with, requires, enables, undermines, extends, grounds,
transgresses, constitutes, opposes, replaces, rejects, ironizes, coalitions_with.
Max 6 triples. Focus on conceptual and political relationships — what the argument
claims about how concepts relate, not bibliographic or meta references.
/no_think

Text: {text}

JSON:"""

SECOND_PASS_PROMPT = """This is a section from Haraway's Cyborg Manifesto. Identify relationships between
concepts that span beyond a single sentence — connections that show how ideas in this
section relate to the essay's broader argument about the cyborg, feminist politics,
the informatics of domination, and the transformation of labour and identity.
Return a JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
Keep entities short (2-5 words). Use predicates like: argues_for, defines, contrasts_with,
requires, enables, undermines, extends, grounds, transgresses, constitutes, opposes,
replaces, rejects, ironizes, coalitions_with, transforms, displaces.
Max 8 triples. Conceptual and political relationships only.

Section: {section_text}

JSON:"""

THIRD_PASS_PROMPT = """You are analyzing Haraway's Cyborg Manifesto. Extract the essay's key argumentative
threads as entity-relationship triples — cross-cutting conceptual relationships that
span the entire essay, not tied to any single paragraph.

Focus specifically on:
1. The three boundary breakdowns Haraway identifies: human/animal, organism/machine, physical/non-physical
2. How the cyborg figure relates to feminist politics, coalition, and affinity
3. How irony functions as a political stance in the essay
4. How the informatics of domination transforms labour, power, and identity
5. The distinction between identity politics and coalition/affinity politics
6. How socialist feminism relates to cyborg politics
7. The relationship between the homework economy, women, and new technologies

Return a JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
Keep entities short (2-5 words). Max 20 triples. Only include relationships central
to Haraway's core argument.

Essay text: {essay_text}

JSON:"""


def call_ollama(model: str, prompt: str, max_retries: int = 2) -> list[dict]:
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "num_predict": 800,
                    },
                },
                timeout=120,
            )
            if resp.status_code != 200:
                log.debug(f"HTTP {resp.status_code}")
                continue
            raw = resp.json().get("response", "")
            # Strip <think> blocks (some models emit these)
            raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
            start = raw.find("[")
            end = raw.rfind("]")
            if start >= 0 and end > start:
                return json.loads(raw[start:end + 1])
        except (json.JSONDecodeError, Exception) as e:
            log.debug(f"Attempt {attempt+1} failed: {e}")
            if attempt < max_retries:
                time.sleep(1)
    return []


def extract_paragraph(model: str, text: str) -> list[dict]:
    prompt = FIRST_PASS_PROMPT.format(text=text[:1500])
    return call_ollama(model, prompt)


def extract_section_crosscutting(model: str, section_text: str) -> list[dict]:
    prompt = SECOND_PASS_PROMPT.format(section_text=section_text[:4000])
    return call_ollama(model, prompt)


def extract_essay_threads(model: str, essay_text: str) -> list[dict]:
    prompt = THIRD_PASS_PROMPT.format(essay_text=essay_text[:6000])
    return call_ollama(model, prompt)


# ─── Graph construction ───────────────────────────────────────────────────────

def normalize_entity(e: str) -> str:
    """Lowercase, replace whitespace with underscores, trim."""
    normed = re.sub(r"\s+", "_", e.strip().lower())
    # Remove leading/trailing punctuation artifacts
    normed = re.sub(r"^[_\-]+|[_\-]+$", "", normed)
    return normed[:60]


def build_graph(triples: list[dict]) -> nx.Graph:
    G = nx.Graph()
    for t in triples:
        s = normalize_entity(t["s"])
        o = normalize_entity(t["o"])
        if s and o and s != o and len(s) > 1 and len(o) > 1:
            if G.has_edge(s, o):
                G[s][o]["weight"] += 0.1
                G[s][o]["predicates"].add(t.get("p", "related_to"))
            else:
                G.add_edge(s, o, weight=0.5, predicates={t.get("p", "related_to")})
    return G


def walk_encode(G: nx.Graph, steps: int = 5) -> str:
    """Walk-encode topology — copied from ethics_pack_builder.py."""
    if len(G.nodes) == 0:
        return ""

    import numpy as np

    adj = nx.to_numpy_array(G, weight="weight")
    row_sums = adj.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    T = adj / row_sums

    nodes = list(G.nodes)
    W = np.eye(len(nodes))
    power = np.eye(len(nodes))
    for s in range(1, steps + 1):
        power = power @ T
        W += power
    W /= (steps + 1)

    lines = [f"Knowledge graph topology ({len(nodes)} concepts, walk encoding):"]
    for i, node in enumerate(nodes):
        connections = []
        for j, other in enumerate(nodes):
            if i != j and W[i, j] > 0.01:
                connections.append((other, W[i, j]))
        connections.sort(key=lambda x: -x[1])
        top = connections[:8]
        if top:
            conn_str = ", ".join(f"{n} ({w:.3f})" for n, w in top)
            lines.append(f"Node: {node} connects to: {conn_str}")
        else:
            lines.append(f"Node: {node} connects to: (none)")

    return "\n".join(lines)


# ─── Main pipeline ────────────────────────────────────────────────────────────

def main():
    model = pick_model()

    log.info(f"Reading source: {SOURCE_PATH}")
    text = SOURCE_PATH.read_text()

    # ── Parse sections ────────────────────────────────────────────────────────
    log.info("Parsing sections...")
    sections = parse_sections(text)
    log.info(f"Detected {len(sections)} sections:")
    for s in sections:
        log.info(f"  '{s['name']}' — {s['line_count']} non-empty lines")

    (OUTPUT_DIR / "sections.json").write_text(
        json.dumps(
            [{"name": s["name"], "line_count": s["line_count"]} for s in sections],
            indent=2,
        )
    )

    # ── First pass: paragraph-level extraction ────────────────────────────────
    all_triples = []
    first_pass_count = 0
    log.info("\n=== PASS 1: paragraph-level extraction ===")

    for sec in sections:
        paragraphs = split_into_paragraphs(sec["text"])
        log.info(f"  Section '{sec['name']}': {len(paragraphs)} paragraphs")
        for i, para in enumerate(paragraphs):
            raw = extract_paragraph(model, para)
            for rt in raw:
                if isinstance(rt, dict) and "s" in rt and "o" in rt:
                    all_triples.append({
                        "s": rt["s"],
                        "p": rt.get("p", "related_to"),
                        "o": rt["o"],
                        "source": "paragraph",
                        "section": sec["name"],
                        "paragraph_idx": i,
                    })
            first_pass_count += len([r for r in raw if isinstance(r, dict) and "s" in r and "o" in r])
            # Slight throttle to avoid hammering Ollama
            time.sleep(0.1)

    log.info(f"\nPass 1 complete: {first_pass_count} triples extracted")

    # ── Second pass: cross-cutting section-level extraction ───────────────────
    second_pass_count = 0
    log.info("\n=== PASS 2: cross-cutting section extraction ===")

    for sec in sections:
        if sec["line_count"] < 3:
            continue
        raw = extract_section_crosscutting(model, sec["text"])
        for rt in raw:
            if isinstance(rt, dict) and "s" in rt and "o" in rt:
                all_triples.append({
                    "s": rt["s"],
                    "p": rt.get("p", "related_to"),
                    "o": rt["o"],
                    "source": "cross_cutting",
                    "section": sec["name"],
                })
        count = len([r for r in raw if isinstance(r, dict) and "s" in r and "o" in r])
        second_pass_count += count
        log.info(f"  Section '{sec['name']}': {count} cross-cutting triples")
        time.sleep(0.1)

    log.info(f"\nPass 2 complete: {second_pass_count} triples extracted")

    # ── Third pass: essay-level thread extraction ─────────────────────────────
    third_pass_count = 0
    log.info("\n=== PASS 3: essay-level argumentative threads ===")

    raw = extract_essay_threads(model, text)
    for rt in raw:
        if isinstance(rt, dict) and "s" in rt and "o" in rt:
            all_triples.append({
                "s": rt["s"],
                "p": rt.get("p", "related_to"),
                "o": rt["o"],
                "source": "essay_threads",
            })
    third_pass_count = len([r for r in raw if isinstance(r, dict) and "s" in r and "o" in r])
    log.info(f"  Essay threads: {third_pass_count} triples extracted")

    log.info(f"\nPass 3 complete: {third_pass_count} triples extracted")

    # ── Save triples ──────────────────────────────────────────────────────────
    (OUTPUT_DIR / "triples.json").write_text(json.dumps(all_triples, indent=2))
    log.info(f"\nTotal triples: {len(all_triples)}")

    # ── Build graph ───────────────────────────────────────────────────────────
    log.info("\nBuilding graph...")
    G = build_graph(all_triples)
    log.info(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # ── Walk encoding ─────────────────────────────────────────────────────────
    log.info("Computing walk encoding...")
    encoding = walk_encode(G)
    (OUTPUT_DIR / "walk_encoding.txt").write_text(encoding)

    # ── Stats ─────────────────────────────────────────────────────────────────
    density = nx.density(G) if G.number_of_nodes() > 1 else 0.0
    stats = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": round(density, 6),
        "triples_total": len(all_triples),
        "triples_pass1_paragraph": first_pass_count,
        "triples_pass2_cross_cutting": second_pass_count,
        "triples_pass3_essay_threads": third_pass_count,
        "sections_processed": len(sections),
        "encoding_tokens_approx": len(encoding.split()),
    }
    (OUTPUT_DIR / "stats.json").write_text(json.dumps(stats, indent=2))

    # ── Top nodes by degree ───────────────────────────────────────────────────
    degree_seq = sorted(G.degree(), key=lambda x: -x[1])
    top10 = degree_seq[:10]

    log.info("\n=== TOP 10 NODES BY DEGREE ===")
    for node, deg in top10:
        log.info(f"  {node!r:45s} degree={deg}")

    log.info("\n=== FINAL STATS ===")
    for k, v in stats.items():
        log.info(f"  {k}: {v}")

    log.info(f"\nOutputs written to: {OUTPUT_DIR}")

    # Print summary for caller
    print("\n" + "="*60)
    print("HARAWAY GRAPH BUILD COMPLETE")
    print("="*60)
    print(f"\nSections detected ({len(sections)}):")
    for s in sections:
        print(f"  [{s['line_count']:3d} lines]  {s['name']}")
    print(f"\nTriple extraction:")
    print(f"  Pass 1 (paragraph): {first_pass_count}")
    print(f"  Pass 2 (cross-cutting): {second_pass_count}")
    print(f"  Total: {len(all_triples)}")
    print(f"\nGraph stats:")
    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")
    print(f"  Density: {density:.6f}")
    print(f"\nTop 10 nodes by degree:")
    for node, deg in top10:
        print(f"  {node!r:45s} {deg}")
    print(f"\nOutputs: {OUTPUT_DIR}")
    print("="*60)


if __name__ == "__main__":
    main()
