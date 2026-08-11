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

## 5. The minimum adoption contract

The complete, ordered list of what adopting actually requires. The playbook stays centrally
maintained — **projects copy templates, never standards**; standards are inherited by reference
through the pin.

1. **Pin** a playbook version (git tag) — §1.1.
2. **Declare** the profile in `CLAUDE.md` from [templates/claude-md.md](../templates/claude-md.md) — §1.2.
3. **Resolve** applicable standards mechanically: `all` + profile tags + triggers
   ([agents/context-map.md](../agents/context-map.md) routes; the
   [enforcement matrix](enforcement-matrix.md) says what's automated vs human).
4. **Copy** the required templates: README, PR template, `CLAUDE.md` (REPO-001); ADR/threat-model/
   runbook/postmortem templates are used as their triggers fire.
5. **Configure validation**: wire the `ci`-tagged checks for the profile into the project's CI
   (CI-002); tooling choices are project ADRs. Note the boundary: the playbook's own
   `tools/validate.py` validates *the playbook repository* and is not installed in application
   repositories — an application's compliance CI is built from its stack's tooling
   (formatter, linter, type checker, tests, coverage, scanners) mapped from the
   [enforcement matrix](enforcement-matrix.md).
6. **Run** [checklists/new-repository.md](../checklists/new-repository.md) to completion.
7. **Initialize** the project `decisions/` directory and record the stack-selection ADR(s) (DOC-003).
8. **Adopt the Definition of Done** — [checklists/definition-of-done.md](../checklists/definition-of-done.md)
   filtered by profile is the project's DoD; extend stricter if needed (RULE-009), never looser.
9. **Integrate playbook-compliance checks into CI** as they become available per the matrix's
   `partial` backlog — honestly classified, never faked.

## 6. Technology annexes

Generic standards are technology-neutral by design; **annexes** carry stack-specific guidance
when a technology family is adopted for reuse. The mechanism (no annexes exist yet — none is
created until an ADR adopts a stack for more than one project):

- Location: `standards/annexes/<technology>.md`, clearly marked technology-specific, with an
  applicability note naming the adopting ADR.
- Derivation: annexes operationalize generic rules for the stack and may only **add strictness**
  (RULE-009); an annex conflicting with a generic standard is defective by definition.
- Lifecycle: created via the change process after the adopting ADR; retired when the stack is.

## 7. Deprecated rules

Per the [rule lifecycle](../standards/_rule-format.md) §5: a Deprecated rule **remains binding**
until Retired, with its replacement named in the rule's Status field. Projects encountering a
deprecated rule follow it (or its replacement, which satisfies it) and treat the deprecation
window as migration time — the tag annotations name every deprecation so upgrades surface them
(§3).

## 8. Feedback loop

Rules that prove wrong, unclear, or costly in practice are challenged through the change process —
not ignored. A project that finds itself repeatedly requesting the same waiver has found a defect
in the playbook, and the quarterly review exists to fix exactly that.
