# Neurodivergent PKM — Research Landscape

**Compiled from**: research agent findings, 2026-04-15  
**Assessment**: Literature is thin academically but practitioner community is extensive and genuinely innovative

---

## Academic work (the thin part)

**"Neurodivergence and Personal Knowledge Management Across Life Domains"**
- Journal: *Including Disability* (Ontario Tech University / Scholars Portal)
- URL: https://ojs.scholarsportal.info/ontariotechu/index.php/id/article/view/244
- 300+ self-identifying neurodivergent adults. Specifically excluded neurotypical controls — not a deficit comparison study.
- Key finding: PKM benefits span ALL life domains, not just employment/productivity. Argues PKM should be studied relative to neurodivergent people's OWN goals.
- This framing (PKM as life support, not productivity optimization) is directly relevant to a researcher whose intellectual work doesn't divide into "academic" and "personal."

**"Designing a PKM System for People with ADHD"**
- DiVA Portal (Swedish university thesis): https://www.diva-portal.org/smash/get/diva2:1777365/FULLTEXT02.pdf
- Design research: voice-to-task automation, adaptive to-do structures, flexible categorization reduce cognitive overload
- Core finding: systems should adapt to natural thought flow, not impose external structure
- This is the structural critique of mainstream PKM applied empirically.

---

## Community practice (the rich part)

**Key insight from Jesse Anderson (Extra Focus, 50k subscribers):**
> Novelty-seeking is a *feature* of ADHD cognition, not a bug. Systems need to *accommodate* it, not suppress it.

This reframes the design problem: not "how do we help ADHD users maintain consistent systems" but "how do we design systems that are generative for associative, novelty-driven minds."

**Key insight from Marie Poulin (Notion Mastery, ADHD-diagnosed PKM consultant):**
- Visual hierarchy, reduced decision load, flexible structure over rigid folders
- Notion's lack of imposed structure is a feature for neurodivergent users — you build structure around how you actually think

**Yaranga** (2025, early-stage): https://yaranga.net/
- Explicitly designed for ADHD/anxious minds
- AI-mediated automatic organization — you capture in natural language, Yaranga organizes behind the scenes
- No folder hierarchies; automatic task extraction from freeform notes
- This is the "third option" direction: rather than teaching ND users neurotypical systems, design a system that doesn't require neurotypical executive function
- Adoption early; evidence anecdotal — worth watching

**Obsidian community ADHD patterns** (forum-sourced, genuinely tested):
- Daily notes as low-pressure capture
- Emergent structure from observed patterns, not imposed taxonomy
- "On This Day" plugin actively resurfaces buried notes (counters out-of-sight/out-of-mind)
- Graph as navigation, not organization
- Rule: simplest system you'll actually use beats elegant system you'll abandon

---

## What this means for our design

### Design constraints from ND research:
1. **Capture must be frictionless** — if the write operation has decision points (where does this go? what is it?) it won't happen
2. **Structure should emerge, not be imposed** — this means designing the ingest pipeline to suggest structure rather than require it
3. **Novelty accommodation** — the system should surface new/unexpected connections, not just confirm existing ones (InfraNodus does this)
4. **No hidden maintenance cost** — systems abandoned when maintenance accumulates invisibly. The lint/health check operation should be explicit and schedulable.
5. **Out-of-sight/out-of-mind is a real problem** — the system needs active resurfacing mechanisms, not just passive storage

### The voice memo pipeline as ND write loop:
The existing `mlx_whisper` → transcription pipeline is already the right instinct. Voice is the lowest-friction capture method. The gap is what happens AFTER transcription — currently ad hoc filing. This should be the first build priority: transcription → structured ingest → indexed memory.

### On "de-atomizing" context:
June's prompt asks: how do we store relationships, not just atoms? The research suggests:
- Atomic notes + explicit relationship types (A-MEM model) is better than files + implicit links
- InfraNodus-style network analysis on top of atomic notes surfaces emergent relationships
- Block-level linking (Logseq) captures relationships at a more granular level than file-level linking (Obsidian)

The question "how do we de-atomize context" may be better asked as: "how do we make the relationships between atoms first-class, not second-class?" The atoms are still useful; what we want is rich relationship metadata.
