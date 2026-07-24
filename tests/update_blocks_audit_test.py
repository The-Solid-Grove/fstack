#!/usr/bin/env python3

from pathlib import Path
import unittest

from update_blocks_audit import audit_file, audit_repo


ROOT = Path(__file__).parents[1]

CONFORMING = """\
Some module prose.

> **Post-course update (verified July 2026): vendors consolidated.**
> Datadog acquired Eppo
> ([Datadog](https://www.datadoghq.com/blog/datadog-acquires-eppo/),
> May 2025).

More prose.
"""

MISSING_STAMP = """\
> **Post-course update: vendors consolidated.**
> Datadog acquired Eppo
> ([Datadog](https://www.datadoghq.com/blog/datadog-acquires-eppo/)).
"""

MISSING_SOURCE = """\
> **Post-course update (verified July 2026): vendors consolidated.**
> Datadog acquired Eppo, trust me.
"""

PLAIN_QUOTE = """\
> Example: *If we offer a 2nd subscription for meal plans, ARPPU grows.*
"""

TWO_BLOCKS = CONFORMING + "\n" + MISSING_SOURCE


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class UpdateBlocksAuditTest(unittest.TestCase):
    def test_conforming_block_passes(self):
        self.assertEqual(audit_file(CONFORMING, "module.md"), [])

    def test_missing_verified_stamp_is_rejected(self):
        self.assertIn(
            "update-block-verified-stamp", codes(audit_file(MISSING_STAMP, "module.md"))
        )

    def test_missing_source_link_is_rejected(self):
        self.assertIn(
            "update-block-source-link", codes(audit_file(MISSING_SOURCE, "module.md"))
        )

    def test_plain_blockquotes_are_ignored(self):
        self.assertEqual(audit_file(PLAIN_QUOTE, "module.md"), [])

    def test_blocks_are_audited_independently(self):
        diagnostics = audit_file(TWO_BLOCKS, "module.md")
        self.assertEqual(codes(diagnostics), {"update-block-source-link"})
        self.assertEqual(len(diagnostics), 1)

    def test_diagnostics_point_at_block_start_line(self):
        diagnostics = audit_file(MISSING_SOURCE, "module.md")
        self.assertEqual([d.line for d in diagnostics], [1])

    def test_current_corpus_conforms(self):
        self.assertEqual(
            [d.render() for d in audit_repo(ROOT)],
            [],
        )


if __name__ == "__main__":
    unittest.main()
