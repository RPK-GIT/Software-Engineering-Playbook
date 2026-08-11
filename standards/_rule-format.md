# Rule Format — Meta-Standard (RULE)

> **Class:** Standard · **Rule prefix:** `RULE` · **Status:** Active
> Governs every normative document in this playbook. It is authored first because every other
> standard depends on its grammar, and it is written in its own format (self-hosting).
> Document classes and precedence: [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §1–2.

## 1. Normative vocabulary

Exactly five normative keywords exist. Their meanings follow RFC 2119.

| Keyword | Meaning | Default exception path |
|---|---|---|
| **MUST** | Absolute requirement | Waiver only — [governance/waivers.md](../governance/waivers.md) |
| **MUST NOT** | Absolute prohibition | Waiver only |
| **SHOULD** | Required unless a valid reason exists in the specific case | Recorded, justified deviation |
| **SHOULD NOT** | Prohibited unless a valid reason exists in the specific case | Recorded, justified deviation |
| **MAY** | Genuinely optional; no justification needed either way | n/a |

No additional normative keywords are permitted. Words like "required", "shall", "always", or
"never" in lowercase prose carry **no** normative force anywhere in this playbook.

## 2. The canonical rule block

A rule is normative **only** when expressed in this exact structure:

```markdown
### <PREFIX>-<NNN>: <statement containing exactly one normative keyword>

- **Level:** MUST | MUST NOT | SHOULD | SHOULD NOT | MAY
- **Enforcement:** ci | review | manual
- **Applies to:** <comma-separated tags from the applicability registry>
- **Rationale:** <1–2 sentences; cites at least one principle P-n>
- **Exceptions:** waiver-only | none | justified-deviation | <explicit conditions>
```

Machine-readable grammar for the heading line (for validation tooling):

```
^### (?P<id>[A-Z]{2,6}-[0-9]{3}): (?P<statement>.+)$
```

Field semantics:

- **Statement** — imperative, active voice, explicit subject, one atomic requirement. If you need
  the word "and" to join two obligations, write two rules.
- **Level** — repeats the keyword used in the statement (redundancy is deliberate: it makes the
  block parseable without NLP).
- **Enforcement** — `ci`: deterministically checkable by a pipeline; `review`: verified at a named
  human gate; `manual`: a process obligation outside the PR flow (e.g., quarterly review).
- **Applies to** — tags from the registry in §4. An empty or unregistered tag is a format defect.
- **Exceptions** — `waiver-only` (default for MUST/MUST NOT), `justified-deviation` (default for
  SHOULD/SHOULD NOT), `none` (not even a waiver can lift it — reserved for legal/safety floors),
  or explicit conditions under which the rule does not apply.
- **Status** *(optional field)* — omitted means Active. `Deprecated (replaced by <ID>)` when
  superseded; deprecated rules remain binding until retired. Retired rules are removed from the
  document body and listed in the owning document's retirement log; their IDs are never reused.

Non-normative content (preambles, explanations, examples) is permitted in standards and is marked
by context; examples carry the prefix "Example (non-normative):".

## 3. Rule ID registry

| Prefix | Owning document | Prefix | Owning document |
|---|---|---|---|
| `RULE` | standards/_rule-format.md (this file) | `TEST` | standards/testing.md |
| `ARCH` | standards/architecture.md | `CI` | standards/ci-cd.md |
| `CODE` | standards/coding.md | `INFRA` | standards/infrastructure.md |
| `APP` | standards/application.md | `OBS` | standards/observability.md |
| `SEC` | standards/security.md | `OPS` | standards/operations.md |
| `API` | standards/api.md | `GIT` | standards/git.md |
| `DB` | standards/database.md | `REPO` | standards/repository.md |
| `WEB` | standards/web.md | `DOC` | standards/documentation.md |
| `MOB` | standards/mobile.md | `AGENT` | agents/ai-agent-standards.md |

New prefixes require a change through [governance/change-process.md](../governance/change-process.md).

## 4. Applicability tag registry

| Tag | Kind | Meaning |
|---|---|---|
| `all` | universal | Applies to every project and every change |
| `web` | profile | Project ships a browser-based interface |
| `mobile` | profile | Project ships a mobile application |
| `api-service` | profile | Project exposes a network API to other systems |
| `library` | profile | Project is consumed as a dependency, not deployed |
| `uses-database` | profile | Project owns a persistent datastore |
| `handles-pii` | trigger | The project or change touches personally identifiable information |
| `public-api` | trigger | The change affects an externally consumed contract |

*Profile* tags are declared once per project in its repository's `CLAUDE.md` (format defined in
[templates/claude-md.md](../templates/claude-md.md)). *Trigger* tags activate per change, based on
what the change touches. New tags require a change through governance/change-process.md.

