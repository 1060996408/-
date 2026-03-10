---
name: huawei-health
description: 华为健康数据手动导入解析器
---

# 华为健康数据导入

## 📱 导出数据 (手机操作)

1. 打开 **华为健康** App
2. 我的 → 右上角设置图标
3. 数据管理 → 导出数据
4. 选择数据类型:
   - ✅ 步数
   - ✅ 心率
   - ✅ 睡眠
   - ✅ 体重
5. 选择时间范围 (建议最近 30 天)
6. 导出格式: CSV 或 JSON
7. 保存到手机

## 💻 传输到电脑

### 方法 1: USB 连接
```bash
# 连接手机,复制文件到电脑
cp /path/to/phone/health_data.csv ~/.openclaw/workspace/skills/huawei-health/
```

### 方法 2: 微信/邮件
- 通过微信文件传输助手发送到电脑
- 或发送到自己邮箱,电脑下载

### 方法 3: 云盘
- 上传到华为云盘/百度网盘
- 电脑端下载

## 🔧 解析导入

```bash
# 进入 skill 目录
cd ~/.openclaw/workspace/skills/huawei-health

# 解析 CSV 文件
python3 parse_huawei.py ~/Downloads/health_data.csv

# 或解析 JSON 文件
python3 parse_huawei.py ~/Downloads/health_data.json
```

## 📊 查看结果

```bash
# 查看今天的健康数据
cat ~/.openclaw/workspace/memory/health-$(date +%Y-%m-%d).json
```

## 🤖 自动化

### 设置定期提醒

```bash
# 每周日晚上 8 点提醒导出数据
openclaw cron add \
  --name "提醒导出华为健康数据" \
  --schedule "0 20 * * 0" \
  --payload '{"kind":"systemEvent","text":"📱 该导出本周的华为健康数据了!"}'
```

### 快速导入脚本

```bash
# 创建快捷命令
cat >> ~/.bashrc << 'EOF'
alias import-health='python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py'
EOF

source ~/.bashrc

# 使用
import-health ~/Downloads/health_data.csv
```

## 📝 数据格式

导入后的数据格式:
```json
{
  "date": "2026-03-10T18:25:00",
  "source": "huawei-manual",
  "data": {
    "steps": [
      {"date": "2026-03-10", "value": 8234}
    ],
    "heart_rate": [
      {"date": "2026-03-10T08:30:00", "value": 72}
    ],
    "sleep": [
      {"date": "2026-03-09", "duration": "7h 32m", "quality": "良好"}
    ],
    "weight": [
      {"date": "2026-03-10", "value": 70.5}
    ]
  }
}
```

## 🎯 优势

- ✅ 无需 API 审核
- ✅ 立即可用
- ✅ 数据完整
- ✅ 简单可靠

## ⏱️ 时间投入

- 首次导出: 5 分钟
- 传输到电脑: 2 分钟
- 解析导入: 1 分钟
- **总计: 8 分钟**

每周重复一次即可。
