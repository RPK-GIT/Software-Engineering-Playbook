# Postmortem — Incident Title

<!--
Template satisfying OPS-008. BLAMELESS is load-bearing: the unit of analysis is the system —
processes, tooling, signals, defenses — never the individual. People acted reasonably on the
information they had; if a reasonable action broke production, the system made that action
possible. Names appear only in the timeline as roles. A postmortem that produces blame produces
hidden truth next time.
Write it within days of resolution, while memory is fresh. Delete comments.
-->

- **Incident date / duration:** <!-- start -> resolved, timezone -->
- **Severity:** <!-- per operations.md §2, final classification -->
- **Author(s):** · **Review date:** <!-- postmortem review, not incident date -->
- **Status:** Draft <!-- Draft | Reviewed | Actions tracked -->

## 1. Summary

<!-- Three sentences: what broke, what the impact was, what the trigger turned out to be. -->

## 2. Impact

<!-- Quantified: users affected, duration, requests failed, data at risk, SLO/error-budget
consumption (OBS-011), support volume. Customer impact stated plainly. -->

## 3. Timeline

<!-- Timestamped facts from the incident channel and change log (OPS-009, OPS-007) — detection,
declaration, key decisions, mitigation, recovery. Roles, not names. Include the gap between
impact start and detection: that gap is a finding. -->

| Time | Event |
|---|---|

## 4. Detection

<!-- How did we find out — alert (which?), customer report, luck? If telemetry existed but didn't
alert, or alerted and was ignored, say so (OBS-010, OPS-002). -->

## 5. Root and contributing factors

<!-- Usually several factors, not one villain: the defect, the conditions that let it reach
production (which gate should have caught it?), the conditions that amplified it, the reasons
detection/recovery took as long as they did. Cite the rules whose enforcement would have helped —
that feeds §9. -->

## 6. Response assessment

**What worked:** <!-- runbook entries that helped, rollback that executed, alerts that fired true -->

**What failed or was missing:** <!-- stale runbook steps (OPS-005), missing telemetry, unclear
escalation, rollback blocked by a migration (DB-002) -->

## 7. Recovery

<!-- What actually restored service; how recovery was verified (CI-007, OBS-008); any temporary
mitigations still in place and their tracked work items. -->

## 8. Security implications

<!-- Was data exposed? Were secrets involved (SEC-011 executed?)? Does the threat model need
updating (SEC-027)? "None identified" is an acceptable answer; silence is not. -->

## 9. Corrective actions

<!-- Each action: specific, owned, dated, tracked. "Be more careful" is not an action; a new
gate, alert, runbook entry, or rule change is. If a playbook rule gap contributed, the action is
an RFC (governance/change-process.md). -->

| # | Action | Type (prevent / detect / mitigate) | Owner | Due | Work item |
|---|---|---|---|---|---|

## 10. Lessons learned

<!-- What this incident taught about the system that the team didn't know before — including
what to keep doing because it worked. -->

## 11. Verification

<!-- How and when we'll confirm the corrective actions actually closed the gap — checked at the
quarterly review (change-process.md §4) and at each action's due date. -->
