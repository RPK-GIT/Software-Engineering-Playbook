# Agent Context Map

> **Class:** Instrument · **Status:** Active — **seed** (completed and tuned in Phase 6)
> Routing only — this file defines no rules (RULE-007). It answers one question: *given this task
> in this project, which playbook files does an agent load?* Binding agent behavior:
> [ai-agent-standards.md](ai-agent-standards.md).

## Reading order (AGENT-001, AGENT-002)

1. **Project repo `CLAUDE.md`** — pinned playbook version, profile tags, project ADR index location.
2. **Playbook `CLAUDE.md`** — routes here.
3. **Always-applicable set** (below).
4. **Conditional set** — resolved from the project's profile tags and the task type (below).
5. **ADR scan** — the project's `decisions/` index, then org [decisions/README.md](../decisions/README.md),
   for accepted decisions touching the affected area.

## Always-applicable set (any task, any profile)

| Document | Available |
|---|---|
| [standards/_rule-format.md](../standards/_rule-format.md) — how to read every rule | ✅ now |
| [agents/ai-agent-standards.md](ai-agent-standards.md) — binding agent behavior | ✅ now (seed) |
| [governance/waivers.md](../governance/waivers.md) — what agents may and may not do about exceptions | ✅ now |
| `standards/coding.md`, `standards/git.md`, `standards/testing.md`, `standards/documentation.md` | Phase 2 |
| `standards/security.md`, `standards/observability.md` | Phase 3 |
| `checklists/definition-of-done.md` — completion gate | Phase 2 |

## Conditional set by task type

Load in addition to the always-applicable set. Documents not yet authored are listed so routing is
stable from day one; until they exist, the engineering principles plus project ADRs govern
([governance/how-to-use.md](../governance/how-to-use.md) §4).

| Task touches… | Load | Available |
|---|---|---|
| Module/service structure, cross-component interfaces | `standards/architecture.md`, `standards/application.md` | Phase 2 |
| An API contract | `standards/api.md` (+ trigger `public-api` rules) | Phase 3 |
| Schema, migrations, persisted data | `standards/database.md` | Phase 3 |
| Auth, secrets, PII, external surface | `checklists/security-review.md` (+ trigger `handles-pii` rules) | Phase 3 |
| Browser UI | `standards/web.md` | Phase 4 |
| Mobile UI | `standards/mobile.md` | Phase 4 (stub until triggered) |
| Pipelines, releases, environments | `standards/ci-cd.md`, `standards/infrastructure.md` | Phase 5 |
| Incidents, runbooks, on-call artifacts | `standards/operations.md`, `checklists/incident-response.md` | Phase 5 |
| Repository creation or layout | `standards/repository.md`, `checklists/new-repository.md` | Phase 2 |
| The playbook itself | [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md), [governance/change-process.md](../governance/change-process.md) | ✅ now |

## Profile resolution

A project's profile tags (declared in its `CLAUDE.md`; registry in
[standards/_rule-format.md](../standards/_rule-format.md) §4) filter every loaded standard: a rule
applies when its `Applies to` field contains `all`, one of the project's profile tags, or a trigger
tag raised by the change at hand. A project without `mobile` in its profile never loads
`standards/mobile.md` at all.

## Escalation paths

- Conflict between equal-precedence documents → stricter reading + report (AGENT-003).
- Ambiguity affecting a mandatory rule → stop and ask (AGENT-004).
- Task requires violating a mandatory rule → halt and report (AGENT-006).
- Playbook silent → project ADRs, then principles, then record an ADR
  ([governance/how-to-use.md](../governance/how-to-use.md) §4).
