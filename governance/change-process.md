# Change Process

> **Class:** Governance · **Status:** Active
> How the playbook itself changes. Nothing normative changes outside this process (RULE-013).
> Terms: [GLOSSARY.md](../GLOSSARY.md). Precedence: [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.

## 1. Ownership

- **Playbook Owner / Principal Architect** — approves all normative changes (rules added, changed,
  deprecated, retired), all new documents, all new prefixes and tags, and all waivers.
- **Anyone** (engineer or AI agent) may propose a change. AI agents propose only; they never merge
  normative changes on their own authority.

## 2. Versioning policy (approved 2026-08-11)

The playbook is versioned with **Semantic Versioning through annotated git tags** (`vMAJOR.MINOR.PATCH`).

| Segment | Incremented for |
|---|---|
| **MAJOR** | Breaking changes to mandatory engineering standards: adding, removing, or materially changing MUST / MUST NOT requirements in a way that can invalidate existing compliant projects |
| **MINOR** | New standards or documents, new SHOULD / SHOULD NOT / MAY requirements, new applicability tags, and other backward-compatible additions |
| **PATCH** | Editorial, clarification, typo, formatting, and other non-normative changes |

Additional provisions:

- **`v1.0.0` = "Production Engineering Foundation"**: tagged at Phase 3 completion. It certifies
  the core architecture, engineering, security, API, database, observability, and reliability
  foundations for backend/service development — not completeness of profile-specific standards
  (web and mobile projects additionally require their Phase 4 standards; see
  [PLAYBOOK-ROADMAP.md](../PLAYBOOK-ROADMAP.md) "What v1.0.0 means").
- Every tag is annotated with a summary of the normative changes it contains (rule IDs added /
  changed / deprecated / retired).
- Project repositories pin a tag; see [how-to-use.md](how-to-use.md) for the upgrade contract.
- Retagging or deleting a published tag is prohibited; a bad release is followed by a corrective one.

## 3. Change flow

| Change class | Path |
|---|---|
| **Normative** (any rule or registry change → MAJOR/MINOR) | RFC required: create a proposal from [templates/rfc.md](../templates/rfc.md) → open a PR containing the RFC and the change → Playbook Owner decides → merge → tag |
| **Non-normative** (→ PATCH) | Direct PR, no RFC; Playbook Owner or a delegate approves; tagged individually or batched |
| **New document** | Follows the roadmap phase plan; the document's PR includes its DOCUMENT-INDEX.md entry and any new GLOSSARY terms; Playbook Owner approves |

Steps for a normative change:

1. Author the RFC (motivation, affected rule IDs, change class, migration impact).
2. Open a PR with the RFC and the proposed document edits together, so the decision and the diff
   are reviewed as one unit.
3. The Playbook Owner accepts, rejects, or returns it for revision. Acceptance is recorded in the
   RFC's decision section.
4. On merge: update `DOCUMENT-INDEX.md` if documents changed, update
   `governance/enforcement-matrix.md` if MUST rules changed (RULE-006), add GLOSSARY terms
   (RULE-010), and tag per §2.

## 4. Review cadence

The Playbook Owner runs a **quarterly review**: active waivers checked against expiry, deprecated
rules evaluated for retirement, rules that no project could cite in the quarter evaluated for
deletion ([P-11](../principles/engineering-principles.md)), and validation tooling gaps reviewed.

## 5. Playbook self-validation — required capabilities

Per the approved Phase 1 decision, this section defines **capabilities and acceptance criteria
only**; technology selection is a Phase 6 decision.

The playbook's own CI must be able to verify, on every PR to this repository:

| # | Capability | Acceptance criterion |
|---|---|---|
| V1 | Link integrity | Every relative link in every `.md` file resolves to an existing file |
| V2 | Rule-block format | Every `### <PREFIX>-<NNN>:` block parses against the grammar in [standards/_rule-format.md](../standards/_rule-format.md) §2 with all required fields present and valid |
| V3 | Rule-ID uniqueness | No ID appears in more than one rule block; no retired ID reappears |
| V4 | Prefix and tag registries | Every ID prefix and every "Applies to" tag exists in the §3/§4 registries (RULE-002, RULE-005) |
| V5 | Rule placement | No canonical rule block exists outside `standards/` and `agents/ai-agent-standards.md` (RULE-007) |
| V6 | Keyword discipline | No uppercase normative keyword imposes an obligation outside a rule block (RULE-004) — heuristic lint flags candidates for human review |
| V7 | Citation integrity | Every rule ID cited anywhere resolves to an existing Active or Deprecated rule |
| V8 | Enforcement-matrix completeness | Every Active `ci`/`review` MUST appears in the matrix (RULE-006; active from Phase 2) |
| V9 | Index consistency | Every file in the repo appears in `DOCUMENT-INDEX.md` and every ✅ entry exists on disk |

Until Phase 6 selects tooling, these checks are run ad hoc (scripted or manual) before each merge,
and a failed check blocks the merge exactly as CI would.
