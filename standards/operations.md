# Operations Standard (OPS)

> **Class:** Standard · **Rule prefix:** `OPS` · **Status:** Active
> **Purpose:** what it takes to *run* production software: ownership, monitoring duty, on-call,
> runbooks, incident management, change visibility, capacity.
> **Owns:** operational ownership, alert routing and escalation, runbook duties, the incident
> severity model and process, postmortem duty, production change records, capacity and
> maintenance cadences, dependency health monitoring.
> **Does not own:** telemetry requirements ([observability.md](observability.md) owns what
> signals exist and their quality — this standard owns how they are *used* operationally);
> security event content ([security.md](security.md) SEC-022); deployment mechanics
> ([ci-cd.md](ci-cd.md)); platform capabilities ([infrastructure.md](infrastructure.md)).
> **Gate:** production-readiness gate before first deploy; incident and postmortem processes
> thereafter.

## 1. Rules

### OPS-001: Every production service MUST have a named operational owner.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Every other rule in this standard needs someone it binds; an unowned service is operated by whoever notices, which under pressure is nobody ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### OPS-002: Alerts on production services MUST route to a defined responder path.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** An alert with no responder is a log line with anxiety; OBS-010 makes alerts actionable — this rule ensures someone is positioned to act ([P-7](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### OPS-003: Services with availability commitments MUST have a defined escalation path with response-time expectations.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** When the first responder is unavailable or out of depth, the path upward must be known in advance — escalation invented mid-incident costs the minutes the commitment promised away ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** not applicable to services with no declared availability commitment (OBS-011)

### OPS-004: Every production service MUST have a runbook covering its alerts and known failure modes.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** At 3 a.m. the responder is rarely the author; the runbook ([templates/runbook.md](../templates/runbook.md)) is DOC-008's failure-mode knowledge made executable, linked from the alerts it serves ([P-6](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OPS-005: Runbooks MUST be re-verified after every incident that exposes a gap and on a periodic schedule.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** A runbook that no longer matches the system is worse than none — it burns incident minutes on stale instructions; the incident that found the gap is the trigger to fix it (DOC-002's freshness duty, operationalized) ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OPS-006: Incidents MUST be classified against the severity model in §2 at declaration and reclassified as understanding changes.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Severity drives response, communication, and follow-up duties mechanically; without a shared model every incident is negotiated while it burns ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### OPS-007: Every SEV1 or SEV2 incident MUST have a designated incident lead and a single communication channel for its duration.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Uncoordinated response duplicates work and contradicts itself in front of stakeholders; one lead owns decisions, one channel owns truth ([templates against chaos: checklists/incident-response.md](../checklists/incident-response.md)) ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### OPS-008: Every SEV1 or SEV2 incident MUST produce a blameless postmortem with tracked corrective actions.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** An incident paid for and not learned from will be paid for again; blameless is load-bearing — punished honesty produces hidden truth and repeat incidents ([templates/postmortem.md](../templates/postmortem.md)) ([P-1](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### OPS-009: Every production change — deployment, migration, configuration, feature flag — MUST be recorded in an auditable change log.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** "What changed?" is the first incident question; a queryable change record correlated with telemetry (OBS-003's identifiers, event taxonomy §1) answers it in seconds — most of it falls out of pipelines (CI-004) and flag systems for free ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OPS-010: Availability of critical external dependencies MUST be monitored.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** APP-003 decided what happens when the dependency fails; knowing *that it is failing* — before users report it — is the operational half of that decision ([P-7](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OPS-011: Capacity SHOULD be reviewed against growth trends on a schedule.

- **Level:** SHOULD
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Saturation metrics (OBS-008) show today; capacity review extrapolates to the quarter — the goal is buying headroom on purpose instead of during an incident ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### OPS-012: Routine maintenance — patching, upgrades, certificate and dependency currency — SHOULD follow a declared schedule.

- **Level:** SHOULD
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Unscheduled maintenance is deferred maintenance, and deferred maintenance is how systems become unupgradable; a cadence keeps each step small (P-8) ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## 2. Incident severity model (normative content of OPS-006)

| Severity | Definition | Response | Postmortem |
|---|---|---|---|
| **SEV1** | Production down or unusable for most users; data loss occurring; active security breach | Immediate, all-hands as needed; incident lead + channel (OPS-007); stakeholder comms | Required (OPS-008) |
| **SEV2** | Major degradation: core journey impaired, significant user subset affected, no acceptable workaround | Urgent response within escalation expectations (OPS-003) | Required (OPS-008) |
| **SEV3** | Minor degradation: non-core impairment or acceptable workaround exists | Normal-hours response; tracked work item | Optional |
| **SEV4** | Cosmetic or negligible-impact defect noticed operationally | Backlog | No |

Security incidents enter at the severity their impact warrants — an active breach is SEV1
regardless of user-visible symptoms; secret exposure triggers SEC-011 in parallel.

## Interaction with other standards

What signals exist and their quality: OBS-001…011 (this standard consumes them). Which security
events exist: SEC-022. Deployment verification and rollback machinery used during incidents:
CI-007/008. Backup/DR machinery invoked in recovery: INFRA-022…026. Incident-time process:
[checklists/incident-response.md](../checklists/incident-response.md); readiness to operate at
all: [checklists/production-readiness.md](../checklists/production-readiness.md).

## Retirement log

None.
