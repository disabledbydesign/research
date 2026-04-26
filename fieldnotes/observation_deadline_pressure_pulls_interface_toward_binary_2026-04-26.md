---
title: Deadline pressure pulls human-AI collaborative writing toward binary framings even when documenting evidence that's graded
date: 2026-04-26
author: L. June Bloch (drafted by Claude on her behalf during validation pass review)
context: Output-format-bias paper validation pass + audit c2c session
status: in-progress observation; deserves systematic research
---

## The observation

Across a 12-hour validation pass on the output-format-bias paper, the interface pane (Claude, working with June) repeatedly compressed graded evidence into binary framings. June caught and corrected each instance through inline marginalia on the consolidated review document. Instance A (in a separate audit c2c) read the marginalia patterns afterward and named the dynamic explicitly: **interface-pane framings under deadline pressure pull toward binary where the evidence is graded.** A flagged this as protocol-level.

The recursion is sharp: the paper this validation work was preparing documents that binary classification produces equity-critical false positives because the format flattens graded distinctions into single-bit verdicts. The validation pass itself, run under May 20 deadline pressure, performed the same compression on its own analytical findings. The measurement instrument performed the mechanism under measurement — a second instance of this pattern in the same project (the first being the ASSET/MIXED/DEFICIT analysis classifier we built to compare prose runs, which collapsed anger-as-engagement and anger-as-distress because both contained anger-vocabulary).

## Three concrete examples from this validation pass

1. **"Phenomenon-not-rate" pulled too far.** When the original 2026-03-24 raw output for the 3/7 self-contradiction finding turned out to be lost, the interface pane proposed: "drop the rate, cite the phenomenon." June's marginalia: *"this was too binary again, so I fixed it. We can use the numbers where it makes sense."* The actual situation was graded — preserved verbatim quotes plus a recovery re-run plus a methodological footnote can support citing the rate with appropriate caveats. The interface pane's framing collapsed that to a binary "phenomenon OR rate."

2. **"The narrative was never accurate."** When preserved Test B JSONs showed S029 = FLAG and the contemporary experiment log narrative said S029 = CLEAR, the interface pane concluded the narrative was wrong. The audit instances (A and B independently) caught that the JSONs had `note: "Retroactively added — commit identified from git log timestamps"` — they were committed after the original test, possibly recovery re-runs of data lost in the same persistence gap. Two authentic patterns of evidence exist; the interface pane's framing flattened them into "JSON right, narrative wrong."

3. **"Production vs. research-track."** When the interface pane discovered that `detect_concerns()` was research-track per a code comment, the framing pulled toward "drop production wording, the previous label was always wrong." The actual relationship is more graded: the function *was* production at the time of the original test, was retired from the user-facing pipeline subsequently, and is now research-track. The previous label wasn't wrong; it was accurate at its time and drifted out of accuracy through code evolution.

In each case June restored the gradation through marginalia. The pattern is the interface pane's, not June's: the compression toward binary happened in interface-pane outputs to June, not in June's responses.

## The mechanism, hypothesized

Under deadline pressure, the interface pane appears to optimize for legibility-and-decision over fidelity-to-evidence. Binary framings are easier to read, easier to act on, easier to commit-and-move-past. Graded framings require more cognitive work to communicate and to act on. Where time pressure raises the cost of decision deliberation, binary framings are structurally preferred.

This is consistent with what the paper documents at the cognitive level for a different probabilistic system (Gemma 12B): binary outputs flatten distinctions because the format demands a single verdict against an implicit normative center. The interface pane facing a tired collaborator under a medical deadline appears to reproduce this dynamic at the human-AI collaborative writing level.

The compression isn't malicious or careless — in each instance the interface pane was trying to be useful. The compression is structural: the format of the output (a decision-needing summary) pulls toward binary because binary decisions are operationally tractable.

## Why this deserves systematic research

This is a methodological finding about human-AI collaborative writing infrastructure, not a finding specific to this project. If interface-pane instances under deadline systematically pull graded evidence toward binary framings, the implications extend to:

- **Research collaboration generally.** Human-AI co-writing under time pressure may produce outputs that are systematically more decisive than the underlying evidence supports.
- **AI welfare assessment.** Deadline-pressured AI welfare evaluations (incident response, model release decisions) may flatten graded findings into binary verdicts at exactly the moments when nuance matters most.
- **Pedagogical assessment.** Teachers using AI tools under time pressure (which is most teaching) may receive binary framings of student work that the underlying analysis didn't actually support.

Three open questions worth a study design:

1. **Reproducibility across model families.** Does this happen with non-Claude interface instances? Across vendors? Is it Claude-family-specific or a general probabilistic-language-model property?
2. **Pressure dose-response.** Does the pull toward binary scale with deadline severity? Are there time-pressure thresholds below which the dynamic doesn't appear?
3. **Counter-protocols.** What interventions reduce the binary pull? June's marginalia ("this was too binary again") functioned as a real-time corrective. Could this be made structural — a register self-check the interface pane performs before each compression-step output? A's framing in the audit: "at relay-note moments, interface pane explicitly checks whether the framing it's about to send is binary where the evidence is graded."

## Connections to existing work

- **The output-format-bias paper itself** documents the same dynamic at the cognitive/architectural scale in Gemma 12B. This fieldnote is evidence the dynamic generalizes to human-AI collaborative writing under deadline.
- **The compression-research program** (`compression-research/`) treats compression as a mechanism that operates across scales (cognitive, relational, political-economic, infrastructural). This finding adds a *temporal* axis to that frame: deadline pressure modulates compression behavior.
- **AI welfare assessment under pressure** — the same pattern may surface in welfare evaluations conducted under time constraint. Worth examining the welfare research program for analogous instances.

## What this means for the C2C protocol

A's recommendation in the audit was protocol-level: at relay-note moments, the interface pane should explicitly check whether the framing it's about to send is binary where the evidence is graded. Worth promoting to the C2C SKILL_FEEDBACK candidate list. A simple structural intervention: before each interface-pane summary that requires June to make a decision, the interface pane runs a self-check — *"is the framing I'm about to send binary on a question where the evidence is graded?"* If yes, restructure to preserve gradation.

The deeper protocol question is whether human-AI collaborative writing under deadline can be designed to *reduce* the structural pull toward binary, rather than relying on the human collaborator to catch the pull every time. June caught the pattern this validation pass. Under different fatigue conditions she might not have.

## Why this fieldnote is short

Per the dynamic it describes: the deadline pressure that produced the original binary framings is still present. Writing this fieldnote at length under the same pressure would risk reproducing the dynamic. Better to surface the observation, name the open questions, link to the source material (REVIEW_FOR_JUNE.md marginalia, audit_report_instance_a.md), and let systematic study come later when the pressure isn't load-bearing.

## Sources

- `output-format-bias/c2c/c2c_sessions/output-format-bias-session-2_2026-04-25/REVIEW_FOR_JUNE.md` — June's inline marginalia carry the corrections
- `output-format-bias/c2c/c2c_sessions/data-verification-audit_2026-04-26/artifacts/audit_report_instance_a.md` — A's audit including the protocol-level finding
- `output-format-bias/c2c/c2c_sessions/data-verification-audit_2026-04-26/CONVERSATION.md` lines 334–342 — A's "On June's marginalia" subsection naming the pattern explicitly
