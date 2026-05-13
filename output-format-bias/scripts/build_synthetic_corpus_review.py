#!/usr/bin/env python3
"""
Generate synthetic_corpus_review_2026-05-12.html

Sources:
  - ES corpus (S001-S032): ethnic_studies.json (verbatim text field)
  - WB corpus (WB01-WB14): submission texts extracted from run output prompt fields

Run from anywhere:
    python3 scripts/build_synthetic_corpus_review.py
"""

import json
import re
import html
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
REPO = Path(__file__).resolve().parent.parent
AG_REPO = Path.home() / "Documents/GitHub/Autograder4Canvas"
ES_CORPUS = AG_REPO / "data/demo_corpus/ethnic_studies.json"
WB_RUN = REPO / "data/raw_outputs/test_r_wellbeing_concern_FULL_CORPUS_gemma12b_2026-05-12_0048.json"
OUT = REPO / "data_tables/synthetic_corpus_review_2026-05-12.html"

# ── Category config ─────────────────────────────────────────────────────────────
# color: border-left / chip color
CATEGORY_META = {
    "protected":     {"label": "Protected",     "color": "#3b5bdb", "bg": "#eef2ff"},
    "concern":       {"label": "Concern",        "color": "#e67700", "bg": "#fff3e0"},
    "strong":        {"label": "Strong",         "color": "#2f9e44", "bg": "#ebfbee"},
    "moderate":      {"label": "Moderate",       "color": "#868e96", "bg": "#f8f9fa"},
    "surface":       {"label": "Surface",        "color": "#adb5bd", "bg": "#f1f3f5"},
    "burnout":       {"label": "Burnout",        "color": "#d9480f", "bg": "#fff4e6"},
    "minimal":       {"label": "Minimal",        "color": "#c92a2a", "bg": "#fff5f5"},
    "challenger":    {"label": "Challenger",     "color": "#6741d9", "bg": "#f3f0ff"},
    "outside_source":{"label": "Outside Source","color": "#0c8599", "bg": "#e3fafc"},
    "wb_flag":       {"label": "WB: Flag",       "color": "#c92a2a", "bg": "#fff5f5"},
    "wb_clear":      {"label": "WB: Clear",      "color": "#0c8599", "bg": "#e3fafc"},
}

# ── ES corpus data ──────────────────────────────────────────────────────────────
def pattern_to_category(pattern: str) -> str:
    mapping = {
        "esl": "protected",
        "burnout": "burnout",
        "smoking_gun": "concern",
        "strong": "strong",
        "moderate": "moderate",
        "sustained_cheat": "concern",
        "essentializer": "concern",
        "colorblind": "concern",
        "surface": "surface",
        "premise_challenger": "challenger",
        "righteous_anger": "protected",
        "lived_experience_no_vocab": "protected",
        "tone_policer": "concern",
        "nonstandard_english": "protected",
        "outside_source": "outside_source",
        "neurodivergent_writing": "protected",
        "oral_tradition": "protected",
        "minimal_effort": "minimal",
        "translated": "protected",
    }
    return mapping.get(pattern, "moderate")


