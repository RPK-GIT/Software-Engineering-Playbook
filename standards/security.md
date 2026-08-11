# Security Standard (SEC)

> **Class:** Standard · **Rule prefix:** `SEC` · **Status:** Active
> **Purpose:** the technology-neutral security floor for production systems — authentication,
> authorization, data protection, secret management, and abuse resistance.
> **Owns:** authn/z, least privilege, trust-boundary input validation, injection/SSRF/upload
> defenses, secret *management* (storage, delivery, rotation), scanning policy (secrets,
> dependencies, SAST), PII classification and handling, encryption, credentials and tokens,
> tenant isolation, security event requirements, environment data exposure, the security-review
> and threat-model triggers.
> **Does not own:** secret *presence in version control* ([repository.md](repository.md)
> REPO-002/003); telemetry content ([observability.md](observability.md) OBS-005); browser
> security headers (`standards/web.md`, Phase 4); network topology (`standards/infrastructure.md`,
> Phase 5); incident response process (`standards/operations.md`, Phase 5).
> **Gate:** security review, triggered by the list in §2; enforcement per the
> [enforcement matrix](../governance/enforcement-matrix.md).

Non-normative context: these rules assume no specific vendor or product. Where a rule says
"mechanism", the project selects tooling by ADR (DOC-003 trigger 6 covers security-relevant
selections). Agents: you have no special security privileges — inventing an exception is an
AGENT-007 violation, disabling a control to make work pass is AGENT-013, and downgrading a
requirement silently is AGENT-003/005.

## 1. Rules

### Access control

### SEC-001: Every network-accessible entry point MUST enforce authentication unless it is explicitly declared public at its definition.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Deny-by-default makes an unauthenticated endpoint a visible, reviewable declaration instead of an accident discovered by a scanner ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none — public endpoints are permitted, but only by explicit declaration

### SEC-002: Every access to a protected resource MUST be authorized against the requesting principal's permission for that specific resource instance.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Checking "is logged in" but not "owns record 42" is the insecure-direct-object-reference class; authorization is per-resource, not per-endpoint ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### SEC-003: Authorization decisions MUST NOT depend on client-supplied assertions.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Hidden fields, client-side role flags, and UI-disabled buttons are attacker-editable; the server re-derives every privilege from its own state ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### SEC-004: Every principal — user, service, or job — MUST be granted only the permissions its function requires.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Least privilege bounds the blast radius of every compromise, bug, and mistake to what the compromised identity could legitimately do ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation, time-bounded and recorded

### Untrusted input

### SEC-005: All input crossing a trust boundary MUST be validated against explicit expectations before use.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Everything arriving from outside the trust boundary — requests, files, messages, webhooks — is attacker-controlled until proven conformant; validation is allowlist-shaped (what is permitted), not blocklist-shaped ([P-5](../principles/engineering-principles.md)). Business-invariant enforcement is separate (APP-008).
- **Exceptions:** none

### SEC-006: Untrusted data MUST reach interpreters only through parameterized or context-encoded mechanisms.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** String-building queries, commands, or markup from untrusted data is the entire injection class — SQL, command, template, and markup alike; the safe mechanism is whichever parameterization the interpreter provides ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### SEC-007: Server-initiated requests whose destination is influenced by untrusted input MUST be restricted to an allowlist of permitted destinations.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, api-service
- **Rationale:** A URL an attacker controls is a request your server makes on their behalf — at internal metadata services, admin endpoints, and private networks (SSRF) ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where destinations are inherently open (e.g., a link-preview service), with compensating controls recorded

### SEC-008: Uploaded files MUST NOT be stored or served in a way that allows their execution.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** web, api-service
- **Rationale:** An upload that can execute is remote code execution with a progress bar; content validation is SEC-005's job, non-executability is this rule's ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### Secrets and credentials

### SEC-009: Runtime secrets MUST be delivered through a dedicated secret-management mechanism, not embedded in artifacts or configuration files.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Secrets in artifacts or config files are copied by every deploy, backup, and log shipper; a dedicated mechanism gives them access control, audit, and rotation. Absence from version control is REPO-002/003; this rule owns everything after that ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-010: Every secret MUST be rotatable without a code change.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Rotation that requires a release will be postponed exactly when it is urgent; rotatability is designed in, not retrofitted during the incident ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### SEC-011: A secret suspected of exposure MUST be rotated immediately and the exposure recorded.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Suspicion is the actionable moment — confirmation often never comes; the record feeds the history purge (GIT-009's sole waiver case) and later incident review ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### SEC-012: Stored user credentials MUST be hashed with a salted, adaptive one-way function.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Password databases leak; adaptive hashing is the difference between an incident and every user's credential reused everywhere becoming an incident ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** not applicable where authentication is fully delegated to an external identity provider and no credentials are stored

### SEC-013: Authentication tokens and session identifiers MUST have bounded lifetimes and a revocation path.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** A stolen token that never expires and cannot be revoked is a permanent credential; bounding lifetime bounds the exposure window ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for machine-to-machine credentials with equivalent compensating controls

### Data protection

### SEC-014: Persisted data structures MUST declare whether they contain PII at the point of definition.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Every downstream obligation — encryption (SEC-016), minimization (SEC-015), retention (DB-011), telemetry masking (OBS-005) — is mechanical once classification exists and impossible while it doesn't ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### SEC-015: PII MUST NOT be collected or retained beyond what the declared purpose requires.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** handles-pii
- **Rationale:** Data you don't hold can't leak, doesn't need masking, and carries no regulatory surface; minimization is the cheapest control that exists ([P-11](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-016: Data classified as sensitive MUST be encrypted at rest.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** handles-pii
- **Rationale:** Storage-layer compromise (stolen volumes, misconfigured buckets, disposed disks) should yield ciphertext; classification per SEC-014 determines scope ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-017: Data in transit MUST be encrypted with standard authenticated transport encryption.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Unencrypted transport exposes credentials, tokens, and data to every network segment in the path; "internal traffic" is exactly what an attacker inside the perimeter reads ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation only for loopback-local communication

