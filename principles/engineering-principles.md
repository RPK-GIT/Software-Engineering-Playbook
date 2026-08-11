# Engineering Principles

> **Class:** Principles · **Status:** Active
> The stable "why" layer. Principles are **not rules**: they carry no rule IDs, no enforcement, and
> no normative keywords. Their role (per [PLAYBOOK-ARCHITECTURE.md](../PLAYBOOK-ARCHITECTURE.md) §2.2)
> is to justify standards and to break ties where standards are silent — a decision made on
> principles alone is recorded as an ADR so the gap gets closed.
> Every rule's rationale should trace back to at least one principle here (RULE-012).

## P-1 · Production is the measure of done

Work is finished when it runs correctly, securely, and observably in production — not when the code
compiles, not when the PR merges.
**Implications:** completion claims are checked against the Definition of Done; "works on my
machine" is a starting point, not a result; operational duties (logging, alarms, runbooks) are part
of the feature, not follow-up work.

## P-2 · Explicit over implicit

Rules, contracts, dependencies, and assumptions are stated where they can be read — by a human or a
machine — not carried in someone's head or inferred from convention.
**Implications:** explicit rules beat guidelines; configuration over convention when the two
conflict; interfaces declare their contracts; ambiguity is treated as a defect, not a flexibility.

## P-3 · Single source of truth

Every fact, rule, and decision has exactly one authoritative home; everything else references it.
**Implications:** rules are cited by ID, never copied; duplicated logic, duplicated schema
definitions, and duplicated documentation are all the same defect; when two sources disagree, fixing
the disagreement outranks the task that surfaced it.

## P-4 · Boring technology by default

Choose proven, widely understood technology unless a documented decision justifies novelty. Innovate
in the product, not in the plumbing.
**Implications:** new technology enters only through an ADR; the burden of proof is on the novel
choice; operational maturity (docs, hiring pool, failure modes known) counts as a feature.

## P-5 · Secure by default

Security is a starting condition, not an added layer. The safe path is the default path; the unsafe
path requires explicit, recorded intent.
**Implications:** least privilege everywhere; secrets never live in code; input is untrusted until
validated; security review is triggered by what a change touches, not by whether anyone remembered.

## P-6 · Design for failure

Everything fails: networks, disks, dependencies, deploys, people. Systems are built so failure is
survivable, visible, and recoverable.
**Implications:** timeouts, retries with backoff, and idempotency are design requirements, not
hardening; rollback paths exist before rollout; single points of failure require a recorded decision.

## P-7 · Observable by construction

A system's behavior must be explainable from its telemetry without attaching a debugger to
production. Observability is written with the code, not bolted on during the first incident.
**Implications:** structured logs, metrics, and traces are authoring-time duties; "how will we know
this is broken?" is a design-review question; unexplained states are treated as defects.

## P-8 · Small, reversible steps

Prefer many small changes that are easy to review, test, and undo over rare large changes that are
none of those things.
**Implications:** small PRs; incremental migrations; feature flags over long-lived branches;
anything hard to reverse (data deletion, public contracts, published versions) gets extra scrutiny.

## P-9 · Automate the repeatable, reserve humans for judgment

Anything checkable by a machine is checked by a machine; human attention is spent only where
judgment is genuinely required.
**Implications:** style debates end in a formatter config; CI gates encode the enforceable rules;
human review exists for design, boundaries, security, and meaning — not for whitespace.

## P-10 · Consistency over personal preference

A codebase reads as if one careful engineer wrote it. Individual taste yields to the established
standard, and changing the standard is done for everyone at once, through the change process.
**Implications:** follow the local idiom even when you'd choose differently; "better" alternatives
go through an RFC, not a one-off exception; consistency is what makes both humans and AI agents
effective across many repositories.

## P-11 · Build only what is needed

Solve the problem in front of you. Speculative generality, premature abstraction, and standards for
situations that don't exist yet are liabilities, not foresight.
**Implications:** this playbook itself defers documents until a real trigger exists (mobile);
abstractions must earn their existence with at least a second concrete use; deleting unused code and
unused rules is maintenance, not loss.

## P-12 · Legible to humans and machines

Every work product — code, documents, rules, decisions — is structured so that both a human and an
AI agent can find it, parse it, and act on it without a guide.
**Implications:** small single-topic files; stable IDs and closed vocabularies; declared context
(profiles, pinned versions) instead of tribal knowledge; if an agent misreads a document, the
document is the defect.
