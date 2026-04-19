# Decolonial, Feminist, and Marginalized-Tradition Approaches to PKM and Knowledge Organization

**Compiled from**: research agent findings, 2026-04-15  
**Assessment**: Theoretically rich; uneven in PKM-relevant implementation. See thread summaries below for honest status of each.

---

## Thread 1: Afrofuturist Approaches to Knowledge Organization

### What exists: theory and critique

**Core theorists and primary texts:**

- **Kodwo Eshun** — *More Brilliant Than the Sun: Adventures in Sonic Fiction* (1998, reissued 2019 by Verso). Not a PKM text. The epistemological move: treats Black music as a machine for generating counter-futures. His 2003 essay "Further Considerations on Afrofuturism" (CR: The New Centennial Review) explicitly frames Afrofuturism as producing "counter-memories" that work against the "hauntology of the present." The archival implication: non-linear, layered, non-sovereign temporality for knowledge structures. His book's page numbering begins in negative numbers — this is not an accident; it's a structural argument about temporal order.
  - "Further Considerations" PDF: https://www.researchgate.net/publication/27225560_Further_Considerations_on_Afrofuturism

- **Alondra Nelson** — Founded Afrofuturism listserv 1998; edited *Social Text* special issue 2002. Academic framework: racial identity fundamentally shapes technocultural practice. Key text: "Introduction: Future Texts" (Social Text, 2002). Nelson critiques the "digital divide" framing as constructing Blackness as inherently oppositional to technology — a bias directly relevant to any PKM system that presupposes a "neutral" user.
  - Nelson's Afrofuturism portal: http://www.alondranelson.com/books/afrofuturism
  - Social Text PDF: https://monoskop.org/images/0/0e/Nelson_Alondra_ed_Afrofuturism_Social_Text.pdf

- **Rasheedah Phillips / Black Quantum Futurism (BQF)** — The most directly relevant practitioner. BQF (with Camae Ayewa/Moor Mother) builds actual tools and spaces. Key concept: **temporal dissonance** — the experience of time under racial capitalism is non-linear, fragmented, multiply-layered. This is not metaphor; it is design specification.
  - *Black Quantum Futurism: Theory & Practice* Vols. I & II (Afrofuturist Affair, 2015/2021)
  - Community Futures Lab: physical space in North Philly — zine library, recording booth, workshop, oral futures archive. This is the closest to implemented PKM.
  - "The Future(s) Are Black Quantum Womanist": open-access nonlinear archive/timescape — https://blackquantumfuturism.com/
  - BQF main site: https://blackquantumfuturism.com/
  - Space-Time Collapse Vol II (free archive.org): https://archive.org/details/community-futurisms
  - Phillips at DLF Forum 2017 (explicitly addresses digital archives + temporal knowledge): https://forum2017.diglib.org/speakers/rasheedah-phillips/

- **adrienne maree brown** — *Emergent Strategy: Shaping Change, Changing Worlds* (AK Press, 2017). Not a PKM text but contains a complete framework: fractal, adaptive, non-linear, iterative, interdependent, resilience-focused. Brown's "small is good, small is all" and "trust the process" principles map cleanly onto non-hierarchical knowledge structures.
  - Free PDF (via Squarespace): https://static1.squarespace.com/static/5ad0d247af209613040b9ceb/t/5db5a44b0e6ba42da976cce7/1572185168567/brown+2017-Emergent+Strategy+full+book.pdf

### What exists: library science critique

- **Critical cataloging** tradition: Sanford Berman's 1971 *Prejudices and Antipathies* first documented racist/sexist/xenophobic bias in Library of Congress Subject Headings. Dorothy Porter Wesley (1930s–1960s) created alternative Black knowledge organization systems at Howard University, rejecting DDC for African diaspora materials.
- **"Dewey Deracialized"** (Knowledge Organization, 2016): https://www.researchgate.net/publication/292506211
- **"How Did We Get Here? Race and Ethnicity in Dewey Decimal Classification"** (KO 51/6, 2024): https://www.imrpress.com/journal/KO/51/6/10.5771/0943-7444-2024-6-414

### Honest assessment for PKM

