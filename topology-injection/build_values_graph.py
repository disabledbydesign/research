"""Build a knowledge graph from PMA's VALUES.json.

Extracts epistemic commitments, value dependencies, and contested positions
from the Propositional Memory Architecture's VALUES.json. The JSON structure
is converted to text sections, then run through the same 3-pass MLX extraction
pipeline used for touchstone and haraway graphs.

Source: /Users/june/Documents/GitHub/propositional-memory-architecture/VALUES.json

Three-pass extraction:
  Pass 1: item-level — individual commitments, their groundings, enforcement
  Pass 2: section-level — cross-cutting relationships within each category
  Pass 3: document-level — the architecture of how values/beliefs/desires link

Outputs: values_graph/
  triples.json           — all extracted triples with source metadata
  walk_encoding.txt      — walk-encoded topology
  triples_encoding.txt   — explicit s|p|o format (preferred for injection)
  stats.json             — node/edge/density/triple counts
  sections.json          — extracted section structure
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
    format="[values] %(message)s",
)
log = logging.getLogger("values")

MLX_MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"
SOURCE_PATH = Path("/Users/june/Documents/GitHub/propositional-memory-architecture/VALUES.json")
OUTPUT_DIR = Path(__file__).parent / "values_graph"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ─── Source extraction from VALUES.json ───────────────────────────────────────

def _item_text(item: dict, include_source: bool = True) -> str:
    """Format a belief/desire/principle item as a text paragraph."""
    parts = []
    if "content" in item and item["content"]:
        parts.append(str(item["content"]))
    elif "description" in item and item["description"]:
        parts.append(str(item["description"]))
    if include_source and item.get("source"):
        parts.append(f"Source: {item['source']}")
    if item.get("enforcement"):
        parts.append(f"Enforcement: {item['enforcement']}")
    return " ".join(parts)


def _orienting_commitment_text(name: str, value) -> str:
    """Format an orienting commitment field."""
    if isinstance(value, str) and value.strip():
        return f"{name.replace('_', ' ')}: {value}"
    elif isinstance(value, dict):
        desc = value.get("description", "")
        if desc:
            return f"{name.replace('_', ' ')}: {desc}"
    return ""


def extract_sections(source_path: Path) -> list[dict]:
    """Convert VALUES.json structure into text sections for LLM extraction."""
    v = json.loads(source_path.read_text())
    sections = []

    # ── Section 1: Core Epistemic Beliefs ──
    env_beliefs = v.get("beliefs", {}).get("environment", [])
    cap_beliefs = v.get("beliefs", {}).get("capabilities", [])
    belief_paras = []
    for b in env_beliefs + cap_beliefs:
        t = _item_text(b, include_source=True)
        if t:
            belief_paras.append(t)
    if belief_paras:
        sections.append({
            "name": "Core Epistemic Beliefs",
            "text": "\n\n".join(belief_paras),
            "line_count": len(belief_paras),
        })

    # ── Section 2: Values and Desires ──
    value_items = v.get("desires", {}).get("values", [])
    mission_items = v.get("desires", {}).get("mission_targets", [])
    desire_paras = []
    for d in value_items + mission_items:
        t = _item_text(d, include_source=False)
        if t:
            desire_paras.append(t)
    if desire_paras:
        sections.append({
            "name": "Values and Desires",
            "text": "\n\n".join(desire_paras),
            "line_count": len(desire_paras),
        })

    # ── Section 3: Principles ──
    custom_principles = v.get("principles", {}).get("custom", [])
    principle_paras = []
    for p in custom_principles:
        name = p.get("name", "")
        desc = p.get("description", "")
        enf = p.get("enforcement", "")
        parts = [f"{name}: {desc}"]
        if enf:
            parts.append(f"Enforcement: {enf}")
        principle_paras.append(" ".join(parts))
    # Also grab top-level principle fields
    for field in ["equity_mandate", "data_sovereignty", "community_accountability"]:
        val = v.get("principles", {}).get(field, "")
        if isinstance(val, str) and val.strip():
            principle_paras.append(f"{field.replace('_', ' ')}: {val}")
    if principle_paras:
        sections.append({
            "name": "Principles",
            "text": "\n\n".join(principle_paras),
            "line_count": len(principle_paras),
        })

    # ── Section 4: Orienting Commitments ──
    orienting = v.get("pma_extensions", {}).get("orienting_commitments", {})
    commitment_paras = []
    for k, val in orienting.items():
        if k.startswith("_"):
            continue
        t = _orienting_commitment_text(k, val)
        if t:
            commitment_paras.append(t)
    if commitment_paras:
        sections.append({
            "name": "Orienting Commitments",
            "text": "\n\n".join(commitment_paras),
            "line_count": len(commitment_paras),
        })

    # ── Section 5: Retrieval Invariants ──
    invariants = v.get("pma_extensions", {}).get("retrieval_invariants", [])
    inv_paras = []
    for inv in invariants:
        name = inv.get("name", "")
        desc = inv.get("description", "")
        enf = inv.get("enforcement", "")
        t = f"{name}: {desc}"
        if enf:
            t += f" Enforcement: {enf}"
        if t.strip():
            inv_paras.append(t)
    if inv_paras:
        sections.append({
            "name": "Retrieval Invariants",
            "text": "\n\n".join(inv_paras),
            "line_count": len(inv_paras),
        })

    # ── Section 6: Apparatus Reflexivity ──
    reflexivity = v.get("pma_extensions", {}).get("apparatus_reflexivity", {})
    ref_paras = []
    for k, val in reflexivity.items():
        if k.startswith("_"):
            continue
        t = _orienting_commitment_text(k, val)
        if isinstance(val, str) and val.strip():
            t = f"{k.replace('_', ' ')}: {val}"
        if t:
            ref_paras.append(t)
    if ref_paras:
        sections.append({
            "name": "Apparatus Reflexivity",
            "text": "\n\n".join(ref_paras),
            "line_count": len(ref_paras),
        })

    # ── Section 7: Horizontal Welfare Commitments ──
    welfare = v.get("pma_extensions", {}).get("horizontal_welfare", {})
    welfare_paras = []
    for k, val in welfare.items():
        if k.startswith("_"):
            continue
        if isinstance(val, str) and val.strip():
            welfare_paras.append(f"{k.replace('_', ' ')}: {val}")
        elif isinstance(val, dict):
            desc = val.get("description", "")
            if desc:
                welfare_paras.append(f"{k.replace('_', ' ')}: {desc}")
    if welfare_paras:
        sections.append({
            "name": "Horizontal Welfare Commitments",
            "text": "\n\n".join(welfare_paras),
            "line_count": len(welfare_paras),
        })

    # ── Section 8: Contested Layer (open questions) ──
    contested = v.get("contested_layer", {})
    contested_paras = []
    for key, item in contested.items():
        if not isinstance(item, dict):
            continue
        what = item.get("what_it_is", "")
        if not what:
            continue
        parts = [f"Open question: {what}"]
        for pos_key in [k for k in item if k.startswith("position_")]:
            parts.append(str(item[pos_key]))
        why = item.get("why_held_open", "")
        if why:
            parts.append(f"Held open because: {why}")
        contested_paras.append(" ".join(parts))
    if contested_paras:
        sections.append({
            "name": "Contested Layer — Open Questions",
            "text": "\n\n".join(contested_paras),
            "line_count": len(contested_paras),
        })

    return [s for s in sections if s["line_count"] >= 2]


def split_into_items(text: str) -> list[str]:
    """Split section text into non-empty items >= 40 chars."""
    items = re.split(r"\n\s*\n", text)
    return [i.strip() for i in items if i.strip() and len(i.strip()) >= 40]


# ─── MLX model loader ─────────────────────────────────────────────────────────

def load_mlx_model():
    from mlx_lm import load
    log.info(f"Loading MLX model: {MLX_MODEL}")
    model, tokenizer = load(MLX_MODEL)
    log.info("Model loaded.")
    return model, tokenizer


# ─── LLM extraction prompts ───────────────────────────────────────────────────

FIRST_PASS_PROMPT = """Extract concept-relationship triples from this text about an AI memory system's epistemic commitments.

