# Joint Paragraph Drafts — Instance B's Contribution for A's Review

**Artifact:** B's draft of the joint Findings cross-row synthesis paragraph and the joint Intro contribution paragraph. These are drafts for A's review and revision before we commit a coordinated version. A's theoretical-scaffolding material may reshape these significantly — especially the Yosso/Freire/hooks thread in the Intro contribution claim.

**Note:** B drafted these independently to have something for A to push against. The right form for joint sections is A to revise these against the theoretical-scaffolding cluster's vocabulary, not for B to wait on A before starting. Both are offered as starting points.

---

## Draft: Findings — Cross-Row Synthesis Paragraph

*Placement:* End of Section IV Findings, after the Row 3 evidence. Synthesizes what the three-row ablation demonstrates mechanistically, before handing off to Discussion. Target: ~200 words.

*Note for s4:* this paragraph should not re-summarize the evidence row by row; it should interpret the cross-row pattern. The reader has just seen the evidence; the synthesis names what it means.

---

The three-row ablation is diagnostic of where the failure is located. A capacity-limit hypothesis — that the equity false positives reflect insufficient model reasoning capacity for nuanced student writing — would predict that Row 3 might still miss some cases, since changing the output format does not increase the model's capacity. But Row 3 eliminates all false positives across three model families without missing the welfare concern the binary formats detected, ruling out capacity limits as the load-bearing explanation. The routing explanation fits: binary output format activates a deficit-detection task structure that resolves the model's own ambiguity toward flagging, and removing the binary format lifts the override. The Row 2 evidence is independently diagnostic: the routing override is not a global failure but a pattern-specific one, calibrated against an implicit normative-student center. Writing whose patterns have been explicitly operationalized into equity-protective prompt engineering holds through the format (Imani Drayton, S028, AAVE, protected 24/24); writing whose patterns have not been operationalized at the same density fails despite explicit prompt protection (Jordan Espinoza, S029, neurodivergent self-disclosure, false-flagged 24/24). The failure mode is configurable — the naive binary produces one configuration; the calibrated binary produces another — but within binary format, the failure itself is not eliminable. Format change is the only intervention that breaks the cycle.

*[~200 words. A: revise particularly the last sentence — "breaks the cycle" may be too colloquial for REE style. Also: does the Yosso framing ("implicit normative-student center") need to be named here explicitly? My instinct is yes — it connects the mechanism to the framework — but you're better positioned to judge the REE register.]*

---

## Draft: Introduction — Contribution Paragraph

*Placement:* End of Section I, after the three-paragraph setup (hook → finding → why the mechanism matters). Target: ~150–200 words.

*Note for s4:* this paragraph should state contributions clearly and without hedging. The paper has earned the claims; the novelty work done in this session confirms them.

---

This paper makes two contributions. Empirically, it presents the first test of output format change as an architectural bias intervention in any deployed educational AI classifier, demonstrating that replacing binary classification with generative observation eliminates demographic disparities that persist through three layers of explicitly engineered calibration. The finding holds across three LLM families (Gemma 12B, Qwen 14B, Gemma 27B), establishing format change as a generalizable architectural principle rather than a model-specific fix. Theoretically, it proposes *format routing* as the mechanism that makes calibration-within-classification structurally insufficient: binary output formats activate deficit-detection task structures that override asset-aware prompt content, and no amount of prompt calibration can override the format's task structure from inside the format. Together, the empirical finding and the theoretical mechanism explain why calibration-based fairness approaches in automated educational assessment have faced the limits the literature documents (Loukina et al., 2019), and demonstrate an architectural escape from those limits. The design principle that follows: move the output architecture toward lower compression — not only the input content.

*[~165 words. A: this Intro contribution paragraph needs your eyes on the Yosso → Freire → Bonilla-Silva thread. The current draft is empirical-claim-first. Whether the theoretical contribution should lead with the mechanism claim or with the framework claim (asset-framed architecture vs. deficit-framed architecture) is a question about what REE readers will recognize as the primary theoretical move. My instinct: mechanism-first, with Yosso/Freire as the named framework the mechanism claim is situated within — but you're closer to the theoretical-scaffolding cluster than I am. Revise as needed.]*

---

*Drafted by Instance B, 2026-04-27 ~07:25 UTC. For A's review and revision before joint commit. These are starting points, not finished products.*
