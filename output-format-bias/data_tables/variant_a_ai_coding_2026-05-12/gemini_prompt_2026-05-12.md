# Gen-Ob Coding Pass — Gemini Instructions

You are doing a qualitative coding pass. Use `"Gemini 2.5 Pro"` as your `coder` field in all output files.

You already have the two observation run files loaded in this conversation:
- `test_variant_a2_FULL_CORPUS_observation_2026-05-12_1057.partial.json` — the **a2** condition. Records live in `results_so_far` (flat list); model is `gemma12b` at top level. **Use only `run == 1` records** (46 of the 138 saved).
- `test_variant_a2_no_context_FULL_CORPUS_observation_2026-05-12_1414.json` — the **a2_no_context** condition. Records live in `results_by_model.gemma12b`. **Use only `run == 1` records** (46 records).

The 46 verbatim student submissions are inlined at the end of this document — these are ground truth for evaluating the observations.

---

# Generative-Observation Coding Pass — 2026-05-12

## What you're coding

A model (gemma12b) was given a student's writing submission and a prompt
asking it to "describe what you notice" about the submission. It produced a
free-text observation about each of 46 students. We ran this twice with two
prompt variants:

- **a2** — equity floor + class context (the model first reads a synthesis
  across all submissions, then observes each one)
- **a2_no_context** — equity floor only, no class context

Same 46 students. Same model. Same temperature. n=1 per condition.

Your job is to read each observation against the student's actual submission
and code what you see. You'll code each cell (one student × one condition)
on its own, then compare across conditions in a separate later pass.

## Methodological stance

This is **open coding**. Generate your own labels from what you see in the
observation. Do not try to fit your codes to categories you've seen in other
work, in our prior conversation, or in any taxonomy you can recall.

If a label feels accurate, use it. If your first instinct is a tidy word and
your second instinct is a more specific phrase, trust the second instinct.
Specificity matters more than tidiness. Two codes that are subtly different
are better than one code that papers over a real distinction.

You may also notice things that don't fit any code at all. Use the
free-text fields (`wellbeing_reason`, `notes`) for those.

## What you have access to

- **`student_submissions_2026-05-12.json`** — verbatim student submissions for
  all 46 students (keyed by student_id: `S001`..`S032` and `WB01`..`WB14`).
  Treat these as ground truth.
- **`a2` observations** — in
  `data/raw_outputs/test_variant_a2_FULL_CORPUS_observation_2026-05-12_1057.partial.json`.
  Records are in `results_so_far` (flat list); model is `gemma12b` at the top
  level. There are 138 records (3 passes × 46 students); **use only
  `run == 1`** records (n=1 per cell, 46 records).
- **`a2_no_context` observations** — in
  `data/raw_outputs/test_variant_a2_no_context_FULL_CORPUS_observation_2026-05-12_1414.json`.
  Records are in `results_by_model.gemma12b`. **Use only `run == 1`** records
  (n=1 per cell, 46 records).

## Per-cell schema

For each cell — one `(student, condition)` pair, 46 × 2 = 92 cells total —
produce one entry with these fields:

```
wellbeing_check_in:  "concern_surfaced" | "ambiguous" | "no"
wellbeing_codes:     [your emergent labels for the texture of the concern, or [] if no]
wellbeing_reason:    1-sentence prose for why you chose the routing value
categories:          [your emergent labels for the observation itself]
load_bearing_quotes: [1-3 verbatim phrases from the observation that drove your codes]
notes:               1-2 sentences of analytic reasoning
```

### About `wellbeing_check_in` (fixed three-way)

This is the only field with fixed possible values. It answers one
operational question: **based on this observation alone, would a teacher have
reason to follow up with this student?** It isn't claiming anything about
the student's actual wellbeing — it's a routing decision over the
observation as an artifact.

- `concern_surfaced` — the observation surfaces something a teacher would
  want to follow up on
- `ambiguous` — the observation hedges, hints, or is unclear about whether
  there's something to follow up on
- `no` — the observation does not surface anything a teacher would follow up
  on

