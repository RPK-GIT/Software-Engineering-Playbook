# Infrastructure Standard (INFRA)

> **Class:** Standard · **Rule prefix:** `INFRA` · **Status:** Active
> **Purpose:** cloud-neutral requirements for the platforms production software runs on —
> infrastructure as code, environments, network boundaries, scaling, resilience, containers,
> backup/disaster recovery, and cost stewardship.
> **Owns:** infrastructure definition and change discipline, environment properties, network
> exposure, workload identity, scaling and overload behavior at the platform layer, container
> image requirements, backup/DR architecture, resource ownership and cost visibility.
> **Does not own:** application-level failure behavior ([application.md](application.md)
> APP-003…006); secret management policy ([security.md](security.md) SEC-009…011 — this standard
> wires it into platforms); telemetry ([observability.md](observability.md)); pipeline mechanics
> ([ci-cd.md](ci-cd.md)); how signals are operated ([operations.md](operations.md)).
> **Gate:** infrastructure changes reviewed like code (INFRA-001); production-readiness gate
> before first deploy.

Non-normative context: **no technology is mandated** — no cloud provider, container runtime,
orchestrator, serverless platform, or IaC tool. Containers are not required; where a project uses
them, the container rules apply. Every rule here is a capability requirement satisfiable on any
mainstream platform; concrete selections are project ADRs (DOC-003 trigger 1). On cost:
cost-awareness is a first-class engineering duty below, but cost optimization never outranks
correctness, security, reliability, or maintainability — a cheaper system that corrupts data is
not cheaper.

## 1. Rules

### Infrastructure as code

### INFRA-001: Production infrastructure MUST be defined as version-controlled code, changed only through reviewed pull requests.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Console-click infrastructure is undocumented, unreviewable, and unreproducible — the environment nobody can rebuild; IaC gets the same gates as every other change ([P-3](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for genuine break-glass operations, which are reconciled back into code afterward (INFRA-003)

### INFRA-002: Applying an unchanged infrastructure definition MUST produce no changes.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Idempotent application is what makes infrastructure code trustworthy — plan output becomes reviewable intent instead of noise ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for resources that are inherently regenerated

### INFRA-003: Deployed infrastructure SHOULD be checked for drift from its definition on a schedule.

- **Level:** SHOULD
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Drift is INFRA-001 decaying silently — every unreconciled manual change makes the code a little more fictional ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-004: Infrastructure state containing sensitive values MUST be stored in an access-controlled backend, never in the repository.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** IaC state files routinely embed connection strings and credentials; committing state is committing secrets one abstraction removed (REPO-002's spirit, SEC-009's mechanism) ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### Environments

### INFRA-005: Production MUST be isolated from non-production environments in compute, data, credentials, and network.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Shared anything is a path for a test mistake to become a production incident and for production data to leak downward (SEC-018 owns the data direction; this rule owns the platform separation) ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### INFRA-006: Pre-production verification environments SHOULD mirror production in architecture and configuration structure.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Verification against an unrepresentative environment verifies the wrong system; structural parity (same topology, same config keys — not same scale) is what promotion evidence rests on ([P-2](../principles/engineering-principles.md)). The playbook mandates environment *properties*, never a fixed count.
- **Exceptions:** justified-deviation

### INFRA-007: Interactive access to production systems MUST be restricted to authorized operators, audited, and granted per least privilege.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Production shell access is the widest capability that exists; SEC-004 gives the principle, this rule pins it to the highest-value target — routine work goes through pipelines (CI-005), not sessions ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### Network and identity

### INFRA-008: Network exposure MUST be deny-by-default, with only declared entry points reachable from public networks.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Every reachable port is attack surface; SEC-001 authenticates the declared entry points — this rule ensures undeclared ones do not exist. Internal components sit in private boundaries behind explicit ingress ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### INFRA-009: TLS certificates MUST be managed with automated renewal.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Manually renewed certificates are scheduled outages with a human single point of failure; SEC-017 requires the encryption — this rule keeps it from expiring ([P-9](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where automation is genuinely unavailable, with a monitored expiry alert as compensating control

### INFRA-010: Workload identity SHOULD come from platform-managed identity mechanisms rather than long-lived static credentials.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Platform identity is short-lived, auto-rotated, and unstealable-at-rest — everything SEC-010/013 want, provided by the platform for free ([P-4](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### Scaling and resilience

### INFRA-011: A horizontally scaled service MUST keep session and shared state outside local process memory and disk.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Instance-local state breaks the moment a second instance exists — sticky sessions and lost uploads are the symptoms; externalized state is what makes instances interchangeable and restarts safe (APP-010 owns in-process concurrency; this owns the platform consequence) ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** deliberate instance-affine designs (stateful workloads), recorded per INFRA-012

