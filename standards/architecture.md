# Architecture Standard (ARCH)

> **Class:** Standard · **Rule prefix:** `ARCH` · **Status:** Active
> **Purpose:** structural rules that keep systems understandable, changeable, and safe to evolve —
> concrete enough for an AI coding agent to apply and a reviewer to check.
> **Owns:** layering, boundaries, dependency direction, coupling, data ownership, when-to-split.
> **Does not own:** technology choices (ADRs via DOC-003), code-level construction
> ([coding.md](coding.md)), runtime behavior ([application.md](application.md)), API contract rules
> (`standards/api.md`, Phase 3), infrastructure topology (`standards/infrastructure.md`, Phase 5).
> **Gate:** architecture review — any change that alters component boundaries, dependencies between
> components, or data ownership.

Non-normative context: the default architecture is a single deployable with well-separated internal
components. Distribution, messaging, caching layers, and other architectural machinery are costs
that must be justified by requirements, not aspirations ([P-11](../principles/engineering-principles.md),
[P-4](../principles/engineering-principles.md)). "Component" means any separately owned unit of
code with a declared boundary — a module, package, or service.

## Rules

### ARCH-001: Every component MUST have one clearly stated responsibility, recorded where the component is defined.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A component whose responsibility cannot be stated in one sentence cannot be reasoned about, tested at its boundary, or safely changed ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### ARCH-002: Domain logic MUST be separated from delivery mechanisms and infrastructure concerns.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Business rules outlive transports, frameworks, and datastores; mixing them couples the longest-lived code to the shortest-lived ([P-8](../principles/engineering-principles.md)). Example (non-normative): an order-pricing calculation does not import an HTTP framework or a database driver.
- **Exceptions:** waiver-only

### ARCH-003: Domain logic MUST NOT depend on concrete delivery or infrastructure implementations.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Dependency direction runs inward: delivery and infrastructure depend on the domain, never the reverse; where the domain needs a capability (persistence, time, messaging), it depends on an interface it owns ([P-2](../principles/engineering-principles.md), [P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### ARCH-004: Components MUST interact only through each other's declared public interfaces.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Reaching into another component's internals creates coupling invisible at the boundary, making every internal change a potential breaking change ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### ARCH-005: Every integration with an external system MUST be isolated behind an interface owned by this codebase.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Third-party APIs and services change on their own schedule; an owned adapter makes the blast radius of that change one file wide and gives failure handling a single home ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### ARCH-006: Component boundaries and their allowed dependency directions MUST be declared in a machine-checkable form.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Boundary rules that live only in reviewers' heads erode one convenient import at a time; a declared dependency graph lets CI reject violations deterministically ([P-9](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)). The declaration format is per-project tooling; the obligation is its existence and CI enforcement.
- **Exceptions:** waiver-only

### ARCH-007: Every persistent datastore or schema MUST have exactly one owning component through which all writes flow.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Shared write access to a schema couples every writer to every other writer's assumptions and makes migrations unownable ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### ARCH-008: Architectural mechanisms MUST NOT be introduced for requirements that do not yet exist.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Speculative queues, caches, plugin systems, and abstraction layers are permanent costs paid for hypothetical benefits; the simplest architecture satisfying current, known requirements is the default ([P-11](../principles/engineering-principles.md), [P-4](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation is not available — a real, recorded requirement (ADR per DOC-003) is the only path

### ARCH-009: A component MUST NOT be extracted into a separately deployed service unless a recorded requirement cannot be met within the existing deployable.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Distribution converts function calls into network calls, adding latency, partial failure, versioning, and operational surface; the requirement forcing that trade (independent scaling, isolation, team topology) is recorded as an ADR per DOC-003 ([P-6](../principles/engineering-principles.md), [P-11](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

## Interaction with other standards

Structural decisions that qualify as ADR triggers are governed by DOC-003. Boundary declarations
(ARCH-006) are verified in CI per the [enforcement matrix](../governance/enforcement-matrix.md).
Failure-handling behavior *within* the isolation points required here is owned by
[application.md](application.md) (APP-003…APP-006).

## Retirement log

None.
