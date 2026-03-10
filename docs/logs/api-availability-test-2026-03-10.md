# API 可用性测试报告 - 2026-03-10 11:59

## ✅ NewAPI (全部可用)

| 模型 | 状态 | Provider |
|------|------|----------|
| gpt-5 | ✅ 可用 | newapi |
| gpt-5-codex | ✅ 可用 | newapi |

**结论**: NewAPI 稳定,两个模型均正常工作

---

## 🔄 Kiro API (apiyi)

| 模型 | 状态 | 备注 |
|------|------|------|
| auto | ❌ 失败 | 连接问题 |
| claude-opus-4.6 | ⚠️ 容量不足 | 429 错误 |
| claude-sonnet-4.6 | ⚠️ 容量不足 | 429 错误 |
| claude-opus-4.5 | ⚠️ 容量不足 | 429 错误 |
| claude-sonnet-4.5 | ✅ 可用 | 正常 |
| claude-sonnet-4 | ✅ 可用 | 正常 |
| claude-haiku-4.5 | ✅ 可用 | 正常 |

**可用**: 3/7 (43%)
**容量不足**: 3/7 (43%)
**失败**: 1/7 (14%)

---

## 📊 总结

### 推荐使用 (5个模型)

**NewAPI** (稳定):
- `newapi/gpt-5` ✅
- `newapi/gpt-5-codex` ✅

**Kiro API** (部分可用):
- `apiyi/claude-sonnet-4.5` ✅
- `apiyi/claude-sonnet-4` ✅
- `apiyi/claude-haiku-4.5` ✅

### 暂时不可用 (4个模型)

- `apiyi/auto` - 连接失败
- `apiyi/claude-opus-4.6` - 容量不足
- `apiyi/claude-sonnet-4.6` - 容量不足
- `apiyi/claude-opus-4.5` - 容量不足

---

## 💡 使用建议

**日常使用**:
```
/model apiyi/claude-sonnet-4.5  (当前使用)
/model apiyi/claude-sonnet-4
```

**代码任务**:
```
/model newapi/gpt-5-codex
```

**快速响应**:
```
/model apiyi/claude-haiku-4.5
```

**通用任务**:
```
/model newapi/gpt-5
```

---

**测试时间**: 2026-03-10 11:59 GMT+8
**当前模型**: apiyi/claude-sonnet-4.5 ✅
