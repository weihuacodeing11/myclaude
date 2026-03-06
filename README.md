# myclaude

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-7.0-green)](https://github.com/weihuacodeing11/myclaude)

> Streamlined AI workflow for Claude Code - from requirements to complete app

English | [中文](README_CN.md)

## What is this?

A single, comprehensive workflow (`/do`) that takes you from a simple idea to a fully implemented app or website. No external dependencies, no complex setup - just Claude Code doing what it does best.

## Requirements

**For using the `/do` workflow:**
- **Python 3.7+** (uses only standard library, no external packages needed)
- **Claude Code CLI**

**For installation:**
- **Node.js** (if using NPX installer)
- **OR Python 3.7+** (if using `python install.py`)

Most systems have Python 3 pre-installed. Check with:
```bash
python3 --version
```

If not installed:
- **macOS/Linux**: Usually pre-installed
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

## Quick Start

```bash
# Install
npx github:weihuacodeing11/myclaude

# Use
/do "build a todo app with user authentication"
```

That's it! The workflow will:
1. 📋 Generate a comprehensive PRD through interactive dialogue
2. 🔍 Explore your codebase for patterns
3. ❓ Clarify any technical ambiguities
4. 🎨 Design database, backend, and frontend
5. ✅ Get your approval on the design
6. 💻 Implement everything with tests
7. 🚀 Review and provide deployment checklist

## The `/do` Workflow

A 7-phase systematic approach:

| Phase | What it does |
|-------|-------------|
| **1. Understand** | Gather requirements via interactive PRD generation |
| **2. Clarify** | Optional technical clarification |
| **3. Optimize** | Transform requirements with best practices |
| **4. Design** | Database, backend, and frontend architecture |
| **5. Review** | Design consistency and security check |
| **6. Implement** | Direct implementation with current Claude model |
| **7. Complete** | Final code review and deployment checklist |

## Features

- ✨ **Zero Dependencies** - Uses Claude Code's current model for everything
- 🎯 **Single Workflow** - One command, complete solution
- 🔄 **Interactive** - Asks questions when needed, not before
- 📦 **Simple Install** - One NPX command
- 🧪 **Test-Driven** - Generates and validates test cases
- 🎨 **Design-First** - Get approval before implementation

## Installation

```bash
# Interactive installer (recommended)
npx github:weihuacodeing11/myclaude

# Or install directly with Python (overwrites existing installation)
python install.py
```

## After Installation

The workflow installs to `~/.claude/`:

```
~/.claude/
├── skills/do/              # The /do workflow
│   ├── SKILL.md           # Main workflow definition
│   └── scripts/           # Task management scripts
└── installed_modules.json  # Tracks installation
```

## Examples

### Build a Todo App
```bash
/do "build a todo app with user authentication and real-time updates"
```

### Create a Landing Page
```bash
/do "create a modern landing page for a SaaS product with pricing tiers"
```

### Add a Feature
```bash
/do "add export to CSV functionality to the existing dashboard"
```

## How It Works

The `/do` workflow integrates several specialized skills:

- **product-requirements** - Interactive PRD generation with quality scoring
- **ask-questions-if-underspecified** - Clarify technical choices
- **best-practices** - Optimize requirements with 5 transformation principles
- **database-design** - Design database schema and migrations
- **backend-development** - Design backend API and architecture
- **frontend-design** - Design frontend UI and components
- **test-cases** - Generate structured test cases

All orchestrated by Claude Code's current model - no external tools needed.

## Troubleshooting

**Module not loading:**
```bash
cat ~/.claude/installed_modules.json
python install.py --force --module do
```

**Installation errors:**
```bash
python3 --version  # Requires 3.7+
python install.py --force --module do
```

## Uninstall

```bash
# Remove all installed files
python uninstall.py
```

## License

AGPL-3.0 - see [LICENSE](LICENSE)

For commercial use without AGPL obligations, contact: support@stellarlink.co

## Support

- [GitHub Issues](https://github.com/weihuacodeing11/myclaude/issues)
