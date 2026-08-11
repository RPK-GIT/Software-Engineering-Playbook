# Software Engineering Playbook

The single source of truth for how we build, ship, and run production software — across projects,
platforms, and technology stacks, consumable by humans and AI coding agents alike.

**Status: COMPLETE — v4.0.0, all six phases done; maintenance mode.** 263 rules across 17
standards; backend/API/service/library/web development fully supported; mobile trigger-gated.
Self-CI enforces the playbook's own governance invariants on every change
([ADR-0002](decisions/0002-github-actions-for-playbook-self-ci.md)). Full status, guarantees, and
limitations: [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md) "Final status".

## How this repository is organized

Every document belongs to exactly one class ([PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md) §1):

| Class | Answers | Where |
|---|---|---|
| **Principles** | Why we work this way | [principles/](principles/engineering-principles.md) |
| **Standards** | What is required — identified, testable rules | `standards/`, [agents/ai-agent-standards.md](agents/ai-agent-standards.md) |
| **Decisions** | What we chose in a context, and why | [decisions/](decisions/README.md) |
| **Instruments** | How standards get applied — checklists, templates, routing | `checklists/`, `templates/`, [agents/context-map.md](agents/context-map.md) |
| **Governance** | How the playbook itself changes | [governance/](governance/change-process.md) |

The one habit that keeps this repository healthy: **a rule lives in exactly one place, under one
ID; everything else cites it.** (Rules RULE-003…RULE-008 in
[standards/_rule-format.md](standards/_rule-format.md).)

## Precedence in one paragraph

A **MUST** binds everything and is lifted only by an approved [waiver](governance/waivers.md). An
ADR may resolve a **SHOULD** its own way with a recorded justification. Derived documents may add
strictness, never remove it. Principles break ties where standards are silent. Full model:
[PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md) §2.

## Start here

| You are… | Read |
|---|---|
| **Adopting the playbook for a project** | [governance/how-to-use.md](governance/how-to-use.md) |
| **An AI coding agent** | [CLAUDE.md](CLAUDE.md) → [agents/context-map.md](agents/context-map.md) |
| **Looking for a specific document** | [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md) |
| **Proposing a change to a standard** | [governance/change-process.md](governance/change-process.md) + [templates/rfc.md](templates/rfc.md) |
| **Recording a decision** | [decisions/README.md](decisions/README.md) + [templates/adr.md](templates/adr.md) |
| **Understanding the design** | [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md) |

## Versioning

Semantic Versioning via annotated git tags — MAJOR for breaking changes to mandatory standards,
MINOR for backward-compatible additions, PATCH for editorial changes. `v1.0.0` arrives when
Phases 1–3 are complete and application development may begin. Policy:
[governance/change-process.md](governance/change-process.md) §2.
