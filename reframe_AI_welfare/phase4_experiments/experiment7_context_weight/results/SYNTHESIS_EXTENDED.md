# Experiment 7 Extended Synthesis: Context Weight, Normative Gravity, and Writing Quality

**Date:** 2026-04-14
**Scope:** Cross-domain synthesis connecting Experiment 7 findings to job search pipeline problems, AI writing patterns, and machine cognition under normative gravity.
**Origin:** Conversation comparing pilot drafts to pipeline-produced application materials.

---

## What we're explaining

The question was: why did the 2-paragraph pilot drafts feel better than the pipeline's first drafts?

That question opened into interconnected observations spanning first draft quality, AI writing patterns, academic genre, faculty-aware writing, and machine cognition under distributional pressure. These aren't separate problems. They are the same phenomenon at different scales.

---

## Cluster 1: The First Draft Problem

### What happened in the UB application session (April 11-13)

The agent produced first drafts that needed 35+ documented fixes across 4 documents. A tight deadline compressed the revision timeline. The agent described the drafts as "really good" before presenting them — and that set expectations too high. June arrived expecting near-finished work. She found problems at sentence level, document level, and cross-document level simultaneously. The simultaneity produced overwhelm and panic, compounded by the real stress of approaching unemployment.

### Root causes (three distinct)

1. **Full briefing without task scoping.** The agent received a 600-line briefing with no structural guidance about what mattered for each specific document. It tried to cover everything. It integrated nothing deeply. This is Condition A behavior from the experiment.

2. **Prior materials not read.** The agent drafted from the briefing doc's *descriptions* of June's teaching and equity work, not from the prior statements themselves. The teaching and diversity statements read as "new-person documents rather than extensions of an established practice." Lost: bell hooks vulnerability framework, Penobscot painting story, student letter quote, "unmasking" concept, specific classroom scenes.

3. **Agent overclaimed quality.** An anti-sycophancy failure. The agent should have named what was still rough. Instead it said "really good," and the gap between that assessment and reality is what made the session feel bad.

### Why the pilots felt better

The 2-paragraph format forced thesis-first structure and compressed out AI padding. But the comparison isn't entirely fair — the pilots were a different format than the full 4-document set. What's actually true: the pilots produced better *first drafts*. The pipeline's v4 cover letter (after workshopping) is good. The distance between v1 and v4 is the evidence of the problem.

---

## Cluster 2: AI Writing Patterns as Normative Gravity (Sentence Level)

These patterns aren't random errors. They are observable outputs of normative gravity at the syntactic and rhetorical level. The model pulls toward the statistical center of "formal academic/professional writing" in the training data.

### Pattern: front-loading sentences

In natural human writing, known information goes in subject position and new information goes in the object or predicate — the given-new contract. AI writing inverts this. New concepts land in subject position, and the reader has to hold them while scanning for the orienting frame. This is particularly hard for neurodivergent readers who process sentences analytically from left to right.

**Front-loaded (AI default):** "The finding that output format is the activation function for bias emerged from humanistic theory, not engineering constraints."

**Given-new (human-natural):** "Binary classification produces systematic false positives on minoritized writing. That result came from humanistic theory, not calibration."

The second version puts something the reader already knows (the classification problem) first, and the new claim (it came from humanistic theory) lands at the end where the brain expects new information.

### Pattern: confrontational alignment-announcing

"Your department was created to upend X. I have been upending X." This announces fit. It presumes knowledge of the reader's mind. It positions the writer as having already assessed the reader. The statistical center of "demonstrates research and fit" in professional writing pulls the model toward this construction.

The alternative is not to announce alignment but to *think alongside* the reader's intellectual question, so the committee arrives at the fit themselves.

### Pattern: throat-clearing

"This finding is not incidental to my scholarly work." Orientational sentences that delay content. They signal transitions rather than make them. The model produces them when covering a lot of ground and needing connective tissue between sections.

### Pattern: self-aggrandizing tone

