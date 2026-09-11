# Setup and access

## Run Museon and Discord setup in parallel

Do not finish Discord setup first and only then discover the business scope. Begin both tracks together, stopping at any human authorization boundary.

### Museon track

1. Check whether `museoncli` or its `museon` alias is available.
2. If absent, direct the user to the latest stable artifact on the official [Museon CLI releases page](https://github.com/Museon-AI/museon-cli/releases). Prefer `uv tool install <exact-release-wheel-url>` when `uv` and a supported Python are already available. Do not hardcode a version, install a mutable branch, or replace Python/package-manager tooling without approval.
3. Verify the installed version and inspect current auth commands with CLI help.
4. Start device authorization. Show the complete verification URL produced by the CLI, never a raw device code, and let the user finish authorization in their browser.
5. Finish the auth wait, list workspaces, and select the explicit customer workspace.
6. Search relevant Campaign collections by the customer/campaign name. Use current schemas and help for both the creative Campaign and campaign-monitor surfaces when the business object is ambiguous.
7. If multiple results are plausible, no result is clear, or the Discord server name does not match exactly, ask the customer which workspace and Campaign to use.

Before a strategy, audit, or onboarding task, list the current Museon business skills and load only the relevant one.

### Discord track

1. Require Node.js 22.12 or later and install the current `@discord-mcp/cli` package if `discord-mcp` / `discord-mcp-cli` is absent.
2. Tell the operator to place the separately supplied token in their approved local environment. Expected shape for the upstream CLI is `DISCORD_TOKEN="Bot ..."`; do not inspect or echo its value.
3. Create a caller-owned Discord profile with `discord-mcp setup`. Inspect help first and select:
   - a named profile;
   - the verified bot identity;
   - the exact guild boundary;
   - preview or read-only behavior during initialization.
4. Run the CLI's online doctor/access check and read-only smoke test.

Profiles may store only non-secret configuration. The token stays in the launch environment or secret store.

## Bot installation link

If the bot has not joined the guild, construct a standard Discord bot authorization URL from the verified Application ID:

```text
https://discord.com/oauth2/authorize?client_id=<APPLICATION_ID>&permissions=<PERMISSION_BITSET>&scope=bot%20applications.commands
```

The server administrator opens this link, selects the target server, and approves. A callback or redirect URL is not required for this bot-install flow.

Prefer least privilege:

- Analysis only: View Channels and Read Message History.
- Workspace operations: add only the required Manage Channels, Send Messages, Embed Links, or Attach Files permissions.
- Administrator: use only when the customer explicitly chooses that broad scope.

Guild-level permissions do not automatically grant access to private Creator Workspace channels. The relevant category or channel overwrite must include the bot role. After approval, verify actual access by reading the intended channel; guild membership alone is insufficient.

When Discord returns 403, inspect bot identity, guild allowlist, role hierarchy, and category/channel overwrites. Do not rotate the token as a generic fix.

## Mapping checkpoint

Record and show the user the confirmed, non-secret mapping:

```text
Customer: <name>
Museon workspace: <name + id>
Museon Campaign: <name + id + object type>
Discord guild: <name + id>
Creator Workspace category/categories: <name + id>
Discord profile: <local non-secret profile name>
```

Ask the customer to resolve any ambiguous field before analysis or automation proceeds.
