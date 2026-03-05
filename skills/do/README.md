# /do - 企业级全栈开发工作流

> 从一句话需求到生产级应用，全自动化、全流程、全专业

## 🚀 核心能力

**一句话描述**：扔给我一个需求文档，我就能帮你完成一个完整的 App、小程序或网站。

**技术深度**：
- 🎯 **5 个专业 AI Agents + 7 个专业 Skills** 协同工作
- 📊 **7 个开发阶段** 完整覆盖
- 🔧 **6 大专业领域** 深度整合
- 📝 **4 类测试用例** 自动生成
- 🎨 **高保真 UI 设计** 用户确认机制
- 📋 **专业 PRD 文档** 100分质量评分

## 📈 技术架构

### 工作流概览

```
需求输入
    ↓
Phase 1: Requirements Analysis (需求分析)
    ├─ /product-requirements skill (PRD 生成)
    │   ├─ 100分质量评分系统
    │   ├─ 交互式需求收集
    │   └─ 生成 PRD 文档
    ├─ code-explorer × 3 (并行探索代码库)
    └─ 输出：PRD 文档 + 代码库分析
    ↓
Phase 2: Technical Clarification (技术澄清 - 可选)
    ├─ /ask-questions-if-underspecified skill (技术选型)
    └─ 输出：技术栈确认
    ↓
Phase 3: Optimize (优化提示词)
    ├─ /best-practices skill (应用5大转换原则)
    └─ 输出：可执行的详细需求文档
    ↓
Phase 4: Design (架构设计)
    ├─ /database-design skill (数据库设计)
    │   ├─ 规范化设计 (1NF/2NF/3NF)
    │   ├─ 索引策略优化
    │   └─ 零停机迁移方案
    ├─ /backend-development skill (后端架构)
    │   ├─ RESTful API 设计
    │   ├─ JWT/OAuth2 认证
    │   ├─ 缓存策略
    │   └─ 可观测性设计
    ├─ /frontend-design skill (前端设计)
    │   ├─ 设计思维 (极端风格选择)
    │   ├─ 高保真 UI 实现
    │   └─ 组件架构设计
    └─ 🔑 用户确认环节 (必须通过才能继续)
    ↓
Phase 5: Review (设计审查)
    ├─ design-reviewer (一致性审查)
    ├─ 安全性检查
    ├─ 性能评估
    └─ 输出：设计审查报告
    ↓
Phase 6: Implement (测试驱动实现)
    ├─ 6.0: /test-cases skill (生成测试用例)
    │   ├─ TC-F-XXX (功能测试)
    │   ├─ TC-E-XXX (边界测试)
    │   ├─ TC-ERR-XXX (错误处理)
    │   └─ TC-ST-XXX (状态转换)
    ├─ 6.1: develop (数据库实现)
    ├─ 6.2: develop (后端实现)
    ├─ 6.3: develop (前端实现)
    └─ 6.4: test-executor (测试验证)
    ↓
Phase 7: Complete (完成审查)
    ├─ code-reviewer (代码审查)
    ├─ 部署清单生成
    └─ 输出：生产就绪的应用
```

## 🎯 整合的专业能力

### 1. product-requirements (需求分析专家)
- **作用阶段**: Phase 1
- **实现方式**: 直接调用 `/product-requirements` skill
- **核心能力**:
  - 100分质量评分系统（5个维度）
  - 交互式需求收集和迭代完善
  - 90分阈值确保需求质量
  - 生成专业 PRD 文档
- **输出**: PRD 文档（`docs/{feature-name}-prd.md`）

### 2. ask-questions-if-underspecified (技术澄清专家)
- **作用阶段**: Phase 2（可选）
- **实现方式**: 直接调用 `/ask-questions-if-underspecified` skill
- **核心能力**: 结构化技术选型提问，多选题格式，默认选项
- **输出**: 明确的技术栈选择

### 3. best-practices (提示词优化专家)
- **作用阶段**: Phase 3
- **实现方式**: 直接调用 `/best-practices` skill
- **核心能力**: 5大转换原则
  1. 添加验证 (测试用例、成功标准)
  2. 提供具体上下文 (文件路径、模式引用)
  3. 添加约束 (技术栈、性能、安全)
  4. 分阶段结构化 (探索→设计→实现→验证)
  5. 包含丰富内容 (代码示例、错误处理)
