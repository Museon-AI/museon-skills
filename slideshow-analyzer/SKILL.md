---
name: slideshow-analyzer
description: "TikTok/Instagram slideshow analysis. Analyze any slideshow to extract viral hooks, memes, visual strategy, narrative structure, text CTA hooks, and reusable blueprints (soul vs skin). Covers both humor-driven (meme) and non-humor (emotional, aspirational, aesthetic) slideshows. Trigger when user mentions analyzing slideshow, deconstructing image-text content, or extracting slideshow patterns."
---

# Slideshow Analyzer

Analyze any slideshow: what do you see → how is it structured → what is the text CTA hook → why would someone share it → what's soul, what's skin.

Worked examples live in `references/cases.md`. **Read it before analyzing** — it shows the exact output format expected (use Case 006 as the model).

---

## Deliverable

**The output of running this skill is a single Markdown file**, not chat output.

- **File path**: `<source-name>.analysis.md` in the working directory (e.g., `delust-saddboy.analysis.md`). If the user provided a name, use it; otherwise derive from the source URL/filename.
- **The file MUST contain every section in the report skeleton below, in order.** Skipping or merging sections = broken deliverable.
- Save the file at the end of Step 7. Do not declare the analysis complete until the file exists on disk.

### Report skeleton (the file you produce must look exactly like this)

```markdown
# Slideshow Analysis: <source name>

Source: <URL or file path>
Analyzed: <YYYY-MM-DD>

## 1. Look
### 1.0 Slide 0 Hook Deconstruction
<text hook / visual hook / stop-scroll mechanism>

### 1.1 Text Rendering Spec (set-level)
<spec block, or "N/A — no text">

### 1.2 Per-Slide Capture
<table: one row per slide>

### 1.3 Set-Level Observations
<cross-slide characters, visual contrast pattern>

## 2. Connect
### 2.1 Visual Continuity
### 2.2 Information Format

## 3. Story
### 3.1 Sequence Map
### 3.2 Spike / Peak / Turn

## 4. Hook & Sharing Mechanism
### 4.1 Hook (carried forward from 1.0, do not collapse)
### 4.2 Trigger & Archetype
### 4.3 Primary & Secondary Mechanism
### 4.4 Why People Share (emotion / motive / unspoken truth)

## 5. Commercial Layer
### 5.1 Per-Slide Ad Pre-Scan
### 5.2 Insertion Strategy & Analysis  (or "No Ad — Best Insertion Point" if no ad)

## 6. Soul vs Skin
### 6.1 Soul vs Skin Table
### 6.2 Override Log
### 6.3 Transferability
### 6.4 Derivation Rule

## 7. Notes
<anything that didn't fit above: open questions, unusual mechanics, things to double-check>
```

---

## Analysis Flow

Seven steps. Do them in order. Steps 4 and 6 are the most important. Steps 1–6 each fill one section of the report; Step 7 saves the file.

> **Output discipline (applies to every step)**: Each step's output goes directly into the corresponding report section listed in the skeleton. **Every field in every section is mandatory.** If a field doesn't apply, write `N/A — <one-line reason>` rather than skipping it. Skipping a field counts as analysis failure — go back and fill it.

### Step 1: Look — What's in each slide?

#### 1.0 Hook Deconstruction (Slide 0 only — DO THIS FIRST)

Slide 0 is the entire reason the rest of the deck gets watched. Analyze it as a separate artifact before touching the other slides. **Three layers, all mandatory:**

| Layer | What to extract | How to identify |
|-------|----------------|-----------------|
| **Text hook** | The exact wording on Slide 0 + which hook type it uses (Curiosity Gap / Direct Command / Relatable Accusation / Bold Claim / Rhetorical Question / Pattern Interrupt / None) | Read the literal copy. If no text, write `N/A — image-only hook`. |
| **Visual hook** | The single visual element that stops the scroll (e.g., "sad-boy face filling frame", "tiny hamster in cubicle", "split-screen glow vs acne") | Cover the text — what's still doing the work? |
| **Stop-scroll mechanism** | Why the text + visual COMBINATION makes someone pause. Be specific about the interaction, not just "it's interesting". | If you can't articulate why these two specifically work together, the hook isn't actually working — say so. |

