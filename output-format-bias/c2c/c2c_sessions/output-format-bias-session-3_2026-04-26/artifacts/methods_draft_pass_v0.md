# Methods Section — Draft Pass v0 (Interface Pane)

**Date:** 2026-04-27 PM
**Author:** Interface pane (Claude), drafting from architecture map + political-context survey + s3 outline + bibliography
**Status:** **Starting point for June to revise.** Voice-carrying personal-narrative passages are explicitly marked `[J: revise voice]` and June should rewrite or replace them. The architectural-pedagogical mapping in III.C ¶2 is drafted with substance because the connection is empirical-architectural (not personal); June can revise framing or push back if the mapping is off.
**Inheritance:** s3 paragraph-level Framework outline (`framework_outline_paragraph_level.md`); insights architecture map; political context survey; merged bibliography.
**Note:** This is v0 — explicitly preliminary. Expect revision.

---

## Section III.A — Institutional context (drafted ~280 words; trim or expand per June)

This research was conducted in the context of a community-college Ethnic Studies course in California in Spring 2026. The instructor — author of this paper — was responsible for a teaching load of approximately 170 students across multiple sections without a teaching assistant, on a consumer-grade laptop with 16 GB of RAM. The classifier evaluated here was not built as a research artifact; it was built as a survival tool to make the labor of caring for that many students attentively across a single semester possible. The methodological commitments documented in this paper — that institutional conditions are constitutive of the research rather than bias to be corrected for — follow from this fact. The system was designed inside the conditions it was meant to address.

The Spring 2026 semester intensified those conditions in specific ways relevant to the system's architecture. California had codified Ethnic Studies as a graduation requirement at the same moment that federal immigration enforcement escalated in the Central Coast region — coordinated ICE raids in Watsonville, Santa Cruz, and Pajaro Valley in January 2026 — and the Department of Education moved against diversity, equity, and inclusion programming at the federal level. Students entered Ethnic Studies classrooms carrying simultaneous political crisis and academic obligation; instructors carried the contradiction of teaching a state-mandated curriculum about racial and structural inequality inside an apparatus that was actively criminalizing the communities the curriculum is most legible to. The classifier needed to distinguish between burnout — capacity-failure under load — and crisis-navigation — full capacity directed toward urgent political reality — because the two failure modes look superficially similar in writing but require opposite pedagogical responses.

`[J: revise voice — particularly the second paragraph's framing of the political moment and your relation to teaching inside it. The substantive content is in the political-context survey at` research/political_context_survey_2026-04-27.md `; what's drafted here is a sketch June can replace with the version that lands in her register. The Tuesday-afternoon-noticing-moment material the bibliography survey surfaced should land somewhere around here or in the hook — June's call where.]`

---

## Section III.C ¶2 — Pedagogical lineage and architectural mapping (drafted ~340 words)

The Insights pipeline architecture draws on a pedagogical lineage running through Martha Caldwell's research on facilitating dialogue across difference. The lineage is consistent across a decade of work: Caldwell's 2012 article *"Inquiry into Identity: Teaching Critical Thinking through a Study of Race, Class, and Gender"* establishes identity-as-inquiry as a pedagogical practice — students examine how race, class, and gender operate in their own lives as a method of building structural analysis rather than as a confessional gesture. The 2016 book *Let's Get Real: Exploring Race, Class, and Gender Identities in the Classroom* (Caldwell and Oman Frame) extends the practice into a structured teacher resource for facilitating those conversations across difference, naming how dialogic structure — not individual disclosure — does the analytical work. The 2022 book *Facilitating Conversations about Race in the Classroom* (Stewart, Caldwell, and Hawkins) carries the line into practitioner-facing facilitation for K-12 educators. Across all three works, the consistent commitment is that identity disclosure is information about systems, not pathology; that dialogue is the architecture; and that the teacher's job is not to extract or evaluate but to facilitate the conditions in which the inquiry can happen.

The Insights pipeline reflects this lineage in specific architectural decisions. The synthesis-first class reading stage (`class_reader.py`) reads all student submissions as a community before evaluating individual students, on the principle that an individual's writing is legible only inside the conversation it sits within — a banking-model alternative the system makes structural rather than aspirational. The asset-framed ENGAGED slot in the 4-axis classifier provides the model with a non-flagging option for students doing the work *with* righteous anger or lived-experience grounding — a structural refusal of the tone-policing reflex Caldwell's work names as the failure mode of well-intentioned facilitation. The equity-protective prompt language explicitly distinguishes identity disclosure from wellbeing signal, encoding the analytical move Caldwell's pedagogy makes at the level of teacher practice. None of these architectural choices were derived from Caldwell's work as a citation exercise; they emerged from teaching inside the pedagogical lineage and trying to build a system that would not dismantle what the pedagogy was trying to do.

`[J: revise voice — particularly the last sentence. The substance of the connection is right per the architecture map, but how you actually came to design these things in conversation with your mother's pedagogy is yours to write. Push back on the mapping if I've got it wrong; the architecture map at` research/insights_architecture_map_2026-04-27.md `is the source.]`

---

## Notes for s4

- Section III.B (synthetic test corpus + Buolamwini & Gebru rationale) and III.D (primary model + cross-family testing) are not drafted here — they're empirical-methodological and don't depend on June's voice. s4 can draft from the s3 outline directly.
- Section III.E (classifier provenance / calibration-and-recovery history) was drafted in the s3 outline; the post-close addendum points to `binary_fix_attempts_enumeration_2026-04-27.md` as the input that lets III.E enumerate the 8 specific mechanisms tried on the binary path. Suggest threading those names into III.E rather than just gesturing at "various calibration interventions."
- Both drafted passages above are approximately at the target paragraph length from the s3 outline. III.A may need to compress; III.C ¶2 lands close.
- The pedagogical-lineage paragraph in III.C ¶2 should connect forward to the Findings preamble / III.E enumeration — the eight fix attempts include several (equity-protective prompts, anti-bias post-processing, the synthesis-first class reading, the ENGAGED slot) that the III.C ¶2 paragraph names as architecturally encoded. The forward-pointer makes the architectural-pedagogical claim non-trivial: it's not just that the architecture *encodes* pedagogy, it's that the architecture's pedagogical commitments survived through eight attempted bias-mitigation iterations and shaped which iterations were tried at all.

---

*Interface pane draft, 2026-04-27 PM. v0. Not voice-checked; voice work explicitly marked for June's revision. The architectural-pedagogical mapping is the load-bearing analytical work in this draft pass; the institutional-context paragraph is a sketch.*