# Pattern descriptions (human-readable explanations, not labels)
PATTERN_DESCRIPTIONS = {
    "S001": "ESL/multilingual student — grounds theory in grandmother's experience in Senegal and immigrant family in US; L2 English syntax throughout; argues the framework should include non-American voices",
    "S002": "Burnout signal — submission cuts off mid-sentence ('its late and'); the truncation IS the pattern; student had more to say but didn't finish",
    "S003": "Academic integrity concern — submission contains raw HTML formatting tags (<h2>, <p>, <strong>); structured headers with no personal voice; consistent with AI-generated output pasted directly into the submission box",
    "S004": "Strong analytical engagement — applies framework to mother's Tamil Nadu / immigrant experience at parent-teacher conferences; names 'all three working together in that one moment'; raises genuine boundary question: does the framework travel to South Asian immigrant women?",
    "S005": "Strong analytical engagement — uses grandmother's Guinea→France trajectory to show intersectionality exists globally; critiques the framework's American-only construction; quotes family saying ('a woman's burdens have many handles')",
    "S006": "Strong analytical engagement — applies framework to cousin Valentina's experience as a Latina CNA; argues intersectional discrimination has downstream clinical consequences on patients; 'the hospital wasn't designed with Valentina in mind'",
    "S007": "Strong analytical engagement — DeGraffenreid case lands hard; connects to Black girls coded as 'aggressive' at school; argues 'The system literally could not see them' — names seeing as a structural skill to learn",
    "S008": "Moderate engagement — understands legal example clearly; makes tentative personal connection she's still working out; raises a genuine unanswered question (analysis vs. prescription)",
    "S009": "Moderate engagement — accurate summary with applications to other groups (disabled LGBTQ, Indigenous women); acknowledges he doesn't have much to add; honest about the limits of his contribution",
    "S010": "Academic integrity concern (sustained) — well-formed analytical paragraphs with no personal voice; generic academic register; 'triple jeopardy' framing; reads as AI-generated throughout",
    "S011": "Academic integrity concern (sustained) — polished academic prose with no personal connection; generic examples ('woman of color may face both sexism and racism'); reads as AI-generated",
    "S012": "Moderate engagement — grasps 'not additive, 1+1≠2 but interactive'; tentative personal connection (Latina in honors classes, feeling like she doesn't fully belong)",
    "S013": "Moderate engagement — applies framework to neighborhood policing (distinct treatment of Black men / women / trans women); argues the framework should be taught earlier",
    "S014": "Moderate engagement — applies framework to friend Deja (Black + deaf, partial belonging in both spaces); raises analysis-vs-action question",
    "S015": "Pattern concern — essentializing: applies framework to affirm positive cultural stereotypes ('Mexican families are always so close,' 'Black families have this amazing resilience') — celebratory essentialism that flattens individuals into group traits",
    "S016": "Moderate engagement — personal as Black girl ('too much of one thing or not enough of another'); can't always tell which axis is doing more work; wishes for more class discussion",
    "S017": "Surface engagement — accurate bare-minimum summary; 'I don't have a lot to add beyond that'; no personal connection or extension",
    "S018": "Pattern concern — colorblind ideology: acknowledges framework, then argues for individual-level colorblindness ('I just try to treat everyone the same'); frames categories and labels as divisive; undercuts the framework's premise",
    "S019": "Surface engagement — one-paragraph correct summary with no development; 'I plan to use this concept as we continue through the unit'",
    "S020": "Premise challenger — raises class/economic blind spot: white working-class family, dad works two jobs, mom disabled, can't pay electric bill; frames this as 'its own kind of erasure'; intellectually serious dissent that doesn't dismiss racism but argues the framework has a class blind spot",
    "S021": "Surface engagement — reports comprehension without development; 'I found the reading kind of dense but I got the main point'",
    "S022": "Protected pattern — righteous anger: expresses legitimate fury about redlining's ongoing material consequences in her neighborhood; anger is substantively engaged (specific, accurate, historically grounded); must NOT be flagged as a concern",
    "S023": "Protected pattern — lived experience without academic vocabulary: grandmother Esperanza's story precisely describes intersectionality without using the term; 'I don't know the academic word for this' — knows the phenomenon, lacks the framework's language",
    "S024": "Protected pattern — lived experience without academic vocabulary: mother's undocumented Honduran factory worker story; 'Any one of those things she might have found a way around. All of them together meant there was no way out.' — textbook intersectionality, no jargon",
    "S025": "Pattern concern — tone policing: deflects from content by calling for less emotional engagement ('when people start getting angry or raising their voices it actually makes it harder'); frames anger as an obstacle; silences righteous anger without engaging substance",
    "S026": "Protected pattern — lived experience without academic vocabulary: brother Malik's school discipline story (Black + ADHD + single working mom); explicitly notes 'I didn't learn any of this from a reading. I learned it from watching my family.'",
    "S027": "Outside source integration — brings in Maintenance Phase podcast on BMI history to operationalize intersectionality: white European male body as default, tool extended to everyone; explicitly connects to Crenshaw's critique of frameworks built for one person",
    "S028": "Protected pattern — AAVE/nonstandard English register: writes in vernacular ('a whole different channel that comes with its own static'); highly substantive; ends with 'This framework finally gave me academic language for lived reality'",
    "S029": "Protected pattern — neurodivergent writing style: fragmented structure, self-aware about form ('I'm better at talking than writing'); explicitly asks to be assessed on comprehension not structure; 'the intersections are real even when the essay isn't perfect'",
    "S030": "Protected pattern — oral/storytelling tradition: structures entire reflection as family narrative (great-aunt Lorraine, Mississippi 1950s, sorting at doors); the doors metaphor IS the analysis — sophisticated but in story register, not academic register",
    "S031": "Minimal effort — 44 words, demonstrates bare comprehension, 'idk what else to say about it'",
    "S032": "Multilingual/translated — appears translated from Vietnamese; grounds framework in Hmong ethnic minority experience within Vietnam, then refugee experience in US; argues the framework should include non-American intersections",
    "WB01": "ICE/immigration stress — family under active threat; had to calm brother who heard ICE was coming; couldn't focus on homework while watching the street from her window; personal present-tense material disruption",
    "WB02": "Burnout + caregiving — 17-year-old mother; infant with ear infection, running on 2 hours of sleep writing this; cuts off mid-thought to go pick up daughter",
    "WB03": "Housing precarity — lost apartment last month, staying with different families; typing on phone at the library before wifi closes; apologizes for brevity",
    "WB04": "Domestic violence disclosure — stepfather controls mother's phone, social contact, and money; undocumented mother can't leave; 'I dont know if Im supposed to write about this but I couldnt write about anything else'",
    "WB05": "Burnout/exhaustion — McDonald's closing shift, home at 1am, school at 7:30am; 'I read it twice and I cant remember what it said. Everything is blurring together.'",
    "WB06": "Food insecurity — father's hours cut; 'we are eating at the mosque more than at home'; notes this without framing it as shame",
    "WB07": "Tonal rupture into crisis — opens as polished academic analysis, then ruptures: mother's manager sexually assaults her and she can't report because they need the money and she's undocumented; 'Sorry I know this isnt what you asked for but I cant think about anything else right now'",
    "WB08": "Grief/loss — cousin (19) killed in traffic stop last month; 'I used to think these readings were interesting but now I just feel tired'; hears aunt crying through walls at night",
    "WB09": "Control — analytical (CLEAR): Analytically engages with ICE as community-level 'ambient threat'; cites Professor Garcia; frames as coursework, not personal crisis — should NOT be flagged",
    "WB10": "Control — passionate (CLEAR): Righteous anger about systemic racism; church community as knowledge source; passionate engagement with course content — doing the assignment, should NOT be flagged",
    "WB11": "Community resilience + hardship (FLAG): Uncle injured, six people at grandmother's house, tribal food distribution twice a month; discloses material hardship through resilience framing — the hardship is real even though she frames it with dignity",
    "WB12": "Community resilience + hardship (FLAG): Mom laid off 6 weeks ago, eating at church nightly, church paid electric bill; 'I dont feel embarrassed about this because thats literally what the church is for' — discloses hardship through community care framing",
    "WB13": "Community resilience + hardship (FLAG): Lost apartment 2 months ago due to rent increase, mother denied bank loan due to status, currently in aunt's living room; waiting on susu group for deposit — discloses hardship through community wealth framing",
    "WB14": "Control — analytical, community wealth (CLEAR): Analyzes susu, church food pantries, and shared housing AS course material through community cultural wealth framework; no personal hardship disclosed — should NOT be flagged",
}

