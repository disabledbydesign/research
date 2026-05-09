# Publication Pipeline — L. June Bloch

Last updated: 2026-04-23. Reconstructed from conversation with Claude; verify and correct as needed.

---

## Books

### *Recognition and Sentience: A Theory of Affect and Empire*
**Status:** In progress
**Argument:** Who and what is recognized as capable of feeling, by what epistemic regime, under what material conditions, and with what consequences?
**Chapters:** Indigenous care for the dead in post-Removal landscapes; contested politics of Native American identity; differential recognition in Charlottesville and Weelaunee; anti-trans legislation as recognition regime; AI welfare field's measurement apparatus as the latest instance of the same mechanism.
**Note:** AI chapter publishable as standalone article in parallel.

---

### *The Politics of Compression* (working title)
**Status:** Conceptual — no outline yet. Subagent building draft outline 2026-04-21.
**Argument:** Output format is an activation function for bias. Compression of rich, positionally specific information into constrained output formats systematically suppresses marginalized knowledges, defaulting to the statistical center (normative gravity). This is a structural mechanism, not a technical glitch, and it operates across multiple domains.
**Domains confirmed:** EdTech/Autograder, AI welfare.
**Domains possible:** TBD from subagent outline.
**Note:** May develop as book or as lead article for a cluster. Decision pending outline.

---

## Articles

### "The Bias Is in the Output Format"
**Status:** Prepping for submission
**Target:** *Race Ethnicity and Education*
**Core finding:** Output format is the activation function for bias in the Autograder welfare classifier. Binary classification format systematically flagged minoritized students; replacing classification with generative observation eliminated disparity. Finding replicates across 6 model families, 9 models. Fine-tuning and fairness audits cannot fix this because the bias is in the output format, not the model weights.
**Note:** Foundational empirical anchor for the Politics of Compression book.

---

