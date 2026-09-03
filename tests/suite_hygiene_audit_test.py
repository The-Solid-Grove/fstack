#!/usr/bin/env python3

from pathlib import Path
import tempfile
import unittest

from suite_hygiene_audit import (
    audit_pairing,
    audit_python_syntax,
    audit_repo,
    audit_runner_wiring,
    audit_shell_conventions,
)


ROOT = Path(__file__).parents[1]

CONFORMING_SHELL = """\
#!/usr/bin/env bash
set -euo pipefail

echo ok
"""

WRONG_SHEBANG = """\
#!/bin/sh
set -euo pipefail

echo ok
"""

MISSING_STRICT_MODE = """\
#!/usr/bin/env bash

echo ok
"""

LATE_STRICT_MODE = """\
#!/usr/bin/env bash
# one
# two
# three
# four
set -euo pipefail
"""


def codes(diagnostics):
    return {diagnostic.code for diagnostic in diagnostics}


class ShellConventionTest(unittest.TestCase):
    def test_conforming_script_passes(self):
        self.assertEqual(audit_shell_conventions(CONFORMING_SHELL, "tests/x.sh"), [])

    def test_wrong_shebang_is_rejected(self):
        self.assertIn(
            "shell-shebang", codes(audit_shell_conventions(WRONG_SHEBANG, "tests/x.sh"))
        )

    def test_missing_strict_mode_is_rejected(self):
        self.assertIn(
            "shell-strict-mode",
            codes(audit_shell_conventions(MISSING_STRICT_MODE, "tests/x.sh")),
        )

    def test_strict_mode_outside_window_is_rejected(self):
        self.assertIn(
            "shell-strict-mode",
            codes(audit_shell_conventions(LATE_STRICT_MODE, "tests/x.sh")),
        )

    def test_empty_file_is_rejected(self):
        self.assertEqual(
            codes(audit_shell_conventions("", "tests/x.sh")),
            {"shell-shebang", "shell-strict-mode"},
        )


class FakeRepo:
    def __init__(self, base: Path):
        self.root = base
        (self.root / "tests").mkdir()

    def write(self, relative: str, text: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


class PairingTest(unittest.TestCase):
    def test_paired_audit_passes(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit.py", "x = 1\n")
            repo.write("tests/thing_audit_test.py", "x = 1\n")
            self.assertEqual(audit_pairing(repo.root / "tests"), [])

    def test_audit_without_test_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit.py", "x = 1\n")
            diagnostics = audit_pairing(repo.root / "tests")
            self.assertEqual(codes(diagnostics), {"audit-test-pairing"})
            self.assertIn("thing_audit_test.py", diagnostics[0].message)

    def test_test_without_audit_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit_test.py", "x = 1\n")
            self.assertEqual(
                codes(audit_pairing(repo.root / "tests")), {"audit-test-pairing"}
            )


class PythonSyntaxTest(unittest.TestCase):
    def test_valid_python_passes(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/helper.py", "def f():\n    return 1\n")
            self.assertEqual(audit_python_syntax(repo.root / "tests"), [])

    def test_broken_python_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/helper.py", "def f(:\n")
            self.assertEqual(
                codes(audit_python_syntax(repo.root / "tests")), {"python-syntax"}
            )


class RunnerWiringTest(unittest.TestCase):
    def test_wired_audit_passes(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit.py", "x = 1\n")
            repo.write("tests/thing_audit_test.py", "x = 1\n")
            repo.write(
                "tests/thing.sh",
                'python3 "$ROOT/tests/thing_audit_test.py"\n'
                'python3 "$ROOT/tests/thing_audit.py" "$ROOT"\n',
            )
            self.assertEqual(audit_runner_wiring(repo.root / "tests"), [])

    def test_audit_never_run_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit.py", "x = 1\n")
            repo.write("tests/thing_audit_test.py", "x = 1\n")
            repo.write("tests/thing.sh", "echo no python here\n")
            diagnostics = audit_runner_wiring(repo.root / "tests")
            self.assertEqual(codes(diagnostics), {"audit-runner-coverage"})
            self.assertEqual(len(diagnostics), 2)

    def test_unit_tests_skipped_by_runner_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing_audit.py", "x = 1\n")
            repo.write("tests/thing_audit_test.py", "x = 1\n")
            repo.write("tests/thing.sh", 'python3 "$ROOT/tests/thing_audit.py"\n')
            diagnostics = audit_runner_wiring(repo.root / "tests")
            self.assertEqual(codes(diagnostics), {"audit-runner-coverage"})
            self.assertIn("thing_audit_test.py", diagnostics[0].path)

    def test_dangling_runner_reference_is_rejected(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/thing.sh", 'python3 "$ROOT/tests/gone_audit.py"\n')
            self.assertEqual(
                codes(audit_runner_wiring(repo.root / "tests")),
                {"runner-python-refs"},
            )

    def test_non_audit_python_is_out_of_scope(self):
        with tempfile.TemporaryDirectory() as base:
            repo = FakeRepo(Path(base))
            repo.write("tests/helper.py", "x = 1\n")
            repo.write("tests/thing.sh", "python3 -c 'import yaml'\n")
            self.assertEqual(audit_runner_wiring(repo.root / "tests"), [])


class RepoTest(unittest.TestCase):
    def test_fstack_repo_is_clean(self):
        diagnostics = audit_repo(ROOT)
        self.assertEqual(
            [diagnostic.render() for diagnostic in diagnostics],
            [],
            "fstack's own suites violate suite hygiene",
        )


if __name__ == "__main__":
    unittest.main()
