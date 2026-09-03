#!/usr/bin/env python3
"""Audit the health of fstack's own test suites and shell entry points.

Every guarantee fstack makes is enforced by a suite under `tests/`, so the
suites themselves need a mechanical floor: a runner that silently stopped
running its unit tests, an audit whose test file was renamed away, or a shell
script without strict mode would rot without anyone noticing. This audit
enforces:

1. Shell convention — every `tests/*.sh` plus the repo's shell entry points
   (`setup`, `scripts/ensure-fgrove-cli`) starts with `#!/usr/bin/env bash`
   and enables `set -euo pipefail` within its first five lines. (`bash -n`
   syntax checking lives in the runner, tests/suite-hygiene.sh.)
2. Audit/test pairing — every `tests/*_audit.py` has a sibling
   `tests/*_audit_test.py`, and vice versa.
3. Python parseability — every `tests/*.py` parses as Python source.
4. Runner coverage — every `tests/*_audit.py` and `tests/*_audit_test.py`
   is invoked by name from at least one `tests/*.sh` runner.
5. Runner references — every audit-shaped `*.py` name mentioned in a
   `tests/*.sh` runner resolves to a real file under `tests/` (catches
   renames that leave a runner pointing at nothing).

Exit code 0 when everything conforms, 1 with one line per violation.
"""

from __future__ import annotations

import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SHELL_ENTRY_POINTS = ("setup", "scripts/ensure-fgrove-cli")
EXPECTED_SHEBANG = "#!/usr/bin/env bash"
STRICT_MODE = "set -euo pipefail"
STRICT_MODE_WINDOW = 5
AUDIT_NAME_RE = re.compile(r"\b([a-z0-9_]+_audit(?:_test)?\.py)\b")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.code}: {self.message}"


def shell_scripts(root: Path) -> list[Path]:
    scripts = sorted((root / "tests").glob("*.sh"))
    for entry in SHELL_ENTRY_POINTS:
        path = root / entry
        if path.is_file():
            scripts.append(path)
    return scripts


def audit_shell_conventions(text: str, path: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != EXPECTED_SHEBANG:
        diagnostics.append(
            Diagnostic(
                code="shell-shebang",
                path=path,
                line=1,
                message=f"first line must be `{EXPECTED_SHEBANG}`",
            )
        )
    window = [line.strip() for line in lines[:STRICT_MODE_WINDOW]]
    if STRICT_MODE not in window:
        diagnostics.append(
            Diagnostic(
                code="shell-strict-mode",
                path=path,
                line=1,
                message=(
                    f"`{STRICT_MODE}` must appear within the first "
                    f"{STRICT_MODE_WINDOW} lines"
                ),
            )
        )
    return diagnostics


def audit_pairing(tests_dir: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    audits = {path.name for path in tests_dir.glob("*_audit.py")}
    unit_tests = {path.name for path in tests_dir.glob("*_audit_test.py")}
    for audit in sorted(audits):
        expected = audit.replace("_audit.py", "_audit_test.py")
        if expected not in unit_tests:
            diagnostics.append(
                Diagnostic(
                    code="audit-test-pairing",
                    path=f"tests/{audit}",
                    line=1,
                    message=f"audit has no unit-test sibling tests/{expected}",
                )
            )
    for unit_test in sorted(unit_tests):
        expected = unit_test.replace("_audit_test.py", "_audit.py")
        if expected not in audits:
            diagnostics.append(
                Diagnostic(
                    code="audit-test-pairing",
                    path=f"tests/{unit_test}",
                    line=1,
                    message=f"unit tests have no audit sibling tests/{expected}",
                )
            )
    return diagnostics


def audit_python_syntax(tests_dir: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for path in sorted(tests_dir.glob("*.py")):
        source = path.read_text(encoding="utf-8")
        try:
            ast.parse(source, filename=path.name)
        except SyntaxError as error:
            diagnostics.append(
                Diagnostic(
                    code="python-syntax",
                    path=f"tests/{path.name}",
                    line=error.lineno or 1,
                    message=f"file does not parse as Python: {error.msg}",
                )
            )
    return diagnostics


def audit_runner_wiring(tests_dir: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    python_files = {path.name for path in tests_dir.glob("*.py")}
    audit_shaped = {name for name in python_files if AUDIT_NAME_RE.fullmatch(name)}
    referenced: set[str] = set()
    for runner in sorted(tests_dir.glob("*.sh")):
        text = runner.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            for name in AUDIT_NAME_RE.findall(line):
                referenced.add(name)
                if name not in python_files:
                    diagnostics.append(
                        Diagnostic(
                            code="runner-python-refs",
                            path=f"tests/{runner.name}",
                            line=number,
                            message=f"references tests/{name}, which does not exist",
                        )
                    )
    for name in sorted(audit_shaped - referenced):
        diagnostics.append(
            Diagnostic(
                code="audit-runner-coverage",
                path=f"tests/{name}",
                line=1,
                message="not invoked by any tests/*.sh runner",
            )
        )
    return diagnostics


def audit_repo(root: Path) -> list[Diagnostic]:
    tests_dir = root / "tests"
    diagnostics: list[Diagnostic] = []
    for script in shell_scripts(root):
        relative = str(script.relative_to(root))
        diagnostics.extend(
            audit_shell_conventions(script.read_text(encoding="utf-8"), relative)
        )
    diagnostics.extend(audit_pairing(tests_dir))
    diagnostics.extend(audit_python_syntax(tests_dir))
    diagnostics.extend(audit_runner_wiring(tests_dir))
    return diagnostics


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    diagnostics = audit_repo(root)
    for diagnostic in diagnostics:
        print(diagnostic.render(), file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    sys.exit(main())
