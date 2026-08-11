# CLAUDE.md — AI Agent Entry Point

This repository is the **Software Engineering Playbook**: a standards repository, not an
application. There is no code to build, run, or test here — the work products are normative
documents. This file routes; it defines no rules (RULE-007).

## If you are consuming the playbook (working in a project repository)

1. You should have arrived from the project repo's own `CLAUDE.md` (pinned version + profile tags).
2. Load documents per [agents/context-map.md](agents/context-map.md) — reading order,
   always-applicable set, conditional sets.
3. Your binding behavior is defined in [agents/ai-agent-standards.md](agents/ai-agent-standards.md)
   (AGENT-001…AGENT-021): stricter reading on conflicts, stop on mandatory-rule ambiguity, never
   approve waivers, record deviations, verify before claiming done, surface unresolved questions,
   and the production/playbook integrity prohibitions.

## If you are editing the playbook itself

1. Structure is governed by [PLAYBOOK-ARCHITECTURE.md](PLAYBOOK-ARCHITECTURE.md); if your change
   contradicts it, fix your change or raise the contradiction — never silently rewrite the architecture.
2. Before authoring content, check the **anti-duplication register**
   (PLAYBOOK-ARCHITECTURE.md §6) and the document-ownership definitions (§5): every topic has
   exactly one owning document.
3. All normative content follows [standards/_rule-format.md](standards/_rule-format.md) — canonical
   blocks, registered prefixes and tags, one atomic requirement per rule.
4. Normative changes require the process in [governance/change-process.md](governance/change-process.md)
   (RFC, owner approval, semver tag). Non-normative fixes are direct PRs.
5. Before finishing any edit: run the self-CI locally — `python tools/validate.py` (blocking
   invariants V1–V15) and `python tools/gen_matrix.py` (then confirm no diff in
   `governance/enforcement-matrix.md`). The same checks run as required CI on GitHub
   ([ADR-0002](decisions/0002-github-actions-for-playbook-self-ci.md),
   `.github/workflows/validate.yml`). Update [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md),
   [GLOSSARY.md](GLOSSARY.md), and [PLAYBOOK-ROADMAP.md](PLAYBOOK-ROADMAP.md) statuses as needed.
6. Never modify playbook rules to make an implementation compliant (AGENT-021) — rule defects
   are proposed via RFC as their own change.

## Repository conventions

- Markdown links only to files that exist; planned documents are referenced in backticks.
- Keep documents single-topic and small; navigation belongs in the index and context map.
- Commits push automatically to GitHub via a Stop hook (`.claude/settings.json`); never commit
  secrets or credentials.
