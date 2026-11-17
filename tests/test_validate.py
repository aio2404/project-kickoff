"""Exercise detection and reporting without storing real private data."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('package_validator', Path(__file__).resolve().parents[1] / 'scripts/validate.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PrivacyChecks(unittest.TestCase):
    def test_detects_credentials_without_echoing_them(self):
        fake = 'gh' + 'p_' + 'a' * 36
        findings = validator.privacy_findings('example.txt', fake)
        self.assertIn('example.txt: github-token', findings)
        self.assertNotIn(fake, '\n'.join(findings))

    def test_detects_home_paths(self):
        samples = ['/Us' + 'ers/example/private.txt', '/ho' + 'me/example/private.txt', 'C:' + '\\Users' + '\\example\\private.txt']
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertTrue(validator.privacy_findings('example.txt', sample))

    def test_detects_email(self):
        self.assertTrue(validator.privacy_findings('example.txt', 'person' + '@' + 'example.org'))

    def test_refuses_auth_and_session_files(self):
        self.assertTrue(validator.privacy_findings('auth.json', '{}'))
        self.assertTrue(validator.privacy_findings('session.jsonl', '{}'))

    def test_allows_placeholder_and_plugin_coordinate(self):
        self.assertEqual([], validator.privacy_findings('example.md', '<your-project>/.claude/skills; plugin@marketplace'))


class LocalLinks(unittest.TestCase):
    def test_missing_and_escaping_links_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            file = root / 'README.md'
            self.assertEqual(2, len(validator.local_link_findings(root, file, '[a](missing.md) [b](../outside.md)')))

    def test_existing_relative_and_external_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            file = root / 'README.md'
            (root / 'guide.md').write_text('ok')
            self.assertEqual([], validator.local_link_findings(root, file, '[a](guide.md#section) [b](https://example.org)'))

    def test_packaged_repository_passes(self):
        self.assertEqual([], validator.validate(Path(__file__).resolve().parents[1]))


if __name__ == '__main__':
    unittest.main()
