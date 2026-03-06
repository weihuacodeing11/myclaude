# myclaude

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-7.0-green)](https://github.com/weihuacodeing11/myclaude)

> 为 Claude Code 打造的精简 AI 工作流 - 从需求到完整应用

[English](README.md) | 中文

## 这是什么？

一个完整的工作流（`/do`），让你从一个简单的想法到一个完全实现的应用或网站。零外部依赖，无需复杂配置 - 只需 Claude Code 做它最擅长的事。

## 系统要求

**使用 `/do` 工作流时：**
- **Python 3.7+**（仅使用标准库，无需额外安装包）
- **Claude Code CLI**

**安装时：**
- **Node.js**（如果使用 NPX 安装器）
- **或 Python 3.7+**（如果使用 `python install.py`）

大多数系统已预装 Python 3。检查方法：
```bash
python3 --version
```

如未安装：
- **macOS/Linux**：通常已预装
- **Windows**：从 [python.org](https://www.python.org/downloads/) 下载

## 快速开始

```bash
# 安装
npx github:weihuacodeing11/myclaude

# 使用
/do "构建一个带用户认证的待办事项应用"
```

就这么简单！工作流会：
1. 📋 通过交互式对话生成完整的 PRD
2. 🔍 探索你的代码库寻找模式
3. ❓ 澄清任何技术细节
4. 🎨 设计数据库、后端和前端
5. ✅ 获取你对设计的批准
6. 💻 实现所有功能并编写测试
7. 🚀 代码审查并提供部署清单

## `/do` 工作流

7 个阶段的系统化方法：

| 阶段 | 功能 |
|-------|-------------|
| **1. 理解需求** | 通过交互式 PRD 生成收集需求 |
| **2. 技术澄清** | 可选的技术选型澄清 |
| **3. 优化需求** | 应用最佳实践转换需求 |
| **4. 架构设计** | 数据库、后端和前端架构设计 |
| **5. 设计审查** | 设计一致性和安全性检查 |
| **6. 代码实现** | 使用当前 Claude 模型直接实现 |
| **7. 完成总结** | 最终代码审查和部署清单 |

## 特性

- ✨ **零依赖** - 完全使用 Claude Code 当前模型
- 🎯 **单一工作流** - 一个命令，完整解决方案
- 🔄 **交互式** - 需要时才提问，不提前询问
- 📦 **简单安装** - 一条 NPX 命令
- 🧪 **测试驱动** - 生成并验证测试用例
- 🎨 **设计优先** - 实现前获得批准

## 安装

```bash
# 交互式安装器（推荐）
npx github:weihuacodeing11/myclaude

# 或使用 Python 直接安装（覆盖已有安装）
python install.py
```

## 安装后

工作流会安装到 `~/.claude/`：

```
~/.claude/
├── skills/do/              # /do 工作流
│   ├── SKILL.md           # 主工作流定义
│   └── scripts/           # 任务管理脚本
└── installed_modules.json  # 跟踪安装状态
```

## 使用示例

### 构建待办事项应用
```bash
/do "构建一个带用户认证和实时更新的待办事项应用"
```

### 创建落地页
```bash
/do "为 SaaS 产品创建一个现代化的落地页，包含定价层级"
```

### 添加功能
```bash
/do "为现有仪表板添加导出到 CSV 的功能"
```

## 工作原理

`/do` 工作流集成了多个专业技能：

- **product-requirements** - 带质量评分的交互式 PRD 生成
- **ask-questions-if-underspecified** - 澄清技术选择
- **best-practices** - 用 5 个转换原则优化需求
- **database-design** - 设计数据库架构和迁移
- **backend-development** - 设计后端 API 和架构
- **frontend-design** - 设计前端 UI 和组件
- **test-cases** - 生成结构化测试用例

全部由 Claude Code 当前模型编排 - 无需外部工具。

## 会生成什么？

### 数据库层
- 规范化的架构设计
- 优化的索引
- 迁移脚本
- 种子数据

### 后端层
- RESTful API 端点
- 认证/授权
- 数据访问层
- 缓存策略
- 错误处理
- 日志和监控

### 前端层
- 组件架构
- 状态管理
- API 集成
- 响应式设计
- 无障碍访问（WCAG AA）
- 加载状态和错误处理

### 测试
- 单元测试
- 集成测试
- 端到端测试
- 测试覆盖率 > 80%

## 技术特性

- **设计优先**：实现前获得批准
- **测试驱动**：编码前生成测试用例
- **最佳实践**：自动应用行业标准
- **安全聚焦**：内置安全检查
- **性能优化**：缓存和查询优化
- **生产就绪**：包含部署清单

## 故障排除

**模块未加载：**
```bash
cat ~/.claude/installed_modules.json
python install.py --force --module do
```

**安装错误：**
```bash
python3 --version  # 需要 3.7+
python install.py --force --module do
```

## 卸载

```bash
# 删除所有已安装的文件
python uninstall.py
```

## 许可证

AGPL-3.0 - 查看 [LICENSE](LICENSE)

商业使用无需 AGPL 义务，请联系：support@stellarlink.co

## 支持

- [GitHub Issues](https://github.com/weihuacodeing11/myclaude/issues)
