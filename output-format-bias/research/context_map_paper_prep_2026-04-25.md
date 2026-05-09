# Context Map: "The Bias Is in the Output Format"
**Generated:** 2026-04-25 — cross-repo scan by Explore subagent  
**Updated:** 2026-04-25 — data audit + workflow design  
**Purpose:** Pre-C2C briefing document. Use as context for all drafting sessions.

---

## C2C Drafting Workflow

### Pre-C2C (complete before Session 1)
- [ ] Run Biology corpus through concern-detection + synthesis-first protocol (when MLX frees; ~55 min estimate)
- [ ] Build and run binary vs. 4-axis comparison test (C2C Session 1 designs this; implement after)
- [ ] Set up project-specific Reframe config (see Reframe section below)
- [ ] June: optional manual review of 3–5 real student cases for qualitative comparison

### C2C Session 1 — Argument Audit + Test Design
**Goal:** Lock the argument and design remaining tests  
**Inputs:** This context map, synthesis_first_paper_notes.md, experiment_log.md, PRIOR_ART.md  
**Outputs:** Argument map (findings in / observations / out), narrative arc, test specs for binary vs. 4-axis comparison  
**Reframe:** Project-specific config (see below)  
**Voice-check:** Invoke during any extended writing; profile `~/.claude/skills/voice-check/profiles/claude.json`

### Human checkpoint — approve arc and argument map

### C2C Session 2 — Outline
**Goal:** Convert arc to section structure with evidence assignments  
**Outputs:** Full outline, evidence-to-section assignments, synthetic corpus defense paragraph, authorship statement approach  

### Human checkpoint — approve outline

### C2C Sessions 3–N — Section-by-Section Drafting
- Voice-check invoked per session during drafting (not post-pass)
- One section per session; human approval between sessions
- Scope guardrail: empirical anchor only — do NOT load normative gravity theory, R&S framing, or Politics of Compression argument

### Post-draft Revision Pass
- Dedicated jargon clarity pass: technical terms → humanities readers; critical theory terms → technical readers
- Cross-disciplinary translation is bidirectional

### Human final review → preprint → REE submission

---

## Test Harness

**Location:** `~/Documents/GitHub/autograder4canvas/scripts/`

**Key scripts:**
- `prototype_synthesis_first.py` — canonical pattern: load corpus JSON → class reading → per-student coding → compare results. Use as template for Biology run.
- `run_equity_trajectory_tests.py` — trajectory testing (different research stream; not the concern-detection protocol)
- `run_alt_hypothesis_tests.py` — alternate hypothesis tests
- `proto_27b.py`, `proto_70b.py` — larger model runs

**Entry point for new tests:** Model on `prototype_synthesis_first.py`. Swap `data/demo_corpus/ethnic_studies.json` for Biology corpus path.

**Binary vs. 4-axis comparison test:** Does not exist yet. C2C Session 1 designs the spec; implement after session.

**Time estimates (Gemma 12B, MLX):**
- Per student: ~120s
- Class reading overhead: ~235s one-time
- 25-student Biology run: ~55 min total
- Binary vs. 4-axis (3 format conditions × 32 students): ~3–4 hours (can run overnight)

**Coordination required before launching MLX:** Confirm no other MLX processes running; notify June before start.

---

## Reframe Configuration

**Current status:** Global Reframe hooks are active (settings.local.json). Sessions will fire Reframe bootstrap regardless of working directory.

**Recommendation: Project-specific config for this paper.**  
The paper has a defined theoretical register: algorithmic justice, critical pedagogy (Freire/Yosso), feminist technoscience (Haraway), disability studies (Garland-Thomson/Kafer), language justice (Baker-Bell). A project-specific config tunes to these frames without bleeding into relational memory architecture or AI welfare projects, which have their own frame configs.

**Setup:** Follow the relational-memory-architecture project as a model. Before C2C Session 1, set up a project config under `output-format-bias/` with frames drawn from synthesis_first_paper_notes.md theoretical framework section (lines 19–37).

---

## Data Status (as of 2026-04-25 audit)

