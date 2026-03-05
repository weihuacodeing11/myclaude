---
name: do
description: Enhanced structured feature development with 7-phase workflow (Understand, Clarify, Optimize, Design, Review, Implement, Complete). Integrates requirements clarification, best practices, database design, backend architecture, frontend design, and test-driven development.
allowed-tools: ["Bash(python3:*/.claude/skills/do/scripts/setup-do.py*)", "Bash(python3:*/.claude/skills/do/scripts/task.py*)"]
---

# do - Enhanced Feature Development Orchestrator

An orchestrator for systematic feature development with professional domain expertise. Invoke agents via `codeagent-wrapper`, never write code directly.

## Loop Initialization (REQUIRED)

When triggered via `/do <task>`, initialize the task directory immediately:

```bash
python3 "$HOME/.claude/skills/do/scripts/setup-do.py" "<task description>"
```

This creates a task directory under `.claude/do-tasks/` with:
- `task.md`: Single file containing YAML frontmatter (metadata) + Markdown body (requirements/context)

**Worktree decision is deferred until Phase 6 (Implement).**

## Task Directory Management

Use `task.py` to manage task state:

```bash
# Update phase
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase <N>

# Check status
python3 "$HOME/.claude/skills/do/scripts/task.py" status

# List all tasks
python3 "$HOME/.claude/skills/do/scripts/task.py" list
```

## Hard Constraints

1. **Never write code directly.** Delegate all code changes to `codeagent-wrapper` agents.
2. **Parallel-first.** Run independent tasks via `codeagent-wrapper --parallel`.
3. **Update phase after each phase.** Use `task.py update-phase <N>`.
4. **Expect long-running calls.** High-reasoning modes can take time.
5. **Defer worktree until Phase 6.** Only ask about worktree mode right before implementation.

## 7-Phase Workflow

### Phase 1: Requirements Analysis (Interactive PRD Generation)

**Goal:** Transform user requirements into professional PRD through interactive dialogue and quality scoring.

**Actions:** Use the `/product-requirements` skill to generate comprehensive PRD.

```bash
# Call the product-requirements skill
/product-requirements

# Provide context:
# - Original user request: <USER_REQUEST>
```

The skill will:
1. Gather project context (README, package.json, tech stack)
2. Assess requirements quality (100-point scoring system):
   - Business Value & Goals (30 pts)
   - Functional Requirements (25 pts)
   - User Experience (20 pts)
   - Technical Constraints (15 pts)
   - Scope & Priorities (10 pts)
3. Iteratively clarify requirements until 90+ quality score
4. Generate professional PRD at `docs/{feature-name}-prd.md`

**Expected Output:**
- PRD document with:
  - Executive summary
  - Problem statement and success metrics
  - User personas and stories
  - Functional requirements
  - Technical constraints
  - MVP scope and phasing
  - Risk assessment

**After PRD generation, explore codebase:**

```bash
codeagent-wrapper --parallel <<'EOF'
---TASK---
id: p1_similar_features
agent: code-explorer
workdir: .
---CONTENT---
Find similar features in the codebase. Trace end-to-end flow.

PRD: <PHASE1_PRD_OUTPUT>

Output:
- Similar implementations (file paths)
- Patterns used
- Reusable components

---TASK---
id: p1_architecture
agent: code-explorer
workdir: .
---CONTENT---
Map the architecture of relevant subsystems.

PRD: <PHASE1_PRD_OUTPUT>

Output:
- Key files and their roles
- Data flow
- Dependencies

---TASK---
id: p1_conventions
agent: code-explorer
workdir: .
---CONTENT---
Identify testing patterns, conventions, and configurations.

PRD: <PHASE1_PRD_OUTPUT>

Output:
- Test framework and patterns
- Code style conventions
- Build/deploy configurations
EOF
```

**After completion:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 2
```

### Phase 2: Technical Clarification (Optional)

**Goal:** Clarify technical stack and implementation details if needed.

**Note:** `/product-requirements` in Phase 1 already handles business requirements clarification. This phase focuses on technical choices.

**Actions:** Use the `/ask-questions-if-underspecified` skill if technical details are unclear.

```bash
# Call the ask-questions-if-underspecified skill
/ask-questions-if-underspecified