## 5. Rule lifecycle

`Proposed` (exists only inside an RFC) → `Active` (merged; binding) → `Deprecated` (binding;
replacement named) → `Retired` (not binding; ID permanently reserved). All transitions go through
[governance/change-process.md](../governance/change-process.md) and are versioned per its policy.

---

## 6. Rules

### RULE-001: Every normative rule MUST be expressed in the canonical rule block defined in §2.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** A single parseable shape makes every rule identifiable, loadable, and checkable by humans, AI agents, and tooling alike ([P-12](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-002: Every rule ID MUST use a prefix from the registry in §3, followed by a three-digit sequence number that is unique within the prefix and is never reused after retirement.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Stable, unique IDs are what allow citation instead of duplication ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-003: A rule statement MUST contain exactly one normative keyword and exactly one atomic requirement.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Compound rules cannot be individually enforced, waived, or cited; atomicity removes interpretation disputes ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-004: An uppercase normative keyword MUST NOT be used to impose an obligation outside a canonical rule block.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** If binding language floats in prose, readers and agents cannot distinguish obligations from commentary. Mentioning a keyword (defining it, quoting a rule, discussing "a MUST") is permitted; using one to create a requirement outside a rule block is not ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### RULE-005: Every value in a rule's "Applies to" field MUST come from the applicability tag registry in §4.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Applicability resolution is mechanical only if the tag vocabulary is closed ([P-2](../principles/engineering-principles.md), [P-12](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-006: Every Active rule at level MUST or MUST NOT whose enforcement is `ci` or `review` MUST be listed in `governance/enforcement-matrix.md` with its gate.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** An unenforced mandatory rule reads as enforced and silently rots; the matrix is the honesty ledger ([P-2](../principles/engineering-principles.md), [P-9](../principles/engineering-principles.md)). The matrix ships in Phase 2; this rule binds from that point.
- **Exceptions:** waiver-only

### RULE-007: Normative rules MUST NOT be defined in any document outside `standards/` and `agents/ai-agent-standards.md`.

- **Level:** MUST NOT
- **Enforcement:** ci
- **Applies to:** all
- **Rationale:** Checklists, templates, governance, and routing documents are views and processes; letting them define rules recreates the duplication the playbook exists to prevent ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-008: A document that needs a rule owned by another document MUST cite the rule's ID instead of restating or paraphrasing the rule text.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** One authoritative rule in one place; copies drift and then conflict ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** a one-line non-normative summary next to the citation is permitted

### RULE-009: A derived or lower-precedence document MUST NOT relax a requirement established by a standard.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Derived documents may add strictness but never remove it; this is the mechanism that prevents implementation detail from overriding architecture (PLAYBOOK-ARCHITECTURE.md §2.2, [P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-010: A term with a specialized meaning MUST be defined in `GLOSSARY.md` before its first normative use.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A rule is only enforceable when its terms have exactly one meaning ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### RULE-011: A numeric policy value MUST be defined only in the standard that owns the topic, and every other document needing the value MUST cite that rule's ID.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** Thresholds (coverage floors, size limits, budgets) are policy choices that change; duplicating numbers guarantees stale contradictions ([P-3](../principles/engineering-principles.md)).
- **Exceptions:** none

### RULE-012: A rule's rationale SHOULD cite at least one engineering principle.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** all
- **Rationale:** A rule that serves no principle is a candidate for deletion; the citation keeps the rulebook honest ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### RULE-013: Rule lifecycle transitions MUST occur only through the process defined in `governance/change-process.md`.

- **Level:** MUST
- **Enforcement:** manual
- **Applies to:** all
- **Rationale:** Rules changed outside the change process are unversioned and unauditable, breaking the pinning contract projects rely on ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

## Retirement log

None.
