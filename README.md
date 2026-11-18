# AI 对话应用

基于 FastAPI + DeepSeek API 的网页版 AI 助手，对话记录持久化到 SQLite。

## 目录结构

- `app.py` / `db.py` / `index.html`：项目主代码
- `practice/`：Python 学习练习（基础语法到数据库）

## 功能

- 浏览器聊天界面，支持多轮对话
- 对话历史存入 SQLite，刷新页面/重启服务不丢失
- 每次请求自动带上最近 20 条上下文

## 技术栈

- 后端：FastAPI + SQLite
- 前端：原生 HTML / JavaScript
- 模型：DeepSeek API

## 本地运行

## 部署（Ubuntu 服务器）

### 1. 准备
- Ubuntu 22.04 服务器（2 核 2G）
- 安全组放行 8000 端口

### 2. 安装基础环境
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
```

### 3. 拉取代码
```bash
git clone https://github.com/QiuQ446/ai-chat-app.git
cd ai-chat-app
```

### 4. 创建虚拟环境并安装依赖
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 5. 配置密钥
创建 `secret.py`：

```python
API_KEY = "你的 DeepSeek API Key"
```

### 6. 后台启动
```bash
nohup uvicorn app:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
```

### 7. 验证
浏览器访问 `http://服务器公网IP:8000/health`，返回 `{"status":"ok"}` 即部署成功。