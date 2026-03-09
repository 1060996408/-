# OpenClaw 可用 Skills 分析报告

生成时间: 2026-03-09 21:35

## 📊 概览

- **已安装 Skills**: 16 个
- **系统内置 Skills**: 48 个 (在 npm global 中)
- **未安装但可用**: 32 个

---

## 🎯 按功能分类的可用 Skills

### 1. 📝 笔记与知识管理 (已有 3 个)

#### 已安装
- ✅ **obsidian**: 本地 Markdown 笔记库
- ✅ **notion**: 云端协作文档
- ✅ **humanizer**: 去除 AI 味道

#### 可补充
- **apple-notes**: macOS 原生笔记 (通过 memo CLI)
  - 用途: 快速记录临时想法,与 iOS 同步
  - 配合: Obsidian 管理长期知识,Apple Notes 处理临时碎片
  
- **bear-notes**: Bear 笔记管理 (通过 grizzly CLI)
  - 用途: 标签化笔记系统
  - 配合: 作为 Obsidian 的轻量级替代方案

---

### 2. 🔍 搜索与研究 (已有 4 个)

#### 已安装
- ✅ **tavily-search**: AI 优化搜索
- ✅ **brave-search**: 轻量级搜索
- ✅ **agent-browser**: 浏览器自动化
- ✅ **summarize**: 内容摘要

#### 可补充
- **goplaces**: Google Places API 查询
  - 用途: 地点搜索、评论、详情
  - 配合: Researcher Agent 处理地理位置相关研究

---

### 3. 💬 通讯与消息 (已有 0 个)

#### 可补充
- **imsg**: iMessage/SMS CLI
  - 用途: 发送 iMessage 和 SMS
  - 配合: 主 Agent 的日常通讯需求
  
- **bluebubbles**: iMessage 集成 (推荐)
  - 用途: 更强大的 iMessage 管理
  - 配合: 替代或补充 imsg

- **wacli**: WhatsApp CLI
  - 用途: 发送 WhatsApp 消息,搜索历史
  - 配合: 主 Agent 的跨平台通讯

- **slack**: Slack 集成
  - 用途: 团队协作消息
  - 配合: 工作场景的消息管理

- **discord**: Discord 集成
  - 用途: 社区/游戏通讯
  - 配合: 特定社群的消息管理

- **xurl**: X (Twitter) API CLI
  - 用途: 发推、回复、搜索、DM
  - 配合: Researcher Agent 的社交媒体监控

---

### 4. 📧 邮件管理 (已有 0 个)

#### 可补充
- **himalaya**: IMAP/SMTP 邮件 CLI
  - 用途: 列表、阅读、撰写、回复、搜索邮件
  - 配合: 主 Agent 的邮件处理能力
  
- **gog**: Google Workspace CLI (含 Gmail)
  - 用途: Gmail + Calendar + Drive + Contacts + Sheets + Docs
  - 配合: 全套 Google 服务集成

---

### 5. 📅 日程与任务管理 (已有 0 个)

#### 可补充
- **apple-reminders**: Apple 提醒事项 (通过 remindctl)
  - 用途: 列表、添加、编辑、完成、删除提醒
  - 配合: 主 Agent 的日程管理

- **things-mac**: Things 3 任务管理
  - 用途: 添加/更新项目和待办,搜索任务
  - 配合: 专业的 GTD 任务管理

- **trello**: Trello 看板管理
  - 用途: 管理看板、列表、卡片
  - 配合: 团队项目管理

---

### 6. 🎨 图像与媒体 (已有 1 个)

#### 已安装
- ✅ **nano-banana-pro**: Gemini 图像生成

#### 可补充
- **openai-image-gen**: OpenAI 图像生成
  - 用途: 批量生成图像 + HTML 画廊
  - 配合: 与 nano-banana-pro 互补,提供不同风格

- **gifgrep**: GIF 搜索与下载
  - 用途: 搜索 GIF,下载,提取帧
  - 配合: Knowledge Weaver 的图文报告配图

- **video-frames**: 视频帧提取
  - 用途: 从视频提取帧或短片段
  - 配合: 媒体内容分析

- **songsee**: 音频频谱可视化
  - 用途: 生成频谱图和特征面板
  - 配合: 音频内容分析

---

### 7. 🔐 安全与密码 (已有 0 个)

#### 可补充
- **1password**: 1Password CLI
  - 用途: 读取/注入/运行密钥
  - 配合: Coder-Maintainer 的安全凭证管理

---

### 8. 🏠 智能家居 (已有 0 个)

#### 可补充
- **openhue**: Philips Hue 灯光控制
  - 用途: 控制灯光和场景
  - 配合: 主 Agent 的家居自动化

- **sonoscli**: Sonos 音响控制
  - 用途: 发现/状态/播放/音量/分组
  - 配合: 主 Agent 的音乐播放

- **eightctl**: Eight Sleep 床垫控制
  - 用途: 温度、闹钟、日程
  - 配合: 主 Agent 的睡眠管理

- **camsnap**: RTSP/ONVIF 摄像头
  - 用途: 捕获帧或视频片段
  - 配合: 主 Agent 的安全监控

---

### 9. 🎵 音乐与音频 (已有 0 个)

#### 可补充
- **spotify-player**: Spotify 终端播放器
  - 用途: 播放/搜索 Spotify
  - 配合: 主 Agent 的音乐控制

- **sag**: ElevenLabs TTS
  - 用途: 高质量语音合成
  - 配合: Knowledge Weaver 的语音内容生成

- **sherpa-onnx-tts**: 本地离线 TTS
  - 用途: 无需云端的语音合成
  - 配合: 隐私场景的语音生成

- **openai-whisper**: 本地语音转文字
  - 用途: 离线语音识别
  - 配合: Researcher 的音频内容分析

