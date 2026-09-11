# Discord Campaign Ops

面向 UGC Campaign 运营的 Discord 工作流插件。插件本身不包含 Bot token，也不注册完整 Discord MCP 工具目录；skill 会引导 Agent 安装依赖、完成授权、按需发现命令并建立经用户确认的运营输出和 automation。

主要流程：

1. 并行完成 Museon CLI 授权、工作区选择、Campaign 映射与 Discord Bot 初始化。
2. 只读盘点 Creator Workspace、onboarding、消息等待方、明确意图、视频进度和风险。
3. 根据用户选择建立运营数据载体；Lark Base 是推荐模板之一，不是唯一格式。
4. 推荐每小时增量更新，但创建前询问确认。
5. 询问是否需要每日日报，并严格按用户确认的模板生成和投递。

分析和汇报始终采用 Campaign PM 视角。Museon 数据库提供 Campaign Creator、
onboarding、Creator 链接、授权、帖子和表现等 canonical 状态；Discord 的频道名、
成员和聊天文本用于把私人频道关联到正确 Creator，并补齐 warm-up、沟通意图和
视频进展。插件报告 Creator 数量与运营健康度；只有 PM 提供客户目标、交付要求、
时间和 Campaign 上下文后，才能判断 Creator 是否充足。

完整操作契约见 `skills/discord-campaign-ops/SKILL.md`。
