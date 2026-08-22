"""Generate governance/enforcement-matrix.md from the canonical rule blocks.

Ad hoc Phase 2 tooling (not the Phase 6 CI selection). Classification sets below are
hand-curated - honesty about automatability is the point of the matrix.
"""
import re, glob, os

# Rules where enforcement is 'ci' but tooling is per-project, incomplete, or pending a later phase
PARTIAL = {
    'ARCH-006': 'Dependency-rule check; requires per-project boundary declaration + tooling',
    'CODE-011': 'Suppression-comment lint; tooling varies by ecosystem',
    'CODE-015': 'Complexity/length warning in static analysis (values accepted 2026-08-11)',
    'GIT-006': 'Commit-message lint in CI',
    'GIT-008': 'Platform merge-method setting; deliberate exceptions possible',
    'GIT-013': 'PR-size warning in CI (accepted 2026-08-11; never auto-blocking)',
    'TEST-003': 'CI reruns / flake detection - detects, cannot prove absence',
    'TEST-004': 'Test-order randomization in CI - detects, cannot prove absence',
    'TEST-015': 'Diff-coverage report/warning (accepted 2026-08-11); exceptions per AGENT-009',
    'REPO-002': 'Secret scanning per SEC-020; tooling selection per project; review vigilance meanwhile',
    'REPO-004': 'Template-file presence check; key completeness needs review',
    'REPO-010': 'Platform auto-delete setting; stale-branch detection is periodic',
    'AGENT-009': 'PR-description section lint - tooling to be built; interim: review',
    'SEC-019': 'Dependency vulnerability scanner in CI - tooling selection per project (ADR)',
    'SEC-020': 'Secret scanner in CI - tooling selection per project (ADR)',
    'SEC-021': 'SAST in CI where the ecosystem has viable tooling',
    'SEC-028': 'Scanner severity gate (CVSS v3.1 >= 7.0; accepted 2026-08-11); waiver path is human-only',
    'API-001': 'Contract presence/lint check; contract *quality* needs review',
    'DB-001': 'Migration-tool presence/ordering check; migration *content* needs review',
    'CI-004': 'Artifact versioning/traceability check - registry and pipeline tooling per project',
    'INFRA-018': 'Non-root check in image lint/policy - tooling per project',
    'INFRA-020': 'Image scanner in pipeline - tooling selection per project (ADR); SEC-028 gate applies',
    'INFRA-021': 'SBOM generation step - tooling maturity varies by ecosystem',
    'INFRA-027': 'Attribution policy check (tagging/naming) - platform-dependent',
    'WEB-003': 'Accessibility lint (label association is deterministic); coverage depends on tooling',
    'WEB-006': 'Contrast checks in accessibility tooling; dynamic states need review',
    'WEB-009': 'Accessibility check step present in CI - tooling selection per project (ADR)',
    'WEB-010': 'Budget verification in CI - measurement tooling per project (ADR); values pending approval',
    'WEB-017': 'Response-header validation in CI/tests; per-response-class exceptions need review',
    'WEB-024': 'SRI/self-host lint on script tags; dynamically injected scripts need review',
}
# Rules where the human check is expert judgment (not an itemizable checklist)
JUDGMENT = {'ARCH-001','ARCH-002','ARCH-003','ARCH-008','ARCH-009',
            'APP-013','APP-014',
            'CODE-004','CODE-009','TEST-011','GIT-011',
            'SEC-004','DB-008','OBS-010','OBS-011','API-011',
            'WEB-008','WEB-016','WEB-018',
            'CI-011','CI-012','INFRA-013','INFRA-017'}
