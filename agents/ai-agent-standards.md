# AI Coding Agent Standards (AGENT)

> **Class:** Standard · **Rule prefix:** `AGENT` · **Status:** Active — **seed**
> Seeded in Phase 1 so agent behavior is governed from day one; completed and tuned in Phase 6
> ([PLAYBOOK-ROADMAP.md](../PLAYBOOK-ROADMAP.md)). Seed rules are fully binding.
>
> This document owns **agent behavior only**. Agents read the same engineering standards humans
> do — no engineering rule is defined or restated here (RULE-007, RULE-008). Navigation lives in
> [context-map.md](context-map.md); precedence in [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.2.

## Rules

### AGENT-001: An AI agent MUST read the project repository's `CLAUDE.md` and this playbook's `CLAUDE.md` before making any change.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** The entry points declare the pinned playbook version, the project profile, and the routing an agent needs; skipping them means working against unknown obligations ([P-12](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### AGENT-002: An AI agent MUST load the always-applicable standards plus the conditional standards selected by the project profile and task type, per `agents/context-map.md`, before authoring a change.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Applicability is mechanical (profile + trigger tags, RULE-005); loading the right subset is what makes compliance possible without loading everything ([P-12](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### AGENT-003: When two documents of equal precedence conflict, an AI agent MUST apply the stricter reading and report the conflict as a playbook defect.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Silently choosing the weaker interpretation converts a documentation defect into a compliance hole; the stricter-reading default makes conflicts safe until fixed (PLAYBOOK-ARCHITECTURE.md §2.2, [P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-004: An AI agent MUST stop and request clarification when an ambiguity affects compliance with a mandatory rule and no precedence or conflict-resolution rule resolves it.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Guessing at mandatory obligations produces confident non-compliance; ambiguity below the mandatory line is handled by judgment plus AGENT-011 reporting ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-005: An AI agent MUST NOT knowingly produce work that violates a mandatory rule.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Mandatory rules bind every layer, and agents get no special exemption; the escape paths are AGENT-006 (halt) and the waiver process — never quiet violation ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-006: When a task cannot proceed without violating a mandatory rule, an AI agent MUST halt and report the rule ID, the nature of the conflict, and the available options.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** A blocked task with a clear report is recoverable; a completed task with a hidden violation is not ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-007: An AI agent MUST NOT approve, assume, extend, or renew a waiver.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Waiver authority rests solely with the Playbook Owner ([governance/waivers.md](../governance/waivers.md) §1); an agent granting itself exceptions dissolves the entire mandatory tier ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-008: An AI agent MAY draft a waiver request, with justification, affected rule IDs, scope, and proposed compensating controls, for human decision.

- **Level:** MAY
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Agents are well placed to detect the need and prepare the record ([governance/waivers.md](../governance/waivers.md) §3); preparing is not approving ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** n/a

### AGENT-009: An AI agent MUST record every deviation from a recommended rule in the pull request description under a `## Standards deviations` heading, citing the rule ID and the justification.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Recommended rules permit justified deviation — but an unrecorded deviation is indistinguishable from ignorance, and the record is what reviewers and the quarterly review consume ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### AGENT-010: An AI agent MUST verify, before claiming a task complete, that every applicable mandatory rule among its loaded standards is satisfied.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Completion is a compliance claim, not a feeling ([P-1](../principles/engineering-principles.md)). From Phase 2, `checklists/definition-of-done.md` becomes the concrete instrument for this verification.
- **Exceptions:** waiver-only

### AGENT-011: An AI agent MUST report unresolved questions, assumptions it was forced to make, and known gaps explicitly in its final output.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Buried uncertainty becomes someone else's incident; surfaced uncertainty is a work item ([P-2](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-012: An AI agent SHOULD cite rule IDs when a design choice, review comment, or pull request description is grounded in a standard.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Citations make agent reasoning auditable and teach humans the rulebook as a side effect ([P-12](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### AGENT-013: An AI agent MUST NOT modify repository governance controls — branch protection, required checks, review requirements, CI configuration, permissions — in order to make its own work pass.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The gates exist precisely to check the agent's work; an agent that can loosen its own gates has no gates. Legitimate governance changes are proposed to a human as their own reviewed change, never bundled with the work they would unblock ([P-5](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-014: An AI agent MUST NOT force-push to or rewrite the history of any shared branch without explicit human authorization given for that specific operation.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** History rewriting is the one git operation that destroys the audit trail everything else relies on (GIT-009); standing permission does not exist — authorization is per-operation, in the current task, from a human ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-015: An AI agent MAY prepare deployment, infrastructure, CI, and container configuration, analyze pipeline failures, and draft rollback plans — as proposed changes for review.

- **Level:** MAY
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Preparation is where agents excel and where mistakes are still cheap: everything lands as a reviewable artifact (PR, plan, draft) inside the normal gates, never as a direct production action ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** n/a

### AGENT-016: An AI agent MUST NOT modify production infrastructure, production secrets, or deployment controls without explicit human authorization for that specific operation.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The production boundary is where a wrong action stops being a diff and starts being an incident; AGENT-013 covers repository governance — this rule covers the runtime estate: infrastructure state, secret values, release gates, required approvals, vulnerability-finding suppression (which follows the waiver path, SEC-028, never an edit) ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none

### AGENT-017: An AI agent MUST explicitly identify, in its output, every prepared change that requires human authorization before it can take effect.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The complement of AGENT-015/016: an agent that prepares a production-affecting change and does not flag the authorization boundary invites a human to rubber-stamp it as routine; the flag is what keeps the human gate a real gate (CI-010) ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

## Retirement log

None.
