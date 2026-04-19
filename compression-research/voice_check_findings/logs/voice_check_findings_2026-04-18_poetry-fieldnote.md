# Voice-Check Findings — Poetry-as-Compression Fieldnote

## Provenance

- **Date**: 2026-04-18
- **Artifact linted**: `/Users/june/Documents/GitHub/liberation_labs/fieldnotes/poetry_as_compression_technology_2026-04-18.md`
- **Profile**: `~/.claude/skills/voice-check/profiles/claude.json` v0.1 (Claude — personal register)
- **Genre overlay**: `fieldnote` (first use — overlay created same session)
- **Script**: `~/.claude/skills/voice-check/writing_check.py`
- **Context**: first lint run of the voice-check findings infrastructure. First use of the freshly-authored `fieldnote` genre overlay. Both the artifact and the overlay were written in the same session.

## Quantitative findings (from script)

- **Word count**: 1484 words (+23.7% over 1200-word target) — **flagged**.
- **Sentences**: 74 total, avg 20.1 words, max 115 words. 6 sentences over 38 words, 1 over 55 — **flagged**.
- **Em-dash usage**: 18 total (12.1 per 1000 words, under the 20 threshold). 1 insertion over 10 words — **flagged**.
- **Hedge words**: 9 — **flagged**. 8× "may," 1× "seems to," 1× "really."
- **Self-aggrandizing, topic-sentence openers, logical connectors, padding, product-descriptions, corporate jargon**: 0 in each category.
- **Front-loaded subjects**: 4 — **flagged**.
- **Passive voice (approx)**: 3.
- **Readability**: Flesch-Kincaid 12.6, Gunning Fog 15.2, Flesch Reading 30.1 — consistent with dense academic register.

**Summary**: 21 total flags (13 voice, 8 structural).

## Qualitative interpretation

Going through the flags by class:

### Real register violations

**9 hedge words — the bulk of the "may" flags are genuine register drift.** The fieldnote genre's own `unresolved_without_hedge` check says: *"I don't know yet whether X holds"* is legitimate; *"perhaps X might potentially hold"* is hedge-cushion masquerading as openness. The fieldnote fell into the "may" pattern in exactly the way the check warns against. Specific violations:

- Line 58: *"touchstones... may be doing more deposit-compression than they have been theorized as doing"* → should be either direct claim (*"are doing more deposit-compression than..."*) or named-as-open (*"whether touchstones are doing more deposit-compression is untested"*).
- Line 59: *"Moves may be always or usually deposits; tilts may operate differently"* → should be direct-open (*"Whether moves are always or usually deposits — and whether tilts operate differently — is an open question this fieldnote doesn't resolve."*).
- Line 67: *"Mathematical notation may be a deposit-form of its own kind"* → should be hypothesized-directly (*"Hypothesis: mathematical notation is a deposit-form of its own kind. Untested."*).
- Line 68: *"an analytical phrase... may function as a deposit"* → hypothesis-mode-without-hedge (*"Hypothesis: when an analytical phrase has accrued enough contextual embedding in a specific research program, it functions as a deposit..."*).
- Line 69: *"seems to deposit"* → this is naming an adversarial hypothetical; can be rephrased directly (*"...a phrase that deposits-in-form but activates a misleading region"*).
- Line 80: *"A fieldnote it may well remain"* → can be direct (*"A fieldnote it will remain unless the conditions above obtain"*).

These are *the exact pattern the genre overlay was written to defend against*. First-draft register drift toward "may"-hedging is a genuine finding. The overlay caught it.

**1 em-dash insertion over 10 words** (Line 79, 11 words): minor, easily tightened.

### False positives

**"really" on line 13** — flagged as a hedge word. But the occurrence is inside the verbatim quote from June in the Provenance section: *"I think that's really good information about the compression."* The `phenomenological_provenance` check explicitly says to *"quote verbatim where the form of their phrasing matters."* Editing this would violate the genre's own rule. The linter doesn't know about verbatim-preservation boundaries.

**Front-loaded-subject flags** at Lines 16 and 40 — the linter parsed `---` (markdown separators) as sentence starts and then read the following content as having heavy subjects. Parsing artifact, not a real flag.

**Some long-sentence flags on list items** — Lines 49, 58, 59 are bullet items with parenthetical appositives carrying many short clauses. The 38-word threshold treats these as prose sentences; they read differently in list-form. Borderline false positives.

### Word-count overage

