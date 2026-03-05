# /do Skill Architecture

## Agents vs Skills

### Agent
- **Definition**: A `.md` file containing prompts
- **Invocation**: `codeagent-wrapper --agent <agent-name>`
- **Purpose**: Execute single, focused tasks
- **Input**: Receives text input
- **Output**: Returns text output
- **Location**: `skills/do/agents/*.md`
- **Cannot**: Call other skills or agents, execute code

### Skill
- **Definition**: A complete workflow with its own `SKILL.md`
- **Invocation**: `/skill-name` or `Skill` tool
- **Purpose**: Orchestrate multiple agents or other skills to complete complex tasks
- **Capabilities**: Can call agents, use tools, interact with users
- **Location**: `skills/*/SKILL.md`

## /do Skill Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      /do Skill (Top Level)                   │
│                   (skills/do/SKILL.md)                       │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Orchestrates
                            ↓
        ┌───────────────────┴───────────────────┐
        │                                       │
        ↓                                       ↓
┌───────────────────┐                  ┌──────────────────┐
│   Internal Agents │                  │  External Skills │
│  (do/agents/)     │                  │  (other skills)  │
└───────────────────┘                  └──────────────────┘
        │                                       │
        ├─ code-explorer                        ├─ /product-requirements
        ├─ design-reviewer                      ├─ /ask-questions-if-underspecified
        ├─ test-executor                        ├─ /best-practices
        ├─ code-reviewer                        ├─ /database-design
        └─ develop                              ├─ /backend-development
                                                ├─ /frontend-design
                                                └─ /test-cases
```

## How They Work Together

### Method 1: /do Calls Internal Agents

**Example: Phase 1 - Codebase Exploration**

```bash
# /do skill calls code-explorer agent
codeagent-wrapper --agent code-explorer - . <<'EOF'
## Task
Find similar features in the codebase. Trace end-to-end flow.

PRD: <PHASE1_PRD_OUTPUT>
EOF
```

**Flow**:
1. `/do` skill reaches Phase 1
2. Calls `code-explorer` agent
3. Agent reads prompts from `agents/code-explorer.md`
4. Agent explores codebase and returns findings
5. Returns results to `/do` skill

**Agent's Role**:
- `code-explorer` is a simple agent that explores code
- It doesn't call other skills
- It's a lightweight tool for /do's internal use

### Method 2: /do Calls External Skills

**Example: Phase 1 - Requirements Analysis**

```bash
# /do skill calls /product-requirements skill
/product-requirements

# Provide context:
# - Original user request: <USER_REQUEST>
```

**Flow**:
1. `/do` skill reaches Phase 1
2. Calls `/product-requirements` skill
3. `/product-requirements` skill has its own workflow:
   - Gathers project context
   - Assesses requirements quality (100-point scoring)
   - Iteratively clarifies requirements
   - Generates professional PRD
4. Returns PRD document to `/do` skill
5. `/do` skill continues to next phase

**Skill's Role**:
- `/product-requirements` is a complete skill with its own SKILL.md
- It has its own workflow, agents, and tools
- `/do` just calls it and receives the output

**Example: Phase 4 - Design**

```bash
# /do skill calls design skills directly
/database-design <PHASE3_OUTPUT>
/backend-development <PHASE3_OUTPUT>
/frontend-design <PHASE3_OUTPUT>
```

**Flow**:
1. `/do` skill reaches Phase 4
2. Calls `/database-design`, `/backend-development`, `/frontend-design` skills
3. Each skill executes its own workflow
4. Returns design documents to `/do` skill
5. `/do` skill continues to Phase 5 (design review)

## Why Create Internal Agents?

### 1. code-explorer Agent

**Why not use a skill?**
- No corresponding `/code-explorer` skill exists
- This is a simple task: explore codebase and find patterns
- Doesn't need complex workflow or user interaction

### 2. design-reviewer Agent

**Why not use a skill?**
- No corresponding `/design-review` skill exists
- This is a /do-specific task: review consistency across database, backend, and frontend designs
- Doesn't need user interaction, just returns a review report

### 3. test-executor Agent

**Why not use a skill?**
- No corresponding `/test-executor` skill exists
- This is a /do-specific task: execute tests and generate reports
- Doesn't need user interaction

### 4. code-reviewer Agent

**Why not use a skill?**
- No corresponding `/code-review` skill exists
- This is a /do-specific task: final code review for quality, security, and performance
- Doesn't need user interaction

### 5. develop Agent

**Why not use a skill?**
- This is a general code implementation agent, not a domain-specific skill
- Used in Phase 6 to implement code according to design documents

## Design Philosophy

### When to Use Skills?

**Conditions**:
1. A mature skill already exists
2. The skill's workflow fully meets the need
3. The skill's user interaction is acceptable

**Examples**:
- `/product-requirements` - Complete PRD generation workflow with quality scoring
- `/database-design` - Complete database design workflow
- `/backend-development` - Complete backend architecture workflow
- `/frontend-design` - Complete frontend design workflow (includes user confirmation)
- `/test-cases` - Complete test case generation workflow

### When to Use Agents?

**Conditions**:
1. No corresponding skill exists
2. Need precise control over input/output
3. No user interaction needed
4. It's an "internal step" of /do workflow

**Examples**:
- `design-reviewer` - /do-specific design review step
- `test-executor` - /do-specific test execution step
- `code-explorer` - /do-specific codebase exploration step

## Complete Call Chain Example

### Phase 1: Requirements Analysis

```
/do skill (SKILL.md)
    │
    ├─ Call /product-requirements skill
    │   │
    │   └─ /product-requirements skill (skills/product-requirements/SKILL.md)
    │       ├─ Gather project context
    │       ├─ Assess requirements quality (100-point scoring)
    │       ├─ Iteratively clarify requirements
    │       └─ Generate PRD at docs/{feature-name}-prd.md
    │
    └─ Call code-explorer agents (3 in parallel)
        └─ Read agents/code-explorer.md
        └─ Explore codebase
        └─ Return: similar features, architecture patterns