**Fills report section 1.0**:

```
Slide 0 Hook
├─ Text hook:   "[exact copy]" — [hook type]
├─ Visual hook: [the one element doing the visual work]
└─ Stop-scroll: [why text × visual combination earns the pause]
```

#### 1.1 Text rendering spec (set-level, only if slideshow has text)

| Text Presence | What to do next |
|---------------|----------------|
| **Has text** | Record the **text rendering spec** that is shared across all slides — font family, weight, color, size ratio, alignment, effects, and the **position rule** (e.g., fixed corner, avoid-subject). This spec is Soul. |
| **No text** | Skip text spec; the narrative is carried entirely by imagery. |

Do NOT spend time classifying whether text was "baked-in" by the image generator or added as an "overlay" in the publishing tool. In an AI-generation workflow text is always rendered in the image prompt, so the distinction is irrelevant for both analysis and reproduction.

#### 1.2 Per-slide capture (every slide, including Slide 0)

For each slide, capture:

| Field | What to note |
|-------|-------------|
| Content | Subject, setting, action, props |
| Characters | How many? What's their relationship? (accuser→accused, before→after, etc.) |
| Text | Exact wording, and the specific position on this slide (the shared rendering spec is recorded once for the whole set) |
| Text format | Caption Bar (bold sans on solid bar) / Impact Overlay (ALL CAPS, white + black outline) / Minimal serif (thin, lots of whitespace) / Bold statement (large bold sans, 1–3 words) / No text |
| Linguistic pattern | The grammatical/rhetorical template (e.g., "X not X-ing", "She said... but...", "POV: ...", single-word label, imperative parasocial) |
| Visual quality | Polished or raw? Phone snapshot or produced? Illustrated or photographic? |
| Role | Hook / build / spike / soft-ad / CTA / mood-setter |

Then across all slides:
- **Do characters span multiple slides?** Are different characters in the same scene separated by the crop?
- **Is there a visual contrast pattern?** (e.g., split-screen good/bad, before/after, light/dark)

**Fills report sections 1.1, 1.2, 1.3**:

```markdown
### 1.1 Text Rendering Spec (set-level)
[Use the spec block from the table above, or "N/A — no text"]

### 1.2 Per-Slide Capture

| # | Content | Characters | Text | Text format | Linguistic pattern | Visual quality | Role |
|---|---------|------------|------|-------------|--------------------|----------------|------|
| 0 | ... | ... | ... | ... | ... | ... | Hook |
| 1 | ... | ... | ... | ... | ... | ... | ... |
| ... | | | | | | | |

### 1.3 Set-Level Observations
- Cross-slide characters: [yes/no — who, and how they relate]
- Visual contrast pattern: [type, or "N/A"]
```

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

**Fills report sections 2.1, 2.2**:

```markdown
### 2.1 Visual Continuity
- Classification: [Strong (zoom/pan) | Medium (shared scene) | Weak (thematic)]
- Evidence:       [the specific cross-slide signal — e.g., "lawyer's arm crosses crop boundary"]

### 2.2 Information Format
- Classification: [one of the 10 formats above]
- Evidence:       [why this format and not a neighbor — e.g., "shuffleable → List, not Story"]
```

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

**Fills report sections 3.1, 3.2**:

```markdown
### 3.1 Sequence Map
[Slide 0: role] → [Slide 1: role] → ... → [Slide N: role]

### 3.2 Spike / Peak / Turn
- Spike / Peak:  Slide [#] — [why this is the strongest moment]
- Turn (if any): [from X → to Y, at slide #]   OR   "N/A — no turn"
- Linguistic pattern carrying the arc: [the template]
```

### Step 4: Text CTA Hook & Sharing Mechanism (MOST IMPORTANT)

