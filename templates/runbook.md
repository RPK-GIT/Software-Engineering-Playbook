# Runbook — Service Name

<!--
Template satisfying OPS-004. Written for the responder who did not build the service, at 3 a.m.,
under pressure: exact commands, exact dashboard links, no prose that doesn't help. Lives in the
service repository (DOC-007). Re-verify after incidents and on schedule (OPS-005).
Delete comments before committing.
-->

- **Service:** <!-- name + one-line purpose -->
- **Operational owner:** <!-- team/role per OPS-001 -->
- **Escalation path:** <!-- who's next when the responder is stuck, with response expectations (OPS-003) -->
- **Last verified:** YYYY-MM-DD <!-- by whom; OPS-005 -->

## Quick links

<!-- Dashboard, logs (filtered to this service), alert console, change log (OPS-009), deploy
pipeline, threat model. Every link the responder would otherwise have to hunt for. -->

## What this service does

<!-- Two or three sentences: purpose, criticality, who is affected when it breaks. -->

## Dependencies

| Dependency | Failure mode (per APP-003) | What breaks here when it's down |
|---|---|---|

## Health indicators

<!-- How to tell it's healthy in 60 seconds: liveness/readiness endpoints (OBS-007), the
baseline metrics and their normal ranges (OBS-008), one known-good log pattern. -->

## Alerts and responses

<!-- One row per configured alert (OBS-010). If an alert has no runbook entry, the alert or the
runbook is defective. -->

| Alert | Meaning | First response |
|---|---|---|

## Diagnosis

<!-- Ordered checks from cheapest to deepest: recent changes first (OPS-009), then correlation-ID
trace through the stack (OBS-003), then dependency health (OPS-010). Exact commands/queries. -->

## Known failure modes

<!-- From DOC-008 and past incidents. Symptom -> cause -> remediation, one block each. -->

## Remediation actions

<!-- Safe actions the responder may take, with exact commands: restart, scale, flag off
(APP-011), shed load (INFRA-014). Mark clearly anything requiring authorization (INFRA-007). -->

## Rollback and recovery

<!-- How to roll back a deployment (CI-008), current migration rollback constraints (DB-002),
how to invoke restore/DR if data is involved (INFRA-024/026), and how to verify recovery
(CI-007, OBS-008). -->

## Verification after any action

<!-- The specific checks that prove the service is actually healthy again — not just quiet. -->
