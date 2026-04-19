# V-JEPA and Predictive Architectures for Knowledge Systems

**Primary sources**:  
- LeCun 2022 world model paper: https://openreview.net/pdf?id=BZ5a1r-kVsf  
- I-JEPA (CVPR 2023): https://arxiv.org/abs/2301.08243  
- V-JEPA (Feb 2024): https://openreview.net/forum?id=WFYbBOEOtv  
- V-JEPA 2 (June 2025): https://arxiv.org/abs/2506.09985  
- WKM (NeurIPS 2024): https://arxiv.org/abs/2405.14205  
- Friston free energy principle: https://pmc.ncbi.nlm.nih.gov/articles/PMC2666703/  
**Date assessed**: 2026-04-15

---

## What JEPA actually is

**Joint Embedding Predictive Architecture** — a self-supervised learning method that predicts the *representation* of masked regions from the representation of visible context. Critically: it predicts in **embedding space**, not pixel/data space.

The key distinction from generative models (MAE, GPT): generative models reconstruct raw data (pixels, tokens) and must model every irrelevant detail. JEPA predicts semantic representations — what's conceptually there, not photographically. This is LeCun's core thesis: intelligence requires operating in representation space, not data space.

**The family**:
- **I-JEPA** (2023, CVPR): image patches masked and predicted
- **V-JEPA** (2024): spatio-temporal patches in video
- **V-JEPA 2** (2025): scaled to 1M+ hours of video; includes action-conditioned world model (V-JEPA 2-AC); deployed zero-shot on Franka robots with ~80% success on pick-and-place
- **LLM-JEPA** (2025, arXiv:2509.14252): applies JEPA objectives to LLM training; early but promising
- **VL-JEPA** (2024, arXiv:2512.10942): vision-language variant

**EBM lineage**: JEPA is formally an Energy-Based Model. The energy function is prediction error between the predicted embedding and the actual target embedding. Non-contrastive collapse prevention: the target encoder is a slowly-updating exponential moving average of the context encoder, not trained via gradients. Related to SimCLR/BYOL but without negative examples.

---

## LeCun's 6-module cognitive architecture

From "A Path Towards Autonomous Machine Intelligence" (2022):

1. **Perception** — estimates current world state from sensors
2. **World model** — predicts future world states given actions (where JEPA lives)
3. **Short-term memory** — holds current and predicted states
4. **Long-term memory** — persistent knowledge store
5. **Cost/reward** — intrinsic motivation, drives action selection
6. **Configurator** — meta-module that orchestrates all others; sets objectives and constraints for retrieval and action

**JEPA is not the whole architecture.** It's the architecture for the world model module specifically.

---

## The configurator problem — most important for PKM

The configurator is what determines *what the system is currently trying to do*, setting objectives for all other modules. Applied to PKM:

Current PKM systems (MemGPT, GraphRAG, Zep, A-MEM, all of them) retrieve based on query similarity with no model of task context. They don't know whether you're doing a literature review, writing a methodology section, or brainstorming a new direction.

A configurator-aware PKM would know: "right now you're revising the argument in section 3.2 of this paper, which means the retrieval goal is *finding challenges to the current framing*, not *finding supporting evidence*." That changes what gets retrieved.

This is architecturally unimplemented in any existing PKM system. The closest analog is kintsugi-cma's BDI governance layer — but that filters on values alignment, not task context. The configurator problem is distinct and not yet solved.

---

## Gap detection: what transfers and what doesn't

### What transfers — the structural analogy

V-JEPA asks: given what I can see, what should be in the masked region?

Applied to knowledge: given the concepts present in a knowledge graph, what concept *should* be connecting these clusters? This is the same epistemic operation: inference about the unobserved from the observed.

InfraNodus does a version of this at the graph topology level (structural holes, betweenness centrality). A JEPA-inspired enhancement would do it in **semantic embedding space**: not "there's a topological gap between these nodes" but "these two clusters of concepts have no semantic bridge concept, and here's where in the embedding space that bridge would live."

This would let the system say: "your notes on AI welfare and your notes on disability temporality are topologically connected via the concept 'recognition,' but semantically there's a gap around the question of agency and temporality that you haven't written about."

### What doesn't transfer

**The masking problem is inverted.** V-JEPA masks known positions and predicts them. In PKM, you don't know where the gaps are — finding them is the work. JEPA provides position codes; PKM must discover position codes. These are inverted problems. You can't import V-JEPA's training procedure, only the principles.

**Scale requirement.** JEPA learns representations from scratch on large datasets (1M+ hours of video). Your vault doesn't have that. The representations would need to come from a pre-trained model (e.g., a general-purpose text encoder), not from training on the vault itself.

**Abstraction vs. particularity.** V-JEPA deliberately abstracts away from texture and low-level detail — that's its strength for physical understanding. But a scholar's second brain often needs the irreducible particular: the specific word choice in a quote, the exact formulation that matters theoretically. A system that aggressively abstracts will lose exactly what critical theory depends on.

---

## Predictive coding (neuroscience counterpart)

**The core idea**: the brain generates top-down predictions about incoming sensory data. What travels up the hierarchy is not raw sensation but **prediction error** — the difference between what was expected and what arrived. Low prediction error = nothing interesting happened. High prediction error = update required.

**Free Energy Principle** (Friston, 2005–present): organisms minimize "variational free energy" (roughly: how much the world differs from the internal model). Two ways to minimize: update the model (perception/learning), or act on the world to match the model (action). This unifies perception and action under a single principle.

**Connection to JEPA**: both operate via prediction and update on mismatch. JEPA is an engineering architecture; predictive coding is a theory of biological computation. The functional analogy is genuine, but JEPA is not derived from predictive coding — LeCun's lineage runs through EBMs.

**Applied to PKM**: prediction error as a curation signal. When you add a new note that causes high prediction error against your existing knowledge model, that note is interesting — it doesn't fit, which means it's either wrong or your model is incomplete. A system that flags "this note conflicts with your existing model of topic X" is implementing predictive coding as an epistemic alert system.

No current PKM system does this. It's an open design space.

---

## WKM — the most actionable related work

**"Agent Planning with World Knowledge Model"**  
Zhu, Wang et al., NeurIPS 2024  
arXiv:2405.14205  
GitHub: https://github.com/zjunlp/WKM

Maintains two types of knowledge during agent planning:
- **Global prior task knowledge** — what the agent knows before starting a task
- **Dynamic local state knowledge** — what has changed during the current task

Uses both to guide retrieval and planning. For a second brain: the PKM knows your general scholarly orientation (global prior) and dynamically tracks what you've already covered in the current document (local state). Retrieves "notes relevant given what I already know you've addressed" rather than just "relevant notes."

This is the architecture that directly addresses the **editing scenario** identified in our retrieval scenarios: when you're revising a paper, you want the system to know what's already in the document so it retrieves what's missing, not what you've already said.

---

## Three conceptual imports for our second brain design

1. **The configurator problem**: Every retrieval should be conditioned on what you're currently trying to accomplish, not just what you queried. LeCun's configurator gives this a name and a module position. Currently unimplemented anywhere in PKM.

2. **Gap detection in representation space**: Extend InfraNodus's topological gap detection with semantic gap detection in embedding space. Concepts that are logically adjacent but have no semantic bridge. Requires embedding the vault with a pre-trained text encoder.

3. **Prediction error as a curation signal**: When a new note conflicts with the existing knowledge model, flag it. High surprise = high value, either as a correction or an extension. Implement as a lint-time comparison: "these claims are in tension — are you aware of this?"
