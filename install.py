#!/usr/bin/env python3
"""Simple installer for myclaude - copies skills to ~/.claude/"""

import shutil
import sys
from pathlib import Path

# Check Python version
if sys.version_info < (3, 7):
    print("Error: Python 3.7 or later is required", file=sys.stderr)
    print(f"Current version: {sys.version}", file=sys.stderr)
    sys.exit(1)

# Paths
SCRIPT_DIR = Path(__file__).parent
INSTALL_DIR = Path.home() / ".claude"

# Skills to install
SKILLS = [
    "do",
    "product-requirements",
    "ask-questions-if-underspecified",
    "best-practices",
    "database-design",
    "backend-development",
    "frontend-design",
    "test-cases",
]


def main():
    print("Installing myclaude to ~/.claude/")

    skills_dir = INSTALL_DIR / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)

    # Copy each skill individually
    for skill in SKILLS:
        source = SCRIPT_DIR / "skills" / skill
        target = skills_dir / skill

        if not source.exists():
            print(f"  Warning: {skill} not found in source")
            continue

        if target.exists():
            print(f"  Updating: {skill}")
            shutil.rmtree(target)
        else:
            print(f"  Installing: {skill}")

        shutil.copytree(source, target)

    # Copy skills/README.md and skill-rules.json if they exist
    for file in ["README.md", "skill-rules.json"]:
        source = SCRIPT_DIR / "skills" / file
        target = skills_dir / file
        if source.exists():
            shutil.copy2(source, target)

    print(f"\n✓ Installation complete!")
    print(f"  Installed {len(SKILLS)} skills to: {skills_dir}")
    print(f"\nNext steps:")
    print('  1. Try: /do "build a todo app with user authentication"')
    print("  2. The workflow will guide you through 7 phases")


if __name__ == "__main__":
    main()
