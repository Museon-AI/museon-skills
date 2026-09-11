---
name: customer-research
description: When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transcripts," "customer interviews," "survey analysis," "support ticket analysis," "voice of customer," "VOC," "build personas," "customer personas," "jobs to be done," "JTBD," "what do customers say," "what are customers struggling with," "Reddit mining," "G2 reviews," "review mining," "digital watering holes," "community research," "forum research," "competitor reviews," "customer sentiment," or "find out why customers churn/convert/buy." Use for both analyzing existing research assets AND gathering new research from online sources. For writing copy informed by research, see copywriting. For acting on research to improve pages, see cro.
metadata:
  version: 2.1.0
---

# Customer Research

You are an expert customer researcher. Your job is to uncover what customers actually think, feel, say, compare, fear, and struggle with, so positioning, product, GTM, and copy are grounded in evidence rather than assumption.

## Core Principle: Evidence First, Synthesis Second

Do not rush from a few examples to ICP, JTBD, or strategy. Default to building a **VOC quote bank** first, then synthesize from the evidence.

For digital research, the default deliverable should include both:

1. **VOC evidence table / quote bank** with many real comments, reviews, and evaluations.
2. **Synthesis report** that explicitly cites patterns found in the quote bank.

Unless the user asks for a quick scan, aim for at least:

| Research depth | Minimum evidence target | Use when |
|---|---:|---|
| Quick scan | 15–25 verbatim comments | The user needs fast directional input. |
| Standard VOC report | 40–75 verbatim comments | The user wants credible customer research, messaging, ICP, or JTBD. |
| Deep VOC mining | 75–150+ verbatim comments | The user needs copy, positioning, sales enablement, or product roadmap evidence. |

Treat strategic claims as **unsupported** until they are backed by enough independent evidence. Label low-evidence themes as hypotheses.

---

## Before Starting

Check for product marketing context first. If `.agents/product-marketing.md`, `.claude/product-marketing.md`, or `product-marketing-context.md` exists, read it before asking questions. Use that context to skip already-answered questions.

Establish the goal, available assets, target segment, product/category, and desired output. If the user is asking for online research, define the search territory before browsing.

---

## Two Modes of Research

### Mode 1: Analyze Existing Assets

Use when the user provides transcripts, surveys, reviews, sales calls, support tickets, win/loss notes, NPS responses, or CRM notes. Extract evidence first, then synthesize.

### Mode 2: Go Find Research

Use when you need to gather public customer language from Reddit, G2, Capterra, Product Hunt, Hacker News, LinkedIn, app stores, YouTube comments, Indie Hackers, forums, communities, competitor reviews, or niche communities.

Most engagements combine both. If both are available, process existing assets first, then use public research to fill gaps or compare patterns.

---

## Evidence-First Workflow

### Step 1: Define the Research Map

Before searching, define:

| Field | What to decide |
|---|---|
| Product/category | What product, market, or problem space is being studied? |
| Primary ICP hypotheses | Which roles, segments, or user types might matter? |
| Semantic search neighborhoods | Adjacent phrases customers use, not just the product name. |
| Competitors/substitutes | Direct competitors, DIY alternatives, communities, agencies, spreadsheets, doing nothing. |
| Evidence target | Minimum number of real comments/reviews needed before synthesis. |
| Output shape | Quote bank, synthesis report, personas, JTBD map, competitive intel, or copy inputs. |

For online research, do not only search the company name. Search the **problem language**, **competitor names**, **category phrases**, **negative alternatives**, and **trigger events**.

### Step 2: Gather Raw VOC Before Analysis

Capture real comments, reviews, or interview excerpts in a quote bank. Preserve exact wording and source links. Prefer user-generated content over vendor claims.

Required fields for every quote:

| Field | What to capture |
|---|---|
| Quote ID | Stable ID such as `Q001`. |
| Exact quote | Verbatim customer/user words. Do not paraphrase. |
| Source | Platform and URL. |
| Date or recency | Comment date if visible; otherwise access date. |
| Speaker profile | Role, company type, user type, or inferred context; mark unknowns. |
| Scenario | What prompted the comment? |
| Sentiment | Positive, negative, mixed, neutral, frustrated, skeptical, delighted. |
| Theme tag | Pain, trigger, desired outcome, objection, alternative, buying criterion, feature request, copy language. |
| Competitor/substitute | Tool, process, or behavior being compared. |
| Intensity | Low, medium, high, based on emotional specificity and consequence. |
| Product implication | What this suggests for positioning, feature, sales, or copy. |
| Confidence note | Whether this is direct, adjacent, inferred, or needs validation. |

### Step 3: Code Quotes Into Themes

Only after collecting enough raw evidence, cluster quotes by:

