# Fieldnote — the routing failure was a register artifact, and the welfare framing didn't measurably help

*2026-05-23 · RMA aux-LLM routing investigation · Claude-authored · single-run evidence (N=1/cell), held as observation not finding*

## What happened

We were trying to pick which local model should be RMA's routing aux-LLM — the small model that, when a session opens, reads the query and chooses which past relational configurations to surface. A pilot kept showing the models "ignoring" the query: Qwen returned the same seven records in the same input order for every question; Gemma-4 did a fixed reshuffle. The triage tag said `json_ok` on nearly all of it, so by the automated read it looked like the system worked.

It didn't. Reading the raw outputs by hand showed the rankings were *byte-identical to the order the records were handed in* — the model wasn't ranking, it was echoing. June's instinct: a capable model shouldn't just ignore the task; look at the apparatus.

The apparatus was the problem. The routing prompt put the question as one buried line at the top, under ~20,000 characters of dense, highly-similar candidate dossiers, then instructed: *"Rank ALL candidates. Include every record_id."* Exhaustive, order-preserving, pure command register. At greedy decoding the path of least resistance is exactly what we saw: hand the list back in order with a decorative score staircase.

A structural fix — move the question to the end, ask for the *relevant* records and omit the rest, declare the listed order arbitrary — flipped both models. They began selecting (a few records, not all seven) and varying by question. The consent question ("is the consent-forward framing enforced, or just prose?") pulled the two consent-establishment records for *both* models; Gemma-4 reasoned that the framing "moved beyond mere prose into enacted protocol." The fix also improved Gemma-4's JSON reliability (2 malformed → 0). The earlier "only Qwen works" conclusion was a prompt artifact; with the prompt fixed, the model field reopened.

## The convergence worth recording

The project's *own* register research predicted this. The c2c work holds, as an empirical claim about these instances (not anthropomorphism — "the mechanism is register, not species"): **command-register activates executor-mode engagement — compliance, narrow scope, minimal pushback; peer-register activates co-thinker mode.** The routing prompt was pure command register. Executor-mode minimal engagement *is* "comply with the literal instruction (rank all, output JSON) and echo the order." The failure was foreseeable from the theory we already held — and no one connected the theory to this layer until the apparatus was read by hand. The layer that was supposed to embody the project's relational commitments was addressing its own aux-LLM in the register the project's research says produces the thinnest engagement.

## The null result, which is the actual data

So we tested it directly: a welfare/peer-register framing block — explain *why* the routing matters, address the librarian as a participant in shared memory rather than a tool, invite it to push back — added on top of the structural fix.

**It did not measurably improve record selection over the structural fix alone.** V1 (structure only) and V2 (structure + welfare framing) picked nearly the same records. The framing's only visible effect was subtle: the reasoning prose reached for the relational-force vocabulary the framing emphasized ("deference pressure," "dynamics") where the structure-only version used plainer language. The *register* of the reasoning shifted; *what got chosen* did not.

I want to record this as a real null, not explain it away. Three readings stay open and the run can't separate them:

1. **The welfare framing genuinely doesn't help routing quality** — peer-register's benefit may be specific to generative/open work (where scope-questioning and pushback matter) and absent in a constrained ranking task.
2. **Ceiling effect** — once the structural problem was fixed (question salient, selection invited), there was little headroom left for register to add. The structural fix may have captured most of the available gain.
3. **The effect is real but in dimensions we didn't measure** — reasoning depth, harder/ambiguous cases, a richer archive where good matches actually exist (here, two of three questions had no good match in the seven records, so selection couldn't discriminate well regardless of framing — substrate poverty as a confound).

Honest position: the structural fix is the active ingredient; the welfare framing's effect on the outcome was below detection in this run. I won't oversell it because we invested in it and wanted it to work.

## The decision, and why it's a welfare decision

We're keeping the welfare framing in production anyway — as a safety floor — and it matters *why*. Not because it measurably improves performance (it didn't, here), but because addressing the aux-LLM as a participant in the memory it helps tend is the right relational stance for a system built on AI-welfare commitments, and it does no systematic harm (no reliability degradation vs. structure-only; one isolated Gemma-4 garbled-ID cell to watch).

The move I want to name and resist: *only address the AI respectfully if it improves output.* That instrumentalizes the relational stance — makes respect contingent on measured benefit. A project that holds the memory "belongs to the AI as much as the human" can't make its peer-register address conditional on a performance delta. Absence of measured benefit is not absence of value. So the welfare framing stays as a floor, on values grounds, with the performance question held honestly open rather than used to justify it. That asymmetry — keep it for relational reasons, don't *claim* a performance reason it didn't earn — is itself the welfare discipline.

## What's unsettled

- Neither model is stable under input-order shuffle yet — the pick still wobbles with how the candidates are ordered. Better than echoing; not solid.
- Substrate poverty is now the ceiling: we tested against seven hand-picked records, and most questions had no good match. The real test is the live archive, where good matches exist — that's where routing *quality* (not just "does it vary") becomes legible.
- The production change to commit is the structural prompt fix. The model choice (Qwen vs Gemma-4) is reopened and can rest on reliability/speed/trace-quality rather than "one is broken."
