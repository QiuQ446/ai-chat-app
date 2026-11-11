# AI 对话应用

基于 FastAPI + DeepSeek API 的网页版 AI 助手，对话记录持久化到 SQLite。

## 功能

- 浏览器聊天界面，支持多轮对话
- 对话历史存入 SQLite，刷新页面/重启服务不丢失
- 每次请求自动带上最近 20 条上下文

## 技术栈

- 后端：FastAPI + SQLite
- 前端：原生 HTML / JavaScript
- 模型：DeepSeek API

## 本地运行

1. 安装依赖

```bash
pip install fastapi uvicorn requests
```

2. 创建 `secret.py`，填入你的 key

```python
API_KEY = "你的 DeepSeek API Key"
```

> 注意：`secret.py` 已被 `.gitignore` 排除，不会出现在仓库中，必须自己创建。

3. 启动服务

```bash
uvicorn app:app --reload
```

4. 浏览器打开 http://127.0.0.1:8000