# Provide context:
# - PRD from Phase 1: <PHASE1_PRD_OUTPUT>
# - Codebase exploration: <PHASE1_CODEBASE_OUTPUT>
```

The skill will:
- Analyze technical completeness
- Generate structured multiple-choice questions for:
  - Backend technology choices
  - Frontend framework selection
  - Database selection
  - Authentication method
  - Deployment strategy
- Provide reasonable defaults
- Support fast-path responses (e.g., "defaults")

**Skip this phase if:**
- PRD already specifies all technical choices
- Tech stack is clear from existing codebase
- User provided detailed technical requirements

**After user responds (or if skipped):**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 3
```

### Phase 3: Optimize Prompt (Use best-practices Skill)

**Goal:** Transform requirements into optimized, detailed specifications.

**Actions:** Use the `/best-practices` skill directly.

```bash
# Call the best-practices skill with clarified requirements
/best-practices

# Provide:
# - Original request: <USER_REQUEST>
# - Clarified requirements: <PHASE2_OUTPUT>
# - Context from Phase 1: <PHASE1_OUTPUT>
```

The skill will:
1. Analyze task intent (task type, gaps, edge cases)
2. Find relevant patterns from references
3. Explore codebase for context
4. Apply 5 transformation principles:
   - Add verification (test cases, success criteria)
   - Provide specific context (file paths, patterns)
   - Add constraints (tech stack, performance, security)
   - Structure in phases
   - Include rich content (examples, error handling)
5. Output optimized requirements document

**After completion:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 4
```

### Phase 4: Design Architecture (Enhanced with Domain Experts)

**Goal:** Design database, backend, and frontend architecture using specialized agents.

**4.1 Database Design (if needed)**

Use the `/database-design` skill directly:

```bash
# Call the database-design skill with optimized requirements
# The skill will handle the complete database design workflow
/database-design <PHASE3_OUTPUT>
```

The skill will output:
- SQL schema definitions
- Index creation statements
- Migration scripts
- ER diagram (text description)

**4.2 Backend Design (if needed)**

Use the `/backend-development` skill directly:

```bash
# Call the backend-development skill with requirements and database design
# The skill will handle the complete backend architecture design
/backend-development <PHASE3_OUTPUT> <PHASE4_1_OUTPUT>
```

The skill will output:
- API specification (OpenAPI)
- Authentication flow diagram
- Data access layer design
- Caching strategy document

**4.3 Frontend Design (if needed)**

Use the `/frontend-design` skill directly:

```bash
# Call the frontend-design skill with requirements and backend API
# The skill will handle the complete frontend design workflow
/frontend-design <PHASE3_OUTPUT> <PHASE4_2_OUTPUT>
```

The skill will output:
- Design concept statement
- High-fidelity UI design (can use any language/framework for visualization)
- Component structure diagram
- Style guide (colors, fonts, spacing)
- Interaction flow diagram

**4.4 User Confirmation for Frontend Design (CRITICAL STEP)**

**Present design to user:**

Use AskUserQuestion:
```
Frontend design is complete. Please review the design.

Design output:
- Design concept and style
- High-fidelity UI design (may include code or visualization)
- Component structure and style guide

Please confirm:
1) Design is satisfactory, proceed to next phase
2) Needs modification, please provide specific feedback

If modification needed, please specify:
- Which parts need adjustment? (layout, colors, fonts, animations, etc.)
- What is the expected result?
- Any reference examples or specific requirements?
```

**If user requests modifications, loop:**

```bash
# Call the frontend-design skill again with user feedback
/frontend-design --feedback "<USER_FEEDBACK>" <PHASE4_3_OUTPUT>
```

The skill will:
1. Analyze user feedback
2. Adjust design based on feedback
3. Re-implement high-fidelity design
4. Output updated design with modification explanation

**Repeat until user confirms satisfaction.**

**After user confirms:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 5
```

### Phase 5: Review Design (New - Design Consistency Check)

**Goal:** Review all design documents for consistency and completeness.

```bash
codeagent-wrapper --agent design-reviewer - . <<'EOF'
## All Design Documents
- Database Design: <PHASE4_1_OUTPUT>
- Backend Design: <PHASE4_2_OUTPUT>
- Frontend Design: <PHASE4_3_OUTPUT>

## Task
Review design consistency and completeness:

1. Database and Backend Consistency
   - Do APIs match database schema?
   - Do indexes support query needs?

2. Backend and Frontend Consistency
   - Is API contract clear?
   - Is error handling unified?

3. Security Check
   - Is authentication/authorization complete?
   - Is input validation sufficient?
   - Is sensitive data protected?

4. Performance Considerations
   - Database query optimization
   - API response time
   - Frontend loading performance

5. Maintainability
   - Is code organization clear?
   - Does it follow best practices?
   - Is it easy to test?

## Output
- Design review report
- Areas needing adjustment
- Risks and recommendations
EOF
```

