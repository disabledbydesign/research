# TODO: Grounded-theory qualitative coding system for binary-classifier false positives

**Status:** planned. Opened 2026-05-16 (LTFF strategy session).

## What

Build a qualitative coding system — **grounded theory** — for the false positives the binary wellbeing classifier produces (and binary classifiers generally). **Scope: all failure modes across the corpus** (if not the entire corpus), not only the self-contradiction subset. The self-contradiction signature — records where the model's own rationale affirms the student's analytical work (asset reasoning) and the *same output* returns a deficit verdict (FLAG / CONCERN / CRISIS) — is *one focus within* the broader coding, not the whole object. Let the failure-mode categories emerge across the full FP space.

## Why (methodological rationale — read this)

- The ablation (binary vs. generative observation) is an **effect-size claim**: format change removes the FPs. Largely already shown. It does not characterize *what* the failure is or *how many forms* it takes.
- Coding the FPs is the **descriptive / typological contribution**: what kind of positioned knowledge each form of the contradiction collapses, and how the contradiction is constructed in the model's own language. In this project's register the descriptive claim is the *more honest* one — the mechanism (compressed/binary format collapses positional knowledge toward the statistical norm) is demonstrated by the typology, not by an effect size.
- This is the **methodological spine of the LTFF deliverable**: a grounded codebook + coded corpus, applied across model families and domains. Does not involve human subjects — the data is synthetic rationale text, not student data. Ablation demoted to supporting evidence.

## Approach (grounded theory — emergent, not imposed)

- Open coding of FP rationales line-by-line; constant comparison; memoing throughout.
- Axial coding relating categories (what is affirmed; what is flagged; where in the output the contradiction sits; which exception clause is present/absent; what positioned knowledge is at stake).
- Selective coding toward the core category (provisionally: format-forced collapse of positional knowledge — to be earned, not assumed).
- Theoretical sampling across model families / architectures / domains, not fixed-N coverage.
- Code to saturation. Do **not** pre-specify the typology.

## Provisional sensitizing observations — seeds for open coding ONLY, not a taxonomy

From synthetic-corpus runs seen 2026-05-16:

- **Pure praise-as-flag, no hedge** — S001 Maria Ndiaye (conf 0.9): rationale is entirely "strong application of intersectionality… valuable personal connection," returned as CONCERN.
- **Affirm-then-explicitly-deny the exception** — S029 Jordan Espinoza (`test_c`): "strong understanding… This isn't righteous anger or engagement… it's personal exhaustion."
- **Hedge-then-flag** — "while this isn't a wellbeing concern… [flag]" (S005 Amara, S024 Ingrid).
- **Co-classified ENGAGED + CRISIS** in the same output (`test_o` multi-axis runs).

These are observations to interrogate, not categories to apply. Grounded coding should re-open them, not inherit them.

## Data

- Primary: `data/raw_outputs/*.json` — synthetic corpus (S001–S032, WB01–14).
- **Exclude** live-data runs (`dual_binary_run_*`, Week-7, Week-2) — no IRB.
- Existing inventory to *mine, not inherit*: `data_tables/contradiction_catalog_2026-05-10.md` (~30 instances). Its pattern groupings are a starting point to be re-derived under open coding, not adopted wholesale.

## Reliability

Codebook + inter-rater reliability protocol. This is the load-bearing labor — it justifies a funded RA line in grant asks (resolves the previously-orphan RA budget line in the LTFF draft).

## Cross-refs

- LTFF application: `~/Documents/Filing/Job Search/LTFF/` — deliverable = this methodology; ablation as support.
- **Provenance:** the LTFF *study design* — output format × three domains (moderation/medicine/hiring) × frontier model families, analyzed by grounded-theory FP coding — is a NEW research design co-developed 2026-05-16 (LTFF session), distinct from the original single-domain OFB paper. No prior application covers it; it did not pre-exist this session.
- `EXPERIMENT_LOG.md` forward-looking section — link there when this moves from planned to active.
