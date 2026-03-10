# 华为健康数据导入 - 快速开始

## 🎯 方案对比

| 方案 | 时间 | 难度 | 实时性 | 推荐度 |
|------|------|------|--------|--------|
| **手动导出** | 8分钟 | ⭐ 简单 | 每周 | 🟢 立即可用 |
| Google Fit | 20分钟 | ⭐⭐ 中等 | 每天 | 🟡 需要同步 |
| 华为 API | 1-3天 | ⭐⭐⭐ 复杂 | 实时 | 🔴 需要审核 |

**推荐**: 先用手动导出,简单可靠!

---

## 📱 第 1 步: 导出数据 (5分钟)

### 在手机上操作

1. 打开 **华为健康** App
2. 点击右下角 **"我的"**
3. 右上角 **设置图标** (齿轮)
4. **数据管理** → **导出数据**
5. 选择数据类型:
   - ✅ 步数
   - ✅ 心率  
   - ✅ 睡眠
   - ✅ 体重
6. 时间范围: **最近 30 天**
7. 格式: **CSV** (推荐) 或 JSON
8. 点击 **导出**
9. 保存到手机

---

## 💻 第 2 步: 传输到电脑 (2分钟)

### 方法 A: 微信传输 (最快)

1. 手机微信 → 文件传输助手
2. 发送导出的文件
3. 电脑微信接收
4. 保存到 `~/Downloads/`

### 方法 B: USB 连接

```bash
# 连接手机,找到导出文件
# 通常在: /sdcard/Huawei/Health/export/

# 复制到电脑
cp /path/to/phone/health_data.csv ~/Downloads/
```

### 方法C: 邮件

1. 手机上将文件发送到自己邮箱
2. 电脑打开邮箱下载

---

## 🔧 第 3 步: 导入 OpenClaw (1分钟)

```bash
# 解析并导入数据
python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py ~/Downloads/health_data.csv

# 查看结果
cat ~/.openclaw/workspace/memory/health-$(date +%Y-%m-%d).json
```

**输出示例**:
```
📂 正在解析: /home/user/Downloads/health_data.csv

📊 数据统计:
  步数记录: 30 条
  心率记录: 120 条
  睡眠记录: 30 条
  体重记录: 5 条

✅ 数据已保存到: ~/.openclaw/workspace/memory/health-2026-03-10.json
✅ 导入完成!
```

---

## 🤖 第 4 步: 设置自动提醒 (可选)

### 每周提醒导出

```bash
# 每周日晚上 8 点提醒
openclaw cron add \
  --name "提醒导出华为健康数据" \
  --schedule "0 20 * * 0" \
  --payload '{"kind":"systemEvent","text":"📱 该导出本周的华为健康数据了!\n\n步骤:\n1. 打开华为健康 App\n2. 我的 → 设置 → 数据管理 → 导出数据\n3. 选择最近 7 天\n4. 微信发送到电脑\n5. 运行: import-health ~/Downloads/health_data.csv"}'
```

### 创建快捷命令

```bash
# 添加到 ~/.bashrc
echo "alias import-health='python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py'" >> ~/.bashrc
source ~/.bashrc

# 以后只需要
import-health ~/Downloads/health_data.csv
```

---

## 📊 数据分析示例

创建分析脚本:

```python
#!/usr/bin/env python3
# analyze_health.py - 健康数据分析

import json
from glob import glob
from datetime import datetime

def analyze():
    files = glob(os.path.expanduser("~/.openclaw/workspace/memory/health-*.json"))
    
    total_steps = 0
    heart_rates = []
    sleep_hours = []
    
    for file in files:
        with open(file) as f:
            data = json.load(f)
            
            # 统计步数
            for step in data.get('data', {}).get('steps', []):
                total_steps += step['value']
            
            # 统计心率
            for hr in data.get('data', {}).get('heart_rate', []):
                heart_rates.append(hr['value'])
            
            # 统计睡眠
            for sleep in data.get('data', {}).get('sleep', []):
                duration = sleep.get('duration', '0h 0m')
                # 解析时长...
    
    print(f"📊 健康数据分析:")
    print(f"  总步数: {total_steps:,}")
    print(f"  平均心率: {sum(heart_rates)/len(heart_rates):.1f} bpm")
    print(f"  数据天数: {len(files)}")

if __name__ == '__main__':
    analyze()
```

---

## 🎯 使用流程总结

### 首次设置 (8分钟)
1. 手机导出数据 (5分钟)
2. 传输到电脑 (2分钟)
3. 运行导入脚本 (1分钟)

### 日常使用 (每周 8分钟)
1. 周日晚上收到提醒
2. 手机导出本周数据
3. 微信发送到电脑
4. 运行 `import-health ~/Downloads/health_data.csv`

### 自动化
- ✅ 每周自动提醒
- ✅ 一键导入命令
- ✅ 数据自动保存到 memory/
- ✅ 可以设置分析脚本定期运行

---

## 💡 优势

1. **无需 API** - 不用等审核
2. **立即可用** - 现在就能开始
3. **数据完整** - 导出所有历史数据
4. **简单可靠** - 不依赖第三方服务
5. **隐私安全** - 数据完全本地

---

## 🚀 现在就开始!

```bash
# 1. 打开手机华为健康 App
# 2. 导出数据
# 3. 微信发送到电脑
# 4. 运行导入

python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py ~/Downloads/health_data.csv
```

---

需要我:
1. **帮你测试导入脚本** (用示例数据)
2. **创建数据分析脚本** (自动生成健康报告)
3. **设置提醒 cron** (每周自动提醒)

选哪个?
