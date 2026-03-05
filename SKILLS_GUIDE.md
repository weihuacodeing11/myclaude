# Skills 使用指南

> 完整的 skills 列表和使用方法

## 📚 目录

- [工作流 Skills](#工作流-skills) - 完整的开发工作流
- [专业领域 Skills](#专业领域-skills) - 特定领域的专家能力
- [工具类 Skills](#工具类-skills) - 辅助工具和自动化
- [快速参考](#快速参考)

---

## 🚀 工作流 Skills

这些 skills 提供完整的端到端开发工作流。

### `/do` - 企业级全栈开发工作流 ⭐ 推荐

**用途**: 从需求到生产的完整开发流程

**核心能力**:
- 7 个开发阶段（需求分析 → 技术澄清 → 优化 → 设计 → 审查 → 实现 → 完成）
- 5 个内部 AI Agents + 7 个专业 Skills 协同
- 自动生成 PRD、数据库设计、API 设计、前端设计
- 测试驱动开发（TDD）
- 高保真 UI 设计（用户确认机制）

**使用方法**:
```bash
# 基本用法
/do 实现一个博客系统，包括文章管理、评论功能、用户认证

# 使用 worktree 隔离开发
/do --worktree 实现用户认证系统

# 指定技术栈
/do 使用 Vue + FastAPI + PostgreSQL 实现博客系统

# 提供需求文档
/do @requirements.md 根据这个需求文档实现系统
```

**适用场景**:
- ✅ 全栈 Web 应用
- ✅ 微信小程序
- ✅ 企业管理后台
- ✅ API 服务
- ✅ 电商系统

**详细文档**: `skills/do/README.md`

---

### `/omo` - 多 Agent 智能编排

**用途**: 智能路由和多 Agent 协作

**核心能力**:
- Sisyphus 协调器（智能路由）
- 6 个专业 Agents（Oracle, Librarian, Explore, Develop, Frontend, Document）
- 动态任务分配
- 多后端支持（Claude/Codex/Gemini/OpenCode）

**使用方法**:
```bash
# 基本用法
/omo 调查并修复登录失败的问题

# 复杂任务
/omo 分析性能瓶颈并优化数据库查询
```

**适用场景**:
- ✅ Bug 调查和修复
- ✅ 性能优化
- ✅ 代码重构
- ✅ 复杂问题诊断

**详细文档**: `skills/omo/README.md`

---

### `/sparv` - SPARV 工作流

**用途**: Specify → Plan → Act → Review → Vault 流程

**核心能力**:
- 10 分质量门控
- 结构化规划
- 自动审查
- 知识归档

**使用方法**:
```bash
/sparv 实现用户权限管理系统
```

**适用场景**:
- ✅ 需要严格质量控制的项目
- ✅ 企业级开发
- ✅ 合规要求高的场景

**详细文档**: `skills/sparv/README.md`

---

### `/dev` - 轻量级开发工作流

**用途**: 快速原型和简单任务

**核心能力**:
- 简化的开发流程
- 快速迭代
- 适合小型任务

**使用方法**:
```bash
/dev 添加一个导出 CSV 的功能
```

**适用场景**:
- ✅ 快速原型
- ✅ 小功能开发
- ✅ Bug 修复

---

## 🎯 专业领域 Skills

这些 skills 专注于特定领域的专业能力。

### `/product-requirements` - PRD 生成专家

**用途**: 生成专业的产品需求文档

**核心能力**:
- 100 分质量评分系统（5 个维度）
- 交互式需求收集
- 迭代完善（90 分阈值）
- 生成标准 PRD 文档

**使用方法**:
```bash
/product-requirements

# 系统会交互式询问：
# - 项目背景
# - 核心功能
# - 用户角色
# - 技术约束
# - 成功标准
```

**输出**: `docs/{feature-name}-prd.md`

**质量评分维度**:
1. 清晰度（20分）
2. 完整性（20分）
3. 可行性（20分）
4. 可测试性（20分）
5. 优先级（20分）

---

### `/database-design` - 数据库设计专家

**用途**: 设计规范化的数据库模式

**核心能力**:
- 规范化设计（1NF/2NF/3NF）
- 索引策略优化（B-tree, GIN, 复合索引）
- 零停机迁移方案
- 查询性能优化（EXPLAIN 分析）

**使用方法**:
```bash
/database-design

# 提供需求后，生成：
# - SQL 模式定义
# - 索引创建语句
# - 迁移脚本
# - ER 图（文本描述）
```

**最佳实践**:
- ✅ 外键约束
- ✅ 唯一索引
- ✅ 部分索引
- ✅ 级联删除策略

---

### `/backend-development` - 后端架构专家

**用途**: 设计 RESTful API 和后端架构

**核心能力**:
- RESTful API 设计（OpenAPI 规范）
- 认证授权（JWT, OAuth2, RBAC）
- 数据访问层（ORM 模式）
- 缓存策略（Cache-aside, Write-through）
- 可观测性（日志、监控、追踪）

**使用方法**:
```bash
/backend-development

# 生成：
# - API 规范（OpenAPI）
# - 认证流程图
# - 数据访问层设计
# - 缓存策略文档
```

**API 设计原则**:
- ✅ 资源导向
- ✅ 统一错误处理
- ✅ 版本控制
- ✅ 分页和过滤

---

### `/frontend-design` - 前端设计专家

**用途**: 设计高保真 UI 和前端架构

**核心能力**:
- 设计思维（极端风格选择）
- 高保真 UI 实现
- 组件架构设计
- 用户确认机制（迭代优化）

**使用方法**:
```bash
/frontend-design

# 生成：
# - 设计理念说明
# - 高保真 UI 设计（可视化效果）
# - 组件结构图
# - 样式指南（颜色、字体、间距）
# - 交互流程图
```

**设计原则**:
- 🎨 避免 AI 审美（Inter/Roboto）
- 🎨 选择极端风格（极简/极繁/复古未来）
- 🎨 独特的字体和颜色
- 🎨 高影响力动效

---

### `/test-cases` - 测试用例生成专家

**用途**: 生成完整的测试用例

**核心能力**:
- 7 步测试用例生成流程
- 4 类测试场景（功能/边界/错误/状态转换）
- AAA 模式（Arrange-Act-Assert）
- 覆盖率验证

**使用方法**:
```bash
/test-cases

# 生成：
# - 功能测试用例（TC-F-XXX）
# - 边界测试用例（TC-E-XXX）
# - 错误处理测试用例（TC-ERR-XXX）
# - 状态转换测试用例（TC-ST-XXX）
```

**输出**: `tests/{name}-test-cases.md`

**测试场景**:
- ✅ 正常路径
- ✅ 边界条件
- ✅ 错误处理
- ✅ 状态转换

---

### `/ask-questions-if-underspecified` - 需求澄清专家

**用途**: 结构化的需求澄清

**核心能力**:
- 检查需求完整性（6 个维度）
- 生成结构化问题（多选题格式）
- 提供默认选项
- 优先消除整个工作分支的问题

**使用方法**:
```bash
/ask-questions-if-underspecified

# 自动检查：
# - 目标和完成标准
# - 范围和边界
# - 技术栈
# - 约束条件
# - 环境和部署
# - 安全和合规要求
```

**问题格式**:
```
1) Backend Technology?
   a) Python + FastAPI (default)
   b) Node.js + Express
   c) Go + Gin
   Reply: defaults (or 1a)
```

---

### `/best-practices` - 提示词优化专家

**用途**: 优化提示词质量

**核心能力**:
- 5 大转换原则
- 3 个并行代理（意图分析、最佳实践、代码库上下文）
- 自动添加验证和约束

**使用方法**:
```bash
/best-practices

# 应用 5 个转换原则：
# 1. 添加验证（测试用例、成功标准）
# 2. 提供具体上下文（文件路径、模式引用）
# 3. 添加约束（技术栈、性能、安全）
# 4. 分阶段结构化（探索→设计→实现→验证）
# 5. 包含丰富内容（代码示例、错误处理）
```

---

## 🛠️ 工具类 Skills

这些 skills 提供辅助工具和自动化能力。

### `/browser` - 浏览器自动化

**用途**: Web 测试和数据提取

**核心能力**:
- Playwright 自动化
- 页面截图
- 数据抓取
- E2E 测试

**使用方法**:
```bash
/browser 访问 example.com 并截图
```

---

### `/codeagent` - Codeagent Wrapper 集成

**用途**: 调用 codeagent-wrapper 执行代码任务

**核心能力**:
- 多后端支持（Codex/Claude/Gemini/OpenCode）
- Agent 模式
- 流式输出

**使用方法**:
```bash
/codeagent --agent develop "实现用户登录功能"
```

---

### `/skill-install` - Skill 安装器

**用途**: 从 GitHub 安装 skills

**核心能力**:
- GitHub 仓库下载
- 安全扫描
- 依赖检查
- 自动安装

**使用方法**:
```bash
/skill-install github:username/my-skill
```

---

### `/skill-creator` - Skill 创建器

**用途**: 创建新的 skill

**核心能力**:
- Skill 模板生成
- 最佳实践指导
- 文件结构创建

**使用方法**:
```bash
/skill-creator my-new-skill
```

---

### `/prototype-prompt-generator` - 原型提示词生成器

**用途**: 生成 UI/UX 原型提示词

**核心能力**:
- 结构化需求收集
- 设计系统定义
- 组件规范生成

**使用方法**:
```bash
/prototype-prompt-generator
```

---

### `/harness` - 长时间运行 Agent 框架

**用途**: 管理长时间运行的 agent 任务

**核心能力**:
- 自我反思机制
- 状态持久化
- 错误恢复
- 进度跟踪

**使用方法**:
```bash
/harness start my-long-task
```

---

## 📊 快速参考

### 按使用场景选择

| 场景 | 推荐 Skill |
|------|-----------|
| **完整项目开发** | `/do` |
| **Bug 调查修复** | `/omo` |
| **快速原型** | `/dev` |
| **需求文档** | `/product-requirements` |
| **数据库设计** | `/database-design` |
| **API 设计** | `/backend-development` |
| **UI 设计** | `/frontend-design` |
| **测试用例** | `/test-cases` |
| **需求澄清** | `/ask-questions-if-underspecified` |
| **提示词优化** | `/best-practices` |

### 按复杂度选择

| 复杂度 | 推荐 Skill |
|--------|-----------|
| **简单** | `/dev` |
| **中等** | `/omo` |
| **复杂** | `/do` |
| **企业级** | `/sparv` |

### 组合使用示例

#### 示例 1: 完整项目开发

```bash
# Step 1: 生成 PRD
/product-requirements

# Step 2: 使用 /do 开发
/do @docs/my-feature-prd.md 根据这个 PRD 实现系统
```

#### 示例 2: 数据库优化

```bash
# Step 1: 重新设计数据库
/database-design

# Step 2: 使用 /omo 实现迁移
/omo 根据新的数据库设计实现零停机迁移
```

#### 示例 3: 前端重构

```bash
# Step 1: 设计新 UI
/frontend-design

# Step 2: 生成测试用例
/test-cases

# Step 3: 使用 /dev 实现
/dev 根据新设计重构前端组件
```

---

## 🎓 学习路径

### 初学者

1. 从 `/dev` 开始（简单任务）
2. 尝试 `/product-requirements`（学习需求分析）
3. 使用 `/do`（完整工作流）

### 进阶用户

1. 掌握 `/do` 的所有阶段
2. 学习 `/omo` 的智能路由
3. 使用专业领域 skills（database-design, backend-development, frontend-design）

### 高级用户

1. 组合使用多个 skills
2. 自定义 skill 配置
3. 创建自己的 skills（`/skill-creator`）

---

## 📝 配置说明

### 安装 Skills

```bash
# 使用 npx 安装
npx github:weihuacodeing11/myclaude

# 或使用 Python 安装器
python3 install.py --module do,omo,sparv
```

### 配置 Agent 模型

编辑 `~/.codeagent/models.json`:

```json
{
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

### 查看已安装 Skills

```bash
ls ~/.claude/skills/
```

---

## 🔗 相关资源

- **仓库**: https://github.com/weihuacodeing11/myclaude
- **Issues**: https://github.com/weihuacodeing11/myclaude/issues
- **文档**: 各 skill 目录下的 README.md 或 SKILL.md

---

## 💡 提示

1. **优先使用 `/do`**: 对于大多数开发任务，`/do` 是最佳选择
2. **组合使用**: 可以先用专业 skills 生成设计，再用工作流 skills 实现
3. **查看文档**: 每个 skill 都有详细的 SKILL.md 文档
4. **配置模型**: 根据任务复杂度选择合适的 AI 模型
5. **使用 worktree**: 对于大型任务，使用 `--worktree` 隔离开发

---

**最后更新**: 2026-03-05
