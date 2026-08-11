# API Standard (API)

> **Class:** Standard · **Rule prefix:** `API` · **Status:** Active
> **Purpose:** contract discipline for APIs — what any API style must satisfy to be consumable,
> evolvable, and safe.
> **Owns:** contract-first duty, versioning and breaking-change policy, error contract, request
> validation semantics, pagination/filtering conventions, idempotency declaration, deprecation,
> protocol-semantics fidelity, naming consistency.
> **Does not own:** authn/z ([security.md](security.md) SEC-001…003), rate limiting (SEC-023),
> idempotent *behavior* ([application.md](application.md) APP-006), correlation propagation
> ([observability.md](observability.md) OBS-003/004), contract *tests*
> ([testing.md](testing.md) TEST-007).
> **Gate:** code review; API design semantics reviewed at architecture review when a
> cross-component contract changes (DOC-003 trigger 5); `public-api` trigger rules bind
> externally consumed contracts.

Non-normative context: no API style is prescribed. Resource-oriented HTTP, RPC, and query-language
styles are all acceptable; these rules are the requirements any of them must satisfy. Where a
project picks a style and protocol, that is an ADR (DOC-003 trigger 1). "Published contract" means
the machine-readable definition consumers rely on.

## 1. Rules

### API-001: Every exposed API MUST be defined by a machine-readable contract stored in the owning repository.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** api-service
- **Rationale:** The contract is the single source of truth consumers, tests (TEST-007), docs, and breaking-change tooling all hang off; an API defined only by its implementation is defined by accident ([P-3](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### API-002: A breaking change MUST NOT be made within an existing API version.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** api-service, public-api
- **Rationale:** Consumers program against the contract a version promises; a break inside a version converts every consumer deployment into a coin flip. Breaking changes ship as a new version with the old one deprecated per API-004 ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### API-003: Every API MUST declare its versioning scheme in its contract.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Consumers cannot plan for change they cannot see coming; the scheme (path, header, field — any works) matters less than its declaration ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### API-004: A deprecated API element MUST remain functional until its published removal date.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service, public-api
- **Rationale:** Deprecation is a contract about time; removing early is a breaking change wearing a process costume. Replacement documentation is DOC-004 ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### API-005: Error responses MUST use the standard error contract defined in §2.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** A single error shape lets every consumer, gateway, and agent handle failure generically instead of parsing per-endpoint prose ([P-10](../principles/engineering-principles.md), [P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where a protocol mandates its own error format — the mandated format then carries the same information

### API-006: Error responses MUST NOT expose internal implementation details.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Stack traces, query text, and infrastructure identifiers are reconnaissance gifts; the diagnostic detail belongs in telemetry (OBS-006), correlated by identifier, not in the response ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### API-007: Invalid requests MUST be rejected with a client-error result that identifies each invalid element.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** "Bad request" without which field forces consumers into guess-and-resubmit loops; validation itself is SEC-005 — this rule owns the response semantics ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where enumeration would aid an attacker (auth endpoints), per security review

### API-008: Collection-returning operations MUST be paginated.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Unpaginated collections work until the table grows, then take down client and server together; pagination retrofitted later is a breaking change (API-002) ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** collections with a documented, structurally bounded size

### API-009: Filtering, sorting, and pagination parameters SHOULD follow one convention declared in the contract.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Per-endpoint invention multiplies consumer code and agent context for zero benefit ([P-10](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### API-010: Every mutating operation MUST document its idempotency behavior in the contract.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Consumers implementing retries (APP-005) need to know whether repeat is safe or needs an idempotency key; the *behavior* is APP-006 — this rule owns its declaration ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### API-011: An API built on a protocol with standardized semantics MUST use those semantics as specified.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Methods, status codes, and error signaling carry meaning every client, cache, proxy, and tool already understands; a 200-with-error-body defeats all of them. Example (non-normative): HTTP GET is safe and cacheable — a GET that mutates breaks the internet's assumptions ([P-10](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation, declared in the contract

### API-012: Naming within an API MUST follow one convention declared in the contract.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Mixed `userId`/`user_id`/`UserID` in one API is a permanent consumer tax; which convention matters less than there being exactly one ([P-10](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for fields pass-through from external systems

### API-013: Update operations on concurrently editable resources SHOULD support optimistic concurrency control.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Without a version/precondition mechanism, last-write-wins silently destroys concurrent edits; declared isolation expectations at the datastore are DB-007 ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## 2. Standard error contract (normative content of API-005)

Every error response carries, in the protocol's natural encoding:

| Field | Content |
|---|---|
| `code` | Stable, machine-readable error identifier (documented in the contract; never changes meaning within a version) |
| `message` | Human-readable summary, safe for display, free of internal detail (API-006) |
| `correlation_id` | The request's correlation identifier (OBS-003), for support and telemetry lookup |
| `details` | Optional array of per-element problems — for validation errors, one entry per invalid element (API-007) |

Consumers program against `code`; `message` text is never a contract.

## Interaction with other standards

Authentication/authorization of endpoints: SEC-001…003. Abuse controls: SEC-023. Retry behavior
and idempotency implementation: APP-005/006. Correlation identifiers: OBS-003/004. Contract test
duty: TEST-007. Reference documentation generated from the contract satisfies DOC-001's
API-facing needs; contract changes to externally consumed APIs are an ADR trigger (DOC-003
trigger 5) and a security-review trigger when they cross trust boundaries (SEC-026 trigger 5).

## Retirement log

None.
