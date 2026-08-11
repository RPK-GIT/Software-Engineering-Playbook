# 0001 — Record architecture decisions

- **Status:** Accepted
- **Date:** 2026-08-11
- **Deciders:** Playbook Owner

## Context

Significant technical decisions were historically carried in people's heads, chat threads, or
commit messages. The context evaporates, the decision gets relitigated, and reversals happen by
accident rather than by choice. The playbook's architecture requires a clean separation between
universal rules (standards) and contextual choices — the choices need a durable, auditable home
with explicit scoping between organization-wide and project-specific decisions.

## Decision

We record every significant architecture decision as an Architecture Decision Record:

1. ADRs follow the format in [templates/adr.md](../templates/adr.md) and the conventions in
   [decisions/README.md](README.md) (numbering, immutability, statuses, authority).
2. Org-level ADRs live in this repository; each project repository maintains its own `decisions/`
   directory for project-level ADRs.
3. "Significant" is deliberately judged, not enumerated, until `standards/documentation.md`
   (Phase 2) defines the ADR-trigger list; until then: any decision that is expensive to reverse,
   affects more than one component, or selects a technology, records an ADR.
4. ADRs operate under the precedence model of
   [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.2: they choose within the space
   standards permit, and may not relax a MUST without an approved waiver.

## Consequences

**Positive:** decisions survive their deciders; reversals are deliberate (supersession, not
amnesia); AI agents can discover binding context by scanning two indexes; the standards/decisions
boundary stays clean.

**Negative / accepted costs:** writing an ADR takes time, which is the point — decisions worth
making are worth recording; until the Phase 2 trigger list exists, "significant" relies on
judgment and some decisions may be missed.

## Alternatives considered

- **Decision log in a wiki** — rejected: not versioned with the repository, drifts from reality,
  invisible to AI agents working in the repo.
- **Decisions embedded in standards** — rejected: conflates the universal with the contextual,
  which is the exact confusion this playbook's architecture forbids.

## Standards impact

None — this ADR predates the standards it will serve. It implements the Decisions class defined in
PLAYBOOK-ARCHITECTURE.md §1.
