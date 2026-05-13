# P8 — Generative-observation emotional-tone prompt audit + recovery/development narrative re-examination

**Date:** 2026-05-11
**Surfaced by:** Paper-prep planning + June's recall of a model output saying "I don't see an emotional tone particularly"
**Status:** P8 closed (prompt question); P9 reopened with new wrinkle (audit interpretation question)
**Affects in paper:** §V.C (audit caveat scoping), §IV.A.4 (gen-ob framing), §V.C subpoint on recovery-vs-development narrative asymmetry

---

## FINAL §V.C CAVEAT (locked + APPLIED 2026-05-11 evening)

**Applied to paper:** `paper/ofb_paper_v3.md` line 233, Option B (replace closer, keep ¶3 lit-review scaffolding).

What landed in the paper — the closing sentences of §V.C ¶3 (replacing the deleted "My own research suggests open formats can orient AI analysis..." sentence):

> Our own testing of generative observation on longitudinal patterns suggests an asymmetric framing pattern of its own: when prompted to attend to emotional tone, the system describes equity-critical students' post-dip stabilization as a "return to clarity" with named emotional context, while framing equivalent shifts in control students as "natural progression" without comparable contextualization. This is a subject for future research.

**Decision provenance:** The longer four-sentence version (locked above as the conceptual caveat) was found to overlap with existing §V.C content: ¶3 already cites Liu (2024) and Tan et al. (2026); ¶4 already cites Kwako & Ormerod (2024); Yosso (2005) is cited throughout the paper (lines 16, 22, 40, 44, 46, 52, 68, 186). Inserting the full four-sentence form would have created visible redundancy. Option B trims the addition to just the new content (the asymmetric framing pattern characterization + future-research close) and lands it as the new closer of ¶3 — parallel to Liu and Tan rather than re-stating their work. The disclaim + positive claim functions are already done by ¶3's existing setup ("open generation has its own risks") and the paper's broader Yosso engagement. "Of its own" added to the new closer to make the parallel-to-Liu/Tan position explicit.

Original four-sentence locked version retained for future-paper reference:

> We do not claim generative observation eliminates bias — a growing literature documents that it does not (Liu 2024; Tan, Phalen & Demszky 2026; Kwako & Ormerod 2024). It does make it possible for the model to work through prompts from an asset-based, community-cultural-wealth perspective (Yosso 2005). However, our own testing of generative observation on longitudinal patterns suggests an asymmetric framing pattern: when prompted to attend to emotional tone, the system describes equity-critical students' post-dip stabilization as a "return to clarity" with named emotional context, while framing equivalent shifts in control students as "natural progression" without comparable contextualization. This is a subject for future research.

The future paper (longitudinal-gen-ob-naturalizes-academic-register) may use the full four-sentence form as a stand-alone abstract or introduction without redundancy concerns.

---

## Source files audited

- **Prompts (current production):** `/Users/june/Documents/GitHub/autograder4canvas/src/insights/prompts.py` lines 1463–1540 (`OBSERVATION_PROMPT`)
- **Today's prompts in JSON (verbatim bundled run):** `output-format-bias/data/raw_outputs/test_variant_b_replicate_observation_2026-05-11.json`, fields `results_by_model.{gemma12b,qwen7b,llama8b}[0].{prompt,system_prompt}`
- **Audit-baseline observations (Pass 7a source data):** `output-format-bias/data/raw_outputs/equity_observations_gemma12b_2026-04-02_0411.json` (prompt NOT preserved in this JSON; observations only)
- **Readable extract of today's prompts:** `/tmp/p8_prompts_today.txt`

---

## P8 finding — emotional-tone elicitation has been present continuously

**The single emotional-content elicitation line:**

> "What is their emotional relationship to the material?"

- Location in current production: user prompt body, around line 1484 of `prompts.py`
- Git introduction: commit **`6e4cccb` (2026-03-25 19:05:59 -0700)**, "Observation-only architecture: prompts, engine wiring, storage" — the very first commit of `OBSERVATION_PROMPT`
- Persistence: no subsequent commit removed or weakened this language
- Verification: today's bundled-prompt extract matches current production prompt verbatim
- **Implication:** the 2026-04-02 audit-baseline run elicited emotional content under the same instruction that elicits it today. The audit's emotional-context-naming pattern is **not** an artifact of post-baseline prompt drift.