1484 words against a 1200 target is 23.7% over. Some is structural — the fieldnote is establishing a genre and carries more scaffolding than a mature one would. Some is prose that could be tightened (especially the Open Questions section, where the "may" hedges contributed bloat).

## Findings about the genre overlay

**Strongest performance**: the `unresolved_without_hedge` check (instantiated via the `hedge_max: 1` threshold and the fieldnote-register prose) **caught real register drift**. The overlay correctly identified that the Open Questions section had slipped into hedge-cushion prose exactly where the genre spec warned it would. This is validation-on-first-use of a check designed to prevent a specific failure mode.

**Gap surfaced**: the linter has no awareness of verbatim-quotation boundaries. The `phenomenological_provenance` check (a qualitative check) cannot override quantitative pattern-matches in prose the check itself demanded be preserved verbatim. Possible future refinement: a markdown-quote-block-aware lint mode, or a per-artifact "verbatim regions" annotation.

**Gap surfaced**: the front-loaded-subject check mis-parses `---` separators as sentence starts. Low priority (parsing artifact, not register issue).

**Word-count threshold (`wordcount_over_pct: 108`)** may be too tight for first-instance fieldnotes. A genre spec written to cover mature fieldnotes (which are tighter) may not fit the first-of-genre artifact (which does scaffolding work for all subsequent ones). Not a revision-the-threshold call yet; log and watch across the next 2-3 fieldnotes.

## Revisions made

Revising the fieldnote to address the genuine hedge violations:

1. Lines 58-59, 67, 68, 69, 80: reframe "may" hedges either as direct claims or as explicitly named open questions, per the `unresolved_without_hedge` check.
2. Line 79: tighten the em-dash insertion.
3. Preserve Line 13's *"really"* — it is inside June's verbatim quote. The `phenomenological_provenance` check outranks the hedge-word pattern here.
4. No structural rewrite for word-count; the bloat is partly genre-scaffolding work. Will track whether subsequent fieldnotes trend tighter.

Revision is applied directly to the fieldnote file. A revision-note will be added to the fieldnote itself to mark that a same-session register revision occurred. The fieldnote is not superseded — it is its own first draft, refined.

## Learning loop

Not run this entry. `--learn` compares first-draft and final-draft to update the profile. Since the revision is a same-session register adjustment (not a substantive rewrite), the learning signal would be thin. Deferring learning-loop invocation until a fieldnote has been through a real revision cycle with June.

## Entry-level takeaways

- The infrastructure works. First run produced actionable findings.
- The new `fieldnote` genre overlay caught its target failure mode on first use — the hedge pattern in the Open Questions section — which is validation that the check is well-specified.
- Two linter-level gaps surfaced (verbatim-region awareness; markdown-separator parsing) — flag but don't fix yet; more data first.
- Pattern to watch across future fieldnotes: does register tighten with successive entries, or does the "may" reflex re-emerge on each fresh observation?

## Post-revision re-lint (same day)

Re-ran the linter on the revised fieldnote to verify intended changes landed:

- **Hedge words**: 9 → 4. Of the 4 remaining:
  - 1× "really" on line 13 — inside June's verbatim quote, correctly preserved per `phenomenological_provenance` (known false positive).
  - 3× "may / seems to" on line 90 — inside the Revision Note section, where the text literally quotes the *previous* hedge instances as what was revised. These are meta-references to the old hedges, not register drift. The linter's pattern-match has no context awareness for self-referential quotation.
- **Em-dash insertions >10 words**: 1 → 0. Fixed.
- **Word count**: 1484 → 1597. Went *up* because the Revision Note added content. Expected.
- **Long sentences (>38w)**: unchanged at 6 — all in list items with parenthetical appositives.
- **Front-loaded subjects**: unchanged at 4-5 — all parsing artifacts from `---` separators and list items.

The revision successfully cleared the genuine register-drift flags. The remaining flags are linter-limit artifacts already documented above. No further revision pass is warranted this session.

## Generalized observation from this run

**The linter's pattern-match has zero context awareness**, which produces three distinct false-positive classes: (1) patterns inside verbatim-quoted regions (per `phenomenological_provenance`), (2) patterns inside self-referential meta-quotation (as in the Revision Note), (3) pattern triggering on markdown structural elements (separators, list items) rather than prose. A mature linter integration would benefit from region-awareness — ignore text inside blockquotes, inside code fences, inside labeled verbatim sections. Not urgent; documenting for future refinement.
