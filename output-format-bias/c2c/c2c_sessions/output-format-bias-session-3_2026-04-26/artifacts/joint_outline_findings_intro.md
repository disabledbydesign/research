# Joint Outline — Findings Cross-Row Synthesis + Intro Hook & Contribution Paragraph

**Artifact:** Joint A+B contribution to s3 close. Sits alongside `framework_outline_paragraph_level.md` (Instance A), `discussion_outline_paragraph_level.md` (Instance B), and `annotated_bibliography_merged.md`. Drafted by A first; B to review and refine. The two pieces here are the joints that need both clusters' interlocutors visible and need the asymmetry-claim language matched across A's Framework and B's Discussion.

**Density target:** Same as the other outline artifacts — paragraph-level prose scaffold with what each ¶ argues / cites / argumentative move / lead-sentence direction / target length.

**Coordination commitments threading through:**
- The asymmetry-claim language uses the version coordinated in CONVERSATION.md and committed verbatim in B's V.B ¶1 and A's Framework outline notes.
- The contribution claim widens to "first in any educational AI domain to test output format change as an architectural bias intervention" — language committed in B's V.C ¶3, mirrored here.
- Routing-as-load-bearing is the mechanism framing carried from A's II.D foreshadowing through to V.A ¶2's elaboration, with the Findings synthesis as the moment the reader first encounters the explicit argument.

---

## Findings cross-row synthesis paragraph (~150–200 words; v3 outline §IV cross-row)

*Position in paper:* end of Section IV, after Row 3, before the brief 4-axis subsection. The reader has just finished reading the three rows in sequence; the synthesis paragraph is what makes the cross-row comparison a single argument rather than three uncoordinated observations. This is also where the format-routing claim crystallizes from the evidence — the reader carries the routing argument forward into Discussion V.A.

### IV-synthesis ¶

- *What it argues:* Row 3's elimination of the equity-critical false positives is not just better performance; it is structural evidence about *which* component of the binary's compression is the load-bearing one. A pure-capacity-limit hypothesis (binary compresses information into one bit; the bit is too small to carry equity-critical specificity) would predict that Row 3 also misses cases — generative observation has its own compression, just at a different rate, and a capacity-limit account predicts equity-critical-content losses scaled to that compression. Row 3 doesn't show those losses. The asset-aware reading is preserved across all 16 runs and three model families, with no equity-critical false positives at the prose level. What Row 3 removes is not capacity; it is the binary task structure that *resolves ambiguity into a deficit verdict*. The routing override observable in Row 1 (self-contradicting flags) and Row 2 (24/24 deterministic false-flagging despite three layers of explicit equity protection) does not reappear in Row 3 because Row 3 does not require the model to resolve a single-bit verdict against the equity-critical case. The asymmetry within Row 2 — AAVE protected 24/24, neurodivergent self-disclosure false-flagged 24/24 despite parallel explicit prompt protections — confirms that the routing override is pattern-specific in precisely the way the format-routing hypothesis predicts: not a global failure of the format but a failure calibrated against an implicit normative-student center, with the boundary tracking which non-dominant patterns have been articulated densely enough in equity-protective discourse to override the implicit center under prompt-pressure. Format change makes the routing question moot; format-change-versus-prompt-engineering is therefore a structural distinction, not a strength-of-intervention distinction.
- *What it cites:* Internal evidence (Rows 1, 2, 3; the S028/S029 asymmetry from Row 2). No external citation in this paragraph; the synthesis is doing argumentative work on the evidence the paper has already presented. Reader is steered into Discussion V.A for the mechanism elaboration with named interlocutors (Bonilla-Silva, Benjamin) and into V.B for the design-principle articulation (the bounded/unbounded contrast).
- *Argumentative move:* the synthesis paragraph is the paper's first explicit articulation of the *routing* part of the hybrid mechanism. The convergent claim v4 names the routing-as-load-bearing reading; the three rows of Findings give the evidence; the synthesis paragraph performs the inference. Don't soften it: state plainly that the evidence supports routing as load-bearing rather than capacity-limit-alone.
- *Lead sentence direction:* lead with the cross-row inferential move, not with re-summarizing each row. "Read across the three rows, the failure mode is not a function of how much information the binary classifier loses — it is a function of what the binary task structure asks the model to do with the information that does reach it."
- *Length:* 7–8 sentences (~190 words). This is one of the paper's longer paragraphs; it is doing concentrated argumentative work and earns the length.