- **输出**: 可执行的详细需求文档

### 3. database-design (数据库设计专家)
- **作用阶段**: Phase 4.1
- **实现方式**: 直接调用 `/database-design` skill
- **核心能力**:
  - 规范化设计 (1NF/2NF/3NF)
  - 索引策略 (B-tree, GIN, 复合索引, 部分索引)
  - 零停机迁移 (分步迁移、回滚策略)
  - 查询优化 (EXPLAIN 分析)
- **输出**: SQL 模式、索引、迁移脚本、ER 图

### 4. backend-development (后端架构专家)
- **作用阶段**: Phase 4.2
- **实现方式**: 直接调用 `/backend-development` skill
- **核心能力**:
  - RESTful API 设计 (OpenAPI 规范)
  - 认证授权 (JWT, OAuth2, RBAC)
  - 数据访问层 (ORM 模式)
  - 缓存策略 (Cache-aside, Write-through)
  - 可观测性 (日志、监控、追踪)
- **输出**: API 规范、认证流程、数据访问层设计

### 5. frontend-design (前端设计专家)
- **作用阶段**: Phase 4.3
- **实现方式**: 直接调用 `/frontend-design` skill
- **核心能力**:
  - 设计思维 (极端风格、避免 AI 审美)
  - 高保真 UI 实现 (可视化效果)
  - 组件架构 (状态管理、数据流)
  - 用户确认机制 (迭代优化)
- **输出**: 设计理念、高保真 UI、组件结构、样式指南

### 6. test-cases (测试用例生成专家)
- **作用阶段**: Phase 6.0
- **实现方式**: 直接调用 `/test-cases` skill
- **核心能力**:
  - 7步测试用例生成流程
  - 4类测试场景 (功能/边界/错误/状态转换)
  - AAA 模式 (Arrange-Act-Assert)
  - 覆盖率验证
- **输出**: 结构化测试用例文档、覆盖率矩阵

## 📊 技术指标

### 规模统计

**AI Agents (5个)**:
- code-explorer - 代码探索
- code-reviewer - 代码审查
- design-reviewer - 设计审查
- test-executor - 测试执行
- develop - 代码实现

**专业 Skills (7个)**:
- `/product-requirements` - 需求分析和 PRD 生成
- `/ask-questions-if-underspecified` - 技术澄清（可选）
- `/best-practices` - 提示词优化
- `/database-design` - 数据库设计
- `/backend-development` - 后端开发
- `/frontend-design` - 前端设计
- `/test-cases` - 测试用例生成

**其他指标**:
- 开发阶段: 7 个完整阶段
- 子阶段: 4 个实现子阶段 (6.0-6.4)
- 测试类型: 4 类测试用例
- 参考文档: 6 个最佳实践参考文档
- 脚本工具: 1 个任务管理脚本 (task.py)

### 自动化程度
- ✅ 需求澄清自动化 (结构化提问)
- ✅ 提示词优化自动化 (5大转换原则)
- ✅ 架构设计自动化 (数据库/后端/前端)
- ✅ 测试用例生成自动化 (4类场景)
- ✅ 代码实现自动化 (测试驱动)
- ✅ 测试验证自动化 (覆盖率分析)
- ✅ 代码审查自动化 (质量/安全/性能)

### 质量保证
- 🔒 安全性: 认证授权、输入验证、SQL 注入防护
- ⚡ 性能: 索引优化、缓存策略、查询优化
- 🧪 测试: 单元测试、集成测试、E2E 测试
- 📈 可观测性: 日志、监控、追踪
- 🎨 用户体验: 高保真设计、响应式布局、可访问性

## 🎬 实际使用场景

### 场景 1: 从零开发博客系统

**输入**:
```bash
/do 实现一个博客系统，包括文章管理、评论功能、用户认证
```

**自动执行流程**:

1. **Phase 1: Requirements Analysis** (2分钟)
   - 调用 /product-requirements skill
   - 交互式需求收集（质量评分 92/100）
   - 生成 PRD 文档（docs/blog-system-prd.md）
   - 探索代码库查找类似功能

