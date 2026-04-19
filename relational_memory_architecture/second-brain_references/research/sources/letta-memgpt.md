# Letta / MemGPT — OS-Inspired Context Management

**Paper**: "MemGPT: Towards LLMs as Operating Systems" — https://arxiv.org/abs/2310.08560  
**By**: UC Berkeley, 2023  
**GitHub**: https://github.com/letta-ai/letta (16.4K stars)  
**Website**: https://www.letta.com  
**Status**: MemGPT became **Letta** in September 2024. Most mature open framework for persistent agent memory.  
**Course**: DeepLearning.AI — https://www.letta.com/blog/deeplearning-ai-llms-as-operating-systems-agent-memory

---

## Core concept: LLM as operating system

The key insight: an LLM's context window is analogous to RAM — fast, limited, expensive. External storage is analogous to disk — slow, unlimited, cheap. An operating system manages the boundary between RAM and disk; MemGPT does the same for LLM context.

The **LLM itself decides what to page in and out** — it's not a fixed retrieval algorithm. The agent can call memory functions to move content between context window and external storage.

This is the clearest conceptual model for why flat context fails: you wouldn't run a computer by loading everything from disk into RAM at once. You page what you need when you need it.

---

## Memory Blocks architecture (Letta)

Letta's current implementation uses "Memory Blocks" — structured, named memory slots:
- **Persona block**: The agent's self-model and behavioral guidelines
- **Human block**: Persistent model of the user (preferences, context, history)
- **Custom blocks**: Domain-specific named memory slots (e.g., "active projects", "theoretical commitments")

Each block is:
- **Named** — has a semantic label
- **Updatable** — the agent can modify block contents during a session
- **Typed** — blocks have defined purposes
- **Bounded** — each block has a token budget

The agent reads blocks at context load time and can modify them during the session. Changes persist across sessions.

Blog post on Memory Blocks: https://www.letta.com/blog/memory-blocks

---

## Relevance to our build

### The OS metaphor is the right frame for context management
The capacity building plan's "compile at write time, not query time" is essentially describing the same thing as Letta's paging model. The session-wrapup skill IS a "write to disk" operation. The briefing loading profiles ARE the "page in what you need" operation.

### Memory Blocks map onto loading profiles
The capacity building plan's loading profiles (relational core always loaded, detail loaded per task) can be implemented as Letta-style memory blocks:
- **Relational core block** — always in context (~7.5K tokens): through-lines, key concepts, voice characteristics
- **Task-specific blocks** — loaded per retrieval scenario: story (for drafting), publications (for job apps), etc.
- **Project state block** — current project context, open threads

This is a more formalized version of what the briefing index already does.

### What Letta doesn't solve for us
- Letta is agent-framework infrastructure, not a PKM tool. It manages context for AI agents; it doesn't organize human knowledge.
- The "human block" is a model of the user — this is relevant, but June needs the system to model her *knowledge* not just her preferences.
- Letta doesn't have the relational structure (typed connections, gap analysis) that our design requires.

---

## Key empirical result
Evaluated on:
- Document analysis over documents exceeding context windows
- Multi-session chat with persistent user modeling (Clara, a fictional therapy user)

Both outperformed flat-context approaches. The OS metaphor is empirically validated, not just conceptually compelling.

---

## The connection to what we're building

Letta's Memory Blocks + the briefing loading profiles + the session-wrapup skill are all partial implementations of the same principle. The synthesis: **design the second brain's retrieval layer as explicit Memory Blocks with defined purposes, not a flat bag of context**. Each block has a purpose, a token budget, and a loading condition.

The schema document (from Karpathy's pattern) should define these blocks. The BRIEFING_INDEX.md is already a version of this — it just needs to be extended to cover the full knowledge architecture, not just the briefing.
