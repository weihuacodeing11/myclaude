# /do - Streamlined Full-Stack Development Workflow

> From a simple idea to a production-ready app - fully automated, end-to-end

## 🚀 Core Capabilities

**One-line description**: Give me a requirement, I'll build you a complete app, mini-program, or website.

**Technical depth**:
- 🎯 **7 Development Phases** - Complete coverage
- 📊 **7 Specialized Skills** - Integrated workflow
- 🔧 **Zero Dependencies** - Uses current Claude model
- 📝 **4 Test Categories** - Auto-generated test cases
- 🎨 **High-Fidelity UI Design** - User approval mechanism
- 📋 **Professional PRD** - 100-point quality scoring

## 📈 Workflow Overview

```
User Input
    ↓
Phase 1: Requirements Analysis
    ├─ /product-requirements skill (PRD generation)
    │   ├─ 100-point quality scoring
    │   ├─ Interactive requirement gathering
    │   └─ Generate PRD document
    ├─ Explore codebase (parallel)
    └─ Output: PRD + codebase analysis
    ↓
Phase 2: Technical Clarification (Optional)
    ├─ /ask-questions-if-underspecified skill
    └─ Output: Tech stack confirmation
    ↓
Phase 3: Optimize
    ├─ /best-practices skill (5 transformation principles)
    └─ Output: Detailed executable requirements
    ↓
Phase 4: Design
    ├─ /database-design skill
    │   ├─ Normalization (1NF/2NF/3NF)
    │   ├─ Index optimization
    │   └─ Zero-downtime migration
    ├─ /backend-development skill
    │   ├─ RESTful API design
    │   ├─ JWT/OAuth2 authentication
    │   ├─ Caching strategy
    │   └─ Observability design
    ├─ /frontend-design skill
    │   ├─ High-fidelity UI design
    │   ├─ Component architecture
    │   ├─ Style guide
    │   └─ Interaction flows
    └─ User approval required ✓
    ↓
Phase 5: Review
    ├─ Design consistency check
    ├─ Security review
    └─ Performance review
    ↓
Phase 6: Implement
    ├─ /test-cases skill (generate test cases)
    ├─ Implement database migration
    ├─ Implement backend API
    ├─ Implement frontend UI
    └─ Execute tests
    ↓
Phase 7: Complete
    ├─ Code review
    ├─ Improvement suggestions
    └─ Deployment checklist
```

## 🎯 Usage

```bash
/do "build a todo app with user authentication"
```

That's it! The workflow handles everything from requirements to deployment.

## 📦 What Gets Built

### Database Layer
- Normalized schema design
- Optimized indexes
- Migration scripts
- Seed data

### Backend Layer
- RESTful API endpoints
- Authentication/Authorization
- Data access layer
- Caching strategy
- Error handling
- Logging and monitoring

### Frontend Layer
- Component architecture
- State management
- API integration
- Responsive design
- Accessibility (WCAG AA)
- Loading states and error handling

### Testing
- Unit tests
- Integration tests
- End-to-end tests
- Test coverage > 80%

## 🔧 Technical Features

- **Design-First**: Get approval before implementation
- **Test-Driven**: Generate test cases before coding
- **Best Practices**: Apply industry standards automatically
- **Security-Focused**: Built-in security checks
- **Performance-Optimized**: Caching and query optimization
- **Production-Ready**: Deployment checklist included

## 📝 Example Outputs

### PRD Document
- Executive summary
- Problem statement and success metrics
- User personas and stories
- Functional requirements
- Technical constraints
- MVP scope and phasing
- Risk assessment

### Design Documents
- Database schema with ER diagrams
- API specification (OpenAPI)
- UI design with style guide
- Component structure
- Interaction flows

### Implementation
- Complete source code
- Test suites
- Migration scripts
- Deployment instructions

## 🚀 Advanced Usage

### With Worktree Isolation
```bash
/do "add payment integration to the existing app"
# Choose "Yes" when asked about worktree
```

### Skip Optional Phases
The workflow automatically skips phases that aren't needed:
- Pure frontend task → Skip database/backend design
- Pure backend task → Skip frontend design
- Bug fix → May skip design phase entirely

## 📚 Learn More

See [SKILL.md](SKILL.md) for detailed workflow documentation.
