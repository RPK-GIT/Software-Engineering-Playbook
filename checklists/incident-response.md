# Incident Response Checklist

> **Class:** Instrument (view) · **Gate:** an incident is declared · **Status:** Active
> Response, not analysis — the postmortem ([templates/postmortem.md](../templates/postmortem.md))
> happens after recovery, never during. Severity model: [operations.md](../standards/operations.md) §2.
> Work top to bottom; steps cite their authoritative rules (RULE-008).

## Detect and declare

- [ ] Declare the incident — an unowned anomaly is not being handled; declaring cheap and closing fast beats hesitating
- [ ] Classify severity against the model; reclassify as understanding changes — OPS-006
- [ ] SEV1/SEV2: designate the incident lead and open the single communication channel — OPS-007
- [ ] Consult the service runbook first — OPS-004

## Triage

- [ ] Establish user impact: who, what, how many — this drives severity and comms
- [ ] Check the change log: what deployed, migrated, flipped, or reconfigured recently? — OPS-009
- [ ] Follow correlation IDs through telemetry to localize the failure — OBS-003, OBS-004
- [ ] Check critical dependency health before assuming the fault is local — OPS-010

## Contain and mitigate

- [ ] Stop ongoing damage first (data corruption, cascading load, active exposure) — containment before diagnosis
- [ ] Prefer revert/rollback over fixing forward — GIT-011, CI-008; mind rollback limits from applied migrations — DB-002
- [ ] Use flags to disable the failing path where they exist — APP-011
- [ ] Shed load rather than degrade unboundedly if capacity is the problem — INFRA-014
- [ ] Escalate on stall — the path exists to be used — OPS-003

## If security is involved (suspected breach, exposure, injection)

- [ ] Treat as SEV1 until proven otherwise — OPS-006 (§2: breach enters at SEV1)
- [ ] Rotate any secret suspected of exposure immediately; record it — SEC-011
- [ ] Preserve evidence: logs, access records, artifacts — do not destroy state the investigation needs; audit events are your record — SEC-022
- [ ] Restrict access before restoring service if the entry vector is still open — SEC-001, INFRA-007, INFRA-008

## Communicate

- [ ] Post regular status to the incident channel: known impact, current action, next update time — OPS-007
- [ ] Inform customer-facing stakeholders at SEV1/SEV2; facts and impact only, no speculation
- [ ] Log key decisions and timestamps as you go — the postmortem timeline is built from this, not from memory

## Recover and validate

- [ ] Restore service; run post-deployment verification, not vibes — CI-007
- [ ] Confirm baseline metrics and error rates returned to normal — OBS-008
- [ ] Verify data integrity where data was at risk; invoke restore/DR machinery if needed — INFRA-024, INFRA-026
- [ ] Watch for recurrence before standing down

## Close

- [ ] Declare resolution in the channel with final impact summary
- [ ] File the postmortem for SEV1/SEV2 — mandatory, blameless — OPS-008
- [ ] Capture runbook gaps found during response — OPS-005
- [ ] Convert temporary mitigations (flags, capacity bumps, disabled features) into tracked work items — nothing "temporary" survives untracked