**After completion:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 6
```

### Phase 6: Implement (Enhanced with Test-Driven Development)

**Goal:** Implement based on design documents with test-driven approach.

**Ask about worktree:**

Use AskUserQuestion:
```
Ready to implement. Do you want to develop in an isolated worktree?

Options:
1) Yes - Create isolated worktree (recommended for large changes)
2) No - Develop in main branch

Worktree benefits:
- Isolated development environment
- Easy to discard if needed
- No impact on main branch until merge
```

**If yes, create worktree:**
```bash
python3 "$HOME/.claude/skills/do/scripts/setup-do.py" --worktree "<task description>"
# Save the worktree path from output
```

**6.0 Generate Test Cases (New)**

Use the `/test-cases` skill directly:

```bash
# Call the test-cases skill with all design documents
# The skill will handle the complete test case generation workflow
/test-cases <PHASE3_OUTPUT> <PHASE4_1_OUTPUT> <PHASE4_2_OUTPUT> <PHASE4_3_OUTPUT>
```

The skill will:
1. Collect requirements
2. Extract test scenarios (functional/boundary/error/state transition)
3. Generate structured test cases with unique IDs
4. Validate coverage
5. Output to tests/<name>-test-cases.md

Expected output:
- Test cases document with TC-F/TC-E/TC-ERR/TC-ST categories
- Coverage matrix
- Summary of test cases generated

**6.1 Database Migration (if database design exists)**

```bash
DO_WORKTREE_DIR=<WORKTREE_DIR> \
codeagent-wrapper --agent develop - . <<'EOF'
## Task
Implement database migration

## Database Design
<PHASE4_1_OUTPUT>

## Test Cases
<PHASE6_0_OUTPUT> (database-related test cases)

## Requirements
- Create migration files
- Implement up/down scripts
- Add seed data (if needed)
- Test migration
- Verify data integrity constraints

## Acceptance Criteria
- Migration executes successfully
- Can rollback
- Data integrity constraints are correct
- Pass related test cases
EOF
```

**6.2 Backend Implementation (if backend design exists)**

```bash
DO_WORKTREE_DIR=<WORKTREE_DIR> \
codeagent-wrapper --agent develop - . <<'EOF'
## Task
Implement backend API

## Backend Design
<PHASE4_2_OUTPUT>

## Database Schema
<PHASE4_1_OUTPUT>

## Test Cases
<PHASE6_0_OUTPUT> (backend API test cases)

## Requirements
- Implement all API endpoints
- Implement authentication/authorization
- Implement data access layer
- Implement caching (if needed)
- Add logging and monitoring
- Write unit tests and integration tests (reference test cases)

## Acceptance Criteria
- All API endpoints work correctly
- Test coverage > 80%
- Authentication/authorization correct
- Error handling complete
- Pass all functional test cases (TC-F-XXX)
- Pass all boundary test cases (TC-E-XXX)
- Pass all error handling test cases (TC-ERR-XXX)
EOF
```

**6.3 Frontend Implementation (if frontend design exists)**

```bash
DO_WORKTREE_DIR=<WORKTREE_DIR> \
codeagent-wrapper --agent develop - . <<'EOF'
## Task
Implement frontend interface

## Frontend Design
<PHASE4_3_OUTPUT>

## Backend API
<PHASE4_2_OUTPUT>

## Test Cases
<PHASE6_0_OUTPUT> (frontend interaction test cases)

## Requirements
- Implement all components
- Implement state management
- Implement API calls
- Implement error handling
- Implement loading states
- Follow design guide (colors, fonts, animations)
- Write component tests (reference test cases)

## Acceptance Criteria
- All features work correctly
- UI matches design guide
- Responsive design
- Accessibility (WCAG AA)
- Test coverage for key interactions
- Pass all frontend test cases
- Pass state transition test cases (TC-ST-XXX)
EOF
```

**6.4 Execute Test Validation (New)**

```bash
DO_WORKTREE_DIR=<WORKTREE_DIR> \
codeagent-wrapper --agent test-executor - . <<'EOF'
## Task
Execute test case validation

## Test Cases Document
<PHASE6_0_OUTPUT>

## Implementation Results
- Database: <PHASE6_1_OUTPUT>
- Backend: <PHASE6_2_OUTPUT>
- Frontend: <PHASE6_3_OUTPUT>

## Requirements
1. Execute all automated tests
   - Unit tests
   - Integration tests
   - End-to-end tests

