# 荣耀手表数据导入详细流程

## 方案 2: 华为官方 API (推荐长期方案)

### 📋 前置准备

1. **注册华为开发者账号**
   - 访问: https://developer.huawei.com
   - 注册并完成实名认证
   - 费用: 个人开发者免费

2. **创建应用**
   - 登录开发者联盟
   - 控制台 → 我的应用 → 创建应用
   - 填写应用信息 (名称、类型、包名等)

3. **申请健康服务权限**
   - 应用详情 → 服务 → Health Kit
   - 申请数据权限:
     - 步数 (STEP_COUNT)
     - 心率 (HEART_RATE)
     - 睡眠 (SLEEP)
     - 运动记录 (ACTIVITY)
     - 体重 (WEIGHT)
   - 提交审核 (通常 1-3 个工作日)

### 🔧 技术实现

#### 步骤 1: OAuth 认证

```python
# 1. 获取授权码
# 用户需要在华为账号登录页面授权
authorization_url = f"https://oauth-login.cloud.huawei.com/oauth2/v3/authorize"
params = {
    "client_id": "YOUR_CLIENT_ID",
    "redirect_uri": "YOUR_REDIRECT_URI",
    "response_type": "code",
    "scope": "https://www.huawei.com/healthkit/step.read https://www.huawei.com/healthkit/heartrate.read",
    "state": "random_state"
}

# 2. 用授权码换取 access_token
import requests
token_url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token"
data = {
    "grant_type": "authorization_code",
    "code": "AUTHORIZATION_CODE",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uri": "YOUR_REDIRECT_URI"
}
response = requests.post(token_url, data=data)
access_token = response.json()["access_token"]
```

#### 步骤 2: 获取健康数据

```python
# 获取步数数据
import requests
from datetime import datetime, timedelta

# API 端点
base_url = "https://health-api.cloud.huawei.com"

# 获取最近7天步数
end_time = int(datetime.now().timestamp() * 1000)
start_time = int((datetime.now() - timedelta(days=7)).timestamp() * 1000)

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# 步数数据
step_url = f"{base_url}/healthkit/v1/steps/query"
step_data = {
    "startTime": start_time,
    "endTime": end_time,
    "dataType": "DT_CONTINUOUS_STEPS_DELTA"
}
response = requests.post(step_url, json=step_data, headers=headers)
steps = response.json()

# 心率数据
heart_url = f"{base_url}/healthkit/v1/heartrate/query"
heart_data = {
    "startTime": start_time,
    "endTime": end_time,
    "dataType": "DT_INSTANTANEOUS_HEART_RATE"
}
response = requests.post(heart_url, json=heart_data, headers=headers)
heartrate = response.json()

# 睡眠数据
sleep_url = f"{base_url}/healthkit/v1/sleep/query"
sleep_data = {
    "startTime": start_time,
    "endTime": end_time,
    "dataType": "DT_SLEEP"
}
response = requests.post(sleep_url, json=sleep_data, headers=headers)
sleep = response.json()
```

#### 步骤 3: 创建 OpenClaw Skill

```bash
# 创建 skill 目录
mkdir -p ~/.openclaw/workspace/skills/huawei-health
cd ~/.openclaw/workspace/skills/huawei-health

# 创建配置文件
cat > _meta.json << 'EOF'
{
  "name": "huawei-health",
  "version": "1.0.0",
  "description": "华为健康数据同步",
  "author": "稼轩",
  "requires": {
    "env": ["HUAWEI_CLIENT_ID", "HUAWEI_CLIENT_SECRET", "HUAWEI_ACCESS_TOKEN"]
  }
}
EOF

# 创建主脚本
cat > sync.py << 'EOF'
#!/usr/bin/env python3
import os, requests, json
from datetime import datetime, timedelta

# 配置
CLIENT_ID = os.environ["HUAWEI_CLIENT_ID"]
CLIENT_SECRET = os.environ["HUAWEI_CLIENT_SECRET"]
ACCESS_TOKEN = os.environ["HUAWEI_ACCESS_TOKEN"]

# 获取数据
def fetch_health_data(days=7):
    base_url = "https://health-api.cloud.huawei.com"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    
    end_time = int(datetime.now().timestamp() * 1000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000)
    
    # 步数
    steps = requests.post(
        f"{base_url}/healthkit/v1/steps/query",
        json={"startTime": start_time, "endTime": end_time},
        headers=headers
    ).json()
    
    # 心率
    heartrate = requests.post(
        f"{base_url}/healthkit/v1/heartrate/query",
        json={"startTime": start_time, "endTime": end_time},
        headers=headers
    ).json()
    
    return {"steps": steps, "heartrate": heartrate}

# 保存到 memory
def save_to_memory(data):
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = f"~/.openclaw/workspace/memory/health-{today}.json"
    with open(os.path.expanduser(memory_file), "w") as f:
        json.dump(data, f, indent=2)
    print(f"数据已保存到 {memory_file}")

if __name__ == "__main__":
    data = fetch_health_data()
    save_to_memory(data)
EOF

chmod +x sync.py
```