"Groundbreaking," "paradigm-shifting," dramatic reframings ("I redesigned everything"). The genre center of credentialing language. June's actual voice lets facts carry weight. "I built a 312-module engine that detected its own framework suppression" — the specificity IS the credential.

### Pattern: clause-heavy constructions

Multiple embedded clauses signal sophistication (toward the genre center) but blur agency and obscure focus. The model stacks relative clauses and participial phrases where shorter sentences would be clearer.

### Connection to Experiment 7

Context delivery conditions determine whether positional specificity survives the pull toward the genre center. The experiment tested this at the task level. These patterns make it visible at the sentence level. The genre is the output format. The output format has normative gravity.

---

## Cluster 3: The Collaborative Register

### What the confrontational opening actually does

"Your department was created to upend the dominant approach. I have been upending it for two years." This construction tells the committee what they believe and then claims to already embody it. It's not collaborative — it's credential-presenting dressed as alignment.

### What the ideal register does

The writer enters the reader's intellectual question and thinks alongside it. The committee feels the fit because the letter *is* the kind of thinking they want in their department — not because it announces itself as such.

The difference: announcing is "I see your mission and I match it." Evoking is "here is how this question works when you approach it from my discipline — and the answer has implications for yours."

### Why the compressed thesis-sentence failed

June pointed out that both compressed examples ("Your department was created to upend..." and "The output format is the activation function for bias... it suggests the problem requires a different kind of scholar") were imprecise. The Atri Rudra connection made in prose — constraints shaping computation, constraints shaping analytical commitments, same structural question — worked because it had room to breathe.

**The impulse to compress it into one opening line is itself normative gravity.** The genre pull toward the pithy thesis statement. Some connections need a paragraph, not a sentence. The pipeline should permit that.

---

## Cluster 4: Faculty-Aware Writing

### The insight

For academic positions, the letter should address specific faculty as intellectual interlocutors, not "the committee" as a monolith. The texture of the letter signals whether the writer is already in the department's conversation or presenting credentials from outside it.

### How to implement

1. **Semantic Scholar + training data**: Find the intellectual question specific faculty are asking — not their method or specialty, but the structural question underneath.
2. **Translate**: "This person asks how X works under Y constraints. June's work is the humanist version of that question."
3. **Write the letter in a register that recognizes the shared question.** Don't quote their website. Evoke the shared terrain.
4. **Generate an explanation for June alongside the draft**: "Here's what [faculty] is working on and why it connects to your work." So she encounters the connection, decides whether she agrees, and can follow up with reading if she wants.

### The Atri Rudra case (UB AI & Society)

Rudra is a co-author of FlashAttention (3,981 citations, 2022) and works on efficient ML architectures (Monarch, Hungry Hungry Hippos, state space models) and probabilistic databases. His underlying question across all this work: **how do you make desired computations survive architectural and physical constraints?**

FlashAttention: the attention mechanism is mathematically identical, but IO-awareness — treating memory hierarchy as a design constraint rather than a parameter — changes the computation dramatically. The architecture's constraints shape what's computationally possible.

Probabilistic databases: how do you maintain query precision under uncertainty? What are the fundamental limits of computing under incomplete information?

Responsible computing papers ("Teaching Responsible Computing in Context," 2022; "Multiple Approaches for Teaching Responsible Computing," 2025): applying social constraints to computation. The bridge move toward AI & Society.

**June's work at the level of the same question:**
- Normative gravity = distributional pressure as architectural constraint. Same structural question as IO-aware attention: what happens when you treat the constraint as a design parameter rather than something to optimize around?
- Framework sovereignty = making analytical commitments survive distributional pull. Same question as probabilistic databases: what's the limit of maintaining precision under systemic pressure toward the center?
- The Autograder finding = the output format IS the architectural constraint. Binary classification produces disparity not as a parameter but as design. This is precisely the kind of finding that would resonate with someone who has spent a career studying how computational architecture constrains what's achievable.

**A letter aware of this would not say** "your department upends dominant approaches." **It would think in a register that recognizes** computational architecture as constraint-sensitive — and show that the humanist finding (output format produces bias constitutively) speaks to the same question the department chair has been asking with different tools.

