# How to Use This Playbook

> **Class:** Governance · **Status:** Active
> What it means for a project to adopt the playbook, and how the relationship works over time.
> Terms: [GLOSSARY.md](../GLOSSARY.md).

## 1. What adoption means

An adopting project repository:

1. **Pins a playbook version** — a specific git tag of this repository (see
   [change-process.md](change-process.md) §2). The pinned tag is what the project is compliant
   *against*; compliance claims without a pin are meaningless.
2. **Declares a profile** — the set of profile tags from
   [standards/_rule-format.md](../standards/_rule-format.md) §4 that describe it (e.g.,
   `web, api-service, uses-database`). The declaration lives in the project's `CLAUDE.md`, created
   from [templates/claude-md.md](../templates/claude-md.md).
3. **Inherits every Active rule** whose applicability tags match `all`, the declared profile, or a
   trigger raised by a given change. Inheritance is by reference — the project never copies rule
   text (RULE-008).
4. **Keeps its own ADR log** for project-level decisions. Org-level decisions stay in this repo's
   [decisions/](../decisions/README.md).
5. **Wires the applicable gates** — the checklists (starting with
   [new-repository](../checklists/new-repository.md)) and the CI checks from the
   [enforcement matrix](enforcement-matrix.md).

## 2. Precedence (summary)

Authoritative definition: [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.2. In short:
a MUST binds everything and is lifted only by a [waiver](waivers.md); an ADR may resolve a SHOULD
with a recorded justification; anything derived may be stricter than its source but never looser
(RULE-009); same-layer conflicts are playbook defects and the stricter reading applies until fixed.

## 3. Upgrading the pinned version

- Upgrading is a **deliberate change**: a PR in the project repo that bumps the pinned tag,
  reviewed like any other change.
- **PATCH/MINOR** upgrades are expected to be routine — nothing mandatory changed.
- **MAJOR** upgrades require a compliance review against the tag's annotated change list (which
  names the changed rule IDs): each added or changed MUST is verified or a waiver is requested
  before the bump merges.
- Projects should not lag more than one MAJOR version behind; persistent lag is raised at the
  quarterly review ([change-process.md](change-process.md) §4).

## 4. When the playbook is silent

No rule covers the situation? Then, in order:

1. Check for an applicable ADR (project first, then org).
2. Decide using the [engineering principles](../principles/engineering-principles.md) and record
   the decision as a project ADR.
3. If the gap seems general, propose a rule via [templates/rfc.md](../templates/rfc.md).

Silence in the playbook is never a license for the weakest option — decisions taken in the gap must
be recorded so the gap closes.

## 5. Feedback loop

Rules that prove wrong, unclear, or costly in practice are challenged through the change process —
not ignored. A project that finds itself repeatedly requesting the same waiver has found a defect
in the playbook, and the quarterly review exists to fix exactly that.
