# Security Review Checklist

> **Class:** Instrument (view) · **Gate:** a change matches the SEC-026 trigger list
> ([security.md](../standards/security.md) §2) · **Status:** Active
> For the security reviewer. Items cite rule IDs (RULE-008); the cited rule is authoritative.
> Scanners cover REPO-002/SEC-019/SEC-020 mechanically — spend review attention on what they
> cannot see: authorization logic, trust-boundary reasoning, and data flows.

## Scope first

- [ ] Which triggers fired, and does the diff match the declared scope? — SEC-026
- [ ] Threat model exists and covers this change; updated if a SEC-027 trigger matched — SEC-027
- [ ] No security control weakened or disabled to make the change pass — AGENT-013, AGENT-003

## Authentication and authorization

- [ ] Every new/changed entry point authenticates, or is explicitly declared public — SEC-001
- [ ] Authorization checks the specific resource instance, not just "is logged in" — SEC-002
- [ ] No authorization decision trusts client-supplied assertions — SEC-003
- [ ] New principals/permissions follow least privilege — SEC-004
- [ ] Tokens/sessions introduced here expire and can be revoked — SEC-013
- [ ] Stored credentials (if any) hashed with a salted, adaptive function — SEC-012

## Untrusted input and integrations

- [ ] All new trust-boundary input validated against explicit expectations — SEC-005
- [ ] No untrusted data reaches an interpreter unparameterized/unencoded — SEC-006
- [ ] Server-side requests with attacker-influenced destinations are allowlisted — SEC-007
- [ ] Uploads cannot be stored or served executably — SEC-008
- [ ] New external integrations isolated behind owned adapters, boundary in the threat model — ARCH-005, SEC-027

## Data exposure

- [ ] New persisted structures declare PII classification — SEC-014
- [ ] Collection limited to declared purpose; retention declared — SEC-015, DB-011
- [ ] Sensitive data encrypted at rest; transport encrypted — SEC-016, SEC-017
- [ ] No secrets, credentials, or unmasked PII in logs, traces, or metrics — OBS-005
- [ ] Error responses leak no internal detail — API-006
- [ ] No production data flowing to non-production environments unmasked — SEC-018

## Secrets and dependencies

- [ ] Nothing secret in the diff or in history — REPO-002; if exposed: rotation recorded — SEC-011
- [ ] New secrets delivered via the secret-management mechanism, rotatable — SEC-009, SEC-010
- [ ] Dependency scan findings addressed or explicitly waived — SEC-019
- [ ] New dependencies justified; supply-chain surface considered — CODE-012

## Abuse and operational security

- [ ] Public-facing endpoints carry rate limiting or equivalent — SEC-023
- [ ] Security-relevant events recorded with actor/action/target/outcome — SEC-022
- [ ] Security-relevant defaults are the secure option — SEC-024, APP-011
- [ ] Multi-tenant access paths scoped to the requesting tenant — SEC-025

## Migrations and APIs in this change

- [ ] Migrations touching classified data: preservation step reviewed, rollback path defined — DB-003, DB-002
- [ ] API changes: no in-version breaking change; error contract intact — API-002, API-005

## Closing

- [ ] Waiver requests (if any) complete per the required fields, awaiting owner decision — never self-approved — AGENT-007, AGENT-008
- [ ] Reviewer's unresolved concerns recorded on the PR, not waved through — AGENT-011