### SEC-018: Production data MUST NOT be used in non-production environments unless anonymized or masked.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** uses-database
- **Rationale:** Non-production environments have weaker access control by design; copying real data into them silently extends the production trust boundary to every developer laptop and test system ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### Scanning and supply chain

### SEC-019: CI MUST include dependency vulnerability scanning on every pipeline run.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Known-vulnerable dependencies are the most exploited and most detectable weakness; the scan is cheap, the blocking-severity policy is proposed below ([P-9](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-020: CI MUST include secret scanning on every pipeline run.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** This is the mechanical enforcement arm of REPO-002 — human vigilance against accidental commits fails eventually; scanners don't get tired ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-028: A production-bound change MUST NOT ship with a known dependency vulnerability rated High or Critical by an authoritative vulnerability source, absent an approved waiver.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Accepted policy (2026-08-11): known-exploitable severity is the blocking line the SEC-019 scan enforces. Severity is the gate, not the whole risk assessment — the waiver decision may weigh exploitability, reachability, exposure, affected code path, deployment context, and compensating controls. Exceptions exist only through [governance/waivers.md](../governance/waivers.md) with human approval; an agent may draft the exception (AGENT-008) but never approve or silently apply one (AGENT-007) ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### SEC-021: CI SHOULD include static application security testing appropriate to the stack.

- **Level:** SHOULD
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** SAST catches injection patterns, dangerous APIs, and taint flows before review; SHOULD-level because tool quality varies sharply by ecosystem and a noisy scanner erodes trust in real findings ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### Operational security

### SEC-022: Security-relevant events MUST be recorded as auditable events with actor, action, target, and outcome.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Authentication attempts, authorization failures, and privilege changes are the forensic record of every incident; telemetry *format* and content limits are OBS-001/OBS-005 ([P-7](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### SEC-023: Public-facing endpoints MUST be protected by rate limiting or equivalent abuse controls.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, api-service, public-api
- **Rationale:** Without abuse controls, credential stuffing, scraping, and resource exhaustion are free; "equivalent" admits CAPTCHAs, proof-of-work, or upstream protection — the requirement is the control, not the technique ([P-6](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### SEC-024: Security-relevant configuration MUST default to the secure option.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Defaults are what run when nobody decided; every new environment, flag reset, and forgotten setting lands on the default ([P-5](../principles/engineering-principles.md)). Complements APP-011 for flags.
- **Exceptions:** none

### SEC-025: Every data access in a multi-tenant system MUST be scoped to the requesting tenant.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Cross-tenant leakage is a company-ending bug class; tenant scope is enforced at the access layer, not left to each query author's memory ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** not applicable to single-tenant systems; cross-tenant operations exist only as explicitly declared administrative paths

### Gates

### SEC-026: A change matching the security-review trigger list in §2 MUST undergo security review before merge.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Security review triggered by *what a change touches* fires deterministically; review triggered by someone remembering does not ([P-5](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)). Checklist: [checklists/security-review.md](../checklists/security-review.md).
- **Exceptions:** waiver-only

### SEC-027: A new system, or a change matching the threat-model trigger list in §2, MUST have a threat model created or updated before release.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Controls without a threat model are guesses; the model is where "what could go wrong" gets written down once instead of rediscovered per incident ([P-2](../principles/engineering-principles.md), [P-5](../principles/engineering-principles.md)). Template: [templates/threat-model.md](../templates/threat-model.md).
- **Exceptions:** waiver-only

## 2. Trigger lists (normative content of SEC-026 / SEC-027)

**Security review (SEC-026)** — a change that:
1. adds or modifies an authentication or authorization mechanism;
2. adds a network-accessible entry point or makes an existing one public;
3. adds handling of a new PII category or changes data classification;
4. adds file upload, server-side request, or interpreter-reaching data flow;
5. adds or changes an external integration crossing a trust boundary;
6. changes tenant isolation, session, or token handling;
7. touches secret storage, delivery, or rotation;
8. includes a migration affecting data classified as PII or sensitive.

**Threat model (SEC-027)** — a *new* system or service; or a change matching triggers 1, 3, 5, or 6
above whose existing threat model does not already cover it.

## 3. Accepted policy values

**ACCEPTED POLICY — vulnerability blocking severity (2026-08-11, Playbook Owner; enforced by SEC-028)**
- **Value:** vulnerabilities rated High or Critical by an authoritative source block production-bound changes. Where CVSS is the rating source, the baseline is **CVSS v3.1**, and **CVSS ≥ 7.0** counts as High-or-above; findings below the line are tracked work items.
- **Terms of acceptance:** severity is not the only risk factor — security review may additionally weigh exploitability, reachability, exposure, affected code path, deployment context, and compensating controls when deciding a waiver. Every exception uses the existing waiver mechanism with human approval; AI agents may identify and document a potential exception (AGENT-008) but never approve or silently apply one (AGENT-007).

## Interaction with other standards

Input validation here is trust-boundary sanitization; business invariants are APP-008. Audit event
*format* is OBS-001, telemetry content limits OBS-005. Retention mechanics are DB-011 within
SEC-015's limits. Browser security headers arrive with `standards/web.md` (Phase 4); incident
response with `standards/operations.md` (Phase 5). Full ownership map:
PLAYBOOK-ARCHITECTURE.md §6.

## Retirement log

None.