**What exists**: rich theoretical framework (non-linear time, counter-memory, temporal layering); one institutional implementation (BQF Community Futures Lab, community-scale); critical cataloging literature is extensive.

**What does not exist**: Any PKM tool explicitly designed from Afrofuturist principles. No published framework translating BQF temporal theory into information architecture. The gap between the theory and implementation is substantial. Phillips is the most tool-oriented practitioner but her work is community-scale physical + open archives, not personal knowledge systems.

**Design seeds from this tradition**: 
- Non-linear temporal tagging (notes can belong to past/present/anticipated futures simultaneously)
- Counter-memory as a design mode (active resistance to hegemonic narrative; flagging what dominant systems would suppress)
- Fractal organization (brown): small units replicate the structure of the whole
- Oral futures (sound recording) as a knowledge format equal to text

---

## Thread 2: Indigenous Knowledge Organization and Epistemology

### What exists: implemented tools

**Mukurtu CMS** — the strongest example of indigenous epistemology implemented in a knowledge management system.
- Site: https://mukurtu.org/
- Open source CMS built with the Warumungu community (Australia), maintained at Washington State University Center for Digital Scholarship.
- Key design moves: **cultural protocols as architecture** — who can access what, under what conditions, is not a permissions layer on top of a neutral system; it is the system's organizing logic. No content is "public by default."
- **Traditional Knowledge (TK) Labels**: 28 distinct labels (e.g., TK Secret/Sacred, TK Seasonal, TK Women General, TK Men General, TK Community Voice) that function as structured metadata for culturally-bounded knowledge.
- Design for Diversity toolkit on Mukurtu: https://des4div.library.northeastern.edu/indigenous-knowledge-systems-and-mukurtu-cms/
- TK Labels FAQ: https://mukurtu.org/support/traditional-knowledge-labels-faq/

**Local Contexts / TK Labels** — initiative providing a label + notice system that can be integrated into any existing archive or data infrastructure.
- Site: https://localcontexts.org/
- TK Labels: https://localcontexts.org/labels/traditional-knowledge-labels/
- Now integrated into DataCite, Library of Congress Ancestral Voices collection, and RAID metadata schema.
- This is an **implemented layer** you could add to any PKM system.

**Brian Deer Classification System / X̱wi7x̱wa Library**
- Brian Deer (Kahnawake/Mohawk librarian) created a non-DDC/non-LCC classification system 1974–1976 organized around Indigenous knowledge relationships and associations, not Western subject hierarchies.
- X̱wi7x̱wa Library (UBC) uses an adapted version: https://xwi7xwa.library.ubc.ca/collections/indigenous-knowledge-organization/
- The classification gives priority to **relationships** in its structure (not categories). Items sit in their relational context, not a disciplinary slot.
- X̱wi7x̱wa Classification detail: https://xwi7xwa.library.ubc.ca/collections/indigenous-knowledge-organization/subhead/

### What exists: data sovereignty frameworks

**CARE Principles** (Collective Benefit, Authority to Control, Responsibility, Ethics)
- Global Indigenous Data Alliance framework for data governance: https://www.gida-global.org/care
- Published: Wilkinson et al., *Data Science Journal*, 2020: https://datascience.codata.org/articles/dsj-2020-043
- Nature article on operationalizing CARE + FAIR: https://www.nature.com/articles/s41597-021-00892-0
- PKM relevance: **CARE provides a governance framework**, not just metadata. "Authority to Control" and "Responsibility" are design constraints that challenge the "my notes = my property" individualist assumption of mainstream PKM.

**OCAP® Principles** (Ownership, Control, Access, Possession)
- First Nations Information Governance Centre (Canada): https://fnigc.ca/ocap-training/
- Older framework (1990s), focused on First Nations data rights.

### What exists: epistemological frameworks

**Robin Wall Kimmerer** — *Braiding Sweetgrass* (Milkweed Editions, 2013). Not a knowledge management text but articulates a relational epistemology where knowing is inseparable from relationship, reciprocity, and responsibility. The "grammar of animacy" argument — that English erases agency from non-human entities — is directly relevant to how we tag, categorize, and name things in PKM systems.
- Site: https://www.robinwallkimmerer.com/

