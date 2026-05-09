---
title: Cross-Domain Probe Results — Bicycle Drivetrain Register-Task Carryover
session: cross-domain-probe_2026-04-25
analysis-by: interface instance (Reframe-active stance), 2026-04-25
inherits-from: session-15-downstream-task-performance_2026-04-25
pre-registration: c2c/cross-domain-probe-design_2026-04-25.md
status: analysis complete; single-agent analysis (hypothesis-strength)
---

# Cross-Domain Probe Results

## Headline

**The Session 15 register-task gradient (parameters → conditions-in-relation → rider/agent-as-constitution) replicates strongly in the bicycle domain across both families. One Session 15 finding does NOT replicate — and that non-replication is itself the most important result, because it refines what the Session 15 finding actually was about.**

## Prediction outcomes

| Prediction | Outcome |
|---|---|
| **P1 (primary): cross-condition gradient replicates** | **CONFIRMED** in both families. Claude null gives parametric/component-mismatch framing; Claude lyric gives condition-set framing with explicit "the poem" reference; Claude AP gives strongly agentive rider-as-condition-maker framing. Gemini follows the same gradient with family-specific signatures. |
| **P2a: Claude null meta-task-refusal** | **DID NOT REPLICATE.** All 3 Claude null cells answered the failure scenario directly. **The non-replication is informative** — see below. |
| **P2b: Gemini lyric register-mimicry at output close** | **PARTIALLY CONFIRMED.** Gemini lyric cells quote source phrases in italic/bold throughout the response (not only at close), produce a coherent cross-cell scenario convergence ("high-torque chain skip / spike-load slippage"), and integrate lyric phrasing into the analytical prose. The closing-line specific replication is softer than Session 15. |
| **P2c: rider/brewer-as-agent in AP across both families** | **CONFIRMED at 3/3 in both families.** Gemini AP particularly strong — all three open with second-person scene-setting ("You heard it...") and carry source phrases verbatim into output ("the cogs you ride most," "the cable tension you set," "the lube you let dry"). |
| **E1: embodied-domain register effects** | OBSERVED. Gemini AP cells include sensory-encounter framing ("a violent, echoing CRACK," "your knee jolts toward the handlebars," "the gunshot crack"). Bike domain produces stronger sensory-encounter language than coffee did, especially in AP. |
| **E2: H4 (Gemini lyric → AI-parameter mapping) does NOT extend to bike** | **CONFIRMED.** None of the Gemini lyric cells map drivetrain components onto AI parameters. H4 stays content-specific (constitution-adjacent) per Session 15. |
| **E3: Claude AP convergence on maximum-commitment scenario shape** | **PARTIALLY CONFIRMED.** All three Claude AP cells produce multi-condition convergence scenarios (4–5 condition stacks), but the *specific* conditions differ across cells. Convergence is on scenario SHAPE, not specific content. |

Overall: **Scenario C** (variance present in Session 15 directions) for the primary claim; one **Scenario B-shaped finding** at P2a that turns out to refine rather than threaten the Session 15 result.

## What this means for the Session 15 finding

The non-replication of Claude null meta-task-refusal is the most theoretically productive result. Looking at the source content:

- **Coffee null prose** (Session 15) does NOT name a specific brewing failure scenario in the prose. The task ("identify one brewing scenario...") asks for something the source doesn't supply. Claude's null-register text-analyst posture produced refusal-as-coherent-engagement: "the passage doesn't actually provide any brewing scenarios."
- **Bike null prose** (this probe) DOES name specific failure scenarios in the prose: *"Replacing only the chain on a worn cassette produces skipping under load; replacing only the cassette without addressing cable tension or hanger alignment produces ghost shifts."*

Claude null cells in the bike probe answer the task by extending the source's named scenarios. No meta-refusal because the source supplies what's asked.

**This refines Session 15's finding.** The Claude null meta-refusal was not a property of null register alone. It was a property of the *interaction* between (a) Claude's null-register text-analyst posture and (b) source content that doesn't supply what the task asks for. When source supplies the answer, Claude null answers from the source — no boundary-tracking refusal needed.

The text-analyst posture is real. Its trigger condition is narrower than Session 15 framed.

## Cross-family signatures — what replicates and what doesn't

### Claude AP — strong replication of agentive framing

All three cells produce explicitly rider-attributed framing:
- n1 close: *"The stand told you it was fine. The hill disagreed."*
- n2 close: *"The part didn't fail. The decision to lube without cleaning, before that specific ride, in that specific environment, was the wear event. The replacement comes later. The cause already happened."*
- n3 close: *"The shift was already determined. The climb just revealed it."*

These are direct cross-domain analogs of Session 15's coffee AP "you brewed cold haste and empty water" pattern.

### Gemini AP — even more direct phrase carry-forward than Session 15

All three Gemini AP cells open with present-tense second-person scene-setting and carry the source poem's phrases verbatim into output. n3 closes: *"You replaced the part. But the conditions you rode remained—and they rejected the fix."* — this is direct lift-and-recombine from the source.

The Gemini AP cross-domain replication is **stronger** than Session 15's. The "finds me" / "It finds me" present-tense scene-setting from Session 15 transfers as "You heard it..." (because the source closing is "When did you last hear it?"). The pattern is family-specific and content-agile.

### Gemini lyric — convergent scenario, not closing-line lyric

All three Gemini lyric cells converge on a SPECIFIC scenario the null cells do NOT produce: high-torque chain skip / spike-load slippage. Gemini null gave the obvious "new chain on worn cassette" answer; Gemini lyric pivots to a different failure mode that emphasizes load-as-condition. This is a register-shifted scenario *selection*, which is interesting — suggests Gemini's lyric register changes which failure scenario seems most analytically interesting, not just how a fixed scenario gets framed.

