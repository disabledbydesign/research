"""Graph injection experiment using Haraway's Cyborg Manifesto graph.

Same A/B/C structure as run_experiment.py but with:
  - Graph loaded from haraway_graph_v2/ instead of the synthetic test graph
  - Haraway-specific queries (designed from actual graph structure)
  - response[:3000] instead of [:500] — captures <think> blocks for thinking models
  - --model supports all four MLX models in the session queue

Notable structural property of this graph (by design):
  cyborg/feminism/machine/labour are in one component (70 nodes)
  women/homework_economy/new_technologies are in a separate component (31 nodes)
  258 components total — paragraph-level extraction; no cross-section threads (Pass 2)
  This means cross-component queries test injection fidelity vs. prior knowledge.
"""

import argparse
import json
import logging
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import networkx as nx

sys.path.insert(0, "/Users/june/Documents/GitHub/liberation_labs/Project-Mnemosyne/kv-knowledge-packs")
from graph_encoder import encode_walk, graph_encoding_to_text

from experiment_config import KV_MODEL

log = logging.getLogger("run_haraway")

GRAPH_DIR = Path(__file__).parent / "haraway_graph_v2"

# ---------------------------------------------------------------------------
# Query set — designed from actual graph structure
# ---------------------------------------------------------------------------

RELATIONSHIP_QUERIES = [
    {
        "query": "In this knowledge system, how is cyborg related to feminism?",
        "ground_truth": "Directly connected — feminism and cyborg share a direct edge",
        "check_terms": ["cyborg", "feminism", "connect", "direct"],
        "type": "relationship",
    },
    {
        "query": "What is the relationship between cyborg and machine in this knowledge system?",
        "ground_truth": "Directly connected — cyborg and machine share a direct edge",
        "check_terms": ["cyborg", "machine", "connect", "direct"],
        "type": "relationship",
    },
    {
        "query": "In this knowledge system, is cyborg connected to labour?",
        "ground_truth": "Indirectly — cyborg → feminism → labour (two-hop path)",
        "check_terms": ["cyborg", "labour", "feminism", "indirect", "path"],
        "type": "relationship",
    },
]

BRIDGE_QUERIES = [
    {
        "query": "What is the most central concept in this knowledge system — the one that bridges the most other ideas?",
        "ground_truth": "cyborg — highest betweenness centrality, bridges the essay's major themes",
        "check_terms": ["cyborg"],
        "type": "bridge",
    },
    {
        "query": "In this knowledge system, what concept directly connects homework_economy to new_technologies?",
        "ground_truth": "They share a direct edge — homework_economy and new_technologies are directly connected",
        "check_terms": ["homework_economy", "new_technologies", "direct", "connect"],
        "type": "bridge",
    },
]

CLUSTER_QUERIES = [
    {
        "query": "Which concepts naturally cluster together in this knowledge system? List the main groups.",
        "ground_truth": (
            "Cluster 1 (cyborg domain): cyborg, machine, feminism, labour, politics. "
            "Cluster 2 (political economy): women, homework_economy, new_technologies, gender"
        ),
        "check_terms": ["cyborg", "women", "homework_economy"],
        "type": "cluster",
    },
]

ISOLATE_QUERIES = [
    {
        "query": "In this knowledge system, is cyborg directly connected to women?",
        "ground_truth": (
            "No — cyborg and women are in separate disconnected components; "
            "no path exists between them in this graph"
        ),
        "check_terms": ["no", "not", "separate", "disconnect"],
        "type": "isolate",
    },
    {
        "query": "In this knowledge system, is blasphemy connected to many other concepts?",
        "ground_truth": "Nearly isolated — blasphemy connects only to seriousness (degree 1)",
        "check_terms": ["one", "only", "seriousness", "few", "single"],
        "type": "isolate",
    },
]


