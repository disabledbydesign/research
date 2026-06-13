"""Interactive chat with KV-injected graph knowledge.

Lets you talk to a model under three conditions and switch between them in real time
to explore what graph injection actually changes about the model's reasoning.

Usage:
    python3 chat_with_graph.py
    python3 chat_with_graph.py --graph touchstone
    python3 chat_with_graph.py --graph haraway --encoding triples
    python3 chat_with_graph.py --model mlx-community/Meta-Llama-3.1-8B-Instruct-4bit

Commands during chat:
    /mode a        — baseline: no graph, model's training data only
    /mode b        — text injection: graph pasted into system prompt
    /mode c        — KV injection: graph pre-computed into KV cache
    /mode          — show current mode
    /compare       — run next message in all three modes side by side
    /explain       — explain what each mode does and what we're testing
    /status        — show current graph, encoding, model
    /quit          — exit
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

BASE_DIR = Path(__file__).parent

GRAPH_CONFIGS = {
    "haraway": {
        "dir": BASE_DIR / "haraway_graph_v2",
        "label": "Haraway — Cyborg Manifesto",
        "description": "750-node knowledge graph from paragraph-level extraction of Haraway's Cyborg Manifesto",
    },
    "touchstone": {
        "dir": BASE_DIR / "touchstone_graph",
        "label": "Touchstone #1 — Relational Ontology Critique",
        "description": "Knowledge graph from the Relational Ontology Critique touchstone (novel content, not in training data)",
    },
}

DEFAULT_MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"

MODE_LABELS = {
    "a": "A — Baseline (training data only)",
    "b": "B — Text injection (graph in system prompt)",
    "c": "C — KV injection (graph pre-computed in KV cache)",
}

COLORS = {
    "a": "\033[90m",      # gray
    "b": "\033[34m",      # blue
    "c": "\033[32m",      # green
    "reset": "\033[0m",
    "bold": "\033[1m",
    "yellow": "\033[33m",
    "dim": "\033[2m",
    "cyan": "\033[36m",
}

EXPLAIN_TEXT = """
How KV cache injection works — without the metaphor:
────────────────────────────────────────────────────

Normal generation:
  You write a prompt → model reads every token → generates response.
  Everything it knows comes from (a) training weights + (b) current prompt.

With KV injection (Condition C):
  Before your prompt is processed, we pre-compute the model's internal
  representation of the graph content and inject it as a "fake prefix" —
  a block of key-value vectors that the model's attention mechanism treats
  as if it had just read the graph.

  K (key) vectors = fingerprints of each concept at each attention layer
  V (value) vectors = content retrieved when a key matches

  When the model generates a response, its attention heads can "look up"
  injected keys. If your question activates relevant keys, the model
  retrieves the associated values from the injected graph.

Condition B is the control:
  The same graph content is pasted into the system prompt. The model reads
  it as regular text. This tests whether any improvement comes from the
  content itself (B) or from the pre-computed representation (C).

What we actually don't know:
  Whether C does something structurally different from B is an empirical
  question. For Haraway recall tasks, C > B — the model correctly traces
  paths that B confabulates. For disposition (does reasoning *change*?),
  we don't know yet.

Encoding format matters more than we expected:
  Walk encoding ("Node X connects to: Y (0.8), Z (0.6)...") embeds
  proximity signals that the model treats as graph-proximity — but adjacent
  nodes in the walk document aren't always actually adjacent in the graph.
  This caused structured confabulation on absence queries.

  Triples encoding ("X | argues_for | Y") is one explicit statement per line.
  No proximity artifacts. The Pharos paper (2026-06) found this significantly
  outperforms walk encoding.

