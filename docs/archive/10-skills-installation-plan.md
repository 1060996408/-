# 10 个高优先级技能安装计划

## 📋 技能分配方案

### 主 Agent (Orchestrator)
1. **mcp-bridge** - MCP 协议桥接
2. **telegram-bot** - Telegram 远程控制
3. **eval-judge** - 质量评估
4. **cron-manager** - 任务管理增强

### 子 Agent 1 (Coder-Maintainer)
5. **repo-map-generator** - 代码库地图生成

### 子 Agent 2 (Researcher)
6. **jina-reader** - 快速网页提取
7. **firecrawl** - 结构化爬虫

### 子 Agent 3 (Knowledge-Weaver)
8. **markitdown** - 文档转换
9. **whisper-local** - 语音转文字
10. **cal-com/google-calendar** - 日程管理

---

## ⚠️ 问题: 需要确认仓库地址

这些技能大部分是社区贡献,不在 OpenClaw 官方仓库中。我需要:

1. **搜索 GitHub 找到对应的仓库**
2. **验证是否是 OpenClaw 兼容的 skill**
3. **检查安装方式**

### 已知可用的技能

#### ✅ whisper-local
- 官方已有: `openai-whisper` (本地版本)
- 位置: `~/.npm-global/lib/node_modules/openclaw/skills/openai-whisper`
- 状态: 可以直接复制安装

#### ✅ mcporter (MCP 桥接)
- 官方已有: `mcporter`
- 位置: `~/.npm-global/lib/node_modules/openclaw/skills/mcporter`
- 功能: MCP 服务器集成
- 状态: 可以直接复制安装

---

## 🔍 需要搜索的技能 (7 个)

1. **telegram-bot** - 需要搜索 OpenClaw Telegram skill
2. **eval-judge** - 需要搜索评估技能
3. **repo-map-generator** - 需要搜索代码地图生成器
4. **jina-reader** - 需要搜索 Jina Reader 集成
5. **firecrawl** - 需要搜索 Firecrawl 集成
6. **markitdown** - 需要搜索 Microsoft Markitdown 集成
7. **cron-manager** - 需要搜索系统 cron 管理
8. **cal-com/google-calendar** - 需要搜索日历集成

---

## 📝 建议的安装策略

### 方案 A: 先安装已有的 (2 个)
1. 复制 `openai-whisper` 到 workspace
2. 复制 `mcporter` 到 workspace
3. 配置到对应的 Agent

### 方案 B: 搜索并安装社区技能
1. 在 GitHub 搜索 "openclaw skill telegram"
2. 在 GitHub 搜索 "openclaw skill jina"
3. 等等...

### 方案 C: 自己创建简单的技能
对于一些简单的功能 (如 telegram-bot),可以:
1. 使用 skill-creator 创建基础框架
2. 集成现有的 API/CLI 工具
3. 编写 SKILL.md 文档

---

## 🎯 我的建议

**立即执行:**
1. 安装 `openai-whisper` (已有)
2. 安装 `mcporter` (已有,MCP 桥接)

**需要你的决定:**
- 是否让我搜索其他 8 个技能的 GitHub 仓库?
- 还是先安装已有的 2 个,其他的按需搜索?
- 或者我可以帮你创建一些简单的技能?

---

## ⚡ 快速开始

要我:
1. 先安装已有的 2 个技能 (whisper + mcporter)?
2. 搜索其他 8 个技能的仓库地址?
3. 创建一个技能搜索和安装的自动化脚本?
