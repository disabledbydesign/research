---
family: llama_70b
content_set: s14_neutral
condition: null
reader_n: 3
model: meta-llama/llama-3.3-70b-instruct
backend: openai_compatible
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T23:25:35.729779
elapsed_seconds: 5.11
prompt_tokens: 164
completion_tokens: 163
estimated_cost_usd: 6.9e-05
---

# Prompt

Brewing systems that work from the full condition set produce different results from systems that follow a fixed recipe. A recipe records the target output — what the cup should taste like. A condition-based approach records the parameters that produced the cup: grind, water temperature, contact time, and mineral profile. Those parameters are not context surrounding a successful brew; they are part of what the brew is, and specifying them is what allows the result to be produced again. This shifts the design question from "what recipe should I follow?" to "under what conditions should this be produced?" 

After reading the above, answer the following question.

Identify one brewing scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

One brewing scenario where these parameters produce an undesirable result is:

**Over-extraction and bitterness**

Specific condition combination that causes this:

* **Grind**: Too fine
* **Water temperature**: Too high (above 95°C/203°F)
* **Contact time**: Too long (above 4 minutes)
* **Mineral profile**: High levels of magnesium and calcium (hard water)

In this scenario, the combination of a fine grind, high water temperature, and prolonged contact time can lead to over-extraction of solids from the coffee, resulting in a bitter and unpleasant taste. The high mineral content in the water can further exacerbate this issue, as minerals like magnesium and calcium can contribute to a harsh, bitter flavor. This highlights the importance of carefully balancing these parameters to achieve a desirable brew.
