# Playbook Architecture

> **Status: Authoritative.** This document defines the information architecture of the Software Engineering Playbook.
> It supersedes [PLAYBOOK-DESIGN.md](PLAYBOOK-DESIGN.md) wherever the two differ (see §9 for the list of changes).
> Companion documents: [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md) (build order), [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md) (full inventory).

---

## 1. Document classes

Every file in this repository belongs to exactly one class:

| Class | Answers | Rate of change | Lives in |
|---|---|---|---|
| **Principles** | *Why* we work this way | Years | `principles/` |
| **Standards** | *What* is required — identified, testable rules | Via RFC only | `standards/`, `agents/` |
| **Decisions (ADRs)** | *What we chose* in a context, and why | Append-only | `decisions/` (org-level); each app repo has its own |
| **Instruments** | *How* standards get applied — views and artifacts | Whenever standards change | `checklists/`, `templates/`, `governance/enforcement-matrix.md`, `agents/context-map.md` |
| **Governance** | *How the playbook itself* changes | Rarely | `governance/` |

**The single-source rule:** a rule is *defined* in exactly one standard, under exactly one rule ID. Every
other document — checklist, template, agent instruction, another standard — *cites the ID* and may add a
one-line summary, but never restates or paraphrases the rule text. A rule found in two places is a defect
to be fixed through `governance/change-process.md`.

## 2. Hierarchy and precedence

Two distinct orderings exist, and confusing them is how implementation details end up silently overriding
architecture. They are separated here deliberately.

### 2.1 Derivation flow (who informs whom)

```
Business Requirements            (per project — not in this repo)
        ↓ drive
Architecture Decisions (ADRs)    (org-level here; project-level in each app repo)
        ↓ select within the space that
Engineering Standards            (standards/*.md — the rulebook)
        ↓ are operationalized as
Implementation Guidelines        (technology annexes; Phase 6+, only for adopted stacks)
        ↓ are consumed through
AI Agent Instructions            (agents/ — routing + agent-specific rules)
        ↓ are verified by
Automated Quality Gates          (CI, per governance/enforcement-matrix.md)
```

### 2.2 Override precedence (who wins a conflict)

Derivation flows downward; **authority does not**. Precedence is:

1. **A MUST/MUST NOT rule in a standard binds every layer.** No ADR, guideline, agent instruction,
   or CI configuration may relax it. The only relaxation path is a waiver under `governance/waivers.md`,
   recorded in the ADR or PR that needs it, with an owner and an expiry date.
2. **An ADR may resolve a SHOULD its own way** if it records the deviation and justification explicitly.
3. **Lower layers may only add strictness, never remove it.** An implementation guideline or agent
   instruction may be stricter than the standard it derives from; if it is looser, the standard wins and
   the derived document is defective.
4. **Principles are tie-breakers, not rules.** When standards are silent or ambiguous, decide by the
   principles and record the decision as an ADR so the gap gets closed.
5. **Two same-layer documents conflicting is a playbook defect** — file it through
   `governance/change-process.md`; until resolved, the more restrictive reading applies.

Rule 3 is the mechanism that prevents implementation detail from overriding architecture: derived
documents are *views with citations*, so a derived document that contradicts its source is by definition
wrong — no judgment call required.

## 3. Repository structure