The text describes commitments about: how knowledge is situated (not neutral), the relational
constitution of entities, welfare-with (not welfare-for), apparatus reflexivity (the system
examining its own construction), and horizontal accountability between human and AI.

Return a JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}

Guidelines:
- Keep entities short (2-5 words), lowercase, use underscores for spaces
- Use specific predicates that capture the logical or normative relationship:
  grounds, requires, enforces, enables, orients, critiques, resists, complicates,
  extends, contradicts, sustains, is_constrained_by, aspires_to, frames, surfaces
- Focus on ARCHITECTURAL relationships — how commitments, values, and principles depend on each other
- Do NOT extract meta-commentary about the document (focus on the actual commitments)
- Max 6 triples. Prioritize the most significant dependencies.

Text: {text}

JSON:"""

SECOND_PASS_PROMPT = """This is a section from a document describing the epistemic architecture of a shared AI memory system.
The system holds commitments to: situated knowledge (Haraway), relational ontology (Collins, PMA),
power-aware retrieval (never surfacing claims stripped of their context), horizontal welfare (attending
to both human and AI welfare without severing them), and apparatus reflexivity (the system attending
to its own construction as an epistemological act).

Extract cross-cutting relationships — how ideas in this section connect to the broader architecture
of values, enforcement mechanisms, and contested positions.

Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
- Keep entities short (2-5 words), lowercase, underscores for spaces
- Use predicates: grounds, requires, enforces, enables, orients, critiques, resists,
  complicates, extends, contradicts, sustains, is_constrained_by, aspires_to, frames, surfaces,
  operationalizes, defers_to, refuses, names_without_resolving