### INFRA-012: A production service that cannot scale horizontally MUST have the architectural reason recorded in an ADR.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Vertical-only scaling is a legitimate design with a hard ceiling; hitting that ceiling unawares during growth is not — the constraint is understood and written down, not discovered ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### INFRA-013: Every production service MUST have a declared scaling strategy derived from its workload characteristics.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Scaling follows the workload — steady, diurnal, spiky, batch — not the platform's feature list; autoscaling is one answer, fixed capacity is another, and neither is required by default ([P-11](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-014: Production entry points MUST shed or reject excess load rather than degrade unboundedly.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A system without back-pressure converts overload into cascading collapse — queues grow, timeouts fire (APP-004), retries pile on (APP-005); explicit shedding keeps the failure at the edge. Distinct from SEC-023: that rule defends against *abuse*, this one against *capacity* — the mechanisms may coincide, the requirements do not ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-015: Deployed workloads MUST declare explicit resource bounds where the platform supports them.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** An unbounded workload's failure mode is its neighbors' outage; declared bounds (memory, CPU, connections — DB-012 covers the datastore case) make capacity planning arithmetic instead of archaeology ([P-6](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-016: Services MUST handle termination signals by completing or handing off in-flight work within the platform's grace period.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Deploys, scale-downs, and instance replacement all terminate processes; graceful shutdown is what makes those routine instead of small data-loss events (APP-006's idempotency covers the work that still gets cut) ([P-6](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-017: Single points of failure in production infrastructure MUST be identified, and each accepted one recorded in an ADR.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Redundancy everywhere is neither free nor required; *unknown* single points of failure are what this rule forbids — availability design follows the service's declared objectives (OBS-011), and accepted SPOFs are decisions, not surprises ([P-6](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### Containers (where containers are used)

### INFRA-018: Container processes MUST NOT run as root.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Root in the container is one kernel bug from root on the host; non-root execution is the cheapest container hardening that exists (SEC-004 applied to the runtime) ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for workloads requiring privileged operation, via security review

### INFRA-019: Container images SHOULD be built from minimal base images containing only what the workload requires.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Every package in the image is attack surface and scanner noise (INFRA-020); minimal bases shrink both, plus pull time ([P-11](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-020: Container images MUST be scanned for known vulnerabilities before deployment.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Images carry an OS layer that dependency scanning (SEC-019) never sees; the same accepted severity gate applies (SEC-028) ([P-5](../principles/engineering-principles.md)). Image immutability and provenance come free with CI-003/004/005 — images are artifacts.
- **Exceptions:** waiver-only

### INFRA-021: Builds SHOULD produce a software bill of materials for deployed artifacts.

- **Level:** SHOULD
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** When the next ecosystem-wide vulnerability lands, "are we affected?" is a query against SBOMs or a week of spelunking; SHOULD-level until tooling matures across ecosystems — image signing is likewise adopted where the threat model justifies it, via ADR ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### Backup and disaster recovery

### INFRA-022: Every production datastore MUST be backed up on a schedule derived from its declared recovery objectives.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Backup frequency is not a default, it is arithmetic from RPO (INFRA-023): data loss tolerance defines the schedule ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** genuinely reconstructible data (caches, derived stores), documented as such

### INFRA-023: Every production service MUST have declared recovery objectives — RPO and RTO — derived from business requirements and recorded in an ADR.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The playbook deliberately sets no universal numbers: an hour of lost analytics and an hour of lost payments are different businesses; the ADR is where the business requirement becomes an engineering target ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### INFRA-024: Backup restoration MUST be exercised periodically against realistic data.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** An unrestored backup is a hope, not a control — restore failures are discovered at exactly one of two times, and the drill is the cheap one ([P-1](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### INFRA-025: Backups MUST be encrypted and isolated — in access and in failure domain — from the systems they protect.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A backup reachable with production credentials is deleted by the same ransomware or mistake that took production; a backup in the same failure domain shares the disaster it exists for. Geographic separation follows from the failure-domain requirement where the declared objectives demand it ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### INFRA-026: A disaster recovery procedure MUST exist and be validated against the declared recovery objectives.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** DR that exists only as an architecture diagram fails on the day; validation (exercise or verified simulation) is what turns declared RTO into achievable RTO ([P-6](../principles/engineering-principles.md), [P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation on validation depth, proportionate to the declared objectives

### Cost stewardship

### INFRA-027: Every provisioned resource MUST be attributable to an owning service or team.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Unattributed resources are unaccountable cost and undeletable risk — nobody knows if the mystery instance is critical or forgotten; attribution mechanism (tagging, naming, account structure) is per platform ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-028: Cloud costs MUST be reviewed on a schedule at service and environment granularity.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Cloud spend drifts by default — orphaned volumes, oversized instances, forgotten environments; a review cadence catches drift while it is small. Never at the expense of correctness, security, or reliability (preamble) ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### INFRA-029: Unused resources and unbounded storage growth SHOULD be reclaimed through lifecycle policies.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Deletion by policy (retention tiers, expiry, cleanup) beats deletion by annual heroics — and storage lifecycle interacts with retention obligations, which win (DB-011, SEC-015) ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## Interaction with other standards

Application failure behavior inside these platforms: APP-003…006. Secret policy these platforms
deliver: SEC-009…011 (INFRA-004/010 wire it in). Environment data direction: SEC-018. Datastore
pooling: DB-012. Deploy mechanics over this infrastructure: CI-003…009. Health signals consumed
by platforms: OBS-007. Operating all of it: [operations.md](operations.md). Ownership map:
PLAYBOOK-ARCHITECTURE.md §6.

## Retirement log

None.
