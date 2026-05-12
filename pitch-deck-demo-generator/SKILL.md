---
name: pitch-deck-demo-generator
description: "Generate Pitch Deck JSON data for MuseOn's TikTok Slideshow Campaign from a customer information table + creative research report. Use when: the C-stage of MuseOn's client service pipeline is triggered, converting B-stage research outputs into a structured JSON that the frontend renders into a client-facing Pitch Deck demo page."
---

# Pitch Deck Demo Generator

Generate a complete Pitch Deck JSON for MuseOn's TikTok Slideshow Campaign frontend. This skill is the **C-stage sub-module** in MuseOn's end-to-end Agent pipeline: it takes the two outputs from A→B stages and produces a single JSON object that the frontend renders directly.

## When to Use

Trigger this skill when:
- The A→B pipeline is complete and you have both a **customer information table (JSON)** and a **creative research report (Markdown)**
- You need to produce a Pitch Deck JSON for frontend rendering (not a Markdown deck — for Markdown decks use `museon-deck-generator`)

## Required Inputs

1. **Customer information table** (JSON) — fields used by this skill: `product_name`, `one_line_positioning`, `audience_segments`, `core_selling_points`, `core_features`, `primary_goal`, `strategy_mode`, `overseas_social_experience`
2. **Creative research report** (Markdown) — 5 Parts: Product Understanding, TikTok Reference Pool, 5 Content Directions (3.1→3.5), Testing Mechanism, Package Recommendation

If either input is missing, ask the user before proceeding.

## Generation Workflow

Read `references/prompt.md` in full — it contains the complete system prompt with:
- Role definition and input/output format (`[REASONING]` + `[OUTPUT_JSON]`)
- 4-phase reasoning sequence (Phase 1→4) with all field specifications
- JSON Schema the output must conform to
- Self-check checklist (8 items)

### Phase overview

| Phase | What it produces | Key fields |
|---|---|---|
| 1 | Base fields | `client_name`, `product_category`, `total_views`, `capability_list[]` |
| 2 | Part 2 reasoning (deck soul) | `use_context`, `category_modifier`, `anxiety_keywords`, `emotion_list[]`, `audience_list`, `anxiety_type`, `user_save_motivation`, `universal_pain_quote` |
| 3 | 5 path cards + detail pages | Per path: `path_audience_label`, `path_hook_quote`, `path_description`, `path_test_hooks[]`, `path_market_ref_comment`, `path_museon_version_comment` + B-report fields |
| 4 | Package recommendation | `recommended_badge`, `scenario_a`, `scenario_b`, `our_recommendation` |

### Critical constraints

- `paths[]` order locked to research report 3.1→3.5 — never reorder
- `emotion_list[]` / `capability_list[]` / `paths[]` must each have exactly 5 items
- `recommended_badge` only outputs `"package_a"` or `"package_b"`
- `path_museon_version_image` always outputs `null`
- Language rules: deck body in Chinese; `path_audience_label` / `path_hook_quote` / `path_description` / `path_capability_label` / `path_test_hooks[]` in English

## Reference Files

| File | When to read | Content |
|---|---|---|
| `references/prompt.md` | **Always** — read in full before generating | Complete system prompt with role, inputs, output format, 4-phase reasoning specs, JSON Schema, output example, self-check checklist |
| `references/reasoning-spec.md` | When debugging a specific C-field or improving output quality | Detailed reasoning logic for all 17 C-fields: purpose, inputs, output structure, reasoning steps, good/bad examples, Manus reference fills |
| `references/field-map.md` | When you need to understand where a field appears in the deck or trace field dependencies | Full field inventory across Part 1-5, field type taxonomy (A/B-info/B-report/C), customer info → deck field mapping, C-field index |

## Quality Rules

- Do not fabricate information not present in the inputs
- Write style: professional, restrained, no marketing tone
- After generating, self-check all 8 items in the checklist (end of `references/prompt.md`) before outputting
- `universal_pain_quote` must follow the fixed pattern: `{pain},但 {client_name} 可以直接帮你 {verb}。`
- English fields must contain zero Chinese characters; Chinese fields must contain zero English (except `path_views`/`path_likes`)
