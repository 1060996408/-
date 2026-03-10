# Kiro Claude 模型稳定性测试报告

## 📊 测试结果 (2026-03-10 10:42)

| 模型 | 状态 | 响应 | 备注 |
|------|------|------|------|
| auto | ✅ 正常 | OK | 自动路由工作正常 |
| claude-opus-4.6 | ⚠️ 容量不足 | 429 Error | 高流量,暂时不可用 |
| claude-sonnet-4.6 | ⚠️ 容量不足 | 429 Error | 高流量,暂时不可用 |
| claude-opus-4.5 | ⚠️ 容量不足 | 429 Error | 高流量,暂时不可用 |
| claude-sonnet-4.5 | ✅ 正常 | OK | 稳定可用 |
| claude-sonnet-4 | ✅ 正常 | OK | 稳定可用 (默认) |
| claude-haiku-4.5 | ✅ 正常 | OK | 快速响应 |

## ✅ 可用模型 (4个)

1. **auto** - 自动选择 ✅
2. **claude-sonnet-4.5** - 稳定版 ✅
3. **claude-sonnet-4** - 当前默认 ✅
4. **claude-haiku-4.5** - 快速版 ✅

## ⚠️ 暂时不可用 (3个)

- claude-opus-4.6 (实验性)
- claude-sonnet-4.6 (实验性)
- claude-opus-4.5

**原因**: `INSUFFICIENT_MODEL_CAPACITY` - Kiro API 高流量

## 🎯 推荐使用

**日常使用**:
- `apiyi/claude-sonnet-4` (默认,稳定)
- `apiyi/claude-sonnet-4.5` (最新稳定版)

**快速响应**:
- `apiyi/claude-haiku-4.5`

**自动优化**:
- `apiyi/auto` (智能路由)

## 💡 快速切换模型

### 方法 1: 命令切换 (无需重启)
```
/model apiyi/claude-sonnet-4.5
/model apiyi/claude-haiku-4.5
/model apiyi/auto
```

### 方法 2: 修改默认模型 (需重启)
编辑配置:
```javascript
agents: {
  defaults: {
    model: {
      primary: 'apiyi/claude-sonnet-4.5'
    }
  }
}
```

**推荐**: 使用 `/model` 命令,即时生效,无需重启

## 📝 测试时间
2026-03-10 10:42 GMT+8
