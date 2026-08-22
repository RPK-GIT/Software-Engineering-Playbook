# RFC — Close the resilience gap: circuit breaking and fault containment

- **Status:** Accepted
- **Date:** 2026-08-22
- **Author:** AI agent (Claude Code), on the Playbook Owner's instruction
- **Change class:** MINOR

## Motivation

A coverage review of the playbook against common resilience principles found two gaps:

1. **Circuit breaking.** APP-004 (timeouts) and APP-005 (bounded retries) limit the cost of each
   individual call to a failing dependency, but no rule addresses *persistent* failure: nothing
   stops an application from sending every new request into a dependency that is known to be down,
   amplifying the outage and delaying recovery. The term "circuit breaker" appeared nowhere in the
   playbook.
2. **Fault containment between features.** APP-003 and ARCH-005 govern failure at external
   dependency boundaries, and INFRA-017 governs infrastructure single points of failure, but no
   rule states that the failure of one feature inside a deployable is contained so that unrelated
   features keep working. The playbook's monolith-first stance (ARCH-009) makes this gap material:
   the default architecture concentrates many features in one process.

Both gaps forced undocumented decisions in any project that needed the behavior.

## Affected documents and rules

- `standards/application.md` — two new rules: APP-013, APP-014 (both SHOULD, review, `all`).
- `GLOSSARY.md` — new terms *Circuit breaking*, *Fault containment* (RULE-010).
- `PLAYBOOK-ARCHITECTURE.md` §6 — new anti-duplication row assigning application-level resilience
  to application.md and infrastructure redundancy to infrastructure.md.
- `governance/enforcement-matrix.md` — regenerated (RULE-006 machinery; both rules judgment-class).
- `checklists/code-review.md`, `checklists/definition-of-done.md` — one citation line each (views).
- No existing rule is changed, deprecated, or retired.

## Proposed change

New rules, in canonical form (indented here because canonical blocks live only in `standards/`
per RULE-007; the authoritative copies are in
[standards/application.md](../../standards/application.md)):

    ### APP-013: Calls to an external dependency that is persistently failing SHOULD be suspended automatically until a controlled probe succeeds (circuit breaking).

    - **Level:** SHOULD
    - **Enforcement:** review
    - **Applies to:** all
    - **Rationale:** Timeouts (APP-004) and bounded retries (APP-005) limit the cost of each attempt but still send every new request into a dependency that is down; suspending calls fails fast, sheds load the dependency cannot serve, and gives it room to recover (P-6).
    - **Exceptions:** justified-deviation — e.g., the dependency's declared failure mode (APP-003) is fail-fast for the whole application, or call volume is too low for persistent failure to compound

    ### APP-014: A failure in one feature SHOULD be contained so that features not depending on it remain operational (fault containment).

    - **Level:** SHOULD
    - **Enforcement:** review
    - **Applies to:** all
    - **Rationale:** A single deployable hosts many features; without containment — feature-scoped error handling, isolated resource pools, kill switches per APP-012 — one feature's defect becomes a whole-application outage (P-6).
    - **Exceptions:** justified-deviation for genuinely interdependent features, recorded with the dependency stated

SHOULD (not MUST) is deliberate: both behaviors carry real implementation cost, small or
single-dependency applications legitimately skip them, and the deviation path (recorded
justification per AGENT-009) is the right friction level. This also keeps the change
backward-compatible — MINOR per [change-process](../change-process.md) §2.

## Impact on existing projects

None become non-compliant: SHOULD-level additions bind future changes through recorded deviations,
not waivers. Projects already pinned to earlier tags are unaffected until they upgrade.

## Migration / transition

None needed — no rule is replaced or deprecated. On upgrade, projects address the two rules at the
next change touching dependency-call sites or feature boundaries.

## Decision

**Accepted, 2026-08-22, by the Playbook Owner** — direction given in-session ("close the gaps"
after the coverage review); recorded here by the proposing agent on the Owner's instruction.
Released as **v4.1.0**.