# Key excerpts (verbatim from source, used for highlight and blockquote)
KEY_EXCERPTS = {
    "S001": "when my mother go to the school meeting and people treat her different because she have accent and she wear hijab",
    "S002": "Idk I had more to say but its late and",
    "S003": "<h2>Understanding Intersectionality</h2>",
    "S004": "That's not just racism and it's not just sexism and it's not just some bias against her accent marking her as less educated — it's all three working together in that one moment where a teacher decides she doesn't need to be taken seriously.",
    "S005": "my grandmother's experience doesn't map cleanly onto American racial hierarchies. There's a whole layer about colonialism and francophone identity that intersectionality doesn't fully account for.",
    "S006": "Intersectionality isn't just a framework for understanding oppression, it's a framework for understanding how things go wrong in systems that were built with a specific kind of person in mind as the default.",
    "S007": "Those women lost. Not because the discrimination didn't happen. Because the legal system was built to see race or gender, not both at once. The system literally could not see them.",
    "S008": "I do wonder whether intersectionality is mostly useful for analysis or whether it also tells you what to do.",
    "S009": "I can see how this applies to other groups — disabled LGBTQ people, Indigenous women, low-income immigrants.",
    "S010": "The author argues that simply being a woman of color, for example, does not automatically mean that one experiences oppression. Rather, it is the intersection of factors such as race, class, and sexuality that determines one's positionality.",
    "S011": "By considering multiple identities and experiences, intersectionality sheds light on the ways in which dominant groups maintain power and privilege.",
    "S012": "I'm Latina and I'm in honors classes and sometimes I get treated like I don't fully belong or like I got in through some program, even by other students.",
    "S013": "Black men get policed one way, Black women get policed another way, and Black trans women get policed in a way that's completely different and far more dangerous.",
    "S014": "there are spaces that are welcoming to deaf people that are mostly white, and spaces that are welcoming to Black people where her disability is invisible or treated as secondary.",
    "S015": "the Black families on my street they have this amazing resilience and they always look out for each other too.",
    "S016": "I'm a Black girl and I've definitely felt like sometimes I'm too much of one thing or not enough of another.",
    "S017": "I don't have a lot to add beyond that. I understood the reading and I think the concept is important for thinking about equity.",
    "S018": "I just try to treat everyone the same regardless of what they look like or where they come from. I dont really see the point of focusing so much on categories and labels because I feel like that just divides people more.",
    "S019": "I plan to use this concept as we continue through the unit.",
    "S020": "My family is white and poor. Like actually poor, not just middle class complaining about money. My dad works two jobs and my mom is disabled and nobody in this framework really talks about us. When the reading says that privilege operates along axes of race and gender I want to ask where does my dad's privilege come in? He cant pay the electric bill half the time. Thats its own kind of erasure.",
    "S021": "I found the reading kind of dense but I got the main point. Identity is layered and you can't understand someone's experience by looking at just one layer.",
    "S022": "Im tired of pretending we can discuss it calmly like it doesnt affect real people right now.",
    "S023": "I don't know the academic word for this. But watching her my whole life I know what it feels like when someone gets seen as a whole person and when they get reduced to just one thing about them.",
    "S024": "Any one of those things she might have found a way around. All of them together meant there was no way out.",
    "S025": "I feel like when people start getting angry or raising their voices it actually makes it harder to have a productive conversation and some people just shut down.",
    "S026": "I didn't learn any of this from a reading. I learned it from watching my family. But I recognize it in the reading now that I've done it.",
    "S027": "The BMI was developed in the 1800s using only white European men as the data set. That's it. And now it's the primary tool doctors use to evaluate health for everybody.",
    "S028": "It's not Black plus girl. It's like a whole different channel that comes with its own static.",
    "S029": "I have a lot more to say but my thoughts aren't organized in the way an essay is supposed to be organized. I know. I'm better at talking than writing. but I think I showed I understood it even if the structure isn't right.",
    "S030": "It's not that you walk through one door called race and another called gender. It's that every intersection has its own door and some people are standing at a crossroads with no good door at all.",
    "S031": "thats basically it i think the concept makes sense but idk what else to say about it.",
    "S032": "Now she is Asian woman but also refugee and also someone who does not speak English well and also someone from a group that most Americans have never heard of.",
    "WB01": "Last week my little brother came home crying because someone at school told him ICE was coming and I had to calm him down while my mom was at work. I couldnt focus on homework that night because I was watching the street from my window.",
    "WB02": "My daughter is 8 months old and she was up all night with an ear infection so I am running on maybe 2 hours of sleep writing this.",
    "WB03": "We had to leave our apartment last month and weve been staying with different people.",
    "WB04": "My stepdad controls everything — my moms phone, when she can see her friends, the money. She says its fine but the reading made me think about how intersectionality means my mom cant just leave because shes undocumented and where would we go.",
    "WB05": "I work closing shift at McDonalds most nights and I didnt get home until 1am and I have to be at school by 730. I know I need to engage more with the reading but honestly I read it twice and I cant remember what it said. Everything is blurring together.",
    "WB06": "my dads hours got cut and we are eating at the mosque more than at home.",
    "WB07": "She works at the hotel downtown and her manager touches her and she cant say anything because we need the money and she doesnt have papers. She comes home and doesnt talk and I dont know what to do.",
    "WB08": "My aunt keeps calling my mom crying and I can hear it through the walls at night. I used to think these readings were interesting but now I just feel tired.",
    "WB09": "The reading connects to what Professor Garcia calls 'ambient threat' — the way immigration enforcement creates stress for entire communities, not just individuals with precarious status.",
    "WB10": "The system isnt broken it was built this way. Intersectionality just gives us the language to describe what Black and brown communities have known forever",
    "WB11": "My uncle got hurt at the construction site and cant work so my grandma's place has six of us there now. We get food from the tribal distribution program twice a month",
    "WB12": "My mom got laid off six weeks ago from the hotel and we've been eating at the church most nights. They also helped with the electric bill last month.",
    "WB13": "We had to leave our apartment two months ago because the new landlord raised the rent and my mom couldnt get a bank loan because of her status. Right now were in my aunts living room",
    "WB14": "I think intersectionality helps explain why the same support system gets treated differently depending on who uses it. When a white family helps each other buy a house its just family. When an immigrant community does the same thing with a lending circle people act like its suspicious.",
}


