# Creator analysis

## Read-only inventory

Discover current Discord commands on demand. Inventory only the confirmed guild and the categories/channels relevant to the Campaign:

- Creator Workspace channels and their creator/member mapping;
- messages, attachments, threads, and explicit reactions needed to understand current state;
- tracker, review, or announcement channels only when they provide Campaign evidence;
- Museon Campaign creator/content records needed to reconcile Discord conversation with performance data.

Do not infer onboarding or authorization from Discord membership. First resolve the
private channel to a canonical Museon Creator, then read that Creator's Campaign,
onboarding, account-link, and authorization state from Museon.

## Canonical lifecycle and Discord identity resolution

Creators are usually recruited through direct outreach and join the Discord guild after
an agreement may already have been signed. The Museon database already owns Campaign
Creator membership, onboarding, Creator/account links, and authorization status. Read
those states directly rather than rebuilding them from chat.

The missing association is commonly `private Discord channel ↔ Museon Creator`. Resolve
candidate matches using several signals together:

- private channel name and normalized Creator/display names;
- Discord member display name and username;
- social account handles or profile URLs mentioned in the channel;
- authorization links, video links, and other Creator-specific identifiers in messages;
- surrounding onboarding messages that explicitly name the Creator.

Do not accept a weak name-only match when multiple Creators are plausible. Retain the
candidate, matched signals, confidence, and conflicting signals. Ask the PM to confirm
ambiguous mappings. Once confirmed, persist the stable Museon Creator ID, Discord user
ID, and private channel ID so later runs do not repeat fuzzy matching.

Use the following lifecycle to organize the combined view, but take its modeled states
from Museon and its unmodeled communication or warm-up evidence from Discord:

```text
joined Discord
→ new social account requested
→ new account supplied
→ account added to the Museon Campaign
→ creator authorization link created
→ creator completed account authorization
→ account warm-up
→ ready for formal production
→ video planned / recorded / submitted / published
```

Some steps may overlap. A channel that cannot yet be mapped remains an `unmapped Creator
Workspace`; it is not evidence that a new or non-onboarded Creator exists.

Creator authorization means OAuth authorization of the new social account to Museon or
its approved provider. It is separate from the creator agreement and Discord bot/guild
authorization. Use Museon's Creator link and authorization status as canonical. Chat may
explain a delay or reveal that a user needs help, but it must not replace that status.

Warm-up is account preparation before formal Campaign posting. It can include normal
vertical browsing and interaction and may include warm-up videos. Do not count warm-up
videos as formal Campaign delivery or performance unless the customer explicitly says
they qualify. Distinguish `warming`, `warm-up complete / ready`, and `unknown` from
formal video production stages.

Warm-up video identity is commonly not stored as structured state. Reconstruct it from
the conversation sequence, for example: an operator asks the creator to publish a
warm-up video, the creator shares or confirms the post, and the operator later asks for
that post to be removed from the Campaign. Track these as separate states:

- `warm-up video requested`;
- `warm-up candidate published`, with post URL or observable identity;
- `removal from Campaign pending`;
- `removed from Campaign`, only with explicit confirmation or current Campaign evidence;
- `ambiguous`, when the language or post identity is not sufficient.

A warm-up candidate still present in the Campaign is a PM action item because its views
must not inflate Campaign performance. Exclude confidently identified warm-up posts
from adjusted PM metrics, show both raw and adjusted totals when they differ, and list
ambiguous candidates separately. Do not remove content automatically unless the user
requested that mutation.

## Evidence precedence

The database is the source of truth for Campaign membership, onboarding, Creator/account
links, authorization, posts, and performance. Do not overwrite those facts with chat
inference. Use Discord text analysis for channel-to-Creator identity resolution,
current intent and waiting party, operational explanations, warm-up instructions,
warm-up post identity/removal intent, and video progress that has not yet become a
canonical Campaign record.

- Missing database state for an unmodeled fact means `unknown`, not `not done`.
- Store chat-derived state as an inference with evidence and confidence; never present it
  as a database fact.
- Do not use a chat message saying a link was sent as the authorization status; read the
  canonical authorization record.
- Do not use guild or private-channel membership as onboarding status; read the canonical
  onboarding record after resolving the Creator identity.
- Prefer the latest explicit completion or reversal message over an older request.
- When chat and Museon records conflict, show both timestamps, mark the state as
  conflicting, and recommend verification instead of silently choosing one.
- Every inferred stage must retain a short evidence reference and timestamp.

## Per-creator facts

For each tracked creator, derive and retain evidence for:

- canonical Museon Creator ID plus mapped Discord user/channel IDs and mapping confidence;
- whether a private Workspace exists;
- canonical Campaign membership, onboarding, Creator/account link, and authorization status;
- warm-up status and current stage;
- warm-up post candidates and removal-from-Campaign status;
- last creator message time;
- last team message time;
- current waiting party;
- whether the team needs to reply;
- creator's explicit intent;
- recommended next action and a proposed reply;
- video/content status, distinguishing planned, recorded, submitted, warm-up, and formally published content;
- explicit promised date or formal deadline, if any;
- risk reason and evidence timestamp.

Do not redefine `Onboarded` from Discord messages. Report Museon's onboarding status,
authorization status, warm-up readiness, and formal production readiness as separate
facts.

## Status language

Never show an ambiguous metric such as `超过 24 小时` by itself. Split it into:

- `Creator 未回复 >24h`: the last substantive message is from the team and the creator has not replied for over 24 hours.
- `团队未回复 >24h`: the last substantive message is from the creator and the team has not replied for over 24 hours.

Do not label someone `逾期` without an explicit due date or a clear promise with a date. Without that evidence, use `交付风险` or `存在可见承诺，待确认截止时间`.

Avoid vague values such as `阻塞` and `待确认` without a subject. Use explicit states such as:

- `待 Creator 提供账号`;
- `待团队发送协议`;
- `待 PM 决定是否继续 Campaign`;
- `待确认是否属于该 Campaign`;
- `Creator 排期暂缓`.

## Required summary

Answer these PM questions in a scan-friendly form:

1. What is the current Creator headcount and operating health: how many are in the
   pipeline, authorized, warming, ready, producing, inactive, or blocked?
2. Which creator messages currently await the team, what is each creator's intent, and
   what response/action is recommended?
3. Which creators have not replied for more than 24 hours, missed a verified delivery
   date, or otherwise threaten production capacity?
4. Which warm-up posts are still included in the Campaign, which are ambiguous, and how
   do raw versus adjusted post/view totals differ?
5. What are the observed content and view pace? If the PM has supplied the customer's
   goals, delivery volume, timeline, Campaign stage, and relevant constraints, compare
   against that context and present the capacity decision for PM confirmation. Otherwise
   report health only and ask for the missing context; do not conclude that Creators are
   sufficient or insufficient and do not prescribe recruitment as fact.
6. Which videos materially outperform, what observable hook/script/format appears worth
   inspecting or replicating, and what should the PM decide next?

Every count must link back to a named/filtered list in the chosen operations view. Explain numerator/denominator differences, for example `15 tracked / 14 with Workspace = one pending person without a private channel`.

Do not send the recommended replies unless the user separately asks to send them.
