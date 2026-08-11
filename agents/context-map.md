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
| [standards/_rule-format.md](../standards/_rule-format.md) — how to read every rule | ✅ |
| [agents/ai-agent-standards.md](ai-agent-standards.md) — binding agent behavior | ✅ (seed) |
| [governance/waivers.md](../governance/waivers.md) — what agents may and may not do about exceptions | ✅ |
| [standards/coding.md](../standards/coding.md), [standards/git.md](../standards/git.md), [standards/testing.md](../standards/testing.md), [standards/documentation.md](../standards/documentation.md) | ✅ |
| [standards/security.md](../standards/security.md), [standards/observability.md](../standards/observability.md) | ✅ |
| [checklists/definition-of-done.md](../checklists/definition-of-done.md) — completion gate (AGENT-010) | ✅ |

## Conditional set by task type

Load in addition to the always-applicable set. Documents not yet authored are listed so routing is
stable from day one; until they exist, the engineering principles plus project ADRs govern
([governance/how-to-use.md](../governance/how-to-use.md) §4).

| Task touches… | Load | Available |
|---|---|---|
| Module/service structure, cross-component interfaces | [standards/architecture.md](../standards/architecture.md), [standards/application.md](../standards/application.md) | ✅ |
| Runtime behavior: external calls, state, config, flags | [standards/application.md](../standards/application.md) | ✅ |
| Reviewing a pull request | [checklists/code-review.md](../checklists/code-review.md) | ✅ |
| An API contract | [standards/api.md](../standards/api.md) (+ trigger `public-api` rules) | ✅ |
| Schema, migrations, persisted data | [standards/database.md](../standards/database.md) | ✅ |
| Auth, secrets, PII, uploads, external surface | [security.md](../standards/security.md) §2 triggers → [checklists/security-review.md](../checklists/security-review.md); threat model per SEC-027 → [templates/threat-model.md](../templates/threat-model.md) | ✅ |
| Browser UI | [standards/web.md](../standards/web.md) | ✅ |
| Mobile UI | [standards/mobile.md](../standards/mobile.md) — stub; `mobile` profile may not be declared until its activation trigger fires | 🧊 stub |
| Pipelines, releases, deployment, environments | [standards/ci-cd.md](../standards/ci-cd.md), [standards/infrastructure.md](../standards/infrastructure.md) | ✅ |
| Infrastructure as code, containers, backup/DR, cost | [standards/infrastructure.md](../standards/infrastructure.md) | ✅ |
| Incidents, runbooks, on-call artifacts | [standards/operations.md](../standards/operations.md), [checklists/incident-response.md](../checklists/incident-response.md), [templates/runbook.md](../templates/runbook.md), [templates/postmortem.md](../templates/postmortem.md) | ✅ |
| First production deploy / major release | [checklists/production-readiness.md](../checklists/production-readiness.md) | ✅ |
| Repository creation or layout | [standards/repository.md](../standards/repository.md), [checklists/new-repository.md](../checklists/new-repository.md) | ✅ |
| The playbook itself | [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md), [governance/change-process.md](../governance/change-process.md) | ✅ |

To determine which checks are automated versus which need human approval for any rule, consult the
[enforcement matrix](../governance/enforcement-matrix.md). Deviation reporting: AGENT-009 via the
`## Standards deviations` PR section ([templates/pull-request.md](../templates/pull-request.md)).

## Profile resolution

A project's profile tags (declared in its `CLAUDE.md`; registry in
[standards/_rule-format.md](../standards/_rule-format.md) §4) filter every loaded standard: a rule
applies when its `Applies to` field contains `all`, one of the project's profile tags, or a trigger
tag raised by the change at hand. A project without `mobile` in its profile never loads
`standards/mobile.md` at all.

## Security gates — when they fire (mechanical, not judgment)

- **Security review required:** the change matches any SEC-026 trigger
  ([security.md](../standards/security.md) §2) — auth changes, new/public entry points, new PII,
  uploads/SSRF/interpreter flows, external integrations, tenant/session/token changes, secret
  handling, classified-data migrations.
- **Threat model required:** new system, or SEC-027 triggers (auth, PII, integration, tenancy)
  not covered by the existing model.
- Security rules are never self-exempted: no invented exceptions (AGENT-007), no disabling
  controls to pass (AGENT-013), no silent downgrades (AGENT-003/005), suppressions only with
  justification (CODE-011) — a security finding is suppressed by waiver or fix, never by edit.

## Deployment authorization boundary (AGENT-015…017)

Agents *prepare* — deployment config, infrastructure changes, CI definitions, container files,
rollback plans, pipeline-failure analysis — always as reviewable artifacts (AGENT-015). Agents
never silently touch production infrastructure, production secrets, or deployment controls
(AGENT-016), never disable gates or suppress findings (AGENT-013, SEC-028 waiver path), and every
prepared change that needs human authorization is explicitly flagged as such in the agent's
output (AGENT-017).

## Escalation paths

- Conflict between equal-precedence documents → stricter reading + report (AGENT-003).
- Ambiguity affecting a mandatory rule → stop and ask (AGENT-004).
- Task requires violating a mandatory rule → halt and report (AGENT-006).
- Playbook silent → project ADRs, then principles, then record an ADR
  ([governance/how-to-use.md](../governance/how-to-use.md) §4).
