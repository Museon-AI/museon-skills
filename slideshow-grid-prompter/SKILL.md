---
name: slideshow-grid-prompter
description: "Generate grid-format image prompts for a slideshow by combining a Soul+Skin template description with a specific product and customized prompt. Input: structured Soul+Skin file + product info + custom instructions. Output: a single prompt that generates all slides in one grid image. Trigger when user wants to generate slideshow prompts in a grid format (e.g., 4x2 grid for 8 slides)."
---

# Slideshow Grid Prompter

**Input**: Soul+Skin description file + Product (name, URL, one-line description) + Customized prompt/instructions
**Output**: A single, comprehensive image generation prompt that produces all slides as panels within one grid image (see `templates/grid-prompt-output.md`)

This skill is a specialized variant of `slideshow-prompt-generator`. Instead of generating separate prompts for each slide, it generates **one master prompt** that instructs the AI to create a seamless grid (e.g., 4x2 for 8 slides) containing all slides. This is highly efficient for generating consistent slideshows in a single API call.

---

## Generation Flow

### Step 1: Understand the inputs
Read the Soul+Skin file, the product information, and any customized instructions from the user.
Identify:
- What rules are locked (soul)
- What elements are open (skin)
- How the user's custom instructions modify the skin or topic
- **What visual style is being used** (realistic/photographic OR illustrated/stylized) — this determines which Constraint 3 path to follow
- **Whether a Visual Hook Persona is present in the Soul rows** — if the source analysis contains a `Visual Hook Persona` row classified as Soul, extract its exact appearance description. This description is a locked constraint that must be carried into the Character Consistency Block, not discarded during skin substitution.

### Step 2: Find a Solution Scenario and Make Skin Decisions
The core logic is: **Product → Solution Scenario → Skin Decisions**.
1. **Find a Scenario**: Identify a specific problem/scenario that the Product solves, which also fits the emotional or narrative structure of the Soul. (e.g., Product: AI content creator → Scenario: A human creator burning out from the daily content grind).
2. **Decide the Skin**: Let the scenario dictate what the open Skin elements should become.
   - *Vehicle (Character)*: Who experiences this scenario?
   - *Setting*: Where does this scenario happen?
   - *Content/Text*: What specific pain points or thoughts fit this scenario?
   - *Visual Style*: What aesthetic best conveys the mood of this scenario?
