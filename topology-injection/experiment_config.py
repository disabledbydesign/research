"""Configuration for graph geometry injection experiment.

This file documents the correct settings to run graph_experiment.py
on this machine. The lib labs script reads OLLAMA_URL and EXPERIMENT_MODEL
from environment variables — set those before running, or patch the module-level
constants at the top of graph_experiment.py.

Usage (from the kv-knowledge-packs directory):
    OLLAMA_URL=http://localhost:11434 EXPERIMENT_MODEL=llama3.1:8b python3 graph_experiment.py

Or import this module and use the constants below.
"""

# ---------------------------------------------------------------------------
# Ollama
# ---------------------------------------------------------------------------

# The lib labs script defaults to port 11436. Our Ollama is on 11434.
OLLAMA_URL = "http://localhost:11434"

# Best available model for queries.
# llama3.1:8b is the closest to the intended qwen3:30b-a3b in instruction
# following capability among what's locally available.
# Available models confirmed 2026-05-30:
#   llama3.1:8b       <- USE THIS (best for instruction following)
#   mistral:7b        <- fallback
#   llama3.2:3b       <- small, less reliable for graph reasoning
#   gemma3:4b
#   qwen2.5vl:3b / 7b (vision models — not appropriate here)
EXPERIMENT_MODEL = "llama3.1:8b"

# ---------------------------------------------------------------------------
# KV injection backend
# ---------------------------------------------------------------------------

# The lib labs script (graph_experiment.py conditions C and any direct KV work)
# uses kv_packs.py, which requires PyTorch/HuggingFace. On this machine (Apple
# Silicon, MLX environment) use mlx_kvpack.py instead.
#
# Injection backend (MLX, Apple Silicon):
KV_BACKEND = "mlx"
KV_BACKEND_MODULE = "mlx_kvpack"   # import MLXKnowledgePack from here
KV_BACKEND_CLASS = "MLXKnowledgePack"

# Default model for KV injection (consistent with THCoalition Qwen-based work).
# Verified working 2026-05-30 — smoke test passed, answered "The capital of
# France is Paris." correctly.
KV_MODEL = "mlx-community/Qwen2.5-7B-Instruct-4bit"

# ---------------------------------------------------------------------------
# Notes on graph_experiment.py compatibility
# ---------------------------------------------------------------------------
#
# graph_experiment.py as written runs conditions A, B, and D only — it does NOT
# include Condition C (KV text injection via Knowledge Packs). The script uses
# Ollama for all inference via query_model(), so it does NOT import kv_packs.py
# directly. This means:
#
#   - Conditions A, B, D: READY to run with env var overrides above.
#     No code changes needed.
#
#   - Condition C (KV cache injection): NOT implemented in graph_experiment.py.
#     Adding it requires: import MLXKnowledgePack from mlx_kvpack, build a
#     pack from the graph text, and run queries through pack.query() instead
#     of query_model(). This is a ~30-line addition, not a rewrite.
#
# The lib labs graph_encoder.py (adjacency, spectral, walk encoders) has no
# external dependencies beyond numpy and networkx — no import changes needed.
#
# graph_experiment.py path (lib labs):
#   /Users/june/Documents/GitHub/liberation_labs/Project-Mnemosyne/kv-knowledge-packs/graph_experiment.py
# graph_encoder.py path:
#   /Users/june/Documents/GitHub/liberation_labs/Project-Mnemosyne/kv-knowledge-packs/graph_encoder.py
# MLX adapter path:
#   /Users/june/Documents/GitHub/research/topology-injection/mlx_kvpack.py