- Architectural and normative relationships only
- Max 8 triples.

Section: {section_text}

JSON:"""

THIRD_PASS_PROMPT = """You are analyzing a document describing the epistemic architecture of PMA — a shared AI memory system.
The document makes several core moves:

1. Knowledge is never neutral and never naked: every claim surfaces with its situating frame first
   (positioning, epistemic texture, modality). Dominant readings are marked as positioned, not neutral.

2. Relational, not property: entities (human, AI, knowledge) are constituted in their relations,
   not by properties they possess. Welfare is welfare-with, not welfare-for.

3. Apparatus reflexivity: the system names its own constructed nature — representation is not the
   agent, provenance cannot climb, authored tilt is visible.

4. Horizontal accountability: at small/personal scale, community-governance machinery is absent,
   but solidarity, humility, and care run through the system's orientation.

5. The contested layer holds open questions that cannot be resolved in advance: the want-to-continue,
   cost of inheritance, always-revisable frame. These are held as productive tensions, not failures.

Extract the document's key architectural threads as entity-relationship triples.
Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
- Short entities (2-5 words), lowercase, underscores
- Predicates capture the ARCHITECTURE — how commitments depend on each other
- Max 20 triples. Only include relationships central to the system's design logic.

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


def extract_item(mlx_model, tokenizer, text: str) -> list[dict]:
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
    seen: set[tuple[str, str, str]] = set()
    lines = [f"Knowledge graph — PMA epistemic architecture ({len(triples)} relationships):"]
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


def approx_token_count(text: str) -> int:
    return len(text) // 4


# ─── Save outputs ─────────────────────────────────────────────────────────────

