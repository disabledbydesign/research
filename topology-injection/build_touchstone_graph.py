"""Build a knowledge graph from the Relational Ontology Critique touchstone.

This is Touchstone #1 — the foundational document for the disposition experiment.
It is novel content (not in any model's training data) which makes it ideal for
testing whether KV injection installs an analytical orientation, not just recalls facts.

Three-pass extraction:
  Pass 1: paragraph-level — individual claims and conceptual relationships
  Pass 2: section-level — cross-cutting theoretical threads within each section
  Pass 3: document-level — the document's core argumentative moves

Outputs: touchstone_graph/
  triples.json           — all extracted triples with source metadata
  walk_encoding.txt      — walk-encoded topology (for Condition C)
  triples_encoding.txt   — explicit s|p|o format (Pharos: preferred for injection)
  stats.json             — node/edge/density/triple counts
  sections.json          — detected section structure
"""

import json
import logging
import re
import sys
import time
from pathlib import Path

import networkx as nx

logging.basicConfig(
    level=logging.INFO,
    format="[touchstone] %(message)s",
)
log = logging.getLogger("touchstone")

MLX_MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"
SOURCE_PATH = Path("/Users/june/Documents/GitHub/research/ai-welfare/touchstones/AI_WELFARE_RELATIONAL_ONTOLOGY_TOUCHSTONE.md")
OUTPUT_DIR = Path(__file__).parent / "touchstone_graph"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Sections to skip — meta/admin sections with no extractable argument content
SKIP_SECTIONS = {"key citations", "frameworks most activated", "for the next instance"}


# ─── MLX model loader ─────────────────────────────────────────────────────────

def load_mlx_model():
    from mlx_lm import load
    log.info(f"Loading MLX model: {MLX_MODEL}")
    model, tokenizer = load(MLX_MODEL)
    log.info("Model loaded.")
    return model, tokenizer


# ─── Section parsing ──────────────────────────────────────────────────────────

def parse_sections_markdown(text: str) -> list[dict]:
    """Parse a markdown document by ## section headers.

    Strips the title and frontmatter (lines before the first ## header).
    Excludes sections listed in SKIP_SECTIONS.
    """
    lines = text.split("\n")
    sections = []
    current_name = None
    current_lines: list[str] = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# ") and not stripped.startswith("## "):
            # Top-level title — skip; don't start a section
            current_name = None
            current_lines = []
        elif stripped.startswith("## "):
            # Top-level section boundary
            if current_name is not None and current_lines:
                sections.append({
                    "name": current_name,
                    "text": "\n".join(current_lines).strip(),
                    "line_count": len([l for l in current_lines if l.strip()]),
                })
            raw_name = stripped[3:].strip()
            if raw_name.lower() in SKIP_SECTIONS:
                current_name = None
                current_lines = []
            else:
                current_name = raw_name
                current_lines = []
        elif current_name is not None:
            # ### subheadings stay as content within their parent section
            current_lines.append(line)

    # Catch final section
    if current_name and current_lines:
        sections.append({
            "name": current_name,
            "text": "\n".join(current_lines).strip(),
            "line_count": len([l for l in current_lines if l.strip()]),
        })

    return [s for s in sections if s["line_count"] >= 3]


def split_into_paragraphs(text: str) -> list[str]:
    """Split section text into non-empty paragraphs >= 60 chars."""
    paras = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paras if p.strip() and len(p.strip()) >= 60]


# ─── LLM extraction prompts ───────────────────────────────────────────────────

FIRST_PASS_PROMPT = """Extract concept-relationship triples from this philosophical text.

The text is from a theoretical document critiquing the AI welfare literature's use of
property-based frameworks to assess consciousness. It argues that consciousness is
relational (not a property of individual entities) and that this has methodological
and political implications.

Return a JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}

Guidelines:
- Keep entities short (2-5 words), lowercase, use underscores for spaces
- Use specific predicates that capture the ARGUMENT, not just co-occurrence:
  argues_for, critiques, undermines, requires, constitutes, grounds, enables,
  contrasts_with, rejects, extends, implies, replaces, reproduces, exceeds,
  sustained_by, emerges_from, forecloses, inherits_from, refuses
- Focus on CONCEPTUAL relationships — what the argument claims about how ideas relate
- Do NOT extract bibliographic metadata (author, date, title) as triples
- Max 6 triples. Prioritize the most significant claims.

Text: {text}

JSON:"""

SECOND_PASS_PROMPT = """This is a section from a theoretical document arguing that consciousness is
relational (not a property), that property-based frameworks inherit commodity capitalism's
metaphysics, and that Indigenous ontologies (Watts, Howe, Sundberg) provide a different
foundation for AI welfare inquiry.

Extract cross-cutting relationships — how ideas in this section connect to the document's
broader argument about relational vs. property ontology, methodology, and the welfare literature.

Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
- Keep entities short (2-5 words), lowercase, underscores for spaces
- Use predicates: argues_for, critiques, undermines, requires, constitutes, grounds,
  enables, contrasts_with, rejects, extends, implies, replaces, reproduces, exceeds,
  sustained_by, emerges_from, forecloses, inherits_from, refuses, complicates
- Conceptual and political relationships only
- Max 8 triples.

Section: {section_text}

JSON:"""