# Mechanism text overrides (default derived from enforcement + prefix)
MECH = {
    'GIT-002': 'Platform branch protection (PR-only)',
    'GIT-003': 'Platform branch protection settings',
    'GIT-004': 'Platform required-approval setting + CODEOWNERS',
    'GIT-005': 'Platform required-status-checks setting',
    'GIT-009': 'Platform force-push protection',
    'GIT-010': 'Tag presence check in release pipeline',
    'GIT-012': 'Same platform gates as regular changes',
    'REPO-001': 'Required-file presence check (new-repository checklist / CI)',
    'REPO-003': '.gitignore + tracked-file pattern check',
    'REPO-005': '.gitignore + tracked-file pattern check',
    'REPO-006': 'Lockfile presence check',
    'REPO-008': 'CODEOWNERS coverage check',
    'REPO-009': 'Pipeline-config presence check',
    'CODE-001': 'Formatter check (per-project tooling)',
    'CODE-002': 'Linter (per-project tooling)',
    'CODE-003': 'Type checker as blocking CI step',
    'CODE-010': 'Complexity rule in static analysis (value pending owner approval)',
    'TEST-014': 'Coverage measurement + report step in CI',
    'RULE-001': 'Playbook validation (V2)', 'RULE-002': 'Playbook validation (V3/V4)',
    'RULE-004': 'Playbook review + heuristic lint (V6)',
    'RULE-005': 'Playbook validation (V4)', 'RULE-006': 'Playbook validation (V8)',
    'RULE-007': 'Playbook validation (V5)',
}
GATE_BY_PREFIX = {
    'ARCH': 'Architecture review (structural changes, in code review)',
    'CODE': 'Code review', 'APP': 'Code review', 'TEST': 'Code review',
    'DOC': 'Code review', 'GIT': 'Code review', 'REPO': 'New-repository checklist / code review',
    'RULE': 'Playbook PR review', 'AGENT': 'Review of agent output (PR review)',
    'SEC': 'Security review (SEC-026 triggers) / code review',
    'API': 'Code review; architecture review for cross-component contracts',
    'DB': 'Code review; security review for classified-data migrations',
    'OBS': 'Code review',
    'WEB': 'Code review (web items in DoD); security review where SEC-026 triggers fire',
    'MOB': 'n/a - stub, no rules',
    'CI': 'Pipeline-change review / production-readiness gate',
    'INFRA': 'Infrastructure-change review / production-readiness gate',
    'OPS': 'Production-readiness gate / operational process',
}
PHASE1 = re.compile(r'^(RULE-\d+|AGENT-0(0\d|1[012]))$')
PHASE3_PREFIXES = {'SEC', 'API', 'DB', 'OBS'}
PHASE4 = {'WEB', 'MOB'}
PHASE4_IDS = {'SEC-028'}
PHASE5_PREFIXES = {'CI', 'INFRA', 'OPS'}
PHASE5_IDS = {'AGENT-015', 'AGENT-016', 'AGENT-017', 'WEB-029'}
PHASE6_IDS = {'AGENT-018', 'AGENT-019', 'AGENT-020', 'AGENT-021'}

rules = []
heading = re.compile(r'^### ([A-Z]{2,6}-[0-9]{3}): (.+)$', re.M)
for f in sorted(glob.glob('standards/*.md')) + ['agents/ai-agent-standards.md']:
    text = open(f, encoding='utf-8').read()
    for m in heading.finditer(text):
        rid = m.group(1)
        block = text[m.end():m.end()+900]
        lvl = re.search(r'\*\*Level:\*\* (MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b', block).group(1)
        enf = re.search(r'\*\*Enforcement:\*\* (\w+)', block).group(1)
        app = re.search(r'\*\*Applies to:\*\* ([^\n]+)', block).group(1).strip()
        rules.append((rid, os.path.basename(f), lvl, enf, app))