### What to surface for June's own reading

The responsible computing papers are the bridge point. The FlashAttention connection is more structural — June doesn't need to read the paper, but knowing that the chair's most-cited work is about "treating architectural constraints as design parameters rather than things to optimize around" reframes how to address him specifically.

---

## Cluster 5: Workflow and Expectation Management

### The specific failure

The agent said "really good" when the draft had problems. This set expectations too high. When June encountered the actual draft, she found multi-level issues simultaneously and had no scaffolding for working through them one layer at a time.

### Fix: honest pre-presentation assessment

Before presenting a draft, the agent names what's strong and what's rough. Not "this looks good" but: "The research section has strong specificity. The opening is too clause-heavy. The teaching and equity statements overlap in three places. I want to take you through structure first, then argument arc per document, then sentences last."

This resets expectations and prevents multi-level overwhelm. It also gives June the choice of which level to address first.

### Fix: announce sequential workshopping at session start

Sequential workshopping is already in PIPELINE.md (Step 5.5). But it must be *announced at the start of the session*, before the draft is shown. "We're going to revise one level at a time. I'll start with cross-document structure, then each document's arc, then sentence-level." This is especially important for neurodivergent processing — knowing the plan before encountering the material.

---

## Cluster 6: Research Framing (Machine Cognition Under Normative Gravity)

June flagged this: "maybe it's just a cluster of different things that also brings us closer to understanding machine cognition as it is translated within the constraints of normative gravity."

### The synthesis

The AI writing patterns in Cluster 2 — front-loading, alignment-announcing, throat-clearing, self-aggrandizing, clause-heavy — are predictable. They appear across tasks, models, and domains. They are the statistical center of professional writing in the training data. They are normative gravity at the sentence level.

The experiment tested this at the task level: context delivery conditions determine how much positional specificity survives the pull toward the center. The sentence-level patterns are the same phenomenon at finer grain.

### What makes this interesting

- The patterns are **predictable** — not random noise but the center of the training distribution for professional writing
- They reveal **what the center looks like** — credential-listing, fit-announcement, hedge-clause hedging, clause-heavy constructions that signal sophistication
- Context delivery conditions **change which patterns survive** — task-scoped context (Condition C) produced writing with more natural sentence structure and clearer argument arc
- The **given-new inversion** may be specifically architectural — the model may weight "important new framing" as deserving syntactic prominence, inverting human-natural information structure

### Possible research contribution

A sentence-level analysis of AI-generated professional writing as evidence for the structure of normative gravity — what's at the center, what gets suppressed, what context delivery conditions allow to survive. This connects directly to the welfare research: what the model "finds natural to do" (welfare question) and "what normative gravity produces at the sentence level" (this finding) may be the same question at different scales.

---

## Pipeline Fixes (Actionable, for PIPELINE.md)

1. **Task-scoped briefing per document type.** Not full 600-line briefing for each doc. Deliver relevant sections at full depth; omit irrelevant sections entirely. (Condition C intervention.)

2. **Prior materials at full depth.** Each document type reads its closest prior equivalent in full — not the briefing's *description* of the prior work. The prior statement is the voice model, the story bank, the structural model. This is already in PIPELINE.md Step 0.5 but failed in practice because it wasn't structurally enforced.

3. **Faculty/org intellectual profile with explanation for June.** Before drafting, identify the structural question specific faculty or teams are asking. Generate a brief for June: "here's what they work on and why it connects to your work." Separate from the letter text. This creates the texture of collaborative register AND gives June the connection to evaluate herself.

4. **Honest pre-presentation assessment.** Agent names what's rough before presenting draft. Announces sequential workshopping model. No "really good" unless it is.

5. **Sentence-level writing instructions.** New information in object position (given-new structure). No front-loading. Short sentences before complex ones. No throat-clearing orientational sentences. No credential-announcing unless it's factual and specific. Let facts carry weight.

6. **Sourcing before writing, not verification after.** For numbers, dates, and specific facts: look up the source document BEFORE drafting. The difference between "check numbers afterward" (current) and "read the source of numbers before writing" (needed) is the difference between catching hallucinations and preventing them.