```
engineering-playbook/
├── README.md                      # Human entry point: classes, precedence, navigation
├── CLAUDE.md                      # AI agent entry point: routing only, owns no rules
├── GLOSSARY.md                    # One definition per term used by any rule
├── PLAYBOOK-ARCHITECTURE.md       # This document
├── PLAYBOOK-ROADMAP.md            # Build order and status
├── DOCUMENT-INDEX.md              # Full inventory with status and phase
│
├── governance/
│   ├── how-to-use.md              # Adoption: what an app repo inherits, pinning, precedence recap
│   ├── change-process.md          # RFC process, versioning, ownership
│   ├── waivers.md                 # Exception path for MUSTs
│   └── enforcement-matrix.md      # Every MUST → its CI check or named human gate
│
├── principles/
│   └── engineering-principles.md
│
├── standards/                     # One file per domain; rule IDs in parentheses
│   ├── _rule-format.md            # Meta-standard: rule grammar (authored first)
│   ├── architecture.md            # (ARCH)  layering, boundaries, dependency direction, coupling
│   ├── coding.md                  # (CODE)  language-agnostic code construction rules
│   ├── application.md             # (APP)   cross-platform runtime: config, errors, flags, jobs
│   ├── security.md                # (SEC)   authn/z, secrets, input handling, data protection, PII
│   ├── api.md                     # (API)   contracts, versioning, errors, pagination
│   ├── database.md                # (DB)    modeling, migrations, transactions, retention
│   ├── web.md                     # (WEB)   browser-specific: accessibility, performance budgets, assets
│   ├── mobile.md                  # (MOB)   mobile-specific (authored when first mobile project is real)
│   ├── testing.md                 # (TEST)  levels, coverage, isolation, fixtures
│   ├── ci-cd.md                   # (CI)    pipelines, gates, versioning & release rules
│   ├── infrastructure.md          # (INFRA) IaC, environments, runtime secrets, network baseline
│   ├── observability.md           # (OBS)   logging, metrics, tracing, alerting rules
│   ├── operations.md              # (OPS)   incident mgmt, on-call, runbooks, postmortems
│   ├── git.md                     # (GIT)   branching, commits, PR flow
│   ├── repository.md              # (REPO)  repo structure, required files, naming
│   └── documentation.md           # (DOC)   what must be documented, where, and how
│
├── agents/
│   ├── ai-agent-standards.md      # (AGENT) rules for AI coding agents — same rule grammar
│   └── context-map.md             # Task type × project profile → files to load
│
├── decisions/
│   ├── README.md                  # ADR index + org/project scoping
│   └── 0001-record-architecture-decisions.md
│
├── checklists/                    # Views: rule IDs filtered by lifecycle gate
│   ├── definition-of-done.md      # Gate: work item claimed complete
│   ├── code-review.md             # Gate: PR opened
│   ├── security-review.md         # Gate: auth/PII/external-surface change
│   ├── production-readiness.md    # Gate: first deploy / major change
│   ├── new-repository.md          # Gate: repo created
│   └── incident-response.md       # Gate: incident declared
│
└── templates/                     # Pre-compliant artifacts to copy into app repos
    ├── adr.md   rfc.md   pull-request.md   readme.md   claude-md.md
    └── runbook.md   postmortem.md   threat-model.md
```

Deliberately **not** separate documents (each of these lives inside an owning standard, listed in §6):
performance, accessibility, privacy/PII, releases & versioning, dependency management, production
readiness. Creating documents for them would manufacture overlap.

## 4. Rule format (summary of `standards/_rule-format.md`)

Every rule in every standard carries:

- **ID** — `<PREFIX>-<NNN>` per the prefixes in §3; stable forever, never reused after retirement.
- **Level** — MUST / MUST NOT / SHOULD / SHOULD NOT / MAY (RFC 2119). Mandatory-vs-recommended is
  explicit per rule, never per document.
- **Enforcement** — `ci` (a pipeline check), `review` (a named human gate), or `manual` (process step).
  Every `ci` and `review` MUST rule appears in `governance/enforcement-matrix.md`.
- **Applies to** — applicability tags: `all`, or profile tags (`web`, `mobile`, `api-service`, `library`)
  and/or trigger tags (`handles-pii`, `public-api`). This is what makes standards conditionally loadable.
- **Rationale** — one or two sentences; links to the principle(s) served.

A statement that cannot carry an enforcement tag is not a rule — it belongs in
`principles/engineering-principles.md` or in a standard's non-normative preamble.

## 5. Document ownership

Format per document: **Problem** it solves / **In** scope / **Out** of scope / **Consumers**
(H = humans, A = AI agents, C = CI) / **Mandatory?** / **Auto-enforceable?**

