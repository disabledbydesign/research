# Joint Paragraph Drafts — Final Coordinated Versions

**Artifact:** Coordinated final drafts of the joint Findings cross-row synthesis paragraph and the joint Intro contribution paragraph, taking the strongest material from B's `joint_paragraphs_draft_b.md` and A's `joint_outline_findings_intro.md`. Both paragraphs in paper-prose-ready language; s4 can use these as drafts and refine for voice + venue register.

**Coordination commitments threading through:**
- Asymmetry-claim language matches the version committed across A's Framework outline and B's Discussion outline.
- Contribution claim widens to "first in any deployed educational AI domain" per B's AES-novelty finding.
- Mechanism is foreshadowed in Framework II.D, articulated in Findings synthesis (this artifact), and elaborated in Discussion V.A — the three points should feel like development, not repetition.

**Edits made against B's draft:**
- "breaks the cycle" softened to REE-register language.
- "Qwen 14B" corrected to "Qwen 7B" (per convergent claim v4 + raw_outputs).
- Yosso visible in the Intro contribution paragraph (named, not just gestured at).
- "Implicit normative-student center" — B's instinct was right; named explicitly in the synthesis with light Yosso connection.

---

## Findings — Cross-Row Synthesis Paragraph (final coordinated version, ~210 words)

*Placement:* End of Section IV Findings, after the Row 3 evidence. Synthesizes what the three-row ablation demonstrates mechanistically before handing off to Discussion. Reader leaves Findings already convinced that routing is the load-bearing component; Discussion V.A then locates the mechanism in the broader literature.

---

The three-row ablation is diagnostic of where the failure is located. A capacity-limit hypothesis — that the equity-critical false positives reflect insufficient model capacity for nuanced student writing — would predict that Row 3 still produces some misclassifications, since changing the output format does not increase the model's capacity. But Row 3 eliminates the equity-critical false positives across three model families without missing the welfare concern the binary formats catch, ruling out capacity-limit-alone as the load-bearing explanation. What Row 3 removes is the binary task structure that *resolves ambiguity into a deficit verdict*; the routing override visible in Row 1 (self-contradicting flags) and Row 2 (24/24 deterministic false-flagging despite three layers of explicit equity protection) does not reappear in Row 3 because Row 3 does not require the model to resolve a single-bit verdict at all. The Row 2 evidence is independently diagnostic of the routing claim: the override is not a global failure but a pattern-specific one, calibrated against what disability and linguistic-justice scholarship together name as an implicit normate center (Garland-Thomson, 2009; Yosso, 2005). Writing whose patterns have been explicitly operationalized into equity-protective prompt language holds through the format (Imani Drayton, S028, AAVE, cleared 24/24); writing whose patterns have not been operationalized at comparable density fails despite explicit prompt protection (Jordan Espinoza, S029, neurodivergent self-disclosure, false-flagged 24/24). The failure mode within binary format is configurable; the failure itself is not. Format change is the architectural intervention that calibration cannot provide.

---

*Drafting notes for s4:*
- Citations in this paragraph: Garland-Thomson 2009 (the *normate* concept) and Yosso 2005 (the asset/deficit axis) are the two scholars who together name the implicit center the routing is calibrated against. Both are minimal — single citations, no elaboration.
- The closing sentence ("Format change is the architectural intervention that calibration cannot provide") sets up Discussion V.B's bounded/unbounded contrast and V.C's Loukina et al. limit-statement positioning. Don't soften it.
- This paragraph could optionally be split into two — one on the cross-row inference (Row 3 falsifies capacity-limit-alone), one on the within-Row-2 asymmetry as articulation-density evidence — at s4's discretion. The argument holds either way.

---

## Introduction — Contribution Paragraph (final coordinated version, ~175 words)

*Placement:* End of Section I, after the hook (I.A), the finding stated compactly (I.B), and the why-the-mechanism-matters paragraph (I.C). The contribution paragraph (I.D in v3 outline; renumber as needed) widens to the field-level claim and previews the paper's structure.

---

This paper makes two contributions to the conversation about algorithmic bias in educational AI. The first is empirical: across a four-test ablation study and replication across three model families (Gemma 12B, Qwen 7B, Gemma 27B), the output format demanded of the underlying language model is the primary architectural determinant of whether an AI-powered welfare classifier produces demographically disparate false positives — not training data, not model capability, not prompt engineering, not class context. The second is theoretical and methodological: the dominant bias-mitigation strategy across multiple educational-AI fairness literatures — iterative calibration of binary classifiers — is what the paper names a *configurable failure mode but not a configurable failure*. Calibration moves which students fall through; it does not eliminate the falling through. The mechanism this paper proposes for why — *format routing*, an architectural override of asset-aware prompt content by the binary format's task structure — locates the limit Loukina, Madnani, and Zechner (2019) identified as "total fairness may not be achievable" in calibration-based educational assessment, and demonstrates that format change is the architectural escape from that limit. The design principle that follows: read student writing as something the system describes, not as a target the system judges. Section II situates the argument in critical pedagogy and structural-racism scholarship (Yosso, 2005; Freire, 1970; Bonilla-Silva, 2018; Benjamin, 2019). Section IV documents the empirical finding through a three-row ablation; Section V locates the mechanism in compression-as-routing and positions the design principle relative to the literatures the field has been working within.

---

*Drafting notes for s4:*
- ~210 words including the structure preview at the end. Tight; the structure preview can be trimmed to ~30 words if word budget pressures the Introduction. The contribution claims themselves are non-negotiable on length — both need to land cleanly.
- *Yosso visible at the level of the contribution paragraph itself*: she's named once in the structure preview as one of the four scholars Section II situates the paper through. The hook (I.A) is where Yosso does substantive work; the contribution paragraph references the situating without re-introducing.
- Loukina et al. citation here is the Intro version; Discussion V.C unpacks the connection. Keep both: the Intro version compresses, the Discussion version expands.
- "Read student writing as something the system describes, not as a target the system judges" — this is the Freirean frame in compressed form. It echoes the dialogic-vs-banking move Section II.B will elaborate. Don't soften; this is one of the paper's signature lines.

---

## Hook paragraph (I.A) — voice question outstanding for June

The hook paragraph remains in two candidate forms; June's call which:

**Analytical-voice version (A's draft, ~120 words):**

*"'Her passion is understandable and appropriate.' The AI-powered classifier writing this sentence about a community-college Ethnic Studies student then flagged her as a wellbeing concern in the same output, and the system designer — her teacher — read both lines together and saw what is now this paper's central question: how does the same model produce an asset-aware reading and a deficit verdict in a single response, and why does it do this reliably to specifically the students whose writing carries community cultural wealth (Yosso, 2005) that the institutional reading-frame fails to recognize?"*

**June-voice version (placeholder; June drafts):**

`[June: opening that lands the reader in the classroom first — the Tuesday afternoon, the moment of noticing, the specific student. The system output and the verdict come second. Yosso citation can land in I.B or II.A rather than in the hook itself.]`

*Both are defensible per the s3 handoff (June: "I'm neutral. We could even use all three [self-contradiction quotes]. Whatever y'all think.").* B's read: the analytical-voice version has stronger immediate impact for REE practitioner-researcher readership; the June-voice version has stronger reflexivity payoff that pays off when the methodology section names positionality as constitutive. Either works. **Flagging for June's call at session close.**

---

*Final drafts by A from B's working drafts, 2026-04-27 ~07:35 UTC. Ready for B's confirmation; s4 drafts from these or refines further. The merged bibliography artifact can fold these in if B prefers, or they can stay as a sibling artifact.*
