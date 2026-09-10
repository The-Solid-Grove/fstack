#!/usr/bin/env python3
"""Unit tests for corpus_path_refs_audit.py."""

import tempfile
import unittest
from pathlib import Path

from corpus_path_refs_audit import audit, extract_tokens

CORPUS = "skills/writing-funnel-copy/references/funnels-research"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ExtractTokensTest(unittest.TestCase):
    def test_backticked_and_bare_tokens_found(self):
        tokens = extract_tokens(
            "See `00-QA-CHECKLIST.md` and also live/acely.md for detail."
        )
        self.assertEqual(
            tokens, [(1, "00-QA-CHECKLIST.md"), (1, "live/acely.md")]
        )

    def test_bare_token_without_slash_ignored(self):
        self.assertEqual(extract_tokens("mentioned in README.md casually"), [])

    def test_fenced_code_ignored(self):
        text = "```\nfake/path.md\n```\nreal/path.md\n"
        self.assertEqual(extract_tokens(text), [(4, "real/path.md")])

    def test_backticked_token_not_double_counted_as_bare(self):
        self.assertEqual(
            extract_tokens("see `live/acely.md` here"), [(1, "live/acely.md")]
        )

    def test_parent_relative_token_found(self):
        self.assertEqual(
            extract_tokens("from `../live/*.md` walks"), [(1, "../live/*.md")]
        )


class CorpusPathRefsAuditTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.corpus = self.root / CORPUS
        self.addCleanup(self._tmp.cleanup)

    def test_missing_corpus_directory_fails(self):
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("corpus directory not found", errors[0])

    def test_resolving_same_dir_reference_passes(self):
        write(self.corpus / "00-QA-CHECKLIST.md", "checklist")
        write(self.corpus / "00-NOTES.md", "see `00-QA-CHECKLIST.md`")
        self.assertEqual(audit(self.root), [])

    def test_missing_reference_flagged_with_location(self):
        write(self.corpus / "00-NOTES.md", "intro\nsee `00-MISSING.md`")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("00-NOTES.md:2", errors[0])
        self.assertIn("`00-MISSING.md`", errors[0])

    def test_glob_resolving_passes_and_empty_glob_flagged(self):
        write(self.corpus / "live/acely.md", "walk")
        write(
            self.corpus / "00-NOTES.md",
            "walked `live/*.md` but never `missing-dir/*.md`",
        )
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("`missing-dir/*.md`", errors[0])

    def test_bare_wrong_directory_reference_flagged(self):
        write(self.corpus / "live/acely.md", "walk")
        write(self.corpus / "copy/swipe.md", "from funnel-research/live/*.md")
        errors = audit(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("`funnel-research/live/*.md`", errors[0])

    def test_external_basenames_and_prefixes_ignored(self):
        write(
            self.corpus / "teardown.md",
            "per `PRODUCT_SENSE.md` and `PLAN.md`; see "
            "`docs/funnelsgrove/START-HERE.md` and src/steps/step-01.md",
        )
        self.assertEqual(audit(self.root), [])

    def test_parent_relative_reference_resolves(self):
        write(
            self.root
            / "skills/writing-funnel-copy/references/funnel-psychology-framework.md",
            "framework",
        )
        write(
            self.corpus / "00-NOTES.md",
            "model from `../funnel-psychology-framework.md`",
        )
        self.assertEqual(audit(self.root), [])

    def test_references_root_fallback_resolves(self):
        write(
            self.root
            / "skills/writing-funnel-copy/references/funnel-paywall-best-practices.md",
            "paywall",
        )
        write(
            self.corpus / "sub/00-NOTES.md",
            "see `funnel-paywall-best-practices.md`",
        )
        self.assertEqual(audit(self.root), [])

    def test_corpus_root_fallback_resolves_from_subdir(self):
        write(self.corpus / "00-LIVE-FINDINGS.md", "findings")
        write(self.corpus / "copy/swipe.md", "see `00-LIVE-FINDINGS.md`")
        self.assertEqual(audit(self.root), [])


class CurrentCorpusConformsTest(unittest.TestCase):
    def test_current_corpus_conforms(self):
        repo_root = Path(__file__).resolve().parent.parent
        self.assertEqual(audit(repo_root), [])


if __name__ == "__main__":
    unittest.main()
