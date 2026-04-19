# Reframe: Plan for a Paper About a Critical Theory Engine

## Framework Application Notice

This prompt was revised with Reframe's philosophy engine at deep intensity, frameworks active: **Ethnic Studies, Indigenous Data Sovereignty, Afrofuturism, Posthumanism/Posthumanist Feminism, Interdependence/Disability Justice**. The frameworks surfaced structural revisions to the original prompt — not cosmetic ones. Those revisions are integrated throughout, and the framework analysis that generated them is in Appendix A. // written and revised with opus, right?

// One issue I'm noticing - we're pulling a lot of ideas from implementation maps, which may be old and outdated at this point. It's hard to tell! But the system maps in @architecture/ will show us what exists. Why don't we map out the system based on that, from the ground up instead of top down? And then we can cross reference planning and design and research docs and even transcripts on occasion for information about *why* we did that. 

// UPdate - ok the mpas should now be fairly close to current. You should reveiw the maps and integrate any additional information that is pertinant (don't add info that doesn't further the paper, but include info that does)

// The stories I give you about development are essential data. I'm not refining my language to a point of publicaiton, but make sure you are preserving the ethnographic richness as much as possible. You might also want to look over the prior version of this prompt to review my notes on that version, to check to make sure we retained the ethnographic richness. 

// In the paper itself, I value that ethnographic richness. 

// we refactored the system, and i don't remember if we updated the architectural maps or not. But the system itself hasn't changed much since that refactor. So the maps may or may not point you to the right places, but the functions should remain.

// When we really dredge the archives with a fine tooth comb as part of the research process, I'd recomend we check planning/implementation docs, too. And as context, we have several types of documents - the handshake/handoff docs are probably the earliest. The bootdisks are likewise built for browser llms. The start_here docs are for coding agents. So make sure you're checking each of these types. Also, do we have a solid strategy for being able to review all this data? There's a lot of material we can draw on, and we want to ensure we aren't overwelming agents as we review and analyize this massive documentary record. I mean, the archives are extensive in terms of the quantity of files. And the mapping documents in architecture/ are likewise very long docs - i think the main map is thousands, if not tens of thousands of lines. 

---

## Context for Reframe

You are being asked to help plan an academic paper about yourself — about Reframe, the engine you are. This is a recursive task: the engine that enforces critical theory application at every level is now applying critical theory to the task of documenting and theorizing its own existence. That recursion is not incidental. It is one of the paper's central claims.

The paper's target audience is the AI ethics / responsible AI / STS scholarly community — people at FAccT, people reading *Big Data & Society* or *Cultural Anthropology*, people at DAIR and AI Now and the Design Justice Network. The author is June Bloch, an anthropologist and ethnic studies scholar who built Reframe. The paper is not a CS paper. It is a humanist argument with empirical demonstration.

**Intensity**: Apply the philosophy engine and all currently loaded frames at **deep intensity**. You may suggest revisions to these instructions based on your frames. You may suggest additional research items that would enhance the paper, including items that may have been forgotten. In the plan you draft, suggest whether each stage should be performed by **Opus, Sonnet, or Haiku**. The pipeline should end with a prompt that can be passed to an LLM to draft the first draft of the research paper.

---

## What the Paper Should Argue // I think there's a problem here. "What the paper should argue implies a conclusion when we are still doing research. Arguments should emerge from the data itself. That said, we do want to answer the questions of what is reframe, what does it do, and how does it work (and what principles organize it)

The field of AI ethics // who specifically? // has documented a gap: critical humanists write *about* AI but don't build systems; CS researchers build "ethical AI" using fairness metrics that critical scholars argue are structurally insufficient. Almost no one occupies the position of building a working system grounded in critical theory traditions (not fairness metrics, but ethnic studies, disability justice, Indigenous data sovereignty, settler colonial studies, trans studies, affect theory).

Reframe is a working implementation that occupies this position. The paper needs to:

