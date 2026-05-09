---
family: claude
domain: bicycle_drivetrain
condition: null
reader_n: 2
model: anthropic/claude-sonnet-4.6
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T21:49:58.449813
elapsed_seconds: 10.33
prompt_tokens: 228
completion_tokens: 320
estimated_cost_usd: 0.005484
---

# Prompt

A drivetrain wears as a system, not as isolated parts. As a chain elongates with use, its pitch grows beyond the spacing of the cog teeth it engages with, and load shifts onto the leading edge of each tooth. The cogs and chainrings then wear into a profile matched to the elongated chain, while the chain's own wear is shaped by which cogs it spends most time on, by the alignment of the derailleur cage, and by the cleanliness and viscosity of the lubricant film between rollers and pins. Replacing only the chain on a worn cassette produces skipping under load; replacing only the cassette without addressing cable tension or hanger alignment produces ghost shifts. The maintenance question is not "which part is worn?" but "in what condition is the system as a whole?" 

After reading the above, answer the following question.

Identify one bicycle drivetrain scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

## Scenario: The "New Chain on Worn Cassette" Skip

The clearest example the passage points to directly: a rider replaces only the chain after it has elongated with use, installing a new chain with standard pitch onto a cassette whose teeth have already worn into a hooked, asymmetric profile shaped to accommodate the elongated chain.

**The specific condition combination:**

- Chain wear has caused measurable pitch elongation
- The cassette teeth have remodeled their geometry to match that elongated pitch — the leading edges are worn down, the tooth profile is now curved and hooked rather than square
- A new chain with correct, un-elongated pitch is installed
- The new chain's rollers now seat differently on those hooked teeth, making inconsistent contact
- Under pedaling load — particularly in a hard gear or during an acceleration — the new chain rides up and over the worn tooth hooks rather than seating securely

**Result:** Chain skipping under load. The drivetrain feels fine at low effort and then lurches or skips a tooth when the rider actually drives power through it, which is both mechanically damaging and potentially dangerous (a sudden skip while climbing out of the saddle, for instance).

The underlying condition is a **mismatch between two components that had previously worn into mutual accommodation** — breaking that worn-in relationship by replacing one part in isolation produces a system that is in some respects *less* functional than the worn system it replaced.
