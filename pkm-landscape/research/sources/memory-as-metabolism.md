# Memory as Metabolism

**Source**: https://arxiv.org/abs/2604.12034
**By**: Stefan Miteski
**Type**: arXiv design paper (no implementation)
**Date**: May 2026
**Date assessed**: 2026-05-09

---

## What it is

A design proposal for personal-scale, single-user wiki-style memory systems. Reframes memory not as storage but as **metabolism** — an active process of cycling, transformation, and replacement. Memories don't sit static; they're processed, broken down, integrated, sometimes rejected.

Explicitly names the lineage it's working in: Karpathy LLM-wiki and MemPalace, both April 2026, both "personal wiki-style memory architectures" that "compile knowledge into an interlinked artifact for long-term use by a single user."

---

## Five operations (the metabolism)

- **TRIAGE** — what comes in worth holding at all?
- **DECAY** — what loses relevance over time?
- **CONTEXTUALIZE** — how does new information relate to what's already there?
- **CONSOLIDATE** — what gets merged, combined, abstracted?
- **AUDIT** — what's still trustworthy?

Supported by what the paper calls "memory gravity mechanisms" (presumably analogous to normative gravity — to verify on full read).

---

## The failure mode it names

**"Entrenchment under user-coupled drift."** When one human is the only source feeding a wiki over time, the wiki's dominant interpretations get more entrenched. New evidence that contradicts them stays minority because the centrality-protected mainstream view keeps winning. The wiki agrees with the user more and more over time, including on things the user should have updated their view on.

This is the exact failure mode "no existing benchmark captures." Direct adjacency to Bloch's normative-gravity framework: same structural condition (compression toward statistical center) at the personal-knowledge scale.

---

## The sharpest claim (the proposed fix)

**Structural path for minority positions to become majority** through "multi-cycle buffer pressure accumulation." Translation: contradictory evidence accumulates across many cycles, and at some threshold it is *architecturally guaranteed* to override the dominant interpretation. Not optional. Not LLM-judged. Structural.

This is the piece kintsugi-cma does NOT have. Kintsugi has decay (significance scoring + Fibonacci spacing) and consolidation (Stage 2 affinity clustering), but its high-significance facts are marked permanent and explicitly resist decay — there is no architectural mechanism for accumulated counter-evidence to override a permanent fact. Memory as Metabolism's pressure-accumulation is the missing piece.

---

## Implementation status

**Design only.** No code, no repo. Authors and affiliations: Stefan Miteski; affiliation not extracted from abstract.

---

## Relevance to our build

**Very high — as inspiration, not substrate.**

What it gives us:
1. **Vocabulary** for what the system already does (decay/consolidate/audit) and what it does not yet do (pressure-accumulation override).
2. **Named failure mode** ("entrenchment under user-coupled drift") that connects directly to Bloch's compression-function-across-scales framework. The personal-knowledge scale of normative gravity.
3. **A specific architectural mechanism** (multi-cycle buffer pressure accumulation) worth porting into kintsugi or the tending-loop layer.
4. **External validation** that the architecture pattern Bloch is building toward — values-governed, single-user, anti-entrenchment — is recognized as a genuine design problem in the literature, not just a personal idiosyncrasy.

What it does not give us: code, benchmarks, implementation guidance.

**Action items**:
- Read the full PDF before locking in the tending-loop design (task #8). The pressure-accumulation mechanism specifically.
- Consider citing in any paper Bloch writes about compression-function-at-personal-knowledge-scale or about the relational-memory architecture. The vocabulary alignment is genuinely useful.
- The five operations (TRIAGE / DECAY / CONTEXTUALIZE / CONSOLIDATE / AUDIT) may be a cleaner framing for the tending-loop layer than the current ad-hoc list.

---

## Open questions for fuller read

- What exactly is "memory gravity"? (Suspect it's analogous to normative gravity but need to verify.)
- The pressure-accumulation mechanism — what's the threshold? How is "centrality-protected" defined operationally?
- How does the paper handle the user's own evolving views? (i.e., is the wiki supposed to track "I used to believe X, now I believe Y" or just hold current best understanding?)
- Does it propose anything about retrieval, or only about write/update dynamics?
