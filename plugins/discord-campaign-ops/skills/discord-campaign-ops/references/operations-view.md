# Operations view

## Choose the destination

Ask where the user wants the durable operations view. Offer Lark Base as a recommended reusable template, not a mandatory format. A spreadsheet, database, project tool, or concise report is acceptable when it better matches the customer's workflow.

Confirm the destination, audience, write access, and whether the user wants a dashboard before creating anything.

## Lark Base template

Suggested fields:

| Group | Fields |
| --- | --- |
| Identity | Campaign, creator name, Discord user ID, channel ID, Workspace link |
| Onboarding | Workspace created, agreement signed, account supplied, onboarded |
| Conversation | last creator message, last team message, waiting party, reply needed, creator intent |
| Action | suggested action, suggested reply, owner |
| Delivery | current stage, video status, explicit due date, overdue evidence |
| Risk | creator no reply >24h, team no reply >24h, risk reason, updated at |

Use a stable upsert key such as `Campaign ID + Discord user ID`, with channel ID as a reconciliation key. Hourly jobs must update records, not append duplicates.

Recommended filtered table views:

- 全部 Creator;
- PM 待处理;
- Creator 未回复 >24h;
- 团队未回复 >24h;
- 已完成 Onboarding;
- 交付风险 / 已确认逾期.

## Dashboard rules

The dashboard is a decision surface, not a wall of cards.

- Put only clearly named totals and meaningful distributions on the dashboard.
- Show the subject in every metric: `Creator 未回复 >24h`, never `超过 24 小时`.
- Use exact labels such as `追踪 Creator（含待确认）` and `已建私人 Workspace`.
- Explain count gaps through a filtered list.
- Do not turn a list of names into a count chart where every bar is `1`.
- Put names, intents, evidence, suggested replies, and owners in table views rather than oversized text cards.
- Create components serially and verify each one.
- If the user asks for the dashboard first, verify the actual block/tab order through the current Base API before moving it. Missing reorder permission must be reported; do not claim success after only creating the dashboard.

For a non-Lark destination, preserve these semantics and filtered views while adapting the native schema and layout.

