# Definition of Done

> **Class:** Instrument (view) · **Gate:** a work item is claimed complete · **Status:** Active
> Items cite rule IDs (RULE-008); the cited rule is authoritative. Filter by your project's
> profile tags — items citing rules whose applicability doesn't match your project don't apply.
> Agents: completing this checklist is how you satisfy AGENT-010. Extended in Phases 3–5.

## Always

- [ ] Formatter, linter, and type checks pass — CODE-001, CODE-002, CODE-003
- [ ] All required CI checks green; no failing check merged past — GIT-005
- [ ] Every static-analysis suppression added carries an inline justification — CODE-011
- [ ] No dead or commented-out code left behind — CODE-007
- [ ] Commit messages follow the convention — GIT-006
- [ ] PR contains one logical change, reviewed by a non-author owner — GIT-007, GIT-004

## When behavior changed

- [ ] Automated tests exercise the changed behavior — TEST-001
- [ ] Failure and boundary cases covered, not just the success path — TEST-009
- [ ] Bug fixes include a test that fails without the fix — TEST-002
- [ ] Tests are deterministic, isolated, and provision their own data — TEST-003, TEST-004, TEST-012

## When structure changed (components, boundaries, dependencies)

- [ ] Component responsibilities still singular and stated — ARCH-001
- [ ] Dependency direction respected; boundary declaration updated — ARCH-003, ARCH-006
- [ ] No speculative mechanisms or unjustified service splits — ARCH-008, ARCH-009
- [ ] New third-party dependencies justified in the PR — CODE-012

## When runtime behavior is involved (external calls, state, config)

- [ ] External calls have timeouts; retries bounded; retried operations idempotent — APP-004, APP-005, APP-006
- [ ] Multi-write operations atomic or compensated — APP-007
- [ ] New config keys: in the tracked template, documented, validated at startup — REPO-004, DOC-005, APP-002
- [ ] New feature flags: safe default, owner, removal condition — APP-011, APP-012
- [ ] Declared failure modes have tests — APP-003, TEST-010

## Documentation and decisions

- [ ] Documentation invalidated by this change updated in the same PR — DOC-002
- [ ] ADR recorded if the change matches a trigger — DOC-003
- [ ] Deprecations documented with replacement and removal plan — DOC-004

## When the change touches security surface, data, or APIs (Phase 3)

- [ ] Security-review triggers checked; review completed if any fired — SEC-026
- [ ] Threat model updated if a SEC-027 trigger matched — SEC-027
- [ ] Trust-boundary input validated; interpreters reached only safely — SEC-005, SEC-006
- [ ] New persisted structures classified; schema change is a versioned, compatible migration with a rollback path — SEC-014, DB-001, DB-004, DB-002
- [ ] API contract updated with the code; no in-version breaking change; errors use the standard contract — API-001, API-002, API-005
- [ ] New code emits structured logs at correct levels, carries the correlation ID, leaks nothing sensitive — OBS-001, OBS-002, OBS-004, OBS-005
- [ ] Changed-line coverage meets the expectation or the deviation is justified — TEST-015

## When the change touches browser-delivered UI (`web` profile, Phase 4)

- [ ] Keyboard-operable; focus managed on dynamic changes — WEB-001, WEB-005
- [ ] Semantic markup; inputs labeled; errors announced — WEB-002, WEB-003, WEB-004
- [ ] Contrast and reflow criteria met; automated accessibility checks green — WEB-006, WEB-007, WEB-009
- [ ] Performance budget respected; images and caching handled — WEB-010, WEB-011, WEB-012
- [ ] Baseline headers, CSP, cookie attributes, CSRF protection intact — WEB-017…020
- [ ] No client-embedded secrets; tokens script-protected; external scripts integrity-pinned — WEB-022, WEB-023, WEB-024
- [ ] User HTML sanitized; CORS origins enumerated — WEB-021, WEB-025
- [ ] i18n rules applied where requirements include localization — WEB-026, WEB-027

## Agents (and honest humans)

- [ ] Deviations from recommended rules recorded under `## Standards deviations` — AGENT-009
- [ ] Unresolved questions and forced assumptions reported, not buried — AGENT-011
- [ ] No secrets or environment values anywhere in the diff — REPO-002, REPO-003
