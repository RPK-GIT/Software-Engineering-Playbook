# Enforcement Matrix

> **Class:** Instrument · **Status:** Active (seeded Phase 2; regenerated whenever rules change)
> The honesty ledger required by RULE-006: every rule mapped to how it is actually verified.
> Generated from the canonical rule blocks by ad hoc tooling, with hand-curated
> automatability classification; Phase 6 replaces the tooling, not the format.
>
> **Class values** - `auto`: deterministically enforced by CI · `partial`: CI catches some
> violations, review covers the rest · `review-only`: checkable by a human against explicit
> criteria · `judgment`: requires expert assessment; AI assists but a human decides ·
> `process`: a process obligation outside the PR flow.
> **AI agent column** - `yes`: the agent can fully self-enforce while authoring ·
> `assists`: the agent applies it but cannot be the final check · `follows`: the agent
> participates in the process. **Blocking** - a MUST-level rule blocks at its gate;
> SHOULD-level deviations are recorded (AGENT-009), not blocked.

| Rule | Standard | Level | Applies to | Enforcement mechanism | Class | CI | AI agent | Human | Blocking | Phase |
|---|---|---|---|---|---|---|---|---|---|---|
| RULE-001 | _rule-format.md | MUST | all | Playbook validation (V2) | auto | yes | yes | no | yes | 1 |
| RULE-002 | _rule-format.md | MUST | all | Playbook validation (V3/V4) | auto | yes | yes | no | yes | 1 |
| RULE-003 | _rule-format.md | MUST | all | Playbook PR review | review-only | no | yes | yes | yes | 1 |
| RULE-004 | _rule-format.md | MUST NOT | all | Playbook review + heuristic lint (V6) | review-only | no | yes | yes | yes | 1 |
| RULE-005 | _rule-format.md | MUST | all | Playbook validation (V4) | auto | yes | yes | no | yes | 1 |
| RULE-006 | _rule-format.md | MUST | all | Playbook validation (V8) | auto | yes | yes | no | yes | 1 |
| RULE-007 | _rule-format.md | MUST NOT | all | Playbook validation (V5) | auto | yes | yes | no | yes | 1 |
| RULE-008 | _rule-format.md | MUST | all | Playbook PR review | review-only | no | yes | yes | yes | 1 |
| RULE-009 | _rule-format.md | MUST NOT | all | Playbook PR review | review-only | no | yes | yes | yes | 1 |
| RULE-010 | _rule-format.md | MUST | all | Playbook PR review | review-only | no | yes | yes | yes | 1 |
| RULE-011 | _rule-format.md | MUST | all | Playbook PR review | review-only | no | yes | yes | yes | 1 |
| RULE-012 | _rule-format.md | SHOULD | all | Playbook PR review | review-only | no | yes | yes | no | 1 |
| RULE-013 | _rule-format.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 1 |
| APP-001 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-002 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-003 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-004 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-005 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-006 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-007 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-008 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-009 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-010 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-011 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| APP-012 | application.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| ARCH-001 | architecture.md | MUST | all | Architecture review (structural changes, in code review) | judgment | no | assists | yes | yes | 2 |
| ARCH-002 | architecture.md | MUST | all | Architecture review (structural changes, in code review) | judgment | no | assists | yes | yes | 2 |
| ARCH-003 | architecture.md | MUST NOT | all | Architecture review (structural changes, in code review) | judgment | no | assists | yes | yes | 2 |
| ARCH-004 | architecture.md | MUST | all | Architecture review (structural changes, in code review) | review-only | no | yes | yes | yes | 2 |
| ARCH-005 | architecture.md | MUST | all | Architecture review (structural changes, in code review) | review-only | no | yes | yes | yes | 2 |
| ARCH-006 | architecture.md | MUST | all | Dependency-rule check; requires per-project boundary declaration + tooling | partial | partial | yes | spot-check | yes | 2 |
| ARCH-007 | architecture.md | MUST | uses-database | Architecture review (structural changes, in code review) | review-only | no | yes | yes | yes | 2 |
| ARCH-008 | architecture.md | MUST NOT | all | Architecture review (structural changes, in code review) | judgment | no | assists | yes | yes | 2 |
| ARCH-009 | architecture.md | MUST NOT | all | Architecture review (structural changes, in code review) | judgment | no | assists | yes | yes | 2 |
| CODE-001 | coding.md | MUST | all | Formatter check (per-project tooling) | auto | yes | yes | no | yes | 2 |
| CODE-002 | coding.md | MUST | all | Linter (per-project tooling) | auto | yes | yes | no | yes | 2 |
| CODE-003 | coding.md | MUST | all | Type checker as blocking CI step | auto | yes | yes | no | yes | 2 |
| CODE-004 | coding.md | MUST | all | Code review | judgment | no | assists | yes | yes | 2 |
| CODE-005 | coding.md | MUST NOT | all | Code review | review-only | no | yes | yes | yes | 2 |
| CODE-006 | coding.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| CODE-007 | coding.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| CODE-008 | coding.md | SHOULD | all | Code review | review-only | no | yes | yes | no | 2 |
| CODE-009 | coding.md | SHOULD | all | Code review | judgment | no | assists | yes | no | 2 |
| CODE-010 | coding.md | MUST | all | Complexity rule in static analysis (value pending owner approval) | auto | yes | yes | no | yes | 2 |
| CODE-011 | coding.md | MUST | all | Suppression-comment lint; tooling varies by ecosystem | partial | partial | yes | spot-check | yes | 2 |
| CODE-012 | coding.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| CODE-013 | coding.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| CODE-014 | coding.md | MUST NOT | library | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-001 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-002 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-003 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-004 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-005 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-006 | documentation.md | SHOULD | all | Code review | review-only | no | yes | yes | no | 2 |
| DOC-007 | documentation.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| DOC-008 | documentation.md | SHOULD | all | Code review | review-only | no | yes | yes | no | 2 |
| GIT-001 | git.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| GIT-002 | git.md | MUST | all | Platform branch protection (PR-only) | auto | yes | yes | no | yes | 2 |
| GIT-003 | git.md | MUST | all | Platform branch protection settings | auto | yes | yes | no | yes | 2 |
| GIT-004 | git.md | MUST | all | Platform required-approval setting + CODEOWNERS | auto | yes | yes | no | yes | 2 |
| GIT-005 | git.md | MUST NOT | all | Platform required-status-checks setting | auto | yes | yes | no | yes | 2 |
| GIT-006 | git.md | MUST | all | Commit-message lint in CI | partial | partial | yes | spot-check | yes | 2 |
| GIT-007 | git.md | SHOULD | all | Code review | review-only | no | yes | yes | no | 2 |
| GIT-008 | git.md | SHOULD | all | Platform merge-method setting; deliberate exceptions possible | partial | partial | yes | spot-check | no | 2 |
| GIT-009 | git.md | MUST NOT | all | Platform force-push protection | auto | yes | yes | no | yes | 2 |
| GIT-010 | git.md | MUST | all | Tag presence check in release pipeline | auto | yes | yes | no | yes | 2 |
| GIT-011 | git.md | SHOULD | all | Code review | judgment | no | assists | yes | no | 2 |
| GIT-012 | git.md | MUST | all | Same platform gates as regular changes | auto | yes | yes | no | yes | 2 |
| REPO-001 | repository.md | MUST | all | Required-file presence check (new-repository checklist / CI) | auto | yes | yes | no | yes | 2 |
| REPO-002 | repository.md | MUST NOT | all | Secret scanning - tooling policy arrives Phase 3 (security.md); interim: review vigilance | partial | partial | yes | spot-check | yes | 2 |
| REPO-003 | repository.md | MUST NOT | all | .gitignore + tracked-file pattern check | auto | yes | yes | no | yes | 2 |
| REPO-004 | repository.md | MUST | all | Template-file presence check; key completeness needs review | partial | partial | yes | spot-check | yes | 2 |
| REPO-005 | repository.md | MUST NOT | all | .gitignore + tracked-file pattern check | auto | yes | yes | no | yes | 2 |
| REPO-006 | repository.md | MUST | all | Lockfile presence check | auto | yes | yes | no | yes | 2 |
| REPO-007 | repository.md | SHOULD | all | New-repository checklist / code review | review-only | no | yes | yes | no | 2 |
| REPO-008 | repository.md | MUST | all | CODEOWNERS coverage check | auto | yes | yes | no | yes | 2 |
| REPO-009 | repository.md | MUST | all | Pipeline-config presence check | auto | yes | yes | no | yes | 2 |
| REPO-010 | repository.md | SHOULD | all | Platform auto-delete setting; stale-branch detection is periodic | partial | partial | yes | spot-check | no | 2 |
| TEST-001 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-002 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-003 | testing.md | MUST | all | CI reruns / flake detection - detects, cannot prove absence | partial | partial | yes | spot-check | yes | 2 |
| TEST-004 | testing.md | MUST NOT | all | Test-order randomization in CI - detects, cannot prove absence | partial | partial | yes | spot-check | yes | 2 |
| TEST-005 | testing.md | MUST NOT | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-006 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-007 | testing.md | MUST | api-service, public-api | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-008 | testing.md | MUST | web, mobile, api-service | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-009 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-010 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-011 | testing.md | SHOULD | all | Code review | judgment | no | assists | yes | no | 2 |
| TEST-012 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-013 | testing.md | MUST | all | Code review | review-only | no | yes | yes | yes | 2 |
| TEST-014 | testing.md | MUST | all | Coverage measurement + report step in CI | auto | yes | yes | no | yes | 2 |
| AGENT-001 | ai-agent-standards.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 1 |
| AGENT-002 | ai-agent-standards.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 1 |
| AGENT-003 | ai-agent-standards.md | MUST | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 1 |
| AGENT-004 | ai-agent-standards.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 1 |
| AGENT-005 | ai-agent-standards.md | MUST NOT | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 1 |
| AGENT-006 | ai-agent-standards.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 1 |
| AGENT-007 | ai-agent-standards.md | MUST NOT | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 1 |
| AGENT-008 | ai-agent-standards.md | MAY | all | Process step (owner / quarterly review) | process | no | follows | yes | no | 1 |
| AGENT-009 | ai-agent-standards.md | MUST | all | PR-description section lint - tooling to be built; interim: review | partial | partial | yes | spot-check | yes | 1 |
| AGENT-010 | ai-agent-standards.md | MUST | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 1 |
| AGENT-011 | ai-agent-standards.md | MUST | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 1 |
| AGENT-012 | ai-agent-standards.md | SHOULD | all | Review of agent output (PR review) | review-only | no | yes | yes | no | 1 |
| AGENT-013 | ai-agent-standards.md | MUST NOT | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 2 |
| AGENT-014 | ai-agent-standards.md | MUST NOT | all | Review of agent output (PR review) | review-only | no | yes | yes | yes | 2 |

**Totals:** 106 rules - auto: 23 · judgment: 9 · partial: 10 · process: 6 · review-only: 58

## Tooling gaps (tracked for Phase 5/6)

Rules classed `partial` above are the CI-automation backlog. Notable gaps: secret scanning
(REPO-002 - policy owner is Phase 3 security.md), PR deviation-section lint (AGENT-009),
boundary-declaration tooling guidance (ARCH-006), commit lint (GIT-006). A `partial` class
is a statement that review currently carries part of the load - not that the rule is optional.