Try /compare on something ambiguous — that's the fastest way to see
whether injection is doing anything beyond the training data.
"""


def colored(text: str, *keys: str) -> str:
    prefix = "".join(COLORS[k] for k in keys)
    return f"{prefix}{text}{COLORS['reset']}"


def normalize_entity(e: str) -> str:
    n = re.sub(r"\s+", "_", e.strip().lower())
    return re.sub(r"^[_\-]+|[_\-]+$", "", n)[:60]


def load_graph(graph_name: str, encoding: str) -> tuple[str, str]:
    """Load graph content and return (graph_text, natural_text).

    graph_text  — the raw encoding (walk or triples)
    natural_text — graph_text prepended with a structural summary
    """
    config = GRAPH_CONFIGS[graph_name]
    graph_dir = config["dir"]

    if not graph_dir.exists():
        print(colored(f"\nGraph directory not found: {graph_dir}", "a", "bold"))
        print(colored("The touchstone graph hasn't been built yet.", "a"))
        print(colored("Run: python3 build_touchstone_graph.py", "dim"))
        sys.exit(1)

    enc_file = "triples_encoding.txt" if encoding == "triples" else "walk_encoding.txt"
    enc_path = graph_dir / enc_file
    if not enc_path.exists():
        # Fall back to the other encoding
        fallback = "walk_encoding.txt" if encoding == "triples" else "triples_encoding.txt"
        fallback_path = graph_dir / fallback
        if fallback_path.exists():
            print(colored(f"  Note: {enc_file} not found, using {fallback}", "yellow"))
            enc_path = fallback_path
        else:
            print(colored(f"  Error: no encoding file found in {graph_dir}", "a"))
            sys.exit(1)

    graph_text = enc_path.read_text()

    # Build natural-language summary from stats + graph structure
    stats_path = graph_dir / "stats.json"
    triples_path = graph_dir / "triples.json"

    if stats_path.exists():
        stats = json.loads(stats_path.read_text())
        n_nodes = stats.get("nodes", "?")
        n_edges = stats.get("edges", "?")
        n_comps = stats.get("components", "?")
    else:
        n_nodes = n_edges = n_comps = "?"

    # Top nodes by degree from triples
    top_nodes_str = ""
    if triples_path.exists():
        import networkx as nx
        triples = json.loads(triples_path.read_text())
        G = nx.Graph()
        for t in triples:
            s, o = normalize_entity(t["s"]), normalize_entity(t["o"])
            if s and o and s != o and len(s) > 1 and len(o) > 1:
                if G.has_edge(s, o):
                    G[s][o]["weight"] = G[s][o].get("weight", 0.5) + 0.1
                else:
                    G.add_edge(s, o, weight=0.5)
        degree_seq = sorted(G.degree(), key=lambda x: -x[1])
        top5 = [(n, d) for n, d in degree_seq[:5]]
        top_nodes_str = "\n".join(f"- {n} (degree {d})" for n, d in top5)

    label = config["label"]
    summary_parts = [
        f"Knowledge graph — {label}.",
        f"Graph size: {n_nodes} concepts, {n_edges} relationships, {n_comps} connected components.",
    ]
    if top_nodes_str:
        summary_parts.append("Most central concepts:")
        summary_parts.append(top_nodes_str)

    natural_text = "\n".join(summary_parts) + "\n\n" + graph_text

    return graph_text, natural_text


def run():
    parser = argparse.ArgumentParser(description="Chat with KV-injected graph knowledge")
    parser.add_argument(
        "--graph",
        default="haraway",
        choices=list(GRAPH_CONFIGS),
        help="Which knowledge graph to inject (default: haraway)",
    )
    parser.add_argument(
        "--encoding",
        default="walk",
        choices=["walk", "triples"],
        help="Encoding format: walk (default) or triples (Pharos-preferred, fewer artifacts)",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"MLX model (default: {DEFAULT_MODEL})",
    )
    args = parser.parse_args()

    config = GRAPH_CONFIGS[args.graph]

    print(colored("\n=== Graph Chat ===", "bold"))
    print(f"Graph:    {config['label']}")
    print(f"Encoding: {args.encoding}")
    print(f"Model:    {args.model}")
    print(colored(f"\n{config['description']}", "dim"))
    print()
    print("Modes:  /mode a (no injection)  /mode b (text in prompt)  /mode c (KV injection)")
    print("        /compare — run all three modes on next message")
    print("        /explain — how KV injection works (no metaphor)")
    print("        /status  — current graph/encoding/model")
    print("        /quit    — exit\n")

    print(colored("Loading graph...", "yellow"))
    graph_text, natural_text = load_graph(args.graph, args.encoding)
    enc_lines = len(graph_text.split("\n"))
    print(colored(f"Loaded {enc_lines} lines ({args.encoding} encoding).", "dim"))

    from mlx_kvpack import MLXKnowledgePack

    print(colored("Building KV pack (pre-computing injection)...", "yellow"))
    pack = MLXKnowledgePack(args.model)
    pack.add_facts([natural_text])
    pack.build()
    print(colored("Ready.\n", "yellow"))

    current_mode = "c"
    compare_next = False

    print(colored(f"Active mode: {MODE_LABELS[current_mode]}", "cyan"))
    print(colored("Tip: try /compare on a question to see what each mode does differently.\n", "dim"))

    while True:
        try:
            user_input = input(colored("You: ", "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            parts = user_input.split()
            cmd = parts[0].lower()

            if cmd == "/quit":
                break

            elif cmd == "/mode":
                if len(parts) == 1:
                    print(colored(f"Mode: {MODE_LABELS[current_mode]}", "cyan"))
                elif parts[1] in ("a", "b", "c"):
                    current_mode = parts[1]
                    print(colored(f"Switched to: {MODE_LABELS[current_mode]}", "cyan"))
                else:
                    print("Usage: /mode [a|b|c]")

            elif cmd == "/compare":
                compare_next = True
                print(colored("Next message runs in all three modes side by side.", "cyan"))

            elif cmd == "/explain":
                print(EXPLAIN_TEXT)

            elif cmd == "/status":
                print(colored(f"\nGraph:    {config['label']}", "cyan"))
                print(colored(f"Encoding: {args.encoding}", "cyan"))
                print(colored(f"Model:    {args.model}", "cyan"))
                print(colored(f"Mode:     {MODE_LABELS[current_mode]}", "cyan"))
                print(colored(f"Graph lines: {enc_lines}", "dim"))
                print()

            else:
                print(f"Unknown: {cmd}. Commands: /mode /compare /explain /status /quit")
            continue

        # Generate response(s)
        if compare_next:
            compare_next = False
            print(colored("\n── A  B  C compare ────────────────────────────────────", "yellow"))

            resp_a = pack.query_baseline(user_input, max_new_tokens=300)
            print(f"\n{colored('[A — no injection]', 'a', 'bold')}")
            print(resp_a.strip())

            resp_b = pack.query_with_context(user_input, natural_text, max_new_tokens=300)
            print(f"\n{colored('[B — text in prompt]', 'b', 'bold')}")
            print(resp_b.strip())

            resp_c = pack.query(user_input, max_new_tokens=300, temp=0.0)
            print(f"\n{colored('[C — KV injection]', 'c', 'bold')}")
            print(resp_c.strip())
            print(colored("────────────────────────────────────────────────────\n", "yellow"))

        else:
            if current_mode == "a":
                resp = pack.query_baseline(user_input, max_new_tokens=400)
            elif current_mode == "b":
                resp = pack.query_with_context(user_input, natural_text, max_new_tokens=400)
            else:
                resp = pack.query(user_input, max_new_tokens=400, temp=0.0)

            label = MODE_LABELS[current_mode]
            color = current_mode
            print(f"\n{colored(f'[{label}]', color, 'bold')}")
            print(resp.strip())
            print()


if __name__ == "__main__":
    run()