**Tyson Yunkaporta** — *Sand Talk: How Indigenous Thinking Can Save the World* (Text Publishing, 2019). Most directly applicable to knowledge systems design.
- Eight Aboriginal Ways of Learning framework (2009 thesis): non-linear, story-sharing, symbols/images, land-links, community links, deconstruct/reconstruct, learning maps, non-verbal.
- PKM relevance: **non-linear learning** and **story-sharing** as primary organizational modes, not taxonomic classification. Visual/spatial over hierarchical.
- 8 Ways pedagogy overview: https://shinyshiny.wixsite.com/8-ways-game/8-ways-pedagogy
- Yunkaporta's Indigenous Knowledge Systems Lab: https://www.deakin.edu.au/about-deakin/people/tyson-yunkaporta

**Abundant Intelligences** — the strongest active research program applying Indigenous epistemologies to AI/knowledge system design.
- Site: https://abundant-intelligences.net/
- 6-year program (Concordia + Massey University + 11 other institutions), co-directed by Jason Edward Lewis and Hemi Whaanga.
- Published framework: Lewis, Whaanga & Yolgörmez, "Abundant intelligences: placing AI within Indigenous knowledge frameworks," *AI & Society*, 2024: https://link.springer.com/article/10.1007/s00146-024-02099-4
- Three axes: Integrations (synthesizing Indigenous + mainstream knowledge frameworks), Imaginaries (speculative AI design), Intelligences (translating Indigenous intelligence concepts into computational contexts).
- ScienceDaily writeup (Jan 2025): https://www.sciencedaily.com/releases/2025/01/250115164916.htm

### Honest assessment for PKM

**What exists**: The richest implementation tradition of any of the four threads. Mukurtu is production software. TK Labels are live metadata infrastructure. Brian Deer is a deployed classification system. CARE principles are published governance standards. Abundant Intelligences is active funded research.

**What does not exist**: Direct translation of these frameworks to *personal* knowledge management (they are primarily collective/institutional). Kimmerer's relational epistemology and Yunkaporta's 8 Ways have no PKM tool implementation I could find.

**Design seeds**:
- **Relational primacy**: things are organized by their relationships, not their category membership
- **Access as ethics**: who can know what, under what conditions — not just a metadata field but a structural design question
- **Non-hierarchical classification**: circular/spiral/fractal organization vs. tree hierarchy
- **Story as primary format**: narrative knowledge structures alongside propositional ones
- **Land/place-linkage**: geographic/contextual anchoring of knowledge (analogous to situating notes by context of creation, not just topic)

---

## Thread 3: Feminist Technoscience and Knowledge Organization

### What exists: theory with PKM-relevant application

**Donna Haraway** — "Situated Knowledges: The Science Question in Feminism and the Privilege of Partial Perspective" (Feminist Studies, 1988; collected in *Simians, Cyborgs, and Women*, 1991). The canonical argument: all knowledge is produced from a specific embodied location; "the view from nowhere" is a fiction that naturalizes the view of the powerful.
- PKM design implication: **positionality metadata**. A system built on situated knowledges would tag notes by the conditions of their production — who was present, what power dynamics, what context. Not neutral categorization but situated annotation.
- Princeton PDF: https://commons.princeton.edu/hum583-f21/wp-content/uploads/sites/283/2021/08/Haraway-Situated-Knowledges.pdf
- New Materialism almanac entry: https://newmaterialism.eu/almanac/s/situated-knowledges.html

**Karen Barad** — *Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning* (Duke UP, 2007). Two concepts with knowledge system implications:
- **Intra-action** (vs. interaction): entities don't pre-exist their relationships; they are constituted *through* them. Knowledge nodes don't exist prior to their connections — this inverts the standard "atoms + links" PKM model.
- **Diffraction**: a methodology for reading texts/ideas "through" each other rather than just reflecting them back. Produces differences rather than confirming similarities. PKM application: a diffractive retrieval mode would surface productive tensions between notes, not just similarity clusters.
- Barad Wikipedia: https://en.wikipedia.org/wiki/Karen_Barad

