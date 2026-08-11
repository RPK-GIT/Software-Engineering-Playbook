# Web Standard (WEB)

> **Class:** Standard · **Rule prefix:** `WEB` · **Status:** Active
> **Purpose:** browser-specific engineering floor — accessibility, performance, browser policy,
> web platform security controls, assets, and internationalization readiness.
> **Owns:** what runs in the browser and how it reaches it. Everything a mobile app would equally
> need lives in [application.md](application.md), not here.
> **Does not own:** general injection defense ([security.md](security.md) SEC-006 — this standard
> owns only the sanctioned rich-text path, WEB-021); token lifetimes (SEC-013 — this standard owns
> browser *storage* of tokens); API behavior ([api.md](api.md)); dependency selection
> ([coding.md](coding.md) CODE-012 — third-party scripts are dependencies).
> **Gate:** code review; header and accessibility checks per the
> [enforcement matrix](../governance/enforcement-matrix.md).
> **Applies to:** the `web` profile throughout; profile inheritance is automatic
> ([governance/how-to-use.md](../governance/how-to-use.md) §1.3) — a web project inherits these
> rules plus every matching core, security, API, database, and observability rule without listing
> anything manually.

Non-normative context: accessibility criteria reference **WCAG 2.2** — an externally maintained
public standard, cited rather than restated. No browser, framework, or tool is prescribed;
rendering-strategy and framework selections are ADRs (DOC-003 triggers 1 and 7).

## 1. Rules

### Accessibility

### WEB-001: All interactive functionality MUST be operable using a keyboard alone.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Keyboard operability is the substrate assistive technology builds on; a mouse-only path excludes users and fails WCAG 2.1.1 ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** functionality that is inherently pointer-dependent (freehand drawing), per WCAG's own exception

### WEB-002: Interfaces MUST use semantic markup — native elements and landmarks — rather than generic containers with re-implemented behavior.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** A native button ships with focus, keyboard, and screen-reader behavior for free; a clickable div ships with none and each re-implementation forgets something ([P-4](../principles/engineering-principles.md), [P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation where no native element exists for the pattern — the replacement then implements the full corresponding ARIA pattern

### WEB-003: Every form input MUST have a programmatically associated label.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** Placeholder text and visual proximity are invisible to assistive technology; the association is machine-checkable, making this one of the cheapest fully-lintable accessibility rules ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** none

### WEB-004: Form validation errors MUST be programmatically associated with the fields they concern and exposed to assistive technology.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** An error message only visible near a field tells a screen-reader user that submission failed and nothing else; association plus announcement is what makes error states accessible ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** none

### WEB-005: Dynamic view changes MUST manage keyboard focus explicitly.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** When content appears, moves, or disappears without focus management, keyboard and screen-reader users are left pointing at nothing — focus moves to new content, is contained in modals, and is restored on dismissal ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### WEB-006: Text and interactive elements MUST meet WCAG 2.2 AA contrast minimums.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** Contrast is objectively measurable and mostly automatable; the thresholds are WCAG's, maintained externally, not invented here ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** WCAG's own exceptions (logotypes, decorative elements, disabled states)

### WEB-007: Interfaces MUST remain functional at 200% zoom and at small-viewport reflow per WCAG 2.2 reflow criteria.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Zoom is the most common low-vision adaptation; layouts that clip, overlap, or trap horizontal scrolling at zoom exclude exactly those users — and the same discipline is what makes responsive behavior real ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** content that genuinely requires 2D layout (maps, data tables, diagrams), per WCAG's exception

### WEB-008: Web interfaces SHOULD conform fully to WCAG 2.2 Level AA.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** WEB-001…007 are the highest-leverage, objectively evaluable criteria; full AA is the complete target, SHOULD-level because whole-standard conformance requires audit-grade judgment beyond per-PR review ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation, recorded per finding

### WEB-009: CI MUST include automated accessibility checks for web interfaces.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** Automated checks catch roughly a third of accessibility defects — labels, contrast, ARIA misuse — for free on every PR; the mechanism is mandatory, tooling selection is per project (ADR) ([P-9](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### Performance

