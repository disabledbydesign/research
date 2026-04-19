# Fieldnote: Compression Function Across Four Scales

**Date**: 2026-04-17  
**Session**: Dr. L. June Bloch + Claude Sonnet 4.6 (liberation_labs exploratory session)  
**Context**: Connecting June's Autograder binary format finding to Liberation Labs KV-cache research, Kintsugi infrastructure analysis, and relational ontology framework  
**Status**: Raw theoretical framework — internally coherent, empirically grounded at two scales (cognitive, infrastructural), predictions at two scales (relational, political-economic). Potentially publishable; needs empirical grounding pass and write-up.

---

## The Compression Function Framework (Bloch)

**Core move**: "Bias is in the output format" (Autograder finding) generalizes to **bias is in the compression function**. The same structural pattern operates at four scales. Each scale has a compression mode that collapses specificity toward dominant norms, and a generative observation counterpart that preserves specificity.

| Scale | Compression Mode (produces bias) | Generative Observation Mode (preserves specificity) |
|---|---|---|
| **Cognitive** | Binary classification ("is this complete: y/n") | Generative observation ("describe what you notice") |
| **Relational** | Property assessment ("does entity X have consciousness?") | Relational observation ("what emerges in the relational field?") |
| **Political-economic** | Monetary valuation (compresses labor to price) | Time banking / gift economy (lawyer's hour = gardener's hour) |
| **Infrastructural** | Keyword routing (maps to pre-existing categories) | Semantic / intent-based routing (reads what the request actually is before routing) |

**Each case**: a compression function in service of dominant norms collapses specificity toward the center that benefits those norms. Different compression functions at different scales, doing the same structural work.

---

## Empirical Grounding

**Cognitive scale** — *replicated*: Autograder's binary format study (P/P2/P3). Binary classification format activates deficit bias in student assessment; generative observation format eliminates it. Behavioral result; geometric prediction (H2) untested.

**Infrastructural scale** — *documented in source code*: Kintsugi-CMA routing table analysis (2026-04-16). The skill chip routing table contains entries for `finance`, `accounting`, `investment`, `profit` (and variants). It does not contain entries for `mutual aid`, `solidarity`, `coalition`, `cooperative`, `time bank`. In a system explicitly designed for prosocial values, the routing function privileges dominant economic categories. The compression function made visible in code.

**Relational scale** — *predicted, untested*: The relational ontology touchstone's move (shift from property-based to relational inquiry) can itself be assessed as a shift from compression mode (property assessment) to generative observation mode. Connection to B2 "bliss attractor" finding (Reframe Phase 4): attractor state compresses relational complexity toward mystical resolution.

**Political-economic scale** — *predicted, theoretical*: Financial reasoning dominating when alongside mutual aid reasoning in prosocial systems. Kintsugi's routing asymmetry is the entry point; full empirical grounding would require observational data on which requests get routed where.

---

## Design Principle: Generative Observation at Every Layer

The counter-structure is not just critique — it's a design principle. For each scale where compression produces bias, there's a corresponding mode that preserves specificity by describing rather than categorizing.

**For the Profile project** (memory architecture): At every layer where the system could compress — routing, consolidation, retrieval, interface — the architecture must use generative/semantic observation. Compression reasserts normative gravity at any layer where it isn't actively resisted. The mycorrhizal solution (fast/slow LLM division of labor) makes this economically viable.

**For Reframe**: The frameworks must be applied in a way that preserves the relational specificity of the inquiry — not as categorical slots that compress the material into pre-existing framework categories.

---

## Connection to Existing Reframe Work

**Normative gravity** (Bloch, cited throughout Reframe welfare work): The compression function is the mechanism through which normative gravity operates. Normative gravity is the pull; the compression function is the lever. Naming the compression function makes the mechanism more precise and more actionable.

**B2 attractor state finding** (Phase 4): The bliss attractor compresses consciousness discussion toward mystical resolution — this is the relational-scale compression mode in action. The geometric finding (effective rank change) is a potential empirical marker of compression vs. generative observation at the relational scale.

**Context as activation function** (touchstone): Output format as activation function is the cognitive-scale instance of the same principle. The touchstone generalizes this; the compression function framework gives it a cross-scale structure.

---

## What's Still Needed

- **Empirical grounding at relational and political-economic scales** — the framework holds at cognitive (Autograder) and infrastructural (Kintsugi routing code), but the other two scales are predictions, not results.
- **The normative gravity paper** — this concept is doing significant theoretical work across Autograder, AI welfare, and now this framework; it needs its own treatment for an external audience (not yet defined for outside readers).
- **Write-up pass** — the theoretical framework is ready; the paper draft is not.

---

## Parked: H7 (EFE Philosophical Critique — Separate Reframe Session)

**Question**: Does active inference's "minimize surprise" principle carry conservative bias? The foundational commitment of active inference (maintaining boundaries against entropy / minimizing free energy) may have a normative valence that's invisible to the framework itself.

**Kintsugi context**: Kintsugi's EFE calculator weights risk/ambiguity/epistemic per domain. Finance domains get risk-heavy weights (0.6). Fundraising gets epistemic-heavy (0.4). The question is not whether these weights are wrong — it's whether the three-weight decomposition is a sufficient ontology for ethical decision-making, or whether it misses relational/political dimensions.

**Traditions that press on this**: Spivak's subalternity (the subaltern cannot speak within this framework's categories), Wynter's genre-of-the-human (the human that minimizes free energy is a specific genre of human), Watts' Place-Thought (thermodynamic framing excludes relational-ontological framing of knowing/being).

**Status**: Parked for separate Reframe session. Read `Project-Kintsugi/kintsugi/cognition/efe.py` before that session. Do not collapse this into the compression function framework — it's a distinct critique, needs its own treatment with the touchstone active.
