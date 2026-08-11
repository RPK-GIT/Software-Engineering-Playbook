# Glossary

> **Class:** Governance · **Status:** Active (seeded in Phase 1; grows as rules introduce terms — RULE-010)
> One definition per term. If a rule depends on a term, the term is defined here and nowhere else.
> Definitions are alphabetical.

**ADR (Architecture Decision Record)** — An append-only record of one significant decision: its
context, the decision, and its consequences. Org-level ADRs live in this repo's `decisions/`;
project-level ADRs live in each project repository. ADRs are superseded, never edited.

**Breaking change** — A change that can make a previously valid consumer of a contract (API,
library interface, configuration) invalid: removing or renaming an element, changing its type or
semantics, tightening what is accepted, or loosening what is returned.

**Correlation identifier** — The identifier assigned to one unit of work at its entry point and
carried by all telemetry and cross-boundary calls belonging to it (OBS-003/004).

**Applicability tag** — A value from the closed registry in
[standards/_rule-format.md](standards/_rule-format.md) §4 that scopes a rule to the projects
(*profile* tags) or changes (*trigger* tags) it binds.

**Deviation** — A recorded, justified departure from a SHOULD or SHOULD NOT rule. Deviations are
declared in the pull request that contains them. Departing from a MUST is never a deviation; it
requires a waiver.

**Derived document** — Any document whose content is produced from standards (checklists,
templates, agent instructions, implementation guidelines). Derived documents cite rules; they may
add strictness but never relax a requirement (RULE-009).

**Enforcement tag** — Classification of how a rule is verified: `ci` (pipeline check), `review`
(named human gate), or `manual` (process obligation). Defined in
[standards/_rule-format.md](standards/_rule-format.md) §2.

**Gate** — A defined moment in the delivery lifecycle where compliance is checked (PR opened,
first deploy, incident declared). Each gate has a checklist that cites the rule IDs applying at
that moment.

**Instrument** — A document class covering the artifacts through which standards are applied:
checklists, templates, the enforcement matrix, and the agent context map.

**Mandatory rule** — A rule whose level is MUST or MUST NOT. Departing from one requires a waiver.

**Migration** — A versioned, ordered change to persistent data structure or stored data, tracked
in the repository (DB-001).

**PII (Personally Identifiable Information)** — Data that identifies, or can reasonably be
combined to identify, a natural person: names, contact details, government identifiers, precise
location, biometric or health data, and identifiers linkable to a person.

**Principal** — Any authenticated identity that acts: a user, a service, or a scheduled job
(SEC-004).

**Normative / Non-normative** — Normative content creates obligations and exists only in canonical
rule blocks (RULE-001, RULE-007). Everything else — preambles, rationale, examples, this glossary —
is non-normative context.

**Recommended rule** — A rule whose level is SHOULD or SHOULD NOT. Departing from one requires a
recorded, justified deviation.

**Pinning** — A project repository's declaration of the exact playbook version (git tag) it
complies with. Upgrades are deliberate changes, reviewed like any other.

**Playbook Owner** — The designated role (currently: Playbook Owner / Principal Architect) with
sole authority to approve changes to standards and waivers of MUST-level rules.

**Profile** — The set of profile tags a project declares in its repository's `CLAUDE.md`,
determining which conditional standards bind it (e.g., `web + api-service + uses-database`).

**Project repository** — An application or library repository that adopts this playbook: it pins a
version, declares a profile, and keeps its own ADR log. Distinct from this playbook repository.

**RFC (Request for Comments)** — The proposal document required to change any standard, created
from [templates/rfc.md](templates/rfc.md) and decided per
[governance/change-process.md](governance/change-process.md).

**Secret** — Any value granting access or proving identity: passwords, API keys, tokens, private
keys, connection strings with credentials. Never in version control (REPO-002); managed per
SEC-009…011.

**Sensitive data** — Data whose exposure causes harm: PII (per its classification under SEC-014),
credentials and secrets, and data a project's threat model designates as sensitive.

**Rule** — A single, atomic, identified, normative requirement expressed in the canonical rule
block of [standards/_rule-format.md](standards/_rule-format.md). The only unit of obligation in
this playbook.

**Rule lifecycle** — The states a rule moves through: Proposed → Active → Deprecated → Retired.
Deprecated rules remain binding; retired rule IDs are never reused.

**Standard** — A document in `standards/` (or `agents/ai-agent-standards.md`) that owns a domain
and defines its rules under a registered ID prefix.

**Telemetry** — Everything a system emits about its own behavior: logs, metrics, traces, and
events (taxonomy in [standards/observability.md](standards/observability.md) §1).

**Threat model** — The structured record of a system's assets, trust boundaries, threats, and
controls, per [templates/threat-model.md](templates/threat-model.md); required by SEC-027 triggers.

**Trust boundary** — Any point where data or control passes between parties with different
privilege or trustworthiness: network entry points, user input, third-party integrations, files,
queues. Input crossing one is untrusted until validated (SEC-005).

**Unit of work** — One request, job execution, message handling, or scheduled run — the scope a
correlation identifier covers (OBS-003).

**Waiver** — An explicit, auditable, time-bounded exception to a MUST or MUST NOT rule, approvable
only by the Playbook Owner, per [governance/waivers.md](governance/waivers.md).
