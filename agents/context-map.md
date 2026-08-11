# Agent Context Map

> **Class:** Instrument · **Status:** Active — **complete** (Phase 6)
> The authoritative navigation map for AI agents: *given this task in this project, what do I
> read?* — answered deterministically, without loading all 46 documents. Routing only: no rules
> are defined here (RULE-007); binding behavior is [ai-agent-standards.md](ai-agent-standards.md).

## Reading order (AGENT-001, AGENT-002)

1. **Project repo `CLAUDE.md`** — pinned playbook version, **profile tags**, project ADR index.
   No profile declared → AGENT-018: request one before profile-dependent work.
2. **Playbook `CLAUDE.md`** — routes here.
3. **ALWAYS READ tier** (below), then the **CONDITIONAL** set for the task, then any
   **TRIGGERED** documents whose triggers fire.
4. **ADR scan** — the project's `decisions/` index, then org
   [decisions/README.md](../decisions/README.md), for accepted decisions touching the affected
   area. Accepted ADRs bind (PLAYBOOK-ARCHITECTURE §2.2).

## Context budget

The goal: minimum required context + complete applicable standards + nothing else.

### ALWAYS READ (every task, every profile — small by design)

| Document | Why |
|---|---|
| [standards/_rule-format.md](../standards/_rule-format.md) §1–2, §4 | How to read any rule; the tag registry |
| [agents/ai-agent-standards.md](ai-agent-standards.md) | Binding agent behavior, AGENT-001…021 |
| [checklists/definition-of-done.md](../checklists/definition-of-done.md) | The completion gate (AGENT-010), profile-filtered |

### CONDITIONAL READ — any implementation task (writing or changing code)

[standards/coding.md](../standards/coding.md) · [standards/testing.md](../standards/testing.md) ·
[standards/git.md](../standards/git.md) · [standards/security.md](../standards/security.md) ·
[standards/observability.md](../standards/observability.md) ·
[standards/documentation.md](../standards/documentation.md)

### CONDITIONAL READ — by task domain (add to the implementation set)

| Task touches… | Add |
|---|---|
| Module/service structure, boundaries, cross-component interfaces | [standards/architecture.md](../standards/architecture.md), [standards/application.md](../standards/application.md) |
| Runtime behavior: external calls, state, config, flags, jobs | [standards/application.md](../standards/application.md) |
| An API contract | [standards/api.md](../standards/api.md) |
| Schema, migrations, persisted data | [standards/database.md](../standards/database.md), [standards/application.md](../standards/application.md) (APP-007), CI-009 in [standards/ci-cd.md](../standards/ci-cd.md) |
| Browser UI | [standards/web.md](../standards/web.md) |
| Mobile UI | [standards/mobile.md](../standards/mobile.md) — stub; `mobile` profile undeclarable until its trigger fires |
| Pipelines, releases, deployment | [standards/ci-cd.md](../standards/ci-cd.md) |
| Infrastructure, IaC, containers, backup/DR, cost | [standards/infrastructure.md](../standards/infrastructure.md) |
| Operational artifacts: runbooks, alerts, on-call | [standards/operations.md](../standards/operations.md), [templates/runbook.md](../templates/runbook.md) |
| Repository creation or layout | [standards/repository.md](../standards/repository.md), [checklists/new-repository.md](../checklists/new-repository.md) |
| Reviewing a pull request | [checklists/code-review.md](../checklists/code-review.md) |
| The playbook itself | [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md), [governance/change-process.md](../governance/change-process.md), `tools/validate.py` (+ AGENT-021) |

Profile filtering applies throughout: a rule binds when its `Applies to` contains `all`, one of
the project's profile tags, or a raised trigger tag (RULE-005 registry). A project without `web`
never loads web.md.

### TRIGGERED READ (loaded when the trigger fires, regardless of task type)