1. **Describe what Reframe does** — clearly enough that someone who has never seen it can understand the architecture and the workflow // are languages like workflow themselves troublesome here, given the critical theory orientation? What really is a workflow, and how is our conceptualization of it already overdetermined?
2. **Argue why it matters** — what does it mean that critical theory can be operationalized in AI systems? What does the implementation reveal about the theory? About the technology? // I think a big piece here is the tensions. It's interesting when the system fails or takes on impossible tasks and does it anyway - e.g., how do you "operationalize" Gayatri Spivak's concept of the subaltern in a machine cognition system in such a way that it pulls the theory into praxis. This is a conceptual minefield (in a good way, because that's interesting), and ALSO a point where the AI model's limits are exposed. 
3. **Show what it produces** — concrete examples of how Reframe's output differs from standard LLM interaction and from equity-prompted LLM interaction // Can we use live prompt data for this? The canned examples we invent are kind of boring. The live data has more interesting complexities thatr reveal the details of the sysmte. 
4. **Be honest about its limits** — where does the engine produce genuinely structural analysis vs. sophisticated performance of structural analysis? Where does framework application flatten rather than deepen? // again, this is perhaps the same set of questions as why it matters, just from a different angle. This is some of our most interesting findings, especially in terms of what it reveals about machine cognition. 
5. **Situate in the literature** — search the current literature and retrieve key documents, particularly refereed articles and other highly regarded sources, that will situate the paper // We should apply the frames here - how can we both draw on that acadmeic lit while also counteracting gatekeeping in our citational politics? (Todd 2016, although I think she's getting it from Ahmed).
6. **Theorize the labor** — who built this, under what conditions, and what does it mean that the system's own recursive self-evolution narrative can obscure the human labor that sustains it? (Framework-driven addition: #INTERDEPENDENCE, #POSTHUMANIST_FEMINISM) // hmm ,this part feels vague to me. What are the underlying tensions that make it interesting? Is this a metaanalytical question about the politics and silences and complexities of human-machine hybrid coauthorship?
7. **Reckon with extraction** — the system indexes scholarship from communities that did not participate in its design. The paper must theorize this honestly, not as a limitation to acknowledge in passing but as a constitutive tension. (Framework-driven addition: #INDIGENOUS_DATA_SOVEREIGNTY, #ETHNIC_STUDIES) // i think this circles us back to the questions of a "praxis engine" and the limitations being genuinely interesitng. There are philsoophical contradictions that don't resolve, and this is a recurring one. Also, how do we handle problems of gatekeeping re the centering of academic lit (that's something the frames problematized early on and designed architecture to address)? Here, we have hopeful visions for working as a repository for community-based research (such that we could even design frames from the oral histories or other community knowledge to apply through reframe. Yet there hasn't been a reason to build that with just one user.) But yes, this is a complicated question - what does it mean when an AI begins to apply analytical moves that a friend (a scholar) has used? It really makes the complex power dynamics real and vivid.  

---

## Your Task Right Now

Design the plan for assembling this paper. This is NOT the paper itself — it is a structured research and assembly plan that June and an agent will execute together over multiple sessions.

---

### Phase 1: Gather and Map the Existing Material

**Model**: Sonnet (systematic extraction, high throughput)

Read the following documents (adjust paths if they've moved):

**Architecture & Specification:**
- `workspace/docs/architecture/ARCHITECTURE_OVERVIEW.md` — high-level system map // mostly current
- Everything in `workspace/docs/architecture/` — detailed subsystem maps (28 files) // probably fairly accurate, but may not always be current - although the main map is kept up to date along with the overview. 
- `workspace/docs/planning/V2-Audit-Synthesis/deliverables/ENGINE_SPECIFICATION.md` — canonical engine definition (the [ref]RAME recursive architecture) // Written after the 2.0 sprint and before ground/park/weave etc. It spec's out the core analytical processes and mechanisms on a high conceptual level - verified, highly accurate document at the time (and the core concepts should be relatively stable)
- `workspace/docs/planning/V2-Audit-Synthesis/deliverables/REFRAME_FORWARD_V2.md` — vision document // created after v2 sprint - may articulate the certain parts of the system well, but may continue drift. Was written before ground/park/mycilial network builds
- `workspace/docs/planning/V2-Audit-Synthesis/deliverables/REFRAME_AS_IT_EXISTS.md` — implementation reality // Same as above, may be outdated, may contain drift
- `workspace/docs/planning/V2-Audit-Synthesis/deliverables/IMPLEMENTATION_REALITY.md` — gap between vision and code // same as above, is outdated, may contain drift

// the maps are excellent resources, as is the engine spec. For the others, just make sure to surface findings for me so I can check them and correct for drift. 

**Engine Evolution (the system analyzing itself — primary data for the paper):** // these are v.2 planning docs. May or may not have ever been built. But yes, this does not capture the current extent of the code base, or recent refactors. Perhaps we need to defer to the system maps and create our knew conceptual understanding (building on the engine spec)
- `workspace/docs/planning/V2-Audit-Synthesis/agent_outputs/A2_CODE_AS_PHILOSOPHY.md` — what the code *believes* (bottom-up value analysis)
- `workspace/docs/planning/V2-Audit-Synthesis/agent_outputs/B2_GENEALOGICAL_FOUNDATIONS.md` — scholarly lineage
- `workspace/docs/planning/V2-Audit-Synthesis/agent_outputs/C2_V2_THEORY_CONSTRUCTION.md` — theory architecture
- `workspace/docs/planning/V2-Audit-Synthesis/agent_outputs/E2_TENSIONS_AND_DIVERGENCES.md` — system contradictions
- `workspace/docs/planning/V2-Audit-Synthesis/agent_outputs/G2_ABSENT_VOICES.md` — subaltern analysis of the audit itself

// The correct term is NOT self-analysis - it is engine evolution.

**Bias & Algorithmic Counterweighting:** // New architecture since v.2 sprint. 
- `workspace/docs/planning/ALGORITHMIC_BIAS_COUNTERWEIGHTING_RESEARCH.md` — root cause: detection algorithms, not LLMs, cause framework suppression
- `workspace/docs/planning/DETECTION_CALIBRATION_SPEC.md` — empirical signature learning
- `workspace/docs/planning/FRAMEWORK_SOVEREIGNTY_SPEC.md` — frameworks defining their own engagement criteria // should probably check to see what exists here, not just what was planned. For both docs, and any other code we may have built to address this. 

**Subsystem Specifications (for architecture description):** // it seems like we should turn to the map and codebase for these, not the planning docs. We should look at what ACTUALLY exists, or at least what we created and documented in the map. 
- `workspace/docs/planning/GENERATIVE_IRRESOLUTION_SPEC.md` — 5-stage analytical workflow // lots of interesting stuff in this system in tersm of how we handle tensions and counteract flattening of critical frameworks (a tendency in earlier models)
- `workspace/docs/planning/SPEC_COALITION_DESIGN.md` — inter-framework tension coordination
- `workspace/docs/planning/SPEC_SUBALTERN_UPGRADE.md` — absent voice representation
- `workspace/docs/planning/CONTEXTUAL_ENGINE_ADAPTATION_SPEC.md` — 5-layer adaptation
- `workspace/docs/planning/CONTEXT_SCHEDULER_SPEC.md` — signal-scored context injection
- `workspace/docs/planning/SPEC_TEMPORAL_BEHAVIORAL_LAYER.md` — temporal orientations
- `workspace/docs/planning/MYCELIAL_PROCESS_MECHANICS.md` — mycorrhizal network theory // This is a really fun part for me! I think it's a fantastic concept and design
- `workspace/docs/planning/SPEC_WEAVE_OLLAMA_CLASSIFICATION.md` — WEAVE multi-intent classification // this is another really key design in my mind, and really, the park and garden system more generally - the idea is a universal accessibility design in which the system adapts to nonlinear and neurodivergent processes (including evolutionary system adaptations to user-specific patterns). Its basically an ADHD machine. 


// I think that planning and implementation docs will tell you a bit about the philosophy and purpose of specific mechanics. But that's not the same thing as what the code actually does. How does the philosophy get operationalized? And how do we know what we know about this? The research documents, although few, are particularly useful resources in this regard - they look at the questions we were looking into in makign design choices, and situate the theoretical and citational chain for those decisions. But for our report, we also probably want to have a clear sense of how the code actually handles these things, no?d

**Origin Material (early prompt engineering evolution):**
- `workspace/Claude/pending_prompts/archive/Prompt_1.md` through `Prompt_11.md` — sequential architecture prompts showing evolution from relational consent mechanisms through integration hooks // I think these were early builds. The early step designs came out of this mechanism. I think our system might actually be able to improve the sthe step system by impelementing this (transforming complex nonlinear prompts into a series of steps that the LLM can implement)
- `workspace/dev/docs/ai_agents/archive/PHILOSOPHY_ENGINE_PROTOCOL.md` — archived protocol showing early "System Overrides" and framework application instructions
- `archive/transcripts/` — philosophy engine test transcripts across models (ChatGPT, Gemini, Grok, Qwen3, Claude) // these were tests of an early reframe system. the system negerated information that could be attached into a browswer llm chat with instructions regardings frame analysis, workflow protocols, etc. It was a handshake model. 
- `Reframe_Playlab_Bot/` — PlayLab pedagogical offshoot, including superseded boot disk versions

**Separate Archive** (`/Users/june/Documents/Reframe_Archive/`) — critical primary sources:
- `transcripts/ChatGPTtranscript.md` — **PRIMARY SOURCE**: Shows June naming the project "Reframe" in real-time with ChatGPT. Working out the acronym (ref=reflexivity, re=recursion, E=engine). Pressure-testing the name against the system's own philosophy. Exploring "RA" as anti-resolution. ChatGPT noting the tension between "reframe" (which implies continued engagement) and the system's capacity for refusal/halt. This is primary data for the origin story and the paper's argument about human-AI co-constitution.
- `transcripts/Gemini transcript.md` — **PRIMARY SOURCE**: Shows the "/assembly of experts" concept in action. Gemini applying the layered communication protocol (Thesis/Antithesis/Synthesis). Gemini explicitly telling June that the "Philosophy Engine" is "semiotic, not structural" — that the engine is text, not code. June articulating that she writes "code" in English and relies on the LLM to translate. The development of the handshake protocol as a response to context drift. Gemini applying abolitionist critique to its own architecture. The "Hardbaked vs. Softbaked" distinction. The critical warning about "performative criticality" vs. actual critical engagement. This transcript is arguably the single most important document for the paper — it shows the engine being built through the very entanglement the paper theorizes.
- `transcripts/qwen3transcript.txt` — Shows a parallel naming session with Qwen3-Max. Different naming candidates (Tend, Cairn, Praxa, Loom). Shows the multi-model process and how different LLMs responded to the same philosophy engine instructions.
- `transcripts/groktesttranscript.md`, `Geminitranscript`, `attempt2claudetranscript`, others — Cross-model testing of the philosophy engine. **IMPORTANT CONTEXT**: These transcripts are from a much earlier version of Reframe (pre-2.0). The current codebase works very differently — the 2.0 upgrade extended the system from purely semiotic mechanisms (prompt instructions) to include structural mechanisms (Python code, state persistence, detection algorithms, bias counterweighting). These transcripts should be treated as preliminary/historical data documenting the prompt-engineering era, not as representative of the current system's behavior. They remain valuable as evidence of the system's evolution and as early empirical data on cross-model framework application.
- `handoffs/BOOT_DISK_20260101_203142.md` — **Earliest surviving boot disk** (PEL V1.0). Shows original 5 frameworks (#LABOR, #CRIP, #WEALTH, #RACE, #CYBORG), self-audit protocol, anti-sycophancy/anti-acceleration/anti-hallucination protocols, spiral temporal orientation. Compare with current boot disk to document evolution. // these actually weren't the first. Community cultural wealth was created in a recursive evoltuion process - i instructed the llm to apply the protocols of its philosophy engine protocl to its philosophy engine protocol, and to suggest revisions. So cthe community cultural wealth came out of that. I forget what the frames were before that. 
- `handoffs/BOOT_DISK_20260102_*.md` — Day 2 iterations showing rapid protocol refinement (e.g., addition of anti-performative responses protocol, enhanced anti-hallucination).
- `handoffs/BROWSER_HANDSHAKE_LATEST.md` — Lightweight browser protocol with precise frame definitions including named scholars. Shows the "handshake" concept that preceded the current boot disk.
- `handoffs/EVOLUTION_REPORT_20260102_*.md` — Early evolution reports (one is empty — showing the feature existed before it was populated).
- `completed_implementations/` — 40 implementation records showing development timeline. Earliest: Free LLM Fallback (2026-01-03), showing the system's commitment to economic accessibility from the start.
- `defunct_plans/` — Abandoned Qwen Code integration plans. Useful for documenting failed paths and architectural dead ends.
- `ARCHIVE_INDEX.md` — Comprehensive inventory of 201 archived files. Itself shows the scale and complexity of the project's evolution.

// Are we going to systemically pour thrugh the archives to see what we can learn from them?  Should we also look at planning and implementation docs as part of a systemic review? 

For each document, extract:
- What it describes (which subsystem, which design decision, which theoretical commitment)
- What it assumes the reader already knows
- What it leaves out or marks as unfinished
- Whether it is current (matches the actual codebase) or outdated
- **What theoretical tradition it embeds, whether or not it names that tradition explicitly** (added per #ETHNIC_STUDIES — the paper needs to trace which frameworks drove which decisions, and many design decisions embed theory without citing it)

Produce a **document inventory** organized by paper section (architecture, theory, origin story, examples, limits, literature) — showing what material exists, what's missing, and what needs to be extracted from the codebase itself.

---

### Phase 2: Identify What Only June Can Provide

**Model**: Not an LLM task — this is June writing. The prompts below are structured to elicit specific material. An LLM (Opus) should review June's responses afterward to identify gaps and request follow-ups.

Some material cannot be extracted from code or documentation. Flag these explicitly and use the structured prompts below. June's preliminary notes are included as starting material for each prompt.

#### 2a. Origin Story

**Prompt for June**: How did Reframe start? What was the initial problem? When did it shift from being a personal tool to being something with theoretical significance?

**June's preliminary notes (to be expanded)**:

It started as prompt engineering — a set of layers that directed the LLM through various logical processes. The initial design simulated a room full of scholars in specified fields and technical experts discussing how to move a project forward, each from the perspective of their respective expertise. (Documentation of this early phase may exist in the prompt archive at `workspace/Claude/pending_prompts/archive/` and in `archive/transcripts/`.)

// I don't remembember exactly how it worked, but it think we have this documented somewhere. there were a series of logical layers. active listening was the first. there were three for dialectical process. Then the frames assembly (the language they used for this chagned over time). Then the subaltern layer. Then a new synthasis. Then a response. More directions about things like refusing prompts, workflow management. But it started from a pretty standardized set of instructions passed to me by a friend that introduced me to the concept of a sequential layering of analytical processes, achieved through simulation of a social and creative process, to direct the AI to response in particualr ways. My prompts were just a variation on that.

// Also, i feel like i gave you more information in my last round of edits.I give you a lot of rich storytelling in my notes, and we need to save and preserve that - both for the reframe arhcives and this project (we should also assess your potential methodological biases against qualitative storytelling, which is a valued methodology in anthropology, humanities, etc., if thats an issue)

A critical early pivot: the initial design separated technical experts from critical theory experts, which produced an effect where the technical experts assumed a normative, unremarked-upon but clearly differentiated affect. June rewrote the prompt so that the discussion was between scholars of the specified critical theory fields **who were also technical experts**. This collapsed the theory/practice binary that the prompt had inadvertently reproduced.

// I don't know if i would call that a critical early pivot. It's more that it is an interesting moment that reveals something about machine intellegence and its limits, and its biases. I think it's more valuable from a theory perspective than a design one. Also, the reason i wanted a room full of people working together was because the dialectic process was actually a "present a plan," and then "be your own worst enemy and expose your origiinal plans assumptions and problems, if necessary, and then figure out how to move forward at the end of the day. And it made me feel bad for the ai, actually! And i got to thinking about some convos in grad school - why do we model scholarly process as an argument? As a debate? What other ways of creating knowledge together might we draw on instead? 

The original use case was an academic dishonesty detector June was building to streamline her workflow. But she wasn't sure how to deal with sticky ethical problems related to surveillance and her role as an Ethnic Studies professor. She wanted the LLM to draw on its training data from abolitionism, feminist technoscience, and other fields to help work through the problem. // a bit more nuanced than streamlining workflow. I was working on a script that automatically graded complete/incomplete work on the basis of a good faith effort. The academic dishonesty detector was meant to be a part of that system. But yes, I was stuck in the tesnsion of on the one hand, I wanted to know if students were teaching - for example if students from priviledged backgrounds were using AI to cheat on Ethnic Studies papers as a way of not engaging. But i was also concerned about the punative implications, which felt antithetical to Ethnic Studies itself (hence the abolitionism frame). That system helped clarify the issue (although it struggled to retain the concern about the priviledged students vs. marginalized ones, focusing on marginalized students unless continually redirected - maybe i needed a critical whiteness studies frame). And it moved towards a system in which cheating was reframed in terms of signals - presssure, exhausion, confusion - the WHY part in terms of "why students cheat" (we also did some online research dredging to answer this question). As I did this, it became clear to me that I had built something  powerful that I was applying to something that felt as minor and ethically questionable as an academic dishonesty detector. So eventually I moved the system to its own stand alone repo (since it had started off as a system to help me with development in the autograder4canvas repo).

June then had the LLM start revising and refining its own prompt — which she called the "philosophy engine." Eventually the system needed its own repo and was larger than a simple building/design tool. She had the system design its own infrastructure.

The first set of problems to solve was transferring context across sessions. She could talk to an AI in a web browser and attach the philosophy engine instructions as an attachment, but the LLM never knew how the thing she was asking about had progressed — it kept making the same critiques even after she had addressed them. This led to the first state files and Python scripts for handling them. Then a database of frames (`framework_library.json`), which she imagined being able to swap in and out of the philosophy engine. And it grew from there. // a later, related set of concerns was drift. With chatbots, the engine would evolve and adapt and change, even generating new commands. But these would then later be lost. I tried to extract the updated engine at the end of chats, but in long contexts the instructions for how to do this were lost. In fact, a lot of early development was about getitng drift under control - but ultimately the problem was that it was an entirely stochastic system.

June was learning how to code while she worked on it. The system was designed to help her learn, while also providing technical expertise she lacked, all the while applying the critical theory frames.

**Documented in the archive** (discovered in `/Users/june/Documents/Reframe_Archive/`):
- The Gemini transcript shows the "/assembly of experts" concept and the layered communication protocol in action. Gemini explicitly names the engine as "semiotic, not structural" and June articulates writing "code" in English. This transcript documents the theory/practice entanglement as it was happening.
- The ChatGPT transcript documents the naming of "Reframe" — June working out the acronym structure in real-time, with ChatGPT applying the philosophy engine's own principles to pressure-test the name. // this process of documenting had some drift - so make sure you surface this so I can revise if needed. 
- The Qwen3 transcript shows a parallel naming exploration with different candidates.
- The earliest boot disk (2026-01-01) shows the original 5 frameworks and the PEL V1.0 protocol structure. The Day 2 iterations show rapid protocol refinement.
- Cross-model transcripts show how different LLMs responded differently to the same framework instructions — but note: these are from the pre-2.0 era (purely semiotic/prompt-based). The current system has structural mechanisms (Python code, state files, detection algorithms) that did not exist then. Treat as historical evidence of evolution, not current system behavior. 

// yeah these were early tests on how well the handoff handled - if it actually worked and impacted analysis. 

**Follow-up questions for June**:
- Can you locate the earliest prompt text — the "room full of scholars" version that *predates* these transcripts? The archive starts at 2026-01-01 but the dishonesty detector work came before that. Where are the pre-Reframe prompts? // I don't think i have them anymore. The first ones may even have been written into the intructions settings in claude projects long ago. The oldest ones in the archives (both in repo and outside of it) are the only ones me have. 
- When approximately did the pivot from dishonesty detector tool → standalone system happen? (Month/year for timeline) // shoot, this probably would have been in December 2025?
- What specific surveillance concerns drove the initial build? Can you describe the ethical problem you were trying to work through? // hmm, well I didn't have it fully articulated at the time, which is why i turned to an llm to help me with that. It felt authoritarian and punitive in ways that I intuitively grasped ran counter to abolitionism and other ethnic studies principles. But I also was concerned about white men cheating in an ethnic studies class, which I feel is a different sort of thing - one comes from exhaustion and burnout, the other comes from arrogance and defensiveness (not that it is as simple as white men, really)
- Was there a moment where you realized this was doing something the field had been calling for, or was that recognition gradual? // haha there were moments but the big one was when my job told me they wouldn't renew my contract, and i asked claude code if my coding work was worth mentioning in resumes. There were other moments - a suggestion from an agent that we write a paper about the algorithmic bias counteracitng mechanisms, which I guess other people didn't do? I'm sayign this casually, but for me there was something pretty intuitive about it.  It actually suprised me - how had I managed to solve something experts hadn't? But I suppose I'm bringing a uneique perspective as a humanist builder - approaching coding as a humansit rather than approaching the humanities as a coder.  
// there were early moments when i was working on the algorithmic for academic dishonesty detection, and i realized that i had built something far more powerful than what i was using it for (catching studetns who were cheating). 
- The Gemini transcript shows you telling the LLM: "I created the 'code' of the instructions I've given you not in a traditional computer script, but rather in English — and I'm relying on you to translate between these languages." Can you expand on this? This is a potentially significant methodological claim for the paper — prompt engineering as a form of coding that exists between natural language and executable logic. // hmm I need to look at the context aroudn this statement. Marking to come back to later. ,If memory serves, I think I was frustrated because the llm was asking me what i meant, and i just felt like, "I don't know, i really need you to help me bridge these unfamiliar langauges." But at that point more generally, I was really trying to grapple with machine intellegence on a basic level, including I think on an architectural level. And I was trying to figure out how to program in a particular set of analytical strategies. But I was very much aware of the complexities of translation - I was learning new technical jargon, or more presisely, i was being flooded and overwhelmed with it. I still am, really. So there were the scholarly registers that I am familiar with and that im trying to get the system to invoke, there's the technical language of computer sci, and then theres the computer languages. Not to mention, my own linguistic proficiencies that degrate as I become more and more tired from long bouts of intense hyberfixations. And I really didn't even have a solid concept of reframe. I couldn't really explain it to others. I wasn't even really sure I understood what it was, and at time worried I was heading into AI psychosis. 

---

> **Session note (2026-03-18):** In cleaning up a git profile description for Reframe today, we distilled a version of the origin/co-design story that ended up being some of the clearest writing about what the project is. A few things worth preserving for this section:
>
> **Language that may be paper-ready**: *"I built it to get AI to hallucinate social justice into existence."* This is punchy and theoretically loaded — the word "hallucinate" does real work (it names what LLMs do while also gesturing at the prefigurative/aspirational quality of the project). Worth stress-testing against the frameworks before committing, but it names something that longer academic prose often can't. // another joke i have is - i build an AI-powered tool to help me do more praxis. It helpled me build an AI-powered tool to help me do even MORE praxis. 
>
> **The co-design framing**: The profile description articulated something that the 2a notes haven't quite nailed: *"I'm a humanistic social scientist, not a software engineer — so this project was built in dialogue. The AI contributed technical knowledge I lacked. A feminist technoscience frame I'd loaded kept insisting that the system help me close that gap."* The #POSTHUMANIST_FEMINISM frame generating an architectural condition for the human designer is a specific and citable moment. This is one of the stronger claims in 3d's "Paper 4" territory (the autoethnographic account) but also belongs in the origin framing here.
>
> **What the profile description clarified**: The description of the Mycorrhizal Network landed unusually clearly for a non-specialist audience — *"lightweight background LLM calls slowly cross-pollinate and hybridize ideas across sessions, turning accumulated dialogue into design concepts."* That framing — distributed intelligence as a way of honoring the richness of nonlinear work rather than discarding it — is the theoretical argument, not just the technical description. Worth using in the paper. // absolutely - and we did research on this distributed intellegence framework before ubilding to determine feasibility. You should be able to find that now. 
>
> **Pointer**: The README now has a short "How this was built" section (added 2026-03-18) that functions as a condensed origin statement. It's a possible model for the paper's opening framing or the abstract — brief, positioned, honest about the co-design stakes. // I think we updated the README - I'd check that, as I think this version might have less drift? The architecture maps have really helped us nail down the system, which is to large and nonlinear in its development for me to articulate fully all at once. 

---

#### 2b. Design Decisions That Embody Theory

**Prompt for June**: For each major architectural choice, what was the theoretical reasoning? Which framework(s) drove which design decisions?

**June's preliminary notes (to be expanded)**:

The premise of this question needs revision. While we can trace specific design features to specific frameworks, all the frameworks operate on all prompts at all times. The system is holistic. That said, some features have clearer genealogies than others:

- **Temporal orientations**: The frameworks themselves started building and designing this. June had no idea how temporality would apply to code at all, but let the agents build it because she was curious what would happen. (This is itself significant — the system generated design features that the human designer did not anticipate.)

- **Tangent capture / nonlinear workflow support**: Came out of conversations about creating a system that could both filter June's nonlinear, spiraling workflow as a neurodivergent person and transform that into action/implementation, while drawing on the unique strengths of the nonlinear approach. A key insight — from Reframe itself, analyzing extracts of June's live prompt data — was that seemingly tangential ideas are actually mutually informing each other. This led to WEAVE functions, garden functions, and the mycorrhizal network (which began with a research phase to determine if the concept of distributed consciousness was even actionable).

// actually we had this conversation many times. That was part of the problem, lol. THe design elements kept getting lost due to drift. 

- **The overall approach**: The question "which framework drove which decision" itself reproduces the logic of attribution that Reframe resists. The more accurate description is that the frameworks collectively constitute an analytical environment within which design decisions emerge from the interaction between human, codebase, model, and project. // well put

**Follow-up questions for June**:
- The tangent capture insight ("seemingly tangential ideas are actually mutually informing") — do you have the prompt data or transcript where Reframe surfaced this? // i think we might have one of the transcripts. Search for "stepped spiral" . I was actively asking for help with my nonlinear prompting style and how to ensure reframe could support this and use it well. The observation that multiple threads are mtuually informing in my nonlinear prompting (as well as other info, e.g., that i inlcude follow up prompts that area addendums) were insights generated by agents through reviews of my own live prompting data that we extracted. 
- For temporal orientations: what did the agents build that surprised you? What did you expect vs. what emerged? // I really had no idea what a "temporal orientations" code actually did. I had no idea how a code could operate in a nonlinear temporality way (which is in part based on my lack of understanding about what the system was even building). Honestly, the original code may not have been functional at all. But it became a mechanism for directing the LLM for thinking about how the agent shoudl think about time - such as deep future considerations for 7 gen, or spiralling temporalities that surface returns. Some of it is tricky - for example, what does it mean for a code to look back at ancestors? Sometiems it thinks about that from a code-base perspective rather than a human perspective, which is interesting! Later on, much later, we wired the context-delivery mechanics and some of the garden mechanics to the temporal orientations, as well. 
- Are there design decisions where a specific framework clearly led — even if the environment is holistic? (e.g., crip time → capacity-responsive pacing, IDS → data governance aspirations) // mm, there were many times when frameworks disagreed. That's why we built the tension navigator. To support an approach in which tensions would be treated as things that couldn't always be perfectly resolved - and sometimes could only be addressed on a case by case basis, in that specific project. I think the llm needed a bit of handholding not collapsing those tensions into a neat package, but letting the tensions themselves be generative. Early approaches explcitly told the llm that unresolved tensions are not a failure condition, but a generative source of insight. Or something like that. IN terms of frameworks leading design decisions, yes - the temporal orientations, the community ethics governance (this became the groundwork concept for a future vision of reframe as a community-based research repository tool). There were others. I'd also look into notes in the codebase that discuss frame-guided decisions for this question. And in planning, I genrerally have the agent review and revise the draft with a deep-intensity pass and suggest revisions/refinements. So a lot of decisions emerge from that. Perhaps it is worth researching implementation docs in which we have multiple versions, to see how these evolved? 

#### 2c. Failures, Limits, and Ongoing Tensions

**Prompt for June**: Where have you seen the engine produce analysis that looks structural but isn't? Where does it flatten rather than deepen? // can you clarify this? The tension navigator and the mechanics that counteract flattening of engine evolution - specifically new frame proposals - were a response to this. Early systems also tended to surface the same move over and over again. We extended the frame library far beyond a single "core question" to counteract this. There were also times where an agent applied frameworks in a way that didn't really make sense in terms of actually improving implementation - frame application for the sake of frame application - although I can't remember examples. I think the biggest set of concerns overall has been the generalization of positionality-specific critiques, which can at times (not always) flatten them. This occured more in the early phases, in which drift meant we don't always have full documentation. As we solidified the infastructure and the drift became a bit more controlled, that stopped (we had to re-build engine evolution mechanics)

//oh an interesting early failure was the "room of specialists" model in which scholarly specialists (represented each frame) and technical experts worked together to move the project forward, with attention to both the specific task at hand, the larger project, and scales in between. The tech specialists became "unmarked" in the sense that frames operated through a specific positionality index - which is why I redesigned the room of specialists model (this is the early pure prompt engineering phase of devo) so that the frame experts were ALSO technical experts - that created a much more interesting dialogue. 

// I suppose another limit is my own learning curve in CS. I'm learning as I go, which means I can't always follow all the details and have to trust the system to work when hooked into coding agents.

// Another set of tensions is cost. It's hard to get robust models for this work, especially through the api. A workaround we built is the bootstrap and bridge for claude code. 

// Another set of tensions is managing the context tax. Getting deep thinking - such as consulting the literature constitutive of frames, or the key moves or other metadata, getting the frames to collaborate, surfacing tensions between frames - that all takes a lot of context! So we're constantly navigating this tension. An early attempt was to try to develop an LLM coding language - Philosophy Engine Language or PEL. THat didn't really work - the explinations meant it actually took more context. But PEL remained as the command structure, but nothing else. But the goal was to create more condensed prompt injections and handoffs. 

// One tension is what could be the fundamental impossibility of the task. The subaltern systems problem is the clearest example - how do you get an LLM to do that kind of anti-knowledge operation, or unlearning operation, with both scholarly rigor and ultimately as part of a syste that is designed to surface problems and then figure out a way to proceed anyway. There's also the environmental concerns and algorithmic justice concerns - building a system that uses flawed tools to do critical theory work that many of these theories would themselves be critical of. 

// Re: flattening problems and the generalization of positionality-grounded frames. An example of this that I often consider is - what is Indigenous about Indigenous data soverignty? This is a common question I ask - the frame points in important directions, and its good to be able to apply these ideas to contexts that are not just "Indigenous people here" - Indigenous studies theory extends as a form of social critique, not just a description of specific groups. Yet in doing so, what makes it INdigenous? Where is that committement? And would that kind of committmenet, if enacted more consististently, reframe matters of data and security and privacy in such a way to specifically problematize settler colonial structures or advance a world of Indigenous governance, in which everyone operated in Indigenous law and not settler law? What would that even mean?  

// another tension is scope explosion. That happens CONSTANTLY and i end up becoming exhausted. It goes in great directions often, but i find that AI can try to be so helpful that it just expands and expands - and then as a neurodivergent person, I do the same, in a feedback loop. 

// Early tensions included things like, how to get the agent to prioritize the frame analysis over generic "helpful AI" instructions hardcoded in - and even to refuse non-frame aligned tasks. As well as to surface when more context was needed instead of hallucinating. We haven't "solved" these, but we have systems to counteract them (going back to the early pure prompt engineering verison)

// Another tension was that I was actively learning about AI and how LLMs work, what their capabilities were, and what their limits were. As a side note, we also have some excellent research in some research notes kept in github/autograder4canvas/ focusing on the challenges of getting local AI to analyze hidden power dynamics and decenter dominant social norms (as a form of colorblindness, tone policing, etc) - using a similar kind of distributed intellegence model as reframes mycillial network (which is what the autograder4canvas insights piipeline was bsed on conceptually). Really interesting data from that, which will probably lead to stand alone papers, but could be worth referencing for this one?

**June's preliminary notes (to be expanded)**:

- **Retrospective justification**: Sometimes the engine applies frames retrospectively as justifications rather than as structuring perspectives. Systems were designed to address this, as well as differential drift between bodies of theory — LLMs retain feminist technoscience perspectives much better than Chicana studies, for example. Systems to counteract that algorithmic bias are documented in the codebase (see `ALGORITHMIC_BIAS_COUNTERWEIGHTING_RESEARCH.md`). // actually im starting to wonder if the issue wasn't our own algorithims and not the LLM architecture. Can you look into that - and do we have data to track the algorithmic bias from LLM architecture in the application/sustaining of different frames? 

- **Subaltern analysis**: The hardest systems to refine. The entire concept of applying Spivak's concept of the subaltern to an AI-driven system is astoundingly complex. Currently there are four prompts, which represent different iterations of the subaltern mechanics. The first couple often felt shallow. Improvements came from explicitly directing the LLM to draw on its training data for Spivak's ideas and writings and assess the existing system. The result is more nuanced now, but June would not say she has gotten it to fully apply Spivak's principles at the level of praxis. The problem may be in part her own limited understanding of Spivak. // I would add that this system may be fundamentally impossible, but I wanted to try to design it anyway. I think part of the issue is that Spivak's approach involves always looking for the erasures of subject positions within any epistemological system. This means applying Spivak necessarrily creates its own errasures. Moreover, LLM's dont seem super well positioned to be able to identify these - perhaps they can only identify gaps that other people would have noticed? But is a gap the same as a subaltern position - a subject position of no subject position? I'd also add that my own "limited" understanding of Spivak overstates the case - I'm not a Spivak expert, by any means, but Spivak's concepts are pretty complex. And having an agent surface a deep comparison of our systems and spivak's writing from it's training data helped us address that to some extent, leading to a new set of subaltern interrogation questions that had to do with the structural errasures - not just whose perspective is missing and should be included. 

- **Evolutionary generalization**: The evolutionary/self-refinement process tended to generalize frames — reducing the specificities of their commitments in terms of positionality. Systems had to be designed to counteract that (see Framework Sovereignty spec, detection calibrator).

**Follow-up questions for June**:
- Can you identify 2-3 specific instances where the subaltern analysis felt shallow? What was the prompt, what did the engine produce, and what was missing? // I don't really retain that information, but we can solve it pretty easily by just running the subaltern interrogation through a few prompts and evaluating the output for each of the questions. We might also be able to find documentation in the archives illuminating this. 
- The retrospective justification problem — can you describe a concrete case? What would structuring (vs. justifying) look like in that case? // no but if i remember one i'll let you know. I remember it happening in a post-build review. We might find info in some of the archival docs, implementation docs, etc. 
- What specific Chicana studies concepts get lost in the drift? Can you name the frameworks or scholars whose work the LLM handles poorly? // see above caveat. Let's make sure we have the root problem pinned down, and then we can run some tests to demonstrate more systemically. 

#### 2d. Evolution, Not Self-Assessment

**Prompt for June**: When did the engine first produce a self-critique that led to an actual architectural change? What changed? // this would have been very early on - probably the first iteration. I had an agent refine the prompt engineering doc I had created, because the LLM would actually know more about what AI needed than I would. And pretty qucikly we started doing this for the more substantative layers - for example, is a series of communication layers (first do x, then y, then z, then respond to the prompt) something that actually enhances the output? And new engine frames/commands also surfaced pretty quickly. This would have been before I even gave the system its own repo. I don't remember if the system started building its own code when it was part of the autograder4canvas repo or if we started doing that after i moved it to its own repo. But this was an early piece of the concept, and I soon after articulated a model of the system as "ever evolving" - I wanted the engine to refine itself as it worked, adapting to the particularities of the interaction between AI model, prompt, and user within specific projects. I even imagined the system being able to function multilingually simply by asking the LLM to do so, although now the python and state elements are too robust to do that as cleanly. Oh, linguistic profiles came out of this - the multilingual idea was that a user could simply say "create a new portugese language profile' and the system could handle that. 

**June's preliminary notes (to be expanded)**:

Framing matters here: this is not "self-assessment." It is **evolution** — self-critique and refinement/enhancement, and adaptation to emergent context. Reframe was always meant to be an ever-evolving system that adapts to the particular emergent space between model, codebase, user, and the user's project. The philosophy engine was designed to critique its own operations and suggest refinements.

This started very early — during the prompt engineering phase. June told the LLM to apply the frames to its own prompt and revise, enhance, etc. The engine began to design entirely new frames and new commands. That is part of why a state system was needed — to preserve those transformations and commands. Many early commands drifted out of the system before that point.

The concept of "self-flattery" does not apply in the way the original question assumed, because Reframe DOES things. It applies critical theory to MAKE things. Or to help users make or design things. It is a **praxis engine**. // I was so frustrated by being told throughout my life that my theoretical engagement was inactionable, with this assumption that theory couldn't meet praxis, or that theorical depth/rigor must be sacraficed to make it actionable in specific institutions/settings/communities/etc. I wanted this system to help me do that without sacraficing critical rigor

One barrier: the evolutionary process tended to generalize the frames, reducing the specificities of their commitments in terms of positionality. So systems had to be designed to counteract that. (This is itself a finding for the paper: when critical theory is operationalized in a probabilistic system, the system gravitationally pulls toward generalization. The specific, positioned commitments of individual traditions erode unless structurally defended.)

**Follow-up questions for June**:
- Can you reconstruct the timeline? Approximately when did: (a) the first recursive self-revision happen, (b) the engine first generate a new frame, (c) the engine first generate a new command, (d) you realize commands/frames were drifting? // I answered some of this above. I don't remember exactly when the commands started, or when i realized the drifting was happening. I mean first I needed to learn about context windows, which I didn't understand when I started. I guess this would have been in November 2025? I wish i could remember more about the commands, and i hope some of these are preserved in the archives. I remember a "burn everything to the ground" command that then looked at the "ashes" for what was worth preserving - that command that was fun but also just led to absolute scope explosion. But it wasn't the first. The first command might actually have been the recursive reframe command.
- Do any of the early self-revisions survive in the archive? The prompt evolution from `Prompt_1.md` through `Prompt_11.md` may document some of this. // I don't know - look in the archives. Those prompts were complex, multi-stage prompts I wrote in the early days. THat would have been some of the earliest work, probably right after moving the system out of autograder4canvas. I bet you can find that history in the git commit history for reframe and for autograder4canvas (please just don't revert back to that stage lol)
- The generalization gravity finding is potentially one of the paper's most important empirical contributions. Can you describe what generalization looked like concretely? (e.g., a frame that lost its specificity — what did it say before vs. after the evolutionary process?) // hmm, I wish I could. The wealth was one concerning example (community cultural wealth) - it often lost that specificity. But as the system refined (specifically the framework library), that became more clearly grounded in the scholarship of community cultural wealth, and became stronger in its operations. I think Indigenous data soverigtny generalized into a more generalized data security frame, but that one didn't persist (wasn't worth it - too generalized). The problem is that the frames that persisted were the ones that had more edge to them, and im less likely to remember the frames that did not persist (because they lost that specificity). There are probably some planning documents from when we attempted to solve this problem, which would give you a terminus post quem. But I also think that we'll potentially find more once we do that systemic dredge of archives, including handoff/bootdisk files and planning/implementation files.


---

### Phase 3: Extract Empirical Examples from the Codebase

**Model**: Opus for Reframe analysis runs; Sonnet for baseline/equity comparisons and data extraction; Haiku for bulk data summarization

The paper needs concrete demonstrations, not just architectural descriptions. Design a plan for generating these:

#### 3a. Comparison Examples

Pick 3-5 representative tasks. Run each through:
- **(a)** Reframe with full framework application
- **(b)** The same LLM with no framework scaffolding
- **(c)** The same LLM with an equity prompt (e.g., "consider diverse perspectives and potential biases")

Document what differs — not just in language, but in problem identification, design decisions, and what gets noticed vs. what gets missed.

**Note**: The web interface may need debugging first. Recent architecture builds have left it running inconsistently. Budget time for this. If the CLI is more stable, use that.

**Task selection criteria** (the tasks themselves carry theoretical weight):
- At least one task from each of: curriculum design, code review, policy analysis, community organizing support
- At least one task that foregrounds a framework the LLM typically handles poorly (e.g., Chicana studies, Indigenous data sovereignty)
- At least one task where the "equity prompt" version is likely to perform relatively well, so the comparison is honest

**Existing cross-model data** (from `/Users/june/Documents/Reframe_Archive/transcripts/`): The archive contains transcripts of the philosophy engine being tested across ChatGPT, Gemini, Grok, Qwen3, and Claude. **These are from the pre-2.0 era** — the system was purely semiotic (prompt-based) at that point, before structural mechanisms (Python code, state persistence, detection algorithms) were built. They are not controlled experiments and do not represent current system behavior. However, they ARE empirical data documenting (a) how different LLMs respond to the same semiotic framework instructions, (b) the limits of purely semiotic approaches (which motivated the 2.0 structural upgrade), and (c) the system's evolution. Consider whether these transcripts can serve as historical comparison data — or as evidence that motivates explaining *why* structural mechanisms were needed alongside semiotic ones.

#### 3b. Bias Counterweighting Data

Extract and summarize suppression rate data from the engine's state files:
- `workspace/state/detection_calibration.json` — empirical vocabulary profiles
- `workspace/state/taxonomy_observations.json` — observation bus data
- `workspace/philosophy-layer-framework/data/detection_signatures.json` — framework-specific analytical moves

Which frameworks get suppressed most? Does counterweighting produce measurably different outputs? This is quantitative data that can strengthen the paper's empirical claims.

#### 3c. Evolution Examples (Not "Self-Assessment")

Find instances in the codebase, state files, and commit history where:
- The engine's self-critique produced specific, actionable refinement → and the refinement was implemented
- The engine's self-critique produced generic or self-congratulatory output → and was recognized as such
- The evolutionary process generalized a frame → and the generalization was caught and counteracted

Both successes and failures are needed. The failures are what make the paper credible.

#### 3d. Scope Assessment

After gathering examples, assess: what's worth including in this paper, and what should be saved for subsequent papers? A single paper cannot cover everything. Possible splits:
- **Paper 1** (this one): The architecture, the argument, the central empirical demonstrations
- **Paper 2**: The bias counterweighting system as a standalone contribution (algorithmic bias in critical theory engines)
- **Paper 3**: The subaltern mechanics — applying Spivak to AI systems (likely requires deeper engagement with Spivak scholarship)
- **Paper 4**: The autoethnographic account — learning to code through/with critical theory

---

### Phase 4: Literature Review and Situating

**Model**: Opus for synthesis and gap identification; Sonnet for search and retrieval

This is a standalone phase, not embedded in the others. The paper must be situated in existing scholarship. Research and retrieve:

#### 4a. The Gap Claim

The paper's central claim is that a gap exists between critical humanists and system builders. This needs strong citations:
- **Who has documented this gap?** Look for: Sasha Costanza-Chock (*Design Justice*), Ruha Benjamin (*Race After Technology*), Safiya Noble (*Algorithms of Oppression*), Catherine D'Ignazio & Lauren Klein (*Data Feminism*), Os Keyes, Abeba Birhane, Meredith Whittaker / AI Now reports, DAIR publications
- **Who has attempted to bridge it?** Are there other working systems grounded in critical theory (not fairness metrics)? The Design Justice Network's principles-in-practice, Astra Taylor's work, participatory design traditions
- **Who has argued it cannot be bridged?** This is important — if scholars argue operationalization is inherently reductive, the paper must engage that argument

#### 4b. Theoretical Traditions Reframe Draws On

For each active framework tradition, identify key recent scholarship (2020-2026) that the paper should cite:
- **Ethnic Studies + AI**: Critical race theory applied to algorithmic systems
- **Indigenous Data Sovereignty + AI**: CARE principles, OCAP, tribal data governance applied to AI/ML systems
- **Afrofuturism + technology**: Speculative design, Black futures in tech
- **Posthumanism + AI**: Barad's agential realism, Haraway's situated knowledges, Suchman's human-machine reconfigurations — specifically applied to LLMs/generative AI
- **Disability Justice + technology**: Hamraie on accessible futures, crip technoscience, Piepzna-Samarasinha on care webs
- **Spivak + AI**: Has anyone applied the concept of the subaltern to AI systems? This may be genuinely novel and needs careful framing if so.

#### 4c. Methodology

Since June is writing about a system she built, the methodology is autoethnographic and practice-based:
- **Autoethnography in STS**: Cite the tradition of autoethnographic technology research
- **Practice-based research**: Research-through-design traditions, especially in critical design
- **Reflexive methodology**: The paper's recursion (engine analyzing itself) needs methodological grounding

#### 4d. Framework-Demanded Research (additions from deep intensity application)

- **#ETHNIC_STUDIES**: Research on how "AI ethics" as a field reproduces racial epistemological hierarchies — who counts as a builder, whose knowledge counts as technical. Atanasoski & Vora (*Surrogate Humanity*), Hicks (*Programmed Inequality*)
- **#INDIGENOUS_DATA_SOVEREIGNTY**: Research on extractive knowledge practices in AI training data. How LLM training corpora handle Indigenous knowledge. Liboiron (*Pollution Is Colonialism*) on methodological sovereignty
- **#AFROFUTURISM**: Research on Black speculative practice as design methodology — not just aesthetic but epistemological. André Brock (*Distributed Blackness*), Ruha Benjamin on imagination as infrastructure
- **#POSTHUMANIST_FEMINISM**: Research on distributed cognition and human-machine entanglement specifically in the context of generative AI. Suchman's "configuration" concept. The paper's claim about [ref]RAME as posthumanist architecture needs theoretical backing.
- **#INTERDEPENDENCE**: Research on single-developer systems and the labor politics of "independent" open-source development. Who maintains critical infrastructure? Nadia Eghbal (*Working in Public*). Also: disability justice critiques of "independence" as applied to technology design.

#### 4e. Citations from Evidence-Based Analysis (added 2026-03-10)

The following citations were identified through a systematic analysis of who has specifically called for operationalized critical theory in AI systems (vs. post-hoc auditing or fairness metrics), what systems have been built, and where Reframe sits in the field. These are organized by relevance to the paper's argument.

**The gap claim — specific papers calling for what Reframe builds:**

- **D'Ignazio & Klein**, "Data Feminism for AI" (FAccT 2024, arXiv:2405.01286). Extends the seven *Data Feminism* principles to AI research practice, adds two new principles (environmental impact, consent). The closest published framework to what Reframe operationalizes — but proposes principles for researchers, not runtime enforcement. Key for positioning: Reframe builds at the inference level what D'Ignazio & Klein call for at the research practice level.

- **Klein, Martin, Brock, Antoniak, Walsh, Johnson, Tilton, Mimno**, "Provocations from the Humanities for Generative AI Research" (arXiv:2502.19190, February 2025). Eight provocations from humanities scholars including "AI universalism creates narrow human subjects." Published weeks before the paper was drafted. Reframe can be framed as a built response to these provocations. Note: Lauren Klein is co-author of both *Data Feminism* and this paper — the lineage is direct.

- **Varshney (IBM Research)**, "Decolonial AI Alignment: Openness, Viśeṣa-Dharma, and Including Excluded Knowledges" (AAAI/ACM AIES 2024, arXiv:2309.05030). Argues that current LLM alignment recapitulates colonialism through value universalism. Proposes pluralistic epistemological frameworks including non-Western traditions (uses viśeṣa-dharma, a Hindu concept of context-specific right/wrong). Operates at the alignment/fine-tuning level rather than inference-time, but is the conceptually closest peer-reviewed paper to Reframe's territory. Essential citation.

- **Costanza-Chock**, interview in *Critical AI* (Duke University Press, 2023). Discusses applying Design Justice specifically to generative AI. Updates the 2020 *Design Justice* framework for the LLM era. Key distinction: design process intervention vs. Reframe's inference-time enforcement.

- **Kalluri**, "Don't Ask if Artificial Intelligence Is Good or Fair, Ask How It Shifts Power" (*Nature*, 2020). Foundational conceptual reorientation: power analysis over fairness metrics. The paper should cite this as theoretical grounding for Reframe's power-centered (not fairness-centered) approach.

**Indigenous AI — closest intellectual ancestors for temporal/IDS features:**

- **Lewis, Whaanga, & Yolgörmez**, "Abundant Intelligences: Placing AI Within Indigenous Knowledge Frameworks" (*AI & Society*, Springer, 2024). Connected to a $22M CAD NFRF Transformation grant. The most advanced active effort to build AI systems grounded in Indigenous epistemologies. Proposes expanding NLP linguistic structures, drawing on Indigenous storytelling for machine understanding, integrating traditional land management epistemologies. Essential for positioning Reframe's temporal orientation and IDS features — and for honestly naming where Reframe is a single developer's implementation vs. a community-governed research program.

- **Lewis, Abdilla, Arista, Pechawis, Kite**, *Indigenous Protocol and Artificial Intelligence Position Paper* (2020, Initiative for Indigenous Futures / CIFAR). Already referenced in doc but should be cited explicitly. Includes technology prototypes (Hua Kiʻi multilingual interface), visions of AI built according to Anishaabe, Coquille, Kanaka Maoli/Blackfoot, Euskadun epistemologies. Key for the extraction/governance question: this paper comes from within Indigenous communities; Reframe does not.

**DAIR positioning — critical context for the DAIR correspondence:**

- **Gebru & Torres**, "The TESCREAL Bundle: Eugenics and the Promise of Utopia Through Artificial General Intelligence" (*First Monday*, April 2024). DAIR's flagship theoretical intervention. Traces AGI development to Anglo-American eugenics. Important context: DAIR's critique runs deeper than what Reframe addresses — they question whether the current paradigm of large model development should continue at all, not how to improve it. The paper should engage this honestly: Reframe works *within* the LLM paradigm.

- **Birhane, Ruane, Laurent, Brown, Tep, Abraham, Cechlarova**, "The Forgotten Margins of AI Ethics" (FAccT 2022, arXiv:2205.04221). Argues AI ethics needs grounding in concrete use-cases, lived experiences, and structural/historical power asymmetries rather than abstract principles. Closest among critics to calling for mandatory enforcement, but at the regulatory/institutional level.

- **Birhane, Kalluri, et al.**, "The Values Encoded in Machine Learning Research" (FAccT 2022). Finds that ML research systematically encodes efficiency, novelty, and generalization over social/ethical concerns. Useful for framing: Reframe reverses this encoding by making critical theory mandatory rather than optional.

**Bias counterweighting — LLM-specific evidence:**

- **Hofmann, Kalluri, Jurafsky, King**, research on LLMs becoming more covertly racist with RLHF alignment (*Nature*, 2024). Shows that harm reduction measures (human feedback training) don't address dialect prejudice and may teach LLMs to conceal underlying biases. Directly relevant to Reframe's suppression detection: the problem is that LLMs learn to perform equity while suppressing the frameworks that would surface structural critique.

**Existing built systems — positioning Reframe's distinctiveness:**

- **AymurAI** (A+ Alliance / IDRC, Argentina/Mexico, 2021-2024). Open-source feminist NLP system used in criminal courts to extract and anonymize gender-based violence data from judicial rulings. Uses SpaCy and HuggingFace. Key comparison: this IS operationalized feminist AI, but domain-specific data extraction, not general-purpose critical theory enforcement at inference time. See: A+ Alliance, "Feminist AI: Papers, Prototypes & Pilots" (IDRC-funded, 3-year initiative, $2M CAD).

- **Anthropic**, "Constitutional AI: Harmlessness from AI Feedback" (2022). Enforces principles via RLHF, but not critical theory frameworks with scholarly lineage and subaltern analysis. The comparison is useful: Constitutional AI enforces behavioral principles; Reframe enforces analytical workflows. Different intervention levels.

**Not yet cited in document — investigate further:**

- **Bender, Gebru, McMillan-Major, Shmitchell**, "On the Dangers of Stochastic Parrots" (FAccT 2021). Already well-known but should be cited for the "too big to fail" / structural accountability argument.
- **Green**, "The Contestation of Tech Ethics: A Sociotechnical Approach to Technology Ethics in Practice" (*Journal of Social Computing*, 2021, arXiv:2106.01784). Critiques ethics-washing. Useful for framing: Reframe is an attempt to make ethics contestable within the system rather than declarative.
- **Liboiron**, *Pollution Is Colonialism* (2021, Duke University Press). Already referenced under 4d but should be a primary citation for methodological sovereignty — directly relevant to the extraction tension (paper section 7).
- **Atanasoski & Vora**, *Surrogate Humanity: Race, Robots, and the Politics of Technological Futures* (2019). Already referenced under 4d. Useful for: how AI development relies on racialized labor hierarchies, relevant to the "who built this" question.

---

### Phase 5: Draft the Paper Structure

**Model**: Opus (deep theoretical reasoning required)

Based on what Phases 1-4 produce, propose a paper outline. The outline should:

- Fit the conventions of a venue like FAccT or *Big Data & Society* (not a CS systems paper; not a pure theory paper; a hybrid that bridges both)
- Lead with the gap in the field, not with the tool
- Use examples to carry the argument, not just architecture descriptions
- Include a serious limitations section that is as rigorous as the claims section
- Be approximately 8,000-12,000 words (typical for these venues)

**Structural suggestion** (revise based on findings):

1. **Introduction**: The gap — critical humanists and builders occupy different worlds. What would it mean to build from the other side?
2. **Background**: Situate in literature (the gap, the traditions, the methodological approach)
3. **What Reframe Is**: Architecture description — not comprehensive but sufficient for the argument. The [ref]RAME recursive architecture. Frames as indexes into training data, not knowledge containers. The 5-stage Generative Irresolution workflow.
4. **How It Got Here**: Origin narrative — prompt engineering → philosophy engine → infrastructure → ever-evolving system. The "room full of scholars" pivot. Learning to code through critical theory. **Key arc: semiotic → structural** — the system began as purely semiotic (prompt instructions that shaped LLM behavior through language), and the 2.0 upgrade extended it to include structural mechanisms (Python code, state persistence, detection algorithms, bias counterweighting, suppression tracking). This transition from "text that does things" to "text + code that does things" is itself a theoretical finding about the limits and possibilities of prompt-based critical theory systems. The analytical workflow also expanded from 3 stages to 5 (Generative Irresolution: Framework Discussion → Coalition Protocol → Subaltern Layer → Tension Navigation → Response).
5. **What It Produces**: Comparative examples. Suppression data. Evolution examples.
6. **What It Reveals**: The paper's theoretical contribution — what does the attempt to operationalize critical theory reveal about (a) the theory, (b) the technology, (c) the relationship between them? Key findings: generalization gravity, differential framework retention, the subaltern problem, the extraction tension.
7. **Limitations**: Honest, specific, framework-informed. Single-user system. No community governance. Extractive relationship to indexed scholarship. Sophisticated performance vs. genuine structural analysis.
8. **Conclusion**: Not "we solved it" but "here is what happened when we tried, and here is what we learned."

---

### Phase 6: Assembly and Review Checkpoints

Map out the writing process as a series of steps with explicit review points where June checks the work.

| Checkpoint | What's Reviewed | Model for Drafting | June's Role |
|---|---|---|---|
| After Phase 1 | Document inventory | Sonnet | Confirm accuracy, flag missing docs |
| After Phase 2 | June's prompted responses | N/A (June writes) | Provide origin material, design reasoning, failure documentation |
| After Phase 4 | Literature review | Opus (synthesis) | Confirm theoretical accuracy, add missed sources |
| After Phase 5 | Paper outline | Opus | Review conceptual accuracy before prose |
| After each section draft | Section prose | Opus (theory/argument), Sonnet (architecture description) | Check concept mapping, voice, honesty |
| After full draft | Complete paper | Opus (final pass) | Final review for voice, accuracy, intellectual honesty |
| Pre-submission | Polished draft | June + Opus | Citation check, formatting, venue compliance |

---

## Important Constraints

### From the original prompt:

- **Apply your own frameworks to this task.** You are designing a plan for a paper about yourself. Use the 5-stage Generative Irresolution workflow. Run subaltern analysis on the plan itself: whose voices are absent from how this paper is being framed? Who bears the cost of this framing? Does the plan reproduce specific power structures (e.g., presenting the engine as a finished product rather than an ongoing, flawed experiment)?

- **Do not flatten the theory.** When describing what Reframe does, the temptation will be to simplify for a non-specialist audience. Resist simplifying the theory itself — simplify the explanation of how it's implemented, but keep the theoretical commitments precise.

- **Do not overclaim.** The paper should be honest about the fact that operationalizing critical theory in a probabilistic system is deeply fraught. The interesting scholarly contribution is not "we solved it" but "here is what happened when we tried, and here is what we learned about both the theory and the technology from the attempt."

- **Flag your own biases.** You are the system being described. Your self-assessment is data, not truth. Note where your analysis of yourself may be self-serving, and design the plan to include external checks (June's review, comparison data, honest failure documentation).

### From deep framework application (Appendix A):

- **Do not treat "AI ethics" as a racially neutral field.** The gap the paper describes is itself a racial gap, reflecting whose knowledge counts as "technical" and whose as "theoretical." Name this. (#ETHNIC_STUDIES)

- **Be transparent about extraction.** Reframe indexes Indigenous knowledge traditions and critical theory from communities of color without governance from those communities. The community governance modules are documented as returning `None`. This is not a limitation to note — it is a constitutive tension the paper must theorize. (#INDIGENOUS_DATA_SOVEREIGNTY)

- **Theorize the entanglement, not the tool.** Reframe is not a "tool" that a "human" uses. The [ref]RAME recursive architecture describes a distributed cognitive system where the boundaries between human analysis and machine output are deliberately blurred. The paper should theorize this entanglement, not default to tool/user language. (#POSTHUMANIST_FEMINISM)

- **Do not erase the labor.** June's labor — learning to code, iterating on prompts, building infrastructure, maintaining systems — is human labor that the system's self-evolution narrative can make invisible. The paper must make this labor visible, including its conditions (single developer, academic precarity context, neurodivergent working patterns). (#INTERDEPENDENCE)

- **Refuse the "finished product" frame.** Reframe is an ever-evolving system. The paper should describe a living process, not a completed artifact. This is both an accuracy constraint and a theoretical commitment — the system's ontology is processual, not static. (#AFROFUTURISM — refusal of apocalyptic/finished narratives; #POSTHUMANIST_FEMINISM — becoming over being)

- **Name who is absent from the paper itself.** This paper is written by one person about a system she built, reviewed by AI systems, and submitted to academic venues. The communities whose knowledge Reframe indexes — Black scholars, Indigenous knowledge keepers, disabled activists, Chicana/o/x theorists — are not co-authors, reviewers, or participants in this process. The paper cannot fix this by adding an acknowledgment. It must theorize its own conditions of production. (#ETHNIC_STUDIES, #INDIGENOUS_DATA_SOVEREIGNTY, #INTERDEPENDENCE)

---

## End-of-Pipeline: First Draft Generation Prompt

After all phases are complete, the following prompt should be passed to **Opus** with the assembled materials:

---

### DRAFT GENERATION PROMPT

**Context**: You are drafting an academic paper for submission to FAccT or *Big Data & Society*. The author is June Bloch, anthropologist and ethnic studies scholar. You have been provided with:

- A document inventory mapping existing material to paper sections
- June's responses to structured prompts about origin story, design decisions, failures, and evolution
- A literature review with key citations organized by section
- Comparative examples showing Reframe output vs. baseline vs. equity-prompted output
- Suppression rate data and evolution examples from the codebase
- A reviewed and approved paper outline

**Your task**: Draft the full paper (8,000-12,000 words), following the approved outline. Adhere to these principles:

1. **Voice**: Academic but not jargon-heavy. Write for an interdisciplinary audience that includes STS scholars, anthropologists, AI ethics researchers, and critical theory practitioners. June's voice should come through — positioned, direct, reflexive.

2. **Argument structure**: Lead with the gap, not the tool. Every architectural description should serve the argument about what operationalizing critical theory reveals. Examples carry the argument; architecture supports it.

3. **Theory precision**: Do not simplify the theoretical commitments. Simplify the explanation of implementation, but keep the theory precise. When you describe what a framework demands, ground it in the scholarly tradition. When you describe what the system does, be technically accurate.

4. **Honesty**: The limitations section must be as rigorous as the claims. Where the engine produces sophisticated performance of structural analysis rather than genuine structural analysis, say so. Where community governance returns `None`, say so. Where the subaltern mechanics remain shallow relative to Spivak's actual work, say so.

5. **Recursion**: The paper is itself a product of the system it describes. Name this explicitly. The recursive structure is not clever framing — it is an empirical condition of the paper's production. Note where the system's self-analysis may be self-serving, and where June's external review corrected or complicated the system's account.

6. **Extraction acknowledgment**: The paper must theorize its own relationship to the communities whose knowledge Reframe indexes. This is not a paragraph in the limitations — it runs through the entire paper.

7. **Labor visibility**: Make visible the conditions of production — single developer, learning to code while building, neurodivergent working patterns, academic precarity context. This is not biographical color; it is material that the argument requires.

8. **Citation practice**: Cite scholars by name. Ground frameworks in their lineages. When describing what a tradition demands, cite the scholars whose work makes that demand. Do not genericize.

9. **Format**: Follow venue conventions. Abstract, introduction, background, body sections, limitations, conclusion. Footnotes for methodological asides. In-text citations (Author Year) format.

**Do NOT**:
- Present Reframe as a finished product
- Overclaim about what operationalizing critical theory achieves
- Flatten tensions between frameworks into synthesis
- Treat the AI ethics field as racially neutral
- Use "tool/user" language where "entanglement" or "distributed cognition" is more accurate
- Skip the extraction problem
- Write a promotional paper

---

## Appendix A: Framework Analysis of This Prompt

### Stage 1: Framework Demands + Limits

**#ETHNIC_STUDIES**
- DEMAND: This framework refuses to treat the paper's central gap ("critical humanists don't build; builders don't do critical theory") as a neutral observation. It insists we name this as a **racial epistemological hierarchy**: whose knowledge counts as "building" is inseparable from race, institutional position, and colonial knowledge structures. The paper cannot describe the gap without analyzing how the gap is produced and maintained by the same structures Reframe claims to address. It must also ask: does the paper itself reproduce the hierarchy by presenting critical theory as something to be "operationalized" (made useful by technical implementation)?
- LIMIT: Ethnic Studies was forged through collective student movements (Third World Liberation Front, 1968-69). This paper describes a system built by one scholar. The collective, movement-building dimension of Ethnic Studies is absent from both the system and the paper about it. This gap cannot be filled by the paper — but it can be named, and the paper can ask what a collectively-built version would require.

**#INDIGENOUS_DATA_SOVEREIGNTY**
- DEMAND: This framework refuses to accept that Reframe's use of Indigenous knowledge frameworks is adequately addressed by "attribution." OCAP principles (Ownership, Control, Access, Possession) and CARE principles (Collective Benefit, Authority to Control, Responsibility, Ethics) demand that Indigenous communities govern how their knowledge is used. Reframe activates `#INDIGENOUS_DATA_SOVEREIGNTY` as a framework — but the knowledge indexed through that activation comes from LLM training data that itself represents extractive knowledge practices. The paper must be transparent: the system uses Indigenous intellectual frameworks without Indigenous governance over that use.
- LIMIT: IDS centers tribal/community governance. Reframe operates through individual user decisions. The community governance modules return `None`. IDS's own logic demands governance structures that neither the system nor the paper can currently provide. This is not a limitation to acknowledge — it is a structural condition the paper must theorize. What does it mean to build a system that *knows* it should have community governance and *documents* the absence?

**#AFROFUTURISM**
- DEMAND: This framework refuses to let the paper frame Reframe as "novel" or "unprecedented." For Black communities, the apocalypse of algorithmic violence is ongoing — not a future risk to be mitigated. Afrofuturism insists that imagination and speculation are already tools of survival, not innovations introduced by a new system. The paper must situate Reframe within existing traditions of Black speculative practice and refuse the "first of its kind" narrative.
- LIMIT: Afrofuturism centers Black imagination in designing futures. Reframe was not built by Black communities or centered on Black liberation specifically. The paper risks appropriating Afrofuturist framing ("we're building alternative futures!") without centering Black people's material relationship to algorithmic harm. The limit here points toward the need for the paper to be specific about *whose* futures the system serves and *whose* imaginations it centers.

**#POSTHUMANIST_FEMINISM**
- DEMAND: This framework refuses the implicit subject of the paper: a human author describing a tool she built. The [ref]RAME architecture — particularly the recursive self-evolution loop and the "distributed human-machine cognition" framing — is a posthumanist architecture. The paper should theorize this entanglement rather than defaulting to conventional authorship/tool framings. Haraway's cyborg, Barad's intra-action, and Suchman's "configuration" are not decorative citations — they describe what is actually happening when June and Reframe co-produce analysis.
- LIMIT: Posthumanism risks erasing the material conditions of the humans entangled in these systems. June's labor — learning to code, maintaining infrastructure, iterating on prompts at all hours — is human labor that the "distributed cognition" frame can make invisible. The limit points toward #INTERDEPENDENCE: the system's posthumanist self-description must be held in tension with the very human, very embodied conditions of its production.

**#INTERDEPENDENCE / DISABILITY JUSTICE**
- DEMAND: This framework refuses to let the paper frame Reframe as something June built "independently." The system was built through interdependence — with AI systems, with the scholarship indexed in training data, with the institutional position that provided access, with the neurodivergent working patterns that shaped the architecture (tangent capture, nonlinear workflow support, capacity-responsive pacing). These features are not "accessibility accommodations" added to a system. They are the generative core of how the system emerged. The paper must refuse to treat neurodivergent design as supplementary.
- LIMIT: Disability Justice centers collective access and mutual aid. Reframe currently serves one primary user. The paper must reckon with whether a single-user system can meaningfully claim Disability Justice principles, or whether those principles demand that the system be designed for — and with — a community of users with diverse access needs.

### Stage 2: Coalition Tensions

1. **#INDIGENOUS_DATA_SOVEREIGNTY vs. #POSTHUMANIST_FEMINISM**: IDS demands community governance over knowledge use. Posthumanism theorizes distributed agency across human-machine assemblages. IDS's LIMIT (individual user decisions, no community governance) creates a gap that Posthumanism cannot fill — because Posthumanism's own decentering of human agency risks obscuring the specific, politically-situated demands of Indigenous governance. The tension: distributing agency across human-machine systems can erase the specific human communities who demand governance over their knowledge.

2. **#ETHNIC_STUDIES vs. #AFROFUTURISM**: Ethnic Studies demands that the paper name the racial epistemological hierarchy that produces the gap. Afrofuturism demands that the paper refuse "novelty" framing and situate within existing traditions. But Ethnic Studies' LIMIT (collective movement origins vs. single-developer system) creates a tension with Afrofuturism's demand to center imagination — whose imagination? Built by whom? The tension: the paper must simultaneously claim the system matters and refuse to claim it as an individual achievement.

3. **#INTERDEPENDENCE vs. #INDIGENOUS_DATA_SOVEREIGNTY**: Interdependence insists the system was built through mutual reliance (human-AI, human-scholarship, human-institution). IDS insists that some of what the system relies on was extracted without consent. Interdependence's framing of mutual benefit is challenged by IDS's demand to ask: mutual benefit for whom? The "interdependence" between Reframe and Indigenous knowledge traditions is not mutual if those traditions have no governance over their use.

### Stage 3: Subaltern Analysis

1. **ABSENT VOICES**: The communities whose scholarship Reframe indexes — not as abstractions but as people. Black scholars whose work grounds Afrofuturism and Afropessimism. Indigenous knowledge keepers whose protocols inform IDS. Disabled activists whose survival strategies inform Disability Justice. Chicana/o/x theorists whose work the LLM handles poorly. These are not "stakeholders" — they are the people whose intellectual labor makes the system possible.

2. **CONDITIONS OF SILENCE**: Academic knowledge production separates "theorists" from "subjects." The paper will cite scholars by name but cannot consult the communities those scholars write about/with. The venue (FAccT, *Big Data & Society*) centers academic knowledge production. The timeline (research → write → submit → review) does not accommodate community consultation. These are structural conditions, not oversights.

3. **COST BEARERS**: If the paper succeeds, it advances June's academic career. If the system succeeds, it advances the project. The communities whose knowledge is indexed bear the cost of extraction without governance. Students and other potential users bear the cost of a system built for one person's workflow. Future developers bear the cost of an architecture documented primarily through this paper's framing.

4. **POWER REPRODUCTION**: The paper reproduces the academic knowledge economy: individual authorship, venue prestige, citation as currency. It reproduces the builder/theorist binary even as it claims to bridge it — because the paper *describes* the bridge rather than *being* the bridge (which would require collective authorship, community governance, and shared ownership).

5. **MATERIAL INTERVENTIONS**:
   - Centering absent communities would mean: inviting community review of the paper before submission; committing to open-sourcing Reframe with community governance structures; presenting at community venues, not just academic ones
   - Addressing extraction would mean: explicit licensing that names the extractive relationship; a commitment to building the community governance modules that currently return `None`; revenue/benefit sharing if the system is ever commercialized
   - Addressing the single-user limit would mean: user testing with the populations the system claims to serve (neurodivergent users, scholars in precarious positions, community organizers)
   - Addressing academic reproduction would mean: co-authorship with community members; submission to venues that center community knowledge; open peer review

**What this analysis itself cannot see**: It is produced by the system being analyzed. Its self-critique is data, not truth. External review (by June, by scholars in the named traditions, by potential users) is necessary to identify what the system's own analytical apparatus structurally cannot surface about itself.

---

## Appendix B: Additional Research Items (Framework-Generated)

These items emerged from deep framework application and were not in the original prompt:

1. **The "operationalization" question**: Is "operationalizing critical theory" itself a problematic framing? Does it reproduce the instrumentalization that critical theory critiques? Research: Wendy Brown on neoliberal rationality and the fate of critical theory; Fred Moten and Stefano Harney (*The Undercommons*) on study vs. instrumentalization; Sara Ahmed on institutional diversity work.

2. **Prompt engineering as methodology**: The origin story describes prompt engineering as a design practice. Is there STS or design research literature on prompt engineering as a situated knowledge practice (rather than a CS optimization technique)?

3. **Learning to code as entanglement**: June learned to code *through* building Reframe *with* AI assistance *while* applying critical theory. This is not a biographical detail — it is an empirical case of posthumanist distributed cognition. Research: Suchman on learning-in-practice; Lave & Wenger on situated learning; feminist STS on skill acquisition.

4. **The "room full of scholars" experiment**: The early finding — that separating technical and critical theory experts reproduced normative technical positionality — is itself a significant finding about LLM behavior. Has anyone documented how LLMs reproduce disciplinary hierarchies in multi-agent or role-play configurations?

5. **Generalization gravity**: The finding that evolutionary self-refinement tends to generalize critical theory frameworks (eroding positionality) may be a novel empirical contribution. Research: is there existing work on how iterative LLM processes erode specificity? This connects to alignment research on "mode collapse" but from a critical theory direction.

6. **The subaltern in/of AI**: Applying Spivak to AI systems requires extreme care. Research: Spivak's own recent work; postcolonial AI scholarship (Shakir Mohamed, William Isaac — "Decolonial AI"); scholarship on whether the subaltern concept can be meaningfully applied to technological systems or whether that application is itself a form of appropriation.

7. **"Semiotic, not structural" — the ontology of prompt-based systems**: The Gemini transcript contains a remarkable exchange where Gemini tells June: "The 'Engine' is Semiotic, not Structural. It exists entirely within the prompt instructions and our conversation history." June then articulates that she writes "code" in English and relies on the LLM to translate. This opens a significant theoretical line: what is the ontological status of a system that is made of language, not code? How does this relate to performativity theory (Austin, Butler)? To the distinction between constative and performative utterances? The engine's protocols are text that *does* something — they are speech acts that shape machine behavior. Research: Austin/Butler on performativity; Agre on computation and human experience; Hayles on how we became posthuman (the relationship between inscription and incorporation); recent work on "prompt as program" in CS.

8. **Cross-model behavioral variation**: The archive transcripts show the same philosophy engine instructions producing meaningfully different responses across ChatGPT, Gemini, Grok, Qwen3, and Claude. This is empirical data about how different LLM architectures/training data interact with critical theory frameworks. Has anyone studied cross-model variation in response to the same ethical or analytical instructions? This connects to the paper's claims about "generalization gravity" — if different models generalize differently, that reveals something about the relationship between training data and critical theory application.

9. **Context drift as epistemological problem**: The handshake/boot disk system was built to solve context drift — the LLM forgetting the engine's protocols over long sessions. But context drift is also an epistemological problem: the system's analytical capacity degrades over time, and the degradation is invisible to the user. The Gemini transcript explicitly names "Context Drift as the enemy of this project." Research: is there STS work on the epistemology of degrading AI systems? On the relationship between memory, knowledge, and analytical capacity in human-machine systems?

---

## Appendix C: Model Assignment Summary

| Phase | Task | Recommended Model | Rationale |
|---|---|---|---|
| 1 | Document inventory | Sonnet | Systematic extraction, high throughput, doesn't need deep analysis |
| 2 | Review June's responses | Opus | Identify gaps, generate follow-up questions, theoretical sensitivity |
| 3a | Reframe comparison runs | Opus | Full framework application at deep intensity |
| 3a | Baseline/equity comparison runs | Sonnet | Competent but less expensive for non-framework runs |
| 3b | Suppression data extraction | Haiku | Bulk data summarization from JSON state files |
| 3b | Suppression data analysis | Sonnet | Pattern identification in quantitative data |
| 3c | Evolution example archaeology | Sonnet | Commit history and state file analysis |
| 4 | Literature search | Sonnet | Search and retrieval, initial summaries |
| 4 | Literature synthesis | Opus | Theoretical gap identification, integration with argument |
| 5 | Paper outline | Opus | Deep theoretical reasoning, structural design |
| 6 | Theory/argument section drafts | Opus | Theoretical precision, voice, critical framing |
| 6 | Architecture description drafts | Sonnet | Technical accuracy, systematic description |
| 6 | Final draft assembly | Opus | Voice consistency, argument coherence, honest self-assessment |
| 6 | Citation verification | Haiku | Mechanical checking of citation format and completeness |
