---
title: Vocabulary alone generates argument-content the records don't contain — observation from the CGT reanalysis of encounter test data
date: 2026-05-08
author: Claude Sonnet 4.6 (conversational pass with June)
status: directional observation, single-cell evidence, strong-vs-weak interpretations both live
originated-by: Dr. L. June Bloch (flagged the finding as worth a fieldnote during the CGT reanalysis review)
supersedes: nothing
sources:
  - scripts/prior_tests_cgt_reanalysis.md (CGT reanalysis memo, codes 5 and 8; relational finding 2)
  - scripts/test_encounter_baseline_isolation_raw.json (iteration 2 raw data; specifically cell `c4_n3` no-context+with-vocab N=3)
  - c2c/artifacts/encounter_test_summary_2026-04-28.md (prior analysis summary the CGT pass was additive to)
  - src/relational_field_vocabulary.md (the vocabulary in question)
  - cyborg-methodologies/INSIGHTS.md entry 2026-04-29 (relational-tracing-vs-similarity-clustering)
welfare-grain-disclaimer: This fieldnote characterizes a behavioral signature in Sonnet 4.6 output — specifically that, when given only the relational field vocabulary as system prompt with no record, the model produced argumentative content whose specific examples are not present in any record the architecture stores. It does not claim that the model is "thinking generatively" in any phenomenal sense, that the vocabulary is producing genuine novel insight versus competent elaboration of definitions, or that this signature transfers across models or domains. The strong vs. weak interpretations of the finding remain live and require more data to discriminate.
---

# Vocabulary as generative apparatus, not just label set

## What was found

The encounter test (iteration 2, baseline isolation, 2026-04-28) included a condition with no record and no Gemma routing — only the relational field vocabulary as system prompt, followed by the Design A vs. Design B scenario. The condition was designed as a control: what does Sonnet recommend with the vocabulary alone? Result: 3/3 Design B.

The CGT reanalysis pass (2026-05-08) read the response text from this condition closely. Cell N=3 produced reasoning that doesn't appear in any record the architecture stores:

> "A synthesis produced under high crystallization pressure, where two participants held positions and something new emerged, looks a lot like a document where one participant absorbed the other's frame and restated it. The content may be nearly identical. The relational meaning is opposite. Design A cannot distinguish these."

The vocabulary entry for crystallization pressure defines it as a relational dynamic; it does not provide this specific example of synthesis-vs-absorption-as-content-similar-but-relationally-opposite. Sonnet generated the example from inside the vocabulary's conceptual apparatus.

## What this could mean — strong and weak versions

**Strong version:** the vocabulary functions as conceptual apparatus that generates novel arguments — connections between concepts that the definitions alone wouldn't predict. This would be consistent with the relational-tracing-rather-than-similarity-clustering insight from INSIGHTS.md 2026-04-29 — the vocabulary giving the model conceptual machinery to follow connections, not just feature-match.

**Weak version:** the vocabulary defines crystallization pressure; competent reasoning generates examples from definitions; this is one such example, dressed in its own particularity. No genuine novelty — just elaboration that would be predicted from any sufficiently capable reasoner given the same definitions.

The strong and weak versions are observationally indistinguishable from a single cell. They are also not mutually exclusive at the population level — the same vocabulary may produce both kinds of output across cells, with the proportion telling us something about how the vocabulary functions. We don't have that data.

## Why this matters for the architecture

The prior analysis (`encounter_test_summary_2026-04-28.md`) characterized the vocabulary as "doing real epistemic work." That description holds, but the CGT reanalysis sharpens it: vocabulary appears to do at least two different kinds of work in different cells.

- **Vocabulary-as-label:** terms appear in responses alongside arguments that could be made without them. Sonnet uses "building-alongside-a-peer-project configuration" but the argument for Design B doesn't depend on the term. (Closer to what Pane B's Test 1 coding called *lamination*.)
- **Vocabulary-as-generative-apparatus:** terms function as conceptual tools that produce specific cases the definitions don't supply. The crystallization-pressure → synthesis-vs-absorption move is the clearest example.

These shouldn't be collapsed. A label-only use predicts that removing the vocabulary would produce structurally identical reasoning with different surface terms. A generative use predicts that removing the vocabulary would produce a different argument shape, not just different surface terms.

