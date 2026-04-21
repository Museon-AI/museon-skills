---
name: slideshow-analyzer
description: "TikTok/Instagram slideshow analysis. Analyze any slideshow to extract viral hooks, memes, visual strategy, narrative structure, text CTA hooks, and reusable blueprints (soul vs skin). Covers both humor-driven (meme) and non-humor (emotional, aspirational, aesthetic) slideshows. Trigger when user mentions analyzing slideshow, deconstructing image-text content, or extracting slideshow patterns."
---

# Slideshow Analyzer

Analyze any slideshow: what do you see → how is it structured → what is the text CTA hook → why would someone share it → what's soul, what's skin.

All accumulated knowledge lives in `references/`:
- **`analysis-playbook.md`** — Four archetypes, trigger types, mechanisms (humor + non-humor), structure rules, ad strategies, soul vs skin framework
- **`cases.md`** — Every analyzed case with full breakdown and reusable blueprint

**Read `analysis-playbook.md` and `cases.md` before analyzing.**

---

## Analysis Flow

Six steps. Do them in order. Steps 4 and 6 are the most important.

### Step 1: Look — What's in each slide?

First, decide whether this slideshow has text (see Text Layer Analysis in playbook):

| Text Presence | What to do next |
|---------------|----------------|
| **Has text** | Record the **text rendering spec** that is shared across all slides — font family, weight, color, size ratio, alignment, effects, and the **position rule** (e.g., fixed corner, avoid-subject). This spec is Soul. |
| **No text** | Skip text analysis entirely, focus on visual narrative |

Do NOT spend time classifying whether text was "baked-in" by the image generator or added as an "overlay" in the publishing tool. In an AI-generation workflow text is always rendered in the image prompt, so the distinction is irrelevant for both analysis and reproduction.

Then for each slide, capture:

| Field | What to note |
|-------|-------------|
| Content | Subject, setting, action, props |
| Characters | How many? What's their relationship? (accuser→accused, before→after, etc.) |
| Text | Exact wording, and the specific position on this slide (the shared rendering spec is recorded once for the whole set) |
| Text format | Caption Bar / Impact Overlay / Minimal serif / Bold statement / No text (see Text Style Recognition in playbook) |
| Linguistic pattern | What grammatical/rhetorical template? (see Linguistic Patterns in playbook) |
| Visual quality | Polished or raw? Phone snapshot or produced? Illustrated or photographic? |
| Role | Hook / build / spike / soft-ad / CTA / mood-setter |

Then across all slides:
- **Do characters span multiple slides?** Are different characters in the same scene separated by the crop?
- **Is there a visual contrast pattern?** (e.g., split-screen good/bad, before/after, light/dark)

### Step 2: Connect — How do the slides relate?

Two dimensions to identify:

**Visual Continuity** (spatial relationship):

| Pattern | What it means | Swipe feels like... |
|---------|--------------|-------------------|
| Zoom | Each slide is a tighter crop | Getting closer |
| Pan (single-image split) | One wide image sliced into frames | Panning a camera |
| Progression | Same object changes state | Advancing time |
| Independent | No spatial link | Turning a page |

When you detect a **single-image split** (strongest form), ask three questions:
1. **What does the crop hide?** What's pushed off-screen in Slide 0?
2. **What does the swipe reveal?** What new thing appears in the next slide?
3. **Does the crop separate characters?** If yes, the relationship between them becomes the narrative engine.

**Information Format** (content logic):

| Format | Each slide is... | Can you shuffle the order? |
|--------|------------------|---------------------------|
| List | One item in a set | Yes |
| Step-by-step | One step in a process | No |
| Story | One plot beat | No |
| Comparison | One side of A-vs-B | Partially |
| Zoom progression | A tighter crop of the same subject | No |
| Showcase | One angle of the same subject | Yes |
| Q&A | One question-answer pair | Yes between pairs |
| Parallel Contrast | Two states per slide (good/bad, before/after) | No |
| Mood Board / Grid | Multi-image collage per slide | Yes between slides |
| Atmospheric Progression | One mood scene per slide, building an arc | No |

(See Slide Structure in playbook for full definitions and examples)

### Step 3: Story — What's the narrative arc?

**For humor slideshows** (Character-Action, Tension-Punchline):

Map the sequence: `[Hook] → [Build...] → [Spike] → [Soft-ad?]`

Identify:
- **Hook type**: Grid preview / bold claim / question / pattern interrupt / conversational opener
- **Where's the spike?** The single strongest moment someone would screenshot or share
- **Is there a soft-ad?** How is it justified in the story?
- **Linguistic pattern**: What text template drives the humor? Is this pattern reusable with different content?

**For non-humor slideshows** (Emotional Arc, Mood Showcase):

Map the sequence: `[Opener] → [Deepening...] → [Turn/Peak] → [Resolution/CTA?]`

