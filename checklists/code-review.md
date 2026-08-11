# Code Review Checklist

> **Class:** Instrument (view) · **Gate:** pull request opened · **Status:** Active
> For the reviewer. Items cite rule IDs (RULE-008); the cited rule is authoritative. The
> mechanical rules (formatting, lint, types, commit format) are CI's job — do not spend review
> attention re-checking them; spend it on the judgment items CI cannot see
> ([enforcement matrix](../governance/enforcement-matrix.md)).

## Before reading the diff

- [ ] CI green — if not, stop; review of a red PR wastes the judgment budget — GIT-005
- [ ] One logical change, right-sized — GIT-007
- [ ] `## Standards deviations` section present and honest (agents: mandatory) — AGENT-009
- [ ] Author's unresolved questions addressed — AGENT-011

## Design and structure (the judgment core)

- [ ] Change lands in the right component; responsibility still singular — ARCH-001
- [ ] Domain logic stays free of delivery/infrastructure concerns — ARCH-002, ARCH-003
- [ ] Interactions go through declared interfaces; external systems behind owned adapters — ARCH-004, ARCH-005
- [ ] No mechanism introduced for a requirement that doesn't exist — ARCH-008
- [ ] Names convey purpose without reading the implementation — CODE-004
- [ ] Comments explain why, not what; none restating code — CODE-009

## Correctness and resilience

- [ ] No swallowed errors; errors carry diagnostic context — CODE-005, CODE-006
- [ ] Resources released on all paths — CODE-013
- [ ] Timeouts, bounded retries, idempotency where execution can repeat — APP-004, APP-005, APP-006
- [ ] Multi-write atomicity or compensation — APP-007
- [ ] Invariants enforced in the domain layer, not just the interface — APP-008
- [ ] Concurrent access to shared state is safe — APP-010

## Tests (meaningfulness is *this* gate — coverage numbers cannot check it)

- [ ] Tests assert the behavior that changed, not incidental implementation — TEST-001, TEST-011
- [ ] Failure/boundary cases present — TEST-009
- [ ] Bug fix carries its regression test — TEST-002
- [ ] No new dependence on external systems from unit tests — TEST-005

## Dependencies, docs, decisions

- [ ] New dependencies justified; nothing a stdlib or existing dep already does — CODE-012
- [ ] Docs updated in this PR where invalidated — DOC-002
- [ ] ADR present if a trigger matched — DOC-003
- [ ] Nothing secret or environment-specific in the diff — REPO-002, REPO-003