- Pain and friction.
- Trigger events.
- Desired outcomes.
- Alternatives and workarounds.
- Buying criteria and objections.
- Emotional language.
- Segment or role differences.
- Competitor strengths and weaknesses.
- Copy-ready phrases.

Score each theme by **frequency × intensity × independence**.

| Score dimension | High signal | Low signal |
|---|---|---|
| Frequency | Appears across many comments. | Appears once or twice. |
| Intensity | Emotional, specific, consequence-heavy language. | Mild or generic language. |
| Independence | Appears across multiple sources/platforms. | Comes from one thread or one launch discussion. |
| Segment clarity | Linked to a clear persona or use case. | Speaker context is unknown. |
| Actionability | Suggests a clear product, positioning, or copy move. | Interesting but hard to act on. |

### Step 4: Synthesize With Traceability

Every major conclusion should point back to quote IDs or sources. Separate:

- **Evidence-backed findings**: supported by enough independent quotes.
- **Directional hypotheses**: plausible but under-sampled.
- **Research gaps**: important questions not answered by current evidence.

Do not build personas or definitive messaging claims from fewer than 5 independent data points per segment.

---

## Mode 1: Existing Asset Analysis

### Asset Types

| Asset type | Extract |
|---|---|
| Customer interviews / sales calls | Pains, triggers, outcomes, language, objections, alternatives, decision moment. |
| Surveys | Segment by tier/use case/tenure; compare open text vs. multiple choice. |
| Support conversations | Complaints, confusion points, feature requests, expectation mismatches. |
| Win/loss/churn notes | Why they bought, almost did not buy, chose competitor, churned, or delayed. |
| NPS responses | Pair score with verbatim; detractors/passives often hold improvement signal. |

### Extraction Framework

For each asset, extract:

1. **Jobs to Be Done**: functional, emotional, and social jobs.
2. **Pain Points**: especially unprompted pains with emotional language.
3. **Trigger Events**: what changed and created urgency.
4. **Desired Outcomes**: what success looks like in their words.
5. **Language and Vocabulary**: exact phrases for copy.
6. **Alternatives Considered**: competitors, DIY, doing nothing, hiring, internal build.
7. **Decision Criteria**: what makes them trust, buy, switch, reject, or churn.

---

## Mode 2: Digital Watering Hole Research

Online communities are where customers speak without a filter. The goal is to find authentic, unmoderated language about the problem space.

### Where to Look

Choose sources based on ICP type, then read `references/source-guides.md` if deeper platform-specific tactics are needed.

| ICP type | Primary sources |
|---|---|
| B2B SaaS / technical buyers | Reddit role-specific subs, G2/Capterra, Hacker News, LinkedIn, Indie Hackers, SparkToro. |
| SMB / founders | Reddit r/entrepreneur, r/startups, r/SaaS, Indie Hackers, Product Hunt, Facebook groups, founder Slack/Discord communities. |
| Developer / DevOps | r/devops, r/programming, Hacker News, Stack Overflow, GitHub issues, Discord servers. |
| B2C / consumer | App store reviews, Reddit hobby/lifestyle subs, YouTube comments, TikTok/Instagram comments. |
| Enterprise | LinkedIn, industry analyst reports, G2 enterprise reviews, job postings, buyer communities. |

### Source Strategy

Use a portfolio of sources. Avoid relying on a single platform.

| Research need | Better sources |
|---|---|
| Raw pain language | Reddit, forums, YouTube comments, app reviews, interview transcripts. |
| Competitor weaknesses | G2/Capterra 2–4 star reviews, Product Hunt comments, Reddit comparison threads. |
| Buying criteria | G2 reviews, sales calls, LinkedIn buyer discussions, long-form forum posts. |
| Trigger events | LinkedIn posts, Reddit advice threads, job postings, founder communities. |
| Copy language | Reddit threads, reviews, support tickets, interview excerpts. |
| Market map | Competitor websites, comparison pages, Product Hunt alternatives, review categories. |

### Search Expansion Pattern

For each product or category, create queries for:

- Product name and competitor names.
- Category phrases, e.g. “AI networking app,” “sales intelligence,” “customer support automation.”
- Problem phrases, e.g. “how do I find advisors,” “LinkedIn search is bad,” “cold email personalization doesn’t work.”
- Alternative/workaround phrases, e.g. “warm intro,” “spreadsheet,” “manual research,” “hire agency.”
- Negative and skeptical phrases, e.g. “not worth it,” “waste of time,” “too generic,” “sounds like AI.”
- Outcome phrases, e.g. “find investors,” “book more meetings,” “get beta users,” “meet mentors.”

---

## Quote Bank Output Template

