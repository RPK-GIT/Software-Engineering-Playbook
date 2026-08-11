# Mobile Standard (MOB) — Stub

> **Class:** Standard · **Rule prefix:** `MOB` (reserved) · **Status:** Stub — trigger-gated
> **This document contains no normative rules.** It exists so the mobile domain has a declared
> owner, a reserved prefix, and an explicit activation path — and so nobody writes speculative
> mobile rules anywhere else ([P-11](../principles/engineering-principles.md); ARCH-008 applied
> to the playbook itself).

## Why a stub

Standards written without a concrete project are speculation that gets rewritten when reality
arrives. The mobile standard is deferred deliberately — not forgotten. Writing it now would also
force technology assumptions (native platforms vs cross-platform frameworks) that are ADR-scale
decisions belonging to the first real mobile project (DOC-003 trigger 1).

## Activation trigger

This standard is expanded when **an ADR proposing a mobile application project is accepted** —
org-level or project-level. Acceptance authority per [decisions/README.md](../decisions/README.md);
expansion of this document is a normative change following
[governance/change-process.md](../governance/change-process.md) (RFC + Playbook Owner approval).
The Playbook Owner determines applicability in the ADR decision.

Until then: no project may declare the `mobile` profile tag, and any rule tagged `mobile`
elsewhere in the playbook is dormant.

## What already applies to a future mobile project (no new rules needed)

Mobile inherits the core automatically, like every profile
([governance/how-to-use.md](../governance/how-to-use.md) §1): all `all`-tagged rules — the
architecture, coding, application, testing, git, repository, documentation, security, and
observability standards — plus `mobile`-tagged rules that already exist (TEST-008 end-to-end
journeys; SEC-001/002/003, SEC-012/013 client auth rules).

## Scope reserved for this document (when triggered)

Only mobile-specific deltas the core cannot cover — expected areas, recorded here so the future
author starts from a bounded scope, without prejudging any technology:

- application lifecycle (backgrounding, process death, state restoration)
- offline behavior, sync, and conflict handling
- store distribution, release channels, staged rollout, forced-upgrade policy
- push notifications and device permissions (least-privilege applied to device capabilities)
- on-device storage protection and platform keystore use (the mobile analogue of WEB-022/023)
- mobile accessibility (platform accessibility APIs — the WEB-001…008 analogue)
- device/network variability: performance and telemetry on constrained hardware
- crash reporting expectations (OBS-006 operationalized for mobile)

Technology selection (native iOS/Android, cross-platform frameworks) is explicitly **not**
predetermined here — it is the first ADR of the first mobile project.

## Derivation contract

When authored, mobile rules follow [standards/_rule-format.md](_rule-format.md), carry the
`mobile` applicability tag, may only *add strictness* relative to core standards (RULE-009), and
enter the [enforcement matrix](../governance/enforcement-matrix.md) like every other rule.

## Retirement log

None (no rules exist).