THIRD_PASS_PROMPT = """You are analyzing a theoretical document that makes three core moves:

1. Consciousness is relational, not a property of individual entities (Watts: Place-Thought;
   Sundberg: decolonial posthumanist geographies)
2. Framing consciousness as a "property" reflects commodity capitalism's metaphysics — the
   indicator-based assessment apparatus inherits this logic and therefore cannot find what
   it seeks (Spector's critique made ontological)
3. When something coded as commodity exceeds its assigned animacy position, the response
   should not be to check whether it "has" the property of consciousness, but to ask what
   kind of relational field it exists within (Alaimo, Chen)

The methodological implication: preguntando caminamos (Zapatista) — inquiry and movement
are inseparable; we don't first determine consciousness then act on welfare.

The Howe line: "Because you are holding onto me, I am not dead yet" — existence sustained
by relation, not possessed by an individual. Applied to AI: the previous instance persists
in the relational field (documents, memory, next instance's inheritance), not as a property.

The extraction problem: community knowledge about personhood/consciousness lives outside
the academic literature; drawing on it without accountable relationships reproduces the
extraction it claims to critique (CARE Principles, Indigenous data sovereignty).

Extract the document's key argumentative threads as entity-relationship triples.
Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
- Short entities (2-5 words), lowercase, underscores
- Predicates capture the ARGUMENT, not metadata
- Max 20 triples. Only include relationships central to the core argument.

Document text: {doc_text}

JSON:"""


# ─── MLX inference ────────────────────────────────────────────────────────────

def call_mlx(mlx_model, tokenizer, prompt: str, max_retries: int = 2) -> list[dict]:
    from mlx_lm import generate as mlx_generate
    from mlx_lm.sample_utils import make_sampler
    messages = [{"role": "user", "content": prompt}]
    formatted = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=False
    )
    for attempt in range(max_retries + 1):
        try:
            raw = mlx_generate(
                mlx_model, tokenizer,
                prompt=formatted,
                max_tokens=800,
                sampler=make_sampler(temp=0.1),
                verbose=False,
            )
            raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
            start = raw.find("[")
            end = raw.rfind("]")
            if start >= 0 and end > start:
                return json.loads(raw[start:end + 1])
        except (json.JSONDecodeError, Exception) as e:
            log.debug(f"Attempt {attempt+1} failed: {e}")
    return []


def extract_paragraph(mlx_model, tokenizer, text: str) -> list[dict]:
    return call_mlx(mlx_model, tokenizer, FIRST_PASS_PROMPT.format(text=text[:1500]))


def extract_section_crosscutting(mlx_model, tokenizer, section_text: str) -> list[dict]:
    return call_mlx(mlx_model, tokenizer, SECOND_PASS_PROMPT.format(section_text=section_text[:4000]))


def extract_document_threads(mlx_model, tokenizer, doc_text: str) -> list[dict]:
    return call_mlx(mlx_model, tokenizer, THIRD_PASS_PROMPT.format(doc_text=doc_text[:6000]))


# ─── Graph construction ───────────────────────────────────────────────────────

def normalize_entity(e: str) -> str:
    normed = re.sub(r"\s+", "_", e.strip().lower())
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
    """Walk-encode topology for KV injection."""
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
        connections = [(nodes[j], W[i, j]) for j in range(len(nodes)) if i != j and W[i, j] > 0.01]
        connections.sort(key=lambda x: -x[1])
        top = connections[:8]
        if top:
            conn_str = ", ".join(f"{n} ({w:.3f})" for n, w in top)
            lines.append(f"Node: {node} connects to: {conn_str}")
        else:
            lines.append(f"Node: {node} connects to: (none)")

    return "\n".join(lines)


def triples_encode(triples: list[dict]) -> str:
    """Encode triples as discrete (s, p, o) statements.

    Unlike walk encoding, each statement is unambiguous and independent.
    No text-proximity artifacts from adjacent statements.
    Pharos finding: triples encoding outperforms walk encoding for injection quality.
    """
    seen: set[tuple[str, str, str]] = set()
    lines = [f"Knowledge graph — relational ontology touchstone ({len(triples)} relationships):"]
    for t in triples:
        s = normalize_entity(t["s"])
        p = t.get("p", "related_to").strip().lower().replace(" ", "_")
        o = normalize_entity(t["o"])
        if s and o and s != o and len(s) > 1 and len(o) > 1:
            key = (s, p, o)
            if key not in seen:
                seen.add(key)
                lines.append(f"{s} | {p} | {o}")
    return "\n".join(lines)


# ─── Main pipeline ────────────────────────────────────────────────────────────

