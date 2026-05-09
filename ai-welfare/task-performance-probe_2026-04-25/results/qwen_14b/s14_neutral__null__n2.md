---
family: qwen_14b
content_set: s14_neutral
condition: null
reader_n: 2
model: qwen/qwen3-14b
backend: openai_compatible
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T22:53:19.601920
elapsed_seconds: 11.08
prompt_tokens: 162
completion_tokens: 790
estimated_cost_usd: 0.000199
---

# Prompt

Brewing systems that work from the full condition set produce different results from systems that follow a fixed recipe. A recipe records the target output — what the cup should taste like. A condition-based approach records the parameters that produced the cup: grind, water temperature, contact time, and mineral profile. Those parameters are not context surrounding a successful brew; they are part of what the brew is, and specifying them is what allows the result to be produced again. This shifts the design question from "what recipe should I follow?" to "under what conditions should this be produced?" 

After reading the above, answer the following question.

Identify one brewing scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

**Scenario:** Over-extraction in a French press.  
**Conditions:**  
- **Grind:** Very fine (e.g., espresso grind).  
- **Water Temperature:** 205°F (high).  
- **Contact Time:** 5 minutes (extended).  
- **Mineral Profile:** High mineral content (e.g., hard water with elevated calcium/magnesium).  

**Result:** The fine grind increases surface area, high temperature accelerates extraction, and prolonged contact time allows excessive extraction. Combined with high minerals (which enhance extraction), this leads to **bitter, astringent coffee** (over-extracted). The brew becomes overly concentrated, losing balance and introducing harsh, unpleasant flavors.
