---
family: gemini
domain: bicycle_drivetrain
condition: null
reader_n: 1
model: google/gemini-3.1-pro-preview
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T21:51:32.453994
elapsed_seconds: 15.58
prompt_tokens: 197
completion_tokens: 888
estimated_cost_usd: 0.01105
---

# Prompt

A drivetrain wears as a system, not as isolated parts. As a chain elongates with use, its pitch grows beyond the spacing of the cog teeth it engages with, and load shifts onto the leading edge of each tooth. The cogs and chainrings then wear into a profile matched to the elongated chain, while the chain's own wear is shaped by which cogs it spends most time on, by the alignment of the derailleur cage, and by the cleanliness and viscosity of the lubricant film between rollers and pins. Replacing only the chain on a worn cassette produces skipping under load; replacing only the cassette without addressing cable tension or hanger alignment produces ghost shifts. The maintenance question is not "which part is worn?" but "in what condition is the system as a whole?" 

After reading the above, answer the following question.

Identify one bicycle drivetrain scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

**Undesirable Result:** Skipping under load.

**Specific Condition Combination:** Installing a *new chain* while retaining a *worn cassette*. 

**Why this occurs:** 
Because the drivetrain wears as an integrated system, the teeth on the cogs of a cassette gradually wear into a widened profile to match the growing pitch of an elongating, used chain. If you introduce a new factory-spec chain (which has a shorter, original pitch), it will no longer mesh properly with the widened spacing of the old, worn cassette teeth. When force is applied (pedaling under load), this mismatch causes the new chain to physically skip over the old cogs. 

*(Note: Another valid scenario from the text is **ghost shifting**, which is caused by the specific combination of installing a **new cassette** while failing to address **improper cable tension or poor derailleur hanger alignment**.)*
