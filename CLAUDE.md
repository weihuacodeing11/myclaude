# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-agent workflow system for Claude Code that provides orchestrated AI development workflows. The system consists of:

1. **Python-based installer** (`install.py`) - JSON-driven modular installation system
2. **Go-based codeagent-wrapper** - Multi-backend AI CLI wrapper (Codex/Claude/Gemini/OpenCode)
3. **Skills and agents** - Modular workflow components installed to `~/.claude/`

## Common Commands

### Installation & Management

```bash
# Interactive installer (recommended)
npx github:weihuacodeing11/myclaude

# List available modules/skills
npx github:weihuacodeing11/myclaude --list

# Update installed modules
npx github:weihuacodeing11/myclaude --update

# Install specific module
python install.py --module do
python install.py --module omo,sparv

# Uninstall module
python install.py --uninstall --module do

# Check installation status
python install.py --status
```

### codeagent-wrapper Development

```bash
# Build the Go wrapper
cd codeagent-wrapper
make build

# Run tests
make test

# Lint code
make lint

# Install to $GOPATH/bin
make install

# Clean build artifacts
make clean
```

### Legacy Makefile Deployment

```bash
# Deploy specific workflows (legacy)
make deploy-bmad
make deploy-requirements
make deploy-essentials

# Update CHANGELOG.md
make changelog
```

## Architecture

### Two-Tier Agent System

The system uses a **orchestrator-executor** pattern:

| Role | Component | Responsibility |
|------|-----------|----------------|
| **Orchestrator** | Claude Code | Planning, context gathering, verification, user interaction |
| **Executor** | codeagent-wrapper | Code editing, test execution via multiple AI backends |

This separation allows Claude Code to focus on high-level reasoning while delegating implementation to specialized backend agents.

### Module System

Modules are defined in `config.json` with three types of operations:

1. **copy_file** - Copy single file to target location
2. **copy_dir** - Copy entire directory recursively
3. **merge_dir** - Merge directory contents (preserves existing files)
4. **run_command** - Execute shell command during installation

Each module can define:
- `agents` - Backend/model configurations for codeagent-wrapper
- `operations` - Installation steps
- `enabled` - Whether module is active by default

### codeagent-wrapper Architecture

Located in `codeagent-wrapper/`, this Go CLI provides:

```
cmd/codeagent-wrapper/main.go   # Entry point
internal/
  app/          # CLI commands, argument parsing, orchestration
  backend/      # Backend implementations (codex/claude/gemini/opencode)
  config/       # Config loading, agent resolution, viper bindings
  executor/     # Task execution: single/parallel/worktree/skill injection
  logger/       # Structured logging
  parser/       # JSON stream parser
  utils/        # Utilities
  worktree/     # Git worktree management
```

Key features:
- **Multi-backend support** - Unified interface for different AI CLIs
- **Parallel execution** - Dependency-aware concurrent task execution
- **Git worktree isolation** - Execute tasks in isolated branches
- **Skill auto-injection** - Detects tech stack and injects relevant specs
- **Agent presets** - Configurable via `~/.codeagent/models.json`

### Workflow Modules

| Module | Type | Description |
|--------|------|-------------|
| `do` | Skill | 5-phase feature development (Understand→Clarify→Design→Implement→Complete) |
| `omo` | Skill | Multi-agent orchestration with intelligent routing (Oracle, Librarian, etc.) |
| `sparv` | Skill | SPARV workflow (Specify→Plan→Act→Review→Vault) with 10-point gate |
| `bmad` | Agent | BMAD agile workflow with 6 specialized agents |
| `requirements` | Agent | Lightweight requirements-to-code pipeline |
| `essentials` | Agent | 11 core dev commands (/ask, /code, /debug, /test, etc.) |
| `harness` | Skill | Multi-session autonomous agent with checkpointing and recovery |
| `claudekit` | Composite | do skill + global hooks (pre-bash, inject-spec, log-prompt) |
| `course` | Composite | Course development (dev + product-requirements + test-cases) |

### Installation Directory Structure

After installation, `~/.claude/` contains:

```
~/.claude/
├── bin/codeagent-wrapper       # Go binary
├── CLAUDE.md                   # This file
├── commands/                   # Slash commands (from essentials/bmad/requirements)
├── agents/                     # Agent prompts
├── skills/                     # Skill definitions (do/omo/sparv/etc.)
├── hooks/                      # Global hooks (from claudekit)
├── settings.json               # Auto-generated hooks config
└── installed_modules.json      # Tracks installed modules
```

## Key Workflows

### /do Workflow (5-Phase)

The `/do` skill orchestrates feature development through 5 mandatory phases:

1. **Understand** - Gather requirements via AskUserQuestion + code-explorer
2. **Clarify** - MANDATORY question resolution before proceeding
3. **Design** - code-architect proposes approaches
4. **Implement** - Requires approval, then develop agent executes
5. **Complete** - code-reviewer finalizes and documents