### WEB-010: Every web project MUST define performance budgets and verify them in CI.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** Performance regresses one small PR at a time; only a budget checked per change catches the drift while it is still one PR big. The mechanism is mandatory; default budget values are the proposed policy in §3 ([P-9](../principles/engineering-principles.md), [P-1](../principles/engineering-principles.md)).
- **Exceptions:** waiver-only

### WEB-011: Images MUST be sized and compressed appropriately for their display context.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Oversized images are the most common and most fixable performance defect — responsive sizing and modern compression are table stakes, not optimization ([P-1](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### WEB-012: Static assets MUST be served with an explicit caching policy.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Default cache behavior is whatever the server happened to send; explicit policy (long-lived immutable for content-addressed assets, revalidation for mutable ones) is the difference between repeat visits being instant or full re-downloads ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### WEB-013: JavaScript not required for the initial render SHOULD be loaded on demand.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Every shipped byte is parsed and compiled on the user's device, including the cheap ones; code splitting and lazy loading make the initial payload proportional to the initial need ([P-11](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### Browser policy

### WEB-014: Every web project MUST declare its supported browser matrix, derived from its user base and recorded with a maintenance rationale.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** "Works in the developer's browser" is not a policy; the matrix makes support decisions explicit and testable. The playbook names no browsers or versions — the project's actual users do, and the recorded rationale is what keeps the matrix maintained ([P-2](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### WEB-015: Browsers outside the supported matrix MUST receive an explicit, comprehensible experience rather than silent breakage.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** An unsupported-browser message costs an hour; a blank page costs every affected user and a support ticket each ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

### WEB-016: Core content and critical functionality SHOULD remain usable when JavaScript fails or is unavailable.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Scripts fail for reasons besides old browsers — flaky networks, blockers, CDN outages, one syntax error; progressive enhancement is failure design (P-6) applied to the client ([P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation — applications that are inherently client-computed (editors, visualization tools) record the decision once

### Web platform security

### WEB-017: Every web response MUST carry the baseline security headers defined in §2.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** These headers are one-line defenses against transport downgrade, MIME sniffing, framing attacks, and referrer leakage; the baseline is deliberately small and near-universal — application-specific tuning happens on top, not instead ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** individual headers inapplicable to a response class (e.g., HSTS on non-HTTPS internal tooling), recorded per project

### WEB-018: Every web application MUST deploy a Content Security Policy appropriate to its script and asset origins.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** CSP is the browser-enforced backstop when an injection defect slips past SEC-006 — it turns script injection from compromise into a violation report. No single configuration fits every application; "appropriate" means restrictive of script sources, reviewed with the threat model ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation with compensating controls, recorded via security review

### WEB-019: Cookies carrying authentication or session state MUST set secure attributes — Secure, HttpOnly, and an explicit SameSite policy.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Three attributes remove three attack classes: interception, script exfiltration, and ambient cross-site sending; token lifetime and revocation remain SEC-013 ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** HttpOnly omitted only where a documented pattern requires script access, with WEB-023 satisfied another way

### WEB-020: State-changing requests authenticated by cookies MUST be protected against cross-site request forgery.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Cookies are sent ambiently — any site can trigger a request that carries them; SameSite (WEB-019) reduces the surface, but tokens or equivalent verification close it ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** not applicable where authentication is exclusively via explicit headers (no ambient credential)

### WEB-021: User-supplied content rendered as HTML MUST pass through a maintained sanitizer with an allowlist configuration.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** SEC-006 forbids untrusted data reaching interpreters unencoded; rich text is the sanctioned exception path, and a maintained allowlist sanitizer is the only safe implementation of it — hand-rolled filters lose to the browser's parsing quirks every time ([P-5](../principles/engineering-principles.md), [P-4](../principles/engineering-principles.md)).
- **Exceptions:** none

### WEB-022: Secrets and privileged credentials MUST NOT be embedded in client-delivered code, configuration, or storage.