| Trigger | Read |
|---|---|
| Change matches a SEC-026 item (auth, new/public entry point, PII, uploads/SSRF/interpreters, external integration, tenancy/session/secrets, classified-data migration) | [security.md](../standards/security.md) §2 + [checklists/security-review.md](../checklists/security-review.md) |
| SEC-027 item (new system; auth/PII/integration/tenancy change uncovered by the model) | [templates/threat-model.md](../templates/threat-model.md) |
| Decision matches the DOC-003 ADR-trigger list (technology selection, service split, new datastore/mechanism, contract change, security mechanism, pattern deviation, hard-to-reverse) | [templates/adr.md](../templates/adr.md) + stop for approval (AGENT-019) |
| First production deploy / major release | [checklists/production-readiness.md](../checklists/production-readiness.md) |
| Incident declared | [checklists/incident-response.md](../checklists/incident-response.md); afterwards [templates/postmortem.md](../templates/postmortem.md) |
| Blocked by a mandatory rule | [governance/waivers.md](../governance/waivers.md) — draft only (AGENT-007/008) |

### REFERENCE ONLY (look up, never bulk-load)

[governance/enforcement-matrix.md](../governance/enforcement-matrix.md) — is this check automated
or human? · [GLOSSARY.md](../GLOSSARY.md) — term definitions ·
[principles/engineering-principles.md](../principles/engineering-principles.md) — tie-breaks where
standards are silent · [DOCUMENT-INDEX.md](../DOCUMENT-INDEX.md) — inventory ·
[governance/how-to-use.md](../governance/how-to-use.md) — adoption/pinning questions ·
[PLAYBOOK-ROADMAP.md](../PLAYBOOK-ROADMAP.md) — history/status.

## Worked routes (non-normative examples)

- **"Add a database migration"** → implementation set + database.md + application.md (APP-007) +
  ci-cd.md (CI-009, CI-008) → triggers: PII/sensitive data in the schema? → security-review
  checklist (SEC-026 item 8) → DoD data section before claiming done.
- **"Fix an XSS in the comment renderer"** → implementation set (security.md already in it) +
  web.md (WEB-021) + api.md if the contract changes → SEC-026 item 4 fires → security-review
  checklist + threat-model currency check (SEC-027) → regression test required (TEST-002).

## When applicability cannot be determined

1. Profile missing or unparseable → **AGENT-018**: request the declaration; only `all`-tagged
   work proceeds meanwhile.
2. Task doesn't match any route above → load the implementation set plus the nearest domain
   set — over-inclusion is safe, under-inclusion is not (the stricter-reading instinct of
   AGENT-003) — and report the routing gap as a playbook defect.
3. Genuine ambiguity about whether a mandatory rule applies → **AGENT-004**: stop and ask.

## Security gates — when they fire (mechanical, not judgment)

- **Security review:** any SEC-026 trigger ([security.md](../standards/security.md) §2).
- **Threat model:** new system or SEC-027 trigger not covered by the existing model.
- No self-exemptions: no invented exceptions (AGENT-007, AGENT-019), no disabling controls
  (AGENT-013) or tests (AGENT-020), no silent downgrades (AGENT-003/005), findings suppressed
  only by waiver or fix (SEC-028), never by edit.

## Deployment authorization boundary (AGENT-015…017)

Agents *prepare* — deployment config, infrastructure changes, CI definitions, container files,
rollback plans, pipeline-failure analysis — always as reviewable artifacts (AGENT-015). Agents
never silently touch production infrastructure, secrets, or deployment controls (AGENT-016), and
every prepared change needing human authorization is explicitly flagged in output (AGENT-017).

## Escalation paths

- Equal-precedence conflict → stricter reading + report (AGENT-003).
- Ambiguity on a mandatory rule → stop and ask (AGENT-004).
- Task requires violating a mandatory rule → halt and report (AGENT-006).
- Playbook silent → project ADRs → principles → record an ADR
  ([governance/how-to-use.md](../governance/how-to-use.md) §4); never invent (AGENT-019).
