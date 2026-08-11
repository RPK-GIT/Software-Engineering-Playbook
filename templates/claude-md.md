<!--
CLAUDE.md template for application/library repositories.
This file is the AI agent's entry point (AGENT-001) and the machine-readable adoption
declaration (governance/how-to-use.md). The `playbook` block below is the authoritative
profile declaration referenced by standards/_rule-format.md §4 - keep it parseable exactly
as shown. Delete all comments.
-->

# CLAUDE.md — Project Name

## Playbook adoption

```yaml
playbook:
  repository: https://github.com/RPK-GIT/Software-Engineering-Playbook
  version: v0.2.0            # pinned tag - upgrades are deliberate PRs (how-to-use.md §3)
  profile: [web, api-service, uses-database]   # tags from standards/_rule-format.md §4
```

All rules whose applicability matches `all`, a profile tag above, or a trigger raised by your
change apply to this repository. Load them per the playbook's `agents/context-map.md`, starting
from its `CLAUDE.md`.

## Decisions

Project ADRs: [`decisions/`](decisions/) — scan the index before designing; accepted ADRs bind you.
Org-level ADRs live in the playbook repository.

## Commands

<!-- The exact commands an agent needs. Keep them copy-pasteable and current (DOC-002). -->

- Build: `<command>`
- Test: `<command>`
- Lint/format/types: `<command>`
- Run locally: `<command>`

## Project conventions

<!--
Only what an agent cannot infer from the playbook or the code: local naming quirks, directories
with special meaning, things that look wrong but are deliberate (link the ADR).
Do NOT restate playbook rules here (RULE-008).
-->

## Boundaries

<!--
Anything in this repo the agent must not touch without asking (generated dirs, vendored code,
compliance-sensitive paths). Delete if none.
-->