3. **Handle Visual Hook Persona (critical — do not skip if present)**:
   - If the source Soul table contains a `Visual Hook Persona` classified as **Soul**, the appearance elements it describes are **locked**. They must be preserved in the Character Consistency Block of the new prompt. You may adapt them to the new scenario (e.g., change hair color or outfit to fit the new character's context), but you MUST NOT replace the underlying visual contrast logic (e.g., if the soul is "looks polished while claiming to struggle", the new character must also look polished, not visibly exhausted).
   - If the source Soul table contains a `Visual Hook Persona` classified as **Skin**, you may freely substitute appearance within the swap boundary described in the constraint column.
   - If no `Visual Hook Persona` row exists in the source (older analysis), treat it as unclassified and apply the decision tree from the slideshow-analyzer skill to determine whether the original appearance is load-bearing before discarding it.
4. **Apply Custom Instructions**: Integrate any specific requests from the user (e.g., specific character type or tone). Note: custom instructions may override Skin elements but MUST NOT override Soul elements, including a Soul-classified Visual Hook Persona.
5. **Anti-Clone**: Ensure you have changed enough Skin elements so the new slideshow doesn't look like a copy of the original template.

### Step 3: Design the Grid Layout
The grid layout must be chosen so that the **overall image ratio matches a standard AI generation ratio**. This ensures the AI does not distort panels, add extra panels, or insert white borders.

Use the lookup table below. For odd slide counts, the last cell is left as a white/blank panel.

| Slides | Grid Cells | Grid Layout | Slide Ratio | Overall Image Ratio | AI Gen Ratio | Match |
|--------|-----------|-------------|-------------|--------------------|--------------|---------|
| 1 | 1 | No grid | 9:16 | 9:16 | **9:16** | Exact |
| 2 | 2 | 2x1 | 4:5 | 8:5 | 3:2 | Close |
| 3 | 4 (+1 blank) | 2x2 | 9:16 | 18:32 | **9:16** | Exact |
| 4 | 4 | 2x2 | 9:16 | 18:32 | **9:16** | Exact |
| 5 | 6 (+1 blank) | 3x2 | 1:1 | 3:2 | **3:2** | Exact |
| 6 | 6 | 3x2 | 1:1 | 3:2 | **3:2** | Exact |
| 7 | 8 (+1 blank) | 2x4 | 1:1 | 2:4 | 9:16 | Close (0.06) |
| 8 | 8 | 2x4 | 1:1 | 2:4 | 9:16 | Close (0.06) |

**Key insight**: Slides 3-4 can use 9:16 per slide. Slides 5-8 must use 1:1 per slide to keep the overall grid ratio compatible with AI generation.

### Step 4: Draft the Panel Content
For each panel (slide) in the grid:
1. **Role**: From the soul's slide structure.
2. **Text**: Fill in the soul's linguistic pattern. Keep text short (max 3 lines, 5-8 words per line).
3. **Scene**: Design a visual scene that carries the text's meaning. Maintain consistent character and style across panels.
4. **Product placement**: Integrate the product on the ad slide according to the soul's ad strategy.

### Step 5: Write the Master Grid Prompt
Write a single, detailed image generation prompt that describes the entire grid. Follow the strict constraints below.

#### Constraint 1: Grid Structure (No Gaps & Correct Ratio)
- Start with: `A seamless [columns]-column by [rows]-row grid of [total] separate [style_descriptor] [slide_ratio] panels telling a story of...`
  - For realistic style, `[style_descriptor]` = leave empty or use nothing (do NOT write "photorealistic")
  - For non-realistic style, `[style_descriptor]` = the style name (e.g., "American comic book style", "anime style", "watercolor")
- Use the **slide ratio** from the Step 3 lookup table (either `9:16 vertical` or `1:1 square`).
- **Crucial**: Explicitly state `The grid has absolutely no gaps, borders, or white space between the panels. The panels touch each other directly to allow for perfect cropping into individual TikTok slides.`

#### Constraint 2: TikTok Font Specs
When specifying baked-in text, you MUST use the native TikTok text style. Keep it simple:
- **Font**: `TikTok Sans` (or a clean, bold sans-serif if the AI doesn't know TikTok Sans).
- **Color**: Any color. Stroke is optional, any color.
- **Default**: When no special requirement is given, use `white text with black outline`.
- **Effects**: None. No drop shadows, no glows, no gradients. Just text + optional stroke.

*Example instruction in prompt*: `White text in TikTok Sans font with a black outline reads exactly: "[Text]".`

#### Constraint 3: Visual Style Execution

This constraint governs how the visual style is prompted. **First, determine which path to follow**, then apply ALL rules for that path.

**Decision rule**: If the visual style is photographic/realistic (real people, real places, phone photos, lifestyle photography), follow **Path A**. If the visual style is illustrated/stylized (comic, anime, watercolor, pixel art, flat design, or any non-photographic style), follow **Path B**.

---

##### Path A: Realistic / UGC Style (Anti-AI Look)

AI-generated "realistic" photos fail because they look too perfect — plastic skin, symmetrical composition, studio lighting, and a general "stock photo" feel. TikTok UGC has the opposite DNA: it looks like someone pulled a photo from their camera roll and threw it into a slideshow in 2 minutes.

**Three layers of anti-AI prompting** (all three MUST be applied):

**Layer 1: RAW iPhone Aesthetic (Camera Identity)**

Instead of describing a "photorealistic" image, describe the **specific device and shooting conditions**. This anchors the AI to a real-world camera behavior.

- **MUST include**: `RAW iPhone aesthetic, shot on iPhone 13/14/15` (pick one specific model)
- **MUST include**: A specific lighting condition: `in low indoor light` / `under harsh overhead fluorescent` / `in natural window light` / `in direct afternoon sun`
- **Optional boost**: Add a fake filename like `IMG_4827.HEIC` or reference `Apple ProRAW, Deep Fusion processing`
- **Optional boost**: Add `posted on Instagram` or `posted on TikTok` to nudge the AI toward social media photo aesthetics

**Layer 2: Imperfection Injection (Anti-Perfection)**

AI defaults to perfection. You must explicitly inject flaws that real phone photos have. **MUST include at least 4 of these per prompt:**

| Category | Keywords to use | What it fixes |
|----------|----------------|---------------|
| Skin | `visible skin texture, natural pores, uneven skin tone, no airbrushing, subtle blemishes` | Fixes plastic/waxy skin |
| Eyes | `natural eye reflections, slight redness in whites of eyes, asymmetric eye shape` | Fixes lifeless doll eyes |
| Pose | `caught mid-motion, natural unposed posture, slightly awkward angle, one eye slightly squinted` | Fixes mannequin stiffness |
| Focus | `slight softness, phone camera deep depth of field, not tack-sharp` | Fixes DSLR-like bokeh that phones don't produce |
| Grain/Noise | `slight grain in shadows, minor JPEG compression, not pixel-perfect` | Fixes the "too clean" digital look |
| Color | `auto white-balance, slightly warm/cool cast, not color-graded, flat contrast` | Fixes cinematic color grading |
| Composition | `slightly off-center framing, asymmetric composition, some dead space, not rule-of-thirds` | Fixes "too perfectly composed" look |
| Background | `real environmental clutter, visible charging cables, random objects on surfaces, not styled` | Fixes "everything is perfectly placed" look |

**MUST NEVER use these words** (they push toward AI/stock look):

`photorealistic, 8K, ultra HD, hyper-realistic, perfect, flawless, studio lighting, sharp focus, bokeh, professional photo, high resolution, masterpiece, best quality, ultra detailed, cinematic lighting, dramatic lighting, golden hour, beautiful, elegant, stunning`

**Layer 3: TikTok UGC Scene DNA (Content Identity)**

Beyond camera and imperfection, the *content* of the scene must feel like TikTok UGC — not a magazine shoot.

**Scene construction rules:**
1. **Selfie or POV angles dominate** — Most TikTok photos are selfies (front camera, slightly above eye level), overhead desk shots, or "I just snapped this" angles. Avoid cinematic wide shots or perfectly framed portraits.
2. **Mundane backgrounds are trust signals** — Real UGC has messy desks, unmade beds, bathroom mirrors, car interiors, crowded cafes. NOT: minimalist studios, perfectly styled spaces, empty rooms with one designer lamp.
3. **Everyday objects as props** — Phone chargers, iced coffee cups (with condensation and straw), crumpled receipts, tote bags, AirPods case, half-eaten snack. NOT: artisan ceramics, designer objects, perfectly arranged books.
4. **Clothing is casual and specific** — "oversized grey hoodie with coffee stain on sleeve", "wrinkled white tee", "old Nike cap". NOT: "stylish blazer", "elegant outfit", "fashionable attire".
5. **Lighting is whatever the room gives you** — Overhead fluorescent, laptop screen glow, window light with harsh shadows, mixed color temperatures. NOT: golden hour, soft diffused light, rim lighting.
6. **People are doing something, not posing** — "caught mid-laugh looking at phone", "typing with one hand while holding coffee", "squinting at laptop screen". NOT: "looking confidently at camera", "smiling warmly", "posing elegantly".

**UGC Scene Template** (append to global style block):
```
Every panel should look like a photo pulled from someone's camera roll — the kind of image a real person would casually post on TikTok or Instagram Stories. Not a photoshoot, not an ad, not a stock photo. The lighting is whatever the room provides. The background has real-life clutter. The person (if present) is caught in a natural moment, not posing. Shot on iPhone [model] in [lighting condition]. RAW iPhone aesthetic with visible skin texture, slight grain in shadows, auto white-balance, and phone camera deep depth of field. No airbrushing, no color grading, no cinematic lighting, no bokeh.
```

**Path A Checklist** (verify before finalizing prompt):

| # | Check | If it fails... |
|---|-------|----------------|
| 1 | Does the prompt specify a phone model? | Add `shot on iPhone 14` or similar |
| 2 | Does the prompt include ≥4 imperfection keywords? | Add from Layer 2 table |
| 3 | Does the prompt avoid ALL banned keywords? | Remove any from the "MUST NEVER use" list |
| 4 | Are backgrounds described with mundane clutter? | Replace styled/minimalist descriptions with real-life mess |
| 5 | Are people described mid-action, not posing? | Rewrite to "caught doing X" instead of "standing/sitting nicely" |
| 6 | Is lighting described as ambient/natural, not cinematic? | Replace "golden hour" / "soft light" with "overhead light" / "window light with harsh shadows" |
| 7 | Is clothing casual and specific, not stylish/elegant? | Replace fashion descriptions with everyday clothes |
| 8 | Does the scene feel like a camera roll photo? | If it reads like a magazine shoot description, rewrite entirely |

---

##### Path B: Illustrated / Stylized (Style Consistency)

For non-realistic styles, the challenge is NOT "looking too AI" — it IS AI-generated art and that's fine. The challenge is **style consistency across panels** and **expressive execution** within the chosen style. Each panel must look like it was drawn by the same artist in the same session.

**Three layers of style prompting** (all three MUST be applied):

**Layer 1: Style Anchor (Identity Lock)**

You MUST lock the art style in the global style block at the top of the prompt, before any panel descriptions. The style anchor has three components:

1. **Style name**: The primary style keyword. Use the reference table below to pick the right keywords.
2. **Artist/reference anchor** (optional but recommended): Name a specific artist, franchise, or reference to lock the style further. E.g., `style of Jim Lee` for American comics, `Studio Ghibli art style` for painterly anime.
3. **Anti-drift clause**: Explicitly state what the style is NOT. E.g., `This is NOT photographic. No realistic textures, no photographic lighting, no camera effects.`

**Style Reference Table:**

| Style | Primary Keywords | Sub-style Keywords | Artist/Reference Anchors |
|-------|-----------------|-------------------|------------------------|
| American Comic | `American comic book style, bold outlines, cel shading, dynamic angles` | `superhero comic art, Ben Day dots, halftone dots` (retro); `gritty noir comic` (dark) | `style of Jim Lee` (classic), `style of Frank Miller` (noir/gritty), `style of Jack Kirby` (cosmic/dynamic) |
| Manga / Anime | `manga style, anime illustration, large expressive eyes, speed lines` | `shonen manga` (action), `shojo manga` (romance/soft), `chibi` (cute/deformed) | `Studio Ghibli art style` (painterly), `style of Akira Toriyama` (Dragon Ball), `style of Junji Ito` (horror) |
| Watercolor | `watercolor illustration, soft washes, transparent colors, bleeding edges, textured paper` | `wet-on-wet technique, botanical watercolor, dreamlike watercolor` | `style of Agnes Cecile` (expressive), `style of Beatrix Potter` (storybook) |
| Pixel Art | `pixel art, retro game art, limited color palette, visible pixels` | `16-bit style, NES/SNES style, dithering` | `style of Superbrothers` (atmospheric), `style of Celeste` (modern pixel) |
| Flat / Vector | `flat design, vector illustration, clean lines, solid colors, geometric shapes` | `minimalist illustration, 2D art, infographic style` | `style of Kurzgesagt` (educational), `style of Malika Favre` (bold/graphic) |
| Ligne Claire | `Ligne Claire style, clear line, even line weight, flat colors` | `Bande Dessinée art, realistic proportions` | `style of Hergé` (Tintin), `style of Moebius` (sci-fi/fantasy) |
| Retro / Vintage | `retro illustration, vintage poster art, mid-century modern illustration` | `1950s advertising style, Art Deco, propaganda poster` | `style of J.C. Leyendecker`, `style of Alphonse Mucha` (Art Nouveau) |
| 3D Render / Claymation | `3D rendered, clay figure style, Pixar-like, soft plastic texture` | `claymation, stop-motion look, isometric 3D` | `style of Pixar`, `style of Aardman` (Wallace & Gromit) |

**Layer 2: Visual Consistency Lock**

Across all panels, the following MUST remain consistent. Define each in the global style block:

| Element | What to lock | Example |
|---------|-------------|---------|
| **Line weight** | Exact thickness and style of outlines | `bold black outlines of uniform 3px weight` or `thin varied ink lines` or `no outlines, shapes defined by color` |
| **Color palette** | The palette approach or specific colors | `limited palette of 5 colors: black, white, red, gold, grey` or `muted pastel tones throughout` or `high-saturation pop colors` |
| **Shading method** | How light and shadow are rendered | `flat cel shading with hard shadow edges` or `crosshatch shading` or `no shading, flat colors only` or `soft gradient shading` |
| **Detail level** | How much detail appears in scenes | `highly detailed backgrounds with intricate linework` or `minimal backgrounds, focus on characters` or `geometric simplified forms` |
| **Texture** | Surface treatment across the image | `visible paper texture throughout` or `smooth digital finish` or `visible brush strokes` or `halftone dot pattern` |

**Layer 3: Expressive Execution**

Non-realistic styles have unique tools for conveying emotion and energy that realistic photos do not. Use them.

| Style | Expression Tools | Example Keywords |
|-------|-----------------|-----------------|
| American Comic | Dynamic angles, speed lines, impact frames, dramatic shadows | `dramatic low angle, speed lines radiating from impact, stark black shadows, dynamic foreshortening` |
| Manga / Anime | Exaggerated expressions, screentones, chibi moments, sweat drops | `huge shocked eyes with tiny pupils, screentone blush, comedic sweat drop, speed lines background, dramatic sparkle effect` |
| Watercolor | Color bleeding for emotion, white space for breathing room, wet edges for softness | `colors bleeding outside the lines to convey chaos, large areas of white paper for calm, wet-on-wet blending for dreaminess` |
| Pixel Art | Limited animation frames, dithering for mood, color palette shifts | `dithered shadows for moodiness, warm palette shift for comfort scenes, cool palette shift for tension` |
| Flat / Vector | Scale contrast, negative space, color blocking for emphasis | `oversized character dwarfing tiny objects for emphasis, bold color block background shift per panel, geometric exaggeration` |

**Path B Checklist** (verify before finalizing prompt):

| # | Check | If it fails... |
|---|-------|----------------|
| 1 | Is the style name explicitly stated in the global block? | Add the primary style keywords from the reference table |
| 2 | Is there an anti-drift clause? | Add `This is NOT photographic. No realistic textures, no photographic lighting, no camera effects.` |
| 3 | Are line weight, color palette, shading method, detail level, and texture all defined? | Add missing elements to the global style block |
| 4 | Does every panel use at least 1 style-specific expression tool? | Add from the Expressive Execution table |
| 5 | Would all 6-8 panels look like they were drawn by the same artist? | Strengthen the consistency lock — add more specific constraints |
| 6 | Are there any realistic/photographic keywords leaking in? | Remove words like `natural lighting`, `skin texture`, `phone camera`, `RAW` — these belong to Path A only |
| 7 | Is the style anchor specific enough? | If just `comic style`, narrow to `American comic book style, style of Jim Lee, bold outlines, cel shading` |

---

#### Constraint 4: Character Consistency
If the slideshow features a recurring character, you MUST lock the character's identity in the global style block at the top of the prompt, before any panel descriptions.

**For Path A (Realistic)**, define:
- **Age, gender, ethnicity, build** (e.g., "a slim East Asian woman in her late 20s")
- **Key distinguishing features** (e.g., "shoulder-length black hair with bangs, small mole below left eye, slightly crooked nose")
- **Wardrobe anchor** (e.g., "wearing the same oversized grey hoodie and black leggings throughout all panels")
- **One physical imperfection** (e.g., "slightly uneven eyebrows", "a few flyaway hairs", "chipped nail polish") — this is critical for breaking the AI "perfect person" default
- **Visual Hook Persona lock (if Soul-classified)**: If the source analysis has a Soul-classified `Visual Hook Persona`, copy its exact appearance elements here. These override any scenario-driven character decisions. The visual contrast logic (e.g., "looks polished despite struggling") must be explicitly stated so the AI renders the right emotional register. Example: `She looks completely put-together: flawless clean-girl makeup, smooth styled hair, chic minimal outfit. This visual polish is intentional — it must contrast sharply with the pain described in the text.`

**For Path B (Illustrated)**, define:
- **Character design sheet** (e.g., "a young woman with short spiky blue hair, round face, large green eyes, small nose")
- **Key visual identifiers** (e.g., "always wears a red scarf and oversized round glasses")
- **Proportions** (e.g., "slightly chibi proportions — large head, small body" or "realistic proportions")
- **Expression range** (e.g., "expressive manga-style eyes that change size with emotion")

Then in every panel description, refer back to the character as `the same woman/man/character` to reinforce continuity.

#### Constraint 5: Panel Descriptions
Describe each panel explicitly: `Panel 1 (Top Left): [Scene description]. [Font Spec] reads exactly: "[Exact Text]".`

**For Path A (Realistic)**, each panel description MUST include:
1. The scene (what's happening, who's in it)
2. At least 1 specific mundane background detail
3. The lighting condition for this specific panel
4. The text overlay specification
5. At least 1 imperfection detail (grain, slight blur, off-center framing, etc.)

**For Path B (Illustrated)**, each panel description MUST include:
1. The scene (what's happening, who's in it)
2. The character's expression/pose using style-specific expression tools
3. At least 1 background detail consistent with the locked style
4. The text overlay specification
5. At least 1 style-specific visual effect (speed lines, screentones, color bleed, etc.)

### Step 6: Validate
- **Anti-clone test**: Is it distinct from the original template?
- **Soul preservation test**: Does it keep the trigger, mechanism, and unspoken truth?
- **Visual Hook Persona test**: If the source has a Soul-classified `Visual Hook Persona`, does the Character Consistency Block explicitly preserve the visual contrast logic? A character who looks "visibly exhausted" when the soul requires "looks polished while struggling" is a failed derivation.
- **Grid format test**: Does the prompt clearly define the grid structure, no-gap rule, TikTok font specs?
- **Style test (Path A)**: Run through the Path A Checklist. Every check must pass.
- **Style test (Path B)**: Run through the Path B Checklist. Every check must pass.
- **Vibe test**: For Path A — does it sound like describing a camera roll, or a photoshoot brief? For Path B — does it sound like a commission brief for a specific artist, or a vague "make it look cool" request?

### Step 7: Output
The deliverable is **only the raw image generation prompt** — no derivation decisions, no anti-clone checks, no captions, no hashtags. Save the prompt as a plain text file (`.md`) to the working directory. The file should contain nothing but the master image prompt itself. **DO NOT generate multiple variants unless explicitly asked.** The goal is to produce ONE perfect, comprehensive prompt that synthesizes the Soul, Skin, Product, and custom instructions.

---

## Common Mistakes

### General (Both Paths)
1. **Forgetting the "No Gaps" rule** — If the AI generates white borders between panels, the user cannot crop them cleanly into individual slides.
2. **Over-designed Text** — Do not ask the AI for drop shadows, glows, or complex typography. TikTok text is simple: white TikTok Sans font, optional black outline.
3. **Too much text per panel** — AI struggles with long text. Keep baked-in text short (1-3 lines max per panel).
4. **Missing panel locations** — Always specify the location (e.g., Top Left, Bottom Right) for each panel to help the AI organize the grid.

### Path A (Realistic) Mistakes
5. **Plastic AI Faces** — The #1 giveaway. MUST include `visible skin texture, natural pores, no airbrushing` AND specify a phone model. Never use `perfect`, `flawless`, or `beautiful` to describe people.
6. **Styled/aspirational backgrounds** — The biggest UGC killer. Real TikTok creators film in messy rooms, not minimalist studios. Replace "cozy styled desk" with "cluttered desk with random papers and a half-empty water bottle".
7. **Cinematic lighting language** — Words like "golden hour", "soft diffused light", "warm ambient glow" trigger the AI's "pretty photo" mode. Use "overhead fluorescent", "laptop screen glow", "harsh window light" instead.
8. **Perfect poses** — "Smiling at camera" or "looking confident" = stock photo. "Caught mid-sentence", "squinting at screen", "one hand in hair while reading phone" = UGC.
9. **Using "photorealistic"** — Counterintuitively, this word makes images LESS realistic. It triggers the AI's "make it look impressive" mode. Use `RAW iPhone aesthetic` instead.
10. **Forgetting physical imperfections** — Real people have flyaway hairs, slightly uneven features, chipped nails. AI defaults to symmetrical perfection. You must explicitly prompt for at least one imperfection per character.
11. **Discarding a Soul-classified Visual Hook Persona** — The most common derivation failure. When a source analysis marks Visual Hook Persona as Soul (e.g., "looks flawless while claiming to struggle"), replacing the polished character with a visibly exhausted one removes the core visual tension that makes the hook work. Always check the Soul table before writing the Character Consistency Block.

### Path B (Illustrated) Mistakes
11. **Style drift between panels** — The #1 problem for illustrated slideshows. If the global style block is vague (just "comic style"), different panels will look like different artists drew them. Be extremely specific: name the style, an artist reference, line weight, color palette, and shading method.
12. **Mixing realistic and illustrated keywords** — Using `natural lighting`, `skin texture`, `phone camera` in an illustrated prompt confuses the AI and produces a weird hybrid. Path A and Path B keywords must NEVER mix.
13. **Forgetting the anti-drift clause** — Without explicitly saying "This is NOT photographic", the AI may drift toward realism, especially for human characters. Always include the anti-drift clause.
14. **Underusing expression tools** — Non-realistic styles have powerful visual vocabulary (speed lines, screentones, color bleeds, exaggerated expressions) that realistic photos cannot use. If your illustrated panels look "static" or "boring", you're not using enough style-specific expression tools.
15. **Vague style names** — "Cartoon style" or "illustrated" is too vague and will produce inconsistent results. Always use the most specific style name possible: "American comic book style, style of Jim Lee, bold outlines, cel shading" is 10x better than "comic style".
