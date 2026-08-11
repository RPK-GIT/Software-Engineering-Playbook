# Engineering Playbook — Repository Design & Execution Plan

> Status: Proposed design, awaiting approval. Once approved, this file moves to `governance/roadmap.md`.
> Date: 2026-08-11

## 1. Design philosophy

Four document classes, strictly separated. Every file in the repository belongs to exactly one:

| Class | Answers | Changes | Example |
|---|---|---|---|
| **Principles** | *Why* we work this way | Rarely (years) | "Boring technology over novel technology" |
| **Standards** | *What* is required — testable rules | Occasionally, via RFC | "SEC-004: Secrets MUST never be committed" |
| **Decisions (ADRs)** | *What we chose* in a specific context, and why | Never (superseded, not edited) | "ADR-0003: PostgreSQL as default relational store" |
| **Instruments** (templates, checklists, agent instructions, enforcement matrix) | *How* the standards get applied | Whenever standards change | PR checklist, ADR template, CLAUDE.md |

Core rules of the design:

1. **Every rule has an ID, a level, and an enforcement tag.** Rules are written as `<DOMAIN>-<NNN>` (e.g., `API-012`), with RFC-2119 levels (MUST / MUST NOT / SHOULD / MAY) and an enforcement tag (`ci` / `review` / `manual`). A "standard" that cannot be checked by a machine or a named human step is not a rule — it moves to Principles.
2. **Single source of truth per rule.** Checklists, the Definition of Done, and agent instructions **reference rule IDs**; they never restate rule text. This is the anti-duplication mechanism: rules live in exactly one file, everything else is a *view*.
3. **AI-first authoring.** Files are small and single-topic so an agent can load only what it needs. `CLAUDE.md` + `agents/context-map.md` route agents to the right files per task type. Rule metadata is structured (consistent headings) so agents and scripts can parse it.
4. **Technology-agnostic core, tech-specific annexes.** Standards say "migrations MUST be reversible", never "use Flyway". Stack choices are ADRs. If a stack is adopted org-wide, a tech annex (e.g., `standards/annexes/typescript.md`) is added — in Phase 4, not before.
5. **Mandatory vs recommended is explicit per rule** (MUST vs SHOULD), never per document. Every document mixes both, clearly labeled.

## 2. Repository structure

```
engineering-playbook/
├── README.md                      # Entry point: what this is, how to navigate, doc classes
├── CLAUDE.md                      # AI agent routing for THIS repo (and pointer to agents/)
├── GLOSSARY.md                    # Shared vocabulary; terms used by rules link here
│
├── governance/
│   ├── how-to-use.md              # How teams/projects adopt the playbook; scope & precedence
│   ├── change-process.md          # RFC process for changing standards; versioning; ownership
│   ├── waivers.md                 # How to get an exception to a MUST, who approves, expiry
│   └── roadmap.md                 # This plan; living status of playbook completion
│
├── principles/
│   └── engineering-principles.md  # 10–15 principles; each with name, statement, implications
│
├── standards/
│   ├── _rule-format.md            # Meta-standard: how rules are written (IDs, levels, tags)
│   ├── security.md                # SEC-xxx
│   ├── api.md                     # API-xxx
│   ├── database.md                # DB-xxx
│   ├── frontend.md                # FE-xxx
│   ├── mobile.md                  # MOB-xxx
│   ├── testing.md                 # TEST-xxx
│   ├── ci-cd.md                   # CI-xxx
│   ├── production-readiness.md    # PROD-xxx
│   ├── operations.md              # OPS-xxx
│   ├── coding.md                  # CODE-xxx
│   ├── repository.md              # REPO-xxx
│   ├── git.md                     # GIT-xxx
│   └── documentation.md           # DOC-xxx
│
├── decisions/
│   ├── README.md                  # ADR index; org-level vs project-level ADR scoping
│   └── 0001-record-architecture-decisions.md   # The founding meta-ADR
│
├── agents/
│   ├── ai-agent-instructions.md   # Non-negotiable rules for AI coding agents (thin; cites IDs)
│   └── context-map.md             # Task type → which playbook files to load
│
├── checklists/                    # Views over standards; every item cites a rule ID
│   ├── definition-of-done.md
│   ├── code-review.md
│   ├── security-review.md
│   ├── production-readiness.md
│   ├── new-repository.md
│   └── incident-response.md
│
├── templates/                     # Copy-paste artifacts for product repos
│   ├── adr.md
│   ├── rfc.md
│   ├── pull-request.md
│   ├── readme.md
│   ├── claude-md.md               # CLAUDE.md template for application repositories
│   ├── runbook.md
│   ├── postmortem.md
│   └── threat-model.md
│
└── enforcement/
    └── enforcement-matrix.md      # Every MUST rule → how it's enforced (CI tool / review gate / manual)
```

