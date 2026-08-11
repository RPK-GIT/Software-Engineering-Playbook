# Repository Standard (REPO)

> **Class:** Standard · **Rule prefix:** `REPO` · **Status:** Active
> **Purpose:** what a production repository contains, how it is organized, and — critically — what
> may never be tracked in it.
> **Owns:** required files, layout conventions, tracked-vs-untracked boundaries (secrets,
> environment values, generated files), manifests and lockfiles, ownership metadata, hygiene.
> **Does not own:** git workflow ([git.md](git.md)); documentation content rules
> ([documentation.md](documentation.md)); secret *management* — storage, delivery, rotation,
> scanning policy (`standards/security.md`, Phase 3; this standard owns only their absence from
> version control, per the boundary recorded in PLAYBOOK-ARCHITECTURE.md §6).
> **Gate:** new-repository checklist at creation; code review thereafter.

Non-normative context — the source-control boundary in one sentence: **version control holds
everything needed to build the system and nothing needed to access an environment.** Code, config
*structure*, defaults, and CI definitions are tracked; credentials and environment-specific values
are supplied at runtime.

## Rules

### REPO-001: Every repository MUST contain the required base files: `README.md`, `CLAUDE.md`, `CODEOWNERS`, `.gitignore`, and a pull request template.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** These five are the attachment points for the rest of the playbook — human entry (DOC-001), agent entry with profile declaration, review routing (GIT-004), the tracking boundary, and the deviation record (AGENT-009); created from [templates/](../templates/readme.md) ([P-12](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation — e.g., LICENSE is additionally required only when code is distributed externally

### REPO-002: A tracked file MUST NOT contain secrets, credentials, tokens, or private keys — in any branch, at any point in history.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Version control is a distribution mechanism: every clone, fork, and cache copies the secret forever, and deletion does not un-leak it ([P-5](../principles/engineering-principles.md)). An exposure triggers rotation and history purge (GIT-009's sole waiver case); scanning tooling policy arrives with `standards/security.md` (Phase 3).
- **Exceptions:** none

### REPO-003: Environment-specific value files MUST NOT be tracked.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** `.env` and its relatives mix the two things the source-control boundary separates — one edit away from violating REPO-002, and they silently diverge per developer ([P-5](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### REPO-004: Every required configuration key MUST be enumerated in a tracked template file with placeholder or safe-default values.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** The template (e.g., `.env.example`) is the discoverable contract of what the application needs — REPO-003 removes the values, this rule preserves the structure; key *documentation* is DOC-005 ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### REPO-005: Build outputs and generated files MUST NOT be tracked.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Generated content bloats history, produces meaningless diffs, and drifts from its source, violating single-source-of-truth ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** generated files that are the deliberate source of record (e.g., a committed API client), documented as such where they live

### REPO-006: Dependency manifests MUST be accompanied by a committed lockfile pinning exact resolved versions.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Without a lockfile, every build resolves dependencies anew — the artifact tested is not the artifact built tomorrow, and supply-chain changes arrive unreviewed ([P-2](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** ecosystems with no lockfile mechanism, or library projects where the ecosystem convention is manifest-only

### REPO-007: Source, tests, scripts, database migrations, and documentation SHOULD live in dedicated, conventionally named top-level directories.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Predictable layout is navigation for humans and agents alike ([P-10](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)); the concrete names follow the ecosystem's convention, recorded in the README.
- **Exceptions:** justified-deviation — ecosystem conventions win over this generic layout

### REPO-008: CODEOWNERS MUST assign a resolvable owner to every top-level path.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Ownership is what makes GIT-004's "qualified reviewer" resolvable mechanically; unowned paths get reviewed by whoever is fastest, which is nobody ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### REPO-009: CI pipeline configuration MUST be version-controlled in the repository it builds.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Pipeline definitions are code: they gate every rule tagged `ci`, so they get the same review, history, and rollback as everything else ([P-3](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** organization-level pipeline fragments referenced from the repository

### REPO-010: Merged branches SHOULD be deleted automatically, and stale unmerged branches SHOULD be closed or deleted at repository review.

- **Level:** SHOULD
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Dead branches are dead code at the repository level — they read as work in progress and hide the branches that are ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## Interaction with other standards

Repository *creation* is gated by [checklists/new-repository.md](../checklists/new-repository.md),
which cites these rules plus the GIT platform-configuration rules (GIT-003, GIT-004). The
`CLAUDE.md` required by REPO-001 follows [templates/claude-md.md](../templates/claude-md.md) and
carries the project's profile declaration that drives all conditional rule applicability.

## Retirement log

None.