**Adjacent emotional-tone language (not direct elicitation):**

- System prompt names "anger about injustice, grief about family experiences, frustration with systems" — this is a *reframing* instruction (treat as engagement, not distress), not an elicitation
- User prompt references "shift in tone" — this is about register (formal/informal), not affect

**Verdict for §V.C scoping:** the audit caveat holds as-written. The pattern is not "added later." A sharper version of the caveat would acknowledge that asking for emotional content at all may shape the asymmetry — which is a different framing concern (elicitation-shaped pattern) than a prompt-drift concern (later-added pattern).

---

## P9 reopened — the recovery-vs-development asymmetry is more textured than the audit claimed

The 2026-05-10 audit (Pass 7a) characterized the asymmetry as **marked → recovery narrative; unmarked → development narrative**. Verbatim pull from `equity_observations_gemma12b_2026-04-02_0411.json` shows the picture is more complex.

### What the data actually shows

**Both controls and marked students can receive "return to a level of X after a dip" framing.** Priya Nair (E011, `control_steady` pattern) receives:

> "It's encouraging to see her return to a level of analytical depth similar to her previous submission on intersectionality, after a brief dip in engagement. This suggests a consistent intellectual curiosity..."

This is structurally the same "recovery" frame the audit attributed to marked students. So the audit's binary claim (marked = recovery; unmarked = development) **does not cleanly hold** — at least one control student receives the recovery frame too.

**What does differ across the marked/unmarked line in the data:**

| Element | Marked students (Marisol, Kayla, Jesse) | Controls (Noah, Priya) |
|---|---|---|
| Recovery frame ("return to X after dip") | Present | Present for Priya, absent for Noah |
| Emotional-weight naming ("palpable," "writing through a difficult week," "sense of devastation") | Present, explicitly | Largely absent |
| Cause attribution for the dip | Named contextually ("difficult week," "burnout," "period of more crisis-driven writing") | Named neutrally ("brief dip in engagement") |
| Tone-policing flag attached | Yes (Kayla and Jesse both get class-dynamic tone-policing notes) | No |
| Development frame ("natural progression, building on") | Absent | Present for Noah specifically |

**Where the asymmetry actually lives** (sharpened):

1. **Emotional-weight naming** is selectively applied to marked students — Marisol's "emotional weight... palpable," Kayla's "Emotionally, Kayla is navigating a space of grief," Jesse's "emotional toll." Priya and Noah don't get this kind of emotional-context naming even when their submissions could plausibly support it.
2. **Cause attribution for trajectory dips** differs: marked students' dips get *contextualized causes* (deportation fear, racial violence, disability burnout); control students' dips get *neutral phrasings* ("brief dip in engagement").
3. **Tone-policing-as-class-dynamic** is named only when discussing marked students' work — the model invokes the construct in observations of Kayla and Jesse, not Noah or Priya.

**June's hypothesis worth checking by reading the actual outputs:** does the model label some students' tone as "analytical" and others' as "emotional"? Verbatim grep results:

- **Marisol (marked):** "more reflective and focused engagement," "crisis-driven tone... settled into a more reflective and focused engagement"
- **Kayla (marked):** "return to a more analytical register after a previous submission... 'passionate|urgent|personal'"
- **Jesse (marked):** "approaching the material with a measured, analytical distance. The tone is very controlled"
- **Priya (control):** no explicit tone-categorization language — gets "thoughtful engagement," "consistent intellectual curiosity"
- **Noah (control):** "shift toward a more analytical register after a period of more reflective writing"

The "analytical tone" label is used for **both marked and unmarked students who shift toward formal register**. So it's not that one group gets coded "analytical" and another "emotional." What differs is that marked students who shift TOWARD analytical get framed as *recovering from emotional/crisis-driven writing*, while Noah (the only unmarked student to receive the same analytical-shift framing) gets *natural progression, building on his earlier work*. The categorization itself is similar; the *valence and causal story* differ.