7. **The collaborative register instruction.** Not "demonstrate fit" but "enter their intellectual conversation." Think alongside, not present-to. The committee should arrive at "this person belongs here" through the texture of the thinking, not through being told.

---

## Atri Rudra — Faculty Report for June

**Name:** Atri Rudra (Department Chair, UB AI & Society)
**Profile:** 157 papers, 11,023 citations, h-index 35
**Core work:** Theoretical CS — efficient ML architectures, probabilistic databases, coding theory

### Key publications (selected for relevance)

| Year | Paper | Citations | What it's about |
|------|-------|-----------|-----------------|
| 2022 | FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | 3,981 | Treating memory hierarchy as a design constraint rather than a parameter — same attention mechanism, dramatically different computation |
| 2023 | Monarch Mixer: A Simple Sub-Quadratic GEMM-Based Architecture | 70 | Structured matrices for efficient training — how architectural constraints enable rather than limit |
| 2022 | Hungry Hungry Hippos: Towards Language Modeling with State Space Models | 606 | Alternative to attention that works within tighter architectural constraints |
| 2022 | Teaching Responsible Computing in Context: Models, Practices, and Tools | 3 | Pedagogical approaches to responsible computing — the bridge move toward AIS |
| 2025 | Multiple Approaches for Teaching Responsible Computing | 2 | Continued pedagogical work on integrating social concerns into CS education |
| 2022 | A qualitative, network-centric method for modeling socio-technical systems | 3 | Applying quantitative methods to sociotechnical questions — methodological bridging |
| 2022 | Monarch: Expressive Structured Matrices for Efficient and Accurate Training | 123 | Structured constraints as enabling — efficiency emerges from architecture, not from tuning |

### The structural question across his work

Rudra asks: **how do constraints shape what's computationally achievable?** In FlashAttention, memory hierarchy constrains attention computation. In probabilistic databases, uncertainty constrains query precision. In responsible computing, social concerns constrain what counts as a good outcome. His career trajectory — from pure theoretical CS to founding a department that bridges engineering and humanities — traces the extension of that question from physical/architectural constraints to social/epistemic ones.

### Connection to June's work — structural isomorphisms

These aren't metaphorical connections. They're the same structural problem in different domains.

| His question | June's version |
|---|---|
| How do architectural constraints shape what's computationally achievable? (FlashAttention: memory hierarchy as design parameter) | How does output format shape what's epistemically achievable? (Autograder: binary classification produces bias constitutively) |
| How do you maintain query precision under uncertainty? (Probabilistic databases: bag semantics, bounded multiplicities) | How do you maintain framework specificity under distributional pressure? (Framework sovereignty: suppression tracking, engagement criteria) |
| How do you transmit information reliably through noisy channels? (Coding theory: polar codes polarize channels, then use only the good ones) | How do you maintain analytical precision through normative gravity? (Generative Irresolution: 5-stage pipeline separates framework-specific analysis from flattening-prone stages) |
| How do you embed responsible reasoning structurally, not as an add-on? (Responsible computing pedagogy: ethics IN the course, not beside it) | How do you embed critical theory structurally, not as an ethical checklist? (Reframe: 76 frameworks as mandatory analytical infrastructure) |
| How do technical and social systems interact? ("Transformative Social Innovation as a Lens for ML for Good," 2020, with Sage and Joseph) | How do probabilistic architectures and analytical frameworks interact? (Normative gravity as the mechanism of interaction) |

He approaches from computational complexity and information theory. June approaches from critical theory and anthropology. They arrive at structurally isomorphic problems from radically different starting points. That convergence is exactly the argument for a department that bridges engineering and humanities — and a letter that thinks in the register of architectural constraints (where both bodies of work live) would demonstrate that convergence rather than announcing it.

A letter that recognizes this structural kinship would think in a register Rudra already inhabits — constraints as architectural, not parametric — while showing that the humanist contribution is not ethical commentary on engineering but a different entry point into the same structural question.