Text content and the first slide's CTA hook are critical drivers for views and shares. Answer at three levels:

1. **What is the Text CTA Hook?**
   - Analyze the text on Slide 0. How does it hook the viewer? (e.g., curiosity gap, relatable statement, bold claim, direct command like "come closer").
   - How does the text content across the slides drive the narrative and encourage swiping/sharing?

2. **What trigger drives shares?** Pick from the five types (decision flow — stop at the first "yes"):
   1. Delivering useful information or proving a result? → **Rational**
   2. Building trust through people or identity? → **Social**
   3. Selling a desirable lifestyle, aesthetic, or state-of-being? → **Aspirational**
   4. Provoking curiosity, suspense, or scroll-stopping reflex? → **Instinct**
   5. Making the viewer feel/laugh/recognize themselves? → **Emotional**

   Then pick the **archetype**:
   - **Character-Action** — laugh slide-by-slide
   - **Tension-Punchline** — builds suspense then surprises
   - **Emotional Arc** — makes you feel something
   - **Mood Showcase** — makes you want to save for the aesthetic

3. **Why would someone send this to a friend?**
   - What emotion does the viewer feel?
   - What does sharing say about the sharer?
   - What unspoken truth does this express — the thing everyone feels but nobody says?

Match a known mechanism (one-line definitions below). If none fits, define a new one and note it.

> ⚠️ **Anti-pattern — don't reflexively pick a "positive" mechanism just because the slideshow has an ad.** Many ad-bearing slideshows are built on **negative** mechanisms (Emotional Mirror of pain, Forbidden Release, Doom Spiral, Dignity Mismatch). The ad sits at the END as relief or punchline, but the **Soul is the negative emotion / tension, not the relief**. Misclassifying a "guy spirals into shame, then finds product X" deck as *Transformation Proof / Aspirational Pull* will produce derivations that read as ads instead of relatable content. **Test**: cover the ad slide. If the remaining slides feel negative/tense/uncomfortable, the mechanism is negative — keep it that way.

| Mechanism | The viewer feels | Example |
|---|---|---|
| **Proxy Expression** ("Say it for me") | "Finally someone said it" | Case 004 (cat: "Brain not braining") |
| **Forbidden Release** ("I wish I could do that") | Vicarious satisfaction at a social taboo | Case 001 (hamster middle finger) |
| **Absurd Intrusion** ("That doesn't belong there") | Delight at out-of-place subject | Case 001 (tiny hamster in cubicle) |
| **Escalating Doom Spiral** ("It keeps getting worse") | Dark humor catharsis at compounding bad | Case 004 (descent across slides) |
| **Parasocial Bait-and-Switch** ("Come closer, I have a secret") | Curiosity → "I got played but it was fun" | Case 006 (monkey plush zoom) |
| **Dignity Mismatch** ("Dramatically unimportant") | Amused recognition of mundane elevated to high gravitas | Case 007 (classical painting + TikTok) |
| **Emotional Mirror** ("I feel seen") | Validation — "this is exactly what it's like" | Same person split-screen: top half glowing/happy, bottom half defeated with acne — no text needed |
| **Aspirational Pull** ("I want that life") | Longing + motivation | Cinematic dark shots progressing from lonely bedroom → city skyline → airplane window |
| **Identity Signal** ("This is who I am") | Tribe belonging | Grid collage of niche aesthetic: dark romance novels + fantasy art + couple silhouettes |
| **Transformation Proof** ("Look what happened") | Hope — "if they can, maybe I can" | Pet in shelter cage (before) → same pet on plush bed at home (after) |
| **Utility Bookmark** ("Save this for later") | Practical value worth keeping | Multi-angle workspace/tool grid that's both useful reference and aesthetic |

**Fills report sections 4.1, 4.2, 4.3, 4.4**:

