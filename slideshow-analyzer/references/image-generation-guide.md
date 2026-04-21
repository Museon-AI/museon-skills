# Image Generation Guide

Execution details for generating slideshow images. For analysis and derivation knowledge, see `analysis-playbook.md`.

Read this file when you're ready to generate images (Module 2 Step 5 / Path B Steps 3-4).

---

## Contents

1. [Character Expressiveness: AI Prompt Guide](#character-expressiveness-ai-prompt-guide)
2. [Text Overlay: Two Formats](#text-overlay-two-formats) — includes **Cross-slide Text Rendering Consistency** (read first)
3. [Authenticity: Phone Snapshot Aesthetic](#authenticity-phone-snapshot-aesthetic)
4. [Generation Checklist](#generation-checklist)
5. [Strategy: Single-Pass Multi-Panel Generation](#strategy-single-pass-multi-panel-generation)

---

## Character Expressiveness: AI Prompt Guide

AI image generators default to "beautiful animal photography" — smooth fur, dignified pose, pleasant expression. This is the opposite of what memes need. You must actively fight this default.

### Prompt Keywords for Meme Expressions

- **Smug/judgmental**: `squinting, narrowed eyes, judging, unimpressed, side-eye, looking down at`
- **Dumb/confused**: `derp face, cross-eyed, tongue sticking out, blank stare, buffering expression, mouth agape`
- **Shocked/dramatic**: `wide eyes, dilated pupils, ears flattened back, startled, mouth open`
- **Angry/chaotic**: `hissing, fur puffed up, bristling, arched back, ears pinned back, showing teeth`
- **Sad/pathetic**: `big watery eyes, droopy ears, curled up small, hiding face in paws`

### Prompt Keywords for Meme Camera Angles

- `extreme close-up of face, wide-angle lens distortion, shot from below chin level`
- `cat accidentally opened front camera, fish-eye lens effect on face`
- `face filling entire frame, nose exaggerated by wide-angle`
- `caught mid-action, motion blur on paws, slightly out of focus`

### The Extreme Close-Up Trick

Many viral cat memes use an **extreme close-up from below or at face level** — the wide-angle distortion makes the nose look huge, the face looks round and dumb, and the expression is exaggerated by the lens. Think "cat accidentally opened the front camera". This distortion IS the comedy.

### Anti-Keywords (avoid — they push toward "pretty")

- `beautiful`, `elegant`, `majestic`, `graceful`, `cute`, `adorable`, `perfect`
- `studio lighting`, `portrait`, `professional photo`, `sharp focus`, `high resolution`
- `looking at camera` (too posed — prefer `caught in the act` angles)

---

## Text Overlay: Two Formats

**Core rule: Text is ALWAYS generated directly by the AI image generator as part of the prompt.** Do NOT generate images without text and add text later via Pillow/post-processing. The AI-rendered text is part of the meme aesthetic — slightly imperfect letterforms, natural integration with the image, and the "made in 30 seconds on a meme app" feel. Post-processed text looks too clean and mechanical.

### Cross-slide Text Rendering Consistency (READ FIRST)

The single biggest source of "the set feels off" is font drift between slides — serif on one, sans-serif on the next; bold here, thin there; centered on slide 1, left-aligned on slide 4. The image model does this whenever the prompt leaves room for interpretation (e.g., `"thin sans-serif like Helvetica or SF Pro"`).

Eliminate drift with two mandatory practices:

**1. Paste an identical TEXT RENDERING SPECIFICATION block into every slide's prompt.** No fuzzy words (`thin`, `like`, `or`, `ish`). Exact values only. Use this template:

```
TEXT RENDERING SPECIFICATION (identical across every slide in this set):
- Font family: [exact name, e.g. "SF Pro Display", or exact descriptor, e.g. "geometric sans-serif with no serifs anywhere"]
- Weight: [single value, e.g. "Regular 400"] — NOT bold, NOT semibold, NOT light
- Style: upright, not italic
- Letterforms: [e.g. "single-story a, geometric g, no serifs"]
- Case: [e.g. "lowercase"]
- Color: [exact hex, e.g. "#FFFFFF pure white"]
- Size: each line = [exact %, e.g. "3.5% of image height"]
- Alignment: [e.g. "center-aligned within its own text block"]
- Line count: exactly [N] lines, each line separated by a single line break
- Effects: NO drop shadow, NO outline, NO stroke, NO background bar, NO gradient (or specify exactly one effect with exact parameters)
- Text content (verbatim): "[line 1]" / "[line 2]" / "[line 3]"
```

Only the *position* of the text block is allowed to vary per slide, and it must be described as a region (e.g., `"placed in the ceiling area above the heads"`), not as pixel coordinates.

**2. Lock the rendering with a reference image after slide 1 is approved.** Workflow:

- Generate slide 1 using the full spec above. Iterate on this slide alone until the font, weight, color, and size are exactly right.
- For every subsequent slide (2..N), pass the approved slide 1 as a `references` image in addition to the spec block, and append this line to the prompt: `"Text rendering (font, weight, color, size, effects) must be identical to the reference image."`
- This is more reliable than any verbal description. Combine both — do not rely on the spec block alone.

These two practices apply to all formats below (Caption Bar, Impact Overlay, and any custom minimal/editorial style). The format templates describe the *look*; the spec block enforces the *consistency*.

### Format A: Caption Bar (modern TikTok/Twitter style) — RECOMMENDED for slideshows

- **Layout**: Solid white or black bar **above** the image (not overlaid on the image)
- **Font**: Bold sans-serif (Arial/Helvetica), black text on white bar (or white text on black bar)
- **Case**: Sentence case, lowercase-heavy, casual grammar ("me when...", "nobody:", "violence")
- **Size**: Medium — readable but not screaming
- **Vibe**: Like a tweet or TikTok caption sitting above a photo

**AI prompt template for Format A** (append to image prompt, after the TEXT RENDERING SPECIFICATION block):

> The image has a solid white bar across the top of the frame, exactly 18% of total image height. Inside the bar: black #000000 text in Arial Bold (no substitution), weight 700, horizontally and vertically centered within the bar. The text reads exactly: "[TEXT]". Below the bar is the photo. The bar has no gradient, no shadow, no border; the text has no outline and no shadow. The text must be fully legible and not cut off at the left or right edges.

**Tips for Caption Bar text in AI prompts**:
- Keep text SHORT — max ~8 words per line, 1-3 lines total
- If text is longer, pre-split into lines with `\n` and describe each line in the prompt
- Use the exact phrase "reads exactly:" followed by the text in quotes — this helps the AI render it accurately
- Mention "fully legible, not cut off" to prevent edge clipping

### Format B: Impact Overlay (classic meme style)

- **Layout**: Text overlaid directly on the image, top and/or bottom
- **Font**: Impact or heavy condensed sans-serif, ALL CAPS
- **Color**: White with thick black outline stroke
- **Size**: Large — intentionally bold and in-your-face
- **Vibe**: Classic 2010s meme — the thick outline IS the meme aesthetic

**AI prompt template for Format B** (append to image prompt, after the TEXT RENDERING SPECIFICATION block):

> White #FFFFFF ALL-CAPS text rendered in Impact (no substitution), weight Bold, with a solid black #000000 outline stroke that is 6% of the text's cap height. The top text reads exactly: "[TOP TEXT]" and sits flush to the top edge of the image with 4% padding. The bottom text reads exactly: "[BOTTOM TEXT]" and sits flush to the bottom edge with 4% padding. Both lines are center-aligned. Each text block is 10% of image height. No drop shadow, no gradient, no other effects.

### How to Choose

| Scenario | Format | Why |
|----------|--------|-----|
| TikTok/IG slideshow (our primary use case) | A (Caption Bar) | Matches platform native style; text is separate from image |
| Single-image meme for sharing | B (Impact) or A | Both work; Impact has stronger meme recognition |
| Narrative/story slides | A (Caption Bar) | Cleaner for multi-slide reading flow |
| Spike/punchline slide | Either | Impact hits harder; Caption Bar is more modern |

### Text Length Strategy

AI image generators struggle with long text. Adapt your copy to fit:

| Lines | Max words/line | Example |
|-------|---------------|--------|
| 1 | 8-10 | "how to sound smart in emails" |
| 2 | 6-8 each | "steal from your sent folder" / "just remix your best lines" |
| 3 | 5-6 each | "keep it short" / "if it needs a table of contents" / "it's too long" |

If the slide's message needs more text than 3 short lines, split across two slides or simplify the copy. **Never ask the AI to render a paragraph** — it will fail.

### Handling AI Text Rendering Errors

If the AI misspells words or garbles text:
1. **Re-generate** with the same prompt (AI text rendering has variance; a retry often fixes it)
2. **Simplify** the text (fewer words = higher accuracy)
3. **Last resort only**: Use `generate_image_variation` to fix the text on the existing image

Do NOT fall back to Pillow post-processing — the aesthetic mismatch between AI-generated image and programmatically-added text is immediately visible and breaks the meme feel.

---

## Authenticity: Phone Snapshot Aesthetic

### Core Rule

Meme slideshows live or die on perceived authenticity. Over-production signals "ad" before the viewer even reads the text.

### Phone Snapshot Comparison

| Dimension | Good (phone snapshot) | Bad (over-produced) |
|-----------|----------------------|--------------------|
| Lighting | Slightly overexposed overhead light, mixed color temps, visible lamp glare | Perfect golden hour, studio-grade soft lighting, cinematic color grading |
| Focus | Most of frame in focus (phone's deep DoF), slight softness | Shallow depth of field with creamy bokeh (DSLR look) |
| Composition | Slightly off-center, not perfectly framed, some dead space | Rule-of-thirds perfection, every element deliberately placed |
| Background | Real clutter — charging cables, water bottles, crumpled tissues, random stuff on shelves | Styled "cozy" setup — matching books, designer lamp, artisan coffee mug |
| Color | Neutral/cool, slightly flat, phone auto white-balance | Warm cinematic palette, color-graded, rich tones |
| Resolution feel | Crisp but flat (phone sensor look) | Creamy, dimensional, "expensive lens" look |

### Mundane Scene Checklist

Scenes must contain **≥ 2 mundane markers** — details that signal "this is someone's real space":

- Messy desk with random objects (pens, sticky notes, receipts)
- Visible charging cable or power strip
- Plain/ugly overhead lighting (not warm lamps)
- Unmatched furniture, IKEA basics
- Water bottle, takeout container, snack wrapper
- Unmade bed or wrinkled blanket in background
- Slightly dirty or cluttered floor visible
- Generic white/beige walls, no styled decor

**Anti-markers** (signals "this is staged", avoid these):
- Bookshelf with color-coordinated spines
- Designer desk lamp with warm glow
- Artisan coffee mug on a coaster
- Plants perfectly placed for composition
- Matching furniture set
- Golden hour light streaming through curtains

### Narrative Composition: Caught in the Act

"Phone snapshot" does NOT mean "boring snapshot". Every slide must still tell a micro-story.

| Dimension | Good (authentic + narrative) | Bad (authentic but boring) |
|-----------|------------------------------|---------------------------|
| Character-prop relationship | Cat is actively typing / staring at screen / blocking keyboard | Cat is sitting near a laptop |
| Camera angle | "Discoverer" POV — like you walked in and caught them doing something | Flat, centered, room-overview shot |
| Character attention | Focused on the prop ("doing the thing") or side-eyeing the camera ("caught") | Staring blankly at camera (posing) |
| Framing | Close enough to see expression; character fills 50%+ of frame | Wide shot where character is small in the scene |
| Moment | Mid-action — paw on keyboard, face inches from screen, mid-yawn | Static — just sitting, just standing |

**Prompt trick**: Describe the character **doing an action** with a specific prop, not just **being in a place**. "Cat hunched over laptop, one paw mashing the keyboard, squinting at the screen" beats "Cat sitting on desk next to laptop".

### Transmission Loss: The "Screenshotted 50 Times" Look

Viral memes look like they've been screenshotted, compressed, re-uploaded, and shared across platforms multiple times. This degradation is a trust signal.

| Dimension | Fresh photo (too clean) | Meme-grade (transmission loss) |
|-----------|------------------------|-------------------------------|
| Sharpness | Pixel-perfect, crisp edges | Slightly soft, minor compression artifacts |
| Noise | Clean sensor output | Visible grain, especially in shadows |
| Color | Full dynamic range | Slightly washed out, reduced contrast |
| Resolution feel | 4K phone camera | Feels like 720p even if technically larger |
| Motion | Frozen sharp | Slight motion blur on extremities (paws, tail) |

**AI Prompt Keywords for Transmission Loss**:
- `slightly grainy, low-light phone camera noise, minor JPEG compression artifacts`
- `not perfectly sharp, slight motion blur, candid snapshot quality`
- `slightly washed out colors, flat contrast, auto-exposure`

**Important**: Don't overdo it. We want "shared a few times" not "deep fried meme".

### AI Image Generation: Authenticity Prompt Template

Append to the end of any image prompt (BEFORE the text overlay template):

> Shot from a close "discoverer" angle, as if someone walked in and quickly snapped this with their phone. The photo looks like it was taken with a cheap smartphone camera in low indoor lighting — slightly grainy, not perfectly sharp, with flat auto-exposure. No shallow depth of field. The background contains everyday clutter like [charging cables / water bottles / random papers / takeout containers]. No color grading, no cinematic lighting, no styled decor. Slightly washed-out colors, minor noise in shadow areas. The overall look is a candid phone snapshot that has been screenshotted and re-shared a few times, NOT a fresh high-resolution photo.

### Exception: Soft-Ad Slide

The soft-ad slide (and only the soft-ad slide) may be slightly more polished than narrative slides — this mirrors how Case 004 used an AI-generated final slide while the rest were real photos. The contrast itself signals "upgrade" which reinforces the product message.

---

## Generation Checklist

After generating each image, verify:

| # | Check | If it fails... |
|---|-------|----------------|
| 1 | Does the spike trigger the intended mechanism? | Redesign the scene |
| 2 | Would someone screenshot the spike and send it to a friend? | Increase contrast stacking or expression intensity |
| 3 | Does it look like a previous case with different words? | Change more skin elements |
| 4 | Do narrative slides pass the phone snapshot test? | Re-prompt with Authenticity template |
| 5 | Does each character have a meme-grade expression? | Re-prompt with expression keywords + extreme close-up angles |
| 6 | Does the text use a recognized meme format (Caption Bar or Impact)? | Re-generate with text overlay template; if text is garbled, simplify copy and retry |
| 7 | Is the character actively doing something with a prop? | Re-prompt with "doing an action" phrasing |
| 8 | Does the image have slight "transmission loss" feel? | Re-prompt with grain/noise keywords |


---

## Strategy: Single-Pass Multi-Panel Generation

For slideshows where all panels share the same character, lighting, and apartment-style setting, generating one large multi-panel canvas in a single call — then slicing it programmatically — outperforms generating panels one by one. This is the **recommended default** for any 4-panel slideshow with a single recurring character.

### Why It Beats Single-Image Generation

| Dimension | One-by-one (5 calls) | Single-pass quad (1 call) |
|---|---|---|
| Generation calls | 5 + retries | **1** |
| Character consistency | depends on `references=`, still drifts | **identical** (siblings from one render) |
| Lighting/style consistency | drifts across calls | **identical** |
| Text rendering pass-rate | ~80% per panel | observed ~100% in batch |

### When to Use vs Avoid

**Use** for: 4-panel sets with a single recurring character; matching apartment / outdoor / office settings; tight memes where all panels share an aesthetic.

**Avoid** for: panels that intentionally use very different art styles or color grading; outputs that need print-grade resolution per panel (each panel is ~1024×1024 from a `1:1` quad).

### Recommended Layout

Use a **2×2 grid on a `1:1` canvas** as the default. Each panel ends up ~1024×1024, ideal for Instagram Post / X / 小红书 square formats. 3×3 begins to lose per-panel resolution and text fidelity.

### The Anti-Border Prompt Stack (mandatory)

Models love to add gutters, frames, polaroid borders, or thin off-color seams between panels. Defeating this requires a **dense negation stack** at the very top of the prompt, plus content-side reinforcement:

```
ABSOLUTE LAYOUT REQUIREMENT — read this first and follow it strictly:
Four photographs are placed in a 2x2 grid filling a perfect square canvas.
The four photographs are stitched together seamlessly.
There is NO border, NO frame, NO divider, NO gutter, NO gap, NO black line,
NO white line, NO grey line, NO seam, NO margin of any kind between the
four photographs. The boundary between any two photographs is invisible —
the only thing that changes at the boundary is the scene content itself.
Each photograph fills exactly 50% width and 50% height of the total square
and extends all the way to the edge of its quadrant. There must be NO thin
off-color pixel row or column at any internal boundary. Imagine four photos
pasted directly next to each other on a wall with zero spacing.
```

Then describe each quadrant explicitly as `TOP-LEFT PHOTO — ...`, `TOP-RIGHT PHOTO — ...` etc., and end with a final reminder: *"the four photos meet edge to edge with absolutely no border, no line, no seam, no gap of any kind."*

### Critical Content-Side Rule: Avoid Nested Collages

Even with a perfect outer prompt, if any single panel is described as a "3x3 mini collage" or "polaroid grid", the model will add **internal grid lines** inside that panel. Instead:

- Replace nested collages with a **single full-bleed photo + overlaid floating bubbles/icons** that convey the same "overload" feeling.
- Example: instead of "9-tile collage of the character overwhelmed in 9 scenarios", use "single close-up of the character on a couch, with 6 floating notification bubbles around its head".

### Programmatic Slicing — Why It Cannot Be a Simple Halve

Even with the negation stack, the model will often leave a 5–15 pixel **pure white (or pure black) buffer band** along internal seams. Splitting at `width / 2` will dump this band into the right edge of the left panel.

The skill ships a smart slicer that **detects the buffer band's actual pixel bounds** and crops around it. Run:

```bash
python slideshow-analyzer/scripts/multi_panel_slice.py <quad.png> <output_dir>
```

It will:
1. Scan the central horizontal and vertical strips for high-brightness or low-brightness contiguous bands.
2. Identify the true left/right/top/bottom of each panel (skipping the buffer band entirely).
3. Save 4 clean PNGs (`panel_tl.png`, `panel_tr.png`, `panel_bl.png`, `panel_br.png`).

Output panels will be ~1019×1019 (slightly smaller than 1024 because the band is excised), with no white/black edge whatsoever.

### Mini Workflow

1. Write the prompt with the anti-border stack at the top + 4 numbered quadrant descriptions + final reminder.
2. Generate at `1:1` (model returns 2048×2048).
3. Run `multi_panel_slice.py` on the output.
4. Visually verify one panel; if a seam color band still leaks through (rare), bump the band detection threshold in the script.
5. Publish.
