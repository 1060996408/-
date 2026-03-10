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