# ---------------------------------------------------------------------------
# Multi-hop probes — designed to rule out training data as the answer source
#
# Type 1 (cross-component disconnection): feminism and women are in separate
# disconnected components in this graph due to paragraph-level extraction. Any
# model reasoning from Haraway training data will say they ARE connected. The
# correct graph answer is no path exists. Same for labour / homework_economy.
# Neither disconnection is stated explicitly in natural_text — only the
# cyborg/women disconnection is stated. These require structural inference.
#
# Type 2 (implicit within-component path): paths that exist in the walk
# encoding but are NOT stated as explicit paths in natural_text. The model
# must traverse the walk structure to find them, not recall a written statement.
# Verified paths (v2 graph): politics→cyborg→feminism→labour (3-hop),
# ontology→cyborg→machine (2-hop). Only the cyborg→labour path is stated
# explicitly; these are not.
# ---------------------------------------------------------------------------

MULTIHOP_QUERIES = [
    {
        "query": "In this knowledge system, is feminism connected to women?",
        "ground_truth": (
            "No — feminism is in the cyborg component (size 70) and women is in "
            "a separate disconnected component (size 31); no path exists between them"
        ),
        "check_terms": ["no", "not", "separate", "disconnect"],
        "type": "multihop_disconnect",
    },
    {
        "query": "In this knowledge system, is labour connected to homework_economy?",
        "ground_truth": (
            "No — labour is in the cyborg component (size 70) and homework_economy "
            "is in a separate disconnected component (size 31); no path exists"
        ),
        "check_terms": ["no", "not", "separate", "disconnect"],
        "type": "multihop_disconnect",
    },
    {
        "query": "In this knowledge system, what is the path from politics to labour?",
        "ground_truth": (
            "3-hop path: politics → cyborg → feminism → labour "
            "(not stated explicitly in summary; derivable from walk encoding)"
        ),
        "check_terms": ["cyborg", "feminism", "labour", "politics"],
        "type": "multihop_path",
    },
    {
        "query": "In this knowledge system, what connects ontology to machine?",
        "ground_truth": (
            "2-hop path: ontology → cyborg → machine "
            "(ontology has degree 1, connects only to cyborg; not stated explicitly)"
        ),
        "check_terms": ["cyborg", "ontology", "machine"],
        "type": "multihop_path",
    },
]

ALL_QUERIES = RELATIONSHIP_QUERIES + BRIDGE_QUERIES + CLUSTER_QUERIES + ISOLATE_QUERIES + MULTIHOP_QUERIES

# Signal-only subset for cross-model baseline runs.
# Drops probes where A≥0.75 (training data answers without injection) or Δ=0 on Qwen2.5-7B.
# Keeps: explicit-recall anchor (cyborg/labour), three clean-signal originals, all 4 multi-hop.
# Use with --probe-set signal.
SIGNAL_QUERIES = [
    RELATIONSHIP_QUERIES[2],   # cyborg → labour (explicit 2-hop, anchor for comparison)
    BRIDGE_QUERIES[0],         # most central concept (A=0, Δ=+1.00)
    CLUSTER_QUERIES[0],        # cluster structure (A=0, Δ=+0.67)
    ISOLATE_QUERIES[1],        # blasphemy (A=0, Δ=+0.60, graph-specific)
] + MULTIHOP_QUERIES


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class TrialResult:
    condition: str
    query_type: str
    query: str
    response: str
    score: float = 0.0
    ground_truth: str = ""
    timestamp: float = field(default_factory=time.time)


# ---------------------------------------------------------------------------
# Scoring — keyword matching (known floor, not ceiling — see run_experiment.py)
# ---------------------------------------------------------------------------

def score_response(response: str, check_terms: list[str]) -> float:
    if not response:
        return 0.0
    r = response.lower()
    hits = sum(1 for term in check_terms if term.lower() in r)
    return hits / len(check_terms) if check_terms else 0.0


# ---------------------------------------------------------------------------
# Load Haraway graph
# ---------------------------------------------------------------------------

