# Automations and daily report

## Hourly update

Recommend an hourly automation after the first successful read and operations-view setup, but ask the user to confirm before creating it.

Before confirmation, state exactly:

- Campaign and Discord guild in scope;
- destination being updated;
- schedule and timezone;
- that the job reads message deltas and Campaign performance data;
- that it updates records idempotently;
- whether it sends notifications;
- that it does not send Discord replies or change permissions.

Use current `museoncli schema routines` and routine subcommand help. Read existing routines first to avoid duplicates. Prefer a draft when the platform supports review. Create or accept only after approval, then verify the active trigger, owner, next run, and destination.

The hourly routine must:

1. Read only changes since a durable per-channel watermark.
2. Reconcile creator/channel records by stable IDs.
3. Recompute the current waiting party and separate creator-waiting from team-waiting.
4. Recompute `>24h` only from message timestamps and the correct waiting party.
5. Mark overdue only from an explicit due date or dated promise.
6. Re-evaluate chat-derived warm-up candidates and whether their Campaign removal is
   pending or confirmed; never infer removal only because an old message asked for it.
7. Update the same records without duplication.
8. Store only non-secret state such as watermarks, Campaign ID, guild ID, and destination identifiers.
9. Stay quiet when nothing actionable changed unless the user requested routine updates; surface failures or required human action.

Never place the Discord token or Museon credential in the routine prompt or persisted state. Use the runtime's approved secret injection.

## Daily report confirmation gate

Always ask whether the user wants a daily report automation. Do not treat agreement to hourly sync as agreement to daily reporting.

Confirm all of the following before creating it:

- daily delivery time;
- timezone;
- destination and recipients;
- reporting window;
- Template A or Template B below, or a user-provided exact format;
- whether the rendered preview is accepted.

The two templates are alternatives derived from the supplied references. Do not merge them or change their section order without confirmation.

### Template A — compact narrative

```text
<Campaign>日报 <M.D-M.D>

今日onboard <N> 位；总共 <N> 位 creator
其中 <N> 位处于 <阶段列表>
已催促其他不活跃 creator

<统计窗口>内 <N> 位 creator 发布 <N> 条帖子，<N> 条 unique 视频
破千：<N> 条

Top vids

<URL> - <creator> <views>
<URL> - <creator> <views>
```

### Template B — structured sections

```text
<Campaign> 日报 | <MMDD>
1. Creator & 账号
• 社群目前 <N> 位可用 creator
• onboard <N> 位，新增 <N> 位
• 已建号 <N> 位、posting <N> 位、warm-up <N> 位
2. 内容产出
• <MMDD> 共新增 <N> 条 Posts
• 累计获得约 <views> Views
• 1K+ Posts 共 <N> 条
3. Top Performing Videos
<creator> / <platform> / <views> Views
<URL>
4. 项目总体进度
• 累计发布 <N> 条 Posts
• 累计约 <views> Views
• <需要 PM 关注的推进结论>
```

## Report evidence rules

- Preserve the confirmed title style, section order, bullet style, blank lines, link order, and metric labels.
- Distinguish daily/window metrics from cumulative metrics.
- Use Campaign performance data for post and view counts, reconciled with Discord onboarding state.
- Report onboarding, account supplied, account authorized, warm-up complete, and ready
  for formal production as separate stages when those facts are available.
- Exclude identified warm-up videos from formal Campaign delivery and performance totals
  unless the customer confirms that they count. If a warm-up candidate is still present
  in Campaign data, show raw totals, adjusted totals, and the pending cleanup item.
- Count unique videos by the customer's confirmed content identity rule; do not equate posts with unique videos by default.
- Rank Top videos from observable synchronized data and include creator, platform, views, and direct URL in the confirmed format.
- Do not invent missing values. Mark incomplete synchronization and its cutoff time.
- Write for the PM who must choose the next action. Surface Creator counts and operating
  health, creators who need intervention, warm-up cleanup, delivery pace, and
  top-performing videos whose hook/script/format deserves review or reuse.
- Never present Creator capacity as definitively sufficient or insufficient from
  operational data alone. Make that assessment only with PM-provided customer goals,
  delivery requirements, timeline, Campaign stage, and constraints, and present it for
  PM confirmation. Otherwise ask for context and limit the report to observed health.
- Preview one report using current data, show it to the user, and obtain explicit acceptance before activating the daily routine.

After creation, verify the schedule, timezone, recipient, next run, and routine status. Keep hourly state refresh and daily message delivery as separate routines so either can be paused independently.