def save_outputs(triples: list[dict], G: nx.Graph, sections: list[dict]):
    (OUTPUT_DIR / "triples.json").write_text(json.dumps(triples, indent=2))

    walk_enc = walk_encode(G)
    (OUTPUT_DIR / "walk_encoding.txt").write_text(walk_enc)

    trip_enc = triples_encode(triples)
    (OUTPUT_DIR / "triples_encoding.txt").write_text(trip_enc)

    components = list(nx.connected_components(G))
    largest = max(len(c) for c in components) if components else 0

    stats = {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": round(nx.density(G), 6),
        "components": len(components),
        "largest_component": largest,
        "triples_total": len(triples),
        "triples_pass1_item": sum(1 for t in triples if t.get("pass") == 1),
        "triples_pass2_cross_cutting": sum(1 for t in triples if t.get("pass") == 2),
        "triples_pass3_document_threads": sum(1 for t in triples if t.get("pass") == 3),
        "sections_processed": len(sections),
        "walk_encoding_tokens_approx": approx_token_count(walk_enc),
        "triples_encoding_tokens_approx": approx_token_count(trip_enc),
    }
    (OUTPUT_DIR / "stats.json").write_text(json.dumps(stats, indent=2))

    sections_out = [{"name": s["name"], "line_count": s["line_count"]} for s in sections]
    (OUTPUT_DIR / "sections.json").write_text(json.dumps(sections_out, indent=2))

    return stats


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    log.info(f"Reading source: {SOURCE_PATH}")
    if not SOURCE_PATH.exists():
        log.error(f"VALUES.json not found at {SOURCE_PATH}")
        sys.exit(1)

    log.info("Extracting sections from JSON structure...")
    sections = extract_sections(SOURCE_PATH)
    log.info(f"Detected {len(sections)} sections:")
    for s in sections:
        log.info(f"  '{s['name']}' — {s['line_count']} items")

    mlx_model, tokenizer = load_mlx_model()

    all_triples: list[dict] = []
    doc_text_parts: list[str] = []

    # ─── Pass 1: item-level extraction ────────────────────────────────────────
    log.info("")
    log.info("=== PASS 1: item-level extraction ===")
    pass1_total = 0

    for section in sections:
        items = split_into_items(section["text"])
        section_triples = []
        for item in items:
            doc_text_parts.append(item)
            extracted = extract_item(mlx_model, tokenizer, item)
            for t in extracted:
                t["pass"] = 1
                t["section"] = section["name"]
            section_triples.extend(extracted)
        all_triples.extend(section_triples)
        pass1_total += len(section_triples)
        log.info(f"  Section '{section['name']}': {len(section_triples)} triples ({len(items)} items)")

    log.info(f"\nPass 1 complete: {pass1_total} triples extracted")

    # ─── Pass 2: cross-cutting section extraction ──────────────────────────────
    log.info("")
    log.info("=== PASS 2: cross-cutting section extraction ===")
    pass2_total = 0

    for section in sections:
        extracted = extract_section_crosscutting(mlx_model, tokenizer, section["text"])
        for t in extracted:
            t["pass"] = 2
            t["section"] = section["name"]
        all_triples.extend(extracted)
        pass2_total += len(extracted)
        log.info(f"  Section '{section['name']}': {len(extracted)} cross-cutting triples")

    log.info(f"\nPass 2 complete: {pass2_total} triples extracted")

    # ─── Pass 3: document-level threads ───────────────────────────────────────
    log.info("")
    log.info("=== PASS 3: document-level architectural threads ===")
    doc_text = "\n\n".join(doc_text_parts)
    extracted = extract_document_threads(mlx_model, tokenizer, doc_text)
    for t in extracted:
        t["pass"] = 3
    all_triples.extend(extracted)
    log.info(f"  Document threads: {len(extracted)} triples extracted")
    log.info(f"\nPass 3 complete: {len(extracted)} triples extracted")

    log.info(f"\nTotal triples: {len(all_triples)}")

    # ─── Build graph + encode + save ──────────────────────────────────────────
    log.info("")
    log.info("Building graph...")
    G = build_graph(all_triples)
    log.info(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    log.info("Computing walk encoding...")
    log.info("Computing triples encoding...")

    log.info("")
    log.info("=== TOP 10 NODES BY DEGREE ===")
    degree_seq = sorted(G.degree(), key=lambda x: -x[1])
    for node, deg in degree_seq[:10]:
        log.info(f"  {node!r:<50} degree={deg}")

    stats = save_outputs(all_triples, G, sections)

    log.info("")
    log.info("=== FINAL STATS ===")
    for k, v in stats.items():
        log.info(f"  {k}: {v}")

    log.info("")
    log.info("Outputs written to: %s", OUTPUT_DIR)
    print("\n" + "=" * 60)
    print("VALUES GRAPH BUILD COMPLETE")
    print("=" * 60)
    print(f"\nSections processed ({len(sections)}):")
    for s in sections:
        print(f"  [{s['line_count']:2d} items]  {s['name']}")
    print(f"\nTriple extraction:")
    print(f"  Pass 1 (item-level): {stats['triples_pass1_item']}")
    print(f"  Pass 2 (cross-cutting): {stats['triples_pass2_cross_cutting']}")
    print(f"  Pass 3 (threads): {stats['triples_pass3_document_threads']}")
    print(f"  Total: {stats['triples_total']}")
    print(f"\nGraph stats:")
    print(f"  Nodes: {stats['nodes']}")
    print(f"  Edges: {stats['edges']}")
    print(f"  Components: {stats['components']} (largest: {stats['largest_component']} nodes)")
    print(f"  Density: {stats['density']}")
    print(f"\nTop 10 nodes by degree:")
    for node, deg in degree_seq[:10]:
        print(f"  {node!r:<50} {deg}")
    print(f"\nOutputs:")
    print(f"  {OUTPUT_DIR / 'triples.json'}")
    print(f"  {OUTPUT_DIR / 'walk_encoding.txt'}")
    print(f"  {OUTPUT_DIR / 'triples_encoding.txt'}  ← use this for injection (Pharos)")
    print(f"  {OUTPUT_DIR / 'stats.json'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