41 markdown documents total.

## 3. Why each document exists

**Root**
- `README.md` — Humans land here. Explains the four document classes, precedence order (standard > principle for conflicts; ADR may waive a SHOULD but never a MUST without a waiver), and navigation.
- `CLAUDE.md` — Agents land here. Keeps agent context small: tells an agent what kind of repo this is and to consult `agents/context-map.md` for task-specific loading.
- `GLOSSARY.md` — Rules are only enforceable if their terms are unambiguous ("service", "breaking change", "PII"). One definition, linked everywhere.

**governance/** — Without a change process, a standards repo rots or gets forked informally. `waivers.md` is the pressure valve that keeps MUSTs honest: if there's no legitimate exception path, people ignore rules silently. `how-to-use.md` defines adoption scope: what a new project inherits automatically vs decides via ADR.

**principles/** — The stable "why" layer. When a standard is ambiguous or missing, principles break the tie. Keeping them in one file forces them to stay few and memorable.

**standards/** — The rulebook, one file per domain so agents load only what's relevant. `_rule-format.md` is the meta-standard that makes all others uniform and machine-parseable — it's authored first because every other file depends on it.

**decisions/** — ADRs separate *contextual choices* from *universal rules* (a key constraint you set). This repo holds only org-level ADRs (e.g., default database engine); each application repo holds its own `decisions/` for project-specific ones. `0001` is the meta-ADR adopting the ADR practice itself.

**agents/** — `ai-agent-instructions.md` is deliberately thin: behavioral rules unique to agents (when to stop and ask, how to cite rule IDs in PRs, never invent waivers) plus pointers. Standards themselves are the agent's rulebook — duplicating them here would guarantee drift. `context-map.md` is the token-efficiency layer: "adding an endpoint → load api.md, security.md §auth, testing.md §integration".

**checklists/** — Lifecycle-gate views: each maps a moment in time (PR opened, release cut, repo created, incident declared) to the rule IDs that apply at that moment. They exist because nobody re-reads full standards at 5pm before a release; they stay correct because they contain only IDs + one-line summaries.

**templates/** — Make the compliant path the lazy path. Every template pre-satisfies the documentation standards, so following the template equals following the rules.

**enforcement/** — The honesty ledger. Every MUST appears exactly once with its enforcement mechanism; any MUST tagged `manual` with no named gate is flagged as debt. This file is also the spec for future CI tooling.

## 4. Relationships between documents

```
principles/  ──justify──▶  standards/  ──constrain──▶  decisions/ (ADRs)
                              │
              ┌───────────────┼────────────────┬──────────────┐
        cited by ID      cited by ID      instantiated    mapped 1:1
              │               │                │              │
         checklists/      agents/         templates/    enforcement/
              │               │
              └──── consumed at lifecycle gates by humans and AI agents
```

- **Principles → Standards**: every standard's preamble names the principles it serves. A rule that serves no principle is a candidate for deletion.
- **Standards → ADRs**: standards define the decision space; ADRs pick a point in it. An ADR conflicting with a MUST requires a waiver (governance/waivers.md) recorded in the ADR itself.
- **Standards → Checklists / DoD**: pure projection — rule IDs filtered by lifecycle gate. Regenerated whenever standards change.
- **Standards → Enforcement matrix**: 1:1 for every MUST. The matrix is the backlog for CI automation.
- **Templates → Documentation standards**: each template is the concrete form of DOC-xxx rules.
- **agents/ + CLAUDE.md → everything**: routing layer only; owns no rules.
- **Playbook repo → application repos**: app repos copy `templates/claude-md.md`, `templates/pull-request.md`, inherit all standards by reference (pinned playbook version), and keep their own ADR log.

## 5. Mandatory before application development begins

**Phase 0 + Phase 1 (blocking):** `README.md`, `CLAUDE.md`, `GLOSSARY.md` (seed), all four `governance/` docs, `engineering-principles.md`, `_rule-format.md`, `git.md`, `repository.md`, `coding.md`, `security.md` (baseline: secrets, auth, dependencies, input handling), `testing.md`, `documentation.md`, `decisions/README.md` + ADR-0001, `templates/adr.md`, `templates/pull-request.md`, `templates/claude-md.md`, `templates/readme.md`, `agents/ai-agent-instructions.md`, `agents/context-map.md` (seed), `checklists/definition-of-done.md`, `checklists/code-review.md`, `checklists/new-repository.md`, `enforcement/enforcement-matrix.md` (seed).

**Before first feature-complete milestone (not before dev starts):** `api.md`, `database.md`, `frontend.md`, `ci-cd.md`, `checklists/security-review.md`, `templates/rfc.md`, `templates/threat-model.md`.

**Before first production deploy:** `production-readiness.md`, `operations.md`, `checklists/production-readiness.md`, `checklists/incident-response.md`, `templates/runbook.md`, `templates/postmortem.md`.

**Only when needed:** `mobile.md` (before the first mobile project, not before), tech annexes.

## 6. CI/CD-enforceable vs human-review standards

**Automatable (tag: `ci`)** — code formatting & linting; commit message format; branch protection & required checks; no direct pushes to main; secret scanning; dependency vulnerability scanning & license allowlist; SAST; test execution & coverage thresholds; API schema lint + breaking-change diff against spec; DB migration checks (reversible, lint, no destructive ops without flag); required repo files present (README, CLAUDE.md, LICENSE, CODEOWNERS, PR template); PR size limits; conventional-commit-driven versioning; container/infra config linting; accessibility static checks (partial); link-checking and rule-ID reference integrity *within the playbook itself*.

**Human review required (tag: `review`)** — architecture & service boundaries; data model design; ADR quality (real alternatives, honest consequences); API design semantics (resource naming, error contract fit, versioning strategy); threat modeling & auth design; test *meaningfulness* (coverage % is automatable; asserting the right things is not); UX/accessibility judgment beyond static checks; performance budgets & query plans; production-readiness sign-off; postmortem quality; any waiver of a MUST.

**Named human gates:** code review (every PR), architecture review (new service / cross-service contract / new ADR), security review (auth changes, new external surface, PII handling), production-readiness review (before first deploy and major changes).

## 7. Roadmap

- **Phase 0 — Foundation (do first, small):** README, CLAUDE.md, GLOSSARY seed, governance/ (all 4), principles, `_rule-format.md`, ADR-0001 + decisions/README, adr + rfc templates. *Exit: a rule can be written, changed, and waived through a defined process.*
- **Phase 1 — Pre-development core:** git, repository, coding, security (baseline), testing, documentation standards; DoD, code-review, new-repository checklists; PR/README/claude-md templates; agent instructions + context map; enforcement matrix seeded with every MUST so far. *Exit: an application repo could be started fully compliant.*
- **Phase 2 — Build & delivery:** api, database, frontend, ci-cd standards; security-review checklist; threat-model template; enforcement matrix updated; first org-level ADRs (default stack) as worked examples. *Exit: feature development and CI gates fully specified.*
- **Phase 3 — Production:** production-readiness, operations standards; production-readiness + incident-response checklists; runbook + postmortem templates. *Exit: first production deploy can be gated and operated.*
- **Phase 4 — Extension & hardening:** mobile standards (when a mobile project is real), tech-specific annexes for the adopted stack, refined agent context map from real usage, playbook self-CI (link check, rule-ID integrity, orphaned-rule detection), quarterly review cadence per governance/change-process.md.

Each phase ends with a consistency pass: no duplicated rule text, every checklist item resolves to a live rule ID, every MUST present in the enforcement matrix.

## 8. Assumptions challenged

1. **20 flat categories → 4 document classes.** The objectives list mixes rules (Security Standards), views (Checklists, DoD), artifacts (Templates), and process (ADRs). Treating them as 20 sibling documents guarantees overlap (production-readiness vs operational; repository vs git vs documentation). The class model + rule IDs + "views cite, never restate" is the fix.
2. **Definition of Done and Checklists should not be independent documents.** As standalone prose they drift from the standards within months. Designed here as projections of rule IDs.
3. **AI Agent Instructions should be thin.** A parallel agent rulebook duplicating standards is the fastest path to drift. Agents read the same standards humans do; the agent doc covers only agent-specific behavior + routing.
4. **"Explicit rules over guidelines" needs an enforcement test.** A rule nobody can check is a guideline wearing a costume. Hence: every rule carries an enforcement tag, and untestable statements are demoted to principles.
5. **Don't write mobile standards yet.** Standards written without a concrete project are speculation that must be rewritten later. Deferred to Phase 4 with an explicit trigger.
6. **The playbook needs its own CI.** A standards repo that doesn't enforce its own integrity (broken rule references, orphaned checklist items) loses authority. Added as Phase 4 self-CI.
7. **Version and pin.** Application repos must pin a playbook version and upgrade deliberately; otherwise a standards change silently breaks every project's compliance overnight. Covered in governance/change-process.md.
