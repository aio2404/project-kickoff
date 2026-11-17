"""Offline package checks. Heuristics complement, never replace, human review."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKIP_DIRS = {'.git', '__pycache__', '.venv'}
PATTERNS = {
    'personal-home-path': re.compile(r'(?:/Users/|/home/)[A-Za-z0-9_.-]+/|[A-Za-z]:\\Users\\[A-Za-z0-9_.-]+\\'),
    'private-key': re.compile(r'-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----'),
    'github-token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b'),
    'provider-key': re.compile(r'\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}\b'),
    'email-address': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
}
REQUIRED = [
    'README.md', 'README.fr.md', 'LICENSE', 'SECURITY.md', 'CONTRIBUTING.md',
    'docs/usage.md', 'docs/evaluation.md',
    'skills/project-kickoff/SKILL.md', 'skills/project-kickoff/agents/openai.yaml',
    '.claude-plugin/plugin.json', '.claude-plugin/marketplace.json',
]


def privacy_findings(path: str, content: str) -> list[str]:
    """Return rule labels without exposing potentially sensitive matches."""
    findings = [f'{path}: {label}' for label, pattern in PATTERNS.items() if pattern.search(content)]
    name = Path(path).name.lower()
    if name in {'auth.json', 'credentials.json', '.env'} or (name.startswith('.env.') and name != '.env.example'):
        findings.append(f'{path}: forbidden-publication-file')
    if name.endswith(('.pem', '.key', '.jsonl')):
        findings.append(f'{path}: sensitive-or-session-file')
    return findings


def local_link_findings(root: Path, file: Path, content: str) -> list[str]:
    findings = []
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content):
        if target.startswith('#') or urlsplit(target).scheme:
            continue
        link = unquote(target.split('#', 1)[0])
        if not link:
            continue
        resolved = (file.parent / link).resolve()
        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
            findings.append(f'{file.relative_to(root)}: missing-or-escaping-local-link')
    return findings


def validate(root: Path) -> list[str]:
    findings = [f'{name}: missing-required-file' for name in REQUIRED if not (root / name).is_file()]
    for file in sorted(root.rglob('*')):
        relative = file.relative_to(root)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if file.is_symlink():
            findings.append(f'{relative}: symlink-not-allowed')
            continue
        if not file.is_file():
            continue
        try:
            content = file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            findings.append(f'{relative}: non-text-file-needs-review')
            continue
        findings.extend(privacy_findings(str(relative), content))
        if file.suffix == '.md':
            findings.extend(local_link_findings(root, file, content))

    skill = root / 'skills/project-kickoff/SKILL.md'
    if skill.is_file():
        content = skill.read_text()
        match = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
        if not match:
            findings.append('SKILL.md: missing-frontmatter')
        else:
            fields = dict(re.findall(r'^([a-z-]+): (.+)$', match.group(1), re.M))
            if fields.get('name') != 'project-kickoff' or not fields.get('description', '').strip():
                findings.append('SKILL.md: invalid-name-or-description')

    manifests = []
    for name in ['plugin.json', 'marketplace.json']:
        try:
            manifests.append(json.loads((root / '.claude-plugin' / name).read_text()))
        except (OSError, ValueError):
            findings.append(f'{name}: invalid-manifest')
    if len(manifests) == 2:
        plugin, marketplace = manifests
        entries = marketplace.get('plugins', [])
        if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
            findings.append('marketplace.json: expected-one-plugin')
        else:
            entry = entries[0]
            if (plugin.get('name') != 'project-kickoff' or entry.get('name') != plugin.get('name')
                    or entry.get('source') != './' or entry.get('version') != plugin.get('version')
                    or not re.fullmatch(r'\d+\.\d+\.\d+', str(plugin.get('version', '')))):
                findings.append('plugin.json: inconsistent-plugin-metadata')
    return findings


if __name__ == '__main__':
    repository = Path(__file__).resolve().parents[1]
    errors = validate(repository)
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('PASS: package structure, local links, manifests and privacy heuristics')
