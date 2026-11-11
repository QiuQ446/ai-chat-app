import json
import requests
from secret import API_KEY

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": MODEL,
    "messages": [{"role": "user", "content": "用三句话介绍 Python"}],
    "stream": True,
}

r = requests.post(URL, headers=headers, json=payload, timeout=60, stream=True)

if r.status_code != 200:
    print("失败:", r.text[:300])
else:
    for line in r.iter_lines():
        if not line:
            continue
        text = line.decode("utf-8")
        if text.startswith("data: "):
            text = text[6:]
        if text == "[DONE]":
            break
        chunk = json.loads(text)
        content = chunk["choices"][0]["delta"].get("content")
        if content:
            print(content, end="", flush=True)
    print()