#!/usr/bin/env python3
"""Validate the local skill library; no image generation or network calls."""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print("Missing PyYAML. Run: python3 -m pip install -r requirements-dev.txt", file=sys.stderr)
    raise SystemExit(2)


FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LOCAL_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
ALLOWED_FIELDS = {"name", "description", "license", "allowed-tools", "metadata"}


def load_mapping(text, label):
    value = yaml.safe_load(text)
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a YAML mapping")
    return value


def validate_skill(folder):
    errors = []
    manifest = folder / "SKILL.md"
    if not manifest.is_file():
        return ["missing SKILL.md"], None
    text = manifest.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return ["missing or malformed YAML frontmatter"], None
    try:
        data = load_mapping(match.group(1), "frontmatter")
    except (ValueError, yaml.YAMLError) as exc:
        return [f"invalid frontmatter: {exc}"], None
    name = data.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append("name must be lowercase hyphen-case and at most 64 characters")
    elif name != folder.name:
        errors.append(f"name {name!r} does not match folder {folder.name!r}")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("description must be nonempty text of at most 1024 characters")
    elif "<" in description or ">" in description:
        errors.append("description must not contain angle brackets")
    unexpected = set(data) - ALLOWED_FIELDS
    if unexpected:
        errors.append("unsupported frontmatter fields: " + ", ".join(sorted(map(str, unexpected))))
    if not text[match.end():].strip():
        errors.append("skill body is empty")
    if "[TODO:" in text:
        errors.append("unfinished scaffold placeholder")

    config_path = folder / "agents" / "openai.yaml"
    if not config_path.is_file():
        errors.append("missing agents/openai.yaml")
    else:
        try:
            config = load_mapping(config_path.read_text(encoding="utf-8"), "UI config")
            interface = config.get("interface")
            if not isinstance(interface, dict):
                errors.append("UI interface must be a mapping")
            else:
                display = interface.get("display_name")
                short = interface.get("short_description")
                if not isinstance(display, str) or not display.strip():
                    errors.append("UI display_name must be nonempty text")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append("UI short_description must be 25–64 characters")
                if "default_prompt" in interface:
                    prompt = interface["default_prompt"]
                    if not isinstance(prompt, str) or not isinstance(name, str) or f"${name}" not in prompt:
                        errors.append("UI default_prompt must mention this skill with $name")
            if "policy" in config:
                policy = config["policy"]
                if not isinstance(policy, dict):
                    errors.append("policy must be a mapping")
                elif "allow_implicit_invocation" in policy and not isinstance(policy["allow_implicit_invocation"], bool):
                    errors.append("allow_implicit_invocation must be boolean")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"invalid UI config: {exc}")
    return errors, name if isinstance(name, str) else None


def broken_local_links(path):
    errors = []
    # Prompt/code samples are not Markdown links.
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
    for match in LOCAL_LINK.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = target.split(' "', 1)[0]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        linked_path = path.parent / unquote(parsed.path)
        if not linked_path.exists():
            errors.append(f"broken local link: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    skill_root = root / ".agents" / "skills"
    folders = sorted(path for path in skill_root.iterdir() if path.is_dir()) if skill_root.is_dir() else []
    if not folders:
        print(f"FAIL: no skill folders in {skill_root}", file=sys.stderr)
        return 1
    failed = False
    names = set()
    for folder in folders:
        errors, name = validate_skill(folder)
        if name and name in names:
            errors.append(f"duplicate skill name: {name}")
        if name:
            names.add(name)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {folder.relative_to(root)}: {error}")
        else:
            print(f"PASS {folder.name}")
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules", "output"} for part in path.relative_to(root).parts):
            continue
        for error in broken_local_links(path):
            failed = True
            print(f"FAIL {path.relative_to(root)}: {error}")
    print(f"{len(folders)} skills checked; {'FAILED' if failed else 'all checks passed'}.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
