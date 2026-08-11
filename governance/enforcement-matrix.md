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
| API-001 | api.md | MUST | api-service | Contract presence/lint check; contract *quality* needs review | partial | partial | yes | spot-check | yes | 3 |
| API-002 | api.md | MUST NOT | api-service, public-api | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-003 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-004 | api.md | MUST | api-service, public-api | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-005 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-006 | api.md | MUST NOT | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-007 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-008 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-009 | api.md | SHOULD | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | no | 3 |
| API-010 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-011 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | judgment | no | assists | yes | yes | 3 |
| API-012 | api.md | MUST | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | yes | 3 |
| API-013 | api.md | SHOULD | api-service | Code review; architecture review for cross-component contracts | review-only | no | yes | yes | no | 3 |
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
| CODE-015 | coding.md | SHOULD NOT | all | Complexity/length warning in static analysis (values accepted 2026-08-11) | partial | partial | yes | spot-check | no | 2 |
| DB-001 | database.md | MUST | uses-database | Migration-tool presence/ordering check; migration *content* needs review | partial | partial | yes | spot-check | yes | 3 |
| DB-002 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-003 | database.md | MUST NOT | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-004 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-005 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-006 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-007 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-008 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | judgment | no | assists | yes | yes | 3 |
| DB-009 | database.md | SHOULD | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | no | 3 |
| DB-010 | database.md | SHOULD | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | no | 3 |
| DB-011 | database.md | MUST | uses-database, handles-pii | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
| DB-012 | database.md | MUST | uses-database | Code review; security review for classified-data migrations | review-only | no | yes | yes | yes | 3 |
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
| GIT-013 | git.md | SHOULD NOT | all | PR-size warning in CI (accepted 2026-08-11; never auto-blocking) | partial | partial | yes | spot-check | no | 2 |
| GIT-014 | git.md | SHOULD | all | Code review | review-only | no | yes | yes | no | 2 |
| OBS-001 | observability.md | MUST | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-002 | observability.md | MUST | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-003 | observability.md | MUST | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-004 | observability.md | MUST | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-005 | observability.md | MUST NOT | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-006 | observability.md | MUST | all | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-007 | observability.md | MUST | api-service, web | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-008 | observability.md | MUST | api-service, web | Code review | review-only | no | yes | yes | yes | 3 |
| OBS-009 | observability.md | SHOULD | api-service | Code review | review-only | no | yes | yes | no | 3 |
| OBS-010 | observability.md | MUST | all | Code review | judgment | no | assists | yes | yes | 3 |
| OBS-011 | observability.md | SHOULD | api-service, web | Code review | judgment | no | assists | yes | no | 3 |
| REPO-001 | repository.md | MUST | all | Required-file presence check (new-repository checklist / CI) | auto | yes | yes | no | yes | 2 |
| REPO-002 | repository.md | MUST NOT | all | Secret scanning per SEC-020; tooling selection per project; review vigilance meanwhile | partial | partial | yes | spot-check | yes | 2 |
| REPO-003 | repository.md | MUST NOT | all | .gitignore + tracked-file pattern check | auto | yes | yes | no | yes | 2 |
| REPO-004 | repository.md | MUST | all | Template-file presence check; key completeness needs review | partial | partial | yes | spot-check | yes | 2 |
| REPO-005 | repository.md | MUST NOT | all | .gitignore + tracked-file pattern check | auto | yes | yes | no | yes | 2 |
| REPO-006 | repository.md | MUST | all | Lockfile presence check | auto | yes | yes | no | yes | 2 |
| REPO-007 | repository.md | SHOULD | all | New-repository checklist / code review | review-only | no | yes | yes | no | 2 |
| REPO-008 | repository.md | MUST | all | CODEOWNERS coverage check | auto | yes | yes | no | yes | 2 |
| REPO-009 | repository.md | MUST | all | Pipeline-config presence check | auto | yes | yes | no | yes | 2 |
| REPO-010 | repository.md | SHOULD | all | Platform auto-delete setting; stale-branch detection is periodic | partial | partial | yes | spot-check | no | 2 |
| SEC-001 | security.md | MUST | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-002 | security.md | MUST | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-003 | security.md | MUST NOT | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-004 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | judgment | no | assists | yes | yes | 3 |
| SEC-005 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-006 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-007 | security.md | MUST | web, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-008 | security.md | MUST NOT | web, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-009 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-010 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-011 | security.md | MUST | all | Process step (owner / quarterly review) | process | no | follows | yes | yes | 3 |
| SEC-012 | security.md | MUST | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-013 | security.md | MUST | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-014 | security.md | MUST | uses-database | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-015 | security.md | MUST NOT | handles-pii | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-016 | security.md | MUST | handles-pii | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-017 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-018 | security.md | MUST NOT | uses-database | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-019 | security.md | MUST | all | Dependency vulnerability scanner in CI - tooling selection per project (ADR) | partial | partial | yes | spot-check | yes | 3 |
| SEC-020 | security.md | MUST | all | Secret scanner in CI - tooling selection per project (ADR) | partial | partial | yes | spot-check | yes | 3 |
| SEC-028 | security.md | MUST NOT | all | Scanner severity gate (CVSS v3.1 >= 7.0; accepted 2026-08-11); waiver path is human-only | partial | partial | yes | spot-check | yes | 4 |
| SEC-021 | security.md | SHOULD | all | SAST in CI where the ecosystem has viable tooling | partial | partial | yes | spot-check | no | 3 |
| SEC-022 | security.md | MUST | web, mobile, api-service | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-023 | security.md | MUST | web, api-service, public-api | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-024 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-025 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-026 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
| SEC-027 | security.md | MUST | all | Security review (SEC-026 triggers) / code review | review-only | no | yes | yes | yes | 3 |
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
| TEST-015 | testing.md | SHOULD | all | Diff-coverage report/warning (accepted 2026-08-11); exceptions per AGENT-009 | partial | partial | yes | spot-check | no | 2 |
| WEB-001 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-002 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-003 | web.md | MUST | web | Accessibility lint (label association is deterministic); coverage depends on tooling | partial | partial | yes | spot-check | yes | 4 |
| WEB-004 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-005 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-006 | web.md | MUST | web | Contrast checks in accessibility tooling; dynamic states need review | partial | partial | yes | spot-check | yes | 4 |
| WEB-007 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-008 | web.md | SHOULD | web | Code review (web items in DoD); security review where SEC-026 triggers fire | judgment | no | assists | yes | no | 4 |
| WEB-009 | web.md | MUST | web | Accessibility check step present in CI - tooling selection per project (ADR) | partial | partial | yes | spot-check | yes | 4 |
| WEB-010 | web.md | MUST | web | Budget verification in CI - measurement tooling per project (ADR); values pending approval | partial | partial | yes | spot-check | yes | 4 |
| WEB-011 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-012 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-013 | web.md | SHOULD | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | no | 4 |
| WEB-014 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-015 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-016 | web.md | SHOULD | web | Code review (web items in DoD); security review where SEC-026 triggers fire | judgment | no | assists | yes | no | 4 |
| WEB-017 | web.md | MUST | web | Response-header validation in CI/tests; per-response-class exceptions need review | partial | partial | yes | spot-check | yes | 4 |
| WEB-018 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | judgment | no | assists | yes | yes | 4 |
| WEB-019 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-020 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-021 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-022 | web.md | MUST NOT | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-023 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-024 | web.md | MUST | web | SRI/self-host lint on script tags; dynamically injected scripts need review | partial | partial | yes | spot-check | yes | 4 |
| WEB-025 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-026 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-027 | web.md | MUST | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | yes | 4 |
| WEB-028 | web.md | SHOULD | web | Code review (web items in DoD); security review where SEC-026 triggers fire | review-only | no | yes | yes | no | 4 |
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

**Totals:** 202 rules - auto: 23 · judgment: 17 · partial: 25 · process: 7 · review-only: 130

## Tooling gaps (tracked for Phase 5/6)

Rules classed `partial` above are the CI-automation backlog. Notable gaps: scanner selection
per project via ADR (SEC-019/020/021, enforcing REPO-002), API contract diffing (API-001/002),
migration linting (DB-001), PR deviation-section lint (AGENT-009), boundary-declaration
tooling (ARCH-006), commit lint (GIT-006). Structured-logging lint (OBS-001) has no
deterministic general implementation and is honestly review-classed. A `partial` class means
review currently carries part of the load - not that the rule is optional.