```

### Phase 2: Technical Clarification (Optional)

```
/do skill (SKILL.md)
    │
    └─ Call /ask-questions-if-underspecified skill
        │
        └─ /ask-questions-if-underspecified skill
            ├─ Check if technical choices are clear
            ├─ Generate structured questions if needed
            └─ Return: clarified technical stack
```

### Phase 3: Optimize Prompt

```
/do skill (SKILL.md)
    │
    └─ Call /best-practices skill
        │
        └─ /best-practices skill
            ├─ Analyze task intent
            ├─ Apply 5 transformation principles
            └─ Return: optimized requirements document
```

### Phase 4: Design

```
/do skill (SKILL.md)
    │
    ├─ Call /database-design skill
    │   └─ Return: database schema, indexes, migrations
    │
    ├─ Call /backend-development skill
    │   └─ Return: API specification, auth flow, data access layer
    │
    └─ Call /frontend-design skill
        ├─ Return: design concept, high-fidelity UI, component structure
        └─ User confirmation loop (built into the skill)
```

### Phase 5: Review Design

```
/do skill (SKILL.md)
    │
    └─ Call design-reviewer agent
        └─ Read agents/design-reviewer.md
        └─ Review all design documents
        └─ Return: design review report
```

### Phase 6: Implement

```
/do skill (SKILL.md)
    │
    ├─ 6.0: Call /test-cases skill
    │   └─ Return: structured test cases document
    │
    ├─ 6.1: Call develop agent (database)
    │   └─ Implement database migrations
    │
    ├─ 6.2: Call develop agent (backend)
    │   └─ Implement backend API
    │
    ├─ 6.3: Call develop agent (frontend)
    │   └─ Implement frontend UI
    │
    └─ 6.4: Call test-executor agent
        └─ Execute tests and generate report
```

### Phase 7: Complete

```
/do skill (SKILL.md)
    │
    └─ Call code-reviewer agent
        └─ Read agents/code-reviewer.md
        └─ Review implementation
        └─ Return: code review report, deployment checklist
```

## Summary

### Role of Agents
1. **Execute single tasks**: Each agent focuses on a specific task
2. **Reusable**: Multiple skills can call the same agent
3. **Lightweight**: Just a prompt file, no complex logic
4. **Fast**: Direct execution, no extra interaction

### Role of Skills
1. **Orchestrate workflows**: Organize multiple agents and tools
2. **User interaction**: Can ask users, show progress
3. **Complex logic**: Can have conditionals, loops, error handling
4. **Independent and complete**: Can be used standalone or called by other skills

### /do Skill Design Philosophy
1. **Reuse existing skills**: Directly call `/product-requirements`, `/database-design`, `/frontend-design`, etc.
2. **Fill gaps**: Create new agents for tasks without corresponding skills (e.g., `design-reviewer`)
3. **Flexible orchestration**: Selectively call agents/skills based on task type

### Why Not Use All Skills?
- Skills have their own interaction flows, less flexible
- Agents are more lightweight, allow precise control of input/output
- Mixed approach balances flexibility and reusability

### Why Not Use All Agents?
- Some domains already have mature skills (e.g., `/database-design`)
- Recreating agents would duplicate work
- Directly calling skills leverages their complete workflows and best practices

## Final Architecture

- **5 Internal Agents**: code-explorer, design-reviewer, test-executor, code-reviewer, develop
- **7 External Skills**: /product-requirements, /ask-questions-if-underspecified, /best-practices, /database-design, /backend-development, /frontend-design, /test-cases
- **7 Phases**: Requirements Analysis → Technical Clarification → Optimize → Design → Review → Implement → Complete

This design fully leverages existing professional skills while maintaining /do workflow's flexibility and control.