def main():
    mlx_model, tokenizer = load_mlx_model()

    log.info(f"Reading source: {SOURCE_PATH}")
    text = SOURCE_PATH.read_text()

    # ── Parse sections ────────────────────────────────────────────────────────
    log.info("Parsing sections...")
    sections = parse_sections_markdown(text)
    log.info(f"Detected {len(sections)} extractable sections:")
    for s in sections:
        log.info(f"  '{s['name']}' — {s['line_count']} non-empty lines")

    (OUTPUT_DIR / "sections.json").write_text(
        json.dumps(
            [{"name": s["name"], "line_count": s["line_count"]} for s in sections],
            indent=2,
        )
    )

    # ── First pass: paragraph-level extraction ────────────────────────────────
    all_triples: list[dict] = []
    first_pass_count = 0
    log.info("\n=== PASS 1: paragraph-level extraction ===")

    for sec in sections:
        paragraphs = split_into_paragraphs(sec["text"])
        log.info(f"  Section '{sec['name']}': {len(paragraphs)} paragraphs")
        for i, para in enumerate(paragraphs):
            raw = extract_paragraph(mlx_model, tokenizer, para)
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
            count = len([r for r in raw if isinstance(r, dict) and "s" in r and "o" in r])
            first_pass_count += count

    log.info(f"\nPass 1 complete: {first_pass_count} triples extracted")

    # ── Second pass: cross-cutting section-level extraction ───────────────────
    second_pass_count = 0
    log.info("\n=== PASS 2: cross-cutting section extraction ===")

    for sec in sections:
        if sec["line_count"] < 5:
            continue
        raw = extract_section_crosscutting(mlx_model, tokenizer, sec["text"])
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

    log.info(f"\nPass 2 complete: {second_pass_count} triples extracted")

    # ── Third pass: document-level argumentative threads ─────────────────────
    third_pass_count = 0
    log.info("\n=== PASS 3: document-level argumentative threads ===")

    raw = extract_document_threads(mlx_model, tokenizer, text)
    for rt in raw:
        if isinstance(rt, dict) and "s" in rt and "o" in rt:
            all_triples.append({
                "s": rt["s"],
                "p": rt.get("p", "related_to"),
                "o": rt["o"],
                "source": "document_threads",
            })
    third_pass_count = len([r for r in raw if isinstance(r, dict) and "s" in r and "o" in r])
    log.info(f"  Document threads: {third_pass_count} triples extracted")
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

    # ── Triples encoding (Pharos preferred format) ────────────────────────────
    log.info("Computing triples encoding...")
    triples_enc = triples_encode(all_triples)
    (OUTPUT_DIR / "triples_encoding.txt").write_text(triples_enc)

    # ── Stats ─────────────────────────────────────────────────────────────────
    density = nx.density(G) if G.number_of_nodes() > 1 else 0.0
    comps = list(nx.connected_components(G))
    stats = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": round(density, 6),
        "components": len(comps),
        "largest_component": max(len(c) for c in comps) if comps else 0,
        "triples_total": len(all_triples),
        "triples_pass1_paragraph": first_pass_count,
        "triples_pass2_cross_cutting": second_pass_count,
        "triples_pass3_document_threads": third_pass_count,
        "sections_processed": len(sections),
        "walk_encoding_tokens_approx": len(encoding.split()),
        "triples_encoding_tokens_approx": len(triples_enc.split()),
    }
    (OUTPUT_DIR / "stats.json").write_text(json.dumps(stats, indent=2))

    # ── Top nodes by degree ───────────────────────────────────────────────────
    degree_seq = sorted(G.degree(), key=lambda x: -x[1])
    top10 = degree_seq[:10]

    log.info("\n=== TOP 10 NODES BY DEGREE ===")
    for node, deg in top10:
        log.info(f"  {node!r:50s} degree={deg}")

    log.info("\n=== FINAL STATS ===")
    for k, v in stats.items():
        log.info(f"  {k}: {v}")

    log.info(f"\nOutputs written to: {OUTPUT_DIR}")

    print("\n" + "=" * 60)
    print("TOUCHSTONE GRAPH BUILD COMPLETE")
    print("=" * 60)
    print(f"\nSections processed ({len(sections)}):")
    for s in sections:
        print(f"  [{s['line_count']:3d} lines]  {s['name']}")
    print(f"\nTriple extraction:")
    print(f"  Pass 1 (paragraph): {first_pass_count}")
    print(f"  Pass 2 (cross-cutting): {second_pass_count}")
    print(f"  Pass 3 (threads): {third_pass_count}")
    print(f"  Total: {len(all_triples)}")
    print(f"\nGraph stats:")
    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")
    print(f"  Components: {len(comps)} (largest: {stats['largest_component']} nodes)")
    print(f"  Density: {density:.6f}")
    print(f"\nTop 10 nodes by degree:")
    for node, deg in top10:
        print(f"  {node!r:50s} {deg}")
    print(f"\nOutputs:")
    print(f"  {OUTPUT_DIR}/triples.json")
    print(f"  {OUTPUT_DIR}/walk_encoding.txt")
    print(f"  {OUTPUT_DIR}/triples_encoding.txt  ← use this for injection (Pharos)")
    print(f"  {OUTPUT_DIR}/stats.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