#### 步骤 4: 设置定时同步

```bash
# 使用 OpenClaw cron
# 每天早上 8 点同步数据
openclaw cron add \
  --name "华为健康数据同步" \
  --schedule "0 8 * * *" \
  --command "cd ~/.openclaw/workspace/skills/huawei-health && python3 sync.py"
```

### 📝 配置环境变量

```bash
# 添加到 ~/.openclaw/openclaw.json
{
  "env": {
    "vars": {
      "HUAWEI_CLIENT_ID": "你的应用ID",
      "HUAWEI_CLIENT_SECRET": "你的应用密钥",
      "HUAWEI_ACCESS_TOKEN": "初始token (会自动刷新)"
    }
  }
}
```

---

## 方案 3: 第三方健康数据平台

### 选项 A: Apple Health (如果有 iPhone)

#### 步骤 1: 同步华为健康到 Apple Health

1. **安装华为健康 App (iOS)**
   - App Store 搜索 "华为健康"
   - 登录华为账号

2. **启用数据同步**
   - 华为健康 → 设置 → 数据共享
   - 开启 "同步到 Apple Health"
   - 选择要同步的数据类型

3. **验证同步**
   - 打开 iPhone 健康 App
   - 查看数据是否出现

#### 步骤 2: 导出 Apple Health 数据

```bash
# 方法 1: 手动导出
# iPhone 健康 App → 个人资料 → 导出健康数据
# 会生成 export.zip 文件

# 方法 2: 使用 HealthKit API (需要 Mac + Xcode)
# 创建 iOS App 读取 HealthKit 数据
```

#### 步骤 3: 解析并导入 OpenClaw

```python
#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import json
from datetime import datetime

def parse_apple_health_export(xml_file):
    """解析 Apple Health 导出的 XML"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = {
        "steps": [],
        "heartrate": [],
        "sleep": []
    }
    
    for record in root.findall('.//Record'):
        record_type = record.get('type')
        
        if 'StepCount' in record_type:
            data["steps"].append({
                "date": record.get('startDate'),
                "value": int(record.get('value'))
            })
        
        elif 'HeartRate' in record_type:
            data["heartrate"].append({
                "date": record.get('startDate'),
                "value": int(record.get('value'))
            })
        
        elif 'SleepAnalysis' in record_type:
            data["sleep"].append({
                "start": record.get('startDate'),
                "end": record.get('endDate'),
                "value": record.get('value')
            })
    
    return data

# 使用
data = parse_apple_health_export('export.xml')
with open('health-data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### 选项 B: Google Fit

#### 步骤 1: 同步到 Google Fit

1. **安装 Google Fit App**
   - 登录 Google 账号

2. **连接华为健康**
   - Google Fit → 设置 → 已连接的应用
   - 添加华为健康 (如果支持)
   - 或使用第三方同步工具: Health Sync, FitToFit

#### 步骤 2: 使用 Google Fit API

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# OAuth 认证 (需要先在 Google Cloud Console 创建项目)
creds = Credentials.from_authorized_user_file('token.json')
service = build('fitness', 'v1', credentials=creds)

# 获取步数
end_time = int(datetime.now().timestamp() * 1000000000)
start_time = int((datetime.now() - timedelta(days=7)).timestamp() * 1000000000)

dataset = f"{start_time}-{end_time}"
response = service.users().dataSources().datasets().get(
    userId='me',
    dataSourceId='derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
    datasetId=dataset
).execute()

steps = response.get('point', [])
```

### 选项 C: Zepp Life (小米生态)

1. **安装 Zepp Life App**
2. **添加华为健康数据源** (如果支持)
3. **使用 Zepp API** (需要申请开发者权限)

---

## 🎯 推荐路径

### 短期 (1-2天)
**方案 3A: Apple Health** (如果有 iPhone)
- 最简单,无需开发者认证
- 华为健康 → Apple Health → 导出 → OpenClaw

### 中期 (1-2周)
**方案 2: 华为官方 API**
- 申请开发者账号
- 创建应用,获取权限
- 实现自动同步

### 对比

| 方案 | 难度 | 时间 | 实时性 | 稳定性 |
|------|------|------|--------|--------|
| 华为 API | 中 | 1-2周 | 实时 | ⭐⭐⭐⭐⭐ |
| Apple Health | 低 | 1-2天 | 延迟 | ⭐⭐⭐⭐ |
| Google Fit | 中 | 3-5天 | 延迟 | ⭐⭐⭐ |

---

需要我帮你:
1. **开始申请华为开发者账号** (方案2)
2. **设置 Apple Health 同步** (方案3A)
3. **创建 health-data skill 框架**

选哪个?
