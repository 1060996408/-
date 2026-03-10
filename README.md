# Workspace 目录结构

```
workspace/
├── AGENTS.md              # Agent 系统说明
├── AGENTS_ARCHITECTURE.md # Agent 架构设计
├── BOOTSTRAP.md           # 初始化引导
├── HEARTBEAT.md           # 心跳检查配置
├── IDENTITY.md            # 身份信息
├── SOUL.md                # 行为准则
├── TOOLS.md               # 工具配置
├── USER.md                # 用户信息
│
├── agents/                # Agent 配置目录
├── memory/                # 记忆文件 (日志)
├── skills/                # 技能目录
├── scripts/               # 脚本目录
├── workflows/             # 工作流目录
│
└── docs/                  # 文档目录
    ├── README.md          # 文档说明
    ├── reports/           # 分析报告
    ├── logs/              # 工作日志
    └── archive/           # 历史归档
```

## 核心文件 (根目录)
- **AGENTS.md** - Agent 系统使用指南
- **SOUL.md** - 输出规则与行为准则
- **USER.md** - 用户信息与偏好

## 文档分类
- **docs/reports/** - 系统分析、技能评估报告
- **docs/logs/** - 每日工作日志、问题清单
- **docs/archive/** - 已完成的临时文档

## 记忆系统
- **memory/** - 按日期组织的记忆文件
- **MEMORY.md** - 长期记忆 (主会话专用)
