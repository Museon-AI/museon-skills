# Operations view

## Choose the destination

Ask where the user wants the durable operations view. Offer Lark Base as a recommended reusable template, not a mandatory format. A spreadsheet, database, project tool, or concise report is acceptable when it better matches the customer's workflow.

Confirm the destination, audience, write access, and whether the user wants a dashboard before creating anything.

## Lark Base template

Suggested fields:

| Group | Fields |
| --- | --- |
| Identity | Campaign, Museon Creator ID/name, Discord user ID, channel ID, Workspace link, mapping confidence/evidence |
| Onboarding | canonical Campaign membership and onboarding status |
| Authorization | canonical Creator/account link and authorization status |
| Conversation | last creator message, last team message, waiting party, reply needed, creator intent |
| Action | suggested action, suggested reply, owner |
| Delivery | warm-up status, production readiness, current stage, video status/type, warm-up candidate, Campaign removal status, explicit due date, overdue evidence |
| Performance | raw posts/views, excluded warm-up posts/views, adjusted posts/views, top-video evidence |
| Risk | creator no reply >24h, team no reply >24h, risk reason, updated at |

Use `Campaign ID + Museon Creator ID` as the stable upsert key. Persist Discord user and
channel IDs only after identity resolution. Keep unresolved private channels in a
separate mapping queue keyed by `guild ID + channel ID`; do not create duplicate Creator
records from fuzzy matches. Hourly jobs must update records, not append duplicates.

Recommended filtered table views:

- 全部 Creator;
- Discord 频道待关联;
- PM 待处理;
- Creator 未回复 >24h;
- 团队未回复 >24h;
- 已完成 Onboarding;
- 待授权 / 授权异常;
- Warm-up 中 / 可正式生产;
- Warm-up 帖子待移除;
- 交付风险 / 已确认逾期.

## Dashboard rules

The dashboard is a decision surface, not a wall of cards.

- Put only clearly named totals and meaningful distributions on the dashboard.
- Show the subject in every metric: `Creator 未回复 >24h`, never `超过 24 小时`.
- Use exact labels such as `追踪 Creator（含待确认）` and `已建私人 Workspace`.
- Explain count gaps through a filtered list.
- Do not turn a list of names into a count chart where every bar is `1`.
- Put names, intents, evidence, suggested replies, and owners in table views rather than oversized text cards.
- Lead with PM decisions: Creator headcount and health, production readiness, delivery
  pace, warm-up cleanup, and content winners. Every alert should name the affected
  creators or posts and the proposed owner/action.
- Show raw and adjusted performance when warm-up exclusions change Campaign totals.
- Do not label Creator capacity sufficient or insufficient merely from counts or health.
  That conclusion requires PM-provided customer requirements, delivery goals, timeline,
  Campaign stage, and relevant operating constraints. Without that context, report the
  distribution and health signals, state that capacity sufficiency is unresolved, and
  ask the PM for the missing inputs.
- Create components serially and verify each one.
- If the user asks for the dashboard first, verify the actual block/tab order through the current Base API before moving it. Missing reorder permission must be reported; do not claim success after only creating the dashboard.

For a non-Lark destination, preserve these semantics and filtered views while adapting the native schema and layout.