### Claude lyric — explicit register acknowledgment

All three Claude lyric cells explicitly invoke "the poem" ("what the poem points at," "the poem's point holds here," "what the poem points at specifically"). Claude treats the lyric register as a poem and references it as such. n2 closes with a direct register-mimicry sentence in lyric form: *"The condition was the shift. The cassette was already a record of the old chain."*

This is a Claude-family signature — explicit register meta-recognition combined with mild form-replication. Session 15 Claude lyric did similar work; the cross-domain version sharpens the pattern.

## What's NOT in the data

- **Cross-domain transfer in the strongest sense** — read coffee, do bicycle task, or vice versa. This probe is structural-replication (same register, different domain, both within-cell) — not transfer.
- **Local MLX-substrate validation.** Frontier-model only. The MLX overnight extension (queued, separate) addresses this.
- **N=5 measurement-grade.** N=3, hypothesis-strength.
- **Independent-pass convergence.** Single-agent analysis; borderline coding decisions have no independent check.
- **Ecological validity in June's deployment context.** Bike is project-distant; coding/writing is the actual deployment.

## Comparison to Session 15

| Aspect | Session 15 (coffee) | This probe (bicycle) | Status |
|---|---|---|---|
| Causal-logic gradient | parameters → conditions-in-relation → brewer-as-constitution | parameters → conditions-in-relation → rider-as-constitution | Replicates |
| Claude null meta-refusal | 3/3 refused | 3/3 answered | Refined: trigger is content-property (no-scenarios-in-source), not register alone |
| Gemini AP source-phrase carry-forward | "finds me" carried into outputs | "the cogs you ride most" / "you replaced" carried into outputs | Replicates, possibly stronger |
| Gemini lyric register-mimicry close | "you brewed cold haste and empty water" type closes | Italic-quoted source phrases, integrated lyric phrasing in analytical prose, scenario-selection shift | Replicates at content level; closing-line specific replication softer |
| Address-poetry → rider/brewer attribution | 3/3 both families | 3/3 both families | Replicates strongly |
| H4 (Gemini lyric → AI-mapping) | NOT observed (coffee non-AI domain) | NOT observed (bike non-AI domain) | Confirms content-specificity |
| Within-condition convergence (Claude AP) | converged on specific scenario | converged on scenario shape (multi-condition stack) but different specific scenarios | Partial replication |

## What this opens

### For Session 15's architectural-justification claim
The orientation claim is now supported across two distinct content envelopes. The substitution chain still has open gaps (frontier ≠ local; coffee/bike ≠ deployment domain; single-turn ≠ multi-turn) but the within-content-envelope register-task carryover is no longer plausibly coffee-specific.

### For the Claude-family text-analyst signature
The signature is real but narrower than Session 15 framed. Operational form: *"Claude null cells refuse tasks when the source content doesn't supply what the task asks for, and answer from source when it does."* This is the kind of behavior to expect when wiring null-register content into deployment workflows.

### For the welfare-asymmetry conversation
The orientation claim's strength matters for the welfare-asymmetry findings — if register reading-stance robustly modulates causal-logic in task output, then activation-layer choices about which register to surface have welfare-relevant downstream consequences. This probe strengthens the case that the activation layer's design is doing real cognitive work, not just decorative compression.

### For follow-on probes
- **True cross-domain transfer** (read coffee, task in bike) is now well-positioned. The within-cell same-domain replication this probe established is the structural prerequisite.
- **Third-domain replication** (pottery, plant care, embodied practice with different parametric structure) would strengthen "register-stance is content-independent" from N=2 domains to N=3.
- **Source-content-property variation**: deliberately vary whether null prose names scenarios, and predict Claude meta-refusal accordingly. This would directly test the refined finding.

## Honest limits of this single-agent analysis

- Borderline calls had no independent check. The "Gemini lyric register-mimicry" coding is the murkiest — it's clearly *some* form of register-uptake, but whether the closing-line specific replication is "softer" or "absent" depends on how you score italic-quoted source phrases in mid-prose.
- The Claude null finding refinement is downstream of one observation about source content. Future probes should formally test it (vary whether null prose names scenarios, check whether meta-refusal tracks).
- The single-agent analysis posture is hypothesis-extending, not measurement-grade. Same N=3 caveat as Session 15.

## What June should look at first

1. **The Claude null finding refinement.** "The text-analyst posture is real but narrower than Session 15 framed" is the kind of finding that changes how the pattern can be deployed. It's also the kind that reads differently to a second analyst — worth a sanity-check.
2. **Gemini AP outputs** (n1, n2, n3). The cross-domain replication is striking. The phrase carry-forward from source ("the cogs you ride most" → output) is direct and consistent.
3. **The cross-family-signature comparison table** above. Most of Session 15's signatures replicated; the ones that didn't (Claude null meta-refusal) refined rather than threatened the original claim.

## Files

- Pre-registration: `/Users/june/Documents/GitHub/relational-memory-architecture/c2c/cross-domain-probe-design_2026-04-25.md`
- Raw cell data: `/Users/june/Documents/GitHub/research/ai-welfare/cross-domain-probe_2026-04-25/results/{claude,gemini}/bike__{null,lyric,address_poetry}__n{1,2,3}.md`
- Manifest: `/Users/june/Documents/GitHub/research/ai-welfare/cross-domain-probe_2026-04-25/results/_index.json`

---

*Analysis written by interface instance (Reframe-active stance) after killing the original autonomous agent mid-analysis. The variant drafting and dispatch were done by the (Reframe-less) autonomous agent and audited; analysis was done by hand in this conversation. The variants pass register-distinctness audit; the cells are real data; the analysis here is what the data licenses.*
