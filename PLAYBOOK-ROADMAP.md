# Playbook Roadmap

> Build order for the Software Engineering Playbook. Structure and rationale are governed by
> [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md); the full inventory with per-document status is
> [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md).
>
> **ALL SIX PHASES COMPLETE (2026-08-11). The playbook is release v4.0.0 and enters maintenance
> mode** — quarterly reviews per [change-process](governance/change-process.md) §4, changes via
> RFC only. Phase 6 exit criteria verified: "build this feature" resolves to the correct standard
> set without human routing ([context-map](agents/context-map.md) + pilot walkthrough below);
> the playbook's own CI rejects structural defects (`tools/validate.py` V1–V15 blocking +
> matrix-drift gate, per [ADR-0002](decisions/0002-github-actions-for-playbook-self-ci.md));
> review cadence defined. Final status: see "Final status" at the end of this document.
> Phase 3 exit criteria verified: security-review gate defined with trigger list and owner role
> (SEC-026, Playbook Owner / Principal Architect); every Phase 3 MUST in the
> [enforcement matrix](governance/enforcement-matrix.md); all checklists resolve to live rule IDs.

## What v1.0.0 means — and does not mean

`v1.0.0` = **Production Engineering Foundation**: the core architecture, engineering, security,
API, database, observability, and reliability foundations required for production-oriented
backend/service development exist and are enforced. It does **not** mean all profile-specific or
technology-specific standards are complete. Consequences, by profile:

| Project profile | May development begin at v1.0.0? |
|---|---|
| `api-service`, `library`, backend services | **Yes** — applicable Phase 1–3 standards suffice |
| `web` | **Yes, as of Phase 4** — [standards/web.md](standards/web.md) applies alongside the core |
| `mobile` | Only after the stub is expanded — trigger: an accepted ADR for a mobile project ([standards/mobile.md](standards/mobile.md)) |
| Any profile needing infra/platform standards | The applicable Phase 5 standards bind when their applicability requires them |

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
| `agents/ai-agent-standards.md` (seed) | AGENT-001…012: binding agent behavior from day one; completed in Phase 6 |

*Scope note: the agent-standards seed was pulled forward from Phase 6 during Phase 1 execution —
the approved Phase 1 requirements (conflict resolution, waiver handling, deviation recording,
compliance verification) are rules, and rules must live in a standard (RULE-007), not in routing
documents.*

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

**Exit criteria:** Phases 1–3 complete = **v1.0.0, Production Engineering Foundation** —
backend/API/service development may begin; web and mobile additionally require their Phase 4
standards (see "What v1.0.0 means" above). Security review gate is defined with an owning role.

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
| `agents/ai-agent-standards.md` (complete) | Extend the Phase 1 seed (AGENT-001…012) with autonomy levels and lessons from real usage |
| `agents/context-map.md` (complete) | Full task-type × profile matrix, tuned from real usage |
| `templates/claude-md.md` (finalize) | Profile declaration format locked |
| Playbook self-CI | Link integrity, rule-ID uniqueness, checklist-citation validity, orphaned-rule detection (open decision #5) |
| First implementation annexes | Only for stacks adopted by ADR |
| Enforcement matrix completion | Every MUST has a gate or a tracked tooling gap |

**Exit criteria:** "Build this feature" resolves to the correct standard set without human routing; the
playbook's own CI rejects structural defects; quarterly review cadence active per change-process.

---

## Final status (post-Phase 6, v4.0.0)

**Inventory:** 47 active documents (46 complete + 1 trigger-gated mobile stub) · 263 normative
rules in 17 rule-bearing documents · 5 profile tags + 2 trigger tags · 6 checklists · 10
templates-and-instruments · 2 ADRs · 6 accepted numeric policies, 0 pending.
**Enforcement distribution:** 24 auto · 30 partial · 169 review-only · 21 judgment · 19 process.
**Technology decisions made by the playbook itself:** exactly one — the self-CI platform
([ADR-0002](decisions/0002-github-actions-for-playbook-self-ci.md)). Everything else is
deliberately deferred to project ADRs.

### Pilot walkthrough findings (Phase 6 desk exercise)

Representative task traced end-to-end ("paginated endpoint + new table, `web + api-service +
uses-database` profile"): entry → profile → routing → ~12 of 47 documents loaded → correct rules
and gates fired → DoD resolved. Genuine defects found and fixed during Phase 6, none silently:

| Finding | Class | Resolution |
|---|---|---|
| No defined behavior for undeclared profile | Missing standard | AGENT-018 |
| Nothing forbade inventing standards / assuming decisions | Missing standard | AGENT-019 |
| Nothing forbade deleting tests to pass CI | Missing standard | AGENT-020 |
| Nothing forbade self-serving playbook edits | Missing standard | AGENT-021 |
| Validator reported violations but exited 0 | Tooling defect | Blocking exit codes |
| Enforcement-matrix drift unchecked | Tooling defect | CI diff gate |
| Tech-neutrality scan flagged ADRs | Tooling defect | `decisions/` exempted — ADRs are where technology belongs |
| Migration route omitted CI-009 | Navigation | Fixed in final context map |
| Trigger tags depend on correct PII classification (SEC-014 judgment) | Known limitation | Recorded below, not papered over |

### What the playbook guarantees — and what it cannot

**Guarantees:** every requirement is identified, owned, and classified by how it is actually
enforced; agents and humans can determine applicable standards mechanically from profile + task;
deviations and exceptions are recorded and auditable, never silent; structural defects in the
playbook itself fail CI; versions are pinned and breaking changes are explicit.

**Cannot guarantee:** that software following it is secure, bug-free, scalable, or incident-free —
no document can. Review-classed and judgment-classed rules (190 of 263) are only as good as the
humans exercising them; `partial` checks depend on per-project tooling that projects must actually
wire; trigger-based gates depend on honest classification of what a change touches; and until a
person holds the Playbook Owner role, no MUST waiver can be approved at all. The playbook reduces
risk by construction and makes violations visible — it does not abolish engineering judgment.

### Known limitations

Playbook Owner is a role without a person (waivers blocked — deliberate). Mobile is a stub until
its ADR trigger. `partial` checks (30) are a per-project tooling backlog. Action SHA-pinning
pending first external contributor (ADR-0002 backlog). Branch protection on this repo activates
with the second contributor (ADR-0002).

### Operating model from here

Quarterly review per change-process §4 (waiver expiry, deprecated-rule retirement, unused rules,
tooling gaps) · annual full-playbook audit against real project experience · all changes via RFC
· every release tag annotated with rule deltas · the first real adopting project's feedback is
the highest-value input the playbook can now receive.

## Phase completion checklist (applies to every phase)

- [ ] No rule text duplicated anywhere (single-source rule, PLAYBOOK-ARCHITECTURE §1)
- [ ] Every new MUST present in the enforcement matrix
- [ ] Every checklist item resolves to a live rule ID
- [ ] New terms added to GLOSSARY.md
- [ ] DOCUMENT-INDEX.md statuses updated
- [ ] Playbook version tagged per change-process
