import re, os, glob

md_files = [f.replace(os.sep, '/') for f in glob.glob('**/*.md', recursive=True)]
md_files = [f for f in md_files if not f.startswith('.claude')]
issues = []

# --- V1: link integrity (relative to each file's directory) ---
for f in md_files:
    base = os.path.dirname(f)
    text = open(f, encoding='utf-8').read()
    for m in re.finditer(r'\[[^\]]*\]\(([^)#\s]+)(#[^)]*)?\)', text):
        t = m.group(1)
        if t.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, t))):
            issues.append(f"V1 {f}: broken link -> {t}")

# --- V2/V3/V4/V5: rule blocks ---
PREFIXES = {'RULE','ARCH','CODE','APP','SEC','API','DB','WEB','MOB','TEST','CI','INFRA','OBS','OPS','GIT','REPO','DOC','AGENT'}
TAGS = {'all','web','mobile','api-service','library','uses-database','handles-pii','public-api'}
LEVELS = {'MUST','MUST NOT','SHOULD','SHOULD NOT','MAY'}
ENF = {'ci','review','manual'}
ALLOWED = {'standards/_rule-format.md', 'agents/ai-agent-standards.md'}
heading_re = re.compile(r'^### ([A-Z]{2,6}-[0-9]{3}): (.+)$', re.M)
ids, statements = {}, {}
for f in md_files:
    text = open(f, encoding='utf-8').read()
    for m in heading_re.finditer(text):
        rid, stmt = m.group(1), m.group(2)
        if f not in ALLOWED and not f.startswith('standards/'):
            issues.append(f"V5 {f}: rule block {rid} outside standards/ and agent standard (RULE-007)")
        if rid.split('-')[0] not in PREFIXES:
            issues.append(f"V4 {f}: unregistered prefix in {rid}")
        if rid in ids:
            issues.append(f"V3 duplicate rule ID {rid} in {f} and {ids[rid]}")
        ids[rid] = f
        if stmt in statements:
            issues.append(f"V3 duplicate statement: {rid} == {statements[stmt]}")
        statements[stmt] = rid
        block = text[m.end():m.end() + 900]
        lvl = re.search(r'\*\*Level:\*\* (MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b', block)
        enf = re.search(r'\*\*Enforcement:\*\* (\w+)', block)
        app = re.search(r'\*\*Applies to:\*\* ([^\n]+)', block)
        rat = re.search(r'\*\*Rationale:\*\*', block)
        exc = re.search(r'\*\*Exceptions:\*\*', block)
        if not (lvl and enf and app and rat and exc):
            issues.append(f"V2 {rid}: missing required field(s)")
            continue
        if enf.group(1) not in ENF:
            issues.append(f"V2 {rid}: invalid enforcement '{enf.group(1)}'")
        if lvl.group(1) not in stmt:
            issues.append(f"V2 {rid}: level '{lvl.group(1)}' not present in statement")
        for tag in [t.strip() for t in app.group(1).split(',')]:
            if tag not in TAGS:
                issues.append(f"V4 {rid}: unregistered applicability tag '{tag}'")

print(f"Rules found: {len(ids)}")
print("  " + ", ".join(sorted(ids)))

# --- V6: heuristic — uppercase keywords outside rule blocks/level fields (human-review list) ---
v6 = []
for f in md_files:
    for i, line in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
        if re.match(r'^### [A-Z]{2,6}-[0-9]{3}:', line) or line.strip().startswith('- **Level:**'):
            continue
        if re.search(r'\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b', line):
            v6.append(f"{f}:{i}: {line.strip()[:100]}")
print(f"\nV6 candidates (mention vs obligation - needs human review): {len(v6)}")
for h in v6:
    print("  " + h)

# --- V7: citation integrity (PLAYBOOK-DESIGN.md exempt: superseded history with illustrative IDs) ---
cite_re = re.compile(r'\b(?:RULE|AGENT|ARCH|CODE|APP|SEC|API|DB|WEB|MOB|TEST|INFRA|OBS|OPS|GIT|REPO|DOC)-[0-9]{3}\b')
for f in md_files:
    if f == 'PLAYBOOK-DESIGN.md':
        continue
    text = open(f, encoding='utf-8').read()
    for c in set(cite_re.findall(text)):
        if c not in ids:
            issues.append(f"V7 {f}: cites nonexistent rule {c}")
ptext = open('principles/engineering-principles.md', encoding='utf-8').read()
pdefined = set(re.findall(r'^## (P-\d+)', ptext, re.M))
for f in md_files:
    if f == 'principles/engineering-principles.md':
        continue
    for p in set(re.findall(r'\bP-\d+\b', open(f, encoding='utf-8').read())):
        if p not in pdefined:
            issues.append(f"V7 {f}: cites nonexistent principle {p}")

# --- V9: index consistency ---
idx = open('DOCUMENT-INDEX.md', encoding='utf-8').read()
for f in md_files:
    if f not in idx and os.path.basename(f) not in idx:
        issues.append(f"V9 DOCUMENT-INDEX.md missing entry for {f}")
for m in re.finditer(r'`([^`]+\.md)`[^|]*\|[^|]*\|[^|]*\|[^|]*✅', idx):
    if not os.path.exists(m.group(1)):
        issues.append(f"V9 index marks existing but file missing: {m.group(1)}")

# --- Technology-agnosticism (all docs except superseded design history) ---
tech = re.compile(r'\b(React|Angular|Vue|Django|Rails|Spring|Flyway|PostgreSQL|MySQL|MongoDB|Kubernetes|Terraform|AWS|Azure|GCP|Node\.js|TypeScript|Python|Java\b|Kotlin|Swift|Docker|Jenkins|GitHub Actions)\b')
for f in md_files:
    if f == 'PLAYBOOK-DESIGN.md':
        continue
    for m in tech.finditer(open(f, encoding='utf-8').read()):
        issues.append(f"TECH {f}: '{m.group()}'")

print("\n" + "=" * 50)
if issues:
    print(f"ISSUES ({len(issues)}):")
    print("\n".join(issues))
else:
    print("ALL AUTOMATED CHECKS PASS: V1-V5, V7, V9 + tech-agnosticism. (V8 n/a until Phase 2 matrix exists.)")
print(f"Files checked: {len(md_files)}")