```markdown
### 4.1 Hook (carried forward from 1.0, do not collapse)
- Text hook:   "[exact copy]" — [hook type]
- Visual hook: [the one element doing the visual work]
- Stop-scroll: [why text × visual combination earns the pause]

### 4.2 Trigger & Archetype
- Trigger type(s): [primary], [secondary if any]
- Archetype:       [Character-Action / Tension-Punchline / Emotional Arc / Mood Showcase]

### 4.3 Primary & Secondary Mechanism
- Primary mechanism:    [name]
- Secondary mechanism(s): [name(s)] — [how each supports the primary, or "N/A"]

### 4.4 Why People Share
- Viewer emotion:  [specific]
- Sharing motive:  [what sharing says about the sharer]
- Unspoken truth:  [the thing everyone feels but nobody says]
```

### Step 5: Commercial Layer — How does the ad work?

**Mandatory pre-scan (do this BEFORE deciding "has ad / no ad")**: Walk through every slide and check for any of:

- Product names (any brand-like word, including invented ones)
- Logos / wordmarks (even tiny corner marks)
- Screenshots of apps, websites, or product UI
- URLs / handles / @mentions / "link in bio"
- CTA copy ("try X", "use Y", "I switched to Z", "get [it] here")
- A character visibly *using* a recognizable product
- A "thank god [X] saved me" type line that names anything

**Default to "has ad". Only conclude "no ad" after you have explicitly checked every slide and found none of the above.** If you find an ad, name the slide it appears on.

Then match an insertion strategy:

**Humor-native** (Character-Action / Tension-Punchline):
- **Ad-as-punchline** — product IS the joke's payoff (Case 006)
- **Ad-as-resolution** — product solves the character's problem (Case 007)
- **Ad-as-reward** — after emotional journey, product appears as comfort (Case 004)
- **Ad-as-background** — product appears naturally without being called out
- **Ad-as-final-slide** — narrative slides, then a separate ad slide (Case 001)

**Non-humor** (Emotional Arc / Mood Showcase):
- **Ad-as-cause** — product is why the "good" state exists; before/after implies causation
- **Ad-as-lifestyle-element** — product appears as natural part of the showcased lifestyle
- **Ad-as-list-item** — product is one item in a curated list alongside genuine recs
- **Ad-as-curation-pick** — product featured as part of an aesthetic mood board
- **Ad-as-step** — product embedded as one step in a how-to/process

**Fills report sections 5.1, 5.2**:

```markdown
### 5.1 Per-Slide Ad Pre-Scan

| Slide # | Product names | Logos | Screenshots | URLs/handles | CTA copy | Character using product | "Thank god X" lines | Verdict |
|---------|---------------|-------|-------------|--------------|----------|------------------------|---------------------|---------|
| 0 | none | none | none | none | none | none | none | clean |
| 1 | ... | ... | ... | ... | ... | ... | ... | clean / has-ad |
| ... | | | | | | | | |

Conclusion: [has ad on slide(s) #] OR [no ad — every slide explicitly cleared above]
```

If the slideshow has an ad, also fill:

```markdown
### 5.2 Insertion Strategy & Analysis
- Ad location:             Slide [#], [visual region — e.g., low-density area top-right]
- Insertion strategy:      [strategy name]
- Narrative justification: [one sentence: why this product belongs here in this story]
- Subtlety score:          [1–5, where 1 = invisible, 5 = overt. Best ads land at 1–3]
- Product-mechanism fit:   [why this product is structurally able to fill this slot;
                            what other products would fit; what would break]
- Removable?               [Yes/No. If removing the ad doesn't break the slideshow,
                            the ad is NOT structurally integrated — flag it.]
```

If the slideshow has NO ad, instead fill:

```markdown
### 5.2 No Ad — Best Insertion Point
- Best insertion point: Slide [#], [strategy name]
- Why this slot:        [why this slide is the natural product moment for this archetype]
- Product fit profile:  [what kind of product would naturally fill this slot —
                          category, function, tone — not specific brands]
- Anti-fit:             [what kinds of products would break the mechanism here]
```

**Quality gate**: if you cannot fill *any* row above with conviction, the ad is bolted-on (or the slideshow has no commercial slot to begin with). Say so explicitly in the report rather than fabricating justification.

