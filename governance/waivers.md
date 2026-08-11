# Waivers

> **Class:** Governance · **Status:** Active
> The only path by which a MUST or MUST NOT rule stops binding a specific case. Waivers exist so
> that mandatory rules stay honest: with no legal exception path, rules get ignored silently.
> Terms: [GLOSSARY.md](../GLOSSARY.md).

## 1. Authority (approved 2026-08-11)

A MUST-level requirement may be waived **only by the designated Playbook Owner / Principal
Architect**. There are no other approvers and no delegation.

Developers and AI coding agents **may**: identify a potential need for a waiver, document the
justification, identify the affected standards and rule IDs, and propose compensating controls.
They **may not** approve a waiver — an AI agent granting or assuming a waiver is itself a
violation (see AGENT-006 in [agents/ai-agent-standards.md](../agents/ai-agent-standards.md)).

Rules whose Exceptions field is `none` cannot be waived at all, by anyone.

## 2. Required content

Every approved waiver record contains **all** of the following:

| Field | Content |
|---|---|
| Waiver ID | `W-<NNN>`, sequential, never reused |
| Rule ID(s) | The exact rule(s) waived |
| Affected project | The project repository (and component, if narrower) |
| Justification | Why compliance is not possible or not reasonable in this case |
| Scope | Precisely what is exempted — never broader than the justification supports |
| Compensating control | What mitigates the risk while the waiver is active (`none` only with explicit reasoning) |
| Approving authority | Named Playbook Owner |
| Approval date | ISO date |
| Expiry / review date | ISO date — every waiver is time-bounded; no permanent waivers |

## 3. Process

1. **Request.** The requester (human or AI agent) prepares the record above, minus approval fields,
   in the PR or ADR that needs the exception.
2. **Decision.** The Playbook Owner approves, narrows, or rejects. Only the Owner fills the
   approval fields.
3. **Record.** Approved waivers are entered in the register below (the auditable, single source of
   truth) and cited by Waiver ID from the requesting project's PR/ADR.
4. **Expiry.** At the expiry/review date the waiver either lapses (compliance restored) or is
   explicitly renewed by the Owner as a new decision. Expired waivers are moved to the archive
   section, never deleted. Expiry checks happen at the quarterly review
   ([change-process.md](change-process.md) §4).

## 4. Waiver register

*Active waivers. None yet.*

| Waiver ID | Rule ID(s) | Project | Scope | Compensating control | Approved by | Approved | Expires |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

## 5. Archive

*Expired or lapsed waivers are moved here with their full record intact. None yet.*