- **Level:** MUST NOT
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Everything delivered to the browser is public — bundles are readable, storage is inspectable; a "hidden" API key in frontend code is published. Server-side handling per SEC-009; this rule owns the client boundary ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** none — publishable client identifiers (by their issuer's definition) are not secrets

### WEB-023: Browser-stored authentication tokens MUST be protected from access by page scripts.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Any XSS foothold can read script-accessible storage; HttpOnly cookies or an equivalent isolation pattern keep a markup injection from becoming account takeover ([P-5](../principles/engineering-principles.md), [P-6](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation via security review, with the exfiltration risk explicitly accepted in the threat model

### WEB-024: Third-party scripts loaded from external origins MUST use subresource integrity or be self-hosted.

- **Level:** MUST
- **Enforcement:** ci
- **Applies to:** web
- **Rationale:** A third-party script runs with the page's full authority — an upstream compromise is your compromise; integrity pinning or self-hosting makes the executed bytes reviewable. Approval of the dependency itself is CODE-012 ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation for scripts that legitimately self-update (documented, threat-modeled), per security review

### WEB-025: CORS policies on authenticated resources MUST enumerate allowed origins rather than reflecting or wildcarding them.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** A reflected or wildcard origin with credentials hands every website your users visit an authenticated API client ([P-5](../principles/engineering-principles.md)).
- **Exceptions:** wildcard permitted only on genuinely public, unauthenticated resources

### Internationalization

### WEB-026: Applications with internationalization requirements MUST externalize user-facing text from code.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Hardcoded strings make localization a rewrite instead of a translation; externalization retrofitted later touches every view once more ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** not applicable to applications whose requirements explicitly exclude internationalization, recorded in the project's README or an ADR

### WEB-027: Applications with internationalization requirements MUST format dates, times, numbers, and currency through locale-aware mechanisms.

- **Level:** MUST
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Hand-formatted `MM/DD/YYYY` and decimal points are wrong for most of the world; the platform's locale facilities exist so nobody rebuilds them badly ([P-4](../principles/engineering-principles.md)).
- **Exceptions:** as WEB-026

### WEB-028: Layouts for localized applications SHOULD tolerate text expansion and direction change.

- **Level:** SHOULD
- **Enforcement:** review
- **Applies to:** web
- **Rationale:** Translations run 30–40% longer than English and some target languages are right-to-left; a layout that truncates or mirrors badly turns a translation task into a redesign ([P-8](../principles/engineering-principles.md)).
- **Exceptions:** justified-deviation

## 2. Baseline security headers (normative content of WEB-017)

| Header | Requirement |
|---|---|
| `Strict-Transport-Security` | Present on all HTTPS origins, with a max-age of meaningful duration |
| `X-Content-Type-Options` | `nosniff` on all responses |
| Frame protection | `frame-ancestors` in CSP (or `X-Frame-Options` where CSP is absent) restricting embedding to declared origins, or denying it |
| `Referrer-Policy` | Explicitly set; no leaking of full URLs cross-origin by default |

Content Security Policy is governed separately by WEB-018 because it cannot be baseline-uniform.
Applications add further headers as their threat model requires; this table is the floor, not the
ceiling.

## 3. Proposed policy values (pending approval — not yet binding)

**PROPOSED POLICY — default performance budgets (would give WEB-010 default values)**
- **Value:** at the 75th percentile on production-representative conditions: Largest Contentful Paint ≤ 2.5 s, Interaction to Next Paint ≤ 200 ms, Cumulative Layout Shift ≤ 0.1; initial-route JavaScript ≤ 200 KB compressed
- **Reason:** the first three are the externally maintained Core Web Vitals "good" thresholds — adopted by reference, not invented, and updated when the external definition updates; the JS budget is the one locally chosen number, set where mid-range mobile hardware keeps parse/execute cost tolerable
- **Risk of too strict:** teams burn time optimizing below human-perceptible differences, or route around the gate
- **Risk of too loose:** budgets stop shaping architecture decisions (rendering strategy, dependency weight) which are the real lever
- **Scope:** `web` profile; measured in CI via lab tooling per project (measurement tool is a project ADR); per-route overrides allowed with recorded justification
- **Status:** REQUIRES PLAYBOOK OWNER APPROVAL

## Interaction with other standards

General injection defense: SEC-006 (WEB-021 owns only the sanctioned rich-text path). Token
lifetime/revocation: SEC-013 (WEB-019/023 own the browser storage side). Rate limiting: SEC-023.
Third-party script approval: CODE-012 (WEB-024 owns delivery integrity). Rendering-strategy and
framework choices: ADRs per DOC-003. Ownership map: PLAYBOOK-ARCHITECTURE.md §6.

## Retirement log

None.
