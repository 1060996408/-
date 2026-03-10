# 插件与技能安装状态分析

检查时间: 2026-03-09 23:26

---

## 📊 已安装情况

### 一、Plugins (底层插件)

#### ✅ 已安装
1. **memory-lancedb-pro** 
   - 位置: `~/.openclaw/plugins/memory-lancedb-pro/`
   - 状态: 已安装
   - 作者: win4r

#### ❌ 未安装
2. **team-tasks** (多 Agent 编排)
   - 状态: 未安装

---

### 二、Skills (技能)

#### ✅ 已安装 (18 个)
1. agent-browser ✓
2. api-gateway ✓
3. auto-updater ✓
4. brave-search ✓
5. gh-issues ✓
6. github ✓
7. humanizer ✓
8. nano-banana-pro ✓
9. nano-pdf ✓
10. notion ✓
11. obsidian ✓
12. proactive-agent ✓
13. self-improving ✓
14. session-logs ✓
15. skill-vetter ✓
16. summarize ✓
17. tavily-search ✓
18. weather ✓

#### ❌ 未安装
- n8n (本地自动化)
- github-pr-reviewer (深度 PR 审查)

---

### 三、安全防线 Skills

#### ❌ 未安装
1. **clauditor** (行为审计)
2. **aegis-shield** (防泄漏过滤)

---

### 四、系统配置

#### ❌ 容器运行时
- Docker: 未安装
- Podman: 未安装
- 当前: 直接在 WSL2 主机运行 (无沙箱隔离)

#### ⚠️ Node.js 版本
- 当前: v22.4.1
- 要求: v22.12+
- 状态: 需要升级

---

## 🎯 必要性分析 (针对你的使用场景)

### 🔥 高优先级 (强烈推荐)

#### 1. team-tasks (多 Agent 编排) ⭐⭐⭐⭐⭐
**为什么必要:**
- 你已经设计了 4 个 Agent 架构 (Orchestrator + 3 个子 Agent)
- 目前只能手动调用子 Agent,无法实现自动化流水线
- team-tasks 提供 3 种工作流:
  - **Linear**: 线性流水线 (适合你的"每日维护"流程)
  - **DAG**: 并行分发 (适合同时处理多个 issues)
  - **Debate**: 多 Agent 辩论 (适合代码审查)

**使用场景:**
- Orchestrator 收到任务 → 自动分发给 Coder/Researcher/Knowledge-Weaver
- 多个 Agent 并行工作,结果汇总
- 代码审查时多个 Agent 交叉验证

**安装难度:** 中等 (需要配置工作流 YAML)

---

#### 2. Node.js 升级到 v22.12+ ⭐⭐⭐⭐⭐
**为什么必要:**
- `openclaw doctor` 命令无法运行
- 可能影响其他功能稳定性
- 官方要求的最低版本

**操作:**
```bash
nvm install 22
nvm use 22
nvm alias default 22
```

---

#### 3. github-pr-reviewer ⭐⭐⭐⭐
**为什么必要:**
- 你已经有 gh-issues (自动修复 issues)
- github-pr-reviewer 是下一步:
  - 自动审查 PR 代码
  - 抓取 CI/CD 报错日志
  - 深度诊断测试失败原因
- 与 Coder-Maintainer 完美配合

**使用场景:**
- gh-issues 生成 PR 后,自动触发审查
- 发现问题自动修复并更新 PR
- 监控 GitHub Actions 失败并诊断

**安装难度:** 低 (基于 gh CLI,你已有 GitHub token)

---

### 🛡️ 中优先级 (安全加固)

#### 4. clauditor (行为审计) ⭐⭐⭐
**为什么有用:**
- 记录所有 Shell 命令和网络请求
- 防止 AI 执行危险命令 (如 `rm -rf`)
- 提供审计日志,事后追溯

**是否必要:**
- WSL2 环境相对安全 (不是生产服务器)
- 如果只是个人使用,优先级可降低
- 如果部署到云端 VPS,必须安装

---

#### 5. aegis-shield (防泄漏) ⭐⭐⭐
**为什么有用:**
- 扫描 AI 发送的数据,防止泄漏密码/私钥
- 防止提示词注入攻击

**是否必要:**
- 你的 GitHub token 已经在配置文件中
- 如果 AI 处理敏感数据 (客户信息/公司代码),必须安装
- 个人项目可选

---

### 🔧 低优先级 (可选增强)

#### 6. n8n 集成 ⭐⭐
**为什么可选:**
- 需要单独部署 n8n 服务
- 适合复杂的自动化流程 (如定时抓取 + 多平台推送)
- 你的 Cron + Skills 已经能覆盖大部分场景

**使用场景:**
- 每天早上抓取 HackerNews 发到微信
- 监控多个 RSS 源并汇总
- 复杂的多步骤自动化

**安装难度:** 高 (需要部署 n8n + 配置 API)

---

#### 7. Podman (沙箱隔离) ⭐⭐
**为什么可选:**
- WSL2 本身已经是隔离环境
- 如果部署到云端 VPS,强烈推荐
- 个人 WSL2 使用,优先级低

**安装难度:** 中等 (需要配置 OpenClaw 使用 Podman)

---

## 📋 推荐安装顺序

### 第一批 (立即安装,提升效率)
1. ✅ **升级 Node.js 到 v22.12+**
2. ✅ **安装 team-tasks** (多 Agent 编排核心)
3. ✅ **安装 github-pr-reviewer** (完善 DevOps 流程)

### 第二批 (安全加固,可选)
4. ⚠️ **安装 clauditor** (如果担心安全)
5. ⚠️ **安装 aegis-shield** (如果处理敏感数据)

### 第三批 (高级功能,按需)
6. ⏸️ **n8n** (如果需要复杂自动化)
7. ⏸️ **Podman** (如果部署到生产环境)

---

## 🎯 针对你的 4-Agent 架构的建议

### 当前架构
```
主 Agent (Orchestrator)
├── 子 Agent 1 (Coder-Maintainer)
├── 子 Agent 2 (Researcher)
└── 子 Agent 3 (Knowledge-Weaver)
```

### 安装 team-tasks 后的增强
```
主 Agent (Orchestrator) + team-tasks
├── Linear 流水线: 每日维护流程
│   └── Coder → 更新依赖 → 审查 → 提交
├── DAG 并行: 处理多个 issues
│   ├── Coder → 修复 issue #1
│   ├── Coder → 修复 issue #2
│   └── Researcher → 调研新技术
└── Debate 辩论: 代码审查
    ├── Coder → 提交代码
    ├── Reviewer → 审查
    └── Knowledge-Weaver → 文档检查
```

### 安装 github-pr-reviewer 后的完整 DevOps 流程
```
1. gh-issues 抓取 issue
2. Coder-Maintainer 生成修复代码
3. 提交 PR
4. github-pr-reviewer 自动审查
5. 发现问题 → 自动修复 → 更新 PR
6. CI/CD 通过 → 合并
```

---

## 💡 总结

**必装 (3 个):**
1. Node.js v22.12+ (系统要求)
2. team-tasks (多 Agent 编排核心)
3. github-pr-reviewer (完善 DevOps)

**可选 (2 个):**
4. clauditor (安全审计)
5. aegis-shield (防泄漏)

**暂不需要 (2 个):**
6. n8n (复杂自动化,当前 Cron 够用)
7. Podman (WSL2 环境,优先级低)

---

## 📝 下一步操作

要我帮你:
1. 升级 Node.js?
2. 安装 team-tasks?
3. 安装 github-pr-reviewer?
