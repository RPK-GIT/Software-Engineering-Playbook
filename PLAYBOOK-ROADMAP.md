# Playbook Roadmap

> Build order for the Software Engineering Playbook. Structure and rationale are governed by
> [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md); the full inventory with per-document status is
> [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md).
>
> **Current phase: Phase 1 not started** (information architecture complete as of 2026-08-11).

## Sequencing logic

The order follows three constraints:

1. **Meta before rules.** The rule grammar, change process, and waiver path must exist before the first
   rule is written, or early standards will be inconsistent and unamendable (Phase 1).
2. **Authoring-time before deploy-time.** Standards that shape how code is *written* (architecture,
   coding, testing, security, observability) come before standards that shape how code is *shipped and
   run* (ci-cd, infrastructure, operations), because application development starts before the first
   deployment and retrofitting authoring standards is expensive.
3. **Generic before specific.** Platform standards (web, mobile) and agent hardening come after the
   cross-platform core they depend on, so platform documents only contain platform-specific rules.

One deliberate deviation from a strict "agents last" reading of Phase 6: agents need *navigation* from
day one, so Phase 1 seeds a provisional `CLAUDE.md` and `agents/context-map.md`. Phase 6 hardens the
operating model; it does not introduce it.

**Application development may begin when Phases 1–3 are complete.** Phase 4 is required before the first
web/mobile feature work; Phase 5 before the first production deployment; Phase 6 before AI agents work
with reduced human review.

---

## PHASE 1 — Foundation

*Goal: a rule can be written, changed, waived, and found — before any rule exists.*

| Deliverable | Notes |
|---|---|
| `README.md` | Orientation: classes, precedence, navigation |
| `CLAUDE.md` | Agent entry point (provisional routing) |
| `GLOSSARY.md` | Seeded; grows as rules introduce terms |
| `governance/how-to-use.md` | Adoption, pinning, profiles |
| `governance/change-process.md` | RFC flow, versioning (open decision #1) |
| `governance/waivers.md` | Requires waiver-authority decision (open decision #2) |
| `principles/engineering-principles.md` | 10–15 principles |
| `standards/_rule-format.md` | Rule grammar — blocks all other standards |
| `decisions/README.md` + ADR-0001 | ADR practice adopted via its own first ADR |
| `templates/adr.md`, `templates/rfc.md` | Needed by the processes above |
| `agents/context-map.md` (seed) | Navigation stub, completed in Phase 6 |

**Exit criteria:** rule grammar approved; change and waiver processes have named owners; an agent landing
in this repo can find the right document for any existing content.

## PHASE 2 — Core Engineering Standards

*Goal: the always-applicable rulebook — any project, any platform, any stack.*

| Deliverable | Notes |
|---|---|
| `standards/architecture.md` | Boundaries, layering, dependency direction |
| `standards/coding.md` | Needs complexity/limit values (open decision #3) |
| `standards/application.md` | Config, errors, flags, jobs |
| `standards/testing.md` | Needs coverage floors (open decision #3) |
| `standards/git.md`, `standards/repository.md` | Workflow + layout |
| `standards/documentation.md` | Including the ADR-trigger list |
| `checklists/definition-of-done.md` | View over Phase 2 rule IDs; extended each later phase |
| `checklists/code-review.md`, `checklists/new-repository.md` | Gate views |
| `templates/pull-request.md`, `templates/readme.md`, `templates/claude-md.md` | App-repo artifacts |
| `governance/enforcement-matrix.md` (seed) | Every MUST so far mapped to a gate |

**Exit criteria:** a new repository could be created fully compliant; every Phase 2 MUST is in the
enforcement matrix; DoD resolves only to live rule IDs.

## PHASE 3 — Security & Reliability

*Goal: safe to build features that touch data and expose surfaces.*

| Deliverable | Notes |
|---|---|
| `standards/security.md` | Includes PII classification, dependency-vuln policy |
| `standards/api.md` | Contract-first, versioning, error shape |
| `standards/database.md` | Modeling, migration safety, retention (cites SEC for PII) |
| `standards/observability.md` | Authoring-time logging/metrics/tracing duties |
| `checklists/security-review.md` | Gate view |
| `templates/threat-model.md` | Referenced by SEC trigger rules |
| Enforcement matrix update | — |

**Exit criteria:** Phases 1–3 complete = **application development may begin**. Security review gate is
defined with a named owner.

## PHASE 4 — Web & Mobile

*Goal: platform-specific floors, containing only what the core does not cover.*

| Deliverable | Notes |
|---|---|
| `standards/web.md` | Accessibility, performance budgets, asset & browser policy |
| `standards/mobile.md` (stub) | Scope + trigger recorded; authored when first mobile project is real (open decision #4) |
| DoD + enforcement matrix updates | Profile-tagged additions |

**Exit criteria:** a web feature can be built and reviewed against explicit platform rules; mobile scope
is bounded so nobody writes speculative rules.

## PHASE 5 — CI/CD & Operations

*Goal: shipping and running under the same discipline as writing.*

| Deliverable | Notes |
|---|---|
| `standards/ci-cd.md` | Pipeline gates operationalize the enforcement matrix; release/rollback rules |
| `standards/infrastructure.md` | IaC, environments, runtime secrets, backup duties |
| `standards/operations.md` | Severity model, on-call, runbook/postmortem duties |
| `checklists/production-readiness.md` | Aggregating view — first deploy gate |
| `checklists/incident-response.md` | Gate view |
| `templates/runbook.md`, `templates/postmortem.md` | — |

**Exit criteria:** first production deployment can be gated end-to-end; every `ci`-tagged MUST has a
specified pipeline check (implementation may still be pending in app repos).

## PHASE 6 — AI Agent Governance

*Goal: agents operate with defined autonomy, verifiable compliance, and a hardened playbook.*

| Deliverable | Notes |
|---|---|
| `agents/ai-agent-standards.md` | AGENT-xxx rules: reading order, deviation protocol, stop conditions |
| `agents/context-map.md` (complete) | Full task-type × profile matrix, tuned from real usage |
| `templates/claude-md.md` (finalize) | Profile declaration format locked |
| Playbook self-CI | Link integrity, rule-ID uniqueness, checklist-citation validity, orphaned-rule detection (open decision #5) |
| First implementation annexes | Only for stacks adopted by ADR |
| Enforcement matrix completion | Every MUST has a gate or a tracked tooling gap |

**Exit criteria:** "Build this feature" resolves to the correct standard set without human routing; the
playbook's own CI rejects structural defects; quarterly review cadence active per change-process.

---

## Phase completion checklist (applies to every phase)

- [ ] No rule text duplicated anywhere (single-source rule, PLAYBOOK-ARCHITECTURE §1)
- [ ] Every new MUST present in the enforcement matrix
- [ ] Every checklist item resolves to a live rule ID
- [ ] New terms added to GLOSSARY.md
- [ ] DOCUMENT-INDEX.md statuses updated
- [ ] Playbook version tagged per change-process
