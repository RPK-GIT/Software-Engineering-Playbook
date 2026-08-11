# Production Readiness Checklist

> **Class:** Instrument (view) · **Gate:** first production deployment of a service, and major
> changes thereafter · **Status:** Active
> The cross-domain aggregation gate: nothing here is a new rule — every item cites its
> authoritative RULE-ID (RULE-008). Filter by profile tags. Sign-off: the operational owner
> (OPS-001) and, where SEC-026 triggers fired, the security reviewer.

## Architecture

- [ ] Component responsibilities stated; boundaries declared machine-checkably — ARCH-001, ARCH-006
- [ ] External dependencies isolated behind owned adapters — ARCH-005
- [ ] No unjustified distribution or speculative mechanisms; SPOFs identified, accepted ones in ADRs — ARCH-008, ARCH-009, INFRA-017
- [ ] Datastore has exactly one owning component — ARCH-007

## Security

- [ ] Threat model exists, current, signed off — SEC-027
- [ ] Entry points authenticated or explicitly public; per-resource authorization — SEC-001, SEC-002
- [ ] Secrets delivered via secret management, rotatable; none in repo or artifacts — SEC-009, SEC-010, REPO-002
- [ ] Scans wired and green: dependencies, secrets, images where used — SEC-019, SEC-020, INFRA-020; severity gate active — SEC-028
- [ ] Data classified; encryption at rest/transit per classification; retention declared — SEC-014, SEC-016, SEC-017, DB-011
- [ ] Abuse controls on public endpoints — SEC-023

## API and data (profile-dependent)

- [ ] Contract published, versioned, error contract implemented — API-001, API-003, API-005
- [ ] Migrations versioned, rollback-defined, compatible with running code, pipeline-applied — DB-001, DB-002, DB-004, CI-009
- [ ] Production query patterns index-verified; bounded connection pool — DB-008, DB-012

## Testing

- [ ] Integration coverage at every external boundary; contract tests where contracts exist — TEST-006, TEST-007
- [ ] Critical journeys covered end-to-end; declared failure modes exercised — TEST-008, TEST-010
- [ ] Suite deterministic and quarantine-clean — TEST-003, TEST-013

## Observability

- [ ] Structured logs, correct levels, correlation propagated and attached — OBS-001…004
- [ ] No sensitive data in telemetry — OBS-005
- [ ] Unhandled-error capture to a monitored destination — OBS-006
- [ ] Liveness/readiness honest; baseline metrics emitted — OBS-007, OBS-008
- [ ] Alerts actionable and routed to responders — OBS-010, OPS-002

## Deployment and infrastructure

- [ ] Full CI check set runs per matrix; artifacts built once, versioned, pipeline-built — CI-001…005
- [ ] Promotion sequence declared; post-deploy verification automated — CI-006, CI-007
- [ ] Rollback procedure defined and exercised at least once — CI-008
- [ ] Release model and deployment strategy declared — CI-010, CI-011
- [ ] Infrastructure as reviewed code; prod isolated; access restricted and audited — INFRA-001, INFRA-005, INFRA-007
- [ ] Deny-by-default exposure; automated cert renewal; resource bounds; graceful shutdown — INFRA-008, INFRA-009, INFRA-015, INFRA-016
- [ ] Overload shedding at entry points; scaling strategy declared — INFRA-014, INFRA-013

## Backup and recovery

- [ ] RPO/RTO declared in an ADR; backup schedule derives from them — INFRA-023, INFRA-022
- [ ] Backups encrypted and isolated; a restore has actually been performed — INFRA-025, INFRA-024
- [ ] DR procedure validated against objectives — INFRA-026

## Operations

- [ ] Named operational owner; escalation path where committed — OPS-001, OPS-003
- [ ] Runbook exists covering alerts and failure modes — OPS-004
- [ ] Severity model understood by the team; incident checklist at hand — OPS-006, [incident-response](incident-response.md)
- [ ] Change log capturing deploys, migrations, config, flags — OPS-009
- [ ] Critical dependency health monitored — OPS-010

## Documentation

- [ ] README enables build/test/run; config keys documented — DOC-001, DOC-005
- [ ] ADRs current for every trigger hit on the way here — DOC-003
- [ ] Cost attribution in place; spend visible — INFRA-027, INFRA-028
