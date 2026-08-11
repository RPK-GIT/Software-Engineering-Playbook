# Observability Standard (OBS)

> **Class:** Standard · **Rule prefix:** `OBS` · **Status:** Active
> **Purpose:** authoring-time telemetry duties — what code must emit so production behavior is
> explainable without a debugger. Placed with development standards deliberately: telemetry is
> written with the code (P-7), not bolted on at deployment.
> **Owns:** log structure and level semantics, correlation propagation, telemetry content limits,
> error capture, health signals, baseline metrics, tracing, alert design principles, SLO duty.
> **Does not own:** which security events must exist ([security.md](security.md) SEC-022);
> error-message content in code ([coding.md](coding.md) CODE-006); API error responses
> ([api.md](api.md) API-005/006); monitoring infrastructure and dashboards
> (`standards/infrastructure.md`, Phase 5); on-call, runbooks, incident process
> (`standards/operations.md`, Phase 5). No vendor or telemetry product is prescribed.
> **Gate:** code review.

## 1. Telemetry taxonomy (non-normative, referenced by the rules)

- **Logs** — discrete, timestamped records of things that happened, optimized for search and
  diagnosis. Answer: *what happened here?*
- **Metrics** — pre-aggregated numeric time series, optimized for trends and alerting. Answer:
  *how is it behaving over time?*
- **Traces** — the causally linked path of one request across components/services. Answer:
  *where did the time or failure go?*
- **Events** — significant state changes (deploy, flag flip, migration, security event) recorded
  as structured facts; security events are required by SEC-022, and events are emitted as
  structured logs unless a project ADR chooses a dedicated channel.

## 2. Rules

### OBS-001: Application logs MUST be emitted in a structured, machine-parseable format.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Prose logs are grep-and-hope; structured fields make every downstream capability — search, correlation, masking verification, alerting — mechanical ([P-7](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for interactive CLI output, which is a user interface rather than telemetry

### OBS-002: Log entries MUST use severity levels according to the semantics defined in §3.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Levels are an interface for filtering and alerting; when ERROR sometimes means "broken" and sometimes "Tuesday", alerting on it is impossible ([P-2](../principles/engineering-principles.md), [P-10](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OBS-003: A correlation identifier MUST be assigned to every unit of work at its entry point and propagated across every component and service boundary it crosses.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Correlation is the thread that turns isolated telemetry into a narrative; it cannot be retrofitted at read time. API error responses expose it (API-005's `correlation_id`), incoming identifiers from trusted callers are honored rather than replaced ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OBS-004: All telemetry emitted while handling a unit of work MUST carry that work's correlation identifier.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Propagation (OBS-003) is worthless if the logs, metrics exemplars, and traces don't actually carry the identifier — this is the attachment half of the same contract ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for aggregate-only metrics where per-work attribution is structurally impossible

### OBS-005: Telemetry MUST NOT contain secrets, credentials, or unmasked PII.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Telemetry systems have the widest read access and longest retention in the company — logging a secret revokes SEC-009's protections in one line; PII in telemetry silently extends SEC-015's scope to every log reader ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### OBS-006: Unhandled errors MUST be captured and reported with stack context to a monitored destination.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** An unhandled error that only the user sees is a defect report you paid for and threw away; "monitored" means someone or something actually consumes it — error *content* rules are CODE-006, response exposure limits API-006 ([P-7](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### OBS-007: Every deployed service MUST expose liveness and readiness signals, with readiness reflecting genuine ability to serve.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service, web
- **Rationale:** Orchestration and load balancing route traffic on these signals; a readiness check that ignores a dead required dependency routes traffic into a black hole ([P-6](../principles/engineering-principles.md)). Fatal-vs-degradable dependency decisions come from APP-003.
- **Exceptions:** justified-deviation for execution models where the platform owns health signaling

### OBS-008: Every deployed service MUST emit baseline operational metrics: request rate, error rate, latency distribution, and saturation of its constrained resources.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service, web
- **Rationale:** These four answer "is it healthy, is it fast, is it about to fall over" for any service whatsoever; everything beyond them is per-domain judgment, these are the floor ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OBS-009: Services participating in multi-service request flows SHOULD emit distributed traces.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** api-service
- **Rationale:** Once a request crosses services, logs alone cannot show where time and failure went; SHOULD-level because a single deployable (the ARCH-009 default) gets most of the value from OBS-003/004 without tracing infrastructure ([P-7](../principles/engineering-principles.md), [P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OBS-010: Every alert MUST indicate an actionable condition.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Alerts that fire without requiring action train responders to ignore alerts — alert fatigue is how real incidents get slept through; conditions worth knowing but not acting on are dashboards, not alerts. Runbook linkage arrives with Phase 5 ([P-7](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### OBS-011: User-facing services SHOULD define service-level objectives for availability and latency.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** api-service, web
- **Rationale:** An SLO converts "is it good enough?" from opinion into measurement, and gives alerting (OBS-010) an objective threshold; SHOULD-level until operational maturity practices arrive in Phase 5 ([P-1](../principles/engineering-principles.md), [P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## 3. Log level semantics (normative content of OBS-002)

| Level | Meaning | Consequence |
|---|---|---|
| ERROR | The operation failed and requires attention — data at risk, user impacted, invariant broken | Feeds error reporting (OBS-006); candidate for alerting |
| WARN | Something abnormal that the system handled — degraded mode entered, retry succeeded, deprecated path used | Reviewed in trends; never routine noise |
| INFO | Significant lifecycle facts — started, stopped, config loaded, unit of work completed | The default production level |
| DEBUG | Diagnostic detail for development and targeted investigation | Off in production by default; enabling it is a deliberate act |

An entry that "happens on every request and means nothing is wrong" is INFO or DEBUG by
definition, whatever severity feels satisfying.

## Interaction with other standards

Security events that must exist: SEC-022 (this standard owns their *format* via OBS-001/002).
Telemetry content limits enforce SEC-009/SEC-015 in the telemetry channel (OBS-005). Failure-mode
decisions surfacing in readiness: APP-003. Correlation exposure to API consumers: API-005.
Dashboards, monitoring infrastructure, on-call and alert routing: Phase 5.

## Retirement log

None.