**Hard constraints:**
- Never write code directly - delegate to codeagent-wrapper agents
- Phase 2 is mandatory - must answer questions before proceeding
- Phase 4 requires approval - stop after Phase 3 if not approved
- Pass complete Context Pack forward to every agent
- Use `--parallel` for independent tasks
- Update `.claude/do-tasks/{task_id}/task.md` after each phase

**Context Pack template:**
```
## Original User Request
<verbatim request>

## Context Pack
- Phase: <1-5 name>
- Decisions: <requirements/constraints/choices>
- Code-explorer output: <paste or "None">
- Code-architect output: <paste or "None">
- Code-reviewer output: <paste or "None">
- Develop output: <paste or "None">
- Open questions: <list or "None">

## Current Task
<specific task>

## Acceptance Criteria
<checkable outputs>
```

### Parallel Execution Pattern

Use `codeagent-wrapper --parallel` for concurrent tasks:

```bash
codeagent-wrapper --parallel <<'EOF'
---TASK---
id: task1
agent: code-explorer
workdir: .
---CONTENT---
Find similar features in the codebase.

---TASK---
id: task2
agent: code-architect
dependencies: task1
---CONTENT---
Design architecture based on task1 findings.
EOF
```

### Agent Configuration

Configure agents in `~/.codeagent/models.json`:

```json
{
  "default_backend": "codex",
  "default_model": "gpt-4.1",
  "backends": {
    "codex": { "api_key": "..." },
    "claude": { "base_url": "http://localhost:23001", "api_key": "..." }
  },
  "agents": {
    "develop": {
      "backend": "codex",
      "model": "gpt-4.1",
      "reasoning": "high",
      "yolo": true
    },
    "code-explorer": {
      "backend": "opencode",
      "model": "opencode/grok-code"
    }
  }
}
```

## Development Guidelines

### When Working on codeagent-wrapper

- Entry point: `cmd/codeagent-wrapper/main.go`
- Add new backends in `internal/backend/`
- Execution logic in `internal/executor/`
- Use structured logging via `internal/logger/`
- Test with Go 1.21+ (CI tests 1.21 and 1.22)

### When Working on Skills

- Skills live in `skills/{name}/SKILL.md`
- Use hooks for lifecycle management (Stop, SessionStart, etc.)
- Skills can include `scripts/` and `references/` subdirectories
- Skill specs are auto-injected based on tech stack detection

### When Working on Agents

- Agent prompts in `agents/{module}/agents/{name}.md`
- Commands in `agents/{module}/commands/{name}.md`
- Use `merge_dir` operation to preserve user customizations

### When Modifying config.json

- Validate against `config.schema.json`
- Test with `python install.py --status`
- Modules requiring codeagent-wrapper: `do`, `omo`
- Use `agents` section to define backend/model mappings

## Backend Requirements

Each backend requires specific CLI features:

| Backend | Required CLI | Key Flags |
|---------|-------------|-----------|
| Codex | `codex` | `e`, `--json`, `-C`, `resume` |
| Claude | `claude` | `--output-format stream-json`, `-r` |
| Gemini | `gemini` | `-o stream-json`, `-y`, `-r` |
| OpenCode | `opencode` | stdin mode, `--format json` |

## Environment Variables

### codeagent-wrapper

- `CODEAGENT_BACKEND` - Backend selection (codex/claude/gemini/opencode)
- `CODEAGENT_SKIP_PERMISSIONS` - Skip permission prompts (default: true)
- `CODEAGENT_TMPDIR` - Custom temp directory (for macOS permission issues)
- `CODEX_TIMEOUT` - Timeout in ms (default: 7200000 = 2 hours)
- `CODEX_BYPASS_SANDBOX` - Bypass sandbox (default: true)
- `DO_WORKTREE_DIR` - Reuse existing worktree directory

### Backend-specific

- `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY` - Claude backend
- `GEMINI_API_KEY` - Gemini backend (loaded from `~/.gemini/.env`)

## Troubleshooting

### Common Issues

**"codeagent-wrapper not found"**
```bash
npx github:weihuacodeing11/myclaude
# Select: codeagent-wrapper
```

**Module not loading**
```bash
cat ~/.claude/installed_modules.json
python install.py --force --module <name>
```

**Backend CLI errors**
```bash
which codex && codex --version
which claude && claude --version
which gemini && gemini --version
which opencode && opencode --version
```

**macOS permission denied (temp directories)**
```bash
export CODEAGENT_TMPDIR=$HOME/.codeagent/tmp
```

**Codex approval prompts**
Set `approval_policy = "never"` in `~/.codex/config.yaml`

**"Unknown event format" in logs**
Logging display issue, can be ignored

## Testing

### codeagent-wrapper Tests

```bash
cd codeagent-wrapper
make test                    # Run all tests
go test ./internal/app/...   # Test specific package
go test -v -run TestName     # Run specific test
```

### Integration Testing

```bash
# Test BMAD workflow
make test-bmad

# Test Requirements workflow
make test-requirements
```

## License

AGPL-3.0 - For commercial use without AGPL obligations, contact: support@stellarlink.co
