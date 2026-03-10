# 华为开发者控制台访问指南

## 📍 正确入口

### 方法 1: 直接访问控制台
**URL**: https://developer.huawei.com/consumer/cn/console

或者:
- https://developer.huawei.com/consumer/cn/service/josp/agc/index.html (AppGallery Connect)

### 方法 2: 从首页导航
1. 访问 https://developer.huawei.com
2. 右上角点击 **"登录"**
3. 登录后,右上角会出现 **"控制台"** 按钮
4. 点击进入

### 方法 3: 服务入口
1. https://developer.huawei.com
2. 顶部菜单 → **"服务"**
3. 选择 **"AppGallery Connect"** 或 **"HMS Core"**
4. 会自动跳转到控制台

## ⚠️ 常见问题

### 问题1: 找不到"控制台"按钮
**原因**: 未登录或未完成开发者认证

**解决**:
1. 确保已登录华为账号
2. 完成实名认证:
   - 个人中心 → 实名认证
   - 上传身份证照片
   - 等待审核 (通常几分钟)

### 问题2: 控制台页面空白
**原因**: 未创建任何应用

**解决**:
1. 点击 "我的项目" 或 "我的应用"
2. 创建第一个项目/应用

## 🎯 Health Kit 具体位置

创建应用后:
1. 控制台 → 我的项目 → 选择项目
2. 左侧菜单 → **"构建"** → **"Health Kit"**
3. 点击 "立即开通"
4. 申请数据权限

---

## 📱 Google Fit 详细方案

由于华为控制台可能比较复杂,我先给你 Google Fit 的完整流程。

### 前提条件
- Google 账号
- 安装 Google Fit App (Android)

### 第一步: 同步华为健康到 Google Fit

#### 选项 A: 使用第三方同步工具 (推荐)

**Health Sync** (最流行):
1. Google Play 下载 "Health Sync"
2. 打开 App,授权访问:
   - 华为健康
   - Google Fit
3. 选择要同步的数据类型:
   - 步数
   - 心率
   - 睡眠
   - 体重
4. 设置自动同步 (每小时/每天)

**FitToFit**:
- 类似 Health Sync
- 免费版功能有限

#### 选项 B: 手动导出导入
1. 华为健康导出数据
2. 使用工具转换格式
3. 导入 Google Fit

### 第二步: 创建 Google Cloud 项目

1. **访问 Google Cloud Console**
   - https://console.cloud.google.com

2. **创建新项目**
   - 点击顶部项目选择器
   - "新建项目"
   - 项目名称: "openclaw-health"

3. **启用 Fitness API**
   - 左侧菜单 → API 和服务 → 库
   - 搜索 "Fitness API"
   - 点击 "启用"

4. **创建 OAuth 凭据**
   - API 和服务 → 凭据
   - 创建凭据 → OAuth 客户端 ID
   - 应用类型: 桌面应用
   - 下载 JSON 文件

### 第三步: 安装 Google API 客户端

```bash
# 安装依赖
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# 创建 skill 目录
mkdir -p ~/.openclaw/workspace/skills/google-fit
cd ~/.openclaw/workspace/skills/google-fit
```

### 第四步: 创建认证脚本

```python
# auth.py - 首次认证
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read',
          'https://www.googleapis.com/auth/fitness.heart_rate.read',
          'https://www.googleapis.com/auth/fitness.sleep.read']

def authenticate():
    creds = None
    
    # 检查是否已有 token
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # 如果没有有效凭据,进行认证
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 保存凭据
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

if __name__ == '__main__':
    creds = authenticate()
    print("认证成功!")
```

### 第五步: 创建数据获取脚本

