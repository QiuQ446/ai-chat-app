import requests
from secret import API_KEY

# ---------- 配置：换平台只改这两行 ----------
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"
# 智谱的话改成：
# URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
# MODEL = "glm-4-flash"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "用一句话解释什么是 API"}
    ],
}

r = requests.post(URL, headers=headers, json=payload, timeout=60)

print("状态码:", r.status_code)

if r.status_code == 200:
    data = r.json()
    print("AI:", data["choices"][0]["message"]["content"])
    print("用量:", data["usage"])
else:
    print("失败原因:", r.text[:300])