"""Generate governance/enforcement-matrix.md from the canonical rule blocks.

Ad hoc Phase 2 tooling (not the Phase 6 CI selection). Classification sets below are
hand-curated - honesty about automatability is the point of the matrix.
"""
import re, glob, os

# Rules where enforcement is 'ci' but tooling is per-project, incomplete, or pending a later phase
PARTIAL = {
    'ARCH-006': 'Dependency-rule check; requires per-project boundary declaration + tooling',
    'CODE-011': 'Suppression-comment lint; tooling varies by ecosystem',
    'GIT-006': 'Commit-message lint in CI',
    'GIT-008': 'Platform merge-method setting; deliberate exceptions possible',
    'TEST-003': 'CI reruns / flake detection - detects, cannot prove absence',
    'TEST-004': 'Test-order randomization in CI - detects, cannot prove absence',
    'REPO-002': 'Secret scanning - tooling policy arrives Phase 3 (security.md); interim: review vigilance',
    'REPO-004': 'Template-file presence check; key completeness needs review',
    'REPO-010': 'Platform auto-delete setting; stale-branch detection is periodic',
    'AGENT-009': 'PR-description section lint - tooling to be built; interim: review',
}
# Rules where the human check is expert judgment (not an itemizable checklist)
JUDGMENT = {'ARCH-001','ARCH-002','ARCH-003','ARCH-008','ARCH-009',
            'CODE-004','CODE-009','TEST-011','GIT-011'}
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
}
PHASE1 = re.compile(r'^(RULE-\d+|AGENT-0(0\d|1[012]))$')

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
    phase = '1' if PHASE1.match(rid) else '2'
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
out.append("Rules classed `partial` above are the CI-automation backlog. Notable gaps: secret scanning")
out.append("(REPO-002 - policy owner is Phase 3 security.md), PR deviation-section lint (AGENT-009),")
out.append("boundary-declaration tooling guidance (ARCH-006), commit lint (GIT-006). A `partial` class")
out.append("is a statement that review currently carries part of the load - not that the rule is optional.")
out.append("")

open('governance/enforcement-matrix.md', 'w', encoding='utf-8', newline='\n').write("\n".join(out))
print(f"Wrote governance/enforcement-matrix.md with {len(rules)} rules")
print("Class totals:", counts)
