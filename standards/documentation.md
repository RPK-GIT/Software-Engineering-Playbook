# Documentation Standard (DOC)

> **Class:** Standard · **Rule prefix:** `DOC` · **Status:** Active
> **Purpose:** what must be documented, where it lives, and when it must be updated — documentation
> as risk reduction, not ceremony.
> **Owns:** README duties, documentation freshness, the ADR-trigger list, configuration and
> deprecation documentation, changelog duties, documentation placement.
> **Does not own:** API contract specifications (`standards/api.md`, Phase 3); migration rollback
> documentation (`standards/database.md`, Phase 3); runbooks and operational docs
> (`standards/operations.md`, Phase 5); the templates themselves ([templates/](../templates/readme.md)
> instantiate these rules).
> **Gate:** code review.

Non-normative context: documentation exists where its absence creates risk — onboarding,
operations, decision-making, maintenance. Documentation that restates code is a drift liability,
not an asset ([P-3](../principles/engineering-principles.md),
[P-11](../principles/engineering-principles.md)). When these rules are silent, the test is: *what
goes wrong if this is not written down?* If the answer is "nothing", do not write it.

## Rules

### DOC-001: Every repository's README MUST enable a new engineer to build, test, and run the project without consulting any other source.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The README is the executable onboarding path; every gap in it is rediscovered by every new human and every new agent session ([P-12](../principles/engineering-principles.md)). Structure per [templates/readme.md](../templates/readme.md).
- **Exceptions:** justified-deviation

### DOC-002: Documentation invalidated by a change MUST be updated in the same pull request as the change.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Documentation debt is created at the moment of divergence and is cheapest to pay there; "docs later" is how every stale README was born ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DOC-003: A decision matching the ADR-trigger list below MUST be recorded as an ADR before or together with the implementing change.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** These are the decisions whose context evaporates fastest and costs most to relitigate; the trigger list makes "significant" mechanical instead of judged ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

**ADR-trigger list** (normative content of DOC-003; extended only via
[change-process](../governance/change-process.md)):

1. Selecting or replacing a technology: language, framework, platform, datastore, major library.
2. Splitting or merging deployable services (see ARCH-009).
3. Introducing a new datastore or a new category of external dependency.
4. Introducing an architectural mechanism (queue, cache, event bus, plugin system — see ARCH-008).
5. Changing a contract consumed by another team or system.
6. Selecting a security-relevant mechanism (authentication scheme, encryption approach).
7. Adopting a pattern that deviates from how the same problem is already solved in the codebase.
8. Any decision that is expensive to reverse.

### DOC-004: A deprecated capability MUST have its replacement and removal plan documented at the point of deprecation.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** An undocumented deprecation is just a rumor; consumers keep building on the old path because nothing tells them where to go or by when ([P-2](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DOC-005: Every configuration key MUST be documented with its purpose, type, and default at the place the key is declared.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Config keys are an interface operated under pressure by people who did not write them; the tracked template required by REPO-004 is the natural home ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DOC-006: Releases SHOULD include human-readable notes describing user-visible changes.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Release notes answer "what changed?" for consumers, operators, and incident responders; Conventional Commits (GIT-006) make generating a draft nearly free ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DOC-007: Engineering documentation MUST be version-controlled alongside the thing it documents.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Documentation in external systems drifts invisibly, escapes review, and is invisible to agents working in the repository; in-repo docs travel with the code across branches and versions ([P-3](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation — e.g., org-wide documents whose scope exceeds any one repository

### DOC-008: Known failure modes and their resolutions SHOULD be documented in the repository as they are discovered.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The second occurrence of a failure should cost minutes, not the original investigation again; full runbook duties arrive with `standards/operations.md` (Phase 5) ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## Interaction with other standards

README presence is REPO-001; this standard owns its content (DOC-001). Config template presence is
REPO-004; this standard owns key documentation (DOC-005). Commit-message structure is GIT-006;
release notes built on it are DOC-006. ADR format and immutability are owned by
[decisions/README.md](../decisions/README.md); this standard owns only *when* an ADR is required
(DOC-003).

## Retirement log

None.
