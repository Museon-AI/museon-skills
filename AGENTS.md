# Repository instructions

This repository distributes team-owned Codex and Claude Code plugins and standalone skills.

- Put installable packages under `plugins/<plugin-name>/` and standalone skills under `skills/<skill-name>/`.
- Keep Codex and Claude Code manifests aligned when a plugin supports both products. Do not duplicate the skill body.
- Never commit credentials, customer data, Discord messages, private channel or guild names, authorization artifacts, or production exports.
- Skills must discover current CLI schemas and help at runtime instead of copying large or unstable command catalogs.
- Any workflow that creates automations, sends messages, changes permissions, or writes external data must obtain the user's explicit confirmation at the relevant boundary.
- Validate the changed plugin and every changed skill before delivery.

