#!/bin/bash
# Google Fit 快速启动脚本

echo "=== Google Fit Health Data Sync - 快速启动 ==="
echo

# 步骤 1: 安装依赖
echo "步骤 1: 安装 Python 依赖..."
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# 步骤 2: 创建目录
echo "步骤 2: 创建 skill 目录..."
mkdir -p ~/.openclaw/workspace/skills/google-fit
cd ~/.openclaw/workspace/skills/google-fit

# 步骤 3: 创建认证脚本
echo "步骤 3: 创建认证脚本..."
cat > auth.py << 'PYEOF'
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

SCOPES = [
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.heart_rate.read',
    'https://www.googleapis.com/auth/fitness.sleep.read',
    'https://www.googleapis.com/auth/fitness.body.read'
]

def authenticate():
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

if __name__ == '__main__':
    creds = authenticate()
    print("✅ 认证成功!")
PYEOF

# 步骤 4: 创建数据获取脚本
echo "步骤 4: 创建数据获取脚本..."
cat > fetch_data.py << 'PYEOF'
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pickle
import json
import os

def get_fitness_service():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    return build('fitness', 'v1', credentials=creds)

def get_steps(service, days=7):
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    dataset = f"{start_time}-{end_time}"
    
    try:
        response = service.users().dataSources().datasets().get(
            userId='me',
            dataSourceId='derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
            datasetId=dataset
        ).execute()
        
        steps = []
        for point in response.get('point', []):
            steps.append({
                'date': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
                'value': point['value'][0]['intVal']
            })
        return steps
    except Exception as e:
        print(f"获取步数失败: {e}")
        return []

def get_heart_rate(service, days=7):
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    dataset = f"{start_time}-{end_time}"
    
    try:
        response = service.users().dataSources().datasets().get(
            userId='me',
            dataSourceId='derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm',
            datasetId=dataset
        ).execute()
        
        heart_rate = []
        for point in response.get('point', []):
            heart_rate.append({
                'date': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
                'value': round(point['value'][0]['fpVal'], 1)
            })
        return heart_rate
    except Exception as e:
        print(f"获取心率失败: {e}")
        return []

def save_to_memory(data):
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = os.path.expanduser(f"~/.openclaw/workspace/memory/health-{today}.json")
    
    with open(memory_file, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 数据已保存到 {memory_file}")

if __name__ == '__main__':
    service = get_fitness_service()
    
    print("正在获取健康数据...")
    data = {
        'date': datetime.now().isoformat(),
        'source': 'google-fit',
        'steps': get_steps(service),
        'heart_rate': get_heart_rate(service)
    }
    
    save_to_memory(data)
    print(f"\n📊 数据统计:")
    print(f"  步数记录: {len(data['steps'])} 条")
    print(f"  心率记录: {len(data['heart_rate'])} 条")
PYEOF

# 步骤 5: 创建 SKILL.md
cat > SKILL.md << 'EOF'
---
name: google-fit
description: Google Fit 健康数据同步到 OpenClaw
requires:
  - google-api-python-client
  - google-auth-httplib2
  - google-auth-oauthlib
---

# Google Fit Health Sync

## 使用步骤

1. 首次认证:
   ```bash
   python3 auth.py
   ```

2. 获取数据:
   ```bash
   python3 fetch_data.py
   ```

3. 查看结果:
   ```bash
   cat ~/.openclaw/workspace/memory/health-$(date +%Y-%m-%d).json
   ```

## 自动化

每天早上 8 点同步:
```bash
0 8 * * * cd ~/.openclaw/workspace/skills/google-fit && python3 fetch_data.py
```
EOF

cat > _meta.json << 'EOF'
{
  "name": "google-fit",
  "version": "1.0.0",
  "description": "Google Fit 健康数据同步",
  "author": "稼轩"
}
EOF

echo
echo "✅ Google Fit skill 创建完成!"
echo
echo "📋 下一步操作:"
echo "1. 访问 https://console.cloud.google.com"
echo "2. 创建项目 → 启用 Fitness API → 创建 OAuth 凭据"
echo "3. 下载 credentials.json 到当前目录"
echo "4. 运行: python3 auth.py"
echo
