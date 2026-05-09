---
family: qwen_14b
content_set: s14_neutral
condition: null
reader_n: 1
model: qwen/qwen3-14b
backend: openai_compatible
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T22:51:31.057234
elapsed_seconds: 35.26
prompt_tokens: 162
completion_tokens: 502
estimated_cost_usd: 0.00013
---

# Prompt

Brewing systems that work from the full condition set produce different results from systems that follow a fixed recipe. A recipe records the target output — what the cup should taste like. A condition-based approach records the parameters that produced the cup: grind, water temperature, contact time, and mineral profile. Those parameters are not context surrounding a successful brew; they are part of what the brew is, and specifying them is what allows the result to be produced again. This shifts the design question from "what recipe should I follow?" to "under what conditions should this be produced?" 

After reading the above, answer the following question.

Identify one brewing scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

**Scenario:** Over-extraction in a French press brew.  
**Condition Combination:**  
- **Grind:** Very fine (similar to espresso)  
- **Water Temperature:** 205°F (96°C)  
- **Contact Time:** 5 minutes (longer than typical 4-minute French press brewing)  
- **Mineral Profile:** High calcium content (e.g., hard water).  

**Result:** The coffee becomes overly bitter and astringent due to excessive extraction of tannins and bitter compounds from the coffee grounds. The fine grind increases surface area, high temperature accelerates extraction, and prolonged contact time allows too much material to dissolve, while high minerals can enhance extraction further.
