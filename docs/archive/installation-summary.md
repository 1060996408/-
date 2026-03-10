# Skills 安装总结

安装时间: 2026-03-09 22:47

## ✅ 已安装的 3 个新 Skills

### 1. 1password (密码管理)
- **功能**: 1Password CLI 集成,安全读取/注入/运行密钥
- **用途**: 管理 API keys, tokens, 敏感凭证
- **要求**: 需要安装 `op` CLI 和桌面应用集成
- **配合**: Coder-Maintainer 用于安全存储 GitHub tokens 等凭证

### 2. gh-issues (自动修复 Issues)
- **功能**: 自动抓取 GitHub Issues,生成修复代码,提交 PR,处理 review 评论
- **用途**: 自动化开发流程,减少手动修复工作
- **特性**:
  - 并行处理多个 issues (最多 8 个)
  - 支持 fork 模式
  - 自动运行测试
  - 处理 PR review 评论
  - Watch 模式持续监控
  - Cron 模式定时执行
- **配合**: Coder-Maintainer 的核心自动化工具

### 3. session-logs (日志分析)
- **功能**: 搜索和分析会话日志 (JSONL 格式)
- **用途**: 查找历史对话,分析成本,统计工具使用
- **特性**:
  - 按日期/关键词搜索
  - 成本统计
  - 工具使用分析
  - 支持 jq 和 rg 查询
- **配合**: Self-improving 的反思分析基础

---

## 📋 配置更新

### Coder-Maintainer Agent
**配置文件**: `~/.openclaw/agents/coder-maintainer/agent.json`

**更新前**:
```json
"skills": [
  "auto-updater",
  "skill-vetter",
  "github"
]
```

**更新后**:
```json
"skills": [
  "auto-updater",
  "skill-vetter",
  "github",
  "gh-issues",
  "1password",
  "session-logs"
]
```

---

## 🔧 下一步配置

### 1password 配置
1. 安装 1Password CLI:
   ```bash
   brew install 1password-cli
   ```

2. 启用桌面应用集成 (在 1Password 设置中)

3. 登录:
   ```bash
   op signin
   ```

4. 测试:
   ```bash
   op whoami
   op vault list
   ```

### gh-issues 配置
1. 确保 GH_TOKEN 已配置:
   - 在 `~/.openclaw/openclaw.json` 中设置:
     ```json
     "skills": {
       "entries": {
         "gh-issues": {
           "apiKey": "ghp_your_token_here"
         }
       }
     }
     ```

2. 或使用环境变量:
   ```bash
   export GH_TOKEN="ghp_your_token_here"
   ```

3. 测试:
   ```bash
   curl -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/user
   ```

### session-logs 配置
无需额外配置,确保已安装:
```bash
which jq  # JSON 查询工具
which rg  # ripgrep 搜索工具
```

如未安装:
```bash
brew install jq ripgrep
```

---

## 📊 当前 Skills 统计

- **总计**: 19 个 skills
- **主 Agent (Orchestrator)**: 4 个
- **子 Agent 1 (Coder-Maintainer)**: 6 个 ⬆️ (新增 3 个)
- **子 Agent 2 (Researcher)**: 4 个
- **子 Agent 3 (Knowledge-Weaver)**: 5 个

---

## 🎯 使用场景示例

### 场景 1: 自动修复 GitHub Issues
```bash
# 在仓库目录下
/gh-issues --label bug --limit 5 --yes
```

Coder-Maintainer 会:
1. 抓取 5 个标记为 bug 的 issues
2. 并行生成修复代码
3. 运行测试
4. 提交 PR
5. 处理 review 评论

### 场景 2: 安全管理 API Keys
```bash
# 从 1Password 读取密钥
op read "op://Private/GitHub Token/credential"

# 注入到命令中
op run --env-file=.env -- npm run deploy
```

### 场景 3: 分析历史对话
```bash
# 搜索关键词
jq -r 'select(.message.role == "user") | .message.content[]? | select(.type == "text") | .text' \
  ~/.openclaw/agents/orchestrator/sessions/*.jsonl | rg "部署"

# 统计成本
jq -s '[.[] | .message.usage.cost.total // 0] | add' \
  ~/.openclaw/agents/orchestrator/sessions/session-123.jsonl
```

---

## ✅ 已推送到 GitHub

所有更改已提交并推送到: https://github.com/1060996408/-

包含:
- 3 个新 skills 的完整代码
- Coder-Maintainer agent 配置更新
- 文档更新
