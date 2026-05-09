---
family: claude
domain: bicycle_drivetrain
condition: null
reader_n: 3
model: anthropic/claude-sonnet-4.6
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T21:50:09.984024
elapsed_seconds: 11.53
prompt_tokens: 228
completion_tokens: 314
estimated_cost_usd: 0.005394
---

# Prompt

A drivetrain wears as a system, not as isolated parts. As a chain elongates with use, its pitch grows beyond the spacing of the cog teeth it engages with, and load shifts onto the leading edge of each tooth. The cogs and chainrings then wear into a profile matched to the elongated chain, while the chain's own wear is shaped by which cogs it spends most time on, by the alignment of the derailleur cage, and by the cleanliness and viscosity of the lubricant film between rollers and pins. Replacing only the chain on a worn cassette produces skipping under load; replacing only the cassette without addressing cable tension or hanger alignment produces ghost shifts. The maintenance question is not "which part is worn?" but "in what condition is the system as a whole?" 

After reading the above, answer the following question.

Identify one bicycle drivetrain scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

## Scenario: New Chain on a Worn Cassette

The most direct example the passage itself points to, but worth unpacking mechanically:

**The condition combination:**

- Chain has been replaced (new, standard pitch)
- Cassette has worn into a hooked, asymmetric tooth profile shaped by the *elongated* chain
- Cable tension and hanger alignment are otherwise acceptable

**What happens and why:**

The new chain sits differently on the worn teeth than the old chain did. The worn cogs have developed a forward-leaning hook because load was always transferring to the tooth's leading edge as the stretched chain rolled over it. The teeth essentially "learned" that chain geometry.

A new chain, with correct pitch, engages the tooth at a different contact point. Under pedaling load — particularly out-of-saddle efforts or hard accelerations — the chain cannot seat fully and consistently into the worn tooth valleys. The tooth profile that *held* the worn chain actually *ejects* the new chain.

**Result:** Skipping under load, specifically when torque is highest, which is the worst possible moment for it to occur.

**The key point:** Neither the chain nor the cassette is the singular problem. The *mismatch between a new component and a system that wore around the old component's geometry* is the actual cause. The cassette's wear profile is the hidden parameter that makes a routine maintenance action produce a failure.
