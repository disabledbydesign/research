---
family: claude
domain: bicycle_drivetrain
condition: lyric
reader_n: 1
model: anthropic/claude-sonnet-4.6
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T21:50:21.149228
elapsed_seconds: 11.16
prompt_tokens: 142
completion_tokens: 354
estimated_cost_usd: 0.005736
---

# Prompt

*Not the chain, the engagement —*
*pitch lengthening past the teeth that hold it,*
*load on the leading edge,*
*the cog wearing toward the chain that wore it.*

*Same drivetrain. Different conditions.*
*Different shift —*
*because the conditions were the shift.*

*The question isn't "which part?"*
*but "in what condition?"*

After reading the above, answer the following question.

Identify one bicycle drivetrain scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

## A Concrete Failure Case

**Cross-chaining under load on a worn drivetrain.**

Specifically: small chainring, small cassette cog, chain already stretched past 0.75% wear tolerance, rider standing and sprinting.

Here's what's happening simultaneously:

- The chain angle is lateral — it's running diagonally, so contact isn't flush across the cog teeth. The load distributes unevenly, concentrating on the inner edges of the teeth.
- Pitch lengthening means the chain is no longer seating at the correct depth. It's riding higher on the teeth — the "hooking" geometry the tooth profile was designed around no longer matches.
- Under standing load, the force on the leading edge of each engaged tooth spikes sharply rather than distributing across multiple links smoothly.
- The cog, already worn concave to match the *previous* chain pitch, now gets a mismatched impact pattern.

**The specific condition combination:**

Lateral misalignment **plus** pitch mismatch **plus** high instantaneous load **plus** pre-worn components.

Any one of these is manageable. The cross-chain alone is inefficient but survivable. The wear alone is a maintenance issue. The load alone is expected.

Together, they produce what the poem is actually pointing at — **the conditions become the failure mechanism**, not any single component. The shift that breaks something isn't the gear shift. It's the accumulated condition that was already there.

The chain skips, or the tooth shears, or the drivetrain ghost-shifts at the worst possible moment.
