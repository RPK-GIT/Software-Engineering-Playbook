# Database Standard (DB)

> **Class:** Standard · **Rule prefix:** `DB` · **Status:** Active
> **Purpose:** datastore-technology-neutral rules for schema evolution, integrity, and safe
> operation of persistent data.
> **Owns:** migration discipline, keys and constraints, isolation declaration, indexing duty,
> timestamps, deletion strategy, retention mechanics, connection management.
> **Does not own:** schema *ownership boundaries* ([architecture.md](architecture.md) ARCH-007);
> multi-write atomicity ([application.md](application.md) APP-007); PII classification and
> retention *limits* ([security.md](security.md) SEC-014/015); environment data exposure
> (SEC-018); backup execution and restore infrastructure (`standards/infrastructure.md`,
> Phase 5); engine choice (ADR — DOC-003 trigger 1).
> **Gate:** code review; migrations touching PII/sensitive data additionally trigger security
> review (SEC-026 trigger 8).

Non-normative context: written for any persistent store — relational, document, or key-value.
Where a rule names a relational concept (constraint, isolation level), it applies where the chosen
engine offers it; the *decision* to forego an integrity feature the engine offers is what needs
justification. "Migration" means any versioned change to persistent structure or stored data.

## 1. Rules

### DB-001: Every schema change MUST be applied through a versioned, ordered migration tracked in the repository.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** uses-database
- **Rationale:** Hand-applied schema changes make environments diverge silently and unreproducibly; the migration history *is* the schema's source of truth ([P-3](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### DB-002: Every migration MUST have a defined rollback path or be explicitly declared irreversible with a recovery plan.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** GIT-011's revert-first strategy dies at the database unless someone decided *in advance* what down looks like; "declared irreversible + recovery plan" is honest, silence is not ([P-6](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DB-003: A migration MUST NOT destroy or rewrite data without an explicit, reviewed preservation step.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Dropped columns and destructive backfills are the changes with no undo; preservation (copy, archive, backup verified restorable) converts the irreversible into the recoverable ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** data whose destruction is the *purpose* (retention enforcement per DB-011, verified deletion per SEC-015)

### DB-004: A schema migration MUST be compatible with the application version running when it is applied.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Deploys are not atomic across schema and code; expand-contract sequencing (add-migrate-remove) is what makes zero-downtime deployment possible at all ([P-8](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** systems with an accepted, recorded maintenance-window deployment model

### DB-005: Every table or collection MUST have an explicit primary key.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Keyless data cannot be referenced, deduplicated, replicated, or safely updated; every engine's tooling assumes identity exists ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** append-only structures where the engine's design is genuinely keyless (some log/time-series stores), documented as such

### DB-006: Integrity rules the datastore can enforce MUST be declared as datastore constraints rather than enforced only in application code.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Application-level checks miss every path that isn't the application — admin scripts, migrations, future services (ARCH-007 notwithstanding, defense in depth at the data layer is cheap); foreign keys, uniqueness, and non-null are declarations, not code ([P-3](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation — e.g., constraints whose cost is measured and prohibitive at scale, recorded via ADR

### DB-007: Code that depends on a specific transaction isolation behavior MUST declare it explicitly rather than relying on engine defaults.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Default isolation differs across engines and versions; correctness that depends on an undeclared default breaks on upgrade or engine change with no diff to review ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DB-008: Production query patterns MUST be supported by indexes verified against the query plan.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Missing indexes are invisible at test scale and incidents at production scale; "verified against the plan" is what separates indexing from guessing ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for genuinely rare access paths where the index's write cost exceeds its value

### DB-009: Mutable records SHOULD carry creation and last-modification timestamps.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Two columns costing nothing at design time answer half of every future support question and enable incremental processing; security-relevant audit *events* are SEC-022, not this ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DB-010: Entities subject to audit, recovery, or reference-integrity requirements SHOULD use soft deletion or archival rather than physical deletion.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Physical deletion of referenced or auditable data destroys history other records depend on; soft deletion is a per-entity design decision, not a global default — and it never overrides SEC-015's obligation to actually delete PII when required ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### DB-011: Every persisted data category MUST have a declared retention policy where its classification or regulation requires one.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database, handles-pii
- **Rationale:** Retention is where SEC-015's minimization meets the schema: this rule owns the mechanism (what is declared where, how enforcement runs); security owns the limits ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for data with no classification-driven or regulatory retention requirement

### DB-012: Applications MUST access the datastore through a bounded connection pool.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Unbounded connections turn application load spikes into datastore outages — the failure arrives at the layer least able to shed it; per-use acquire/release discipline is CODE-013 ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for serverless execution models with platform-managed pooling

## Interaction with other standards

Who may write to a schema: ARCH-007. Atomicity across writes: APP-007. Migration PRs touching
classified data trigger security review (SEC-026 trigger 8). Retention limits for PII: SEC-015;
environment copies: SEC-018. Backup execution and restore drills arrive with
`standards/infrastructure.md` and `standards/operations.md` (Phase 5) — this standard deliberately
defines no backup rules to avoid a second owner.

## Retirement log

None.
