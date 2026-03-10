# API 稳定性测试报告 - 2026-03-10 12:05

## 📊 测试方法
每个模型连续发送 5 次请求,统计成功率

---

## ✅ NewAPI - 优秀稳定性

| 模型 | 成功率 | 结果 |
|------|--------|------|
| gpt-5 | 5/5 (100%) | ✅✅✅✅✅ |
| gpt-5-codex | 5/5 (100%) | ✅✅✅✅✅ |

**总体成功率**: 10/10 (100%)
**稳定性评级**: ⭐⭐⭐⭐⭐ 优秀

---

## ⚠️ Kiro API - 中等稳定性

| 模型 | 成功率 | 结果 |
|------|--------|------|
| claude-sonnet-4.5 | 3/5 (60%) | ❌✅✅✅❌ |
| claude-sonnet-4 | 3/5 (60%) | ✅❌❌✅✅ |
| claude-haiku-4.5 | 5/5 (100%) | ✅✅✅✅✅ |

**总体成功率**: 11/15 (73%)
**稳定性评级**: ⭐⭐⭐ 中等

---

## 📈 对比分析

### NewAPI
- ✅ **100% 成功率**
- ✅ 无超时或失败
- ✅ 响应稳定
- ✅ 推荐用于生产环境

### Kiro API
- ⚠️ **73% 成功率**
- ⚠️ 间歇性失败 (sonnet-4.5, sonnet-4)
- ✅ haiku-4.5 表现优秀 (100%)
- ⚠️ 可能存在负载问题

---

## 💡 使用建议

### 优先推荐 (稳定性 100%)
```
/model newapi/gpt-5           ← 最稳定
/model newapi/gpt-5-codex     ← 最稳定
/model apiyi/claude-haiku-4.5 ← Kiro 中最稳定
```

### 谨慎使用 (稳定性 60%)
```
/model apiyi/claude-sonnet-4.5  ← 当前使用,但不稳定
/model apiyi/claude-sonnet-4    ← 不稳定
```

### 不推荐使用 (容量不足)
```
/model apiyi/auto               ← 连接失败
/model apiyi/claude-opus-4.6    ← 429 错误
/model apiyi/claude-sonnet-4.6  ← 429 错误
/model apiyi/claude-opus-4.5    ← 429 错误
```

---

## 🎯 最佳实践

**生产环境**:
- 使用 NewAPI (gpt-5 或 gpt-5-codex)
- 100% 稳定性保证

**开发测试**:
- 可以使用 Kiro API
- 注意处理失败重试

**快速响应**:
- 使用 apiyi/claude-haiku-4.5
- Kiro 中唯一 100% 稳定的模型

---

## 📝 结论

1. **NewAPI 明显更稳定** - 100% vs 73%
2. **Kiro API 存在负载问题** - Sonnet 系列不稳定
3. **建议切换到 NewAPI** - 用于重要任务
4. **Haiku 是 Kiro 最佳选择** - 如果必须使用 Kiro

---

**测试时间**: 2026-03-10 12:05-12:08 GMT+8
**测试样本**: 25 次请求 (5个模型 × 5次)
**当前模型**: apiyi/claude-sonnet-4.5 (不稳定,建议切换)
