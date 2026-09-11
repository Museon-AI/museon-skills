# Creator analysis

## Read-only inventory

Discover current Discord commands on demand. Inventory only the confirmed guild and the categories/channels relevant to the Campaign:

- Creator Workspace channels and their creator/member mapping;
- messages, attachments, threads, and explicit reactions needed to understand current state;
- tracker, review, or announcement channels only when they provide Campaign evidence;
- Museon Campaign creator/content records needed to reconcile Discord conversation with performance data.

Do not assume every person in a campaign channel is an onboarded creator. Preserve an explicit `pending campaign membership` state.

## Per-creator facts

For each tracked creator, derive and retain evidence for:

- creator identity and Discord user/channel IDs;
- whether a private Workspace exists;
- agreement signed;
- account supplied;
- onboarding status;
- current stage;
- last creator message time;
- last team message time;
- current waiting party;
- whether the team needs to reply;
- creator's explicit intent;
- recommended next action and a proposed reply;
- video/content status;
- explicit promised date or formal deadline, if any;
- risk reason and evidence timestamp.

Define `Onboarded` as `agreement signed + account supplied` unless the customer confirms another rule.

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

Answer these business questions in a scan-friendly form:

1. How many private Creator Workspaces exist, how many creators are tracked, and how many meet the confirmed onboarding definition?
2. Which creator messages currently await the team, what is each creator's intent, and what response/action is recommended?
3. Which creators appear inactive, who has not replied for more than 24 hours, and who has missed a verified delivery date?

Every count must link back to a named/filtered list in the chosen operations view. Explain numerator/denominator differences, for example `15 tracked / 14 with Workspace = one pending person without a private channel`.

Do not send the recommended replies unless the user separately asks to send them.

