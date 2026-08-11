# New Repository Checklist

> **Class:** Instrument (view) · **Gate:** repository created · **Status:** Active
> Completing this checklist is what "adopting the playbook" means mechanically for a new repo
> ([governance/how-to-use.md](../governance/how-to-use.md)). Items cite rule IDs (RULE-008).

## Required files

- [ ] `README.md` from [templates/readme.md](../templates/readme.md) — REPO-001, DOC-001
- [ ] `CLAUDE.md` from [templates/claude-md.md](../templates/claude-md.md), with **playbook version pinned and profile tags declared** — REPO-001
- [ ] `CODEOWNERS` with an owner for every top-level path — REPO-008
- [ ] `.gitignore` covering environment files, build outputs, local tooling — REPO-003, REPO-005
- [ ] Pull request template from [templates/pull-request.md](../templates/pull-request.md) — REPO-001
- [ ] Configuration template (e.g., `.env.example`) with placeholders, keys documented — REPO-004, DOC-005
- [ ] Dependency manifest + lockfile committed — REPO-006
- [ ] LICENSE, if code is distributed externally — REPO-001 (exception clause)

## Platform configuration

- [ ] Default branch protected: no direct pushes, no force pushes — GIT-003
- [ ] PR-only merges with required non-author approval — GIT-002, GIT-004
- [ ] Required status checks configured and blocking — GIT-005
- [ ] Squash-merge set as the merge method — GIT-008
- [ ] Auto-delete merged branches enabled — REPO-010

## Pipeline (minimum viable, day one)

- [ ] CI config committed to the repository — REPO-009
- [ ] Formatter, linter, type check wired as blocking steps — CODE-001, CODE-002, CODE-003
- [ ] Complexity limit active in static analysis — CODE-010
- [ ] Test run + coverage measurement and report — TEST-014, TEST-015
- [ ] Commit-message lint — GIT-006
- [ ] Dependency vulnerability scanning — SEC-019
- [ ] Secret scanning — SEC-020

## Structure and decisions

- [ ] Conventional top-level layout (src/tests/scripts/docs/migrations per ecosystem), stated in README — REPO-007
- [ ] `decisions/` directory initialized with an index — per [decisions/README.md](../decisions/README.md) scoping
- [ ] Stack-selection ADR(s) recorded — DOC-003 (trigger 1)
