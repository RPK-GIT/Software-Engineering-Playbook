# Testing Standard (TEST)

> **Class:** Standard · **Rule prefix:** `TEST` · **Status:** Active
> **Purpose:** a testing strategy — what requires automated verification, at which level, with what
> discipline — rather than an exhortation to "write tests."
> **Owns:** test levels and their boundaries, determinism, isolation, test data, doubles, flake
> policy, regression duty, coverage mechanism.
> **Does not own:** CI orchestration of test runs (`standards/ci-cd.md`, Phase 5); security testing
> (`standards/security.md`, Phase 3); merge gating on check results (GIT-010).
> **Gate:** code review, plus the CI checks below.

Non-normative context — the strategy in one paragraph: **unit tests** verify domain and application
logic in isolation and form the bulk; **integration tests** verify each boundary where the code
meets a real external system; **contract tests** verify agreements between services; **end-to-end
tests** verify only the critical user journeys, because they are the most expensive and least
precise instrument. Verification is required for: every behavior change, every fixed bug, every
external boundary, every declared failure mode, and every critical journey.

## Rules

### TEST-001: Every change in behavior MUST be accompanied by automated tests that exercise the changed behavior.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Untested behavior is unverified behavior; the test written with the change is cheap, the one written after the incident is not ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where automated verification is genuinely impractical — the justification names the manual verification performed

### TEST-002: Every bug fix MUST include a test that fails without the fix.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A bug that happened once has proven the surrounding tests miss it; the regression test is the only durable proof of both the bug and the fix ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-003: Tests MUST produce the same result on every run against unchanged code.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Nondeterminism (real time, randomness, network, sleeps) destroys the information value of every result — a red build stops meaning anything ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### TEST-004: Tests MUST NOT depend on execution order or on state left behind by other tests.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Order coupling makes failures unreproducible in isolation and blocks parallel execution; order randomization in CI detects it deterministically ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### TEST-005: Unit tests MUST NOT perform I/O against external systems.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The unit level exists to be fast and precise; a "unit test" that needs a database is an integration test mislabeled, and it will be slow, flaky, and skipped ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** none — such tests are moved to the integration level, not deleted

### TEST-006: Every integration with an external system MUST be covered by integration tests at that boundary.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** The boundary is where assumptions meet reality — serialization, schemas, auth, timeouts; mocked-everywhere suites pass while the real integration is broken ([P-1](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-007: Every API contract provided to or consumed from another team or system MUST be verified by contract tests.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** api-service, public-api
- **Rationale:** Contracts break at the seam between independently deployed parties; contract tests catch the break before deployment rather than in production ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-008: Every critical user journey MUST be covered by at least one automated end-to-end test.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web, mobile, api-service
- **Rationale:** Journeys whose failure means the product is down (sign-in, checkout, core workflow) warrant the one instrument that exercises the assembled system; "critical" is declared per project in its test strategy ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-009: Tests for a behavior MUST cover failure and boundary cases, not only the success path.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Production inputs are adversarial: empty, oversized, malformed, concurrent, duplicated; the happy path is the case least likely to break ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-010: Every failure mode declared under APP-003 MUST be exercised by an automated test.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Failure handling is code that runs rarely and matters most; untested fallbacks fail at the exact moment they are needed ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-011: Test doubles SHOULD replace only components outside the boundary of the code under test.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Mocking internal collaborators welds tests to the implementation — refactors break tests while behavior is unchanged, which trains everyone to ignore red ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### TEST-012: Tests MUST provision the data they depend on.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Dependence on pre-existing environment data makes tests unrunnable anywhere clean and couples them to state nobody owns ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** shared immutable reference data explicitly documented as such

### TEST-013: A test identified as flaky MUST be quarantined under a tracked work item rather than rerun until green.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Retry-until-green teaches the team that red is negotiable, destroying the signal every other rule here builds; quarantine keeps the suite trustworthy while the flake is fixed ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### TEST-014: CI MUST measure and report code coverage on every pipeline run.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Coverage is a cheap detector of *untested* code (its only honest use — high coverage proves little, but low coverage proves a gap); measurement precedes any floor, and the floor's value is a policy value (RULE-011) pending approval below ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

## Proposed policy values (pending approval — not yet binding)

**PROPOSED POLICY — coverage floor (would extend TEST-014 with a blocking gate)**
- **Value:** changed-line coverage ≥ 80% per pull request (diff coverage), with no repository-wide floor initially
- **Reason:** diff coverage targets exactly the code being introduced now, cannot be gamed by legacy code volume, and never demands retroactive test-writing campaigns; 80% leaves room for genuinely untestable lines without inviting whole untested modules
- **Risk of too low:** new code ships systematically untested and TEST-001 loses its measurable backstop
- **Risk of too high:** contributors write assertion-free tests to satisfy the number — coverage theater that is worse than the gap it hides; test *meaningfulness* remains a review judgment regardless
- **Scope:** all profiles, enforced per pull request in CI; suppressible only by waiver
- **Status:** REQUIRES PLAYBOOK OWNER APPROVAL

## Interaction with other standards

Merge gating on test results is GIT-010. Pipeline stages that run these levels are Phase 5
(`standards/ci-cd.md`). Security-specific testing is Phase 3 (`standards/security.md`). Test
meaningfulness — do the assertions verify the right things — is explicitly a human-review judgment
and appears as such in the [enforcement matrix](../governance/enforcement-matrix.md).

## Retirement log

None.
