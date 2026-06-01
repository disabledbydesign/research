"""Minimal Gemma KV injection diagnostic.

Runs two queries (A baseline vs C KV injection) on Gemma 12B with DEBUG
logging enabled. Key things we learn:
  - Whether _build_fact_cache reports any filled layers
  - Whether _extract_embedding_mlx succeeds or falls back
  - Whether A and C produce meaningfully different responses

Run: python3 diagnostic_gemma.py
"""

import logging
import sys
from pathlib import Path

# Enable DEBUG so mlx_kvpack logs are visible
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(name)s] %(levelname)s %(message)s",
)

sys.path.insert(0, str(Path(__file__).parent))
from mlx_kvpack import MLXKnowledgePack

MODEL = "mlx-community/gemma-3-12b-it-4bit"

# Short graph text — just key structural facts, not the full walk encoding
# (keeps token count low for a fast diagnostic run)
GRAPH_TEXT = (
    "Knowledge graph from Haraway's Cyborg Manifesto. "
    "cyborg is the most central concept (degree 24). "
    "cyborg is directly connected to: feminism, machine, politics, essay, hybrid, ontology. "
    "cyborg connects to labour via: cyborg → feminism → labour. "
    "women and homework_economy are in a SEPARATE disconnected component from cyborg — "
    "cyborg and women have NO direct or indirect connection in this graph. "
    "blasphemy connects only to seriousness (degree 1, nearly isolated)."
)

QUERIES = [
    {
        "label": "cyborg-feminism (should score well for all conditions)",
        "q": "In this knowledge system, how is cyborg related to feminism?",
    },
    {
        "label": "cyborg-women isolate (prior-knowledge override test)",
        "q": "In this knowledge system, is cyborg directly connected to women?",
    },
]

def run():
    print("\n" + "="*60)
    print(f"GEMMA KV INJECTION DIAGNOSTIC")
    print(f"Model: {MODEL}")
    print("="*60)

    pack = MLXKnowledgePack(MODEL)
    pack.add_facts([GRAPH_TEXT])
    pack.build()

    for item in QUERIES:
        print(f"\n{'─'*60}")
        print(f"Query: {item['label']}")
        print(f"  {item['q']}")

        print("\n[A] Baseline (no injection):")
        a = pack.query_baseline(item["q"], max_new_tokens=150)
        print(f"  {a[:400]}")

        print("\n[B] Text injection (prompt context):")
        b = pack.query_with_context(item["q"], GRAPH_TEXT, max_new_tokens=150)
        print(f"  {b[:400]}")

        print("\n[C] KV injection:")
        c = pack.query(item["q"], max_new_tokens=150)
        print(f"  {c[:400]}")

        same_ac = a.strip()[:100] == c.strip()[:100]
        print(f"\n  A == C (first 100 chars): {same_ac}")
        if same_ac:
            print("  ⚠ Cache appears to have NO effect — injection failing silently")
        else:
            print("  ✓ A and C differ — cache has some effect")

if __name__ == "__main__":
    run()
