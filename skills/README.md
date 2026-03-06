# Skills

This directory contains specialized skills that power the `/do` workflow.

## Core Skills

| Skill | Purpose |
|-------|---------|
| `do` | Main 7-phase workflow orchestrator |
| `product-requirements` | Interactive PRD generation with quality scoring |
| `ask-questions-if-underspecified` | Clarify technical choices |
| `best-practices` | Optimize requirements with 5 transformation principles |
| `database-design` | Design database schema and migrations |
| `backend-development` | Design backend API and architecture |
| `frontend-design` | Design frontend UI and components |
| `test-cases` | Generate structured test cases |

## Installation

All skills are installed together with the `/do` workflow:

```bash
npx github:weihuacodeing11/myclaude
```

## Usage

Skills are automatically invoked by the `/do` workflow. You don't need to call them individually.

```bash
/do "your task description"
```

The workflow will:
1. Use `/product-requirements` to generate PRD
2. Use `/ask-questions-if-underspecified` if clarification needed
3. Use `/best-practices` to optimize requirements
4. Use `/database-design`, `/backend-development`, `/frontend-design` for architecture
5. Use `/test-cases` to generate test cases
6. Implement everything using current Claude model

## Skill Structure

Each skill lives in its own directory with:
- `SKILL.md` - Skill definition and instructions
- `references/` (optional) - Supporting documentation

## Learn More

See the main [README](../README.md) for complete documentation.