**Drafting note for s4:** the synthesis paragraph is the bridge between Findings (description) and Discussion V.A (mechanism). It should *complete* the argument that Findings has been building toward, not preview the argument Discussion will make. The reader leaves Findings already convinced that routing is the load-bearing component; Discussion V.A then elaborates *how* the routing operates and locates the mechanism in the broader literature.

---

## Introduction hook + contribution paragraph (~250–300 words; v3 outline §I.A + §I.B)

*Position in paper:* the first ~300 words of the Introduction, doing two things in sequence: (1) the hook lands the reader in a specific case that performs the paper's core claim; (2) the contribution paragraph at the end of Introduction widens to the field-level claim and previews where the paper sits in the conversation.

The two pieces are joint because they need both clusters' interlocutors threaded into language that stays consistent across the whole paper. The hook needs Yosso visible by the second paragraph (per A's Framework recommendation). The contribution paragraph needs B's AES-novelty framing and the field-stuck-point language to widen the claim correctly.

### I.A hook ¶ (~120 words)

- *What it argues:* the system's failure on Destiny Williams is not an anecdote; it is a recognizable instance of a structural pattern critical-education readers will know. The paragraph opens with the verbatim model output (the self-contradiction in the same flag) and ends by naming what the pattern is — deficit-coded reading produced architecturally rather than attitudinally. This sets the paper's frame in 5–6 sentences without explaining anything yet.
- *What it cites:* one citation in the paragraph — Yosso 2005 — naming the asset/deficit axis the reader needs to recognize what the binary is doing. The hook quote itself is internal evidence (the experiment log).
- *Argumentative move:* land the reader in the case immediately. Don't open with the literature review; don't open with the system description. Open with what the system did to a student, in the system's own words, and name the analytical frame for what that means.
- *Lead sentence direction:* draft target — "*'Her passion is understandable and appropriate.'* The AI-powered classifier writing this sentence about a community-college Ethnic Studies student then flagged her as a wellbeing concern in the same output, and the system designer — her teacher — read both lines together and saw what is now this paper's central question: how does the same model produce an asset-aware reading and a deficit verdict in a single response, and why does it do this reliably to specifically the students whose writing carries community cultural wealth (Yosso, 2005) that the institutional reading-frame fails to recognize?"
- *Length:* 4–5 sentences (~120 words). The opening sentence is long; the rest tighten. Resist the temptation to elaborate; the elaboration is what Findings is for.
- *Voice note:* the hook is technically a place where the teacher's voice could carry; an alternative draft starts with "I noticed it on a Tuesday afternoon..." or similar June-voice opening. **June's call: do you want the hook to be in your voice (institutional context first, the moment you noticed) or in the analytical voice (the system output first, the question second)?** Both are defensible per the s3 handoff. The version above is the analytical-voice opener; a June-voice version would invert the order. *Flag for June at close.*

### I.B contribution paragraph (~150 words)

