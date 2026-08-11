# CI/CD Standard (CI)

> **Class:** Standard · **Rule prefix:** `CI` · **Status:** Active
> **Purpose:** the delivery pipeline — how verified source becomes a running production system,
> repeatably and reversibly.
> **Owns:** pipeline completeness, artifact discipline (build-once, versioning, provenance),
> environment promotion, deployment verification and rollback mechanics, release model,
> deployment strategy selection, migration *application*.
> **Does not own:** which checks exist (the [enforcement matrix](../governance/enforcement-matrix.md)
> and the standards it indexes); merge gating (GIT-005); migration *content and compatibility*
> ([database.md](database.md) DB-001…004); infrastructure definition
> ([infrastructure.md](infrastructure.md)); telemetry ([observability.md](observability.md)).
> No CI/CD platform is prescribed — platform selection is a project ADR (DOC-003 trigger 1).
> **Gate:** code review of pipeline changes; production-readiness gate before first deploy.

Non-normative context — where checks live. Four check layers, in order of cheapness:
**authoring-time** (formatter/linter/types in the editor; the agent's self-enforcement),
**CI** (deterministic gates on every PR — the `ci`-tagged rules), **deployment-time**
(post-deploy verification, CI-007), and **runtime** (health signals and alerts, OBS-007…010,
consumed operationally per [operations.md](operations.md)). CI enforces every mandatory
deterministic rule it can; judgment stays human — a required "approval" click that verifies
nothing is not a gate, it is theater.

## 1. Rules

### CI-001: Every repository MUST run its required CI checks automatically on every pull request.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Checks that run sometimes, locally, or on request protect nothing; GIT-005 blocks merging on red — this rule guarantees there is a red to block on ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CI-002: The CI pipeline MUST include every `ci`-tagged mandatory check applicable to the project's profile, per the enforcement matrix.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The matrix is the single source of which checks are owed (RULE-006); this rule makes pipeline completeness auditable against it instead of re-listing checks here and drifting ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CI-003: A release artifact MUST be built once and promoted unchanged through every environment.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Rebuilding per environment means production runs an artifact nothing ever tested; build-once is APP-001's pipeline half ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CI-004: Every release artifact MUST be immutably versioned and traceable to the exact commit that produced it.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** "What is running?" must be answerable to the commit (GIT-010 tags the source side; this rule binds the artifact side); mutable tags like `latest` make rollback and forensics guesswork ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### CI-005: Production deployments MUST use artifacts produced by the CI pipeline.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** An artifact from a developer machine has unverifiable provenance — unknown source state, unscanned dependencies, no audit trail; the pipeline is the only trusted builder ([P-5](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CI-006: A change MUST pass through the project's declared environment promotion sequence before reaching production.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The sequence (however many environments — INFRA owns their properties, not their count) is where deployment-time verification happens with production blast radius of zero ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only — including for hotfixes (GIT-012: expedited, never absent)

### CI-007: Every deployment MUST be verified by automated post-deployment checks before being considered complete.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** "Deployed" and "working" are different claims; readiness signals (OBS-007) and smoke checks convert the second into evidence, and a deployment that fails verification triggers CI-008, not hope ([P-1](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### CI-008: Every production deployment MUST have a defined rollback procedure executable without writing new code.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Roll-forward under incident pressure produces the second incident (GIT-011); rollback limits are dominated by the database — DB-002 (rollback paths) and DB-004 (expand-contract) are what keep the previous artifact deployable against the current schema ([P-6](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where rollback is genuinely impossible (declared-irreversible migrations per DB-002) — the recovery plan then stands in

### CI-009: Database migrations MUST be applied through the deployment pipeline as an ordered, automated step.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Manually applied migrations desynchronize schema from deploy sequencing and leave no audit trail; content, ordering, and compatibility rules are DB-001…004 — this rule owns *how they reach production* ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### CI-010: The production release model — human-approved or automatically promoted on green — MUST be an explicit, recorded decision.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Both models are legitimate; what is not legitimate is not knowing which one you have. Where a human gate exists it verifies something specific (named checklist or judgment), not a reflex click — fake gates erode real ones ([P-2](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### CI-011: Every production service MUST have a declared deployment strategy selected for its risk, availability requirements, and rollback characteristics.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Strategy follows risk, not fashion (guidance in §2); an undeclared strategy means the highest-risk changes ship the same way as typo fixes ([P-6](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### CI-012: High-risk changes SHOULD be released progressively — canary, percentage rollout, or feature flag.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Progressive exposure converts a full-blast failure into a contained one observed at 1% (flags per APP-011/012); "high-risk" is judged at review — auth changes, migrations, dependency majors, hot paths ([P-8](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## 2. Deployment strategy selection (non-normative guidance for CI-011)

| Strategy | Fits when | Watch out |
|---|---|---|
| Rolling | Default for stateless services with health-gated instances | Mixed versions serve traffic simultaneously — API/DB compatibility (API-002, DB-004) |
| Blue/green | Instant cutover and instant rollback justify double capacity | State and in-flight work at switchover; cost |
| Canary | High-risk changes needing production evidence before full exposure | Requires per-slice telemetry (OBS-008) to mean anything |
| Feature flags | Decoupling deploy from release; progressive user-level exposure | Flag hygiene is mandatory (APP-011/012) |

## Interaction with other standards

Merge gating: GIT-005. Migration content: DB-001…004. Environment properties and promotion
isolation: INFRA-005…007. Post-deploy signals: OBS-007/008. Release tagging: GIT-010. Change
records for deployments: OPS-009. Agent limits on pipelines and deployment controls:
AGENT-013, AGENT-015…017.

## Retirement log

None.
