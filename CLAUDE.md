# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a streamlined AI development workflow system for Claude Code. It provides a single, comprehensive workflow (`/do`) that takes you from requirements to a complete app or website.

**Core Philosophy:** One workflow, zero external dependencies, using Claude Code's current model for everything.

## Common Commands

### Installation & Management

```bash
# Interactive installer (recommended)
npx github:weihuacodeing11/myclaude

# Install do workflow
python install.py --module do

# Check installation status
python install.py --status
```

## Architecture

### The `/do` Workflow

A single, comprehensive 7-phase workflow that handles everything from requirements to deployment:

1. **Understand** - Gather requirements via `/product-requirements` skill
2. **Clarify** - Optional technical clarification
3. **Optimize** - Transform requirements via `/best-practices` skill
4. **Design** - Database, backend, and frontend design
5. **Review** - Design consistency check
6. **Implement** - Direct implementation with current Claude model
7. **Complete** - Final code review and summary

**Supporting Skills:**
- `product-requirements` - Interactive PRD generation with quality scoring
- `ask-questions-if-underspecified` - Clarify technical choices
- `best-practices` - Optimize requirements with 5 transformation principles
- `database-design` - Design database schema and migrations
- `backend-development` - Design backend API and architecture
- `frontend-design` - Design frontend UI and components
- `test-cases` - Generate structured test cases

### Installation Directory Structure

After installation, `~/.claude/` contains:

```
~/.claude/
├── CLAUDE.md                   # This file
├── skills/do/                  # The /do workflow
│   ├── SKILL.md               # Main workflow definition
│   ├── scripts/               # Task management scripts
│   └── references/            # Supporting skill references
└── installed_modules.json      # Tracks installed modules
```

## Usage

Simply run:

```bash
/do "build a todo app with user authentication"
```

The workflow will:
1. Generate a comprehensive PRD through interactive dialogue
2. Explore your codebase for patterns
3. Clarify any technical ambiguities
4. Design database, backend, and frontend
5. Get your approval on the design
6. Implement everything with tests
7. Review and provide deployment checklist

## Development Guidelines

### Project Structure

- `skills/do/SKILL.md` - Main workflow definition
- `skills/*/SKILL.md` - Supporting skills (product-requirements, database-design, etc.)
- `config.json` - Module configuration
- `install.py` - Installation script

### Making Changes

- All skills use current Claude model directly
- No external dependencies required
- Test changes with: `python install.py --module do --install-dir /tmp/test`

## Troubleshooting

**Module not loading**
```bash
cat ~/.claude/installed_modules.json
python install.py --force --module do
```

**Installation errors**
```bash
python3 --version  # Requires 3.7+
python install.py --force --module do
```

## License

AGPL-3.0 - For commercial use without AGPL obligations, contact: support@stellarlink.co
