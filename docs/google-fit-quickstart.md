# Google Fit 快速启动指南

## 🚀 一键安装

```bash
bash ~/.openclaw/workspace/scripts/setup-google-fit.sh
```

这个脚本会自动:
- 安装 Python 依赖
- 创建 skill 目录和文件
- 生成认证和数据获取脚本

---

## 📋 完整流程 (3步)

### 第 1 步: 创建 Google Cloud 项目 (10分钟)

1. **访问 Google Cloud Console**
   ```
   https://console.cloud.google.com
   ```

2. **创建新项目**
   - 点击顶部项目选择器
   - "新建项目"
   - 项目名称: `openclaw-health`
   - 点击 "创建"

3. **启用 Fitness API**
   - 左侧菜单 → "API 和服务" → "库"
   - 搜索 "Fitness API"
   - 点击 "启用"

4. **创建 OAuth 凭据**
   - "API 和服务" → "凭据"
   - "创建凭据" → "OAuth 客户端 ID"
   - 应用类型: **"桌面应用"**
   - 名称: `openclaw-desktop`
   - 点击 "创建"

5. **下载凭据**
   - 点击下载按钮 (JSON 图标)
   - 保存为 `credentials.json`
   - 移动到 skill 目录:
     ```bash
     mv ~/Downloads/credentials.json ~/.openclaw/workspace/skills/google-fit/
     ```

### 第 2 步: 同步华为健康到 Google Fit (5分钟)

#### 选项 A: 使用 Health Sync App (推荐)

1. **下载 Health Sync**
   - Google Play 搜索 "Health Sync"
   - 安装并打开

2. **配置同步**
   - 授权访问华为健康
   - 授权访问 Google Fit
   - 选择数据类型:
     - ✅ 步数
     - ✅ 心率
     - ✅ 睡眠
     - ✅ 体重

3. **设置自动同步**
   - 同步频率: 每小时
   - 开启后台同步

4. **手动同步一次**
   - 点击 "立即同步"
   - 等待完成

#### 选项 B: 手动方式

如果没有 Android 手机:
1. 华为健康 App 导出数据
2. 使用转换工具导入 Google Fit
3. (较复杂,不推荐)

### 第 3 步: 运行 OpenClaw Skill (5分钟)

```bash
# 1. 进入 skill 目录
cd ~/.openclaw/workspace/skills/google-fit

# 2. 首次认证
python3 auth.py
# 会打开浏览器,登录 Google 账号并授权

# 3. 获取数据
python3 fetch_data.py

# 4. 查看结果
cat ~/.openclaw/workspace/memory/health-$(date +%Y-%m-%d).json
```

---

## 📊 数据格式示例

```json
{
  "date": "2026-03-10T18:00:00",
  "source": "google-fit",
  "steps": [
    {
      "date": "2026-03-10T08:00:00",
      "value": 1234
    },
    {
      "date": "2026-03-10T09:00:00",
      "value": 2345
    }
  ],
  "heart_rate": [
    {
      "date": "2026-03-10T08:30:00",
      "value": 72.5
    },
    {
      "date": "2026-03-10T09:30:00",
      "value": 68.3
    }
  ]
}
```

---

## 🤖 设置自动化

### 方法 1: OpenClaw Cron (推荐)

```bash
# 每天早上 8 点同步
openclaw cron add \
  --name "Google Fit 健康数据同步" \
  --schedule "0 8 * * *" \
  --command "cd ~/.openclaw/workspace/skills/google-fit && python3 fetch_data.py"
```

### 方法 2: 系统 Cron

```bash
# 编辑 crontab
crontab -e

# 添加这行
0 8 * * * cd ~/.openclaw/workspace/skills/google-fit && python3 fetch_data.py
```

---

## 🔧 故障排查

### 问题 1: 认证失败

**错误**: `Error: invalid_client`

**解决**:
- 确保 `credentials.json` 在正确位置
- 检查 OAuth 客户端类型是 "桌面应用"

### 问题 2: 没有数据

**错误**: `步数记录: 0 条`

**原因**: Google Fit 中没有数据

**解决**:
1. 检查 Health Sync 是否同步成功
2. 打开 Google Fit App 查看数据
3. 手动添加一些测试数据

### 问题 3: Token 过期

**错误**: `Token has been expired or revoked`

**解决**:
```bash
# 删除旧 token,重新认证
rm ~/.openclaw/workspace/skills/google-fit/token.pickle
python3 auth.py
```

---

## 📈 下一步: 数据分析

创建分析脚本:

```python
# analyze.py - 健康数据分析
import json
from datetime import datetime
from glob import glob

def analyze_health_data():
    # 读取所有健康数据文件
    files = glob(os.path.expanduser("~/.openclaw/workspace/memory/health-*.json"))
    
    total_steps = 0
    avg_heart_rate = []
    
    for file in files:
        with open(file) as f:
            data = json.load(f)
            
            # 统计步数
            for step in data.get('steps', []):
                total_steps += step['value']
            
            # 统计心率
            for hr in data.get('heart_rate', []):
                avg_heart_rate.append(hr['value'])
    
    print(f"📊 健康数据分析:")
    print(f"  总步数: {total_steps:,}")
    print(f"  平均心率: {sum(avg_heart_rate)/len(avg_heart_rate):.1f} bpm")
    print(f"  数据天数: {len(files)}")

if __name__ == '__main__':
    analyze_health_data()
```

---

## 🎯 总结

### 时间投入
- Google Cloud 设置: 10 分钟
- Health Sync 配置: 5 分钟
- OpenClaw Skill 运行: 5 分钟
- **总计: 20 分钟**

### 后续维护
- 自动同步: 无需操作
- 数据获取: 每天自动
- Token 刷新: 自动处理

### 优势
- ✅ 快速启动 (20分钟)
- ✅ 无需审核
- ✅ 自动同步
- ✅ 数据完整

---

需要我:
1. **帮你运行安装脚本** (现在就做)
2. **指导 Google Cloud 设置** (截图说明)
3. **测试数据获取** (验证流程)

选哪个?
