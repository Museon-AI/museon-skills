# TikTok Slideshow Tagging System

Read this reference before analyzing or selecting TikTok slideshow videos for a MuseOn pitch deck. Use it to classify **Format** (how images relate to each other) and **Content Angle** (why the content persuades or attracts viewers).

## Candidate Fields

Capture these fields for every candidate before filtering.

| Field | Description |
| --- | --- |
| `video_id` | Stable TikTok video identifier or canonical URL. |
| `source_path` | Keyword search, competitor account, client-owned content, or client-provided reference. |
| `matched_keywords` | Keywords that surfaced this candidate. |
| `keyword_hit_count` | Number of distinct keywords that found the same video. |
| `creator_handle` | TikTok account handle. |
| `url` | Direct video URL. |
| `views` | View count, if visible. |
| `likes` | Like count, if visible. |
| `saves` | Save count, if visible. Use this for conversion-priority ranking. |
| `comments` | Comment count, if visible. |
| `slide_count` | Number of slideshow images. Exclude if greater than nine. |
| `visible_logo_or_product` | Product logo/brand visible in the content. Exclude if it belongs to another product and cannot be adapted. |
| `format_tag` | One Format tag from the taxonomy below. |
| `content_angle_tag` | One Content Angle tag from the taxonomy below. |
| `exclusion_reason` | Reason for rejecting a candidate, if rejected. |
| `adaptation_note` | How this reference can be adapted for the client's product scenario. |

## Exclusion Rules

Reject a candidate immediately if it matches any rule in this table.

| Rule | Why It Is Excluded |
| --- | --- |
| Another product's logo is central to the slideshow. | The reference is too brand-specific and may look copied. |
| Slideshow contains more than nine images. | Too long for the desired reusable deck examples. |
| It is a news event or time-sensitive trend. | It cannot be reliably reused later. |
| The content is too abstract for the agent to understand. | Cannot produce a grounded adaptation. |
| Format is `Mixed`. | The structure is not clean enough to replicate. |
| Content Angle is `Mood / Aesthetic`, `Inspirational`, `Emotional Resonance`, `Meme`, or `Abstract`. | These angles are weaker for MuseOn's product pitch-deck adaptation workflow. |

## Format Decision Tree

Format is determined by the relationship between images. Ask the questions in order and assign exactly one tag.

### Q1. Do the images have sequence dependency?

If the viewer must consume the slides in order, choose among these tags.

| Condition | Tag | Definition |
| --- | --- | --- |
| The goal is to help the viewer perform an action. | `Step-by-step` | A procedural tutorial or how-to sequence. |
| The goal is to help the viewer understand an idea. | `Explainer` | A logical explanation, concept breakdown, or educational sequence. |
| The slides advance a narrative or event chain. | `Story` | A storyline with beginning, middle, and end. |

If there is no sequence dependency, continue to Q2.

### Q2. Is there an explicit comparison intent?

| Condition | Tag | Definition |
| --- | --- | --- |
| Two or more objects are compared on the same dimensions. | `Comparison` | Side-by-side or before/after/option comparison where contrast is the main structure. |

If there is no comparison intent, continue to Q3.

### Q3. What is the organization unit of the slideshow?

| Condition | Tag | Definition |
| --- | --- | --- |
| Each image is one independent item. | `List` | A collection of tips, tools, reasons, mistakes, examples, or recommendations. |
| Each image pair or unit is a question followed by an answer. | `Q&A` | Question-response structure, FAQ, or myth-answer pattern. |
| Images mainly display visuals without information dependency. | `Showcase` | Visual presentation of product, result, style, or portfolio. |
| Multiple structures compete or none fits clearly. | `Mixed` | Reject unless the user explicitly asks to keep it. |

## Content Angle Decision Tree

Content Angle is determined by what makes the content compelling. Ask the steps in order and assign exactly one closest tag.

### Step 1. Does it deliver useful information or prove a fact?

| Condition | Tag | Keep? |
| --- | --- | --- |
| It identifies a problem and offers a solution. | `Problem-Solution` | Keep |
| It shows before/after, metrics, or evidence of improvement. | `Proof of Results` | Keep |
| It helps the viewer choose between A/B options. | `Review & Comparison` | Keep |
| It teaches a concept, skill, or framework. | `Educational Value` | Keep |

If none applies, continue to Step 2.

### Step 2. Does it build trust through people, social proof, or identity?

| Condition | Tag | Keep? |
| --- | --- | --- |
| A major creator, celebrity, or authority recommends it. | `Influencer Endorsement` | Keep |
| An ordinary user tells a personal experience. | `User Story / Testimonial` | Keep |
| It explicitly names a specific group or identity. | `Identity / Belonging` | Keep |
| It embeds the product or idea into an aspirational lifestyle. | `Lifestyle Integration` | Keep |

If none applies, continue to Step 3.

### Step 3. Does it trigger impulse, curiosity, or emotion?

| Condition | Tag | Keep? |
| --- | --- | --- |
| It withholds information to make viewers curious. | `Curiosity Hook` | Keep |
| It states a counterintuitive or contrarian claim. | `Contrarian` | Keep |
| It creates scarcity, deadline pressure, or urgency. | `Scarcity / Urgency` | Keep |
| It is primarily a joke or internet humor. | `Meme` | Exclude |
| It mainly says “this is exactly how I feel.” | `Emotional Resonance` | Exclude |
| It mainly gives encouragement or warmth. | `Inspirational` | Exclude |
| It relies on beautiful mood or visual style. | `Mood / Aesthetic` | Exclude |
| It is intentionally unclear and discussion-driven. | `Abstract` | Exclude |

If none applies, continue to Step 4.

### Step 4. Is it mainly behavior, documentation, or trend participation?

| Condition | Tag | Keep? |
| --- | --- | --- |
| It documents a day, process, or routine without a strong teaching structure. | `Documentation` | Keep if product fit is strong. |
| It uses a platform-wide template or trend. | `Trending` | Keep only if not time-sensitive and easy to adapt. |
| None fits. | Re-evaluate from Step 1 and choose the closest tag. | Depends on final tag. |

## Ranking Guidance

After exclusion and tagging, rank candidates with the following priorities.

| Priority | Ranking Logic |
| --- | --- |
| Client wants conversion | Sort primarily by saves, because saves indicate intention to return, buy, or use. |
| Client wants exposure | Sort primarily by views, because views represent reach. |
| Client wants both or did not specify | Balance views and saves, then use product-fit judgment. |
| Diversity | Avoid selecting five references with the same Format × Content Angle combination. |
| Scenario fit | Prefer videos that can be mapped cleanly to a concrete scenario from the scenario matrix. |
| Client constraints | Exclude Formats or Angles the client already tried and disliked. |

## Selection Output

For each selected candidate, produce a short deck-ready row.

| Field | Expected Content |
| --- | --- |
| Reference | TikTok URL or creator + video ID. |
| Metrics | Views, saves, likes, or the best visible metrics. |
| Format | One Format tag. |
| Content Angle | One Content Angle tag. |
| Why it won | One sentence explaining the data and persuasion logic. |
| Adaptation | One sentence explaining how MuseOn should adapt it to the client's product and scenario. |