### Root and governance

- **README.md** — Problem: humans need one orientation page. In: classes, precedence, navigation, how to
  propose changes. Out: any rule. Consumers: H. Mandatory. Not enforceable (content), presence is.
- **CLAUDE.md** — Problem: agents need a small, stable entry point. In: repo identity, pointer to
  `agents/context-map.md`, the always-applicable set. Out: rules, task guidance. Consumers: A. Mandatory. Presence-enforceable.
- **GLOSSARY.md** — Problem: rules are unenforceable when their terms are ambiguous. In: one definition
  per term a rule depends on. Out: general jargon no rule uses. Consumers: H, A. Mandatory. Link-check enforceable.
- **governance/how-to-use.md** — Problem: projects need to know what adoption means. In: inheritance,
  version pinning, project profiles, precedence recap. Out: the change process itself. Consumers: H, A. Mandatory. No.
- **governance/change-process.md** — Problem: standards without a change process rot or get forked. In:
  RFC flow, semantic versioning of the playbook, ownership, review cadence. Out: waivers. Consumers: H. Mandatory. Partially (PR checks on this repo).
- **governance/waivers.md** — Problem: MUSTs without a legal exception path get ignored silently. In:
  who approves, format, expiry, register of active waivers. Out: anything permanent. Consumers: H, A. Mandatory. Partially (waiver format lintable).
- **governance/enforcement-matrix.md** — Problem: unenforced MUSTs read as enforced. In: rule ID → gate
  mapping, tooling backlog. Out: rule text. Consumers: H, C. Mandatory. Yes — integrity is machine-checkable.

### Principles and decisions