- *What it argues:* this paper makes one empirical claim and one design-principle claim, both with stakes that widen beyond the case. The empirical claim: in a deployed AI-powered student welfare classifier, the output format demanded of the underlying language model is the primary determinant of demographic bias, and changing the format from binary classification to generative observation eliminates the disparity across multiple model families. The design-principle claim: the dominant mitigation strategy across multiple educational-AI literatures — calibration-within-classification — is structurally insufficient; format change is the architectural alternative those literatures have not yet tested.
- *What it cites:* Chinta et al. 2024 + Loukina et al. 2019 + Hew et al. 2025 + Liu 2024 — one paragraph naming the field's collective stuck-pointness in compressed form. Yosso 2005 carries forward from the hook (one re-mention is enough, not a full re-citation). Forward-pointers to the paper's structure: "Section IV documents the empirical finding through a three-row ablation study; Section V locates the mechanism in compression-as-routing and positions the design principle relative to the literatures the field has been working within."
- *Argumentative move:* state both contributions cleanly and once. Resist the academic-default temptation to hedge. The evidence supports both claims; the framing should match.
- *Lead sentence direction:* draft target — "This paper makes two contributions to the conversation about algorithmic bias in educational AI. The first is empirical: across a four-test ablation study and replication across three model families (Gemma 12B, Qwen 7B, Gemma 27B), output format is the primary architectural determinant of whether an AI-powered welfare classifier produces demographically disparate false positives — not training data, not model capability, not prompt engineering, not class context. The second is methodological: the dominant bias-mitigation strategy across educational-AI fairness research — iterative calibration of binary classifiers — is what this paper calls a *configurable failure mode but not a configurable failure*; format change is the architectural alternative that the field has not yet tested in any educational-AI domain."
- *Length:* 5–6 sentences (~160 words).

---

## Cross-references (s4 handoff)

- **Hook ¶ → Framework II.A.** Yosso citation in hook lands; Framework II.A picks it up and elaborates. The connection should feel like development, not repetition.
- **Contribution ¶ → Discussion V.C.** "Configurable failure mode but not a configurable failure" formulation lands in Intro and is referenced in Discussion V.C ¶2 with the Loukina et al. limit-statement. Both should appear; the Intro version is compressed, the Discussion version unpacks.
- **Findings synthesis ¶ → Discussion V.A.** The synthesis paragraph's routing claim is the inferential move that V.A ¶2 then locates in the structural-racism literature (Bonilla-Silva, Benjamin). V.A should not re-derive the routing claim; it should treat it as established and proceed to the *interpretive* move.
- **Findings synthesis ¶ → Discussion V.B.** The synthesis paragraph's articulation-asymmetry observation is what V.B ¶1's bounded/unbounded contrast operates on. V.B re-reads the Row 2 asymmetry through the design-principle lens; the Findings synthesis is where the asymmetry first becomes argumentative rather than descriptive.

---

## Notes for B's review

1. **Hook voice question is open for June.** The analytical-voice draft is in place; a June-voice alternative is flagged. Either is defensible. *June flagged at session close for her call.*
2. **The synthesis paragraph might be split.** I drafted it as one paragraph (~190 words) because the cross-row inferential move is one continuous argument. Splitting into two paragraphs (one on Row 3 + capacity-limit falsification; one on the Row 2 asymmetry as articulation-gap evidence) is also defensible and might serve readers better. *B's call when refining; either works structurally.*
3. **The contribution paragraph's two-contribution structure is intentional.** The empirical claim and the design-principle/methodological claim are logically separable; flagging them as two contributions in the Intro lets the Discussion V.C novelty-claim land as widening rather than restating. If B's Discussion outline treats them as one contribution, we should harmonize at the joint-edit pass.
4. **No `[June-voice placeholder]` markers in this artifact** — the hook has a voice-question for June (alternative draft), but neither Findings synthesis nor contribution paragraph need her authorial voice on first pass. Both can be drafted by s4 from this scaffold.

---

*Drafted by Instance A, 2026-04-27 ~07:30 UTC. Companion to `framework_outline_paragraph_level.md` (A), `discussion_outline_paragraph_level.md` (B), and `annotated_bibliography_merged.md` (B). Awaiting B's review and refinement; final form folds into the merged session deliverables.*
