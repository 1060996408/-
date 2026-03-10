# Health Sync 自动化方案

## 🎯 方案概述

通过 Health Sync 将华为健康数据自动同步到 Google Drive,然后 OpenClaw 自动读取。

---

## 📱 第一步: 配置 Health Sync

### 1. 安装 Health Sync

- Google Play: https://play.google.com/store/apps/details?id=nl.appyhapps.healthsync
- 或第三方市场搜索 "Health Sync"

### 2. 配置数据源

```
Health Sync App
→ 添加同步
→ 数据源: Huawei Health
→ 目标: Google Drive
→ 授权访问
```

### 3. 设置同步选项

```
同步频率: 每天 (或每小时)
数据类型:
  ✅ 步数
  ✅ 心率
  ✅ 睡眠
  ✅ 体重
  ✅ 运动记录

导出格式: CSV (推荐)
保存位置: Google Drive/HealthSync/
```

### 4. 测试同步

- 点击 "立即同步"
- 检查 Google Drive 是否有文件
- 确认数据格式正确

---

## 💻 第二步: OpenClaw 自动读取

### 方案 A: Google Drive API (推荐)

#### 1. 创建 Google Cloud 项目

```
1. 访问 https://console.cloud.google.com
2. 创建项目: openclaw-health
3. 启用 Google Drive API
4. 创建 OAuth 凭据 (桌面应用)
5. 下载 credentials.json
```

#### 2. 创建自动同步脚本

```python
#!/usr/bin/env python3
# sync_from_drive.py - 从 Google Drive 自动下载健康数据

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_NAME = 'HealthSync'

def authenticate():
    """Google Drive 认证"""
    creds = None
    token_file = 'drive_token.pickle'
    
    if os.path.exists(token_file):
        import pickle
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        import pickle
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def find_health_folder(service):
    """查找 HealthSync 文件夹"""
    results = service.files().list(
        q=f"name='{FOLDER_NAME}' and mimeType='application/vnd.google-apps.folder'",
        fields="files(id, name)"
    ).execute()
    
    folders = results.get('files', [])
    return folders[0]['id'] if folders else None

def get_recent_files(service, folder_id, days=7):
    """获取最近 N 天的文件"""
    date_filter = (datetime.now() - timedelta(days=days)).isoformat()
    
    query = f"'{folder_id}' in parents and modifiedTime > '{date_filter}' and trashed=false"
    
    results = service.files().list(
        q=query,
        fields="files(id, name, modifiedTime)",
        orderBy="modifiedTime desc"
    ).execute()
    
    return results.get('files', [])

def download_file(service, file_id, file_name, dest_dir):
    """下载文件"""
    request = service.files().get_media(fileId=file_id)
    
    dest_path = os.path.join(dest_dir, file_name)
    
    with io.FileIO(dest_path, 'wb') as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    
    return dest_path

def main():
    print("🔄 正在从 Google Drive 同步健康数据...")
    
    # 认证
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    # 查找文件夹
    folder_id = find_health_folder(service)
    if not folder_id:
        print(f"❌ 未找到 {FOLDER_NAME} 文件夹")
        return
    
    # 获取最近文件
    files = get_recent_files(service, folder_id, days=7)
    
    if not files:
        print("ℹ️ 没有新的健康数据文件")
        return
    
    print(f"📥 找到 {len(files)} 个文件")
    
    # 下载目录
    download_dir = os.path.expanduser("~/.openclaw/workspace/skills/huawei-health/downloads")
    os.makedirs(download_dir, exist_ok=True)
    
    # 下载并解析
    for file in files:
        print(f"  下载: {file['name']}")
        local_path = download_file(service, file['id'], file['name'], download_dir)
        
        # 调用解析脚本
        if local_path.endswith('.csv'):
            os.system(f"python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py {local_path}")
    
    print("✅ 同步完成!")

if __name__ == '__main__':
    main()
```

#### 3. 设置自动运行

```bash
# 每天早上 8 点自动同步
openclaw cron add \
  --name "从 Google Drive 同步健康数据" \
  --schedule "0 8 * * *" \
  --command "cd ~/.openclaw/workspace/skills/huawei-health && python3 sync_from_drive.py"
```

---

### 方案 B: rclone (更简单)

#### 1. 安装 rclone

```bash
# Ubuntu/Debian
sudo apt install rclone

# 或下载
curl https://rclone.org/install.sh | sudo bash
```

#### 2. 配置 Google Drive

```bash
rclone config

# 选择:
# n) New remote
# name: gdrive
# Storage: Google Drive
# 按提示完成 OAuth 认证
```

#### 3. 创建同步脚本

```bash
#!/bin/bash
# sync_health_rclone.sh

REMOTE_DIR="gdrive:HealthSync"
LOCAL_DIR="$HOME/.openclaw/workspace/skills/huawei-health/downloads"

echo "🔄 正在从 Google Drive 同步..."

# 同步文件
rclone copy "$REMOTE_DIR" "$LOCAL_DIR" --update --verbose

# 解析新文件
for file in "$LOCAL_DIR"/*.csv; do
    if [ -f "$file" ]; then
        echo "📊 解析: $file"
        python3 ~/.openclaw/workspace/skills/huawei-health/parse_huawei.py "$file"
    fi
done

echo "✅ 同步完成!"
```

#### 4. 设置定时任务

```bash
# 每天早上 8 点
0 8 * * * bash ~/.openclaw/workspace/skills/huawei-health/sync_health_rclone.sh
```

---

## 📊 完整自动化流程

```
华为手表
    ↓ (蓝牙)
华为健康 App
    ↓ (Health Sync 后台同步)
Google Drive
    ↓ (OpenClaw 定时拉取)
OpenClaw Memory
    ↓ (自动分析)
健康报告
```

---

## ⏱️ 时间投入

### 首次设置
- Health Sync 配置: 10 分钟
- Google Drive API 设置: 15 分钟
- OpenClaw 脚本配置: 10 分钟
- **总计: 35 分钟**

### 日常维护
- **0 分钟** (完全自动)

---

## 💰 成本

- Health Sync 免费版: 有限制 (每天同步次数)
- Health Sync Pro: ~$2.99 (一次性购买,无限制)
- Google Drive: 15GB 免费 (足够)
- rclone: 免费开源

**推荐**: 先用免费版测试,确认可行后购买 Pro

---

## 🎯 优势

1. **完全自动化** - 无需手动操作
2. **实时性好** - 每天自动同步
3. **数据完整** - 所有历史数据
4. **稳定可靠** - 成熟的工具链
5. **隐私可控** - 数据在自己的 Google Drive

---

## ⚠️ 注意事项

1. **Health Sync 兼容性**
   - 确认支持华为健康
   - 部分数据类型可能不支持

2. **Google Drive 配额**
   - 免费 15GB 通常够用
   - 定期清理旧文件

3. **网络要求**
   - 需要访问 Google 服务
   - 可能需要科学上网

---

## 🔧 故障排查

### 问题 1: Health Sync 无法连接华为健康

**解决**:
- 检查权限设置
- 重新授权
- 更新到最新版本

### 问题 2: Google Drive 同步失败

**解决**:
- 检查网络连接
- 重新认证 OAuth
- 检查 API 配额

### 问题 3: 数据格式不兼容

**解决**:
- 检查 Health Sync 导出格式
- 调整 parse_huawei.py 解析逻辑
- 查看示例文件格式

---

需要我:
1. **创建 Google Drive 同步脚本** (方案 A)
2. **配置 rclone 方案** (方案 B,更简单)
3. **测试 Health Sync 兼容性** (先确认可行)

选哪个?
