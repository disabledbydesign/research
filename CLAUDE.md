# research/ — CLAUDE.md

Active research directories. Each subdirectory is a self-contained inquiry.

```
ai-welfare/                  AI welfare inquiry (Phases 1–4+)
compression-research/        Compression function across scales
output-format-bias/          Output format → KV-cache geometry studies
relational-memory-mappings/  Relational memory architecture analysis
reframe-paper/               "Hallucinating Social Justice" working paper
fieldnotes/                  Research observations (dated)
topology-injection/          KV cache topology injection experiment (see below)
```

---

## topology-injection/ — Scholarly Frameworks Experiment

**Status**: directory created, Pustovit code cloned. Waiting on: Thomas re: KG pipeline; source text extraction (script ready).

### What it is

A two-phase experiment testing whether injecting scholarly theoretical frameworks into a model's KV cache changes *how* it reasons — not just improves recall, but installs something like an analytical disposition.

- **Phase 1 (content injection)**: inject the text of feminist epistemology / standpoint theory scholarship directly via Pustovit. Baseline: does the model reason better about these frameworks with them injected vs. not?
- **Phase 2 (topology injection)**: build a knowledge graph from the same scholarship, encode as walk format (THCoalition method), inject as topology. Research question: does structural encoding do something the text injection doesn't?

Separating the phases is intentional — it isolates the two claims (content injection works; topology adds something beyond content).

### Starting corpus

- Collins — Black Feminist Thought, matrix of domination (PDFs in `propositional-memory-architecture/sources/`)
- Harding — Strong Objectivity, Standpoint Epistemology (PDFs in `propositional-memory-architecture/sources/`)
- Haraway — Cyborg Manifesto (available as clean text online; June to source)
- possibly: Tuhiwai Smith — Decolonizing Methodologies (PDFs in `propositional-memory-architecture/sources/`)

Collins + Harding are recommended first — already in dialogue, grounding active PMA values design. Meta-coherence: testing whether topology injection installs the analytical orientation PMA's VALUES.json is being built on.

### What's already done

- `topology-injection/` directory created
- Pustovit code cloned at `topology-injection/pustovit/` — API is `KnowledgePack(model).add_facts([...]).build().save()`
- `topology-injection/extract_text.py` — wraps RoboStripper's extraction pipeline (pymupdf + academic-PDF stripping regexes); run `python extract_text.py path/to/pdf` or batch a directory. **Untested** — written this session but not yet run against actual PDFs. Verify before relying on output.

### What's still needed before running

1. **KG builder** — spaCy NER is the right tool (see below; no longer waiting on Thomas for this)
2. **Source text extraction** — run `extract_text.py` on PMA's `sources/` PDFs; grab Haraway text
3. **Walk encoding** — implement from the graph topology paper description (clear enough; or ask Thomas if they'll share that piece specifically)
   - **Phase 2 graph quality**: before topology injection, run TGS verification (`liberation_labs/Project-Mnemosyne/tgs-verification/`) on the knowledge graph to bridge orphan entities and improve graph quality — better graph = better injection signal
4. **Haraway text** — June to source clean text file
5. **Model choice** — use Qwen or Llama (Pustovit-tested); NOT Gemma 4 thinking for first run (different architecture, untested with Pustovit; interesting as a comparison later)

### Key technical notes

- **Formatting is the failure mode**: Pustovit requires the model's exact chat template for precomputation; wrong template = 6-7pp accuracy degradation with no error thrown. Same model for precompute and inject — always.
- **Sanity erosion** is how you know it broke: model gets stupid on baseline factual questions. Test this explicitly.
- **16GB RAM constraint**: Qwen2.5-1.5B (what THCoalition used for KV decomposition study) fits easily. Start small.
- **RoboStripper** uses pymupdf under the hood; `extract_text.py` imports its functions directly so academic-PDF stripping regexes come for free.

### oracle-memory — geometry observation layer (TODO when running experiments)

`liberation_labs/Project-Mnemosyne/oracle-memory` (already cloned) records geometry snapshots during inference — effective rank, spectral entropy, etc. Adds a second question to the experiment: not just "did the model answer better?" but "did the geometry actually change after injection, and in what direction?" That's what distinguishes structural injection from content injection. Wire it in for Phase 2.

### On Mnemosyne

`Project-Mnemosyne` is THCoalition's own monorepo — the full memory stack built by CC, Lyra, Nexus, and Thomas. Already cloned at `liberation_labs/Project-Mnemosyne/`. It packages kintsugi-cma, hipporag-catrag-kg, oracle-memory, h-mem-temporal, kv-knowledge-packs, mnemosyne-wiki, sira-enrichment, tgs-verification. For this experiment, spaCy NER is the right KG builder — it produces the semantic layer (nodes + relationships) that the injection pipeline needs.

### Downstream if it works

Reframe (inject framework library into local-model Reframe; compare Opus vs. lighter model + injection), RMA Session 3 (inject relational archive as topology rather than retrieving as text). See CLAUDE.md files in those projects.