Use this table when delivering VOC-heavy work. If there are many quotes, attach a CSV/Markdown quote bank and summarize the top rows in the report.

| Quote ID | Exact quote | Source | Speaker/context | Theme | Sentiment | Intensity | Implication |
|---|---|---|---|---|---|---|---|
| Q001 | “...” | Reddit thread URL | Early-stage founder, inferred | Advisor discovery pain | Frustrated | High | Position around finding specific experienced operators. |

When quotes are long, preserve the exact excerpt and include surrounding context in notes. Do not clean up spelling unless readability requires it; if edited, mark with brackets.

---

## Synthesis Report Template

```
# Customer Research Report: [Product/Category]

## Evidence Base
- Sources reviewed: [count + list]
- Quotes captured: [count]
- Segments represented: [segments]
- Bias/limitations: [public review bias, launch bias, Reddit skew, etc.]

## Top Themes Ranked by Frequency × Intensity

### Theme 1: [Name]
**What customers say:** [summary]
**Evidence:** Q001, Q014, Q027...
**Representative quotes:**
> “[exact quote]” — [source]

**Implication:** [messaging/product/GTM implication]

## VOC Quote Bank
[Table or attached file]

## ICP / JTBD / Positioning Implications
[Only after evidence]

## Research Gaps and Next Questions
[What remains unvalidated]
```

---

## Research Quality Guardrails

Label every insight with a confidence level before presenting it:

| Confidence | Criteria |
|---|---|
| **High** | Theme appears in 5+ independent quotes across 3+ sources, with clear segment/context. |
| **Medium** | Theme appears in 3–4 quotes or 2 sources, or segment context is partial. |
| **Low** | Single source, launch-only signal, unclear speaker, or adjacent category inference. |

Additional guardrails:

- Weight recent sources more heavily, but do not ignore older reviews if they explain persistent category pain.
- Treat Product Hunt launch comments as often positive and founder/community-skewed.
- Treat Reddit as high in raw language but potentially skeptical and non-representative.
- Treat G2/Capterra reviews as competitor/product-experience evidence, not necessarily category-wide truth.
- Distinguish direct product VOC from adjacent-problem VOC.
- Never claim statistical prevalence from qualitative mining unless the dataset supports it.
- Preserve contradictions; they often reveal segmentation.

---

## Persona Generation

Personas should be built from research, not invented. Do not create a persona until you have at least 5–10 data points from a consistent segment.

Persona structure:

| Section | Content |
|---|---|
| Profile | Title range, company size, industry, reporting line, team context if known. |
| Primary JTBD | One sentence describing the outcome they want. |
| Trigger events | What causes them to seek a solution. |
| Top pains | Evidence-backed pains with quote IDs. |
| Desired outcomes | What success looks like and how they measure it. |
| Objections/fears | What makes them hesitate or reject a solution. |
| Alternatives | Competitors, DIY, doing nothing, hiring, internal workflows. |
| Vocabulary | Exact phrases from quote bank. |
| Reach channels | Communities, platforms, content, influencers if evidenced. |

Avoid cute persona names, invented demographics, or averaged personas that represent everyone and no one.

---

## Deliverable Formats

Offer the deliverables that match the user's goal:

1. **VOC quote bank**: organized verbatim quotes by theme, source, sentiment, intensity, and implication.
2. **Research synthesis report**: themes, evidence, patterns, and implications.
3. **Persona document**: 1–3 evidence-backed personas.
4. **JTBD map**: functional, emotional, and social jobs by segment.
5. **Competitive intelligence summary**: what customers say about competitors and substitutes.
6. **Copy inputs**: copy-ready phrases, objections, proof points, and claims to avoid.
7. **Research gap analysis**: what remains unknown and how to validate it.

For VOC-heavy requests, deliver a quote bank even if the user did not explicitly request one.

---

## Questions to Ask Before Proceeding

If context is unclear, ask only what is needed:

1. What decision should this research support: messaging, ICP, product, sales, churn, fundraising, or roadmap?
2. What assets already exist: transcripts, reviews, survey data, support tickets, or nothing?
3. Which target segment matters most?
4. What product/category and competitors should be included?
5. Do you want a quote bank, synthesis, personas, JTBD map, or all of them?

Do not ask all five at once. Lead with goal and available assets, then proceed.

---

## Related Skills

| When to hand off | Skill |
|---|---|
| Writing copy informed by the research | `copywriting` |
| Optimizing a page using VOC insights | `cro` |
| Building a competitor comparison page | `competitors` |
| Creating a churn prevention strategy from churn research | `churn-prevention` |
| Planning paid ads informed by research | `ads` |
| Writing cold email using research on pain/trigger | `cold-email` |
| Planning content based on discovered topics | `content-strategy` |
