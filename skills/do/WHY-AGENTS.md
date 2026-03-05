# 为什么 /do 需要自己的 Agents？

## 核心问题

既然 /do skill 可以直接调用其他 skills（如 `/database-design`, `/frontend-design`），为什么还需要在 `skills/do/agents/` 下创建自己的 agents？

## 答案：Skill vs Agent 的本质区别

### Skill（技能）
- **定义**: 一个完整的工作流，有自己的 SKILL.md
- **特点**:
  - 有自己的用户交互流程
  - 有决策逻辑（如询问用户选择模式）
  - 可以调用其他 skills 和 agents
  - 是一个"独立的应用"
- **例子**: `/ask-questions-if-underspecified` 会询问用户选择模式（"Transform directly" 或 "Build context first"）

### Agent（代理）
- **定义**: 一个单一任务的执行者，只是一个提示词文件
- **特点**:
  - 接收输入，返回输出
  - 没有用户交互
  - 没有决策逻辑
  - 是一个"工具函数"
- **例子**: `design-reviewer` 接收设计文档，返回审查报告，不会问用户任何问题

## /do 下的 Agents 的作用

### 1. code-explorer
- **作用**: 探索代码库，查找相关文件和模式
- **为什么不用 skill**: 没有对应的 `/code-explorer` skill
- **为什么需要**: Phase 1 需要并行探索代码库（3个 explorer 同时运行）

### 2. design-reviewer
- **作用**: 审查数据库、后端、前端设计的一致性
- **为什么不用 skill**: 没有对应的 `/design-review` skill
- **为什么需要**: Phase 5 需要检查各层设计是否对齐，这是 /do 特有的需求

### 3. test-executor
- **作用**: 执行测试用例，生成测试报告
- **为什么不用 skill**: 没有对应的 `/test-executor` skill
- **为什么需要**: Phase 6.4 需要验证实现是否通过测试用例

### 4. develop
- **作用**: 实现代码（数据库、后端、前端）
- **为什么不用 skill**: 这是一个通用的代码实现 agent，不是特定领域的 skill
- **为什么需要**: Phase 6 需要按照设计文档实现代码

### 5. code-reviewer
- **作用**: 最终代码审查，检查质量、安全、性能
- **为什么不用 skill**: 没有对应的 `/code-review` skill
- **为什么需要**: Phase 7 需要全面审查实现结果

## 设计原则

### 什么时候用 Skill？
**条件**:
1. 已经有成熟的 skill 存在
2. Skill 的工作流完全符合需求
3. 不介意 skill 的用户交互流程

**示例**:
- `/database-design` - 有完整的数据库设计工作流
- `/frontend-design` - 有完整的前端设计工作流（包含用户确认环节）
- `/test-cases` - 有完整的测试用例生成工作流

### 什么时候用 Agent？
**条件**:
1. 没有对应的 skill
2. 需要精确控制输入输出
3. 不需要用户交互
4. 是 /do 工作流的"内部步骤"

**示例**:
- `design-reviewer` - /do 特有的设计审查步骤
- `test-executor` - /do 特有的测试执行步骤
- `code-explorer` - /do 特有的代码库探索步骤

## 类比

### Skill = 餐厅
- 有完整的服务流程（接待、点菜、上菜、结账）
- 有自己的决策（推荐菜品、询问口味）
- 可以独立运营
- 例子: `/database-design` 就像一个专门做数据库设计的咨询公司

### Agent = 厨师
- 只负责做菜（接收食材，返回成品）
- 不会问客人问题
- 不能独立运营，需要有人指挥
- 例子: `design-reviewer` 就像一个审查员，只负责审查设计

### /do Skill = 总承包商
- 编排整个项目流程
- 有些工作外包给专业公司（调用 skills）
- 有些工作用自己的员工完成（调用 agents）
- 决定什么时候用外包，什么时候用自己人

## 实际例子

### Phase 4: Design（使用 Skills）

```bash
# 调用专业 skills，因为它们有完整的工作流
/database-design <PHASE3_OUTPUT>
/backend-development <PHASE3_OUTPUT>
/frontend-design <PHASE3_OUTPUT>
```

**为什么用 skills？**
- 这些领域已经有成熟的 skills
- 它们的工作流正好是 /do 需要的
- `/frontend-design` 的用户确认环节正好符合 /do 的需求

### Phase 5: Review（使用 Agent）

```bash
# 调用 agent，因为没有对应的 skill
codeagent-wrapper --agent design-reviewer - . <<'EOF'
## All Design Documents
- Database Design: $PHASE4_1_OUTPUT
- Backend Design: $PHASE4_2_OUTPUT
- Frontend Design: $PHASE4_3_OUTPUT

## Task
审查设计的一致性和完整性
EOF
```

**为什么用 agent？**
- 没有 `/design-review` skill
- 这是 /do 特有的步骤（审查多个设计文档的一致性）
- 不需要用户交互，只需要返回审查报告

## 总结

**do 下面的 agents 的作用**：
1. **填补空白** - 执行没有对应 skill 的任务
2. **精确控制** - 不需要额外的用户交互和决策逻辑
3. **内部工具** - 是 /do 工作流的"私有函数"
4. **轻量级** - 只是提示词文件，没有复杂的工作流

**设计哲学**：
- 能用 skill 就用 skill（复用现有能力）
- 不能用 skill 就创建 agent（填补空白）
- 混合使用，平衡灵活性和复用性

**最终架构**：
- 5个 Agents（内部工具）
- 7个 Skills（外部专家）
- 7个阶段（完整流程）

这样的设计既充分利用了现有的专业 skills，又保持了 /do 工作流的灵活性和可控性。
