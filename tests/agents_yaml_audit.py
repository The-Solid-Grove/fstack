#!/usr/bin/env python3
"""Audit the per-skill `agents/openai.yaml` interface files.

Every skill ships an `agents/openai.yaml` so non-Claude hosts (Codex and other
OpenAI-style agents) get a display name, a short description, and a default
prompt that routes into the skill. These files are easy to forget when adding
a skill and easy to leave stale when renaming one, so this audit enforces the
contract mechanically:

1. Every `skills/<name>/` directory containing a `SKILL.md` has an
   `agents/openai.yaml`.
2. No `agents/openai.yaml` exists for a directory without a `SKILL.md`
   (a leftover from a deleted or renamed skill).
3. The yaml declares non-empty `interface.display_name`,
   `interface.short_description`, and `interface.default_prompt`.
4. `default_prompt` references the skill as `$<skill-dir-name>` so the prompt
   actually routes to the skill it sits next to.
5. `short_description` is a single line of at most 80 characters — it renders
   in list UIs where longer strings truncate.

The yaml shape is fixed (one `interface:` mapping of quoted scalar strings),
so this parses it with a line scanner instead of requiring PyYAML.

Exit code 0 when every skill conforms, 1 with one line per violation.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


SKILLS_DIR = "skills"
AGENTS_YAML = "agents/openai.yaml"
REQUIRED_KEYS = ("display_name", "short_description", "default_prompt")
SHORT_DESCRIPTION_MAX = 80
KEY_RE = re.compile(r'^\s{2}(\w+):\s*"(.*)"\s*$')


@dataclass(frozen=True)
class Diagnostic:
    code: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.code}: {self.message}"


def parse_interface(text: str) -> dict[str, tuple[int, str]]:
    """Return {key: (line_number, value)} for the `interface:` mapping."""
    values: dict[str, tuple[int, str]] = {}
    in_interface = False
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" "):
            in_interface = stripped == "interface:"
            continue
        if in_interface:
            match = KEY_RE.match(line)
            if match:
                values[match.group(1)] = (number, match.group(2))
    return values


def audit_yaml(text: str, path: str, skill_name: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    interface = parse_interface(text)

    for key in REQUIRED_KEYS:
        if key not in interface or not interface[key][1].strip():
            diagnostics.append(
                Diagnostic(
                    code="openai-yaml-missing-key",
                    path=path,
                    line=interface.get(key, (1, ""))[0],
                    message=f'`interface.{key}` must be a non-empty quoted string',
                )
            )

    if "default_prompt" in interface:
        line, prompt = interface["default_prompt"]
        if prompt.strip() and f"${skill_name}" not in prompt:
            diagnostics.append(
                Diagnostic(
                    code="openai-yaml-prompt-skill-ref",
                    path=path,
                    line=line,
                    message=(
                        f"`interface.default_prompt` must reference the skill "
                        f"as `${skill_name}` so it routes to this skill"
                    ),
                )
            )

    if "short_description" in interface:
        line, description = interface["short_description"]
        if len(description) > SHORT_DESCRIPTION_MAX:
            diagnostics.append(
                Diagnostic(
                    code="openai-yaml-short-description-length",
                    path=path,
                    line=line,
                    message=(
                        f"`interface.short_description` is {len(description)} chars; "
                        f"max is {SHORT_DESCRIPTION_MAX} (it truncates in list UIs)"
                    ),
                )
            )

    return diagnostics


def audit_repo(root: Path) -> list[Diagnostic]:
    skills = root / SKILLS_DIR
    diagnostics: list[Diagnostic] = []
    for skill_dir in sorted(path for path in skills.iterdir() if path.is_dir()):
        has_skill = (skill_dir / "SKILL.md").is_file()
        yaml_path = skill_dir / AGENTS_YAML
        relative = str(yaml_path.relative_to(root))
        if has_skill and not yaml_path.is_file():
            diagnostics.append(
                Diagnostic(
                    code="openai-yaml-missing",
                    path=relative,
                    line=1,
                    message="skill has a SKILL.md but no agents/openai.yaml",
                )
            )
        elif not has_skill and yaml_path.is_file():
            diagnostics.append(
                Diagnostic(
                    code="openai-yaml-orphan",
                    path=relative,
                    line=1,
                    message="agents/openai.yaml exists but the directory has no SKILL.md",
                )
            )
        elif has_skill:
            diagnostics.extend(
                audit_yaml(
                    yaml_path.read_text(encoding="utf-8"), relative, skill_dir.name
                )
            )
    return diagnostics


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    diagnostics = audit_repo(root)
    for diagnostic in diagnostics:
        print(diagnostic.render(), file=sys.stderr)
    return 1 if diagnostics else 0


if __name__ == "__main__":
    sys.exit(main())
