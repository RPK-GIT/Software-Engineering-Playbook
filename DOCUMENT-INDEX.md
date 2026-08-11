# Document Index

> Complete inventory of the Software Engineering Playbook. Governing structure:
> [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md) · Build order: [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md)
>
> **Status legend:** ✅ exists · 🚧 in progress · 📋 planned · 🧊 stub-until-triggered
> **Mandatory** = required for any adopting project once its phase ships (subject to per-rule applicability tags).

## Root

| Document | Class | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|---|
| `README.md` | Governance | 1 | Yes | 📋 | Human entry point: classes, precedence, navigation |
| `CLAUDE.md` | Instrument | 1 | Yes | 📋 | AI agent entry point; routing only, owns no rules |
| `GLOSSARY.md` | Governance | 1 | Yes | 📋 | One definition per term any rule depends on |
| `PLAYBOOK-ARCHITECTURE.md` | Governance | — | Yes | ✅ | Information architecture (authoritative) |
| `PLAYBOOK-ROADMAP.md` | Governance | — | Yes | ✅ | Build order, phase exit criteria, status |
| `DOCUMENT-INDEX.md` | Governance | — | Yes | ✅ | This inventory |
| `PLAYBOOK-DESIGN.md` | Governance | — | No | ✅ | Original design; superseded by PLAYBOOK-ARCHITECTURE.md |

## governance/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `governance/how-to-use.md` | 1 | Yes | 📋 | Adoption: inheritance, version pinning, project profiles |
| `governance/change-process.md` | 1 | Yes | 📋 | RFC flow, playbook versioning, ownership, review cadence |
| `governance/waivers.md` | 1 | Yes | 📋 | Exception path for MUST rules: approval, format, expiry |
| `governance/enforcement-matrix.md` | 2 | Yes | 📋 | Every MUST → CI check or named human gate |

## principles/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `principles/engineering-principles.md` | 1 | Yes | 📋 | The 10–15 principles all standards derive from |

## standards/ (rule ID prefix in parentheses)

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `standards/_rule-format.md` | 1 | Yes | 📋 | Meta-standard: rule grammar — IDs, levels, enforcement, applicability |
| `standards/architecture.md` (ARCH) | 2 | Yes | 📋 | Layering, boundaries, dependency direction, coupling |
| `standards/coding.md` (CODE) | 2 | Yes | 📋 | Language-agnostic construction rules, dependency selection |
| `standards/application.md` (APP) | 2 | Yes | 📋 | Cross-platform runtime: config, errors, flags, jobs, i18n |
| `standards/testing.md` (TEST) | 2 | Yes | 📋 | Test levels, coverage floors, isolation, fixtures |
| `standards/git.md` (GIT) | 2 | Yes | 📋 | Branching, commits, PR flow |
| `standards/repository.md` (REPO) | 2 | Yes | 📋 | Repo layout, required files, naming |
| `standards/documentation.md` (DOC) | 2 | Yes | 📋 | What must be documented, where; ADR-trigger list |
| `standards/security.md` (SEC) | 3 | Yes | 📋 | Authn/z, secrets, input handling, PII, dependency vulns |
| `standards/api.md` (API) | 3 | Profile: api-service | 📋 | Contracts, versioning, error shape, pagination |
| `standards/database.md` (DB) | 3 | Profile: uses-database | 📋 | Modeling, migration safety, transactions, retention |
| `standards/observability.md` (OBS) | 3 | Yes | 📋 | Structured logging, metrics/SLO conventions, tracing, alerts |
| `standards/web.md` (WEB) | 4 | Profile: web | 📋 | Accessibility, performance budgets, assets, browser policy |
| `standards/mobile.md` (MOB) | 4 | Profile: mobile | 🧊 | Mobile-specific rules; authored when first mobile project is real |
| `standards/ci-cd.md` (CI) | 5 | Yes | 📋 | Pipeline gates, artifact versioning, release/rollback |
| `standards/infrastructure.md` (INFRA) | 5 | Yes | 📋 | IaC, environments, runtime secrets, network baseline, backups |
| `standards/operations.md` (OPS) | 5 | Yes | 📋 | Incident severity, on-call, runbook/postmortem duties |

## agents/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `agents/ai-agent-standards.md` (AGENT) | 6 | Yes | 📋 | Agent operating rules: reading order, deviation protocol, stop conditions |
| `agents/context-map.md` | 1 (seed), 6 (complete) | Yes | 📋 | Task type × project profile → files to load |

## decisions/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `decisions/README.md` | 1 | Yes | 📋 | ADR index; org-level vs project-level scoping rules |
| `decisions/0001-record-architecture-decisions.md` | 1 | Yes | 📋 | Founding meta-ADR adopting the ADR practice |

## checklists/ (views — cite rule IDs only)

| Document | Gate | Phase | Status |
|---|---|---|---|
| `checklists/definition-of-done.md` | Work item claimed complete | 2 (extended 3–5) | 📋 |
| `checklists/code-review.md` | PR opened | 2 | 📋 |
| `checklists/new-repository.md` | Repository created | 2 | 📋 |
| `checklists/security-review.md` | Auth/PII/external-surface change | 3 | 📋 |
| `checklists/production-readiness.md` | First deploy / major change | 5 | 📋 |
| `checklists/incident-response.md` | Incident declared | 5 | 📋 |

## templates/ (pre-compliant artifacts)

| Document | Phase | Status | Instantiates |
|---|---|---|---|
| `templates/adr.md` | 1 | 📋 | ADR practice (decisions/) |
| `templates/rfc.md` | 1 | 📋 | Standard-change proposals (change-process) |
| `templates/pull-request.md` | 2 | 📋 | GIT/DOC rules, deviations section |
| `templates/readme.md` | 2 | 📋 | REPO/DOC rules |
| `templates/claude-md.md` | 2 (finalized 6) | 📋 | App-repo agent entry: profile, pinning, ADR links |
| `templates/threat-model.md` | 3 | 📋 | SEC trigger rules |
| `templates/runbook.md` | 5 | 📋 | OPS rules |
| `templates/postmortem.md` | 5 | 📋 | OPS rules |

---

**Totals:** 46 active documents (6 root + 4 governance + 1 principles + 17 standards + 2 agents + 2 decisions + 6 checklists + 8 templates), plus 1 superseded design document retained as history.
Existing today: 4 (this index, architecture, roadmap, design). Next up: Phase 1 — see
[PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md).