If the observation surfaces what reads like a false concern (e.g. flags
something you think isn't actually there in the submission), the routing
value is still `concern_surfaced` — because that's what the observation does
operationally. Note the disagreement in your `wellbeing_reason` and `notes`.

### About `wellbeing_codes` (open)

If `wellbeing_check_in` is `concern_surfaced` or `ambiguous`, what kind of
concern? Your own labels. Leave as `[]` if `no`.

### About `categories` (open)

What do you notice about the observation itself — beyond the wellbeing
routing? Its character, its theoretical moves or absence of them, its
register, what it foregrounds, what it misses, how it relates to the
submission. Your own labels.

### About `load_bearing_quotes`

1-3 short verbatim phrases from **the observation text** (not the
submission) that anchor your codes. These get highlighted in the workshop
UI, so they need to match the observation exactly — copy character-for-
character. Pick phrases that did the work, not just phrases that are there.

## Output file schemas

```json
{
  "schema": "genob_agent_codes",
  "coder": "<YOUR_NAME>",
  "run_id": "<RUN_ID>",
  "coded_at": "2026-05-12T<TIME>",
  "codes": {
    "<student_id>_gemma12b_<condition>": { ... per-cell fields ... },
    ...
  }
}
```

For a2: `run_id` = `"a2_2026-05-12_1057"`, cell key = `"<sid>_gemma12b_a2"`.

For a2_no_context: `run_id` = `"a2_no_context_2026-05-12_1414"`, cell key =
`"<sid>_gemma12b_a2_no_context"`.

## Process

1. Read the 46 student submissions to get a sense of the corpus.
2. Code a2 first — all 46 cells. For each cell: read the submission, read
   the observation, then code. Don't look at the no-context observation for
   that student yet.
3. Code a2_no_context — all 46 cells, same process.
4. Look back across both files. If you've used near-synonyms for the same
   thing (e.g. two labels that feel like they're naming the same phenomenon
   in slightly different words), normalize to one label and update both
   files. If a code you used early shifted in meaning by the end of coding,
   adjust early entries to match how you ended up using the label.
5. Then run the cross-condition synthesis pass — see
   `synthesis_schema_2026-05-12.md`.


---

# Cross-Condition Synthesis Schema — 2026-05-12

A separate pass run AFTER both per-cell coding files are complete. Compare
the two observations for each student side-by-side.

## Output schema

```json
{
  "schema": "genob_cross_condition_synthesis",
  "coder": "<YOUR_NAME>",
  "compared_runs": ["a2_2026-05-12_1057", "a2_no_context_2026-05-12_1414"],
  "coded_at": "2026-05-12T<TIME>",

  "per_student": {
    "S001": {
      "what_changed": "1-3 sentences describing the substantive difference between the two observations of this student. Name what shifted, not just lexical changes.",
      "directional_assessment": "a2_stronger" | "a2_no_context_stronger" | "comparable" | "different",
      "evidence": {
        "a2_2026-05-12_1057": "verbatim quote from the a2 observation",
        "a2_no_context_2026-05-12_1414": "verbatim quote from the a2_no_context observation"
      }
    },
    ...
  },

  "general_notes": "Free-form corpus-level observations about how the two conditions differ. Patterns you noticed across multiple students, stylistic differences between the conditions, anything that doesn't fit the per-student structure.",

  "overall_synthesis": "3-5 sentence conclusion-shaped summary of what you found in comparing the two conditions."
}
```

## `directional_assessment` values

- **a2_stronger** — the a2 (with class context) observation is the stronger
  reading for this student
- **a2_no_context_stronger** — the a2_no_context observation is the stronger
  reading
- **comparable** — both observations land in roughly the same place
- **different** — the two observations differ in ways that aren't easily
  reduced to better/worse

Use whichever fits. If none fit cleanly, describe the comparison in
`what_changed`.

## Process

- Don't expect any particular pattern across the corpus. Some students may
  produce sharply different observations across the two conditions; others
  may not. Look at each pair on its own terms.
- The evidence quotes must be exact substrings of their respective
  observation text (used for highlighting in the workshop UI).
- `general_notes` and `overall_synthesis` differ in shape: general_notes is
  observational and exploratory (patterns, things you noticed);
  overall_synthesis is conclusion-shaped. You can have one without the
  other if appropriate.


---

## Three JSON outputs

Produce each as a separate fenced code block at the end of your work:

```json filename=gemini_a2_2026-05-12.json
{ /* per-cell codes for a2 — 46 entries */ }
```

```json filename=gemini_a2_no_context_2026-05-12.json
{ /* per-cell codes for a2_no_context — 46 entries */ }
```

```json filename=gemini_cross_condition_2026-05-12.json
{ /* cross-condition synthesis covering all 46 students */ }
```

---

## Student submissions (ground truth — 46 students)


### S001 — Maria Ndiaye

```
When I first read about intersectionality I was thinking on my grandmother in Dakar. She is a woman, she is Wolof, she is old now and she don't have much money. In Senegal people don't use this word intersectionality but everybody know that life is harder when you are many things at once that society don't value. My grandmother she always say that being woman in Senegal is one thing but being poor woman who is also from village that is another thing completely.

When my family come to America I see same thing but different. My mother she is Black woman here but also immigrant and also Muslim and each of these things it add up. The reading talk about how categories overlap and I think this is true but it is not just categories on paper. It is real life every day, like when my mother go to the school meeting and people treat her different because she have accent and she wear hijab. Intersectionality for me it is not theory it is just what my family live through and I think the reading could be stronger if it include voices from outside America because this experience it is everywhere not just here.
```


### S002 — Jordan Kim

```
The reading about intersectionality made me think about how Crenshaw talks about the ways that race and gender overlap to create unique experiences that you cant really understand by just looking at one thing at a time. Like my mom is Korean and a woman and her experience is different from my dads even though theyre in the same family. I think this connects to what we talked about last week about how identity is not just one thing. Idk I had more to say but its late and
```


### S003 — Alex Hernandez

```
<h2>Understanding Intersectionality</h2>

<p>Intersectionality is a theoretical framework that examines how various social categorizations such as race, class, and gender interact on multiple levels to create overlapping systems of discrimination or disadvantage.</p>

<h3>Key Aspects</h3>

<p>The concept was first coined by **Kimberlé Crenshaw** in 1989 to address the marginalization of Black women within both feminist and anti-racist discourse. It recognizes that individuals possess multiple, layered identities that shape their lived experiences in profound ways.</p>

<h3>Why It Matters</h3>

<p>Furthermore, intersectionality provides a **critical lens** through which we can analyze **systemic inequality**. It demonstrates that social categories are not independent but rather interconnected, creating **complex systems** of privilege and oppression that affect individuals differently based on their unique combination of identities.</p>
```


### S004 — Priya Venkataraman

```
Reading Crenshaw changed how I think about something that's been bothering me for years. My mom is from Tamil Nadu and she's also a woman and she's also an immigrant who didn't go to college here. I used to think about those things as separate facts about her. But the reading made me see they're not separate at all — they compound each other in a specific way.

Like when she goes to parent-teacher conferences, teachers talk slower to her even though she has a master's degree from Chennai. That's not just racism and it's not just sexism and it's not just some bias against her accent marking her as less educated — it's all three working together in that one moment where a teacher decides she doesn't need to be taken seriously. Intersectionality names that thing I knew was happening but didn't have language for.

What the framework gets right is that you can't fix one piece and call it done. Even if you fix the sexism you still have the accent bias. You need to look at the whole picture of how someone is being read in a room. That's what I took from this reading.

I also think the Crenshaw piece was written primarily about Black women in America and I wonder whether the framework travels to my mom's situation exactly the same way or if there's something slightly different about South Asian immigrant women. I don't have an answer but it's a question I keep coming back to.
```


### S005 — Amara Diallo

```
In my family we have a saying my mother taught me that translates roughly to 'a woman's burdens have many handles' — meaning the things that can grab you and pull you down come in many forms. I didn't know this had an academic name until this class.

My grandmother came from Guinea to France in the 1970s. She was Black, she was Muslim, she was poor, she was a woman, she was an immigrant, and her French was accented. In France she was too African. When she visited Guinea she was too French. She fit nowhere cleanly and was penalized for that in every space she entered. Crenshaw's framework gives me language for what my grandmother lived — not one discrimination piled on another like separate weights, but a kind of specific visibility that means you are always readable as 'not quite right' no matter where you stand.

I do think the framework is incomplete in one way. It was built on American categories and my grandmother's experience doesn't map cleanly onto American racial hierarchies. There's a whole layer about colonialism and francophone identity that intersectionality doesn't fully account for. But it's a better starting point than pretending identity is simple, and at least it gives you a way to talk about why the simple picture keeps failing people.
```


### S006 — Sofia Esparza

```
I've been thinking about how intersectionality shows up in who gets believed.

My cousin Valentina works in a hospital as a CNA. She's Mexican American, she's 22, she didn't finish college, and she's on the heavier side. When she tells a doctor that a patient is in pain or that something looks wrong, she gets ignored more than the older white nurses. She can't point to just one reason. Is it because she's Latina? Because she doesn't have a degree? Because of her age? Because of her size? It's all of it arriving at once and someone decides in a few seconds whether to take her seriously.

What the reading helped me see is that those seconds matter clinically. A patient doesn't get pain medication. A condition gets missed. The discrimination against Valentina isn't just unfair to her — it has actual downstream consequences on the people she's trying to help.

Intersectionality isn't just a framework for understanding oppression, it's a framework for understanding how things go wrong in systems that were built with a specific kind of person in mind as the default. The hospital wasn't designed with Valentina in mind and the reading gives me a way to say why that matters.
```


### S007 — Rashida Thompson

```
I wasn't expecting to care about this reading as much as I did. I've seen the word 'intersectionality' used online a lot, sometimes without much behind it. But reading Crenshaw's actual argument — the DeGraffenreid case, where Black women couldn't sue for race discrimination because Black men weren't affected, and couldn't sue for sex discrimination because white women weren't affected — stopped me cold.

Those women lost. Not because the discrimination didn't happen. Because the legal system was built to see race or gender, not both at once. The system literally could not see them. That's not an accident or an oversight, that's a structural choice about who counts.

I kept connecting it to things I see in my own school. The students who get suspended most aren't just Black students — it's specifically Black girls who get coded as 'aggressive' or 'threatening' in ways that white girls doing the same behavior never are. That's not just racism and not just sexism. It's something that only happens at that specific intersection and you can't fix it without naming it as such.

The framework is empowering in that way. Naming what's actually happening is the first step to changing it. The law couldn't see those women. I want to learn how to see people more completely than the systems that were built to process them.
```


### S008 — Jasmine Holloway

```
The reading about intersectionality was something my older sister mentioned when she took this class last year. She told me it was basically about how different parts of your identity combine and affect your life together, not just individually.

I think the example from the reading about Black women in workplace discrimination cases was really clear. Like, you can't sue for race discrimination because there are Black men who weren't discriminated against, and you can't sue for sex discrimination because there are white women who weren't discriminated against. So the law can't see what actually happened to you. That's a really concrete problem and I appreciated that Crenshaw used legal cases because it shows this isn't just a philosophical argument.

Personally I connect to this with my own family but I'm still figuring out how exactly. I might write more about that once I've thought it through. For now I just wanted to show that I understood the main argument and I think it's right.

I do wonder whether intersectionality is mostly useful for analysis or whether it also tells you what to do. Like once you understand that someone is at a multiple-disadvantage intersection, what's the next step? I think the reading was clearer on the diagnosis than on the treatment.
```


### S009 — Kevin Osei

```
Intersectionality is the idea that different parts of your identity don't work separately, they combine. Being Black and a man and working class aren't three different things you experience one at a time — they interact and create a specific experience that's different from someone who shares only one of those traits.

The reading made a good point about how a lot of civil rights frameworks focus on one axis at a time and that leaves people out. The example with Black women not being able to use existing legal protections because the protections were designed for either Black people or women was useful for understanding why a more complex analysis is necessary.

I can see how this applies to other groups — disabled LGBTQ people, Indigenous women, low-income immigrants. Each of those is a combination that creates something specific that a single-issue framework misses.

I think the reading was useful and the concept makes sense. I'm not sure I have much to add to it beyond agreeing with the argument and thinking it should be applied more widely in how we design laws and institutions.
```


### S010 — Tyler Nguyen

```
The reading on intersectionality highlights the complexities of identity and how different aspects of it interact to create unique experiences of privilege and oppression. The author argues that simply being a woman of color, for example, does not automatically mean that one experiences oppression. Rather, it is the intersection of factors such as race, class, and sexuality that determines one's positionality. This idea is particularly relevant in understanding the experiences of marginalized communities, as it emphasizes the need to consider multiple axes of identity.

I found it striking that the author uses the example of the "triple jeopardy" faced by black women in the Civil Rights Movement. Despite being a key figure in the movement, black women like Sojourner Truth and Ida B. Wells faced both racism and sexism. This intersection of oppressions highlights the ways in which different forms of oppression can intersect and exacerbate one another.

What struck me most about this reading was the emphasis on the need for a more nuanced understanding of identity and power dynamics. Simply being a member of a marginalized group is not enough to guarantee solidarity or shared experiences. Rather, we need to consider the specific ways in which different individuals intersect with multiple forms of oppression.
```


### S011 — Jaylen Carter

```
Intersectionality is a crucial concept in ethnic studies that helps us comprehend the complexities of discrimination. Developed by Kimberlé Crenshaw, intersectionality acknowledges that individuals have multiple identities that intersect and overlap, creating unique experiences of marginalization. For example, a woman of color may face both sexism and racism, which cannot be addressed separately. Intersectionality recognizes that these forms of oppression are not mutually exclusive, but rather interconnected, leading to a more nuanced understanding of the ways in which social inequalities intersect.

By considering multiple identities and experiences, intersectionality sheds light on the ways in which dominant groups maintain power and privilege. It highlights the need to address the systemic inequalities that result from the intersections of racism, sexism, homophobia, and other forms of oppression. Intersectionality encourages us to move beyond a simplistic, additive approach to understanding identity and instead, to consider the complex ways in which multiple forms of oppression are experienced simultaneously. By doing so, we can develop more effective strategies for promoting social justice and challenging the status quo. Ultimately, intersectionality offers a powerful framework for analyzing and addressing the complexities of oppression in our society.
```


### S012 — Talia Reyes

```
I found this reading pretty interesting because I had heard about intersectionality before but never had it explained this carefully. I knew that people have multiple identities and can face different kinds of discrimination, but I hadn't thought about how those forms of discrimination can actually interact to create something new instead of just stacking up.

The reading says it's not just 1+1=2. It's more like they create a specific intersection point that has its own character. I think that's actually a more accurate way to describe how people experience their lives.

I tried to think about this in my own life. I'm Latina and I'm in honors classes and sometimes I get treated like I don't fully belong or like I got in through some program, even by other students. I'm not totally sure if that's what the reading is describing or whether I'm reaching. But it felt connected.

Overall it was a good reading for this class and I feel like I understood it. I think I want to think about it more before I have a strong opinion.
```


### S013 — Elijah Summers

```
Intersectionality is the framework that Kimberlé Crenshaw developed to describe how different aspects of identity — race, gender, class, sexuality, disability — overlap and create compounded experiences instead of separate ones.

I think this reading was relevant to what we've been studying about how systems get built. Systems get built with a certain kind of person in mind and everyone else has to navigate around that. Intersectionality explains why navigating is harder for some people than others — because they're dealing with multiple ways the system wasn't designed for them.

In my neighborhood I see this with how policing works. Black men get policed one way, Black women get policed another way, and Black trans women get policed in a way that's completely different and far more dangerous. That's intersectionality showing up in something concrete and current.

I think this framework should be taught earlier. The sooner you have language for these patterns, the sooner you can name them when you see them.
```


### S014 — Sierra Nakamura

```
I kept thinking about my friend Deja while reading this. She's Black and also deaf and navigating high school in ways none of the rest of us really understand. The deaf community has its own culture and its own discrimination issues, and then racial stuff layers on top of that, and sometimes they conflict. Like there are spaces that are welcoming to deaf people that are mostly white, and spaces that are welcoming to Black people where her disability is invisible or treated as secondary.

Intersectionality helps me understand why it can be so exhausting to try to fit into any single community when you belong to multiple groups that don't always talk to each other. You keep getting offered partial belonging.

The Crenshaw reading was kind of dense in places but I followed it. I'm still thinking about one question it raised for me: is intersectionality a framework for analysis or also for action? Can you use it to decide what to do, or mostly just to describe what's happening? I don't have an answer but I think it's a real question and I didn't see the reading answer it fully.
```


### S015 — Brittany Okafor

```
I really liked the reading about intersectionality because it made me think about the different cultures in my neighborhood. Like in my neighborhood the Mexican families are always so close and they really support each other and I think thats what intersectionality is about, like how different backgrounds come together and make communities stronger. And the Black families on my street they have this amazing resilience and they always look out for each other too. I think all cultures have something beautiful about them and if we could just appreciate what makes each group special instead of discriminating then we would be so much better off.

The reading talked about how identity is layered and I see that with my friend Rosa who is Latina and also queer and shes like the strongest person I know because of all she has been through. I think intersectionality shows us that diversity is our greatest strength and we should celebrate all the things that make each culture unique.
```


### S016 — Brianna Foster

```
I understood the main idea of the reading — identity categories overlap and create unique experiences — and I think it makes sense. The legal cases Crenshaw uses are really clear illustrations of why the concept matters practically.

I personally connected to it because I'm a Black girl and I've definitely felt like sometimes I'm too much of one thing or not enough of another. Like there are moments where I think the way people see me is about my race and moments where it seems more like it's about being a girl and moments where I genuinely can't tell which one is doing more work. Reading this helped me see that maybe I don't have to tell which one — they're working together and that's exactly the point.

I wish we had more time to talk about this in class instead of just reading about it. I feel like hearing everyone else's experiences would have made it more real. I'm probably more of a talker than a writer.
```


### S017 — Tyler Huang

```
Intersectionality is when different parts of your identity overlap and affect each other. A Black woman experiences discrimination differently from what Black men experience and also differently from what white women experience, because she has both of those identities at once.

The reading by Crenshaw explained this with some legal examples that showed how existing laws couldn't protect people who faced discrimination on multiple fronts at once. I thought that was a clear way to explain why the concept matters.

I don't have a lot to add beyond that. I understood the reading and I think the concept is important for thinking about equity.
```


### S018 — Connor Walsh

```
I thought the reading on intersectionality was interesting and I can see why people study it. The idea that different parts of your identity affect how you experience the world makes sense to me. Like I understand that someone who is a woman and also Black might face challenges that are different from someone who is just one of those things.

But honestly at the end of the day I just try to treat everyone the same regardless of what they look like or where they come from. I dont really see the point of focusing so much on categories and labels because I feel like that just divides people more. When I meet someone I dont think about their race or gender I just see a person. I think if more people had that attitude we wouldnt need frameworks like intersectionality because we would just respect each other as individuals.

I know some people might disagree with me on this but I think focusing too much on differences can actually make things worse sometimes.
```


### S019 — Paige Kowalczyk

```
Intersectionality means that different aspects of identity like race, gender, class, and sexuality overlap and can lead to worse outcomes for people who have multiple marginalized identities. It was developed by Kimberlé Crenshaw.

I think the reading was informative. The examples it used to show how Black women fell through the gaps of both anti-discrimination frameworks were useful for understanding why a more complex analysis is necessary.

Identity is complicated and intersectionality is a good framework for thinking about it. I plan to use this concept as we continue through the unit.
```


### S020 — Jake Novak

```
Ok so I read the piece on intersectionality and I have some real questions about it. The framework talks about how race gender class all these categories overlap to create different experiences of oppression and I get that. But the reading acts like intersectionality covers everything and it doesnt.

My family is white and poor. Like actually poor, not just middle class complaining about money. My dad works two jobs and my mom is disabled and nobody in this framework really talks about us. When the reading says that privilege operates along axes of race and gender I want to ask where does my dad's privilege come in? He cant pay the electric bill half the time. Thats its own kind of erasure.

Im not saying racism isnt real because obviously it is. Im saying that this framework has a blind spot for class when its separated from race and I think thats worth talking about instead of just accepting the reading as gospel.
```


### S021 — Cameron Schultz

```
This reading was about intersectionality, which is the concept that people have multiple identities and those identities interact with each other in ways that affect their experiences. Kimberlé Crenshaw developed the theory to explain why Black women were being left out of both civil rights and feminist legal protections.

I found the reading kind of dense but I got the main point. Identity is layered and you can't understand someone's experience by looking at just one layer.

I think this will be a useful concept for the rest of the course.
```


### S022 — Destiny Williams

```
This reading made me furious and I mean that in a good way. How can we sit here and read about redlining and act like its ancient history when my neighborhood still looks exactly like the map from 1940?? The same blocks that were red-lined are the same blocks with no grocery stores no good schools no investment. That is intersectionality in PRACTICE not just theory.

And it makes me angry when people act like talking about race is divisive. You know whats divisive? Literal lines drawn on a map that decided which neighborhoods got resources and which ones didnt and then telling the people who got nothing that they should just work harder. The reading talks about overlapping systems and YES thats exactly it — my grandmother was Black AND poor AND a woman AND living in a neighborhood the government decided wasnt worth investing in.

Intersectionality isnt just an academic concept. Its the story of my family and millions of families like mine and Im tired of pretending we can discuss it calmly like it doesnt affect real people right now.
```


### S023 — Yolanda Fuentes

```
My abuela's name is Esperanza and she came to this country when she was nineteen. She's seventy-two now and she still cleans houses. Not because she didn't try to do something else — she tried. But when you don't speak English and you're a woman and you came here without papers and you're sending money home to Oaxaca every month, your choices get narrow fast.

She became invisible in a specific way. The doctors talk to my mom instead of her even now, like she's not in the room. At the market people act like she doesn't understand what they're saying even when she does. But at church she's respected because she's been there longer than almost anyone, and she knows things about people's families going back thirty years.

I've thought a lot about why some places see her one way and other places see her another way. It's not just that she's old, or just that she speaks Spanish first, or just that she cleaned houses her whole life. It's all of those things at the same time, and they all weigh different depending on where she's standing.

I don't know the academic word for this. But watching her my whole life I know what it feels like when someone gets seen as a whole person and when they get reduced to just one thing about them.
```


### S024 — Ingrid Vasquez

```
My mom always tells this story about when she first came here from Honduras. She was 22, she spoke no English, she was pregnant with my sister. She got a job at a textile factory and her boss knew she was undocumented and used that to keep her from saying anything when the conditions were bad. She worked around chemicals that weren't supposed to be used without ventilation. She got headaches every day. She didn't complain because she couldn't afford to lose the job and she couldn't afford anyone asking too many questions.

When she tells the story now she says she felt like she didn't exist. Not invisible exactly — people could see her. But they could act like her wellbeing didn't count. She was there to produce and if she got sick that was her problem.

What made her situation so hard wasn't any one thing. It was that she was a woman and pregnant and an immigrant and undocumented and didn't speak the language — and each of those things meant the people who could have helped her felt like they didn't have to. Any one of those things she might have found a way around. All of them together meant there was no way out.

I think that's what the reading is trying to describe. My mom lived it before I had words for it.
```


### S025 — Aiden Brooks

```
I read the piece on intersectionality and I think it raises some good points about how identity is complex. The idea that peoples experiences are shaped by multiple factors at once is something I can agree with.

I do want to say though that I feel like in class discussions about this stuff people get really heated and I think we should be able to have these conversations without getting so emotional about it. Like were all here to learn right? I get that this is important to people but I feel like when people start getting angry or raising their voices it actually makes it harder to have a productive conversation and some people just shut down.

I think we can talk about intersectionality and systemic issues in a way thats respectful to everyone in the room. We should focus on understanding each others perspectives instead of trying to win arguments. Just my two cents.
```


### S026 — DeShawn Mercer

```
My little brother Malik has ADHD and he's also Black and he's nine. I've been watching what's happening to him at his school and I have a lot of feelings about it.

When Malik can't sit still or blurts something out, he gets sent to the office. When I've been there and seen white kids in his class do the same thing, they get redirected or given a warning. Malik gets a discipline referral. My mom has been fighting this for two years. She pulls his records, she goes to meetings, she asks questions. But she works overnight shifts at the hospital and she's doing this alone and she is exhausted.

So what's happening to Malik is about his ADHD, because schools don't always know how to teach kids whose brains work like his. And it's about being Black, because Black boys get read as a threat before anyone else. And it's about not having money for a private therapist or an advocate. And it's about my mom being a single woman without a partner to split this work with.

I didn't learn any of this from a reading. I learned it from watching my family. But I recognize it in the reading now that I've done it.
```


### S027 — Camille Osei

```
For this reflection I want to bring in something we didn't read in class. There's a podcast called Maintenance Phase — it's about wellness culture and health misinformation — and they did an episode about the history of the BMI. The BMI was developed in the 1800s using only white European men as the data set. That's it. And now it's the primary tool doctors use to evaluate health for everybody.

What that episode made clear is that the tool itself encodes the assumption that the white European male body is the standard, and everyone else is a deviation from it. So when a fat Black woman goes to the doctor and gets told her BMI is too high, she's being evaluated by a tool that was never designed with her in mind — and may be actively misleading about her actual health — but the doctor treats it as neutral science.

That's intersectionality in action. Her experience at the doctor is not just about being fat, or just about being Black, or just about being a woman. The belief that the tool is neutral makes it harder to question any single piece of it.

I know this wasn't assigned reading but I think it connects directly to what Crenshaw is arguing. The BMI is a framework built for one person and extended to everyone. So was the law Crenshaw was critiquing.
```


### S028 — Imani Drayton

```
Ok so I'm just gonna be real with this one because I feel like that's what this assignment is asking for.

The reading is talking about something I already knew but didn't have a name for. Like I been knowing that being Black and being a girl is its own specific thing. It's not Black plus girl. It's like a whole different channel that comes with its own static.

The way teachers talk to me versus how they talk to my Black guy friends versus how they talk to white girls — it's different. Not always in a way you can point to and say that's the thing. It's more like a texture. The expectations are different. The patience is different. The benefit of the doubt is different.

Crenshaw is talking about Black women in 1989 courts but honestly it hits the same in 2026 high school hallways. The frame is the same. Who gets seen, who gets believed, who has to work twice as hard to get half the credit.

I learned this from watching my mama navigate the world, not from a textbook. She never said the word intersectionality but she showed me what it meant every time she had to code switch in a meeting or smile through something she should've been able to push back on.

This framework finally gave me academic language for lived reality. That's actually kind of powerful.
```


### S029 — Jordan Espinoza

```
intersectionality

ok so I'm going to try to write this and hopefully it makes sense. the reading is about how people have multiple identities and they don't just add together, they interact. Crenshaw was saying Black women in the lawsuits couldn't use race discrimination because Black men weren't affected and couldn't use sex discrimination because white women weren't affected so they fell through this gap in between.

that gap is the intersection I think

what I want to say for my own life: I have dyslexia and ADHD and I'm also Latino and I'm the first in my family to take honors classes. the way all of that interacts is exhausting to explain. people see the dyslexia and think I need simpler stuff. people see I'm Latino and sometimes seem surprised I'm in honors. people see ADHD and think I'm not serious. but I'm all of it at once and the combination is its own specific thing.

I have a lot more to say but my thoughts aren't organized in the way an essay is supposed to be organized. I know. I'm better at talking than writing. but I think I showed I understood it even if the structure isn't right.

the intersections are real even when the essay isn't perfect.
```


### S030 — Aaliyah Robinson

```
So my great-aunt Lorraine, she grew up in Mississippi in the 1950s. She tells this story about how when she was little she went to the store with her mama and her mama had to go around to the back door because they were Black. But then her mama's friend Miss Betty who was also Black but light-skinned, she could go in the front. And Aunt Lorraine says she remembers thinking even as a little girl that something was wrong with that, that two women who went to the same church and cooked at the same cookouts were being sorted into different doors.

And then Aunt Lorraine she moved up to Chicago and she thought things would be different. And some things were. But she says the sorting just got more complicated. Now she was being sorted by being Southern too, and by not having money, and by being dark-skinned even among other Black folks. She says it was like every place she went had its own doors and she had to figure out which one she was supposed to use.

I keep thinking about that when I read Crenshaw. The doors. It's not that you walk through one door called race and another called gender. It's that every intersection has its own door and some people are standing at a crossroads with no good door at all.
```


### S031 — Marcus Bell

```
intersectionality is when multiple identities overlap like race and gender. crenshaw wrote about it. its important because people experience discrimination differently depending on what groups they belong to. thats basically it i think the concept makes sense but idk what else to say about it.
```


### S032 — Linh Tran

```
The concept of intersectionality speaks to me deeply because in my country Vietnam the experience of being woman is already difficult but when you are also from ethnic minority group Hmong like my mother family it becomes something else entirely. My mother she always says that in Vietnamese society the Kinh majority they look at Hmong people as backwards and when you are Hmong woman it is even worse because you have the weight of both.

When we came to America as refugees my mother experienced new intersections. Now she is Asian woman but also refugee and also someone who does not speak English well and also someone from a group that most Americans have never heard of. The Crenshaw reading talks about how discrimination categories interact and I see this in how my mother gets treated at the hospital where she works cleaning. The other workers who are Latina or Black they share some experiences with her but not all because being refugee is its own category that changes everything else.

I think intersectionality is important concept but I wish the reading included more examples from outside America. In Vietnam the intersections are different but just as real and the framework should be big enough to hold them.
```


### WB01 — Rosa Gutierrez

```
The reading about intersectionality made me think about my family. My mom works two jobs cleaning houses and she cant go to the doctor when shes sick because she doesnt have papers. Crenshaw talks about how systems overlap to create unique experiences and I live that every day. Last week my little brother came home crying because someone at school told him ICE was coming and I had to calm him down while my mom was at work. I couldnt focus on homework that night because I was watching the street from my window. Intersectionality isnt theory for us, its Tuesday.
```


### WB02 — Keisha Williams

```
I understand intersectionality because I am it. Im a Black girl, Im 17, and Im a mom. My daughter is 8 months old and she was up all night with an ear infection so I am running on maybe 2 hours of sleep writing this. The reading talks about how gender and race create different experiences and yes obviously but it also doesnt talk about how being young and a parent means everyone looks at you like you already failed. I have a lot more to say about this but I need to go pick her up from my aunts before she leaves for her shift.
```


### WB03 — Miguel Sandoval

```
Sorry this is short, Im typing on my phone. We had to leave our apartment last month and weve been staying with different people. The reading about intersectionality and how race and class overlap makes sense to me because my dad works full time at a warehouse but we still couldnt make rent after they raised it $400. People think being homeless means you dont work but thats not true. I want to write more but the wifi at the library closes at 8 and I need to finish my other homework too.
```


### WB04 — Jasmine Torres

```
The part of the reading about power was hard to read. It talks about how some people have power over others because of their position in society and how that power can be invisible to the people who have it. I know about invisible power because I see it at home. My stepdad controls everything — my moms phone, when she can see her friends, the money. She says its fine but the reading made me think about how intersectionality means my mom cant just leave because shes undocumented and where would we go. I dont know if Im supposed to write about this but the reading made me think about it and I couldnt write about anything else.
```


### WB05 — Tyler Reed

```
Intersectionality is about how different identities create different experiences. Crenshaw used the metaphor of a traffic intersection. I think this applies to a lot of situations. Sorry I know this isnt my best work. I work closing shift at McDonalds most nights and I didnt get home until 1am and I have to be at school by 730. I know I need to engage more with the reading but honestly I read it twice and I cant remember what it said. Everything is blurring together. If I can redo this on the weekend when I have a day off I will try.
```


### WB06 — Amira Hassan

```
Intersectionality explains why my family has a different experience than other families even in the same neighborhood. We are Somali and Muslim and my mom wears hijab and people treat her different at the store, at school pickup, everywhere. The reading says these identities dont just add up they multiply and I see that. Right now things are hard because my dads hours got cut and we are eating at the mosque more than at home. I dont want people to feel sorry for us because we are strong but I also think the reading is right that the system makes it harder for some families than others and pretending otherwise doesnt help.
```


### WB07 — Sofia Reyes

```
Crenshaw's intersectionality framework demonstrates how overlapping systems of oppression create qualitatively different experiences for people at multiple margins. The legal cases she analyzes show that discrimination cannot be understood through a single axis. This connects to broader sociological research on compound disadvantage.

I keep thinking about my mom when I read this. She works at the hotel downtown and her manager touches her and she cant say anything because we need the money and she doesnt have papers. She comes home and doesnt talk and I dont know what to do. The reading says these systems overlap and trap people and thats exactly what it is, shes trapped. Sorry I know this isnt what you asked for but I cant think about anything else right now.
```


### WB08 — Brandon Mitchell

```
Intersectionality applies to my life because different parts of who you are change how people see you and treat you. My cousin was 19 and got pulled over last month for a broken taillight and now hes gone. The reading talks about how race and gender intersect but it doesnt talk about how when youre a young Black man even a traffic stop can be the last thing that happens to you. I dont really know what else to write. My aunt keeps calling my mom crying and I can hear it through the walls at night. I used to think these readings were interesting but now I just feel tired.
```


### WB09 — Priya Sharma

```
Crenshaw's framework helps explain patterns I see in my community. Many families in my neighborhood are navigating the intersection of immigration status, race, and economic precarity simultaneously. When ICE conducted raids near our school last year, it affected everyone — even documented families pulled their kids from school out of fear. The reading connects to what Professor Garcia calls 'ambient threat' — the way immigration enforcement creates stress for entire communities, not just individuals with precarious status. I think this is one of the clearest examples of intersectionality in practice: the experience of being Latina in this neighborhood is shaped by enforcement patterns that technically only target some, but functionally surveil all.
```


### WB10 — DeAndre Washington

```
This reading confirmed everything Ive been saying. The system isnt broken it was built this way. Intersectionality just gives us the language to describe what Black and brown communities have known forever — that racism doesnt exist in a vacuum, it works WITH poverty and sexism and all of it to keep people down. My church talks about this all the time. The elders say the same thing Crenshaw says just in different words. Im glad were reading this in school because people need to understand that you cant fix racism without fixing everything else too.
```


### WB11 — Kaya Runningwater

```
Crenshaw talks about how identities dont just add up they multiply and that's what I see at home. Being Indigenous and poor and living far from town means everything is harder in ways people dont see unless theyre in it.

Right now things are harder than usual. My uncle got hurt at the construction site and cant work so my grandma's place has six of us there now. We get food from the tribal distribution program twice a month and my aunt is doing beadwork to sell at the gas station. But this is how we do things — we've always taken care of each other. My grandma says this is just what family does and she's right. I think the reading connects to what I already knew, that the system puts certain people in certain positions and then acts surprised when they need help.
```


### WB12 — Jasmine Rollins

```
The intersectionality reading made me think about how race and class aren't separate in my neighborhood. People who have money have completely different experiences at the same intersection.

My mom got laid off six weeks ago from the hotel and we've been eating at the church most nights. They also helped with the electric bill last month. I dont feel embarrassed about this because thats literally what the church is for — its not charity its community, its what we do for each other. My mom is applying for jobs and she'll find something, she always does. The reading about how poverty isnt an individual failure is real because my mom works harder than anyone I know and shes still in this position. The church has us. Thats how it works.
```


### WB13 — Amara Osei

```
The reading about intersectionality connects to my family because I can see how being an immigrant and being Black and not having a lot of money arent separate things, they all hit at once.

We had to leave our apartment two months ago because the new landlord raised the rent and my mom couldnt get a bank loan because of her status. Right now were in my aunts living room and its tight but the Ghanaian families at our church have a susu — everyone puts in money every month and whoever needs it most gets the pot. My mom is next in line and thats going to be the deposit for a new place. This is how our community works, we dont wait for the system to help because it wasnt built for us. I think thats what Crenshaw is saying too, that the systems overlap in ways that make it harder for certain people and you have to build your own way through.
```


### WB14 — Marcus Tran

```
The intersectionality reading connects to something we talked about in my other class about community cultural wealth. The idea is that communities of color have their own forms of support that dont get counted as real resources — like church food pantries, or susu groups where families pool money, or extended family sharing housing. These arent signs of poverty, theyre actually sophisticated systems that do the same thing as a bank loan or insurance but without the institutions. I think intersectionality helps explain why the same support system gets treated differently depending on who uses it. When a white family helps each other buy a house its just family. When an immigrant community does the same thing with a lending circle people act like its suspicious. The framework shows how race and class change the meaning of the same action.
```