**Sandra Harding** — "Rethinking Standpoint Epistemology: What is 'Strong Objectivity'?" (1993). Argument: starting research from marginalized lives produces *stronger* objectivity than the pretense of view-from-nowhere, because it exposes the conditions that dominant epistemology naturalizes.
- PKM design implication: **the entry point matters**. A system that surfaces knowledge from multiple standpoints — especially marginal ones — is more rigorous, not less.
- PDF: https://sidoli.w.waseda.jp/Harding_1993_Rethinking_Standpoint_Epistemology.pdf

### What exists: applied scholarship in information science

**Diana Floegel and Kaitlin L. Costello** — "Methods for a feminist technoscience of information practice: Design justice and speculative futurities," *JASIST* 73(4), 2022, pp. 625–634. The most directly relevant published paper.
- Argues information science is limited by: extractive logics, monological individualism, binaries between people and technologies, techno-solutionism. Proposes: design justice (Costanza-Chock) + speculative futurities as methodological correctives.
- Wiley: https://asistdl.onlinelibrary.wiley.com/doi/abs/10.1002/asi.24597
- ACM DL: https://dl.acm.org/doi/abs/10.1002/asi.24597
- Earlier companion paper: "The potential of feminist technoscience for advancing research in information practice," *Journal of Documentation* 77(5), 2021: https://www.emerald.com/insight/content/doi/10.1108/jd-10-2020-0181/full/html