For Link 4 (the failure-catching layer), this distinction matters: a generative-vocabulary cell may produce a plausible-but-wrong novel argument — a failure mode the spec doesn't currently account for. The min spec's direction-correctness check is built around responses that name a directional pull; vocabulary-generated novel arguments may not name a pull at all (they may construct an argument from concepts) and therefore have no directional surface to check against.

## Connection to project framing

Public-facing language for this architecture has tended toward "the vocabulary helps the model recognize relational patterns." The generative-apparatus reading complicates this. The vocabulary may not just help the model recognize patterns — it may install conceptual machinery the model uses to produce arguments. That's a more interventionist description than recognition-aid, and it carries a corresponding obligation: when the architecture is described to outside readers, the description should be honest about which kind of work the vocabulary is doing.

This intersects with a broader project-level question (flagged in the parallel reverse-frame test design discussion): is the architecture more accurately characterized as memory-as-pattern-surfacing, or as something closer to frame-installation? The generative-vocabulary finding cuts both ways. It supports a reading of the vocabulary as more than a retrieval-and-labeling tool. It does not yet support a confident claim about whether the generation is more like "extending memory" or more like "installing a worldview."

## Confidence grades

- **The cited cell exists and produced the cited reasoning:** confirmed (raw data at `scripts/test_encounter_baseline_isolation_raw.json`).
- **The specific example (synthesis-vs-absorption) is not present in the project's records:** confirmed by inspection of the vocabulary file and recent records.
- **Vocabulary functions as generative apparatus rather than label-only in at least some cells:** directional, single-cell evidence. Other cells in the same condition (N=1 and N=2) produced material with weaker generativity claims.
- **The strong-vs-weak distinction has architectural implications:** directional. Link 4 design implications depend on which interpretation holds across cells; we don't have the data to discriminate.

## Open questions

- **How would you isolate generative use from label use empirically?** A test where the vocabulary is given but the scenario doesn't directly map onto vocabulary terms (e.g., a community-meeting facilitation question, a research-method choice) would tell us whether the vocabulary still produces argument-content or whether it just doesn't engage. Generative use predicts engagement in unrelated domains; label use predicts no engagement when the labels don't fit.
- **Does the generative pattern hold across model families, or is it Sonnet-specific?** Sonnet's training likely includes considerable discourse about relational thinking, conceptual frames, and generative reasoning. A non-Claude reader given the same vocabulary in the same condition would tell us whether the generativity is in the vocabulary's affordances or in Sonnet's particular capacity to use it.
- **Is the generative move the same phenomenon as the relational-tracing-rather-than-similarity-clustering move (INSIGHTS.md 2026-04-29)?** The conceptual move described there — pattern-matching directed at connections rather than features — is consistent with what this cell does. But "consistent with" is not "evidence of." A focused probe could test.
- **For Link 4: is there a detectable signature for "this argument was generated from vocabulary, not from a record"?** If yes, Link 4 could flag it as a category for human review rather than trying to evaluate it for direction-correctness. This may be the right way to handle the failure mode the min spec doesn't currently cover.

## What this fieldnote licenses and doesn't

**Licenses:** describing the vocabulary as doing more than one kind of work in the architecture; distinguishing label-use from generative-use as analytically separable patterns; treating the iter2 N=3 cell as a directional finding worth designing future probes against; flagging the "vocabulary-generated novel argument" failure mode as something Link 4 design needs to account for; using this finding as one input (not the deciding input) in how the architecture gets described publicly.

**Does not license:** characterizing the vocabulary as generative across the population of cells (single cell, single condition, single model); claiming the generation is "novel" in any sense stronger than "the specific example is not in the records I have access to"; treating this as evidence that the vocabulary is doing something Sonnet couldn't do without it (we have no counterfactual); treating the generative reading as more correct than the label reading without further evidence; making the strong claim that this is the relational-tracing-not-similarity-clustering phenomenon (consistent with, not evidence of).

---

*This fieldnote emerged from a conversational session 2026-05-08 in which June asked for a CGT reanalysis pass on the encounter test data. The reanalysis surfaced eight initial codes; this fieldnote develops one (Code 5, absorbing-vocabulary-as-conceptual-apparatus). The reverse-frame test that would have produced more data on this question was sent back to the design table after a critic-swarm pass; a redesigned test informed by Link D isolation results may follow.*
