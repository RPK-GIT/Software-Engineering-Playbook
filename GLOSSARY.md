# Glossary

> **Class:** Governance · **Status:** Active (seeded in Phase 1; grows as rules introduce terms — RULE-010)
> One definition per term. If a rule depends on a term, the term is defined here and nowhere else.
> Definitions are alphabetical.

**ADR (Architecture Decision Record)** — An append-only record of one significant decision: its
context, the decision, and its consequences. Org-level ADRs live in this repo's `decisions/`;
project-level ADRs live in each project repository. ADRs are superseded, never edited.

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

**Rule** — A single, atomic, identified, normative requirement expressed in the canonical rule
block of [standards/_rule-format.md](standards/_rule-format.md). The only unit of obligation in
this playbook.

**Rule lifecycle** — The states a rule moves through: Proposed → Active → Deprecated → Retired.
Deprecated rules remain binding; retired rule IDs are never reused.

**Standard** — A document in `standards/` (or `agents/ai-agent-standards.md`) that owns a domain
and defines its rules under a registered ID prefix.

**Waiver** — An explicit, auditable, time-bounded exception to a MUST or MUST NOT rule, approvable
only by the Playbook Owner, per [governance/waivers.md](governance/waivers.md).
