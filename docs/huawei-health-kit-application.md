# 华为 Health Kit 申请流程

## 🎯 找到 Health Kit

### 入口 1: HMS Core (推荐)
1. 访问: https://developer.huawei.com/consumer/cn/hms
2. 在 **App Services** 区域找到 **"运动健康服务"**
3. 点击进入

### 入口 2: 直接访问
```
https://developer.huawei.com/consumer/cn/hms/huawei-healthkit
```

---

## 📝 申请步骤

### 第 1 步: 创建应用 (AppGallery Connect)

1. **访问 AGC 控制台**
   ```
   https://developer.huawei.com/consumer/cn/service/josp/agc/index.html
   ```

2. **创建项目**
   - 点击 "我的项目"
   - "新建项目"
   - 项目名称: `openclaw-health`
   - 点击 "确定"

3. **添加应用**
   - 进入项目
   - 点击 "添加应用"
   - 选择平台: **Android** (即使你不发布 App)
   - 应用名称: `OpenClaw Health Sync`
   - 包名: `com.openclaw.health` (随意填写)
   - 点击 "确定"

### 第 2 步: 开通 Health Kit

1. **进入应用详情**
   - 在 AGC 控制台,点击刚创建的应用

2. **开通服务**
   - 左侧菜单 → "构建" → "Health Kit"
   - 或者在 "开发与服务" 区域找到 Health Kit
   - 点击 "立即开通"

3. **申请数据权限**
   - 勾选需要的数据类型:
     - ✅ 步数 (STEP_COUNT)
     - ✅ 心率 (HEART_RATE)
     - ✅ 睡眠 (SLEEP)
     - ✅ 运动记录 (ACTIVITY_RECORD)
     - ✅ 体重 (WEIGHT)
   
4. **填写申请信息**
   - 使用场景: "个人健康数据分析与自动化"
   - 数据用途: "同步健康数据到本地进行分析"
   - 提交审核

5. **等待审核**
   - 通常 1-3 个工作日
   - 审核通过后会收到通知

### 第 3 步: 获取凭据

审核通过后:

1. **获取 App ID 和 App Secret**
   - AGC 控制台 → 项目设置 → 常规
   - 记录:
     - App ID (Client ID)
     - App Secret (Client Secret)

2. **下载配置文件**
   - 项目设置 → 常规
   - 下载 `agconnect-services.json`

---

## 🔧 配置 OpenClaw

### 创建配置文件

```bash
# 创建配置
cat > ~/.openclaw/workspace/skills/huawei-health/config.json << 'EOF'
{
  "client_id": "你的_APP_ID",
  "client_secret": "你的_APP_SECRET",
  "redirect_uri": "http://localhost:8080/callback"
}
EOF
```

### 添加到环境变量

```bash
# 编辑 OpenClaw 配置
# ~/.openclaw/openclaw.json

{
  "env": {
    "vars": {
      "HUAWEI_CLIENT_ID": "你的_APP_ID",
      "HUAWEI_CLIENT_SECRET": "你的_APP_SECRET"
    }
  }
}
```

---

## ⏱️ 时间线

| 步骤 | 时间 | 说明 |
|------|------|------|
| 创建项目和应用 | 10 分钟 | 立即完成 |
| 开通 Health Kit | 5 分钟 | 立即完成 |
| 申请数据权限 | 5 分钟 | 提交申请 |
| **等待审核** | **1-3 天** | 华为审核 |
| 获取凭据 | 5 分钟 | 审核通过后 |
| 配置 OpenClaw | 10 分钟 | 立即完成 |

**总计**: 35 分钟操作 + 1-3 天等待

---

## 💡 审核期间可以做什么?

### 并行方案: Google Fit (立即可用)

在等待华为审核期间,先用 Google Fit:

```bash
# 1. 安装 pip (如果还在安装中,等待完成)
# 2. 运行 Google Fit 安装脚本
bash ~/.openclaw/workspace/scripts/setup-google-fit.sh

# 3. 配置 Google Cloud (20分钟)
# 4. 开始同步数据
```

这样:
- **现在**: 用 Google Fit 获取数据
- **1-3天后**: 华为审核通过,切换到官方 API
- **最终**: 两个数据源都可用,互为备份

---

## 🎯 下一步

需要我:

**A. 等华为审核,先做 Google Fit** (推荐)
- 现在就能用
- 华为审核通过后再切换

**B. 只等华为审核**
- 等待 1-3 天
- 审核通过后再配置

**C. 两个都做**
- Google Fit 立即用
- 华为 API 作为主要数据源

选哪个?
