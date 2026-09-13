# Topology Injection

**Status: paused, not finished (as of 2026-06-15).** This experiment produced a real result and an open question about what to do with it — see "Where this stands" below. It is not a finished study and nothing here should be read as a settled conclusion.

## What this is testing

Whether injecting a knowledge graph's *structure* into a model's KV cache — not just its text — changes how a model reasons about a topic, rather than only what it can recall. The comparison is three-way: a model with nothing injected (A), a model with the same content pasted into its prompt as text (B), and a model with the graph injected directly into the KV cache (C).

## What's verified

- **The injection mechanism works.** `mlx_kvpack.py` reliably injects KV cache content on Qwen2.5-7B and Llama-3.1-8B. Multi-hop graph traversal that isn't stated explicitly in the source text — e.g. a 3-hop path from "politics" to "labour" — is recovered correctly (C=1.00).
- **One architecture is confirmed incompatible.** Gemma-3's alternating local/global attention layers don't hold injected content in the local layers; injection is only reliable in the global layers, and full runs show the model performing at or near baseline. This isn't a bug to fix — it's ruled out.
- **Encoding format matters.** An early "walk" encoding (graph as a narrative-style document) caused the model to confuse text proximity with graph proximity, producing confident wrong answers on questions about what's *not* connected. Switching to explicit triples (`subject | predicate | object`) removed that failure mode.

## What's exploratory / not yet concluded

- **The disposition experiment** — whether injection changes the model's *reasoning frame*, not just its recall — has run (14 probes across two graphs) but the qualitative coding of those results is still pending. The session log describes some promising-looking shifts (e.g. a model reasoning in relational terms rather than checklist terms), but that's an observation from reading transcripts, not a coded finding yet.
- **The two-layer architecture idea** — that KV injection sets a ceiling on what content is *accessible*, and the system prompt's vocabulary determines how close a given query gets to that ceiling — is a working hypothesis drawn from one experiment's pattern, not a confirmed result. It hasn't been tested directly (that would need a fourth condition: injection + activation-primed prompt).
- **Isolating injection from training data.** The Haraway graph is content the model already knows from training, which makes it hard to tell whether a good answer comes from the injection or from prior knowledge. A separate graph built from novel content (referred to in the logs as "Touchstone") was built specifically to control for this, but results there are also still uncoded.

## What's not done

- No downstream integration has been attempted. The session log names three places this could matter (Reframe's framework library, the relational memory architecture, a hypothetical "librarian" retrieval agent) — these are noted as directions worth considering, not work in progress.
- Only two model families have been tested at one parameter scale (7-8B). Nothing here speaks to whether this holds at other scales.

## Where this stands

The experiment reached a real, if partial, result — but not yet a stopping point in the way "finished" would imply. The open decision right now is less "what's the next probe" and more: does the two-layer finding (if it holds up under coding) matter enough to start shaping how you build things now, or does it need more experimental grounding first before it's worth acting on. That's a judgment call, not something the data alone settles.

## Where to look for detail

- `docs/session_log.md` — current state, read this first each session
- `docs/logs/run_history.md` — raw per-probe numbers behind the summary above
- `docs/lib_labs_findings.md` — findings from a related external project (Project Mnemosyne's KV knowledge-packs work) that this experiment's design responds to and diverges from

Note: the top-level `research/CLAUDE.md` file's description of this project ("directory created, waiting on Thomas") is out of date — it describes the state before any of the above was built. Worth updating separately.
