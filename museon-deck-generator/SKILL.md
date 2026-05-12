---
name: museon-deck-generator
description: "Generate a MuseOn-standard TikTok Slideshow Campaign Pitch Deck from client inputs (customer information table, product link, TikTok references, SoulSkin analysis). Use when: producing a client-facing pitch deck for a TikTok slideshow campaign, converting sales intake materials into a structured 5-chapter Markdown deck, or applying MuseOn's testing methodology and package recommendation framework."
---

# MuseOn Deck Generator

Generate a complete TikTok Slideshow Campaign Pitch Deck aligned to MuseOn standards. The output is a single Markdown document ready to send to the client.

## When to Use

Use this skill after the sales intake phase is complete and you have all four required inputs ready. This skill is the **generation step**, not the research step — TikTok references and SoulSkin analyses should already exist.

## Required Inputs

Before generating, confirm you have:

1. **Customer information table** — structured fields from chatbot or sales intake (see `references/prompt.md` §2.1 for field list)
2. **Product link** — client's official website or landing page URL
3. **TikTok Reference list** — 5 verified viral slideshows with URL, keyword, topic, metrics
4. **SoulSkin analysis** — one per reference, containing hook_breakdown, slide_structure, visual_style, content_angle, why_it_worked

If any input is missing, ask the user to provide it before proceeding.

## Generation Workflow

Execute in order:

1. Read all 5 SoulSkin analyses — build a mental model of what each "content container" is good at carrying
2. Read customer info + product link — extract 3-5 core selling points organized by function → user scenario → emotional pain
3. Match directions — pair reference containers with client selling points; ensure 5 directions cover: (a) direct use-case demo, (b) category education / competitive positioning, (c) tool-stack recommendation / scenario packaging
4. Write Chapter 1 (Product Understanding)
5. Write Chapter 2 (TikTok References)
6. Write Chapter 3 (5 Content Directions) — the core of the deck
7. Write Chapters 4-5 (Testing Mechanism + Package Recommendation) — follow MuseOn standard methodology strictly
8. Self-check against the checklist
9. Output final Markdown

## Output Structure

The full prompt with chapter-by-chapter specifications, writing style rules, forbidden patterns, and self-check checklist is in `references/prompt.md`. Read it in full before generating.

Key structural requirements:
- 5 chapters, fixed order, fixed sub-section numbering
- Chapter 3 has 5 directions, each with 8 mandatory modules
- Chapter 4 uses MuseOn's fixed testing framework (thresholds, 30-day rhythm)
- Chapter 5 defaults to recommending Growth Team unless budget signals otherwise
- Title format: `# （v1）[Product Name] TikTok Slideshow Campaign`

## Critical Quality Rules

- Every direction's "创意设计逻辑" must contain a unique, non-obvious insight
- Scripts must be specific enough for a creator to shoot tomorrow
- Never use: 赋能, 打造, 闭环, 抓手, 链路, AI帮你xxx, 一键xxx
- Tables over bullet lists; bullets over paragraphs
- Chinese-English mixed: keep product names, TikTok terms (Hook/CTA/Save rate/Creator), and feature names in English; rest in Chinese
- Numbers must be concrete: "4 个 creator" not "很多 creator"

## Reference

Read `references/prompt.md` for the complete system prompt with all specifications.