Identify:
- **Opener type**: Emotional hook / aesthetic hook / relatable pain point / curiosity
- **Where's the emotional peak?** The slide that hits hardest or is most saveable
- **Is there a turn?** (pain→hope, before→after, struggle→resolution)
- **Is there a product integration?** How naturally does it fit?

### Step 4: Text CTA Hook & Sharing Mechanism (MOST IMPORTANT)

Text content and the first slide's CTA hook are critical drivers for views and shares. Answer at three levels:

1. **What is the Text CTA Hook?**
   - Analyze the text on Slide 0. How does it hook the viewer? (e.g., curiosity gap, relatable statement, bold claim, direct command like "come closer").
   - How does the text content across the slides drive the narrative and encourage swiping/sharing?

2. **What trigger drives shares?**
   - Identify the **trigger type** (Rational, Social, Aspirational, Emotional/Instinct, Behavioral).
   - Pick the **archetype** (Character-Action, Tension-Punchline, Emotional Arc, Mood Showcase).

3. **Why would someone send this to a friend?**
   - What emotion does the viewer feel?
   - What does sharing say about the sharer?
   - What unspoken truth does this express — the thing everyone feels but nobody says?

Match a known mechanism in `analysis-playbook.md`. If none fits, define a new one.

**Humor mechanisms**: Proxy Expression, Forbidden Release, Absurd Intrusion, Escalating Doom Spiral, Parasocial Bait-and-Switch, Dignity Mismatch
**Non-humor mechanisms**: Emotional Mirror, Aspirational Pull, Identity Signal, Transformation Proof, Utility Bookmark

```
Text CTA Hook: [Analysis of Slide 0 text and overall text strategy]
Trigger type(s): [from Step 4.2]
Archetype: [from Step 4.2]

Primary mechanism: [name]
- Viewer emotion: [specific]
- Sharing motive: [what sharing says about the sharer]
- Unspoken truth: [the thing everyone feels but nobody says]

Secondary mechanism(s): [name(s)]
- Role: [how it supports the primary]
```

### Step 5: Commercial Layer — How does the ad work?

Identify: ad location (slide # + visual region), insertion strategy (which type from Ad Insertion Strategies in playbook), narrative justification, subtlety (1–5, best ads = 1–3), and product-mechanism fit.

**Humor-native strategies**: Ad-as-punchline, Ad-as-resolution, Ad-as-reward, Ad-as-background, Ad-as-final-slide

**Non-humor strategies**: Ad-as-cause, Ad-as-lifestyle-element, Ad-as-list-item, Ad-as-curation-pick, Ad-as-step

If no ad: where COULD one be inserted, and which strategy fits this archetype?

### Step 6: Extract Soul vs Skin (CRITICAL FOR DERIVATION)

This is the most important output. For every element, answer: **"If I remove or change this, does the slideshow still trigger the same mechanism for the same reason?"** If no → **soul (LOCKED)**. If yes → **skin (OPEN)**.

Must classify these elements:

| Element | Soul or Skin? | This case's value |
|---------|:---:|---|
| **Text CTA Hook Strategy** (The psychological trap on Slide 0) | ? | |
| **Trigger type** (The psychological reason people share) | ? | |
| **Primary mechanism** (How the trigger is delivered) | ? | |
| **Archetype** (Determines rules, checklist, and vehicle norms) | ? | |
| **Information Format** (The content logic between slides, e.g., Zoom, List) | ? | |
| **Visual Continuity strength** (The spatial relationship between slides) | ? | |
| **Linguistic pattern** (The text template that carries the engagement) | ? | |
| **Text presence** (Has text / no text) | ? | |
| **Text rendering spec** (Cross-slide consistency of font family, weight, color rule) | ? | |
| **Text position rule** (The rule deciding where text lands, e.g., fixed slot) | ? | |
| **Ad insertion strategy** (How the product connects to the narrative) | ? | |
| **Vehicle** (The specific character/subject carrying the mechanism) | ? | |
| **Setting/Environment** (Where the scene takes place, must support the mechanism) | ? | |
| **Specific text content** (What fills the linguistic pattern slots) | ? | |
| **Cultural reference** (What cultural context is used) | ? | |
| **Specific font pick** (Within the chosen family) | ? | |
| **Specific text position** (On each slide, within the rule) | ? | |
| **Visual style** (Photo quality, color palette, era) | ? | |
| **Number of slides** (How many build slides before the spike) | ? | |

**Rule of thumb for text-related rows**: the *shared spec* and the *position rule* are Soul — breaking cross-slide consistency breaks the template. The *specific font pick* within the chosen family and the *specific position* on any single slide (as long as it obeys the rule) are Skin.

Include **transferability**: what products fit this blueprint, what products break it.

**See Case 006 in `cases.md` for a complete worked example.** Follow that format.

---

## Updating This Skill

After each analysis session, append the new case to `references/cases.md` and update `references/analysis-playbook.md` if you discovered a new mechanism, trigger type, tactic, or analysis rule.