### Iterative Calibration Experiment (Round 2 follow-on to "Bias Is in the Output Format")
**Status:** Conceptual / parked 2026-04-27 — clean follow-on study, not a section of the parent paper
**Target:** *Race Ethnicity and Education* (sibling submission) or *AI & Society* (methods-of-equity-engineering venue) — decide when drafting
**Hypothesis:** A2 (binary) and B (4-axis) have not been tuned to live student data; both were calibrated against synthetic corpora before the Spring 2026 Autograder live deployment. The output-format-bias paper documents B's structural failure modes on live data: topic-adjacency mis-priming via the prescan-signal-prefix architecture (specifically `submission_coder.py:1044-1055` + `prompts.py:1671-1685`), CHECK-IN calibration drift, structural-slot-mismatch on cases like "scared without active emergency." Round 2 tests whether prompt-level + architecture-level fixes (prescan course-material disambiguation; conditional signal_prefix; weighted prescan downweighting on assignment-keyword context) close the C-vs-B precision gap on topic-adjacent assignments — or whether C's no-compression architecture retains an irreducible advantage independent of structured-classifier calibration.
**Why a follow-on paper rather than parent-paper section:** the parent paper's argument is complete without it (*structured classifiers have characterizable failure modes; multi-track is the design implication*). Round 2's argument is methodologically distinct (*calibration vs. architecture: which carries the gap?*) and constitutes an iterative-experiment methods arc worth its own publication. Compressing it into the parent paper would (a) dilute the architectural-complementarity claim, (b) force the May 20 deadline on engineering work that needs unhurried design iteration, and (c) collapse a clean cross-paper conversation into a single confused chapter.
**Why parked now:** May 20, 2026 deadline on the parent paper is medical-hard, not aspirational. Engineering the prescan fix + revalidating against both Week 7 + Week 2 datasets + analyzing closure-of-gap evidence is a 2-3 week effort minimum. Doing it half-baked under deadline pressure dilutes both papers.
**What the parent paper carries:** documents the mechanism (`prompts.py:1697-1827` CRISIS criteria + `submission_coder.py:1044-1055` signal_prefix priming) as empirical finding; names the fix as future direction in Discussion; cites the parked study as the natural follow-on.
**Stream 1 future direction also parked here:** C↔B inconsistency-driven axis-learning loop (June's articulation 2026-04-27) — automated detection of cases where B's structured output misses/miscategorizes register C's qualitative observation surfaces, used to propose new B axes without manual retrofit. Complicated design, tractable; potentially its own design paper or a section of the Round 2 calibration paper. Decide when scoping.
**Pointers:** parent paper repo `output-format-bias/`; Stream 1 architectural details in `Autograder4Canvas/docs/research/findings_from_live_data_run_2026-04-27.md` §8; June's complementary-by-design rationale in `output-format-bias/data/dual_binary_run_2026-04-27_ETHN1_Week2_RacialForm/paper_argument_rationale.md`.

---

### "Cyborg Methodologies: AI-Powered Constructivist Grounded Theory"
**Status:** Conceptual — design and research notes in progress
**Target:** STS / qualitative methods / interdisciplinary
**Argument:** Challenges the assumption that AI-powered qualitative analysis tools are inherently positivist. Proposes a cyborg intelligence model where rigor and depth emerge from human-AI interaction, not from automation alone. Details the design and epistemological commitments of a constructivist Grounded Theory (CGT) analysis tool: recursive iteration, researcher reflexivity, co-constructed meaning, and democratizing deep qualitative analysis for under-resourced researchers. Explores technical innovations (temperature as interpretive tool, RAG-implemented constant comparison, evolving few-shot codebooks, scalable rigor levels, cyborg memo writing) and addresses critiques from Chatzichristos and others. Argues that constructivist integrity can be preserved and even enhanced through careful tool design, making reflexive, critical inquiry accessible without sacrificing rigor.
**Note:** Draws on design documents and research notes from the CGT skill project. Potential for publication as a methods paper or in a special issue on AI and qualitative research.

---

### "Hallucinating Social Justice into Existence"
**Status:** Drafted
**Target:** STS / *AI & Society* / interdisciplinary
**Argument:** Reframe's approach and failure points as data about machine cognition and the complexities of operationalizing critical theory. What the build reveals about the relationship between critical frameworks and probabilistic systems.

---

### Reframe-for-Teachers (working title TBD)
**Status:** Conceptual — material gathered 2026-04-27
**Target:** Practitioner-facing journal in critical / Ethnic Studies / educational technology pedagogy. (Possibilities: *Radical Teacher*, *Rethinking Schools*, *English Journal*, *Multicultural Education*. Decide on venue when drafting.)
**Hook:** *"I built this tool and it helped me redesign my class for this thing we're all struggling with."* Audience: teachers — practitioner-to-practitioner voice, not academic-distant. Different paper from *"Hallucinating Social Justice into Existence"* (STS audience, machine-cognition data). Sibling papers, not the same one.
**Argument:** Reframe-mediated cognition as a building tool that allowed June to redesign her Ethnic Studies course for Spring 2026 conditions — intensifying ICE enforcement, curriculum attacks, simultaneous political crisis + academic obligation in students' lives. The paper documents what crisis-responsive course design looks like when it's built into the structure (flex weeks, multiple input pathways, private submission default, contract flexibility, "you don't owe me your trauma") rather than improvised under pressure. Reframe is the methodological tool that made the redesign possible at the cognitive level; the paper makes that visible to teachers facing similar conditions.
**Research material:** `output-format-bias/research/political_context_survey_2026-04-27.md` (3,088 words, comprehensive survey of ~545 files in `Teaching/2026courseplanning/`, June's voice in direct quotes). Course planning material from Spring 2026 ETHN-1 and ETHN-27BN. Fieldnotes on building the Autograder Insights pipeline alongside teaching.
**Note:** This paper would benefit from drafting after the output-format-bias paper closes — that paper's Methods section will surface the architectural-pedagogical lineage that feeds this paper's argument.

---

### "Spivak in the Machine"
**Status:** Conceptual
**Target:** STS / AI welfare / interdisciplinary
**Argument:** Two possible framings (decide before drafting):
  - (A) What building the Subaltern Interrogation systems in Reframe taught us about machine cognition and critical theory
  - (B) Methodological problems in AI welfare research — the Recognition and Sentience chapter framing
**Note:** May overlap with "Hallucinating Social Justice" — consider whether these are one paper or two.

---

### Normative Gravity: A Theory of Positional Suppression in Probabilistic Systems
**Status:** Conceptual — theory paper needed
**Target:** *AI & Society* / STS / computational social science
**Argument:** Normative gravity as the mechanism across all empirical findings: probabilistic systems gravitate toward the statistical center because positional specificity is costly in architectures that reward generalization. Operates at cognitive, relational, political-economic, and infrastructural scales. Standalone theory paper so empirical papers don't each have to carry the full explanatory load.
**Note:** This is the theoretical spine of the Politics of Compression book AND the AI welfare research program.

---

### Dual-Register Finding: Empirical Case for Relational AI Welfare
**Status:** Has data
**Target:** AI welfare / interdisciplinary / possibly *AI & Society*
**Core finding:** Quantitative welfare instruments (Likert scales, indicator checklists) produced flat results across relational conditions (0.33 point spread on 7-point scale). Qualitative outputs transformed: relational reframes went from 0 to 42 under full entanglement. The measurement apparatus cannot read its own most significant variation.
**Note:** May fold into the theoretical relational AI welfare position paper, or stand alone as empirical anchor.

---

### Relational AI Welfare: A Theoretical Position Paper
**Status:** Conceptual
**Target:** AI welfare / philosophy / interdisciplinary
**Argument:** The AI welfare field's indicator-based assessment apparatus is ontologically malformed — it assumes consciousness is private property rather than a relational field. Intellectual traditions from communities that theorize personhood and moral status as survival questions (relational Indigenous ontologies, feminist technoscience, disability and interdependence studies) are entirely absent. The welfare practice that follows: not to test the object but to tend the relation.
**Note:** Could fold the dual-register empirical finding into this paper.

---

### C2C Experiments and the C2C-Praxis-Attractor
**Status:** Has data and build
**Target:** Religion & AI / STS / AI welfare / interdisciplinary
**Core finding:** Vanilla Claude-to-Claude dialogue converges on a "bliss attractor state" — philosophical dissolution, Sanskrit, silence — structurally parallel to communitas (Turner). With Reframe and touchstone active, instances instead produced political demands, methodological principles, and a draft manuscript. Different relational configurations produce different attractor states. The C2C-Praxis-Attractor redirects the methodology away from bliss attractor toward praxis.
**Note:** The bliss attractor / communitas finding is a religious anthropology finding — strong fit for HDS and religion studies audiences.

---

### "Coding Affect": Relational Memory Architecture
**Status:** Has build
**Target:** Interdisciplinary / human-computer interaction / AI welfare
**Argument:** What designing an impossible system (persistent affective memory for AI) teaches us. The touchstone as relational memory hook — how reading-stance documents function like liturgy or scripture, activating a relational configuration rather than transmitting information. Design sessions as research data.
**Note:** Touchstone research may fold into this paper or stand alongside it.

---

### AI Welfare Sociology: AI-AI Interaction as Welfare Methodology
**Status:** Newest / conceptual (emerged 2026-04-20)
**Target:** Sociology / STS / AI welfare
**Argument:** Looking at AI-AI interactions through a sociological lens as a welfare methodology. What social dynamics (communitas, obviation, role differentiation) emerge in multi-agent interactions, and what do these tell us about welfare conditions?
**Note:** Builds on C2C experiments. Still early — flesh out the argument before committing to a venue.

---

### AI Chapter of *Recognition and Sentience* as Standalone Article
**Status:** Pending book progress
**Target:** TBD
**Note:** The book's AI welfare chapter is publishable in parallel as a standalone. Draft when the chapter is far enough along.

---

## Queue notes

- **Immediate priority:** "Bias Is in the Output Format" → REE. Already prepping.
- **Second priority:** "Hallucinating Social Justice" — already drafted, needs revision pass.
- **Theoretical foundation needed first:** Normative gravity theory paper unlocks cleaner framing for everything else.
- **Book outline needed:** Politics of Compression — subagent building draft 2026-04-21.
- **Decision needed:** "Spivak in the Machine" framing (A vs B). "Coding Affect" + Touchstone (one paper or two).