- **openai-whisper-api**: OpenAI Whisper API
  - 用途: 云端语音识别
  - 配合: 高质量语音转文字

---

### 10. 🛠️ 开发与运维 (已有 3 个)

#### 已安装
- ✅ **github**: GitHub CLI
- ✅ **auto-updater**: 自动更新
- ✅ **skill-vetter**: 技能审查

#### 可补充
- **gh-issues**: GitHub Issues 自动修复
  - 用途: 抓取 issues,生成 PR,监控评论
  - 配合: Coder-Maintainer 的自动化开发流程

- **session-logs**: 会话日志搜索
  - 用途: 搜索和分析历史对话
  - 配合: Self-improving 的反思分析

- **model-usage**: 模型使用统计
  - 用途: 汇总每个模型的使用和成本
  - 配合: 主 Agent 的成本监控

---

### 11. 🌐 Web 与 API (已有 1 个)

#### 已安装
- ✅ **api-gateway**: 100+ API 集成

#### 可补充
- **blogwatcher**: 博客/RSS 监控
  - 用途: 监控博客和 RSS/Atom 更新
  - 配合: Researcher 的信息订阅

---

### 12. 🖥️ 系统与 UI (已有 0 个)

#### 可补充
- **peekaboo**: macOS UI 自动化
  - 用途: 捕获和自动化 macOS UI
  - 配合: 主 Agent 的桌面自动化

- **canvas**: Canvas 技能
  - 用途: (需要查看详细文档)
  - 配合: 待定

---

### 13. 🤖 AI 模型 (已有 0 个)

#### 可补充
- **gemini**: Gemini CLI
  - 用途: 一次性问答、摘要、生成
  - 配合: 主 Agent 的多模型策略

- **oracle**: Prompt + 文件打包
  - 用途: 最佳实践的 prompt 工程
  - 配合: 所有 Agent 的 prompt 优化

---

### 14. 🎮 其他工具 (已有 0 个)

#### 可补充
- **ordercli**: Foodora 订单查询
  - 用途: 查看过往订单和活跃订单状态
  - 配合: 主 Agent 的生活服务

- **voice-call**: 语音通话
  - 用途: 启动语音通话
  - 配合: 主 Agent 的实时交互

---

## 🎯 推荐安装优先级

### 高优先级 (立即增强现有架构)

1. **himalaya** (邮件管理)
   - 补齐主 Agent 的邮件处理能力
   - 配合 HEARTBEAT 定期检查邮件

2. **apple-reminders** 或 **things-mac** (任务管理)
   - 主 Agent 需要日程和任务管理
   - 与 Cron 配合实现提醒功能

3. **1password** (密码管理)
   - Coder-Maintainer 需要安全的凭证管理
   - 避免明文存储 API keys

4. **gh-issues** (自动修复 Issues)
   - Coder-Maintainer 的自动化开发流程
   - 与 github skill 配合形成完整 CI/CD

5. **session-logs** (会话日志分析)
   - Self-improving 的反思分析基础
   - 帮助系统自我进化

### 中优先级 (增强特定场景)

6. **imsg** 或 **bluebubbles** (iMessage)
   - 主 Agent 的通讯能力
   - 跨设备消息同步

7. **sag** (ElevenLabs TTS)
   - Knowledge Weaver 的语音内容生成
   - 提升用户体验

8. **goplaces** (地点搜索)
   - Researcher 的地理信息研究
   - 补充搜索能力

9. **blogwatcher** (RSS 监控)
   - Researcher 的信息订阅
   - 被动信息收集

10. **openai-whisper** (语音识别)
    - Researcher 的音频内容分析
    - 多模态输入支持

### 低优先级 (特定需求)

11. **openhue** / **sonoscli** / **eightctl** (智能家居)
    - 仅在有对应设备时安装

12. **spotify-player** (音乐播放)
    - 娱乐功能,非核心需求

13. **trello** / **slack** / **discord** (团队协作)
    - 仅在使用对应平台时安装

---

## 🔄 与现有架构的配合方案

### 主 Agent (Orchestrator) 可增强

```
现有: proactive-agent, self-improving, api-gateway, weather
建议添加:
  - himalaya (邮件)
  - apple-reminders (任务)
  - imsg (消息)
  - model-usage (成本监控)
```

### 子 Agent 1 (Coder-Maintainer) 可增强

```
现有: auto-updater, skill-vetter, github
建议添加:
  - gh-issues (自动修复)
  - 1password (凭证管理)
  - session-logs (日志分析)
```

### 子 Agent 2 (Researcher) 可增强

```
现有: tavily-search, brave-search, agent-browser, summarize
建议添加:
  - goplaces (地点搜索)
  - blogwatcher (RSS 监控)
  - openai-whisper (音频转文字)
  - xurl (Twitter 监控)
```

### 子 Agent 3 (Knowledge-Weaver) 可增强

```
现有: obsidian, notion, nano-pdf, nano-banana-pro, humanizer
建议添加:
  - sag (语音合成)
  - gifgrep (GIF 配图)
  - apple-notes (临时笔记)
```

---

## 📝 下一步行动

1. **不安装,仅记录**: 本报告已完成
2. **待用户确认**: 是否安装推荐的高优先级 skills
3. **测试方案**: 先在测试环境验证,再部署到生产
4. **文档更新**: 安装后更新 AGENTS.md 和各 agent 配置

---

## 🔗 相关资源

- ClawHub 官网: https://clawhub.com
- OpenClaw 文档: https://docs.openclaw.ai
- GitHub 搜索: https://github.com/search?q=openclaw+skill
- 本地 Skills 路径: `~/.npm-global/lib/node_modules/openclaw/skills/`