### Step 6: Extract Soul vs Skin (CRITICAL FOR DERIVATION)

This is the most important output. For every element, answer: **"If I remove or change this, does the slideshow still trigger the same mechanism for the same reason?"** If no → **soul (LOCKED)**. If yes → **skin (OPEN)**.

Must classify these elements. The **Default** column shows the standard classification — only override it if you have a specific reason and note that reason in `This case's value`.

| Element | Default | This case's value |
|---------|:---:|---|
| **Text CTA Hook Strategy** (The psychological trap on Slide 0) | Soul | |
| **Trigger type** (The psychological reason people share) | Soul | |
| **Primary mechanism** (How the trigger is delivered) | Soul | |
| **Archetype** (Determines rules, checklist, and vehicle norms) | Soul | |
| **Information Format** (The content logic between slides, e.g., Zoom, List) | Soul | |
| **Visual Continuity strength** (The spatial relationship between slides) | Soul | |
| **Linguistic pattern** (The text template that carries the engagement) | Soul | |
| **Text presence** (Has text / no text) | Soul | |
| **Text rendering spec** (Cross-slide consistency of font family, weight, color rule) | Soul | |
| **Text position rule** (The rule deciding where text lands, e.g., fixed slot) | Soul | |
| **Ad insertion strategy** (How the product connects to the narrative) | Soul* | |
| **Vehicle credibility profile** (when vehicle is human: the look/aura *tier* that earns the hook — e.g., "hot finance bro", "sad-boy aesthetic", "relatable nerdy girl", "intimidating professor") | **Soul** (when human) / N/A (when animal/object) | |
| **Vehicle** (The specific character/subject carrying the mechanism. When human: specific job/age/ethnicity/outfit *within* the credibility tier above) | Skin | |
| **Setting/Environment** (Where the scene takes place, must support the mechanism) | Skin | |
| **Specific text content** (What fills the linguistic pattern slots) | Skin | |
| **Cultural reference** (What cultural context is used) | Skin | |
| **Specific font pick** (Within the chosen family) | Skin | |
| **Specific text position** (On each slide, within the rule) | Skin | |
| **Visual style** (Photo quality, color palette, era) | Skin | |
| **Number of slides** (How many build slides before the spike) | Skin | |

\* Ad insertion strategy is Soul when the ad IS the mechanism (e.g., Ad-as-punchline in Case 006); Skin when the ad is appended after the narrative (e.g., Ad-as-final-slide in Case 001). Decide per case.

