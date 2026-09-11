# Museon Team Agent Plugins & Skills

Museon 团队维护的 Codex / Claude Code 插件与独立 skills。仓库公开用于团队分发和协作；任何客户数据、Bot token、API key、授权文件或本地 `.env` 都不得提交。

## 目录

```text
.
├── .agents/plugins/marketplace.json       # Codex marketplace
├── .claude-plugin/marketplace.json        # Claude Code marketplace
├── plugins/                               # 可安装插件
│   └── discord-campaign-ops/
│       ├── .codex-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       └── skills/discord-campaign-ops/
└── skills/                                # 可单独引用的通用 skills
```

## 一键安装 Codex 插件

复制执行下面一行，然后开启一个新的 Codex 会话：

```bash
codex plugin marketplace add Museon-AI/museon-skills --ref main && codex plugin add discord-campaign-ops@museon-team
```

如果已经添加过 marketplace，先刷新再重新安装：

```bash
codex plugin marketplace upgrade museon-team
codex plugin add discord-campaign-ops@museon-team
```

也可以在 Codex CLI 输入 `/plugins`，从 `Museon Team` marketplace 安装。

## Claude Code

```bash
claude plugin marketplace add Museon-AI/museon-skills
claude plugin install discord-campaign-ops@museon-team
```

## Discord Campaign Ops

`discord-campaign-ops` 用于把 Discord Creator Workspace、Museon Campaign、运营看板和定时更新串成一个可复用流程。它默认：

- 引导安装并授权 `museoncli`，明确工作区和 Campaign；
- 使用 `discord-mcp-cli` 按需发现 Discord 命令，不把完整工具目录塞进上下文；
- 先只读分析，再按确认后的模板建立运营视图；
- 推荐每小时增量更新，但创建 automation 前必须询问；
- 询问是否创建每日自动日报，并先让用户确认日报格式、时间、时区和投递位置。

Bot token 不随插件分发。运营人员应通过线下渠道获得 token，并只保存在本地环境或组织批准的 secret store 中。详见插件 skill 的初始化说明。

## 贡献约定

- 可安装能力放在 `plugins/<plugin-name>/`；独立 skill 放在 `skills/<skill-name>/`。
- 插件名和 skill 名使用 kebab-case。
- 同时支持 Codex 与 Claude Code 的插件，应维护两个 marketplace 与两个 plugin manifest，并让二者引用同一份 `skills/` 内容。
- 不提交 secret、客户标识、Discord 消息、私人频道名、真实日报截图或导出的业务数据。
- 新增或修改插件后，分别运行对应平台的 validator，并用全新会话验证 skill 可被发现。

