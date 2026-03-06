#!/usr/bin/env python3
"""Simple uninstaller for myclaude - removes only myclaude skills"""

import shutil
import sys
from pathlib import Path

# Check Python version
if sys.version_info < (3, 7):
    print("Error: Python 3.7 or later is required", file=sys.stderr)
    print(f"Current version: {sys.version}", file=sys.stderr)
    sys.exit(1)

INSTALL_DIR = Path.home() / ".claude"

# Skills to uninstall (only myclaude skills)
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
    print("Uninstalling myclaude from ~/.claude/")

    skills_dir = INSTALL_DIR / "skills"
    removed_count = 0

    # Remove only myclaude skills
    for skill in SKILLS:
        skill_path = skills_dir / skill
        if skill_path.exists():
            print(f"  Removing: {skill}")
            shutil.rmtree(skill_path)
            removed_count += 1

    # Remove hooks directory (only for claudekit)
    hooks_dir = INSTALL_DIR / "hooks"
    if hooks_dir.exists():
        # Check if it's our hooks (has pre-bash.py, inject-spec.py, log-prompt.py)
        our_hooks = ["pre-bash.py", "inject-spec.py", "log-prompt.py"]
        if all((hooks_dir / h).exists() for h in our_hooks):
            print(f"  Removing: hooks")
            shutil.rmtree(hooks_dir)

    if removed_count > 0:
        print(f"\n✓ Uninstall complete ({removed_count} skills removed)")
    else:
        print("\n  No myclaude skills found")


if __name__ == "__main__":
    main()