```python
# fetch_data.py - 获取健康数据
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pickle
import json

def get_fitness_service():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    return build('fitness', 'v1', credentials=creds)

def get_steps(service, days=7):
    """获取步数"""
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    
    dataset = f"{start_time}-{end_time}"
    
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

def get_heart_rate(service, days=7):
    """获取心率"""
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    
    dataset = f"{start_time}-{end_time}"
    
    response = service.users().dataSources().datasets().get(
        userId='me',
        dataSourceId='derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm',
        datasetId=dataset
    ).execute()
    
    heart_rate = []
    for point in response.get('point', []):
        heart_rate.append({
            'date': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
            'value': point['value'][0]['fpVal']
        })
    
    return heart_rate

def get_sleep(service, days=7):
    """获取睡眠"""
    end_time = int(datetime.now().timestamp() * 1000000000)
    start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000000000)
    
    dataset = f"{start_time}-{end_time}"
    
    response = service.users().dataSources().datasets().get(
        userId='me',
        dataSourceId='derived:com.google.sleep.segment:com.google.android.gms:merged',
        datasetId=dataset
    ).execute()
    
    sleep = []
    for point in response.get('point', []):
        sleep.append({
            'start': datetime.fromtimestamp(int(point['startTimeNanos']) / 1000000000).isoformat(),
            'end': datetime.fromtimestamp(int(point['endTimeNanos']) / 1000000000).isoformat(),
            'type': point['value'][0]['intVal']  # 1=awake, 2=sleep, 3=out-of-bed, 4=light, 5=deep, 6=REM
        })
    
    return sleep

def save_to_memory(data):
    """保存到 OpenClaw memory"""
    today = datetime.now().strftime("%Y-%m-%d")
    memory_file = f"~/.openclaw/workspace/memory/health-{today}.json"
    
    with open(os.path.expanduser(memory_file), 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"数据已保存到 {memory_file}")

if __name__ == '__main__':
    service = get_fitness_service()
    
    data = {
        'date': datetime.now().isoformat(),
        'steps': get_steps(service),
        'heart_rate': get_heart_rate(service),
        'sleep': get_sleep(service)
    }
    
    save_to_memory(data)
    print(f"获取数据成功:")
    print(f"- 步数: {len(data['steps'])} 条记录")
    print(f"- 心率: {len(data['heart_rate'])} 条记录")
    print(f"- 睡眠: {len(data['sleep'])} 条记录")
```

### 第六步: 创建 SKILL.md

```markdown
---
name: google-fit
description: Google Fit 健康数据同步
requires:
  - google-api-python-client
  - google-auth-httplib2
  - google-auth-oauthlib
---

# Google Fit Health Data Sync

## 首次使用

1. 认证:
   ```bash
   python3 auth.py
   ```
   会打开浏览器,登录 Google 账号授权

2. 获取数据:
   ```bash
   python3 fetch_data.py
   ```

## 自动化

设置 cron 每天同步:
```bash
0 8 * * * cd ~/.openclaw/workspace/skills/google-fit && python3 fetch_data.py
```
```

### 第七步: 使用流程

```bash
# 1. 放置 credentials.json (从 Google Cloud 下载的)
cp ~/Downloads/credentials.json ~/.openclaw/workspace/skills/google-fit/

# 2. 首次认证
cd ~/.openclaw/workspace/skills/google-fit
python3 auth.py
# 会打开浏览器,登录并授权

# 3. 测试获取数据
python3 fetch_data.py

# 4. 查看结果
cat ~/.openclaw/workspace/memory/health-$(date +%Y-%m-%d).json
```

---

## 🎯 总结对比

| 步骤 | 华为 API | Google Fit |
|------|----------|------------|
| 1. 注册开发者 | 华为开发者 (免费) | Google Cloud (免费) |
| 2. 创建项目 | 华为控制台 | Google Cloud Console |
| 3. 启用 API | Health Kit | Fitness API |
| 4. 数据同步 | 直接读取 | 需要先同步到 Google Fit |
| 5. 开发难度 | 中等 | 中等 |
| 6. 审核时间 | 1-3天 | 立即可用 |

**Google Fit 优势**:
- 无需审核,立即可用
- API 文档完善
- Python 库成熟

**华为 API 优势**:
- 数据直接来源
- 无需第三方同步
- 更实时

---

需要我:
1. **帮你创建 Google Fit skill** (立即可用)
2. **继续找华为控制台** (长期方案)
3. **两个都做** (并行)

选哪个?
