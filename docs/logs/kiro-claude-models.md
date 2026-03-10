# Kiro Claude 模型配置

## 📋 可用模型 (7个)

### 1. auto
- **名称**: Auto (Models chosen by task)
- **说明**: 根据任务自动选择最优模型
- **Context**: 200K tokens
- **用途**: 智能路由,自动优化

### 2. claude-opus-4.6 (实验性)
- **名称**: Claude Opus 4.6 (Experimental)
- **说明**: 最新 Opus 实验预览版
- **Context**: 200K tokens
- **用途**: 复杂推理,高难度任务

### 3. claude-sonnet-4.6 (实验性)
- **名称**: Claude Sonnet 4.6 (Experimental)
- **说明**: 最新 Sonnet 实验预览版
- **Context**: 200K tokens
- **用途**: 平衡性能与速度

### 4. claude-opus-4.5
- **名称**: Claude Opus 4.5
- **说明**: 稳定版 Opus 4.5
- **Context**: 200K tokens
- **用途**: 高质量输出,深度分析

### 5. claude-sonnet-4.5
- **名称**: Claude Sonnet 4.5
- **说明**: 稳定版 Sonnet 4.5
- **Context**: 200K tokens
- **用途**: 日常使用,性价比高

### 6. claude-sonnet-4 (当前默认)
- **名称**: Claude Sonnet 4
- **说明**: 混合推理与编码
- **Context**: 200K tokens
- **用途**: 常规使用,编码任务

### 7. claude-haiku-4.5
- **名称**: Claude Haiku 4.5
- **说明**: 最新 Haiku 模型
- **Context**: 200K tokens
- **用途**: 快速响应,简单任务

## 🎯 使用方式

切换模型:
```
/model apiyi/auto
/model apiyi/claude-opus-4.6
/model apiyi/claude-sonnet-4.6
/model apiyi/claude-opus-4.5
/model apiyi/claude-sonnet-4.5
/model apiyi/claude-sonnet-4
/model apiyi/claude-haiku-4.5
```

## 📊 模型选择建议

- **复杂推理**: claude-opus-4.6 / claude-opus-4.5
- **日常使用**: claude-sonnet-4.5 / claude-sonnet-4 (默认)
- **快速响应**: claude-haiku-4.5
- **自动优化**: auto
- **实验功能**: claude-opus-4.6 / claude-sonnet-4.6

## ✅ 配置状态

- **Provider**: apiyi (Kiro Proxy)
- **Base URL**: http://127.0.0.1:13000
- **API**: anthropic-messages
- **状态**: 已配置并重启生效 (PID 28858)
