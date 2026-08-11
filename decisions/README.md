# Architecture Decision Records

> **Class:** Decisions · **Status:** Active
> Context-specific choices, kept separate from universal rules. A standard says what is always
> required; an ADR says what we chose here, and why, so the choice can be understood and revisited.

## Scoping: org-level vs project-level

- **This directory** holds **org-level** decisions: choices that bind every adopting project
  (e.g., a default technology stack, adopted org-wide via ADR — none yet).
- **Each project repository** holds its own `decisions/` directory for project-level choices.
  Project ADRs must comply with org ADRs and with all applicable standards
  ([PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.2).

## Conventions

- **Numbering:** `NNNN-short-kebab-title.md`, four digits, sequential, never reused.
- **Immutability:** an accepted ADR is never edited into a different decision. To change course,
  write a new ADR that supersedes the old one; the old ADR's status is updated to
  `Superseded by NNNN` and nothing else in it changes.
- **Statuses:** `Proposed` → `Accepted` | `Rejected`; `Accepted` → `Deprecated` | `Superseded by NNNN`.
- **Format:** [templates/adr.md](../templates/adr.md). Every ADR records the standards it touches
  and any deviations or waivers it depends on.
- **Authority:** org-level ADRs are accepted by the Playbook Owner. AI agents may draft ADRs
  (status `Proposed`) but never accept them.

## Index

| ADR | Title | Status | Date |
|---|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted | 2026-08-11 |
| [0002](0002-github-actions-for-playbook-self-ci.md) | GitHub Actions for playbook self-CI | Accepted | 2026-08-11 |
