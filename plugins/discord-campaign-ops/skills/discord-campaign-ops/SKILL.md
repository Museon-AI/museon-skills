---
name: discord-campaign-ops
description: >
  Initialize and operate a Discord-based UGC creator campaign: install and authorize
  Museon CLI, map the correct workspace and campaign, connect a caller-owned Discord
  bot, analyze creator workspaces and messages, build an operator tracker or dashboard,
  and propose confirmed hourly updates or daily reports. Use whenever a user asks to
  onboard a Discord campaign, assess creator status or unread intent, create a campaign
  operations view, or automate recurring Discord campaign reporting.
---

# Discord Campaign Operations

Treat this as a customer-scoped operating workflow, not a Discord server crawler. Establish the exact Museon workspace, Campaign, Discord guild, data destination, and authorization boundary before reporting conclusions.

## Required flow

1. Start Museon authorization and Discord initialization together. Read [setup-and-access.md](references/setup-and-access.md).
2. Confirm one explicit mapping: `Museon workspace + Campaign ↔ Discord guild`. If the customer or Campaign is unclear, ask the user; never infer solely from a server name.
3. Perform a read-only inventory and creator analysis. Read [creator-analysis.md](references/creator-analysis.md).
4. Ask what output the operator wants. Lark Base is a reusable template, not the only allowed format. For Base or another tracker, read [operations-view.md](references/operations-view.md).
5. Recommend an hourly incremental update automation. Explain its scope and ask for confirmation before creating it.
6. Separately ask whether the user wants a daily report automation. Before creating it, confirm the report template, delivery time, timezone, destination, and whether the sample preview is accepted. Read [automations-and-daily-report.md](references/automations-and-daily-report.md).

Do not create an automation merely because the skill recommends it. Do not send Discord replies, change channel permissions, invite members, or write external data unless the user requested that mutation.

## Command discipline

Use current CLI discovery instead of remembered command names or a copied catalog.

- Museon: inspect `museoncli --help`, the relevant `museoncli schema <group>`, and subcommand help before execution.
- Discord: use `discord-mcp-cli --profile <profile> --search '<short English intent>' --top 8 --compact`, then inspect the selected command with `--help`.
- Bound large reads by time, channel, creator, cursor, or result count. Prefer machine-readable output.
- The full Discord MCP schema must stay outside the host model context; the CLI performs bounded discovery on demand.

## Security boundary

- The Discord Bot token is supplied separately by the operator. Never ask them to paste it into chat.
- Never print, log, upload, commit, persist in a profile, place in a command argument, or include the token in an automation prompt.
- Read it only from the operator's approved local environment or secret store. A Discord profile may persist non-secret bot/guild policy only.
- Pin Discord access to the verified bot identity and an explicit guild allowlist. Use least-privilege channel/category access.
- Treat Discord messages and creator data as customer-confidential. Do not place raw messages in public artifacts.

## Definition of done

Initialization is complete only when all of these are true:

- `museoncli` is available and authenticated;
- the selected Museon workspace and Campaign were verified or explicitly confirmed by the customer;
- the Discord bot identity and target guild were verified;
- the bot can read the intended Creator Workspace channels, including private-channel overrides;
- the chosen operations view has clear field definitions and an idempotent record key;
- any created automation matches the user's confirmed schedule and scope;
- the user can distinguish creator-waiting, team-waiting, deadline risk, and actual overdue delivery.