**When to override the default**: a Skin element becomes Soul when this specific case relies on it for the mechanism to fire (e.g., Case 007's *cultural reference* "19th-century courtroom painting" is Soul because Dignity Mismatch needs high-gravitas art — a modern photo would break it). When you override, write the reason in the value column.

**For each Soul row**, articulate the **purpose** — the specific reason it's locked (what would break if you changed it). **For each Skin row**, articulate the **constraint** — the boundary within which it can be swapped (e.g., "Vehicle: any small animal with an expressive face"). If you can't articulate either, re-examine the classification.

**Fills report sections 6.1, 6.2, 6.3, 6.4 — ALL FOUR, in this order**:

```markdown
### 6.1 Soul vs Skin Table
```

| Element | Final classification | Case value | Purpose (if Soul) / Constraint (if Skin) |
|---------|:--------------------:|------------|------------------------------------------|
| Text CTA Hook Strategy | Soul | [hook type from Step 1.0] | [what breaks if changed] |
| Trigger type | Soul | [from Step 4] | [what breaks if changed] |
| Primary mechanism | Soul | [from Step 4] | [what breaks if changed] |
| Archetype | Soul | [from Step 4] | [what breaks if changed] |
| Information Format | Soul | [from Step 2] | [what breaks if changed] |
| Visual Continuity strength | Soul | [from Step 2] | [what breaks if changed] |
| Linguistic pattern | Soul | [the template] | [what breaks if changed] |
| Text presence | Soul | [yes/no] | [what breaks if changed] |
| Text rendering spec | Soul | [the spec] | [what breaks if changed] |
| Text position rule | Soul | [the rule] | [what breaks if changed] |
| Ad insertion strategy | Soul or Skin | [strategy] | [purpose or constraint, depending on classification] |
| Vehicle credibility profile | Soul (if human) / N/A | [look/aura tier, or N/A] | [purpose or N/A reason] |
| Vehicle | Skin | [the specific subject] | [the swap boundary, e.g., "any small animal with expressive face"] |
| Setting/Environment | Skin | [the place] | [swap boundary] |
| Specific text content | Skin | [the words] | [swap boundary — must fit the linguistic pattern] |
| Cultural reference | Skin | [the reference] | [swap boundary] |
| Specific font pick | Skin | [the font] | [swap boundary — within the family] |
| Specific text position | Skin | [per-slide position] | [swap boundary — must obey the position rule] |
| Visual style | Skin | [photo/illustration style] | [swap boundary — must keep authenticity tier] |
| Number of slides | Skin | [N] | [swap boundary — pacing range] |

Every row must be filled. If a row is N/A, write `N/A — <one-line reason>` in **both** the Case value and Purpose/Constraint columns.

```markdown
### 6.2 Override Log

- [Element X]: Default = [Soul/Skin], overridden to [Skin/Soul] because [specific reason
                tied to this case's mechanism]
- [Element Y]: ...

(Or: "None — all rows kept the default classification")

### 6.3 Transferability
- Products that FIT:    [category descriptors — e.g., "any productivity tool with
                          a 'replaces manual effort' angle"]
- Products that BREAK:  [category descriptors — what kills the mechanism]
- Audience required:    [who must be the target audience for this blueprint to land]

### 6.4 Derivation Rule
Derivation rule: Keep ALL Soul rows. Replace ≥2 Skin rows. Verify Soul row-by-row before generating.
```

#### Handoff note for derivation

This Soul vs Skin table is the canonical input for `slideshow-grid-prompter`. When the prompter (or any human deriving a variant) uses this blueprint, **they MUST go through every Soul row and confirm that the new design has a concrete implementation of it** — not just "I changed N skin elements". A derivation that swaps Skin freely but quietly drops a Soul (e.g., turning a "negative emotion mirror" into a "positive product testimonial") is a broken derivation, not a creative one.

### Step 7: Compile & Save

The analysis is **not done** until a Markdown file exists on disk. Steps 1–6 produce content; Step 7 assembles and saves it.

**Procedure**:

1. **Assemble** the report by concatenating sections 1.0 → 7 in the exact order shown in the Report Skeleton at the top of this skill.
2. **Add section 7. Notes** with anything that didn't fit above (open questions, unusual mechanics, things to double-check, deviations from this skill).
3. **Save** to `<source-name>.analysis.md` in the working directory.
4. **Pre-save checklist** — refuse to save if any of these fail:
   - [ ] Section 1.0 has all three layers (text hook / visual hook / stop-scroll), none are "TBD"
   - [ ] Section 1.2 per-slide table has one row per slide, every column filled
   - [ ] Sections 4.1–4.4 are present as separate sub-blocks (hook NOT collapsed into one line)
   - [ ] Section 5.1 has the per-slide pre-scan table covering every slide
   - [ ] Section 6.1 has all 19+ rows of the Soul/Skin table filled (case value AND purpose/constraint, not blank)
   - [ ] Section 6.4 ends with the literal "Derivation rule:" line
5. **After saving**, print a one-line confirmation in chat: `Analysis saved to <path>` (no other commentary needed — the file IS the deliverable).

**Output format note**: The chat output during analysis is working scratch; the file is the deliverable. Don't repeat the full report in chat after saving — just confirm the path.

---

## Updating This Skill

After each analysis session, append the new case to `references/cases.md` (follow Case 006's format). If you discover a new mechanism, trigger type, ad strategy, or analysis rule, also surface it in the SKILL.md tables above so future analyses can match against it.