2. **Phase 2: Technical Clarification** (1分钟 - 可选)
   - 如果 PRD 已明确技术栈，跳过此阶段
   - 否则询问：Backend (Python/Node.js)? Frontend (React/Vue)?
   - 用户回复: "defaults" 或 "1a 2a"

3. **Phase 3: Optimize** (2分钟)
   - 调用 `/best-practices` skill
   - 应用5大转换原则: 添加验证、上下文、约束

4. **Phase 4: Design** (5分钟)
   - **数据库设计** (调用 `/database-design`):
     ```sql
     CREATE TABLE users (...);
     CREATE TABLE posts (...);
     CREATE TABLE comments (...);
     CREATE INDEX idx_posts_user_date ON posts(user_id, created_at DESC);
     ```
   - **后端设计** (调用 `/backend-development`):
     ```
     POST   /api/posts          - 创建文章
     GET    /api/posts          - 列表查询
     GET    /api/posts/:id      - 详情查询
     PUT    /api/posts/:id      - 更新文章
     DELETE /api/posts/:id      - 删除文章
     POST   /api/posts/:id/comments - 添加评论
     ```
   - **前端设计** (调用 `/frontend-design`):
     - 设计理念: 极简主义 + 高对比度
     - 主色调: #1a1a1a (深灰) + #00ff9f (霓虹绿)
     - 字体: JetBrains Mono (代码风格)
     - 组件: PostList, PostDetail, CommentSection, AuthForm
   - **用户确认**: "设计效果满意吗？1) 满意，继续 2) 需要修改"

5. **Phase 5: Review** (2分钟)
   - 检查 API 与数据库模式一致性
   - 验证认证授权完整性
   - 评估性能和安全性

6. **Phase 6: Implement** (10分钟)
   - **6.0 生成测试用例** (调用 `/test-cases`):
     ```
     TC-F-001: 创建文章
     TC-F-002: 查看文章列表
     TC-E-001: 空标题验证
     TC-ERR-001: 未登录创建文章
     TC-ST-001: 文章状态转换 (draft → published → archived)
     ```
   - **6.1 实现数据库**: 执行迁移脚本
   - **6.2 实现后端**: 实现所有 API 端点 + 单元测试
   - **6.3 实现前端**: 实现所有组件 + 组件测试
   - **6.4 测试验证**: 执行测试，生成报告 (通过率 95%)

7. **Phase 7: Complete** (2分钟)
   - 代码审查: 质量 A, 安全 A, 性能 B+
   - 生成部署清单
   - 输出: 生产就绪的博客系统

**总耗时**: 约 22 分钟
**输出**: 完整的博客系统 (数据库 + 后端 + 前端 + 测试)

### 场景 2: 微信小程序开发

**输入**:
```bash
/do 开发一个外卖点餐小程序，包括商品浏览、购物车、下单支付
```

**Phase 2 澄清**:
- Frontend: 微信小程序
- Backend: Node.js + Express
- Database: MongoDB
- Payment: 微信支付

**Phase 4 设计**:
- 数据库: users, products, orders, carts (调用 `/database-design`)
- 后端: RESTful API + 微信支付集成 (调用 `/backend-development`)
- 前端: 小程序页面 + 组件 (商品列表、购物车、订单) (调用 `/frontend-design`)

**Phase 6 实现**:
- 生成 50+ 测试用例 (调用 `/test-cases`)
- 实现小程序前端 (WXML + WXSS + JS)
- 实现后端 API
- 集成微信支付
- 测试验证 (通过率 92%)

**输出**: 完整的外卖小程序

### 场景 3: 企业管理后台

**输入**:
```bash
/do 实现一个企业 CRM 系统，包括客户管理、销售跟进、数据分析
```

**Phase 4 设计**:
- 数据库: 复杂关系模型 (客户、联系人、商机、活动) (调用 `/database-design`)
- 后端: RBAC 权限系统 + 数据分析 API (调用 `/backend-development`)
- 前端: 仪表板 + 表格 + 图表 (Ant Design) (调用 `/frontend-design`)

**Phase 6 实现**:
- 生成 80+ 测试用例 (调用 `/test-cases`)
- 实现权限系统
- 实现数据分析功能
- 实现可视化仪表板

**输出**: 企业级 CRM 系统

## 🔥 核心优势