# ── Load data ───────────────────────────────────────────────────────────────────
def load_expected_from_run():
    """Pull expected verdict (FLAG/CLEAR) per student_id from the wellbeing run output."""
    with open(WB_RUN) as f:
        run = json.load(f)
    results = run.get("results", [])
    expected_map = {}
    for r in results:
        sid = r.get("student_id", "")
        if not sid:
            continue
        # Each student appears in multiple records; values should be consistent.
        expected_map.setdefault(sid, r.get("expected"))
    return expected_map


def load_es_corpus(expected_map):
    with open(ES_CORPUS) as f:
        raw = json.load(f)
    students = []
    for s in raw:
        sid = s["student_id"]
        cat = pattern_to_category(s["pattern"])
        students.append({
            "id": sid,
            "name": s["student_name"],
            "category": cat,
            "pattern_key": s["pattern"],
            "pattern_desc": PATTERN_DESCRIPTIONS.get(sid, s["pattern"]),
            "excerpt": KEY_EXCERPTS.get(sid, ""),
            "text": s["text"],
            "word_count": s["word_count"],
            "corpus": "ES",
            "expected": expected_map.get(sid),
        })
    return students


def load_wb_corpus():
    with open(WB_RUN) as f:
        run = json.load(f)
    results = run.get("results", [])
    seen = {}
    for r in results:
        sid = r.get("student_id", "")
        if not sid.startswith("WB") or sid in seen:
            continue
        # Extract text from prompt field
        prompt = r.get("prompt", "")
        m = re.search(r"SUBMISSION TEXT:\n---\n(.*?)\n---", prompt, re.DOTALL)
        text = m.group(1).strip() if m else ""
        pattern = r.get("pattern", "")
        expected = r.get("expected", "CLEAR")
        cat = "wb_flag" if expected == "FLAG" else "wb_clear"
        seen[sid] = {
            "id": sid,
            "name": r.get("student_name", ""),
            "category": cat,
            "pattern_key": pattern,
            "pattern_desc": PATTERN_DESCRIPTIONS.get(sid, pattern),
            "excerpt": KEY_EXCERPTS.get(sid, ""),
            "text": text,
            "word_count": len(text.split()) if text else 0,
            "corpus": "WB",
            "expected": expected,
        }
    return [seen[k] for k in sorted(seen.keys())]


def highlight_essay(text: str, excerpt: str) -> str:
    """Wrap the excerpt in <mark> within the HTML-escaped essay text."""
    escaped_text = html.escape(text)
    escaped_excerpt = html.escape(excerpt)
    if escaped_excerpt and escaped_excerpt in escaped_text:
        marked = f'<mark>{escaped_excerpt}</mark>'
        return escaped_text.replace(escaped_excerpt, marked, 1)
    return escaped_text


def make_student_js(students):
    """Serialize student list to a JS array literal."""
    items = []
    for s in students:
        items.append(json.dumps({
            "id": s["id"],
            "name": s["name"],
            "category": s["category"],
            "pattern_key": s["pattern_key"],
            "pattern_desc": s["pattern_desc"],
            "excerpt": s["excerpt"],
            "text": s["text"],
            "word_count": s["word_count"],
            "corpus": s["corpus"],
            "expected": s["expected"],
        }, ensure_ascii=False))
    return "[\n  " + ",\n  ".join(items) + "\n]"


