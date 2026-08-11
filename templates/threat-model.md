# Threat Model — System / Feature Name

<!--
Template satisfying SEC-027. Usable by a human engineer or an AI coding agent; an agent may draft
every section but the sign-off is human-only (an agent approving its own threat model violates
AGENT-007's spirit and the sign-off rules below).
Method: structured brainstorming per trust boundary and data flow. STRIDE (Spoofing, Tampering,
Repudiation, Information disclosure, Denial of service, Elevation of privilege) is the suggested
lens per element; any systematic method is acceptable. No commercial tool is required.
Keep it living: update on SEC-027 triggers, don't rewrite.
Delete comments before submitting.
-->

- **Status:** Draft <!-- Draft | Reviewed | Approved -->
- **Date / last updated:** YYYY-MM-DD
- **Author(s):** <!-- human or AI agent (drafting) -->
- **Scope:** <!-- what this model covers and explicitly does not -->

## 1. System overview

<!-- One paragraph + a diagram (text/ASCII is fine): components, datastores, external parties. -->

## 2. Assets

<!-- What an attacker wants and what you must protect. Include data classes (cite SEC-014
classifications), credentials/secrets, availability of critical journeys, and trust itself
(e.g., the integrity of what you display to users). -->

| Asset | Classification | Why it matters |
|---|---|---|

## 3. Actors

<!-- Who interacts: legitimate roles, service principals, and attacker profiles worth modeling
(anonymous internet, authenticated user, malicious tenant, compromised dependency, insider). -->

## 4. Trust boundaries and entry points

<!-- Every point where privilege or trustworthiness changes: network entry points, user input,
third-party callbacks/webhooks, file uploads, queues, admin interfaces. Each entry point cites
its authentication posture (SEC-001) — public entry points listed explicitly. -->

| # | Boundary / entry point | Auth posture | Notes |
|---|---|---|---|

## 5. Data flows

<!-- The paths sensitive data takes across boundaries, including into telemetry and third
parties. A numbered list matching the diagram is enough. -->

## 6. Threats and attack scenarios

<!-- Per boundary/flow, what could go wrong - apply STRIDE or equivalent per element. Write
scenarios concretely: actor -> action -> impact. Rate likelihood/impact coarsely (H/M/L); precision
theater helps nobody. -->

| # | Element | Threat (STRIDE class) | Scenario | L | I |
|---|---|---|---|---|---|

## 7. Existing controls

<!-- What already mitigates which threat - cite rule IDs where the control is a playbook
obligation (e.g., SEC-006 parameterization, SEC-023 rate limiting, OBS-005 telemetry masking). -->

| Threat # | Control | Cites |
|---|---|---|

## 8. Mitigations (planned)

<!-- Gaps between threats and controls: what will be done, by whom, tracked where. -->

| Threat # | Mitigation | Owner | Work item |
|---|---|---|---|

## 9. Residual risks

<!-- Risks accepted after mitigations, stated plainly. Acceptance is a decision - name who
accepted each and when. MUST-level rule exceptions among them require waivers (cite W-nnn). -->

## 10. Assumptions

<!-- What this model takes as given (e.g., "platform IAM is correctly configured", "TLS
termination is trustworthy"). Each assumption is a place the model is blind - list honestly. -->

## 11. Unresolved questions

<!-- Open items per AGENT-011 discipline: unknowns, deferred analysis, expertise gaps. -->

## 12. Sign-off

<!-- Human approval only. For org-standard systems: the security reviewer + owning engineer.
An AI agent may not fill this section for its own draft. -->

| Role | Name | Date |
|---|---|---|
| Security reviewer | | |
| Owning engineer | | |
