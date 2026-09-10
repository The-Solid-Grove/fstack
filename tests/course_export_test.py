"""Exercise course export via its CLI against real temporary Git revisions."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/sync-course'
CONTENT = 'apps/web/src/content/web2web'

class CourseExportTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        self.git('init', '-q')
        for name, text in [('index.md', '# Course\n\n[Lesson](01-intro.md)\n'), ('01-intro.md', '# Intro\n\nExact source text.\n'), ('templates/index.md', '# Templates\n')]:
            p = self.source / CONTENT / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
        cards = self.source / 'apps/web/src/lib/web2webOnePagers.json'
        cards.parent.mkdir(parents=True, exist_ok=True)
        cards.write_text(json.dumps({'cards': [{'slug': '01-intro', 'title': 'Memo', 'thesis': 'Exact thesis.', 'coreRule': 'Rule.', 'sections': [{'title': 'Section', 'items': ['Exact item.']}], 'decisionCheck': 'Check?'}]}))
        self.git('add', '.')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'course')
        self.sha = self.git('rev-parse', 'HEAD').strip()
        self.dest = self.root / 'skill'

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.source), *args], text=True)

    def run_cli(self, *args, ok=True):
        result = subprocess.run(['python3', str(SCRIPT), '--skill-dir', str(self.dest), *args], text=True, capture_output=True)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return result

    def export(self):
        self.run_cli('--source', str(self.source), '--ref', self.sha)

    def test_exact_committed_export_and_offline_check(self):
        (self.source / CONTENT / '01-intro.md').write_text('uncommitted replacement')
        self.export()
        self.assertEqual((self.dest / 'references/01-intro.md').read_text(), '# Intro\n\nExact source text.\n')
        self.assertEqual(json.loads((self.dest / 'course.json').read_text())['commit'], self.sha)
        memo = (self.dest / 'references/one-pagers.md').read_text()
        for phrase in ('Memo', 'Exact thesis.', 'Rule.', 'Section', 'Exact item.', 'Check?'):
            self.assertIn(phrase, memo)
        self.run_cli('--check')
        self.run_cli('--check', '--source', str(self.source), '--ref', self.sha)

    def test_check_detects_changes_additions_and_deletions(self):
        for kind in ['change', 'addition', 'deletion']:
            with self.subTest(kind=kind):
                self.export()
                p = self.dest / 'references/01-intro.md'
                if kind == 'change': p.write_text('drift')
                elif kind == 'addition': (p.parent / 'extra.md').write_text('extra')
                else: p.unlink()
                self.run_cli('--check', ok=False)

    def test_failed_source_preserves_snapshot(self):
        self.export()
        before = (self.dest / 'course.json').read_bytes()
        self.run_cli('--source', str(self.source), '--ref', 'missing-ref', ok=False)
        self.assertEqual((self.dest / 'course.json').read_bytes(), before)
        self.run_cli('--check')

    def test_new_revision_replaces_removed_files(self):
        self.export()
        self.git('rm', CONTENT + '/01-intro.md')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.test', 'commit', '-qm', 'remove lesson')
        self.run_cli('--check', '--source', str(self.source), '--ref', 'HEAD', ok=False)
        self.run_cli('--source', str(self.source), '--ref', 'HEAD')
        self.assertFalse((self.dest / 'references/01-intro.md').exists())
        self.run_cli('--check')

if __name__ == '__main__': unittest.main()