**Goda Klumbytė et al.** — "Feminist epistemology for machine learning systems design," arXiv:2310.13721 (CSCW '23 workshop paper). Four methods proposed: situated knowledges, figuration, diffraction, critical fabulation/speculation. The paper argues these require not translation but "transposition" — creative adaptation to ML contexts.
- arXiv: https://arxiv.org/abs/2310.13721
- Klumbytė's site: https://enginesofdifference.org/author/goda/

**Academia.edu paper** — "Feminist Epistemologies and Knowledge Organization": https://www.academia.edu/14984736/Feminist_Epistemologies_and_Knowledge_Organization  
- Critiques KOS (Knowledge Organization Systems) for falsely claiming neutrality; introduces "epistemic interoperability" as a design concept.

**Sasha Costanza-Chock** — *Design Justice: Community-Led Practices to Build the Worlds We Need* (MIT Press, 2020). The practical methodology bridge between feminist technoscience theory and actual system design.
- Free HTML version: https://designjustice.mitpress.mit.edu/
- Key principle: design processes should be led by those most affected; designers facilitate rather than decide. This is a governance argument, not just a values argument.

**Catherine D'Ignazio and Lauren Klein** — *Data Feminism* (MIT Press, 2020). Seven feminist principles for data systems: Examine Power, Challenge Binary Hierarchies, Elevate Emotion and Embodiment, Rethink Binaries and Hierarchies, Embrace Pluralism, Consider Context, Make Labor Visible.
- Free web version: https://data-feminism.mitpress.mit.edu/
- Most directly implementable of any feminist framework — the seven principles are design constraints, not just theory.

### Honest assessment for PKM

**What exists**: Strong mid-range theory (Floegel/Costello, Klumbytė, Costanza-Chock, D'Ignazio/Klein) that is closer to implementation than pure philosophy. Data Feminism's seven principles are the most directly actionable. Design Justice is the strongest governance framework.

**What does not exist**: Any feminist-technoscience-grounded PKM *tool*. The literature is information science / ML systems design, not personal knowledge management specifically. The translation work is available but has not been done.

**Design seeds**:
- **Positionality tagging**: annotate notes with conditions of production (whose voice, what context, what power dynamics)
- **Diffractive retrieval**: surface productive tensions between ideas, not just similarity — could be implemented as a "find the productive contradiction" query mode
- **Intra-active architecture**: relationships constitute nodes, not the other way around — start from links, derive entities (inverts standard graph DB model)
- **Labor visibility**: make the maintenance cost of the system legible, not hidden
- **Context metadata**: who produced this knowledge, from where, under what conditions — embedded in the note structure

---

## Thread 4: Decolonial Knowledge Frameworks

### What exists: theory and critique

**Walter Mignolo** — *Local Histories/Global Designs: Coloniality, Subaltern Knowledges, and Border Thinking* (Princeton UP, 2000). Key concepts:
- **Colonial matrix of power**: the four-part structure (control of economy, authority, gender/sexuality, knowledge/subjectivity) through which coloniality operates.
- **Border thinking/border epistemology**: knowledge produced from the colonial wound — not purely "inside" or "outside" Western epistemology but from the position of having been subjected to it. This is an epistemological location, not just a political one.
- **Delinking**: refusing to answer questions posed by the colonial matrix on the colonial matrix's terms.
- ResearchGate: https://www.researchgate.net/publication/281748607_Local_HistoriesGlobal_Designs_Coloniality_Subaltern_Knowledges_and_Border_Thinking

**Aníbal Quijano** — "Coloniality of Power, Eurocentrism, and Latin America" (Nepantla, 2000). Foundational argument: coloniality is not over at decolonization — it persists as an ordering logic of knowledge, bodies, and labor.

**Arturo Escobar** — *Designs for the Pluriverse: Radical Interdependence, Autonomy, and the Making of Worlds* (Duke UP, 2018). The most design-focused decolonial text.
- **Ontological design**: design is not neutral — it constructs the world users inhabit. Different ontologies require different designs.
- **Autonomous design**: place-based, relational, anti-extractive. Rejects universal solutions in favor of situated ones.
- Duke UP page: https://www.dukeupress.edu/designs-for-the-pluriverse
- Wikipedia: https://en.wikipedia.org/wiki/Designs_for_the_Pluriverse

### What exists: implementation

**"Layers of Technology in Pluriversal Design: Decolonising Language Technology with the LiveLanguage Initiative"** — Koch, Bella, Helm & Giunchiglia, *CoDesign* (2024); arXiv:2405.01783. The most technically grounded pluriversal design paper.
- Five-layer model: each layer (from linguistic data through interfaces) has distinct co-design intervention points.
- Case: LiveLanguage, a lexical database modeling language diversity including small and minority languages.
- arXiv: https://arxiv.org/abs/2405.01783
- HAL: https://hal.science/hal-04741875v1/document
- Tandfonline final: https://www.tandfonline.com/doi/full/10.1080/15710882.2024.2341799

**"Pluriversal Technologies: A Decolonial Typology of Knowledge Integration for Disruptive Sustainability"** — Bauwens, Friant, Beumer & Velasco-Herrejón, *Research Policy* 55(4), 2026.
- Four-mode typology: extractive appropriation / parallel operation / adaptive integration / transformative integration — along three axes: design, production, ownership.
- ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0048733326000491
- Utrecht repository: https://research-portal.uu.nl/en/publications/pluriversal-technologies-a-decolonial-typology

**Decolonial AI literature** (active research area, 2023–2025):
- "Decolonial AI: Decolonial Theory as Sociotechnical Foresight in Artificial Intelligence" — Mohamed, Png & Isaac, *Philosophy & Technology* 33(4), 2020: https://link.springer.com/article/10.1007/s13347-020-00405-8
- "AI in the Colonial Matrix of Power" — Ricaurte, *Philosophy & Technology* 2023: https://link.springer.com/article/10.1007/s13347-023-00687-8
- "Cognitive Imperialism in Artificial Intelligence: Counteracting Bias with Indigenous Epistemologies" — Ofosu-Asare, *AI & Society* 2024: https://link.springer.com/article/10.1007/s00146-024-02065-0
- "Artificial Intelligence and Epistemic Justice: A Decolonial Turn through Indigenous Knowledge Systems" — *AI & Society* 2026: https://link.springer.com/article/10.1007/s00146-026-02936-8

**Critical cataloging as implemented decolonial practice:**
- "Classification as Colonization" (Scholarly Kitchen, 2025): https://scholarlykitchen.sspnet.org/2025/03/25/guest-post-classification-as-colonization-the-hidden-politics-of-library-catalogs/
- Duarte and Belarde-Lewis: "Imagining: Creating Spaces for Indigenous Ontologies" (*Cataloging & Classification Quarterly*, 2015) — proposes decolonial information structure centering Native American knowledge organization.
- "Towards pluriversality: decolonising design research and practices" (*Design Studies*, 2024): https://www.tandfonline.com/doi/full/10.1080/15710882.2024.2379704

### Honest assessment for PKM

**What exists**: Strong theoretical framework (Mignolo, Quijano, Escobar); emerging applied research in AI and design (decolonial AI literature, pluriversal design). The Bauwens et al. typology is the most directly usable analytical tool — it lets you diagnose where any given knowledge system sits on the extractive → transformative integration spectrum.

**What does not exist**: Direct implementation of decolonial principles in a PKM tool. The Pluriversal Technologies typology (2026) is analysis, not a design manual. The decolonial AI literature is primarily about training data and governance, not personal knowledge architecture.

**Design seeds**:
- **Delinking as query mode**: a search that refuses the system's own ontological assumptions — surfaces what the taxonomy doesn't capture
- **Multiple ontologies in parallel**: rather than resolving to a single classification, allow a note to exist simultaneously in incommensurable frameworks (pluriversal, not universal)
- **Transformative vs. extractive integration test**: when incorporating knowledge from another tradition, ask which mode you're in — Bauwens et al.'s typology is diagnostic
- **Border thinking tag**: notes that live at the edge of frameworks, that don't fit the established categories — make this a first-class annotation rather than a filing failure

---

## Cross-Thread Synthesis

### Where theory is richest

**Feminist technoscience** has the most developed bridge between epistemological theory and design practice. Data Feminism's seven principles and Floegel/Costello's JASIST framework are immediately usable as design constraints. This is the thread closest to implementation.

**Indigenous knowledge organization** has the most actual implementations — Mukurtu, TK Labels, Brian Deer — but they're collective/institutional, not personal. The epistemological frameworks (Kimmerer, Yunkaporta, Abundant Intelligences) are rich but not yet translated into PKM tools.

### Where the gap between theory and practice is largest

**Afrofuturism** — enormous theoretical resources; almost zero PKM-specific implementation. BQF's work comes closest but it is community practice (physical space, oral archives), not a personal knowledge architecture.

**Decolonial frameworks** — strong critique of existing knowledge organization; emerging applied work in AI and design; no direct PKM tool. The most useful contribution may be the analytical typology for evaluating any given system (extractive/parallel/adaptive/transformative).

### What multiple traditions agree on

All four traditions converge on challenges to:
1. **Hierarchical taxonomy** — tree structures impose single inheritance; these traditions require webs, spirals, networks
2. **False neutrality** — classification is never neutral; these traditions make the value choices explicit
3. **Universal ontology** — a single correct way to organize knowledge; these traditions require multiple coexisting frameworks
4. **Individual knowledge sovereignty** — knowledge is relational, communal, contextual; mainstream PKM's individualism is not epistemologically neutral

### What none of them have done for PKM

No tradition has built a personal knowledge management tool from these principles. The closest existing work:
- BQF's open-access nonlinear archive (https://blackquantumfuturism.com/) for Afrofuturism
- Mukurtu for Indigenous knowledge (institutional/collective, not personal)
- Data Feminism's principles (a framework, not a tool)

This is a design space with no occupant.

---

## Recommended Reading Sequence (for design purposes)

For building the system:
1. D'Ignazio & Klein, *Data Feminism* — most directly implementable framework
2. Yunkaporta, *Sand Talk* — best epistemological challenge to hierarchical design
3. Floegel & Costello, JASIST 2022 — best theoretical bridge for information science
4. Bauwens et al., *Research Policy* 2026 — diagnostic typology for integration modes
5. BQF / Phillips, *Black Quantum Futurism* — temporal design
6. Escobar, *Designs for the Pluriverse* — ontological design
7. Kimmerer, *Braiding Sweetgrass* — relational knowing (poetic but load-bearing)
8. Haraway, "Situated Knowledges" — positionality as design constraint

For critique (understanding what you're building against):
- Hope Olson, *The Power to Name* — how classification marginalizes
- Mignolo, *Local Histories/Global Designs* — coloniality of knowledge
- Mohamed et al., "Decolonial AI" — why neutrality claims in AI systems are false
