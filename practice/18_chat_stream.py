import json
import requests
from secret import API_KEY

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

messages = []

while True:
    q = input("\n你：")
    if q in ("quit", "exit", "q"):
        break

    messages.append({"role": "user", "content": q})

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": True,
    }

    r = requests.post(URL, headers=headers, json=payload,
                      timeout=60, stream=True)

    if r.status_code != 200:
        print("失败:", r.text[:200])
        messages.pop()
        continue

    print("AI：", end="", flush=True)

    full = ""
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
            full += content

    print()
    messages.append({"role": "assistant", "content": full})