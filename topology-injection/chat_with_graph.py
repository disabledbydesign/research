"""Interactive chat with Qwen 7B + Haraway graph injection.

Lets you converse with the model in three modes and toggle between them,
to explore whether KV injection changes conversational reasoning, not just
fact retrieval.

Usage:
    python3 chat_with_graph.py

Commands during chat:
    /mode a    — switch to baseline (no injection)
    /mode b    — switch to text injection (graph in system prompt)
    /mode c    — switch to KV injection (graph in KV cache)
    /mode      — show current mode
    /compare   — run next question in all three modes side by side
    /quit      — exit
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mlx_kvpack import MLXKnowledgePack

MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"
GRAPH_DIR = Path(__file__).parent / "haraway_graph_v2"

GRAPH_TEXT = (Path(__file__).parent / "haraway_graph_v2" / "walk_encoding.txt").read_text()

# Prepend structural summary (same as run_haraway_experiment.py)
GRAPH_CONTEXT = (
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
    + GRAPH_TEXT
)

MODE_LABELS = {
    "a": "A — Baseline (no graph)",
    "b": "B — Text injection (graph in prompt)",
    "c": "C — KV injection (graph in KV cache)",
}

COLORS = {
    "a": "\033[90m",   # gray
    "b": "\033[34m",   # blue
    "c": "\033[32m",   # green
    "reset": "\033[0m",
    "bold": "\033[1m",
    "yellow": "\033[33m",
}


def colored(text, color):
    return f"{COLORS[color]}{text}{COLORS['reset']}"


def print_response(mode, response):
    label = MODE_LABELS[mode]
    color = mode
    print(f"\n{colored(f'[{label}]', color)}")
    print(response.strip())
    print()


def run():
    print(colored("\n=== Haraway Graph Chat ===", "bold"))
    print(f"Model: {MODEL}")
    print(f"Graph: {GRAPH_DIR.name} (753 nodes, 498 edges)")
    print("\nModes: /mode a (baseline)  /mode b (text)  /mode c (kv injection)")
    print("       /compare — run next message in all three modes")
    print("       /quit — exit\n")

    print("Loading model and building KV pack...")
    pack = MLXKnowledgePack(MODEL)
    pack.add_facts([GRAPH_CONTEXT])
    pack.build()
    print("Ready.\n")

    current_mode = "c"
    compare_next = False

    print(colored(f"Current mode: {MODE_LABELS[current_mode]}", "yellow"))
    print("Type a message to begin. Try asking about graph structure,")
    print("or just have a conversation about Haraway's ideas.\n")

    while True:
        try:
            user_input = input(colored("You: ", "bold")).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if not user_input:
            continue

        # Commands
        if user_input.startswith("/"):
            parts = user_input.split()
            cmd = parts[0].lower()

            if cmd == "/quit":
                break

            elif cmd == "/mode":
                if len(parts) == 1:
                    print(colored(f"Current: {MODE_LABELS[current_mode]}", "yellow"))
                elif parts[1] in ("a", "b", "c"):
                    current_mode = parts[1]
                    print(colored(f"Switched to: {MODE_LABELS[current_mode]}", "yellow"))
                else:
                    print("Usage: /mode [a|b|c]")

            elif cmd == "/compare":
                compare_next = True
                print(colored("Next message will run in all three modes.", "yellow"))

            else:
                print(f"Unknown command: {cmd}")
            continue

        # Generate response(s)
        if compare_next:
            compare_next = False
            print(colored("\n── Compare mode ──", "yellow"))
            for mode in ("a", "b", "c"):
                if mode == "a":
                    resp = pack.query_baseline(user_input, max_new_tokens=300)
                elif mode == "b":
                    resp = pack.query_with_context(user_input, GRAPH_CONTEXT, max_new_tokens=300)
                else:
                    resp = pack.query(user_input, max_new_tokens=300)
                print_response(mode, resp)
        else:
            if current_mode == "a":
                resp = pack.query_baseline(user_input, max_new_tokens=400)
            elif current_mode == "b":
                resp = pack.query_with_context(user_input, GRAPH_CONTEXT, max_new_tokens=400)
            else:
                resp = pack.query(user_input, max_new_tokens=400)
            print_response(current_mode, resp)


if __name__ == "__main__":
    run()
