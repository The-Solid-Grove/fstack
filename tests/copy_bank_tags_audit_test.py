#!/usr/bin/env python3

from pathlib import Path
import unittest

from copy_bank_tags_audit import (
    audit,
    audit_text,
    corpus_stems,
    normalize,
    tag_resolves,
)

ROOT = Path(__file__).parents[1]

STEMS = {
    normalize(stem)
    for stem in [
        "12min",
        "betterme-chair-yoga",
        "blesse",
        "blesse-live",
        "headway",
        "headway-funnel",
        "iq-brain",
        "muscle-booster",
    ]
}


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class TagResolutionTest(unittest.TestCase):
    def test_exact_match(self):
        self.assertTrue(tag_resolves("blesse", STEMS))

    def test_hyphen_insensitive(self):
        self.assertTrue(tag_resolves("iqbrain", STEMS))

    def test_tag_is_prefix_of_stem(self):
        self.assertTrue(tag_resolves("betterme", STEMS))

    def test_stem_is_prefix_of_tag(self):
        # `[headway-live]` means "the live walkthrough of headway".
        self.assertTrue(tag_resolves("headway-live", STEMS))

    def test_unknown_tag_does_not_resolve(self):
        self.assertFalse(tag_resolves("colonbroom", STEMS))

    def test_short_tag_requires_exact_match(self):
        self.assertFalse(tag_resolves("he", STEMS))
        self.assertTrue(tag_resolves("12", STEMS | {"12"}))


class AuditTextTest(unittest.TestCase):
    def test_tagged_lines_pass(self):
        text = '- "Become the most interesting person" [headway]\n'
        self.assertEqual(audit_text(text, STEMS), [])

    def test_multi_tag_line_passes(self):
        text = '- "3-minute quiz" [headway, 12min]\n'
        self.assertEqual(audit_text(text, STEMS), [])

    def test_untagged_list_line_is_flagged(self):
        text = '- "An orphaned line with no source"\n'
        diagnostics = audit_text(text, STEMS)
        self.assertEqual(codes(diagnostics), {"copy-bank-untagged-line"})
        self.assertEqual([d.line for d in diagnostics], [1])

    def test_unresolved_tag_is_flagged(self):
        text = '- "Gut issues suck" [colonbroom]\n'
        self.assertEqual(codes(audit_text(text, STEMS)), {"copy-bank-unresolved-tag"})

    def test_one_bad_tag_among_good_ones_is_flagged(self):
        text = '- "3-minute quiz" [headway, colonbroom]\n'
        diagnostics = audit_text(text, STEMS)
        self.assertEqual(codes(diagnostics), {"copy-bank-unresolved-tag"})
        self.assertEqual(len(diagnostics), 1)

    def test_markdown_link_is_not_a_tag(self):
        text = "- see [Headway](https://example.com)\n"
        self.assertEqual(codes(audit_text(text, STEMS)), {"copy-bank-untagged-line"})

    def test_non_list_lines_are_ignored(self):
        text = "## Section header\n\n**Cluster label:**\n"
        self.assertEqual(audit_text(text, STEMS), [])

    def test_fenced_code_is_ignored(self):
        text = "```\n- untagged line inside a fence\n```\n"
        self.assertEqual(audit_text(text, STEMS), [])

    def test_trailing_whitespace_is_tolerated(self):
        text = '- "quiz" [headway]  \n'
        self.assertEqual(audit_text(text, STEMS), [])


class CorpusStemsTest(unittest.TestCase):
    def test_indexes_and_readmes_are_not_source_notes(self):
        stems = corpus_stems(ROOT / "skills/writing-funnel-copy/references/funnels-research")
        self.assertNotIn(normalize("README"), stems)
        self.assertNotIn(normalize("00-COPY-BANK-by-screen-type"), stems)
        self.assertIn(normalize("headway-funnel"), stems)
        self.assertIn(normalize("iq-brain"), stems)


class RepoAuditTest(unittest.TestCase):
    def test_current_copy_bank_conforms(self):
        self.assertEqual(audit(ROOT), [])


if __name__ == "__main__":
    unittest.main()