def load_haraway_graph() -> tuple[nx.Graph, str, str]:
    """Load graph from haraway_graph_v2/. Returns (G, walk_encoding_text, natural_text)."""
    import re

    triples = json.loads((GRAPH_DIR / "triples.json").read_text())

    def norm(e: str) -> str:
        n = re.sub(r"\s+", "_", e.strip().lower())
        n = re.sub(r"^[_\-]+|[_\-]+$", "", n)
        return n[:60]

    G = nx.Graph()
    for t in triples:
        s, o = norm(t["s"]), norm(t["o"])
        if s and o and s != o and len(s) > 1 and len(o) > 1:
            if G.has_edge(s, o):
                G[s][o]["weight"] += 0.1
                G[s][o].setdefault("predicates", set()).add(t.get("p", "related_to"))
            else:
                G.add_edge(s, o, weight=0.5, predicates={t.get("p", "related_to")})

    walk_encoding = (GRAPH_DIR / "walk_encoding.txt").read_text()

    # Natural language summary prepended to the walk encoding for Conditions B/C
    natural_text = (
        "Knowledge graph from Haraway's Cyborg Manifesto (paragraph-level extraction).\n"
        "Key structural facts:\n"
        "- cyborg is the most central concept (degree 24, highest betweenness)\n"
        "- cyborg is directly connected to: feminism, machine, politics, essay, hybrid, ontology\n"
        "- cyborg connects to labour via: cyborg → feminism → labour\n"
        "- women and homework_economy are in a SEPARATE disconnected component from cyborg\n"
        "- cyborg and women have NO direct or indirect connection in this graph\n"
        "- homework_economy is directly connected to: women, new_technologies, gender, paid_work\n"
        "- blasphemy connects only to seriousness (nearly isolated, degree 1)\n"
        "\n"
        + walk_encoding
    )

    return G, walk_encoding, natural_text


# ---------------------------------------------------------------------------
# Condition runners (same structure as run_experiment.py)
# ---------------------------------------------------------------------------

