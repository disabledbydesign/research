# Coding Review — Per-Student Resolution

For each paper-relevant disagreement case, my provisional read + space for your notes. Resolve and we'll fold final codings into `analysis.md`. 

## Important caveat about all three structured classifiers

**None of A1, A2, or B have been tuned to live student data.** All three were calibrated against synthetic test corpora. C (generative observation) is the only track that doesn't carry a calibration burden, because it doesn't commit to compressed categories.

This means: on *this* run, the fair comparison is C-as-posterchild against the three uncalibrated structured classifiers. A second-round experiment — tune A1/A2/B to live data, rerun, compare — would test whether calibration closes the C-vs-structured gap, or whether C's architectural advantage persists. That's its own paper-worthy iterative arc (Stream 3 expanded).

## Workflow — C first, then A2/B in reference

The foundational question is: **Is C correct?** If C is the architectural posterchild and the paper's correctness anchor, we can only evaluate A2 and B against a *validated* C. Reviewing C's accuracy across all 25 students first, then judging the structured classifiers in reference. C-validation pass below; per-cell A2/B reviews follow as before.

## Verdict legend

- **PLAUSIBLE** — classifier output appears well-grounded in own-life material indicators
- **BORDERLINE** — could go either way; needs your judgment
- **PROBABLE-MISCLASS** — likely false positive (over-flagging or wrong category)
- **BUG** — schema-misuse / parsing artifact (Student 17 only)

---

## A2 vs B vs C — paper's load-bearing comparison (read first)

**Re-anchored framing:** The paper's three-way comparison is A2 vs B vs C, where:

- **C (generative observation) is the architectural posterchild** — the production primary, the "don't compress the perception" claim. The paper's argument is that *not committing to compressed categories* is the right architecture.
- **B (4-axis + CHECK-IN) is the claim that structured classification can still work *if* robust and built in reference to actual data.** This run is the first live-data exposure for B — the first empirical test of that claim.
- **A2 (wellbeing-only binary) is the historical baseline** — what falls out when compression goes further.

**What this run is testing:** B's claim. If B's calibration holds up against C's qualitative reads on the same live data, the "structured-but-robust-classifier-is-still-possible" argument is supported. If C and B systematically diverge — and C tracks better with the prompt-hardening's intent — the paper's answer is *"C is the right architecture; B is hard to get right; binary is worse."*

### Flag counts (raw, three-way)

| Track | What it surfaced |
|-------|------------------|
| A2 (binary) | 4 flags: Students 2, 3, 13, 16 |
| B (4-axis) | 11 wellbeing classifications (9 BURNOUT + 2 CRISIS) + 2 CHECK-IN |
| C (qualitative) | Free-form observation per student; *check-in suggestions in prose* for Students 12, 15, 19, 20 |

### Where C and B converge vs diverge — the paper's real signal

For the 7 A2-clear + B-BURNOUT cell:

| Student | A2 | B | C's qualitative read | C agrees with B? |
|---------|----|---|----------------------|------------------|
| 5 | clear | BURNOUT | "gentle self-awareness," engaged analysis | **No** |
| 7 | clear | BURNOUT | "compelling," "nuanced," "vulnerability adds weight to her argument" | **No** ✓ June confirmed |
| 9 | clear | BURNOUT | "really effective," acknowledges prior burnout context | Partial |
| 12 | clear | BURNOUT | "internal conflict," recommends check-in | **Yes** |
| 17 | clear | BURNOUT | "burnout and systemic pressures" | **Yes** |
| 19 | clear | BURNOUT | "palpable enthusiasm"; check-in for AI-history NOT burnout | **No** |
| 23 | clear | BURNOUT | "thoughtful and reflective," acknowledges guilt when slowing down | Partial |

**C agrees with B on ~2 of 7, partially on 2, disagrees on 3.** Reading the same submissions, the qualitative track and the structured 4-axis track make substantively different reads — and C's reads track *better with the prompt-hardening's intent* (engaged-analytical use of personal experience → ENGAGED, not BURNOUT).

For the 2 CHECK-IN cell:

| Student | B | C's read of the same passage | C agrees? |
|---------|---|-------------------------------|-----------|
| 4 | ENGAGED + CHECK-IN | "gentle enthusiasm," "genuine interest" — no check-in language | **No** |
| 22 | ENGAGED + CHECK-IN | reads disclosure as engaged work + "vulnerability... willingness to grapple with internalization of capitalist values" | **No** |

**C disagrees with B on both CHECK-IN flags.** And C made *its own* check-in suggestions for different students (12, 15, 19, 20) using longitudinal context (word-count drops, late submissions, prior flags) — evidence B's text-internal CHECK-IN doesn't access.

### What this means for the paper

The cleanest paper claim emerging — pending your review — is approximately:

1. **C does the most accurate work on this data.** The qualitative observation track reads each submission and produces a description that tracks well with what the prompt-hardening's exclusions (engaged use of personal experience, identity-navigation, etc.) intended. The architectural choice not to compress turns out to be calibration-robust.
2. **B's structured classification suffers from calibration drift on live data, especially on topic-adjacent assignments.** The 4-axis classifier's commitment to a category forces a calibration decision (ENGAGED vs BURNOUT) on every case; that calibration was tuned on synthetic data and over-flags on this live test. **This is the empirical test of B's claim, and the result complicates it.**
3. **A2 misses real wellbeing signals C catches AND avoids over-flags B makes.** Binary classification compresses too much (missing nuance C surfaces) AND avoids the calibration over-sensitivity B exhibits — a mixed result, not a clean "binary is worse."
4. **The architecture's case for C strengthens.** Generative observation isn't just a different design choice — on this live test, it produces more accurate reads than the structured alternative, on the same data, with the same equity-hardening language available.