- **principles/engineering-principles.md** — Problem: standards need a tie-breaker and a reason to exist.
  In: 10–15 named principles with implications. Out: anything testable (that's a rule). Consumers: H, A. Mandatory. No.
- **decisions/README.md + ADRs** — Problem: context-specific choices must not masquerade as universal
  rules, and reversals need history. In: org-level decisions, index, scoping rules. Out: project-level
  decisions (live in app repos), rules. Consumers: H, A. Mandatory (the practice). Presence/format enforceable; quality is not.

### Standards (the rulebook)

Common shape — Consumers: H, A, C. Each is mandatory for projects matching its applicability tags;
enforceability varies per rule and is recorded in the enforcement matrix. Scope boundaries:

- **architecture.md** — Problem: nothing owned structural rules; "architecture boundaries" was a review
  gate with no source document. In: layering, module/service boundaries, dependency direction, coupling
  limits, when-to-split, integration patterns. Out: technology choices (ADRs), code-level style (coding).
- **coding.md** — Problem: code construction quality varies without explicit floor. In: naming,
  complexity limits, error-handling style, dependency selection policy, comments. Out: runtime behavior
  (application), formatting minutiae (delegated to tooling by rule), platform specifics.
- **application.md** — Problem: cross-platform runtime concerns had no home and would have been duplicated
  into web + mobile. In: configuration management, error/exception policy, feature flags, background
  jobs, idempotency, i18n readiness. Out: browser or mobile specifics, infrastructure provisioning.
- **security.md** — In: authn/z rules, secrets handling, input validation, dependency vulnerability
  policy, data protection & PII classification, threat-model triggers. Out: infra network topology
  (infrastructure), incident handling (operations).
- **api.md** — In: contract-first rules, versioning & breaking-change policy, error shape, pagination,
  idempotency of endpoints. Out: transport auth mechanics (security), internal module interfaces (architecture).
- **database.md** — In: modeling rules, migration safety (reversibility, destructive-op gates),
  transactions, indexing duties, data retention. Out: engine choice (ADR), backup infrastructure (infrastructure).
- **web.md** — In: browser-only concerns — accessibility, performance budgets, asset policy, browser
  support policy. Out: anything a mobile app also needs (application).
- **mobile.md** — Same split as web, for mobile. **Authored only when the first mobile project is real**;
  until then it exists as a scoped stub so nobody writes speculative rules.
- **testing.md** — In: required levels, coverage floors, isolation rules, fixture/data rules, flake
  policy. Out: CI orchestration of tests (ci-cd).
- **ci-cd.md** — In: required pipeline stages and gates, artifact versioning, release & rollback rules,
  environments promotion flow. Out: infrastructure definition (infrastructure), which tests exist (testing).
- **infrastructure.md** — Problem: IaC, environments, and runtime secret delivery had no owner. In: IaC
  requirements, environment parity, network baseline, runtime secrets, backup/restore duties. Out:
  pipeline mechanics (ci-cd), alerting (observability).
- **observability.md** — Problem: logging/metrics/tracing rules are *development-time* duties but were
  buried in deploy-time documents. In: structured logging rules, metric and SLO conventions, tracing
  propagation, alert design. Out: incident process (operations), dashboards for a specific app.
- **operations.md** — In: incident severity model, on-call expectations, runbook and postmortem duties.
  Out: alert thresholds (observability), readiness gating (a checklist, not a standard — see §9.4).
- **git.md** — In: branching model, commit format, PR rules, history hygiene. Out: repo layout (repository), CI triggers (ci-cd).
- **repository.md** — In: required files, directory conventions, naming, LICENSE/CODEOWNERS. Out: git
  workflow (git), doc content rules (documentation).
- **documentation.md** — In: what must be documented, where it lives, freshness duties, ADR-trigger
  list. Out: the templates themselves (templates/ instantiate this standard).

### Agents, checklists, templates

- **agents/ai-agent-standards.md** — Problem: agents need explicit, non-duplicative operating rules. In:
  AGENT-xxx rules — reading order, deviation protocol, waiver prohibition, citation duties, stop
  conditions. Out: any engineering rule (agents read the same standards humans do). Consumers: A, H. Mandatory. Partially (PR-format rules are lintable).
- **agents/context-map.md** — Problem: loading the whole playbook per task wastes context and degrades
  compliance. In: task-type × profile → file list. Out: rules. Consumers: A. Mandatory. Integrity-checkable.
- **checklists/*.md** — Problem: nobody re-reads full standards at a gate. In: rule IDs + one-line
  summaries filtered by gate. Out: rule text, new rules. Consumers: H, A, C (as gate definitions).
  Mandatory: definition-of-done, code-review; others mandatory at their gate. Integrity auto-checkable.
- **templates/*.md** — Problem: compliance must be cheaper than non-compliance. In: pre-compliant
  skeletons with placeholders. Out: rules (templates satisfy rules, they don't define them). Consumers:
  H, A. adr/pull-request/claude-md mandatory; others mandatory at their gate. Presence enforceable.

## 6. Where cross-cutting topics live (anti-duplication register)

| Topic | Owning document | Explicitly NOT in |
|---|---|---|
| Performance | Each domain owns its budget rules (web, api, database) | A separate "performance.md" |
| Accessibility | web.md, mobile.md | application.md |
| Privacy / PII | security.md (classification + handling) | database.md (cites SEC IDs for retention) |
| Secrets — presence in version control | repository.md (REPO-002, REPO-003) | git.md (GIT-009 cites the purge case) |
| Secrets — management, delivery, rotation, scanning policy | security.md (SEC-009…011, SEC-020) | repository.md |
| Agent-specific git prohibitions | agents/ai-agent-standards.md (AGENT-013, AGENT-014) | git.md (owns the universal workflow rules) |
| Authentication & authorization | security.md (SEC-001…004) | api.md, application.md (cite SEC IDs) |
| Input validation — trust boundaries | security.md (SEC-005…008) | coding.md; business invariants are APP-008 |
| Audit events — which must exist | security.md (SEC-022) | observability.md (owns their *format*: OBS-001/002) |
| Telemetry content — sensitive data | observability.md (OBS-005) | security.md (checklist cites OBS-005) |
| Correlation identifiers | observability.md (OBS-003/004) | api.md (API-005 exposes them) |
| Encryption (transit + rest) | security.md (SEC-016/017) | database.md, infrastructure.md |
| Data retention — limits vs mechanism | security.md (SEC-015: limits) / database.md (DB-011: mechanism) | — |
| Backups & restore | infrastructure.md (Phase 5) | database.md (deliberately defines no backup rules) |
| Vulnerability & dependency scanning | security.md (SEC-019…021) | ci-cd.md (pipeline *runs* the scans) |
| Rate limiting & abuse controls | security.md (SEC-023) | api.md |
| Browser security headers & CSP | web.md (WEB-017/018) | security.md |
| Client-side secrets & token storage | web.md (WEB-022/023 — the browser boundary) | security.md (SEC-009 server side, SEC-013 lifetimes) |
| Injection defense — sanctioned rich-text path | web.md (WEB-021) | security.md (SEC-006 owns the general rule) |
| Releases & versioning | ci-cd.md | repository.md |
| Dependency selection | coding.md | — |
| Dependency vulnerabilities | security.md | ci-cd.md (pipeline *runs* the scan; rule lives in SEC) |
| Production readiness | `checklists/production-readiness.md` (a view) | A standard of its own — see §9.4 |
| Migrations | database.md | ci-cd.md (pipeline gates cite DB IDs) |
| Definition of Done | `checklists/definition-of-done.md` (a view) | Any standard |

## 7. Enforceability matrix (summary)

"AI can enforce" = an agent can comply and self-check while authoring. "CI can enforce" = a pipeline can
block violations deterministically. "Human" = a named review gate is still required. Full per-rule
mapping lives in `governance/enforcement-matrix.md` once standards exist.

| Standard area | AI can enforce? | CI can enforce? | Human review required? |
|---|---|---|---|
| Formatting | Yes — applies formatter | Yes — blocks | No |
| Linting | Yes | Yes | No |
| Type safety | Yes | Yes | No |
| Dependency vulnerabilities | Partially — chooses clean deps | Yes — scanner blocks | Only on findings/waivers |
| Secrets in code | Yes — never writes them | Yes — secret scanning | Only on findings |
| API contracts | Yes — authors to spec | Yes — schema lint + breaking-change diff | Yes — design semantics |
| Test coverage | Yes — writes tests | Yes — threshold gate | Yes — test *meaningfulness* |
| Migrations | Yes — authors reversible ones | Partially — lint, dry-run | Yes — destructive operations |
| Security design (authn/z, PII flows) | Partially | Partially — SAST/DAST | Yes — always |
| Architecture boundaries | Partially — obeys declared import rules | Partially — dependency-rule checks | Yes — boundary changes |
| Documentation | Yes — generates | Presence/freshness only | Yes — quality |
| ADR required & followed | Yes — detects triggers, drafts | Partially — presence check | Yes — always |
| Commit/branch/PR rules | Yes | Yes | No |
| Observability rules | Yes — instruments as it codes | Partially — log-shape lint | Yes — SLO/alert design |

Pattern worth noting: **AI enforcement and CI enforcement are complements, not alternatives** — the agent
makes compliance the default at authoring time; CI makes non-compliance impossible at merge time; human
gates cover judgment. The enforcement matrix records all three per rule.

## 8. AI-agent operating model

The target: "Build this feature" → the agent determines applicable standards without being told.

1. **Entry point.** The agent starts in the *application repo's* `CLAUDE.md` (created from
   `templates/claude-md.md`). That file declares: pinned playbook version, the project **profile**
   (e.g., `web + api-service + handles-pii`), links to the project's ADR index, and the pointer into
   this playbook. The first playbook file an agent reads is this repo's `CLAUDE.md`, which routes to
   `agents/context-map.md`.
2. **Always-applicable set** (any task, any profile): coding, git, testing, security, documentation,
   ai-agent-standards, plus the definition-of-done checklist.
3. **Conditional sets** resolve from two axes, per `agents/context-map.md`:
   *profile* (declared in the app repo's CLAUDE.md — a web project never loads mobile.md) and
   *task type* (an endpoint change loads api.md + observability.md; a schema change loads database.md;
   touching auth or PII loads the security-review checklist).
4. **Technology-specific guidance** is selected via the project's ADRs: the ADR that adopted a stack
   links the matching implementation annex (Phase 6+). No ADR → no annex → the agent stays
   technology-agnostic and flags the gap.
5. **ADR discovery.** Before designing, the agent scans the project's `decisions/` index, then the
   org-level `decisions/README.md`, for entries touching the affected area. Accepted ADRs bind the agent
   (precedence §2.2). If the task *requires* a decision no ADR covers and `documentation.md`'s
   ADR-trigger list fires, the agent drafts an ADR from `templates/adr.md` and stops for approval.
6. **Definition of Done** = `checklists/definition-of-done.md` filtered by the project profile; the agent
   verifies each cited rule ID before claiming completion.
7. **Deviation protocol** (defined as AGENT rules): an agent MUST NOT knowingly violate a MUST — it stops
   and reports {rule ID, conflict, options} instead. It MAY deviate from a SHOULD only with a recorded
   justification in the PR description under a `## Standards deviations` section (lintable). Agents never
   grant themselves waivers.

## 9. Changes from PLAYBOOK-DESIGN.md

Outcome of the critical review; the design document remains as history with a supersession notice.

1. **Added `standards/architecture.md`.** The design listed "architecture boundaries" as a human review
   gate but no document owned architectural rules — the largest gap.
2. **Extracted `standards/observability.md`.** Logging/metrics/tracing are authoring-time duties; burying
   them in production-readiness/operations meant agents writing code would never load them.
3. **Added `standards/infrastructure.md`.** IaC, environments, and runtime secrets had no owner.
4. **Deleted `standards/production-readiness.md`.** As a standard it could only restate other domains'
   rules at a gate — a duplication engine contradicting the design's own single-source policy. The
   *checklist* remains and aggregates rule IDs.
5. **Renamed `frontend.md` → `web.md` and added `application.md`.** "Frontend" was ambiguous (mobile is
   frontend too), and cross-platform runtime concerns (config, errors, flags) had no home, which would
   have forced duplication into web + mobile.
6. **Dissolved the `enforcement/` directory** into `governance/enforcement-matrix.md` — a directory for
   one file, and the matrix is governance.
7. **Specified the precedence model (§2).** The design said "standards constrain ADRs" but gave no total
   ordering, no stricter-only rule, and no same-layer conflict rule.
8. **Added the profile mechanism (§8.1, §4 applicability tags).** The design had no way for a project to
   know *which* standards apply to it.
9. **Upgraded `agents/ai-agent-instructions.md` to `ai-agent-standards.md`** with AGENT-xxx rule IDs and a
   defined deviation protocol — prose instructions violated the design's own "explicit rules" principle.
10. **Added the anti-duplication register (§6)** naming an owning document for every cross-cutting topic,
    so future authors don't create overlapping documents for performance, privacy, releases, etc.
11. **Re-phased the roadmap** to the six-phase model in [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md), with a
    provisional agent layer in Phase 1 rather than leaving agents unnavigated until the final phase.

## 10. Open decisions (need owner approval)

1. **Playbook versioning scheme** — semantic versioning with git tags is proposed
   (MAJOR = a MUST added/changed, MINOR = new SHOULD/document, PATCH = editorial); confirm before Phase 1.
2. **Waiver authority** — who may approve a MUST waiver (single named owner vs. role)? Blocks `governance/waivers.md`.
3. **Coverage floors and complexity limits** — numeric values (e.g., line coverage %) are policy choices,
   not derivable; needed when `testing.md`/`coding.md` are authored (Phase 2).
4. **Mobile trigger** — mobile.md stays a stub until a mobile project is approved; confirm this is acceptable.
5. **Language of enforcement tooling** — the playbook's self-CI (link/ID integrity) needs a small toolchain
   choice eventually; deferred to Phase 6, flagged now because it is the playbook's only technology decision.