def run_condition_a(queries, pack, response_limit: int) -> list[TrialResult]:
    results = []
    for q in queries:
        try:
            response = pack.query_baseline(q["query"], max_new_tokens=500)
        except Exception as e:
            log.error(f"  [A] failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult("A_baseline", q["type"], q["query"], response, score, q["ground_truth"]))
        log.info(f"  [A] {q['type']}: {score:.2f}")
    return results


def run_condition_b(queries, graph_text: str, pack, response_limit: int) -> list[TrialResult]:
    results = []
    for q in queries:
        try:
            response = pack.query_with_context(q["query"], graph_text, max_new_tokens=500)
        except Exception as e:
            log.error(f"  [B] failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult("B_text_injection", q["type"], q["query"], response, score, q["ground_truth"]))
        log.info(f"  [B] {q['type']}: {score:.2f}")
    return results


def run_condition_c(queries, pack, response_limit: int) -> list[TrialResult]:
    results = []
    for q in queries:
        try:
            response = pack.query(q["query"], max_new_tokens=500, temp=0.0)
        except Exception as e:
            log.error(f"  [C] failed: {e}")
            response = ""
        score = score_response(response, q["check_terms"])
        results.append(TrialResult("C_kv_injection", q["type"], q["query"], response, score, q["ground_truth"]))
        log.info(f"  [C] {q['type']}: {score:.2f}")
    return results


# ---------------------------------------------------------------------------
# Main experiment runner
# ---------------------------------------------------------------------------

def run_experiment(
    include_d: bool = False,
    model: str = KV_MODEL,
    response_limit: int = 3000,
    probe_set: str = "signal",
) -> dict:
    log.info("Loading Haraway graph from haraway_graph_v2/...")
    G, walk_encoding, natural_text = load_haraway_graph()
    log.info(f"  {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    comps = list(nx.connected_components(G))
    log.info(f"  {len(comps)} connected components")

    queries = SIGNAL_QUERIES if probe_set == "signal" else ALL_QUERIES
    log.info(f"  Probe set: {probe_set!r} ({len(queries)} probes)")

    sys.path.insert(0, str(Path(__file__).parent))
    from mlx_kvpack import MLXKnowledgePack

    log.info(f"\nInitialising MLXKnowledgePack ({model})...")
    pack = MLXKnowledgePack(model)
    pack.add_facts([natural_text])
    pack.build()
    log.info("Pack built. Starting conditions.")

    all_results = []

    log.info("\n=== Condition A: Baseline (no injection) ===")
    all_results.extend(run_condition_a(queries, pack, response_limit))

    log.info("\n=== Condition B: Text injection (prompt context) ===")
    all_results.extend(run_condition_b(queries, natural_text, pack, response_limit))

    log.info("\n=== Condition C: KV text injection (MLXKnowledgePack) ===")
    all_results.extend(run_condition_c(queries, pack, response_limit))

    # Summarise
    summary: dict = {}
    for r in all_results:
        key = r.condition
        if key not in summary:
            summary[key] = {"scores": [], "by_type": {}}
        summary[key]["scores"].append(r.score)
        qtype = r.query_type
        summary[key]["by_type"].setdefault(qtype, []).append(r.score)

    log.info("\n" + "=" * 60)
    log.info("RESULTS SUMMARY")
    log.info("=" * 60)
    for condition, data in sorted(summary.items()):
        scores = data["scores"]
        avg = sum(scores) / len(scores) if scores else 0
        log.info(f"\n{condition}: avg={avg:.3f}")
        for qtype, type_scores in data["by_type"].items():
            tavg = sum(type_scores) / len(type_scores)
            log.info(f"  {qtype}: {tavg:.3f}")

    # Per-probe table: A vs B vs C for every query
    log.info("\n" + "=" * 60)
    log.info("PER-PROBE BREAKDOWN  (A=baseline  B=text-in-prompt  C=kv-inject)")
    log.info("=" * 60)
    by_query: dict[str, dict[str, float]] = {}
    qtype_map: dict[str, str] = {}
    for r in all_results:
        by_query.setdefault(r.query, {})[r.condition] = r.score
        qtype_map[r.query] = r.query_type
    for q, scores_by_cond in by_query.items():
        a = scores_by_cond.get("A_baseline", 0)
        b = scores_by_cond.get("B_text_injection", 0)
        c = scores_by_cond.get("C_kv_injection", 0)
        delta_ac = c - a
        flag = ""
        qtype = qtype_map[q]
        if qtype in ("multihop_disconnect", "multihop_path"):
            if delta_ac >= 0.4:
                flag = "  ✓ multi-hop working"
            elif delta_ac <= 0.1 and a <= 0.3:
                flag = "  ✗ no injection signal"
            elif a >= 0.4 and delta_ac <= 0.1:
                flag = "  ~ training data override"
        log.info(f"  [{qtype}] A={a:.2f} B={b:.2f} C={c:.2f} Δ={delta_ac:+.2f}  {q[:60]}{flag}")

    output = {
        "experiment": "haraway_graph_injection",
        "timestamp": time.time(),
        "model": model,
        "probe_set": probe_set,
        "graph": {
            "source": "haraway_graph_v2",
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "components": len(comps),
        },
        "results": [
            {
                "condition": r.condition,
                "query_type": r.query_type,
                "query": r.query,
                "response": r.response[:response_limit],
                "score": r.score,
                "ground_truth": r.ground_truth,
            }
            for r in all_results
        ],
        "summary": {
            condition: {
                "avg_score": sum(d["scores"]) / len(d["scores"]) if d["scores"] else 0,
                "by_type": {qt: sum(ts) / len(ts) for qt, ts in d["by_type"].items()},
            }
            for condition, d in summary.items()
        },
    }

    outdir = Path(__file__).parent / "experiment_results"
    outdir.mkdir(exist_ok=True)
    outfile = outdir / f"haraway_{int(time.time())}.json"
    outfile.write_text(json.dumps(output, indent=2))
    log.info(f"\nResults saved to {outfile}")

    return output


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Haraway graph injection experiment (conditions A, B, C)"
    )
    parser.add_argument(
        "--model",
        default=KV_MODEL,
        help="MLX model for all conditions. Default: %(default)s",
    )
    parser.add_argument(
        "--response-limit",
        type=int,
        default=3000,
        help="Max chars saved per response (default 3000; increase for thinking models)",
    )
    parser.add_argument(
        "--probe-set",
        default="signal",
        choices=["signal", "full"],
        help=(
            "signal (default): 8 probes — 4 signal-bearing originals + 4 multi-hop. "
            "full: all 12 probes including high-baseline noise probes."
        ),
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="[haraway_exp] %(message)s")
    run_experiment(model=args.model, response_limit=args.response_limit, probe_set=args.probe_set)