def row(rid, doc, lvl, enf, app):
    prefix = rid.split('-')[0]
    if enf == 'ci':
        cls = 'partial' if rid in PARTIAL else 'auto'
        ci = 'partial' if rid in PARTIAL else 'yes'
        ai, human = 'yes', 'spot-check' if rid in PARTIAL else 'no'
        mech = MECH.get(rid, PARTIAL.get(rid, 'Pipeline check (per-project tooling)'))
    elif enf == 'review':
        cls = 'judgment' if rid in JUDGMENT else 'review-only'
        ci, human = 'no', 'yes'
        ai = 'assists' if rid in JUDGMENT else 'yes'
        mech = MECH.get(rid, GATE_BY_PREFIX[prefix])
    else:
        cls, ci, ai, human = 'process', 'no', 'follows', 'yes'
        mech = MECH.get(rid, 'Process step (owner / quarterly review)')
    blocking = 'yes' if lvl in ('MUST', 'MUST NOT') else 'no'
    if rid in PHASE6_IDS:
        phase = '6'
    elif PHASE1.match(rid):
        phase = '1'
    elif prefix in PHASE5_PREFIXES or rid in PHASE5_IDS:
        phase = '5'
    elif prefix in PHASE4 or rid in PHASE4_IDS:
        phase = '4'
    elif prefix in PHASE3_PREFIXES:
        phase = '3'
    else:
        phase = '2'
    return f"| {rid} | {doc} | {lvl} | {app} | {mech} | {cls} | {ci} | {ai} | {human} | {blocking} | {phase} |"

out = []
out.append("# Enforcement Matrix")
out.append("")
out.append("> **Class:** Instrument · **Status:** Active (seeded Phase 2; regenerated whenever rules change)")
out.append("> The honesty ledger required by RULE-006: every rule mapped to how it is actually verified.")
out.append("> Generated from the canonical rule blocks by ad hoc tooling, with hand-curated")
out.append("> automatability classification; Phase 6 replaces the tooling, not the format.")
out.append(">")
out.append("> **Class values** - `auto`: deterministically enforced by CI · `partial`: CI catches some")
out.append("> violations, review covers the rest · `review-only`: checkable by a human against explicit")
out.append("> criteria · `judgment`: requires expert assessment; AI assists but a human decides ·")
out.append("> `process`: a process obligation outside the PR flow.")
out.append("> **AI agent column** - `yes`: the agent can fully self-enforce while authoring ·")
out.append("> `assists`: the agent applies it but cannot be the final check · `follows`: the agent")
out.append("> participates in the process. **Blocking** - a MUST-level rule blocks at its gate;")
out.append("> SHOULD-level deviations are recorded (AGENT-009), not blocked.")
out.append("")
out.append("| Rule | Standard | Level | Applies to | Enforcement mechanism | Class | CI | AI agent | Human | Blocking | Phase |")
out.append("|---|---|---|---|---|---|---|---|---|---|---|")
for r in rules:
    out.append(row(*r))
out.append("")
counts = {}
for r in rules:
    rid = r[0]
    if r[3] == 'ci':
        c = 'partial' if rid in PARTIAL else 'auto'
    elif r[3] == 'review':
        c = 'judgment' if rid in JUDGMENT else 'review-only'
    else:
        c = 'process'
    counts[c] = counts.get(c, 0) + 1
out.append(f"**Totals:** {len(rules)} rules - " + " · ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
out.append("")
out.append("## Tooling gaps (tracked for Phase 5/6)")
out.append("")
out.append("Rules classed `partial` above are the CI-automation backlog. Notable gaps: scanner selection")
out.append("per project via ADR (SEC-019/020/021, enforcing REPO-002), API contract diffing (API-001/002),")
out.append("migration linting (DB-001), PR deviation-section lint (AGENT-009), boundary-declaration")
out.append("tooling (ARCH-006), commit lint (GIT-006). Structured-logging lint (OBS-001) has no")
out.append("deterministic general implementation and is honestly review-classed. A `partial` class means")
out.append("review currently carries part of the load - not that the rule is optional.")
out.append("")

open('governance/enforcement-matrix.md', 'w', encoding='utf-8', newline='\n').write("\n".join(out))
print(f"Wrote governance/enforcement-matrix.md with {len(rules)} rules")
print("Class totals:", counts)