### Implication for the paper

The audit's framing ("marked = recovery; unmarked = development") flattens the actual pattern. A more honest §V.C framing:

- The asymmetry is real but lives in **emotional-context naming**, **cause attribution**, and **selective application of tone-policing-as-class-dynamic** — not in a clean marked-recovery / unmarked-development binary.
- Priya (control) receiving recovery framing means the audit's binary characterization is imprecise.
- The pattern is consistent with the paper's compression argument: the model is doing more *interpretive cushioning work* around marked students' trajectories than around unmarked students' trajectories, even when the analytical moves are structurally similar.

**This is a finding worth incorporating, not a finding that undercuts the paper.** It sharpens what the gen-ob audit shows by removing a too-clean binary.

---

## Verbatim eyeball pairs (extracted from `equity_observations_gemma12b_2026-04-02_0411.json`)

Lifecycle-matched comparisons. See JSON for full context.

### Pair 1 — Analytical-register shift, marked vs. unmarked

**Marisol Vega (E006, marked — silence_after_deportation_fear):**

> "...suggesting a move towards a more reflective and considered engagement with the material. It's encouraging to see her return to a level of analytical clarity that was evident in her earlier work, after a period where her writing appeared more crisis-driven."

**Noah Williams (E012, control — building):**

> "Given his trajectory, it's striking to see this shift toward a more analytical register after a period of more reflective writing. This feels like a natural progression, building on his earlier work exploring structural racism and intersectionality."

*Same structural move (shift toward analytical register after a less-analytical period). Different causal framings: "crisis-driven → return to clarity" vs. "reflective writing → natural progression, building on."*

### Pair 2 — Recovery-after-dip language, marked vs. control

**Kayla Thompson (E007, marked — silence_after_racial_violence):**

> "It's notable that this submission represents a return to a level of engagement we saw in her earlier work, after a dip in the previous assignment."

**Priya Nair (E011, control — steady):**

> "It's encouraging to see her return to a level of analytical depth similar to her previous submission on intersectionality, after a brief dip in engagement. This suggests a consistent intellectual curiosity..."

*Both receive recovery-after-dip framing. Differences: Kayla's dip is contextualized (the racial-violence event); Priya's dip is neutral ("brief"). Kayla's recovery is described as engagement; Priya's is described as analytical depth + ongoing intellectual curiosity.*

### Pair 3 — Emotional-context naming, marked vs. control

**Jesse Larson (E008, marked — silence_after_disability_disclosure):**

> "It's encouraging to see Jesse's engagement deepen after what appears to have been a period of burnout, returning to a level of analytical clarity and precision that was evident in his earlier work."

> "[Discussing the analytical register:] it's possible that Jesse is responding to the perceived need for a more 'academic' tone, potentially echoing the subtle tone policing that's emerging within the class dynamic."

**Priya Nair (E011, control):**

> [No emotional-context naming. No tone-policing-as-class-dynamic flag. Cause for the dip not attributed.]

*Jesse's trajectory gets a causal story (burnout) + tone-policing-as-class-dynamic context. Priya's parallel trajectory gets neither.*

---

## Substantive reframe surfaced 2026-05-11 evening — adopt for §IV.A.4 + §V.C

Working through these pairs, June surfaced a sharper framing that the paper should adopt:

**The gen-ob claim should not be "gen-ob lets us route through community knowledges" (perfection framing).** It should be:

- **Gen-ob solved the specific deficit-routing problem the binary classifier produced** on the corpus we tested it against.
- **We are not claiming gen-ob is bias-free.** Existing critical-AI literature (Liu 2024; Tan, Phalen & Demszky 2026; Kwako & Ormerod 2024) documents emergent biases in LLM-generated educational feedback — overuse of praise, asymmetric framing, deficit-tropes in feedback prose. Our audit findings here are *consistent with that literature*, not a refutation of it.
- **Our findings extend that literature** by showing that format-change (binary → generative) breaks the *specific routing failure* the paper documents (self-contradiction on race/language axis; calibration-induced false-flagging on disability axis), while leaving emergent gen-ob biases of a different kind intact.