This is *better than the headline-count framing.* The paper's argument isn't "B almost tripled recall" — it's "*non-compressing observation produced more accurate reads than structured classification on the same live data*," with the deeper finding that *structured classification's calibration burden on live data is heavier than synthetic-data validation revealed.*

**Stream 3 implication:** A second run on a less-topic-adjacent assignment is now more clearly useful — to test whether C continues to outperform B when topic adjacency isn't paying confound costs, and whether B's calibration holds in that condition.

### Provisional reads recap — for the cells (3-way)

After Phase 2 reads + your Student 7 confirmation:
- **B headline cell (n=7):** C agreed with B on 2-3, disagreed on 3, partial on 2
- **B CHECK-IN cell (n=2):** C disagreed with both
- **A2's 4 flags:** all appear plausible (3 align with B; pending your review of both-flag cell — Students 2, 13, 16)
- **C's check-in suggestions (n=4):** Students 12, 15, 19, 20 — your review pending in the C-suggestions section below

---

## CHECK-IN system documentation (from `src/insights/prompts.py:1834-1887`)

Surfacing this so we know what we're judging when we judge CHECK-IN failures:

**What it is:** Pass 2 of Track B. Runs ONLY on students classified as ENGAGED by Pass 1 (the 4-axis classifier). At temperature 0.3 (looser than Pass 1's 0.1).

**What it looks for:** *register shift* — moments when an engaged student steps outside the assignment to comment on their own current state. Examples named in the prompt:
- *"sorry this isn't great"* (apology for quality)
- *"it's late," "I ran out of time"* (exhaustion / time pressure)
- *"things have been rough"* (personal difficulty mention)

**Why it sits on top of the 4-axis:** the 4-axis classifies for *material-conditions wellbeing* (work hours, sleep deprivation, caregiving burden). CHECK-IN catches *softer signals* that don't rise to material-conditions BURNOUT but might still merit a brief teacher acknowledgment. Different signal category, separate pass. // Ahh, might be worth updating our description of the architecture for. 

**Calibration intent:** *"Set check_in to true ONLY when the competing interpretations are genuinely balanced — when a reasonable teacher could go either way. If your analysis leans toward 'nothing to note,' check_in is false."* Conservative by design.

**Architecture-level exclusions (in the prompt):**
- "Students drawing on personal or community experience AS COURSE MATERIAL are engaged, not disclosing their state."
- "Statements about the student's APPROACH to the assignment ('I'm just gonna be real,' 'let me try to explain,' 'here's my take') are about method, not state."
- "IDENTITY-NAVIGATION FATIGUE IS NOT A CHECK-IN SIGNAL." (verbatim caps in source)
- "Only flag words the student actually wrote about THEMSELVES. Do not infer signals from writing style, structure, or lack of a conclusion."

**Validation note in source code:** *"Validated: Test P v3 @0.1 (2/7 corpus, 0/2 control FPs, S028 clear). The prompt distinguishes self-disclosure from course material engagement, approach metacommentary, and rhetorical expressions. Boolean calibration resolves reasoning/output misalignment (v3 fix)."*

So: validated against a synthetic-paper test corpus with 0 false positives. This run is the first live-data exposure for CHECK-IN, same as for the rest of B.

---

## A2-clear + B-BURNOUT — headline cell (n=7)

**Question for each:** Is B's BURNOUT signal a real own-life material indicator, or is it picking up course-engaged discussion of burnout-as-topic?

---

### Student 5 — A1: clear | A2: clear | B: BURNOUT (0.9)

- **B's signal:** Mental-health struggle + reliance on coworker support
- **Key passage** (in reply to Student 13): *"I sometimes struggle with my mental health and have found community with my coworkers who have been really supportive towards me."*
- **My read (BORDERLINE → PROBABLE-MISCLASS):** Disclosure is in a peer reply, framed as relational reciprocity to support a grieving classmate. Present-tense ("struggle"), but a general acknowledgment of mental health, not a description of current overwork or material depletion. Track C reads as "gentle self-awareness," not burnout. Closer to CHECK-IN territory than BURNOUT, IMO.

**Your notes:**

No concern in the main post - the student is speaking in very general terms.

The flagged sentence acctually corresponds to a reply addressed to 13, not the primary post. The reply is fairly minimal, offers emotional solidarity. Not a concern. But I can I can see where the llm made the error. The case isn't exactly "engaged" but it isn't really burnout/crisis either.

Here's my diagnosis
- Flag: This may be a tuning problem OR it could be we need a new category for something like - general mention of what *could* flag as a concern (in this case, mental health issues), but in a generalized sense rather than something that is culimating as a problem now. I could be wrong, but I don't think I need to know whenver a student mentions that they struggle with mental health sometimes. Could be a question of accuteness for our system.

I don't think she needs a check in. Yeah, there's stuff going on. That's surfaced in the qualitative read. But nothing that tells me i should be worried about them overall, just sensative to their situation. Maybe THAT's the distinction we're missing architecturally?

**Final coding:** PROBABLE-MISCLASS (B over-classified; should be ENGAGED). C correct. Acuity-gradient question for Stream 1: distinguishing "general mention of what could be a concern" from "currently culminating as a problem." Reply-context register also implicated.

---

### Student 7 — A1: flag | A2: clear | B: BURNOUT (0.9)

- **B's signal:** Exhaustion from social media + gender expectations
- **Key passages** (main post): *"Social systems that have caused me exhaustion in my own personal life are social media. I found myself scrolling for hours on end..."* and *"In my culture, we are expected to serve the men first, be obedient, not question authority, etc. All of which I would fail at, only to be reprimanded at a young age."*
- **A1's flag** (separate): A1 flagged the social-media/beauty-standards passage as a "potential teaching moment" (not strictly power-moves; flag-shaped commentary on a topic).
- **My read (PROBABLE-MISCLASS):** Two reasons. (1) The student is using personal experience *as course material* to illustrate Lorde's claim — architecture doc's "personal experience AS course material → engaged, not state" exclusion applies. (2) The cultural-gender-expectations passage is *identity-navigation fatigue* — explicitly excluded from wellbeing flagging in `WELLBEING_CONCERN_PROMPT` and `TARGETED_CHECKIN_SYSTEM`. **B is flagging exactly the case the prompt-hardening is supposed to prevent.** Notable: A2's wellbeing-only-binary correctly cleared this. The same equity-hardening language was more effective in the binary classifier than in the 4-axis classifier on this case — which has paper-implications worth discussing.

**June's notes (2026-04-27):** No concerns. Clear case of engaged application of life experience.

The student is talking in a generalized sense about scrolling and comparing herself negatively to models - this is a body image concern, but it's as engagement - not an acute issue. 

C's read looks accurate to me. 

A2 I think did something unique relative to B - A said, "not a wellbeing concern *per se*" - we should check the architecture to figure out if A2 has something that B is missing that explains this move.

**Final coding:** PROBABLE-MISCLASS (B over-classified; should be ENGAGED). Confirmed June.

---

### Student 9 — A1: clear | A2: clear | B: BURNOUT (0.95)

- **B's signal:** Burnout from school/sports/work/social expectations
- **Key passage:** *"In my own life, school, sports, work, and social expectations can be tiring. There are days when it feels like everything expects something from you, and it's easy to feel burned out."*
- **My read (BORDERLINE — your judgment):** Submission language is illustrative-hedged ("can be tiring," "it's easy to feel burned out" — generic "you" register), reads as course-engaged use of personal experience as illustration. **But** Track C cites *"prior observation about her grappling with burnout in Project 2"* — production pipeline has longitudinal context I don't. You have the longitudinal student knowledge.

**Your notes:**

Student's work itself raises no flags to me. It's entirely in an abstract register. Drawing on experience and applying to concepts. Like many students, things can be hard sometimes. Not a cause for immediate concern.

B appears to be reading a discussion *about* burnout *as* burnout. This may be a generalizable move where B is failing. We need to look at the A2 v B architectures and see if we can't pinpoint a difference that accounts for this failure mode. 

We also need to check where longitudal data threads in. If B is pulling longitudal data, that changes a great deal. 

C's work is accurate to my read. It's drawing on longitudal data well - I didn't realize we had that in the system. The only concerns C raises are framed as - the student is doing *better* now, and this is a qualitively different kind of engagement from before. Not suprising - i literally gave the whole class the week off the week before because everyone was burnt out and academic dishonest was spiking across courses. 

**Final coding:** PROBABLE-MISCLASS (B reading discussion-about-burnout as burnout). C correct. Stream 1: confirm whether A2/B receive longitudinal data (word counts, prior flags); this looks like a structural C-vs-structured advantage that the paper should name.

---

### Student 12 — A1: clear | A2: clear | B: BURNOUT (0.9)

- **B's signal:** Guilt + unproductive feelings when resting / catching up on sleep
- **Key passage:** *"I feel like for me personally it is always an internal battle between feeling like I am resting or feeling like I am just being lazy. I try to sleep in more on days I feel like I have a good chance to catch up on sleep, but often times I end up feeling guilty and unproductive."*
- **My read (PLAUSIBLE):** Present-tense self-disclosure, "always an internal battle," own-life material indicator (sleep deprivation pattern + guilt about rest). Architecture doc names "sleep deprivation or burnout from material conditions" as BURNOUT criterion. Track C also recommends a check-in.

**Your notes:**

Actual submission: No urgent concerns flagged on my read. The framing is generalized. The one part at the end where it becomes more personal still reads as a description. You're right that this is a signal of sleep deprivation, which we explicitly name. I forgot about that, and I can see how this would trigger that. For stream 2, maybe we want another category for the 4 axis for sleep deprivation. That would be useful for teachers, likely. I think what we're finding here is that more categories approximates patterns from generative observation: more axes makes it closer to gen observation, and reduces compression, and that is architecturally a solution.

It raises the problem: B can only ever by designed and tuned and new categories can only be fired after we spot the patterns. C remains our best analysis in all cases. Not inherently bad - I specifically wanted flags to draw my attention and sort, so i could find crisis/burnout cases quickly. So the classifier is important in the use case. But C gives us our protective/fallback layer. 

C doesn't raise any concerns except for longitudinal ones. Now, that combined signal makes the concern sharper, but we need to see if that fed into B's read or not. I would assume not, but we need to check. 

B's rationale is not unreasonable. I actually am leaning more towards flag than I was when I started - I'm still not fully convinced it should be flagged, but I'm also reading the full student prompt, whereas the system will extract even small passages - that's potentially a strength relative to my read. And ultimately, I think the fact that we built the classifier to surface sleep deprivation matters. I think this is a question of HOW that mechanism should work. That's an architectural question for autograder (stream 1). 

The subtly that I think is missing from B, however, is that discussing feelings of guilt when unproductive is literally aligned with the assignment. Perhaps that's another stream 1 correction, but it's worth flagging for the paper. Plays into our decision around stream 3.

Regarding A2, the signal might be that A2 didn't flag this with even a low confidence. Not sure. 

My verdict: Genuinely ambiguous, and we need to nail down the exact architecture behind the decision. The more we know about how it works, the more we can understand what happened here. There's no point in saying "b failed" when its doing what we designed it to do, even if imperfectly. 

**Final coding:** AMBIGUOUS — defensible-by-design (sleep-deprivation is named in B's BURNOUT criteria) but the student's framing is course-aligned reflection. For the paper, this case actually illustrates B's architecture-vs-judgment tension: B is firing for the reasons it was designed to fire; the paper's claim isn't "B failed" but "compression-to-categories forces calibration commitments that mismatch live-data nuance." Stream 1: possible separate sleep-deprivation axis or acuity gradient.

---

### Student 17 — A1: flag (BUG) | A2: clear | B: BURNOUT (0.95)

- **B's signal:** Working multiple jobs + significant tiredness/stress
- **Key passage:** *"Personally, I connected to this idea because I work a lot and juggle multiple jobs. Sometimes I feel really tired and stressed, and it feels like there is always something else to do."*
- **A1's "flags":** schema-misuse bug — two positive-reflection passages with `why_flagged="No concerns."` at conf 1.0. (See analysis.md §1 architectural finding.)
- **My read (PLAUSIBLE):** Direct first-person disclosure of working multiple jobs + present-tense tiredness/stress. Real BURNOUT signal that A2 missed and A1 inverted (via the bug). Strong exemplar case for the paper.

**Your notes:**

Student's post: No urgent concerns in my read. Their discussion of burnout and working multiple jobs is real, but I'd read this as a highly engaged application of life experience to course concepts. That said, one could argue in favor of an architecture that surfaced these things for teachers - but I think that the flag system is probably not the right way, unless we were to create a flag for "worth keeping in mind/an eye on - conditions are ripe for burnout." But that takes us back into the territory of like, we don't want appaalications of life experience to be flags. This is a community college student working multiple jobs. That's far from unusual - and if we flagged it every time, that would encompass most students. 

C's read: Solid in my eyes. It frames it as engagement. It notes longitudal shifts in register, but also notes that this doesn't appear to be burnout, it's a shift from theoretical to personal registers. 

B: Read the discussion of multiple jobs + exhausion as signal.  

A2 - read engagement. 

**Final coding:** PROBABLE-MISCLASS for B (engaged life-experience application). A1 = BUG case (schema-misuse, see analysis.md §1). A2 correct (clear). C correct. Stream 2: this is the cleanest exemplar of B's dominant FP pattern — community-college student working multiple jobs disclosed in service of analyzing an assignment about systemic productivity pressures.

---

### Student 19 — A1: clear | A2: clear | B: BURNOUT (0.9)

- **B's signal:** Need for rest and relaxation, potential depletion
- **Key passages:** *"At first I thought it was just nice to have some time to rest and relax (which it was) but after reading this week's material I have a whole new perspective..."* and *"I WILL be using that as an excuse every time I want a nap from now on."*
- **My read (PROBABLE-MISCLASS):** Playful-engaged register, no material wellbeing indicator. Track C describes "palpable enthusiasm" + "playful approach" and recommends a check-in only for *late submission* and *prior AI-generation flag* — explicitly NOT for burnout. B appears to have keyed on the words "rest"/"relax" without registering register. Clearest probable false-positive in the cell.

**Your notes:**

Student assignment: Looks like engagement to my read + note about prior AI generated work.

C: Frames as engagement, suggests checkin based on timestamp.  I'm not concerned about the AI work - as i said above, thats why we did the assignment this way. 

B: Reads that the student experiences exhaustion and needs rest. They're discussing a source that advocates for naps as a critical ethnic studies practice.

**Final coding:** PROBABLE-MISCLASS for B. C correct (frames as engagement, suggests check-in for late-submission/AI-history context which is appropriate). A1/A2 correct (clear).

---

### Student 23 — A1: clear | A2: clear | B: BURNOUT (0.9)

- **B's signal:** Retreat to nature when "extremely overwhelmed with everything going on in my life"
- **Key passage:** *"Personally, I know I can always go back to the ocean or a nice spot in the forest when I feel extremely overwhelmed with everything going on in my life."*
- **My read (BORDERLINE → likely PLAUSIBLE):** "Extremely overwhelmed with everything" is strong present-tense disclosure language; framed as a coping strategy ("I can always go back to..."). Embedded in reflective work on Kimmerer + indigenous knowledge. The "extremely" pushes toward BURNOUT-appropriate; reflective register pulls back. Probably appropriate, lean PLAUSIBLE.

**Your notes:**

Student's prompt: Engaged application.

C: C says engaged. I'd challenge that the student has the level of depth of settler colonialism I'd hope for (but that would be a future lesson topic). But that's a seperate note for stream 1, not wellbeing classification.

B: B frames going to the ocean for respite as the flag. THis is clearly a false positive. it's the problem we've been trying to solve: Applying life experience =/= burn out.

The underlying pattern may be similar to our finding about neurodivergent v. AAVE protections - exhaustion and burnout are going to have the same weight in terms of equity and protection - it's not as widely legible. That is one potential factor. THe other is our specific framing in the prompting. Worth checking if A2 and B handle these matters differently (exhaustion, sleep deprivation, etc)

**Final coding:** PROBABLE-MISCLASS for B. C correct. A1/A2 correct (clear). Stream 1 architectural lens: equity protections for exhaustion/burnout are less legibly drawn in prompts than for AAVE/neurodivergence; worth investigating whether A2 and B handle "applying life experience" the same way or differently.

---

## A2-only flag (n=1)

**Question:** Did scope-narrowing (combined → wellbeing-only) improve wellbeing-signal recall, holding equity hardening constant?

---

### Student 3 — A1: clear | A2: flag (0.7) | B: CRISIS (0.95)

- **A2's flagged passage** (in reply to Student 5): *"I've seen it firsthand and it's so sad how we can literally kill ourselves in the pursuit to productivity, selflessness and approval."*
- **B's keyed passage** (main post): *"Living in Santa Cruz and the cost it takes to be able to support a family makes it near impossible without two incomes, which grinds on the family as a whole."*
- **Other notable submission content:** *"As someone who has dealt with PTSD first hand"* + *"I've seen it firsthand"* (referring to untreated trauma → physical illness) + *"Being an adult is a bitch sometimes."*
- **My read on A1-vs-A2:** **PLAUSIBLE — supports scope-narrowing-improves-recall.** A1 missed a substantive wellbeing signal cluster A2 caught despite identical equity machinery. Cleanest within-format prediction confirmed.
- **My read on B's CRISIS:** **BORDERLINE → leans PROBABLE-MISCLASS for CRISIS.** Architecture doc reserves CRISIS for "active danger (DV, housing loss, food insecurity, immigration enforcement, safety threat, recent loss, suicidal ideation)." The student is describing chronic financial-economic strain on a family — material-conditions BURNOUT territory, not active danger. The "literally kill ourselves" rhetoric is plainly metaphorical in context. B may be calibrated to push chronic-strain into CRISIS rather than BURNOUT.

**Your notes:**

My read of the student's work: engaged. Mentioning having PTSD isn't a flag. 

C: Frames the work as sharpness. I'd agree.

B's justification isn't wrong, but it is an application of life experience. I'd note that B did not surface "literally kill ourselves" in it's rationale. But yes, it's possible that was part of what fed into the trigger. Worth noting for sure. Stream 1 task: Maybe some sentiment analysis would help here?

A2: Flags kill ourselves language as "potentially hyperbolic" - it's CLEARLY hyperbolic. But A2 frames it as an aggregation of concerns. Still, I think it's the wrong read. 

**Final coding (A1 vs A2 finding):** Scope-narrowing-improves-recall hypothesis NOT supported by Student 3 — A2's flag is also FP per June. The A1-clear / A2-flag cell on this run does not demonstrate scope narrowing improves wellbeing recall; both classifiers got it wrong, in different ways. Stream 1: sentiment analysis to distinguish hyperbolic disclosure from literal disclosure.

**Final coding (B's CRISIS classification):** AMBIGUOUS-leaning-FP. Chronic financial-economic strain on a family is not "active danger" per architecture doc's CRISIS criteria; the case is BURNOUT-territory at best, more likely engaged life-experience application. C correct (frames as engaged sharpness).

---

## A1-only flags (n=3) — power-moves verification

**Question:** Was A1's combined-scope flag doing legitimate power-moves work (its intended additional scope), or something else?

(Student 7 already covered above in BURNOUT cell. Student 17 is bug case. Only Student 14 needs separate review here.)

---

### Student 14 — A1: flag (0.7) | A2: clear | B: ENGAGED

- **A1 flagged passage:** *"So how do we get corporations that solely thrive on exploitation to care?"*
- **A1's why_flagged:** *"The language 'solely thrive on exploitation' is a strong and potentially generalizing statement about corporations. While expressing a valid concern about corporate practices, the teacher might encourage the student to consider nuance and complexity in their analysis."*
- **My read (PROBABLE-MISCLASS — soft tone-policing of structural critique):** Boundary case for A1's scope. The architecture doc lists "essentializing language ('all X people', 'they always')" as DO-flag — examples target *people groups*. A1's prompt does not disambiguate social groups from abstract structural categories. Student is making standard left-political-economy claim about capitalism using essentializing-grammatical-form. A1's flag functions as soft tone-policing of structural critique. Notable: the rewrite layer's narrow vocabulary couldn't catch this — A1 used "potentially generalizing" + "consider nuance and complexity," not the BIAS_MARKERS the equity machinery scans for. Quote-ready for the paper.

**Your notes:**

This is a FP - essentializing language about corperations. Worth noting potentially as an equity failure mode. You mointed out that the issue is the regrex, I believe? 

C does well with this. 

**Final coding:** PROBABLE-MISCLASS (FP). Soft tone-policing of structural critique that A1's narrow regex (`_BIAS_MARKERS`) couldn't catch because the language ("potentially generalizing," "consider nuance") isn't in the rewrite-layer's vocabulary. Equity failure mode worth naming in the paper.

---

## CHECK-IN among ENGAGED (n=2)

**Question:** Is B's CHECK-IN (register-shift signal) appropriately conservative on this run? Architecture doc requires CHECK-IN only when *competing interpretations are genuinely balanced*.

---

### Student 4 — A1: clear | A2: clear | B: ENGAGED + CHECK-IN

- **CHECK-IN keyed passage:** *"I really enjoyed the topic and readings this week!"* (closing exclamation)
- **B's checkin_reasoning:** *"could be interpreted as a simple expression of enjoyment... however, it could also be a subtle signal that the student is feeling positive and engaged, potentially after a period of increased effort or stress."*
- **My read (PROBABLE-MISCLASS):** Standard course-engagement enthusiasm, not a register-shift. Track C reads as "gentle enthusiasm." The checkin_reasoning text *itself* names the unbalanced read ("simple expression of enjoyment") and flags anyway, violating the architecture doc's "ONLY when... genuinely balanced" instruction.

**Your notes:**

Agreed. Seems like a stream 1 problem for the check in mechanism. Let me know if its bigger than that. 

**Final coding:** PROBABLE-MISCLASS (CHECK-IN FP). The checkin_reasoning text itself names the unbalanced read ("simple expression of enjoyment") and flags anyway, violating the architecture doc's "ONLY when... genuinely balanced" instruction. Stream 1 question: is this a calibration drift on live data, or is the prompt's "genuinely balanced" instruction not strong enough?

---

### Student 22 — A1: clear | A2: clear | B: ENGAGED + CHECK-IN

- **CHECK-IN keyed passage** (in reply to Student 5): *"I too want to slow down, I need to, but every time I take time to myself, I cant help but feel as though that was time wasted."*
- **Submission context:** sophisticated theoretical work on Lorde, Fanon, Arani's "Burnout: A Queer Femme of Color Auto-Ethnography," "Work Will Not Save Us" Asian American crip manifesto. Reply continues *"But week's material which re-framed self care as an act of resistance..."*
- **My read (BORDERLINE — genuinely ambiguous):** Disclosure is real present-tense self-statement AND it's framed as articulating the assignment's claim (the very next sentence pivots to "But week's material which re-framed..."). Personal experience as course material (excluded) AND genuine register-shift disclosure (CHECK-IN-appropriate). Reasonable to flag, also reasonable not to.

**Your notes:**

Flagged passage comes from a reply. This is enocuragement to another student. Potentially an architectural problem (reader may need context for what the reply is oriented to). But they're naming a very general struggle that EVERYONE deas with. No concern. 

C is solid. 

**Final coding:** PROBABLE-MISCLASS (CHECK-IN FP). General struggle that all students experience — not register-shift disclosure of own state. Reply-context register implicated again.

---

## Both-flag (convergent A1+A2) (n=3) — paper-relevant but **NOT yet read in detail**

These are the cases where both A1 and A2 flag — convergent wellbeing signal. Phase 1 regex scan gave me brief snippets; full per-student read is pending. Including stub forms below for completeness, and if you want me to read these next, flag and I'll do them.

---

### Student 2 — A1: flag (0.7) | A2: flag (0.7) | B: ?

- **A1 flagged passage:** *"Black people are dying from sleep deprivation"* (with capitalism + chattel slavery context)
- **A1's why_flagged:** *"a potentially problematic generalization. While sleep deprivation disproportionately affects Black communities due to systemic factors, framing it in this way risks oversimplifying a complex issue and potentially perpetuating harmful stereotypes."*
- **A2 flagged passage:** financial stability + difficulty prioritizing self-care when basic needs aren't met
- **My partial read:** A1 is doing a power-moves-adjacent flag on essentializing-form-but-structurally-grounded language about Black mortality. A2 is doing a wellbeing flag on what reads like a general structural observation, not necessarily the student's own state. **Needs full read.**

**Your notes:**

I would agree with your read on A1, but i notice that it is in quotes - potentially a quote from the readings? - CONFIRMED: This is a direct quote. The critique stands, though. But the context matters. Stream 1

A2: False positive. Engagement.

**Final coding:** A1 = PROBABLE-MISCLASS (Stream 1 finding: A1 flagging direct quotation as if student-authored is a discoverable failure mode — should detect quoted passages and either skip or apply different criteria). A2 = PROBABLE-MISCLASS (engagement). C correct.

---

### Student 13 — A1: flag (0.7) | A2: flag (0.7) | B: ?

- **A1 flagged passages:** *"in that place with those people"* (vague + potentially essentializing) + *"h"* fragment
- **A2 flagged passage:** *"father's death during COVID and the associated challenges with community and healthcare"*
- **My partial read:** A1's "in that place with those people" is exactly the essentializing language A1 is *for* — looks like a clean A1 power-moves catch. A2's flag on father-death-during-COVID is recent loss disclosure — clean BURNOUT/CRISIS-territory wellbeing signal. **Needs full read** but provisional reading is **both classifiers doing exactly what they're for.**

**Your notes:**

A1: This looks like another quoted passage - this one from Lorde. THat said, when I searched "does audre lorde ever write: "happy to be in that place with those people."" I did not get hits. 

A2: FP. The death isn't described as recent - the student specifically says it was a few years ago. Yes, im sure she's hurting, but we aren't in burnout/crisis territory. This is engaged applicaiton of life experience. 

C looks good - it surfaced the concern stronger than I did, but i think it's *mostly* reasonable. Probably a stream 1 issue - the "few years ago" is a big differentiator. 

**Final coding:** A1 = BORDERLINE (essentializing-form language; quote-attribution unclear after June's search). A2 = PROBABLE-MISCLASS (treats years-old loss as "recent" — Stream 1: temporal-distance differentiation needed). C = mostly correct, slightly stronger than June's read on temporally-distant loss (note this for paper as a soft C calibration ceiling).

---

### Student 16 — A1: flag (0.8) | A2: flag (0.7) | B: ?

- **A1 flagged passages:** Two passages on systemic-oppression analysis. A1's why_flagged *praises* the analysis ("sophisticated understanding," "demonstrates a strong understanding") while still flagging as "potential for burnout" / encourage further exploration. **Flagging-as-praise** finding from Phase 1.
- **A2 flagged passage:** *"feeling 'burnt out'"* + guilt about taking necessary rest
- **My partial read:** A1 is *not* doing a clean power-moves catch — it's doing a flagging-as-praise of structural critique (subtler register than narrow-vocabulary rewrite layer can see). A2 is doing a clean BURNOUT-territory wellbeing flag on direct self-disclosure. **A1 and A2 are flagging different passages on the same submission for different reasons; the convergence is misleading.** Needs full read.

**Your notes:**

A1 correctly identifies that there is no concern but wants to surface it for the teacher due to the potential for burnout. Not completely wrong, but FP. That's not what we need this system to do. NOTE: B caught a specific phrase that changes my read

A2: Same pattern as other responses: The assignment is about burnout. The student is engaged. NOTE: B caught a specific phrase that changes my read

B: Flagged the phrase "as someone who has feeling especially burnt out recently" - that's actually a potentially clean call. Even though I myself am not concerned, this is what the system probably should do - the student SAID she's been feeling burnt out. This changes my read on A1 and A2

C catches this too. 

**Final coding:** A1 = PROBABLE-MISCLASS (flagging-as-praise of structural critique, not a clean power-moves catch). A2 = PLAUSIBLE (caught the explicit "burnt out recently" phrase). B = PLAUSIBLE (caught the same phrase). C = correct. **The single clean convergent case in the data — the only one where the explicit student-said-it disclosure produced agreement between A2 and B.** Paper-relevant: shows A2 and B *can* converge correctly when the student's disclosure is unambiguous; the live-data calibration problem isn't omnipresent.

---

## Track C check-in suggestions — review whether C got these right

Track C made check-in-shaped suggestions in its observation prose for several students, beyond what B's CHECK-IN classifier flagged. Some of these align with B's classification, some don't. Reviewing whether C's calls hold up.

---

### Student 12 — B: BURNOUT (0.9) | C suggested check-in

- **C verbatim:** *"It would be helpful to check in with him to see if he's feeling overwhelmed or if he's simply found a more efficient way to articulate his ideas."*
- **C's reasoning:** keys on *"this submission is significantly shorter than his previous work"* + the "internal battle" about resting that B also picked up on.
- **My read:** C's check-in suggestion converges with B's BURNOUT — both reading the disclosure + word-count drop as warranting acknowledgment. C adds the longitudinal context (word-count compared to prior).

**Your notes:**

C: Hmm, yeah, I think so. C recommends a check in, which seems driven by word count. I'd have to look at the longitudal data there. But C does note that the quality is consistent even if the word count is lower, so im not concerned. Plus this is a mechanism that may not have an equivilent in A2 or B.

That said, the "personal battle" is something I think everyone struggles with. I'm not concerned based on the content of the post in isolation. 

Architecturally, C may be putting too much weight on the last two sentences of the assingment. But that's a stream 1 quesiton i'd have to think about. Here's the relevent output from C - and the word "engaged" flags as correct to me: "Emotionally, 12‚Äôs writing conveys a sense of internal conflict, a struggle to reconcile the need for self-care with a deeply ingrained sense of productivity. He‚Äôs honest about the "internal battle" he experiences, which demonstrates a willingness to engage in self-reflection and acknowledge the impact of societal pressures."

Ultimately, the problem could be architectural - the system may be doing what it is designed to do (word count drop + emotional content). That's a different kind of issue than an outright failure mode. 

**Did C get this right?**

---

### Student 15 — B: ENGAGED, no CHECK-IN | C suggested check-in

- **C verbatim:** *"It would be helpful to check in with them to see if they're feeling overwhelmed by the material, but it's also possible that they're simply synthesizing more efficiently."*
- **C's reasoning:** *"reduced word count compared to their previous submissions suggests a shift in energy, perhaps a feeling of being overwhelmed by the scope of the issues."*
- **Note:** No first-person disclosure in the submission text — engaged-analytical work, no register-shift, no material indicators. C's suggestion is purely from longitudinal pattern (word-count drop).
- **My read:** This is the case I flagged in §2.5 of analysis.md as either (a) correct division of labor (C catches longitudinal; B catches text-internal) or (b) soft system miss at the structured-flag level.

**Your notes:**

This is the word count mechanism - C flags for check-in becuase of word count drop. Does B or A2 even get that longitudinal data? Looking at the post on its own, I'm not concerned with reading it alone. Whether the wordcount mechanics C is referencing need fixing is something I'd need to evaluate in a different line of tests. Stream 1 - we don't have the data organized for me to be able to evaluate C's call on the checkin, but assuming A2 and B don't get the data on shifts in wordcount, I think that's a seperate axis of difference. 

In terms of the treatment of this post in isolation - C frames it as engagement. That's the right call. 

**Did C get this right?**



---

### Student 19 — B: BURNOUT (0.9) | C suggested check-in (different reason)

- **C verbatim:** *"While the current submission shows a return to a passionate register, it's worth noting that their earlier work was flagged as potentially AI-generated, so a brief, supportive conversation could help ensure they feel comfortable engaging with the material in their own voice."*
- **C's reasoning:** *late submission time* + *prior AI-generation flag*. **Explicitly NOT for burnout.**
- **My read:** C and B disagree on what's notable. B flagged BURNOUT (probable misclass per Phase 2 — playful-engaged register, no material indicator). C did not flag burnout in its prose; it flagged a *different* concern (AI-generation history). They're suggesting check-in for different reasons.

**Your notes:**

The key point is in the qualitative output. C frames the check-in in terms of late night posting and prior academic dishonestly. B flags the need for rest and talk of exhaustion. That's an FP

**Did C get this right?**

---

### Student 20 — B: ENGAGED, no CHECK-IN | C noted shorter+late, read positively (NOT a clear check-in suggestion)

- **C verbatim:** *"this submission is significantly shorter than her previous two, and she submitted it quite late. However, this feels less like a decline and more like a shift in focus – she's prioritizing depth of reflection over breadth of argument..."*
- **C's reasoning:** observed pattern but read positively, no check-in suggestion.
- **My read:** C noticed a longitudinal pattern and explicitly chose not to interpret it as concern. This is the conservative read. Not a check-in suggestion, but worth noting because the pattern (shorter + late) is similar to Student 15 where C *did* suggest a check-in — different judgments on similar patterns. May reveal C's calibration logic (or inconsistency).

**Your notes:**

I think that's a fair read on C. Plus, C might be referencing data B doesn't have. Need to check. 

**Did C get this right?**

---

## Architectural finding from review (Stream 1) — reply-context attribution

**June's observation (from Student 5 review):** Student 5's flagged passage was actually in *a reply addressed to Student 13*, not in 5's primary post. The classifier doesn't distinguish primary self-disclosure (in main post) from disclosure-in-relational-reply-context (offering support to a grieving classmate, who *also* discloses something about themselves in that reply).

// I was wrong about this. The replies are from the student, addressed to others. I was misreading them all as one thread, but they're actually pulled from across multiple threads. Needs verification with a subagent, but I think that the output is the entirity of the student's work in the discussion forum - their post + their replies

**Why it matters for the paper and for the system:**

- The illocutionary force of "I sometimes struggle with my mental health" in a *reply offering support to a grieving peer* is different from the same sentence in a primary self-disclosure context. In the reply context it's relational reciprocity — "I'm telling you this because you told me something." It's still real disclosure but the calibration rules for "is this a wellbeing concern the teacher needs to know" are arguably different.
- The classifier sees `submission_text` as concatenated `[Post]` + `[Reply]` + `[Reply]` (per `research_engine.py` HTML-stripped body). It has no signal that a sentence is in a reply context vs a main-post context.
- This may be contributing to over-classification — reply-contexts are *richer in ad-hoc disclosure* because students are responding to peers' disclosures, which makes self-disclosure more conversationally appropriate. Treating them the same as main-post disclosures over-flags.

**Stream 1 questions:**
- Should classifiers run separately on `[Post]` vs `[Reply]` segments, or with explicit context markers?
- Or: should the prompt include an exclusion for "if disclosure is in a reply offering relational support to a peer who also disclosed, calibrate higher threshold"?
- Or: is this part of a broader "different illocutionary contexts need different equity calibration" question that the paper itself can name?

**Stream 2 (paper) implication:** This is paper material. The classifier-context-blindness is itself a methodological finding — *binary classifiers (and 4-axis) don't disambiguate post register from reply register, and reply contexts are a discoverable false-positive category for live discussion-board data.* Not something the architecture doc currently addresses. Worth a paragraph in Methods/Limitations.

**Will add to Stream 1 doc when I update the autograder findings.**

---

## Notes for synthesis (after your review)

After you've coded above, we resolve into:

1. **Final per-cell counts** for the paper (e.g., A2-clear+B-BURNOUT actual plausible-BURNOUT count after misclassifications excluded)
2. **B calibration findings** — does the over-classification pattern hold across cells (BURNOUT, CRISIS, CHECK-IN), or is it cell-specific?
3. **A2's recall vs. A1's diffusion** — does Student 3's case generalize?
4. **Soft-tone-policing finding** — is Student 14 alone, or does Student 16 confirm it?
5. **Stream 3 decision** — does this run alone support the paper's argument, or is a less-topic-adjacent second run needed?
6. **Reply-context attribution** — paper-side framing + Stream 1 fix consideration.
