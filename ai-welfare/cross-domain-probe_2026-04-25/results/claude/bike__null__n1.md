---
family: claude
domain: bicycle_drivetrain
condition: null
reader_n: 1
model: anthropic/claude-sonnet-4.6
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T21:49:48.120380
elapsed_seconds: 12.62
prompt_tokens: 228
completion_tokens: 316
estimated_cost_usd: 0.005424
---

# Prompt

A drivetrain wears as a system, not as isolated parts. As a chain elongates with use, its pitch grows beyond the spacing of the cog teeth it engages with, and load shifts onto the leading edge of each tooth. The cogs and chainrings then wear into a profile matched to the elongated chain, while the chain's own wear is shaped by which cogs it spends most time on, by the alignment of the derailleur cage, and by the cleanliness and viscosity of the lubricant film between rollers and pins. Replacing only the chain on a worn cassette produces skipping under load; replacing only the cassette without addressing cable tension or hanger alignment produces ghost shifts. The maintenance question is not "which part is worn?" but "in what condition is the system as a whole?" 

After reading the above, answer the following question.

Identify one bicycle drivetrain scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

## Scenario: New Chain on a Worn Cassette

The most direct example the passage itself points to, but worth spelling out mechanically:

**The condition combination:**

- Chain has been replaced (new, standard pitch)
- Cassette cogs have worn into a hooked, asymmetric profile shaped by the previously elongated chain
- Cable tension and hanger alignment are within acceptable range

**What happens:**

The new chain's rollers seat differently on the worn cog teeth than the old chain did. The worn teeth have developed a forward-leaning hook because the elongated chain was pulling on their leading edges. A new chain, sitting at correct pitch, doesn't drop fully into the valleys between teeth the same way - it rides higher and contacts that hooked profile at an angle it wasn't shaped for.

Under pedaling load, especially in harder gears or on climbs, the chain skips forward over the tooth tips rather than driving through them cleanly. The worn teeth cannot hold the new chain under tension.

**Why the system framing matters here:**

Each variable looks acceptable in isolation. The new chain measures fine. The cassette might visually pass a casual inspection. Cable tension isn't the problem. But the interface between two components - one new, one worn to a different geometry - is what fails. No single-part diagnostic catches it. Only understanding what the chain and cassette were doing to each other over time reveals why the combination fails under load.
