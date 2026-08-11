# 0002 — GitHub Actions for playbook self-CI

- **Status:** Accepted
- **Date:** 2026-08-11
- **Deciders:** Playbook Owner

## Context

The playbook must validate its own governance invariants automatically (change-process §5,
capabilities V1–V15) — link integrity, rule format, ID uniqueness, matrix completeness, and the
rest. Until now these ran as ad hoc local scripts, which means a merge can skip them. Phase 6
permits exactly one technology decision: the toolchain that runs this validation. The repository
is hosted on GitHub; validation is ~200 lines of dependency-free Python; the repository contains
no application code, no secrets, and needs no build.

## Decision

**GitHub Actions runs the self-CI**, executing the existing Python validators
(`tools/validate.py`, `tools/gen_matrix.py`) via `.github/workflows/validate.yml`, with local
execution retained as the pre-push path (documented in CLAUDE.md).

Evaluation against the realistic options:

| Criterion | GitHub Actions | Local-only | External CI (self-hosted/other SaaS) |
|---|---|---|---|
| GitHub/PR/branch-protection integration | Native required-status-checks | None — merges can skip validation | Webhook plumbing to maintain |
| Maintenance | One YAML file | Zero, but unenforceable | New infrastructure for a docs repo |
| Runs existing Python | Preinstalled on runners, zero deps | Yes | Yes |
| Reproducibility | Same script local and CI | Same script | Same script |
| Speed / cost | Seconds; free at this scale | Instant; free | Slowest to set up; new cost/attack surface |
| Security | Read-only token suffices (see below) | n/a | New credential surface |
| AI-agent compatibility | Failure diagnostics in PR checks, readable via API | Agent must remember to run it | Varies |

Local-only fails the defining requirement — enforcement (a check that can be skipped is
advisory); external CI adds infrastructure a documentation repository cannot justify (ARCH-008
applied to ourselves). GitHub Actions is chosen for the integration, not the popularity.

## Security model (self-CI is production infrastructure)

- **Least privilege:** workflow `permissions: contents: read`; validation writes nothing.
- **Untrusted PRs:** triggers use `pull_request` (read-only token for forks), never
  `pull_request_target`; repository-controlled scripts therefore execute only with read access.
- **No secrets:** none are used, referenced, or available to the jobs.
- **Supply chain:** the only third-party action is `actions/checkout`; Python is
  runner-preinstalled, validators have zero dependencies to pin beyond the stdlib.
- **Hardening backlog:** pin `actions/checkout` by commit SHA before accepting external
  contributors (tracked here; version-tag pinning accepted for the single-maintainer bootstrap).

## Quality-gate classification (no second enforcement model)

Derived from existing rule enforcement semantics: **blocking** = deterministic checks backing
mandatory rules (V1–V5, V7–V9, V11–V15, matrix-drift) — the validator exits non-zero and the
required status check fails; **informational** = V6 keyword heuristic (RULE-004 is
review-enforced) and the V10 policy inventory — printed, never blocking, because CI must not
pretend to prove review-only compliance.

## Consequences

**Positive:** governance invariants become unskippable at merge and release; failure diagnostics
appear on the PR for humans and agents alike; the release job blocks a tag whose version
disagrees with the adoption template.

**Negative / accepted costs:** dependency on GitHub availability for merges; the current
direct-push-to-main bootstrap (single author, auto-sync) means enforcement tightens only when
branch protection with required checks is enabled — GIT-002/003/005 apply to this repository as
adoption matures, and enabling them is the first governance action for a second contributor.

## Alternatives considered

Recorded in the evaluation table above; both rejected for the reasons stated.

## Standards impact

- Implements change-process §5 capabilities as enforced checks (RULE-006 backstop V8 included).
- Complies with AGENT-013 by design: agents cannot loosen these gates, since the matrix-drift
  check regenerates from the rules themselves.
- Deviations: none. Waivers required: none.
