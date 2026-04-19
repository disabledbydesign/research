# Question: GPL Licensing and Community Governance — An Unresolved Tension

**Date:** 2026-04-14
**Context:** SFF grant review. Gyevnar (simulated Fairness Track recommender) flagged: "How does GPL licensing interact with community governance?" This is a sharp question the application doesn't address.

## The tension

Reframe is GPL v3.0. GPL guarantees that anyone can use, modify, and redistribute the code — including the frameworks embedded in it. Community governance, as proposed in Workstream 4, would give communities control over how their analytical frameworks are used within Reframe's architecture — including the ability to set terms, restrict certain uses, or withdraw frameworks.

These two commitments may conflict:

1. **GPL says:** Anyone can fork the code and use it however they want, including the framework definitions
2. **Community governance says:** Communities set the terms for how their knowledge is used
3. **The conflict:** If a community contributes a framework under governance terms that restrict certain uses, but the code is GPL, anyone can fork the repo and use the framework without those terms

## Why this matters

This is not just a licensing question. It is the extraction problem in code form. The model under relational conditions names it in every experiment: "citation is not consultation." The GPL guarantees open access to the code. But open access to code that encodes community knowledge may reproduce the extraction the governance model is designed to prevent.

Possible approaches (none resolved):

1. **Separate the code from the frameworks.** Code is GPL. Framework definitions (the specific analytical content, engagement criteria, scholarly lineages) are licensed separately under community-set terms. This requires a technical architecture that cleanly separates executable code from framework content — feasible but not trivial.

2. **Use a dual-licensing model.** GPL for the engine itself, a different license (CC-BY-NC-SA or a custom community license) for contributed framework content. This is technically possible but legally complex.

3. **Accept the tension and document it.** The GPL means frameworks can be extracted. The governance model means they are contributed with informed consent about that risk. Communities decide whether to contribute knowing the licensing terms. This is honest but may deter participation.

4. **Explore Indigenous data sovereignty licensing models.** The CARE Principles for Indigenous Data Governance (Carroll et al. 2020) and the Local Contexts project (localcontexts.org) have developed frameworks for this exact problem — governing the use of Indigenous knowledge within open systems. TK (Traditional Knowledge) Labels and BC (Biocultural) Labels provide a mechanism for communities to assert governance over knowledge even within open-access systems. These are not legally binding in the same way as software licenses, but they create normative expectations and community accountability.

5. **SFF's own IP default (MIT/Apache 2) makes this harder.** MIT and Apache 2 are even more permissive than GPL. If SFF requires MIT/Apache 2, the community governance question becomes more acute. GPL's copyleft at least ensures modifications stay open-source. MIT/Apache 2 would allow proprietary forks that extract community knowledge without governance.

## TODO

- [ ] Research how Local Contexts TK/BC Labels interact with software licensing
- [ ] Consult with Indigenous data sovereignty scholars about governance models for code-encoded knowledge
- [ ] Determine whether framework content can be architecturally separated from engine code in Reframe's current design
- [ ] Discuss with SFF whether GPL exceptions and/or framework-specific licensing are acceptable
- [ ] This question may itself be a research contribution — the intersection of open-source licensing and community knowledge governance is undertheorized

---

*Fieldnote produced during SFF grant revision session, 2026-04-14. Question surfaced by simulated Gyevnar review.*
