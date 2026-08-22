# Application Standard (APP)

> **Class:** Standard · **Rule prefix:** `APP` · **Status:** Active
> **Purpose:** how application behavior is structured at runtime — the cross-platform rules every
> deployable needs regardless of being web, mobile-backend, or service.
> **Owns:** configuration handling, failure behavior (timeouts, retries, degradation, circuit
> breaking, fault containment), idempotency, transactions/state integrity, concurrency discipline,
> feature flags.
> **Does not own:** structural boundaries ([architecture.md](architecture.md)); code-level error
> style ([coding.md](coding.md)); authn/z and input validation at trust boundaries
> (`standards/security.md`, Phase 3); logging/metrics duties (`standards/observability.md`,
> Phase 3); API error shapes (`standards/api.md`, Phase 3); browser/mobile specifics (Phase 4).
> **Gate:** code review.

Non-normative context: "external dependency" means anything reached over a process boundary —
databases, third-party APIs, queues, other services. These rules operationalize
[P-6 Design for failure](../principles/engineering-principles.md) at the application layer.

## Rules

### APP-001: An application artifact MUST be buildable once and deployable to every environment without modification.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Environment-specific builds mean the artifact you tested is not the artifact you run; all environment variance belongs in supplied configuration ([P-2](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### APP-002: Configuration MUST be validated at startup, and validation failure MUST prevent the application from starting.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A missing or malformed setting discovered at first use fails at an arbitrary time under arbitrary load; failing at startup fails loudly, immediately, and before traffic ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for settings that are genuinely optional with safe defaults

### APP-003: Every external dependency MUST have a defined failure mode — fail-fast or degraded operation — decided at design time.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** When the cache is down, does the app serve slower or serve errors? Undecided means decided by accident during the incident ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### APP-004: Every call to an external dependency MUST have an explicit timeout.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A call without a timeout is an unbounded resource hold; defaults are often infinite, and one slow dependency then stalls the whole application ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### APP-005: Automatic retries MUST be bounded in both attempt count and total elapsed time, with backoff between attempts.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Unbounded or immediate retries turn a dependency's bad minute into a self-inflicted denial of service ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### APP-006: An operation that can execute more than once — via retry, redelivery, or resubmission — MUST be idempotent or protected by deduplication.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** At-least-once execution is the reality of retried calls, queue consumers, and background jobs; without idempotency, "resilient" mechanisms silently double-charge and double-write ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** operations proven to execute at most once by construction

### APP-007: A business operation that performs multiple state changes MUST guarantee atomicity or define explicit compensation for partial failure.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Partial completion is the worst outcome — neither the old state nor the new one; either the changes commit together or the design states how the system recovers ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where inconsistency is tolerable and documented

### APP-008: Business invariants MUST be enforced in the domain or application layer, not solely at the interface layer.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Every interface (UI, API, job, admin script) is a path to the same state; an invariant enforced only in one path is not an invariant. Trust-boundary input *sanitization* is separate and owned by `standards/security.md` (Phase 3) ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### APP-009: Entities with lifecycle state MUST reject transitions not explicitly defined as valid.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Allow-by-default state machines accumulate impossible states (shipped-but-unpaid) that every consumer must then defend against ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for entities with trivial state

### APP-010: Shared mutable state accessed concurrently MUST be protected by synchronization or redesigned to avoid sharing.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Data races are heisenbugs — invisible in tests, catastrophic under production concurrency ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### APP-011: A feature flag's default state MUST be the safe, pre-existing behavior.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Flag systems fail, configs get lost, and new environments start from defaults; default-on new behavior turns those events into unreviewed launches ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### APP-012: Every feature flag MUST have an owner and a removal condition recorded at creation.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Flags are temporary by design; unowned flags become permanent config nobody dares touch, doubling the state space of the application ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for permanent operational kill-switches, which are declared as such

### APP-013: Calls to an external dependency that is persistently failing SHOULD be suspended automatically until a controlled probe succeeds (circuit breaking).

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Timeouts (APP-004) and bounded retries (APP-005) limit the cost of each attempt but still send every new request into a dependency that is down; suspending calls fails fast, sheds load the dependency cannot serve, and gives it room to recover ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation — e.g., the dependency's declared failure mode (APP-003) is fail-fast for the whole application, or call volume is too low for persistent failure to compound

### APP-014: A failure in one feature SHOULD be contained so that features not depending on it remain operational (fault containment).

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A single deployable hosts many features; without containment — feature-scoped error handling, isolated resource pools, kill switches per APP-012 — one feature's defect becomes a whole-application outage ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for genuinely interdependent features, recorded with the dependency stated

## Interaction with other standards

The isolation points where these behaviors live are placed by ARCH-005. Application-level fault
containment (APP-014) is distinct from infrastructure redundancy and single-point-of-failure
decisions, which are owned by INFRA-017. Testing of failure modes
required here is governed by TEST-010. Authorization boundaries are owned by `standards/security.md`
(Phase 3); this standard deliberately defines no authorization rules.

## Retirement log

None.