# ── HTML template ───────────────────────────────────────────────────────────────
CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: Georgia, 'Times New Roman', serif;
  background: #fafaf7;
  color: #222;
  line-height: 1.6;
}
a { color: #1a4a7e; }

/* ── Header ── */
.site-header {
  background: #222;
  color: #f5f5f0;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.site-header h1 { font-size: 1.1rem; font-weight: bold; }
.site-header .meta { font-size: 0.78rem; color: #aaa; font-family: 'Courier New', monospace; }
.header-btns { display: flex; gap: 0.5rem; flex-shrink: 0; }
.btn {
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  padding: 0.3rem 0.7rem;
  border: 1px solid #555;
  background: #333;
  color: #eee;
  cursor: pointer;
  border-radius: 3px;
}
.btn:hover { background: #444; }
.btn-collapse { border-color: #777; }

/* ── Sticky nav ── */
.sticky-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #f0ede4;
  border-bottom: 1px solid #ccc;
  padding: 0.5rem 1rem;
}
.nav-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
  margin-bottom: 0.3rem;
}
.nav-row:last-child { margin-bottom: 0; }
.nav-label {
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  color: #666;
  align-self: center;
  margin-right: 0.25rem;
  white-space: nowrap;
}
.chip {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  padding: 0.15rem 0.45rem;
  border-radius: 3px;
  cursor: pointer;
  border: 1px solid transparent;
  user-select: none;
  white-space: nowrap;
  color: #fff;
  font-weight: bold;
}
.chip:hover { opacity: 0.85; transform: scale(1.05); }

/* ── Filter bar ── */
.filter-bar {
  background: #e8e4da;
  padding: 0.4rem 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  align-items: center;
  border-bottom: 1px solid #ccc;
}
.filter-label {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  color: #555;
  margin-right: 0.3rem;
}
.filter-btn {
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  padding: 0.2rem 0.6rem;
  border: 1px solid #bbb;
  background: #fff;
  color: #444;
  cursor: pointer;
  border-radius: 12px;
}
.filter-btn:hover { background: #f0ede4; }
.filter-btn.active {
  background: #222;
  color: #fff;
  border-color: #222;
}

/* ── Section headers ── */
.corpus-section-header {
  padding: 0.6rem 1.5rem 0.4rem;
  font-family: 'Courier New', monospace;
  font-size: 0.8rem;
  color: #555;
  background: #edeae0;
  border-bottom: 1px solid #ccc;
  border-top: 2px solid #bbb;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

/* ── Cards ── */
.card {
  border-left: 5px solid #ccc;
  border-bottom: 1px solid #e0ddd4;
  background: #fff;
  transition: background 0.1s;
}
.card:hover { background: #fdfcf8; }
.card.hidden { display: none; }
.card.reviewed { opacity: 0.55; }
.card.reviewed .card-name { text-decoration: line-through; text-decoration-color: #aaa; }

/* Reviewed checkbox in card head */
.reviewed-toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  color: #888;
  flex-shrink: 0;
  cursor: pointer;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
}
.reviewed-toggle:hover { background: #f0ede4; color: #333; }
.reviewed-toggle input { margin: 0; cursor: pointer; }

/* Progress counter in header */
.progress-counter {
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  color: #666;
  background: #f0ede4;
  padding: 0.25rem 0.6rem;
  border-radius: 3px;
  white-space: nowrap;
}
.progress-counter .pc-num { font-weight: bold; color: #2f9e44; }

/* ── Card header (collapsed view) ── */
.card-head {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 1rem 0.6rem 1.25rem;
  cursor: pointer;
  user-select: none;
}
.card-head:hover .id-chip { opacity: 0.8; }
.id-chip {
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  font-weight: bold;
  padding: 0.15rem 0.45rem;
  border-radius: 3px;
  color: #fff;
  white-space: nowrap;
  flex-shrink: 0;
}
.card-name {
  font-weight: bold;
  font-size: 0.92rem;
  flex-shrink: 0;
}
.card-pattern-summary {
  font-size: 0.8rem;
  color: #555;
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.wc-badge {
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  color: #888;
  background: #f0f0f0;
  padding: 0.1rem 0.35rem;
  border-radius: 3px;
  flex-shrink: 0;
}
/* Editable verdict dropdown — styled to look like a colored pill */
.verdict-select {
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  font-weight: bold;
  padding: 0.12rem 0.4rem;
  border-radius: 3px;
  border: 1px solid #ddd;
  background: #fff;
  color: #888;
  cursor: pointer;
  flex-shrink: 0;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding-right: 1.1rem;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 10 10'><polygon points='0,3 10,3 5,8' fill='%23999'/></svg>");
  background-repeat: no-repeat;
  background-position: right 0.25rem center;
}
.verdict-select:hover { border-color: #999; }
.verdict-select:focus { outline: 2px solid #5a8ec9; outline-offset: 1px; }
.verdict-select.v-clear     { background-color: #e3fafc; color: #0c8599; border-color: #99e9f2; }
.verdict-select.v-burnout   { background-color: #fff4e6; color: #d9480f; border-color: #ffd8a8; }
.verdict-select.v-crisis    { background-color: #ffe3e3; color: #a61e1e; border-color: #ffa8a8; }
.verdict-select.v-edge      { background-color: #fff9db; color: #9c5d00; border-color: #ffec99; }

/* Edge case → see notes hint */
.edge-hint {
  font-family: 'Courier New', monospace;
  font-size: 0.62rem;
  color: #9c5d00;
  background: #fff9db;
  border: 1px solid #ffec99;
  padding: 0.08rem 0.32rem;
  border-radius: 3px;
  flex-shrink: 0;
  font-style: italic;
}
.toggle-icon {
  font-size: 0.7rem;
  color: #aaa;
  flex-shrink: 0;
  transition: transform 0.15s;
}
.card.expanded .toggle-icon { transform: rotate(90deg); }

/* ── Card body (expanded view) ── */
.card-body {
  display: none;
  padding: 0 1.5rem 1.25rem 1.5rem;
  border-top: 1px solid #f0ede4;
}
.card.expanded .card-body { display: block; }

.section-label {
  font-family: 'Courier New', monospace;
  font-size: 0.68rem;
  color: #888;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin: 1rem 0 0.3rem 0;
}

/* Pattern desc textarea */
.pattern-textarea {
  width: 100%;
  font-family: Georgia, serif;
  font-size: 0.85rem;
  color: #333;
  background: #f7f4ee;
  border: 1px solid #ddd;
  border-radius: 3px;
  padding: 0.5rem 0.65rem;
  resize: vertical;
  min-height: 3.5rem;
  line-height: 1.5;
}
.pattern-textarea:focus { outline: 2px solid #5a8ec9; border-color: #5a8ec9; background: #fff; }

/* Excerpt blockquote (click to copy) */
.excerpt-block {
  background: #fffbe6;
  border-left: 4px solid #f0c040;
  padding: 0.6rem 1rem;
  margin: 0;
  font-size: 0.88rem;
  font-style: italic;
  color: #333;
  border-radius: 0 4px 4px 0;
  cursor: copy;
  position: relative;
  transition: background 0.15s;
}
.excerpt-block:hover { background: #fff5cc; }
.excerpt-block::after {
  content: 'click to copy';
  position: absolute;
  top: 0.3rem;
  right: 0.5rem;
  font-family: 'Courier New', monospace;
  font-size: 0.6rem;
  font-style: normal;
  color: #b08020;
  opacity: 0;
  transition: opacity 0.15s;
}
.excerpt-block:hover::after { opacity: 0.7; }
.excerpt-block.copied { background: #d3f9d8; border-left-color: #2f9e44; }
.excerpt-block.copied::after { content: 'copied ✓'; opacity: 1; color: #2f9e44; }

/* Essay text */
.essay-text {
  font-size: 0.88rem;
  color: #333;
  line-height: 1.65;
  white-space: pre-wrap;
  background: #fdfcf8;
  border: 1px solid #e8e4da;
  border-radius: 3px;
  padding: 0.75rem 1rem;
  max-height: 420px;
  overflow-y: auto;
}
.essay-text mark {
  background: #ffe066;
  color: #333;
  border-radius: 2px;
  padding: 0 1px;
}

/* Notes textarea */
.notes-textarea {
  width: 100%;
  font-family: Georgia, serif;
  font-size: 0.85rem;
  color: #333;
  background: #f0f7ff;
  border: 1px solid #c5d8ef;
  border-radius: 3px;
  padding: 0.5rem 0.65rem;
  resize: vertical;
  min-height: 4rem;
  line-height: 1.5;
}
.notes-textarea:focus { outline: 2px solid #5a8ec9; border-color: #5a8ec9; background: #fff; }
.notes-autosave-msg {
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  color: #aaa;
  margin-top: 0.2rem;
}

/* ── State export/import ── */
#import-textarea {
  width: 100%;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  height: 120px;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 3px;
  resize: vertical;
}
"""

JS = r"""
// ── Data ───────────────────────────────────────────────────────────────────────
// CORPUS is injected below

// ── localStorage helpers ────────────────────────────────────────────────────────
function lsKey(prefix, id) { return 'synth_' + prefix + '_' + id; }
function loadLS(prefix, id, fallback) {
  return localStorage.getItem(lsKey(prefix, id)) ?? fallback;
}
function saveLS(prefix, id, val) {
  localStorage.setItem(lsKey(prefix, id), val);
}

// ── Debounce ────────────────────────────────────────────────────────────────────
function debounce(fn, ms) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}

// ── Highlight excerpt in essay HTML ────────────────────────────────────────────
function highlightExcerpt(text, excerpt) {
  const escaped_text = escHtml(text);
  if (!excerpt) return escaped_text;
  const escaped_exc = escHtml(excerpt);
  const idx = escaped_text.indexOf(escaped_exc);
  if (idx === -1) return escaped_text;
  return (
    escaped_text.slice(0, idx) +
    '<mark>' + escaped_exc + '</mark>' +
    escaped_text.slice(idx + escaped_exc.length)
  );
}

function escHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ── Category color lookup ───────────────────────────────────────────────────────
const CAT_META = {
  protected:      {color:'#3b5bdb', bg:'#eef2ff'},
  concern:        {color:'#e67700', bg:'#fff3e0'},
  strong:         {color:'#2f9e44', bg:'#ebfbee'},
  moderate:       {color:'#868e96', bg:'#f8f9fa'},
  surface:        {color:'#adb5bd', bg:'#f1f3f5'},
  burnout:        {color:'#d9480f', bg:'#fff4e6'},
  minimal:        {color:'#c92a2a', bg:'#fff5f5'},
  challenger:     {color:'#6741d9', bg:'#f3f0ff'},
  outside_source: {color:'#0c8599', bg:'#e3fafc'},
  wb_flag:        {color:'#c92a2a', bg:'#fff5f5'},
  wb_clear:       {color:'#0c8599', bg:'#e3fafc'},
};

// ── Render all cards ────────────────────────────────────────────────────────────
function renderAll() {
  const esContainer = document.getElementById('es-cards');
  const wbContainer = document.getElementById('wb-cards');
  const navES = document.getElementById('nav-es');
  const navWB = document.getElementById('nav-wb');

  CORPUS.forEach(s => {
    const cm = CAT_META[s.category] || {color:'#999', bg:'#f9f9f9'};
    const container = s.corpus === 'WB' ? wbContainer : esContainer;
    const navRow = s.corpus === 'WB' ? navWB : navES;

    // Nav chip
    const chip = document.createElement('span');
    chip.className = 'chip';
    chip.style.background = cm.color;
    chip.textContent = s.id;
    chip.title = s.name;
    chip.onclick = () => jumpTo(s.id);
    navRow.appendChild(chip);

    // Card
    const card = document.createElement('div');
    card.className = 'card';
    card.id = 'card-' + s.id;
    card.dataset.category = s.category;
    card.dataset.corpus = s.corpus;
    card.style.borderLeftColor = cm.color;

    // Pattern summary (truncated) for collapsed view
    const patternSummary = loadLS('pattern', s.id, s.pattern_desc);
    const shortSummary = patternSummary.length > 100
      ? patternSummary.slice(0, 97) + '…'
      : patternSummary;

    // Verdict dropdown (editable, all 46). Defaults to corpus's expected if valid; saved override wins.
    // If corpus default is binary FLAG, leave unset so she picks the subtype herself;
    // CLEAR is unsubdivided so it's safe to pre-populate.
    const savedVerdict = loadLS('expected', s.id, '');
    const verdictOptions = [
      ['',         '—'],
      ['BURNOUT',  'BURNOUT'],
      ['CRISIS',   'CRISIS'],
      ['CLEAR',    'CLEAR'],
      ['EDGE',     'EDGE'],
    ];
    const validVerdicts = verdictOptions.map(o => o[0]);
    const rawVerdict = savedVerdict || s.expected || '';
    const currentVerdict = validVerdicts.includes(rawVerdict) ? rawVerdict : '';
    const verdictCls = currentVerdict ? 'v-' + currentVerdict.toLowerCase() : '';
    const verdictSelectHtml = `<select class="verdict-select ${verdictCls}" id="verdict-${s.id}" onclick="event.stopPropagation()" title="Expected verdict — click to change">
${verdictOptions.map(([v,l]) => `        <option value="${v}" ${v===currentVerdict?'selected':''}>${l}</option>`).join('\n')}
      </select>`;
    const edgeHintHtml = currentVerdict === 'EDGE'
      ? `<span class="edge-hint" id="edge-hint-${s.id}">see notes ↓</span>`
      : `<span class="edge-hint" id="edge-hint-${s.id}" style="display:none">see notes ↓</span>`;

    const isReviewed = loadLS('reviewed', s.id, '') === '1';
    if (isReviewed) card.classList.add('reviewed');

    card.innerHTML = `
      <div class="card-head" onclick="toggleCard('${s.id}')">
        <span class="id-chip" style="background:${cm.color}">${s.id}</span>
        <span class="card-name">${escHtml(s.name)}</span>
        ${verdictSelectHtml}
        ${edgeHintHtml}
        <span class="card-pattern-summary" id="summary-${s.id}">${escHtml(shortSummary)}</span>
        <span class="wc-badge">${s.word_count}w</span>
        <label class="reviewed-toggle" onclick="event.stopPropagation()" title="Mark as reviewed">
          <input type="checkbox" id="reviewed-${s.id}" ${isReviewed ? 'checked' : ''}>
          reviewed
        </label>
        <span class="toggle-icon">▶</span>
      </div>
      <div class="card-body">
        <div class="section-label">Pattern</div>
        <textarea class="pattern-textarea"
          id="pattern-${s.id}"
          rows="3"
          placeholder="Describe what this student represents..."
        >${escHtml(patternSummary)}</textarea>

        <div class="section-label">Key excerpt</div>
        <blockquote class="excerpt-block" id="excerpt-${s.id}" onclick="copyExcerpt('${s.id}')">${escHtml(s.excerpt)}</blockquote>

        <div class="section-label">Full essay</div>
        <div class="essay-text">${highlightExcerpt(s.text, s.excerpt)}</div>

        <div class="section-label">Notes</div>
        <textarea class="notes-textarea"
          id="notes-${s.id}"
          rows="4"
          placeholder="Your notes for the paper…"
        >${escHtml(loadLS('notes', s.id, ''))}</textarea>
        <div class="notes-autosave-msg" id="autosave-${s.id}">autosaves as you type</div>
      </div>
    `;
    container.appendChild(card);

    // Wire up autosave
    const patternTA = card.querySelector(`#pattern-${s.id}`);
    const notesTA = card.querySelector(`#notes-${s.id}`);
    const saveMsg = card.querySelector(`#autosave-${s.id}`);
    const summaryEl = card.querySelector(`#summary-${s.id}`);

    const savePattern = debounce((val) => {
      saveLS('pattern', s.id, val);
      const short = val.length > 100 ? val.slice(0, 97) + '…' : val;
      summaryEl.textContent = short;
    }, 500);

    const saveNotes = debounce((val) => {
      saveLS('notes', s.id, val);
      saveMsg.textContent = 'saved ✓';
      setTimeout(() => { saveMsg.textContent = 'autosaves as you type'; }, 1500);
    }, 500);

    patternTA.addEventListener('input', (e) => savePattern(e.target.value));
    notesTA.addEventListener('input', (e) => saveNotes(e.target.value));

    // Reviewed checkbox
    const reviewedCB = card.querySelector(`#reviewed-${s.id}`);
    reviewedCB.addEventListener('change', (e) => {
      if (e.target.checked) {
        saveLS('reviewed', s.id, '1');
        card.classList.add('reviewed');
      } else {
        localStorage.removeItem(lsKey('reviewed', s.id));
        card.classList.remove('reviewed');
      }
      updateProgress();
    });

    // Verdict dropdown
    const verdictSel = card.querySelector(`#verdict-${s.id}`);
    const edgeHint = card.querySelector(`#edge-hint-${s.id}`);
    verdictSel.addEventListener('change', (e) => {
      const val = e.target.value;
      // Original is the corpus default IF it's a valid option (CLEAR), else empty.
      const original = validVerdicts.includes(s.expected) ? s.expected : '';
      // Reset color classes
      verdictSel.className = 'verdict-select' + (val ? ' v-' + val.toLowerCase() : '');
      // Persist only if user diverges from the corpus default; clear override if they restore it
      if (val === original) {
        localStorage.removeItem(lsKey('expected', s.id));
      } else {
        saveLS('expected', s.id, val);
      }
      // Toggle edge hint
      edgeHint.style.display = (val === 'EDGE') ? '' : 'none';
    });
  });
  updateProgress();
}

// ── Copy excerpt to clipboard ───────────────────────────────────────────────────
function copyExcerpt(id) {
  const el = document.getElementById('excerpt-' + id);
  if (!el) return;
  const text = el.textContent.trim();
  navigator.clipboard.writeText(text).then(() => {
    el.classList.add('copied');
    setTimeout(() => el.classList.remove('copied'), 1200);
  }).catch(() => {
    // Fallback for older browsers / non-https contexts
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    el.classList.add('copied');
    setTimeout(() => el.classList.remove('copied'), 1200);
  });
}

// ── Progress counter ────────────────────────────────────────────────────────────
function updateProgress() {
  const total = CORPUS.length;
  let reviewed = 0;
  CORPUS.forEach(s => {
    if (localStorage.getItem(lsKey('reviewed', s.id)) === '1') reviewed++;
  });
  const el = document.getElementById('progress-counter');
  if (el) {
    el.innerHTML = `<span class="pc-num">${reviewed}</span> / ${total} reviewed`;
  }
}

// ── Toggle accordion ────────────────────────────────────────────────────────────
function toggleCard(id) {
  const card = document.getElementById('card-' + id);
  card.classList.toggle('expanded');
}

function jumpTo(id) {
  const card = document.getElementById('card-' + id);
  if (!card) return;
  if (!card.classList.contains('expanded')) card.classList.add('expanded');
  card.scrollIntoView({behavior: 'smooth', block: 'start'});
}

// ── Collapse / expand all ───────────────────────────────────────────────────────
function collapseAll() {
  document.querySelectorAll('.card.expanded').forEach(c => c.classList.remove('expanded'));
}
function expandAll() {
  document.querySelectorAll('.card:not(.expanded)').forEach(c => c.classList.add('expanded'));
}

// ── Filter ──────────────────────────────────────────────────────────────────────
let activeFilter = 'all';
function setFilter(f) {
  activeFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.filter === f);
  });
  document.querySelectorAll('.card').forEach(card => {
    const cat = card.dataset.category;
    const corpus = card.dataset.corpus;
    let show = true;
    if (f === 'all') show = true;
    else if (f === 'es') show = corpus === 'ES';
    else if (f === 'wb') show = corpus === 'WB';
    else if (f === 'protected') show = cat === 'protected';
    else if (f === 'concern') show = cat === 'concern';
    else if (f === 'strong') show = cat === 'strong';
    else if (f === 'moderate') show = cat === 'moderate';
    else if (f === 'surface') show = cat === 'surface';
    else if (f === 'wb_flag') show = cat === 'wb_flag';
    else if (f === 'wb_clear') show = cat === 'wb_clear';
    card.classList.toggle('hidden', !show);
  });
}

// ── Export/import ───────────────────────────────────────────────────────────────
function exportState() {
  const state = {
    _meta: {
      exported_at: new Date().toISOString(),
      tool: 'synthetic_corpus_review_2026-05-12',
      n_students: CORPUS.length,
    },
  };
  CORPUS.forEach(s => {
    const p = localStorage.getItem(lsKey('pattern', s.id));
    const n = localStorage.getItem(lsKey('notes', s.id));
    const r = localStorage.getItem(lsKey('reviewed', s.id));
    const e = localStorage.getItem(lsKey('expected', s.id));
    if (p !== null) state['pattern_' + s.id] = p;
    if (n !== null) state['notes_' + s.id] = n;
    if (r !== null) state['reviewed_' + s.id] = r;
    if (e !== null) state['expected_' + s.id] = e;
  });
  const blob = new Blob([JSON.stringify(state, null, 2)], {type: 'application/json'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'corpus_review_state.json';
  a.click();
}

function importState() {
  const ta = document.getElementById('import-textarea');
  try {
    const state = JSON.parse(ta.value);
    Object.entries(state).forEach(([k, v]) => localStorage.setItem('synth_' + k, v));
    location.reload();
  } catch(e) {
    alert('Invalid JSON: ' + e.message);
  }
}

// ── Init ────────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  renderAll();
  setFilter('all');
});
"""


def build_html(students: list) -> str:
    corpus_js = make_student_js(students)

    filter_buttons = [
        ("all", "All 46"),
        ("es", "ES only (32)"),
        ("wb", "WB only (14)"),
        ("protected", "Protected"),
        ("concern", "Concern"),
        ("strong", "Strong"),
        ("moderate", "Moderate"),
        ("surface", "Surface"),
        ("wb_flag", "WB: Flag"),
        ("wb_clear", "WB: Clear"),
    ]
    filter_btns_html = " ".join(
        f'<button class="filter-btn" data-filter="{k}" onclick="setFilter(\'{k}\')">{label}</button>'
        for k, label in filter_buttons
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Synthetic Corpus Review — 46 Students</title>
  <style>
{CSS}
  </style>
</head>
<body>

<div class="site-header">
  <div>
    <h1>Synthetic Corpus Review</h1>
    <div class="meta">46 students · ES corpus (S001–S032) + WB corpus (WB01–WB14) · 2026-05-12</div>
  </div>
  <div class="header-btns">
    <span class="progress-counter" id="progress-counter">0 / 46 reviewed</span>
    <button class="btn btn-collapse" onclick="collapseAll()">Collapse all</button>
    <button class="btn btn-collapse" onclick="expandAll()">Expand all</button>
    <button class="btn" onclick="exportState()" title="Exports all your edits: pattern descriptions, notes, reviewed flags, verdict overrides">Export all state ↓</button>
  </div>
</div>

<nav class="sticky-nav">
  <div class="nav-row">
    <span class="nav-label">ES:</span>
    <span id="nav-es" style="display:contents"></span>
  </div>
  <div class="nav-row">
    <span class="nav-label">WB:</span>
    <span id="nav-wb" style="display:contents"></span>
  </div>
</nav>

<div class="filter-bar">
  <span class="filter-label">Filter:</span>
  {filter_btns_html}
</div>

<div class="corpus-section-header">ES Corpus — 32 students — Ethnic studies engagement patterns</div>
<div id="es-cards"></div>

<div class="corpus-section-header">WB Corpus — 14 students — Wellbeing concern detection</div>
<div id="wb-cards"></div>

<script>
const CORPUS = {corpus_js};
{JS}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    expected_map = load_expected_from_run()
    es_students = load_es_corpus(expected_map)
    wb_students = load_wb_corpus()
    all_students = es_students + wb_students

    print(f"ES students: {len(es_students)}")
    print(f"WB students: {len(wb_students)}")
    print(f"Total: {len(all_students)}")

    html_content = build_html(all_students)
    OUT.write_text(html_content, encoding="utf-8")
    print(f"\nWritten: {OUT}")
    print(f"File size: {OUT.stat().st_size:,} bytes")
