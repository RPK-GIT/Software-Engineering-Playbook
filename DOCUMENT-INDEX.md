# Document Index

> Complete inventory of the Software Engineering Playbook. Governing structure:
> [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md) · Build order: [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md)
>
> **Status legend:** ✅ exists · 🚧 in progress · 📋 planned · 🧊 stub-until-triggered
> **Mandatory** = required for any adopting project once its phase ships (subject to per-rule applicability tags).

## Root

| Document | Class | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|---|
| `README.md` | Governance | 1 | Yes | ✅ | Human entry point: classes, precedence, navigation |
| `CLAUDE.md` | Instrument | 1 | Yes | ✅ | AI agent entry point; routing only, owns no rules |
| `GLOSSARY.md` | Governance | 1 | Yes | ✅ | One definition per term any rule depends on |
| `PLAYBOOK-ARCHITECTURE.md` | Governance | — | Yes | ✅ | Information architecture (authoritative) |
| `PLAYBOOK-ROADMAP.md` | Governance | — | Yes | ✅ | Build order, phase exit criteria, status |
| `DOCUMENT-INDEX.md` | Governance | — | Yes | ✅ | This inventory |
| `PLAYBOOK-DESIGN.md` | Governance | — | No | ✅ | Original design; superseded by PLAYBOOK-ARCHITECTURE.md |

## governance/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `governance/how-to-use.md` | 1 | Yes | ✅ | Adoption: inheritance, version pinning, project profiles |
| `governance/change-process.md` | 1 | Yes | ✅ | RFC flow, playbook versioning, ownership, review cadence, self-validation capabilities |
| `governance/waivers.md` | 1 | Yes | ✅ | Exception path for MUST rules: approval, format, expiry, register |
| `governance/enforcement-matrix.md` | 2 | Yes | ✅ | Every rule → gate, automatability class, blocking status (generated from rule blocks) |

## principles/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `principles/engineering-principles.md` | 1 | Yes | ✅ | The 12 principles (P-1…P-12) all standards derive from |

## standards/ (rule ID prefix in parentheses)

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `standards/_rule-format.md` (RULE) | 1 | Yes | ✅ | Meta-standard: rule grammar — IDs, levels, enforcement, applicability registries |
| `standards/architecture.md` (ARCH) | 2 | Yes | ✅ | Layering, boundaries, dependency direction, data ownership, when-to-split (9 rules) |
| `standards/coding.md` (CODE) | 2 | Yes | ✅ | Language-agnostic construction rules, dependency selection (14 rules) |
| `standards/application.md` (APP) | 2 | Yes | ✅ | Cross-platform runtime: config, failure modes, idempotency, flags (12 rules) |
| `standards/testing.md` (TEST) | 2 | Yes | ✅ | Test levels, determinism, isolation, flake policy, coverage mechanism (14 rules) |
| `standards/git.md` (GIT) | 2 | Yes | ✅ | Branching, protection, commits, PR flow, releases, reverts (12 rules) |
| `standards/repository.md` (REPO) | 2 | Yes | ✅ | Required files, tracked-vs-untracked boundary, lockfiles, ownership (10 rules) |
| `standards/documentation.md` (DOC) | 2 | Yes | ✅ | What must be documented, where; ADR-trigger list (8 rules) |
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
| `agents/ai-agent-standards.md` (AGENT) | 1 (seed), 6 (complete) | Yes | 🚧 | Agent operating rules AGENT-001…012: discovery, conflicts, waivers, deviations, verification |
| `agents/context-map.md` | 1 (seed), 6 (complete) | Yes | 🚧 | Task type × project profile → files to load |

## decisions/

| Document | Phase | Mandatory | Status | Purpose |
|---|---|---|---|---|
| `decisions/README.md` | 1 | Yes | ✅ | ADR index; org-level vs project-level scoping rules |
| `decisions/0001-record-architecture-decisions.md` | 1 | Yes | ✅ | Founding meta-ADR adopting the ADR practice |

## checklists/ (views — cite rule IDs only)

| Document | Gate | Phase | Status |
|---|---|---|---|
| `checklists/definition-of-done.md` | Work item claimed complete | 2 (extended 3–5) | ✅ |
| `checklists/code-review.md` | PR opened | 2 | ✅ |
| `checklists/new-repository.md` | Repository created | 2 | ✅ |
| `checklists/security-review.md` | Auth/PII/external-surface change | 3 | 📋 |
| `checklists/production-readiness.md` | First deploy / major change | 5 | 📋 |
| `checklists/incident-response.md` | Incident declared | 5 | 📋 |

## templates/ (pre-compliant artifacts)

| Document | Phase | Status | Instantiates |
|---|---|---|---|
| `templates/adr.md` | 1 | ✅ | ADR practice (decisions/) |
| `templates/rfc.md` | 1 | ✅ | Standard-change proposals (change-process) |
| `templates/pull-request.md` | 2 | ✅ | AGENT-009 deviations section, GIT-007 scope |
| `templates/readme.md` | 2 | ✅ | DOC-001, REPO-007 |
| `templates/claude-md.md` | 2 (finalized 6) | ✅ | App-repo agent entry: profile declaration, pinning, ADR links |
| `templates/threat-model.md` | 3 | 📋 | SEC trigger rules |
| `templates/runbook.md` | 5 | 📋 | OPS rules |
| `templates/postmortem.md` | 5 | 📋 | OPS rules |

---

**Totals:** 46 active documents (6 root + 4 governance + 1 principles + 17 standards + 2 agents + 2 decisions + 6 checklists + 8 templates), plus 1 superseded design document retained as history.
**Phase 2 complete (2026-08-11):** 30 documents exist (28 ✅ + 2 🚧 seeds); 106 normative rules
across 9 rule-bearing documents. Next up: Phase 3 — Security & Reliability — see
[PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md).
