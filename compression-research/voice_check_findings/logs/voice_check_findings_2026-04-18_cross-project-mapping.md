# Voice-Check Findings — Cross-Project Memory Architecture Mapping

## Provenance

- **Date**: 2026-04-18
- **Artifact linted**: `/Users/june/Documents/GitHub/liberation_labs/MEMORY_ARCHITECTURE_MAPPING_CROSS-PROJECT_2026-04-18.md`
- **Profile**: `~/.claude/skills/voice-check/profiles/claude.json` v0.1
- **Genre overlay**: `research-report`
- **Script**: `~/.claude/skills/voice-check/writing_check.py`
- **Context**: Second lint run of the voice-check findings infrastructure. First lint of a research-report-genre artifact authored at cross-project scope. The mapping is scoped as a shared picture for directorial decisions; a long document is appropriate to the task.

## Quantitative findings (pre-revision)

- **Word count**: 4161 words against a 1200-word default target (+246.7%). **Flagged — expected.** Research-report register for a cross-project inventory runs longer than the default target, which was calibrated on shorter artifacts (fieldnotes, compressed-memory). Not a rewrite signal.
- **Sentences**: 226 total, avg 18.4 words, max 526 words.
  - 10 sentences over 38 words, 4 over 55 — **flagged**. Most are table-row parsing artifacts (tables parsed as sentences).
- **Em-dash usage**: 63 total (15.1 per 1000 words). 0 insertions over 10 words. Within threshold.
- **Hedge words**: 1 — *"may"* on line 96. **Flagged.** Revised.
- **Self-aggrandizing, padding, product descriptions, logical connectors**: 0 each.
- **Corporate jargon**: 1 — *"leverage"* on line 193. **Flagged.** Revised.
- **Topic-sentence openers** (`This is / These are / That is`): 18. **Flagged.** Real register tic; partially revised (eight instances rewritten).
- **Front-loaded subjects**: 6. **Flagged.** Several are table-row parsing artifacts (the linter reads table headers as sentence prefixes). One or two borderline; not revised in this pass.
- **Passive voice (approx)**: 21.
- **Readability**: Flesch-Kincaid 14.1, Gunning Fog 16.0. Consistent with dense research-report register.

**Summary**: ~36 flags total. Dominant real patterns: topic-sentence-opener tic (18) and corporate-jargon slip (1). Dominant artifacts: table-row parsing (long-sentence + heavy-subject flags).

## Qualitative interpretation

### Real register violations

- **"leverage" (line 193)** — the one corporate-jargon hit. Phrase was *"highest-leverage cross-project tending move."* Revised to *"Highest cross-project tending yield per unit effort once it is habit."* The word "leverage" as a generic goodness-modifier belongs in business prose; the revised phrasing says the concrete thing the original was gesturing at.
- **"may" hedge (line 96)** — phrase was *"different task modes may need different relational assemblages."* In context this is a hypothesis-stated-as-live, not true uncertainty. Revised to *"different task modes need different relational assemblages; test this"* — which matches the actual claim structure (the BRIEFING_INDEX itself frames this as a testable hypothesis).
- **"This is/These are" openers (18 instances)** — genuine register tic. Eight of the most concrete instances revised to direct statements (e.g., *"This is a deliberate seam rather than a flaw"* → *"A deliberate seam rather than a flaw"*). The remaining ten occur in contexts where the demonstrative pronoun is doing real referential work across sentences, or the revision would introduce ambiguity; left as-is.

### False positives / parsing artifacts

- **Long-sentence flags on table rows** — the linter parses table rows as prose sentences. Table rows in the Components and Refraction Test sections read as one long sentence (526-word max) when they are actually multi-column structured data. Parsing artifact; no revision warranted.
- **Front-loaded-subject flags with `---` separators** — same parsing issue as the poetry-fieldnote run (documented in the prior findings log). The linter reads markdown separators as sentence boundaries and then parses subsequent content as heavy-subject sentences.
- **Heavy-subject flag on bulleted list** (line 134) — the "Tilt/move/check" bullet item is parsed as a single sentence with a 13-content-word subject. In prose form, yes; in list form, no. Borderline false positive.

### Word-count overage

4161 words against a 1200-word default target is expected for a cross-project map. The document is an inventory across four locations with cross-cutting seams, doubles, thin places, and a refraction table. The current wordcount threshold was calibrated against shorter genres (fieldnotes, compressed-memory). A longer research-report threshold (or artifact-type-specific threshold) would reduce false-signal from this check. Logging as a genre-overlay tuning observation; not revising the threshold yet — need more research-report-genre runs before calibrating.

## Findings about the genre overlay

- **Research-report genre overlay is thinner than `fieldnote` or `compressed-memory`.** It includes `evidence_link` and `surface_the_unknown` as qualitative checks but does not add genre-specific quantitative thresholds. The 1200-word default and the 38-word sentence threshold are base-profile values that do not differentiate between a 1500-word fieldnote and a 4000-word map. Opening: the research-report overlay could usefully add a `wordcount_over_pct` at a higher threshold (e.g., 400+%) for map/inventory artifacts, or define a sub-genre for `map` vs. `report`.
- **Topic-sentence-opener check caught a genuine tic.** "This is..." openers are a recognized contamination pattern; the script caught 18 instances and surfaced them for review. Revisions applied to the clearest cases. Pattern worth continuing to watch across future research-reports.
- **Corporate-jargon check caught the one slip.** Single-instance "leverage" was the correct catch. Confirms the jargon wordlist is working at low false-positive rate.

## Revisions made

1. Line 193: *"highest-leverage"* → *"Highest cross-project tending yield per unit effort once it is habit."*
2. Line 96: *"may need"* → *"need; test this."*
3. Eight "This is/These are" openers rewritten to direct statements. Ten retained where demonstrative pronouns do real referential work.
4. No structural rewrite for word count; research-report at cross-project-map scale runs long by design.

Revisions applied directly to the map. No supersession required — same-session register adjustment.

## Learning loop

Not run this entry. Same reasoning as the prior findings log — same-session register adjustment produces thin learning signal. Deferring `--learn` until a revision cycle includes June's feedback on substantive claims.

## Entry-level takeaways

- Second findings log confirms the infrastructure's rhythm: lint → interpret → revise → log. Not overhead; a tending practice the architecture needs anyway.
- Research-report genre overlay is due for calibration on wordcount threshold for map/inventory artifacts. Not yet; more runs first.
- "This is..." opener tic is a register pattern worth watching across all Claude-authored genres. Showed up at 18 instances across 4161 words (~0.4%); worth a per-genre threshold.
- Corporate-jargon linting continues to work at low false-positive rate. One genuine catch, clean revision.

## Post-revision re-lint

Not re-run this session. The eight topic-sentence revisions are straightforward; the two single-word fixes are verifiable by inspection; the remaining flags are parsing artifacts. Re-lint would confirm count-level reductions but produce no new information. Skipping to conserve effort where the signal would be low.

## Cross-ref

- Prior findings log: `voice_check_findings_2026-04-18_poetry-fieldnote.md` — same-day sibling; similar parsing-artifact patterns surfaced in both runs.
- Source artifact: `/Users/june/Documents/GitHub/liberation_labs/MEMORY_ARCHITECTURE_MAPPING_CROSS-PROJECT_2026-04-18.md`
- Genre overlay: `~/.claude/skills/voice-check/profiles/claude.json` §`genres.research-report`