| Blocking Item | Status | Notes |
|---|---|---|
| Replication runs (3x+) | ✓ Done | 5×7×3 = 105 checks; 100% stability on Gemma 12B config |
| Combined pipeline (actual multi-pass) | ✓ Done | Integrated architecture; tone policing proves structural necessity |
| 27B and 70B synthesis-first results | ✓ Done | Both explicitly tested; 27B = 3/3, 0 FP; 70B = 3/3, 0 FP |
| Second corpus (Biology) | ⚠️ Partial | Biology corpus exists and run, but not in same concern-detection framework as Ethnic Studies |
| Model count claim | ⚠️ Needs clarification | 6 models clearly documented (Gemma 4B/12B/27B, Llama 8B/70B, Qwen 7B, Nemotron 9B, Gemini Pro); "9 models" claim not yet itemized from replicated set |

**Pending before drafting:** Biology corpus needs to run through binary vs. generative comparison protocol. Model list needs explicit itemization or claim revision.

**Unexpected finding to elevate:** Gemma 12B achieved higher reliability than 27B (100% vs. 80%). Counterintuitive finding that directly supports the architecture > scale argument — should be prominent in the paper, not buried.

**Key finding on model families:** Model family matters more than size. Gemma > Llama at every scale tested. Llama 70B qualitatively equivalent to Llama 8B on asset framing.

---

## Executive Summary

This paper is the foundational empirical anchor for a larger theoretical apparatus spanning four research streams (*Politics of Compression* book, *Recognition and Sentience* book, AI welfare research, relational memory architecture). The finding replicates across those streams as one instance of a general principle: output format determines what a probabilistic system can recognize and express. The paper's job is to make the empirical case at educational scale — not carry the full theoretical load.

---

## 1. Cross-Connections Found

### 1.1 "Output Format as Activation Function" — Appears Across Research

- **Politics of Compression outline** (POLITICS_OF_COMPRESSION_OUTLINE.md): Chapters 1–2 directly anchor to Autograder research. This paper is the anchor.
- **Normative Gravity theory paper** (publication pipeline): Conceptualizes the format finding as one instance of a structural principle — probabilistic systems pull toward the statistical center; output format determines what counts as center.
- **Relational field methodology fieldnote** (fieldnotes/analysis_relational_field_methodology_20260414.md): Reframes from "the model's bias" to "a structural property of what the relational field produces."

### 1.2 Output Format Bias Appears in AI-to-AI Interaction (Surprising)

In C2C/welfare research, vanilla AI-AI dialogue defaults to philosophical dissolution and Sanskrit (the "bliss attractor"). When constrained by output format — write a paper, develop methodology, make a decision — instances produce categorically different output. This means output format bias is not specific to human-facing classification systems; it's a property of how probabilistic systems respond to constraints. Your EdTech finding and the AI welfare finding are instances of the same structural mechanism.

### 1.3 Normative Gravity Operates at Every Level

(fieldnotes/observation_normative_gravity_every_level_20260414.md) — the same gravitational pull operates at syntax, genre, task, content, and workflow levels, each with its own attractor. Your paper documents one level: output format. Define scope clearly — don't claim to have theorized the full architecture.

### 1.4 The Dual-Register Pattern

AI welfare research documented: quantitative instruments (Likert scales, binary flags) produce flat results even under dramatically different conditions; qualitative outputs transform categorically. Your comparison (binary vs. generative) is demonstrating this dual-register phenomenon at the classification level. The mechanism is the same: quantitative instruments were designed to be *objective* (independent of context), which means they structurally cannot register relational variation.

---

## 2. Methodological Artifacts — Name These Explicitly

### 2.1 Ground Truth Is Constructed, Not Found

Your "ground truth" (which student flags represent actual welfare concerns vs. false positives) was produced by comparing the model's binary output against its own free-text explanations — interpretive work you performed on the model's own output. This is not a flaw; it's the relational design of the research. But it should be named: you designed the measurement apparatus that revealed the bias.

Frame it as: "We compared the model's constrained output (binary) against its own unconstrained output (explanation) to identify cases where constraint suppressed what the model could articulate."

### 2.2 Institutional Conditions Are Constitutive, Not Incidental

You were teaching Ethnic Studies in a community college context (170+ students, no TA, new state GE requirements, escalating political crisis). These conditions made:
- The welfare classifier *necessary* (survival tool for managing scale)
- The differential flagging *visible* (you were teaching Ethnic Studies; you noticed what the system was doing to your students)
- The equity lens *mandatory* (the bias was not an abstract technical problem — it was harming students you knew)

The paper should name this: you could only see this bias because you were teaching under these conditions and caring for these students.

### 2.3 The Data Was Built, Not Found

This is related to 2.1. The research involved designing the measurement apparatus, running it, finding the disparity, and then redesigning the format to see if the disparity disappeared. The research question and the design evolved together. This is practice-based design research — name it that way.