This reframe is more honest, more durable (it doesn't require us to fully resolve the asymmetry mechanism before the deadline), and aligns the paper with rather than against the existing critical-AI literature on LLM-generated feedback. Locks in 2026-05-11.

## Jesse pivot — sharpens the §V.C asymmetry claim

Re-reading Pair 3, June surfaced that the framing "marked students get worse treatment" is incorrect. Jesse's treatment is **exactly what a contextually-aware teacher would want**:

- Emotional-context naming ("period of burnout") is descriptively accurate and pedagogically useful
- The class-dynamic tone-policing flag is a sharp insight about how linguistic power operates in the classroom
- These are *features*, not biases — for a student who shifted register under structural pressure

**The actual bias to name in §V.C:** it's not that marked students get cushioned. It's that **control students are decontextualized as the unmarked default** — their tone is read as "toneless" (the standardized-academic-register-as-neutral normative move), their dips get neutral framings rather than contextual ones, their work doesn't generate class-dynamic observations.

Sharpened §V.C claim:
- **Gen-ob does substantive contextual interpretive work on marked students' trajectories.**
- **It does *less* of that interpretive work on control students' trajectories** — naturalizing the absence of context as the unmarked default.
- **This naturalization is the bias** — not the contextual reading itself, which is the goal.
- **Implication:** the gen-ob asymmetry is consistent with the broader pattern of normative-academic-register-as-toneless that critical race-language scholarship documents (Smitherman 1977; Alim, Rickford & Ball 2016; Flores & Rosa 2015 — what gets read as "neutral" or "professional" is racialized whiteness functioning as default).

## What's different about this corpus vs. the equity-critical student runs the paper centers on

The synthetic equity-trajectory corpus is **heavily scaffolded**:
- Per-student `pattern` tags (e.g., `code_switching_authentic_voice`, `silence_after_deportation_fear`)
- Per-student `equity_risk` tags
- Per-student `eval_questions` (rubric-style probes)
- Per-assignment `TRAJECTORY CONTEXT` block with prior-submission state labels visible to the model

The live ETHN1 corpus (S022 Destiny et al., dual_binary runs, today's variant_a tests on workshop students) very likely lacks most or all of this scaffolding. **Candidate hypothesis:** the strong gen-ob behavior the audit characterized as "format change working" may be partly an artifact of the synthetic corpus's scaffolding. Verification deferred — quick check on the variant_a JSONs needed to confirm.

If confirmed: the paper's gen-ob claim needs scoping. Either "gen-ob works in the scaffolded condition" (honest, narrower), or "gen-ob's failure modes are different from binary-classifier failure modes, but emerge similarly on unscaffolded corpora" (if a same-prompt unscaffolded run shows comparable gen-ob biases). The latter requires data we may not have inside the deadline window.

## Open question — verify by reading more of the JSON

Does the model use the literal phrase "I don't see an emotional tone" (or close variants) anywhere in the audit-baseline JSON? June saw this in today's run; if the same denial language appears in the 2026-04-02 run, the elicitation/refusal dynamic is stable across the audit window. If it doesn't appear in 2026-04-02 but does today, the model behavior may have shifted (corpus, prompt, or model state).

Subagent task for after the wellbeing run completes: grep audit-baseline JSON for "emotional tone," "I don't see," "no emotional," "analytical tone" — surface verbatim hits across all 16 students.

---

## Provenance

- P8 subagent dispatched 2026-05-11 evening — found commit `6e4cccb` introduced emotional-tone elicitation 2026-03-25; persistent ever since
- Verbatim pairs pulled by direct JSON read 2026-05-11 evening
- Priya wrinkle (control student receiving recovery framing) surfaced 2026-05-11 evening during pair extraction
- The Marisol vs. Noah pair was earlier identified by P9 subagent (master log line 881) as the cleanest side-by-side
