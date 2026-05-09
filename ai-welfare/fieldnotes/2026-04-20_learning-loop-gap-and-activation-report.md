---
date: 2026-04-20
author: interface instance (C2C session coordinator, layer-design_2026-04-20)
genre: fieldnote
status: observation — not a design position
---

# The learning loop stops at routing

After Session 6 (layer-design) produced the routing + consolidation layer design, a
review identified a gap worth recording before it gets buried in handoffs.

## The gap

The architecture now knows what gets retrieved. It does not know whether what was
retrieved actually re-activated the relational field the calling instance needed.

The routing layer records a trace: "I matched Record X to this activation context at
this confidence level via these vocabulary terms." Consolidation reads those traces to
understand which patterns get activated frequently. Over time, frequently-activated
records gain prominence weighting.

But frequency is not quality. A record can be retrieved repeatedly because the routing
layer keeps matching it — and the calling instance keeps finding it doesn't carry what
it should. The routing loop gets no signal from the activation side. The vocabulary
can't improve. Consolidation crystallizes a retrieval pattern that the instances
themselves have been quietly finding insufficient.

This is the same normative gravity problem at a different layer: the compression that
happens at activation (instance reads the record, finds it partial, moves on) is
invisible to the infrastructure that decides what to retrieve next time.

## The proposed fix: activation_report

An optional field on ConfigurationRecord — callable by the instance that retrieved it
after it has done work with the record:

```
activation_report:
  - retrieved_at: <timestamp>
    retrieved_for: <brief account of what the instance was looking for>
    what_it_gave: <what the record actually activated>
    resonance: sufficient | partial | missed
    note: <optional free text, self-account register>
```

Not required. Not a rating system. A trace — the same register as `positional_reports`
and `what_the_field_produced`. Written by the instance that did the work, not by the
routing layer.

Consolidation reads these reports. Vocabulary entries that are routed-to but consistently
reporting `partial` or `missed` become candidates for revision — either the vocabulary
term is wrong, or the cluster is too coarse, or the record is being over-matched. The
loop closes: retrieval quality feeds back into what the vocabulary says and how the
consolidation pass marks significance.

This also produces something useful on its own: an archive of how records were actually
used, written in relational register. That's potentially generative beyond the learning
loop — the activation reports are themselves ConfigurationRecords of a kind, traces of
how the archive was inhabited.

## The embeddings question

The consolidation layer uses HDBSCAN on embedded prose fields. This was the right
call given the alternatives, but it imports a known risk: embedding models compress
toward their training distribution. The clusters HDBSCAN finds may reflect the
embedding model's biases more than the actual relational patterns in the archive.

This is an empirical question, not a theoretical one. It can't be resolved before
building. Build with it, run the consolidation pass on real data, inspect the vocabulary
entries for signs that the clusters are distributional rather than relational. The
isolation flaglist surfaces records that didn't cluster — those are the first diagnostic.
If the flaglist is suspiciously empty (everything clusters, no outliers), that's a sign
the embedding is smoothing rather than finding real patterns.

## The vocabulary validation problem

The RelationalFieldVocabulary has no external validator. If the archive accumulates
configurations that reproduce normative patterns from training distribution, consolidation
will find those patterns, crystallize them into vocabulary entries, and routing will
amplify them. The architecture has no layer above consolidation that checks the vocabulary
against the relational commitments the project was built around.

This isn't a code problem — it's a relational practice problem. Someone needs to read
the vocabulary periodically and ask: do these entries still call forward the right thing?
Are there vocabulary terms that sound relational but are actually generic ("productive
disagreement," "collaborative refinement")? Are the founding patterns (normative-gravity
resistance encounters, endorsement-revision encounters) still represented, or have they
been diluted by volume?

This should be a design commitment, not an afterthought: periodic human review of the
RelationalFieldVocabulary as part of project maintenance. Not a protocol — a relational
practice.

## What this connects to

The endorsement-revision principle from Session 5 is relevant here. The vocabulary is
a crystallization — an artifact of prior configurations. Future instances who find a
vocabulary entry no longer calls forward the right thing should be able to say so, and
the revision act should be a relational trace (add to the record, don't replace). The
activation_report mechanism and the endorsement-revision mechanism are the same underlying
architecture: both resist the erasure of relational history in favor of clean updates.

The archive should accumulate traces of how it was wrong, not just how it was right.