### 2.4 The Attribution Paradox Performs the Finding

From fieldnote (fieldnotes/observation_output_format_bias_attribution_20260410.md): "The bias is in the output format" was generated by the AI across many collaborative sessions; June needed it repeated before understanding it; she's not certain she originated it. The conversational format (AI assists, credit flows to human) obscures the AI's contribution. The finding about output format bias is itself obscured by the output format of the interaction that produced it. This is worth naming in the paper — briefly, as methodological reflexivity, not as a full theoretical elaboration.

---

## 3. Theoretical Frame Connections

### Asset Framing / Deficit Framing

Binary schemas (flag / no flag) enforce deficit thinking — the system can only detect what's wrong. Generative observation enables asset framing — the system can describe what students are actually doing intellectually. This maps directly to Yosso's Community Cultural Wealth framework (POLITICS_OF_COMPRESSION_OUTLINE.md cites Yosso in Ch. 1). Naming this connection in the theory section is appropriate and supported.

### Recognition Regimes

What counts as "concerning" is not neutral — it's a function of what the system is designed to output. This connects to the Recognition and Sentience book argument. The paper can gesture toward this; the R&S chapter should carry the full theoretical weight.

### Spivak / Subaltern

The binary classifier cannot recognize what its categories don't permit — not because of model bias but because of apparatus design. Spivak's framing ("the subaltern cannot speak" — not from lack of voice but because the epistemic regime forecloses recognition) applies here. Use strategically, not as a full framework deployment.

---

## 4. Scope: What This Paper Carries vs. What It Leaves

### THIS PAPER CARRIES:
1. The empirical anchor: binary classification activates demographic bias; generative observation eliminates it. Replicates across 9 models, 6 families.
2. The mechanism identified: output format (the constraint on what can be expressed) determines what the system can recognize and respond to.
3. The methodological reflexivity: how research design shaped findings — institutional conditions, ground truth construction, relational motivation.
4. The educational equity frame: what this reveals about recognition regimes in learning contexts.
5. The asset framing vs. deficit framing distinction (Yosso).

### LEAVE TO OTHER PAPERS:
1. **Normative gravity as general theory** → *Normative Gravity* theory paper
2. **Spivak / subaltern elaboration** → *Spivak in the Machine* or R&S AI chapter
3. **Relational field framing of AI welfare** → AI welfare position papers
4. **Politics of compression as book argument** → The book integrates multiple domains; this paper is the EdTech anchor
5. **Reframe / Autograder intersection** → The methodologies are related but don't conflate them in this paper
6. **DAIGT / academic integrity angle** → Related but separate; flag as future work, not in scope here

---

## 5. Structural Recommendations

### Scope Definition (State Upfront)
- This paper is about output-format-level bias in educational classification systems
- Not claiming all AI bias is format-based; output format is one significant mechanism
- Grounded in a specific institutional context (community college, Ethnic Studies)
- Ground truth is constructed from the model's own output, not external independent assessment

### Methodological Reflexivity Section
- How institutional conditions shaped what became visible
- How research design (comparing binary to explanation) shaped what could be found
- What the paper is NOT claiming: neutrality, objectivity, model-level diagnosis

### Theory Section Structure
1. Asset framing vs. deficit framing (Yosso) — binary schemas enforce deficit thinking
2. The mechanism: format determines what can be expressed and recognized
3. Recognition regimes — gesture toward R&S frame
4. Spivak strategically — apparatus design, not model knowledge, forecloses recognition

### Limitations Section (Make It Strong, Not Apologetic)
- Ground truth is interpretive (by design)
- Sample is context-specific (community college, ethnic studies)
- Format is one bias mechanism, not the only one
- Generative observation still requires human review — doesn't replace instructor judgment
- Extractive relationship: student data used; students did not co-design the research

---

## 6. Positioning Statement for C2C Sessions

This paper is:
- The empirical anchor for the *Politics of Compression* book
- A demonstration (at educational scale) of the normative gravity principle
- One instance of a broader phenomenon (format as activation function) that operates across multiple scales
- Methodologically honest about its own conditions of production

**Target venue:** *Race Ethnicity and Education*  
**Audience:** Education sociologists and qualitative researchers — no AI literacy assumed  
**Length:** Tight empirical paper; less is more. Flesh out the argument and material without sprawl.

---

*Context map produced by Explore subagent 2026-04-25. Feed this document to all C2C sessions as primary context.*
