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

## Agents (and honest humans)

- [ ] Deviations from recommended rules recorded under `## Standards deviations` — AGENT-009
- [ ] Unresolved questions and forced assumptions reported, not buried — AGENT-011
- [ ] No secrets or environment values anywhere in the diff — REPO-002, REPO-003