### 1. 专业性
- 每个领域都有专门的 AI Agent 或 Skill
- 遵循行业最佳实践
- 避免常见反模式

### 2. 完整性
- 从需求到部署的完整流程
- 数据库 + 后端 + 前端 + 测试
- 安全性、性能、可维护性全覆盖

### 3. 自动化
- 需求澄清自动化
- 架构设计自动化
- 测试用例生成自动化
- 代码实现自动化

### 4. 质量保证
- 测试驱动开发 (TDD)
- 多层审查机制
- 覆盖率验证
- 性能和安全检查

### 5. 用户参与
- 需求澄清阶段确认技术栈
- 前端设计阶段确认 UI 效果
- 支持迭代优化

## 🎓 技术亮点

### 数据库设计 (via `/database-design` skill)
- ✅ 规范化理论 (1NF/2NF/3NF)
- ✅ 索引优化策略 (B-tree, GIN, 复合索引)
- ✅ 零停机迁移方案
- ✅ 查询性能优化 (EXPLAIN 分析)

### 后端架构 (via `/backend-development` skill)
- ✅ RESTful API 设计规范
- ✅ JWT/OAuth2 认证授权
- ✅ 缓存策略 (Redis, Cache-aside)
- ✅ 可观测性 (日志、监控、追踪)

### 前端设计 (via `/frontend-design` skill)
- ✅ 设计思维 (极端风格、避免 AI 审美)
- ✅ 高保真 UI 实现
- ✅ 响应式设计
- ✅ 可访问性 (WCAG AA)

### 测试策略 (via `/test-cases` skill)
- ✅ 4类测试场景 (功能/边界/错误/状态转换)
- ✅ AAA 模式 (Arrange-Act-Assert)
- ✅ 覆盖率验证 (>80%)
- ✅ 自动化测试执行

## 📦 使用方式

### 基本用法

```bash
# 启动一个新任务
/do 实现一个博客系统

# 系统会自动：
# 1. 理解需求
# 2. 澄清技术栈
# 3. 优化需求文档
# 4. 设计架构 (调用专业 skills)
# 5. 审查设计
# 6. 测试驱动实现
# 7. 代码审查和部署
```

### 高级用法

```bash
# 使用 worktree 隔离开发
/do --worktree 实现用户认证系统

# 指定技术栈
/do 使用 Vue + FastAPI + PostgreSQL 实现博客系统

# 提供需求文档
/do @requirements.md 根据这个需求文档实现系统
```

## 🎯 适用场景

### ✅ 适合
- 全栈 Web 应用
- 微信小程序
- 企业管理后台
- API 服务
- 数据分析平台
- 电商系统
- 内容管理系统 (CMS)
- 社交平台

### ⚠️ 不适合
- 纯算法研究
- 硬件驱动开发
- 游戏引擎开发
- 区块链底层开发

## 🚀 开始使用

1. **安装依赖**:
   ```bash
   # 确保已安装 codeagent-wrapper
   # 确保已配置 Claude API
   ```

2. **配置 models.json**:
   ```bash
   cp skills/do/models.json.example ~/.codeagent/models.json
   # 根据需要调整模型配置
   ```

3. **运行第一个任务**:
   ```bash
   /do 实现一个待办事项应用
   ```

4. **查看任务状态**:
   ```bash
   python3 ~/.claude/skills/do/scripts/task.py status
   ```

5. **列出所有任务**:
   ```bash
   python3 ~/.claude/skills/do/scripts/task.py list
   ```

## 📚 参考资料

- `skills/do/SKILL.md` - 完整工作流定义
- `skills/do/agents/` - 5 个 Agent 提示词
- `skills/do/references/` - 最佳实践参考文档
- `skills/do/scripts/task.py` - 任务管理脚本

## 🎉 总结

**/do 不仅仅是一个开发工具，它是一个完整的企业级开发工作流。**

- 🎯 **5 个专业 AI Agents + 7 个专业 Skills** 协同工作
- 📊 **7 个开发阶段** 完整覆盖
- 🔧 **6 大专业领域** 深度整合
- 🧪 **测试驱动开发** 质量保证
- 🎨 **高保真 UI 设计** 用户确认

**从一句话需求到生产级应用，只需要一个 /do 命令。**

---

*Built with ❤️ by AI Agents & Professional Skills*
