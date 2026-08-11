# Coding Standard (CODE)

> **Class:** Standard · **Rule prefix:** `CODE` · **Status:** Active
> **Purpose:** the technology-neutral floor for production code construction.
> **Owns:** readability, naming, typing, code-level error handling, duplication, complexity
> mechanism, dead code, suppressions, dependency *selection*, resource handling, library interfaces.
> **Does not own:** runtime behavior — timeouts, retries, config ([application.md](application.md));
> input validation at trust boundaries and dependency *vulnerabilities* (`standards/security.md`,
> Phase 3); lockfiles and manifests ([repository.md](repository.md)); language-specific style
> (technology annexes, Phase 6, selected by ADR).
> **Gate:** code review, plus the CI checks below.

Non-normative context: these rules assume each project configures concrete tooling (formatter,
linter, type checker) appropriate to its stack — the choice is per-project (ADR/annex); the
obligation that such tooling exists, blocks, and passes is universal.

## Rules

### CODE-001: All source code MUST be formatted by the project's configured automatic formatter.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Formatting by machine ends style debate and makes diffs pure signal ([P-9](../principles/engineering-principles.md), [P-10](../principles/engineering-principles.md)).
- **Exceptions:** generated or vendored files excluded by the formatter configuration

### CODE-002: All source code MUST pass the project's configured static analysis with no unresolved findings.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Linters catch entire defect classes for free; a warning ignored today is a hundred ignored next year ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** findings suppressed per CODE-011

### CODE-003: Projects in languages with optional static typing MUST enable type checking as a blocking CI step.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Types are machine-checked documentation of every interface; opting out discards the cheapest correctness tool available ([P-9](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CODE-004: Identifiers MUST convey their purpose without requiring the reader to inspect the implementation.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Names are the interface of every function and variable; misleading or opaque names tax every future reader, human or agent ([P-12](../principles/engineering-principles.md)). Example (non-normative): `daysUntilExpiry`, not `dUE` or `temp2`.
- **Exceptions:** established domain or ecosystem idioms (loop indices, mathematical notation)

### CODE-005: An error MUST NOT be caught and discarded without being handled, logged, or propagated.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A swallowed error converts a diagnosable failure into silent corruption discovered much later ([P-6](../principles/engineering-principles.md), [P-7](../principles/engineering-principles.md)).
- **Exceptions:** explicitly documented at the site, stating why discarding is correct

### CODE-006: Errors MUST carry enough context to diagnose the failure without reproducing it.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** "Operation failed" costs an incident responder the reproduction; the operation, inputs (never secrets), and cause cost the code author one line ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### CODE-007: Unreachable or unused code MUST be removed rather than retained in comments or disabled blocks.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Dead code is read, maintained, and trusted by tools and agents as if alive; version control is the archive ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### CODE-008: Logic duplicated across three or more sites SHOULD be consolidated into a single shared implementation.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The rule of three balances P-3 (single source of truth) against P-11 (premature abstraction is also a defect): two occurrences may be coincidence; three is a pattern.
- **Exceptions:** justified-deviation — e.g., when the copies are expected to diverge

### CODE-009: Comments SHOULD state intent, constraints, or invariants rather than restating what the code does.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Restating code creates a copy that drifts (P-3); the only knowledge worth a comment is what the code cannot express ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### CODE-010: Static analysis MUST include an enforced complexity limit.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Complexity is where defects live and where reviews go shallow; a mechanical ceiling forces decomposition before that point ([P-9](../principles/engineering-principles.md)). The numeric value is a policy value (RULE-011) — see the proposed policy below.
- **Exceptions:** per-site suppression under CODE-011

### CODE-011: Every static-analysis or type-check suppression MUST carry an inline justification at the suppression site.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Suppressions are the escape hatch that keeps CODE-002/003/010 honest; an unjustified suppression is a silent waiver, and agents must never grant themselves waivers ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### CODE-012: Adding a third-party dependency MUST be explicitly justified in the pull request that introduces it.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Every dependency is an ongoing liability — supply chain, upgrades, licenses, transitive weight; the review criteria (non-normative): solves a real need a stdlib or existing dependency cannot; actively maintained; compatible license; sane transitive footprint ([P-4](../principles/engineering-principles.md), [P-11](../principles/engineering-principles.md)). Vulnerability policy is owned by `standards/security.md` (Phase 3).
- **Exceptions:** development-only tooling dependencies need only a one-line justification

### CODE-013: Acquired resources MUST be released deterministically on all code paths, including error paths.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Leaked connections, handles, and locks are failures that surface far from their cause and only under load ([P-6](../principles/engineering-principles.md)). Use the language's scoped-release idiom.
- **Exceptions:** resources owned by a managing framework or pool

### CODE-014: A released library MUST NOT ship a breaking change to its public interface without a major version increment.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** library
- **Rationale:** Consumers pin against the contract a version number promises; breaking it silently converts every upgrade into a gamble ([P-8](../principles/engineering-principles.md)). Public interfaces of a library are documented at their point of definition (DOC-004 governs configuration keys; interface docs are part of the definition per this rule's review).
- **Exceptions:** waiver-only

### CODE-015: A function SHOULD NOT exceed a cyclomatic complexity of 10 or a length of 50 logical lines.

- **Level:** SHOULD NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Accepted policy values (2026-08-11): a quality signal, not an absolute prohibition — exceeding the limits is permitted with a justification (CODE-011 suppression or recorded deviation per AGENT-009); these are the values the CODE-010 mechanism enforces ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## Accepted policy values

**ACCEPTED POLICY — complexity limits (2026-08-11, Playbook Owner)**
- **Value:** cyclomatic complexity ≤ 10 per function; function length ≤ 50 logical lines (CODE-015)
- **Terms of acceptance:** SHOULD-level quality signal, not an absolute prohibition; exceptions may be justified where appropriate; surfaced as static-analysis warnings via CODE-010

## Retirement log

None.
