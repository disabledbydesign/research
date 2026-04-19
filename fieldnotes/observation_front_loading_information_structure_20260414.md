# Front-Loading as Normative Gravity at the Syntax Level

**Date:** 2026-04-14
**Context:** Conversation comparing Experiment 7 pilot drafts to pipeline-produced application materials. June identified that she struggles to read AI-generated text because new concepts appear at the beginning of sentences, forcing her to hold them while scanning for orientation.

## The observation

AI-generated text inverts the given-new contract. In good English prose, known information goes in subject position and new information goes in object or predicate position — this is the information structure principle linguists call the given-new contract (also: topic-comment structure, theme-rheme). The reader orients with what they already know, then encounters the new claim at the end of the sentence where the brain expects it.

Note: this is a feature of skilled writing, not a universal property of English. Not all human writers do this naturally — it's an actively taught technique for clarity. June was taught it explicitly. The point is not that AI writing deviates from how all humans write, but that it deviates from a known principle of clear prose in a predictable, patterned way.

AI writing puts new concepts in subject position. The model treats "important framing" as deserving syntactic prominence, which produces sentences that front-load new information:

**Front-loaded (AI default):** "The finding that output format is the activation function for bias emerged from humanistic theory, not engineering constraints."

**Given-new (human-natural):** "Binary classification produces systematic false positives on minoritized writing. That result came from humanistic theory, not calibration."

The second version puts something the reader already knows (the classification problem) first. The new claim (humanistic origin) lands at the end, where the brain expects new information.

## Why this matters

This is not a random error. It is normative gravity at the syntax level. The statistical center of formal academic/professional writing in the training data rewards syntactic density and conceptual front-loading — "important" things go first. This is the distributional attractor for "sounds academic." The given-new contract is positional specificity that's costly to maintain under that pull.

June identified this as a specific processing difficulty: "I struggle to read your writing sometimes because I get stuck trying to find the first few words, only to find the connection much later in the sentence or paragraph." This is particularly acute for neurodivergent readers who process sentences analytically and sequentially — left to right, seeking orientation before processing new content.

## Connection to Experiment 7

Context delivery conditions determine whether positional specificity survives normative gravity at the task level (Experiment 7 finding). This observation extends that to the syntax level. The same mechanism operates: the model's default produces the distributional center (front-loaded academic prose), and structural interventions (voice constraints, sentence-level instructions) are required for the positional specificity (given-new structure) to survive.

## Implications

1. **For the voice-check skill**: The given-new inversion is potentially quantifiable. A sentence-level check could flag sentences where the grammatical subject introduces a concept not yet established in the preceding context. This would catch front-loading as a pattern.

2. **For pipeline writing instructions**: "New information goes at the end of the sentence, not the beginning. The subject of the sentence should be something the reader already knows." This is a concrete, teachable instruction.

3. **For the research**: If front-loading is the syntactic expression of the same normative gravity that produces generic outputs at the task level, then the "what does the model find natural to do" question (welfare research) has a syntactic signature. The training distribution's center is visible not just in what the model says but in how it structures sentences.

## Open questions

- Is front-loading consistent across models, or does it vary by model family?
- Does task-scoped context (Condition C) produce less front-loading than full-briefing context (Condition A)? If so, that would connect the syntax-level finding to the task-level finding directly.
- Is the given-new inversion specific to formal/academic register, or does it appear in casual AI writing too?
- Could front-loading frequency serve as a quantitative indicator of normative gravity's strength in a given output?