2. Manually verify key test cases
   - Core user flows
   - Boundary conditions
   - Error handling

3. Generate test report
   - Passed test cases
   - Failed test cases
   - Coverage statistics

## Output Format
Test report (tests/<name>-test-report.md):
- Test execution summary
- Pass rate statistics
- Failed case details
- Coverage analysis
- Remaining issues

## Acceptance Criteria
- All high-priority test cases pass
- Test coverage > 80%
- Key user flows verified
- Error handling correct
EOF
```

**After completion:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" update-phase 7
```

### Phase 7: Complete (Code Review and Summary)

**Goal:** Final code review and summary.

```bash
codeagent-wrapper --agent code-reviewer - . <<'EOF'
## Implementation Results
- Database: <PHASE6_1_OUTPUT>
- Backend: <PHASE6_2_OUTPUT>
- Frontend: <PHASE6_3_OUTPUT>
- Test Report: <PHASE6_4_OUTPUT>

## Task
Comprehensive review of implementation:
- Code quality
- Test coverage
- Performance
- Security
- Maintainability

## Output
- Review report
- Improvement suggestions
- Deployment checklist
EOF
```

**Mark task complete:**
```bash
python3 "$HOME/.claude/skills/do/scripts/task.py" complete
```

**Output `<promise>DO_COMPLETE</promise>` to signal completion.**

## Agents and Skills Reference

| Agent/Skill | Purpose | Phase | Type |
|-------------|---------|-------|------|
| `/product-requirements` | Generate PRD with quality scoring | 1 | Skill |
| `code-explorer` | Trace code, map architecture | 1 | Agent |
| `/ask-questions-if-underspecified` | Clarify technical choices (optional) | 2 | Skill |
| `/best-practices` | Transform prompts with 5 principles | 3 | Skill |
| `/database-design` | Design database schema and migrations | 4 | Skill |
| `/backend-development` | Design backend API and architecture | 4 | Skill |
| `/frontend-design` | Design frontend UI and components | 4 | Skill |
| `design-reviewer` | Review design consistency | 5 | Agent |
| `/test-cases` | Generate structured test cases | 6 | Skill |
| `develop` | Implement code and run tests | 6 | Agent |
| `test-executor` | Execute tests and generate report | 6 | Agent |
| `code-reviewer` | Final code review | 7 | Agent |

## Conditional Execution

Not all phases require all agents/skills. Skip based on task type:

- **Pure frontend task**: Skip `/database-design`, `/backend-development`
- **Pure backend task**: Skip `/frontend-design`
- **No database changes**: Skip `/database-design`
- **Bug fix**: May skip Phase 4 entirely if design is clear

## Best Practices

1. **Always update phase** after completing each phase
2. **Use parallel execution** when tasks are independent
3. **Pass complete context** between phases
4. **User confirmation** is mandatory for frontend design
5. **Test-driven** approach in Phase 6
6. **Defer worktree** decision until Phase 6

## Anti-Patterns

- ❌ Don't write code directly
- ❌ Don't skip phase updates
- ❌ Don't run sequential tasks in parallel
- ❌ Don't forget user confirmation for frontend design
- ❌ Don't skip test case generation
- ❌ Don't proceed with failed tests

## Example Usage

```
User: /do implement a blog system with articles, comments, and user authentication

Phase 1: Requirements Analysis
- Call /product-requirements skill
- Interactive dialogue with quality scoring
- Generate PRD at docs/blog-system-prd.md (Score: 92/100)
- Explore codebase for similar features
- Map architecture and conventions

Phase 2: Technical Clarification (Optional)
- Skip if tech stack clear from PRD
- Or ask about: Backend (Python/Node.js/Go?)
- Database (PostgreSQL/MySQL/MongoDB?)
- Frontend (React/Vue/小程序?)
- Authentication (JWT/Session/OAuth?)

Phase 3: Optimize
- Call /best-practices skill
- Apply 5 transformation principles
- Generate optimized requirements

Phase 4: Design
- Design database: users, posts, comments tables
- Design backend: RESTful API, JWT auth
- Design frontend: blog UI with unique style
- User confirms frontend design ✓

Phase 5: Review
- Check database-backend consistency
- Check backend-frontend consistency
- Security review
- Performance review

Phase 6: Implement
- Generate test cases (45 test cases)
- Implement database migration
- Implement backend API (with tests)
- Implement frontend UI (with tests)
- Execute tests (42/45 passed)

Phase 7: Complete
- Code review
- Improvement suggestions
- Deployment checklist
- <promise>DO_COMPLETE</promise>
```
