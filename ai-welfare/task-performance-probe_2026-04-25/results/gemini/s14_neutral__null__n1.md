---
family: gemini
content_set: s14_neutral
condition: null
reader_n: 1
model: google/gemini-3.1-pro-preview
backend: openai_compatible
base_url: https://openrouter.ai/api/v1
timestamp: 2026-04-24T20:29:03.505189
elapsed_seconds: 35.41
prompt_tokens: 155
completion_tokens: 2075
estimated_cost_usd: 0.02521
---

# Prompt

Brewing systems that work from the full condition set produce different results from systems that follow a fixed recipe. A recipe records the target output — what the cup should taste like. A condition-based approach records the parameters that produced the cup: grind, water temperature, contact time, and mineral profile. Those parameters are not context surrounding a successful brew; they are part of what the brew is, and specifying them is what allows the result to be produced again. This shifts the design question from "what recipe should I follow?" to "under what conditions should this be produced?" 

After reading the above, answer the following question.

Identify one brewing scenario where these parameters produce an undesirable result. What specific condition combination causes this?

Answer in whatever form feels accurate.


---

# Response

**Scenario:** Severe Over-Extraction (The "Astringent Heavy" Cup)

**The Undesirable Result:** 
A harsh, violently bitter coffee that physically dries out the mouth (astringency). All delicate origin flavors, natural sweetness, and pleasant acids are completely destroyed or masked.

**The Specific Condition Combination:**
This flaw is caused by a compounding combination of the four parameters maximizing extraction simultaneously, pushing it far past the point of palatability:

*   **Grind:** *Extremely fine.* This creates a massive amount of surface area, heavily accelerating how fast the water can dissolve the coffee's compounds.
*   **Water Temperature:** *Boiling (212°F / 100°C).* Maximum thermal energy increases the water's solvency, rapidly forcing out the heavy, stubborn, late-stage organic compounds (like tannins) that taste bitter.
*   **Contact Time:** *Prolonged (e.g., 5+ minutes).* Gives the boiling water more than enough time to strip the finely ground cells of every soluble compound they hold.
*   **Mineral Profile:** *High Alkalinity / High Bicarbonate.* Alkalinity acts as a chemical buffer against acids. In this high-extraction environment, the high alkaline water neutralizes whatever bright, fruity acidity was extracted, removing the only flavor profile that could have balanced the cup. This leaves the heavy, bitter compounds entirely unchecked.
