"""Build a topology pack (triples + walk encoding) from a markdown source text.

Pipeline:
  1. Chunk source text into ~1500-char segments
  2. Extract entity-relationship triples per chunk via local Ollama LLM
  3. Build knowledge graph from all triples
  4. Walk-encode the graph topology
  5. Save triples.json, walk_encoding.txt, stats.json

Usage:
    python build_pack.py harway_cyborg_manifesto.md
    python build_pack.py harway_cyborg_manifesto.md --model llama3.1:8b --test
"""

import argparse
import json
import logging
import re
import time
from pathlib import Path

import networkx as nx
import requests

log = logging.getLogger("build_pack")

OLLAMA_URL = "http://localhost:11434"

EXTRACT_PROMPT = """Extract entity-relationship triples from this text.
Return JSON array only. Each triple: {{"s": "subject", "p": "predicate", "o": "object"}}
Keep entities short (2-4 words). Use specific predicates (argues_for, defines, contrasts_with, requires, enables, undermines, extends, grounds, transgresses, constitutes, opposes, replaces).
Max 8 triples. Focus on conceptual and political relationships, not bibliographic or meta.
/no_think

Text: {text}

JSON:"""


def llm_extract(text: str, model: str) -> list[dict]:
    prompt = EXTRACT_PROMPT.format(text=text[:1500])
    try:
        resp = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False,
                  "options": {"temperature": 0.1, "num_predict": 800}},
            timeout=120,
        )
        if resp.status_code != 200:
            log.warning(f"Ollama returned {resp.status_code}")
            return []
        raw = resp.json().get("response", "")
        raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        start = raw.find("[")
        end = raw.rfind("]")
        if start >= 0 and end > start:
            return json.loads(raw[start:end + 1])
    except (json.JSONDecodeError, Exception) as e:
        log.debug(f"Extract failed: {e}")
    return []


def chunk_text(text: str, size: int = 1500) -> list[str]:
    # Split on paragraph breaks first, then fallback to size
    paragraphs = [p.strip() for p in re.split(r"\n\n+", text) if p.strip()]
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) < size:
            current = (current + "\n\n" + para).strip()
        else:
            if current:
                chunks.append(current)
            current = para
    if current:
        chunks.append(current)
    return chunks


def normalize(e: str) -> str:
    return re.sub(r"\s+", "_", e.strip().lower())[:50]


def build_graph(triples: list[dict]) -> nx.Graph:
    G = nx.Graph()
    for t in triples:
        s = normalize(t.get("s", ""))
        o = normalize(t.get("o", ""))
        p = t.get("p", "related_to")
        if s and o and s != o:
            if G.has_edge(s, o):
                G[s][o]["weight"] += 0.1
                G[s][o]["predicates"].add(p)
            else:
                G.add_edge(s, o, weight=0.5, predicates={p})
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
    for _ in range(1, steps + 1):
        power = power @ T
        W += power
    W /= (steps + 1)

    lines = [f"Knowledge graph topology ({len(nodes)} concepts, walk encoding):"]
    for i, node in enumerate(nodes):
        connections = [(nodes[j], W[i, j]) for j in range(len(nodes))
                       if i != j and W[i, j] > 0.01]
        connections.sort(key=lambda x: -x[1])
        top = connections[:8]
        if top:
            conn_str = ", ".join(f"{n} ({w:.3f})" for n, w in top)
            lines.append(f"Node: {node} connects to: {conn_str}")
        else:
            lines.append(f"Node: {node} connects to: (none)")
    return "\n".join(lines)


def run(source: Path, model: str, test: bool = False):
    text = source.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    log.info(f"Source: {source.name} — {len(text):,} chars, {len(chunks)} chunks")

    if test:
        chunks = chunks[:3]
        log.info("TEST MODE: running first 3 chunks only")

    all_triples = []
    for i, chunk in enumerate(chunks):
        log.info(f"  chunk {i+1}/{len(chunks)} ({len(chunk)} chars)")
        raw = llm_extract(chunk, model)
        valid = [t for t in raw if isinstance(t, dict) and "s" in t and "o" in t]
        log.info(f"    → {len(valid)} triples")
        all_triples.extend(valid)

    log.info(f"Total triples: {len(all_triples)}")

    G = build_graph(all_triples)
    encoding = walk_encode(G)

    # Save
    out_dir = source.parent / (source.stem + "_pack")
    out_dir.mkdir(exist_ok=True)

    (out_dir / "triples.json").write_text(json.dumps(all_triples, indent=2))
    (out_dir / "walk_encoding.txt").write_text(encoding)

    stats = {
        "source": source.name,
        "model": model,
        "chunks": len(chunks),
        "triples": len(all_triples),
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": nx.density(G) if G.number_of_nodes() > 1 else 0,
        "encoding_tokens_approx": len(encoding.split()),
        "test_mode": test,
    }
    (out_dir / "stats.json").write_text(json.dumps(stats, indent=2))

    log.info(f"\nDone → {out_dir}/")
    log.info(f"  {stats['nodes']} nodes, {stats['edges']} edges")
    log.info(f"  ~{stats['encoding_tokens_approx']} tokens in walk encoding")
    log.info(f"  density: {stats['density']:.4f}")
    return stats


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="[pack] %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--model", default="llama3.1:8b")
    parser.add_argument("--test", action="store_true",
                        help="Run on first 3 chunks only to verify pipeline")
    args = parser.parse_args()
    run(args.source, args.model, args.test)
