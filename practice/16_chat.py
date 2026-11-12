import requests
from secret import API_KEY

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

messages = [
    {"role": "system", "content": "你是一个只用五个字以内回答的助手，语气冷淡"}
]

while True:
    q = input("你：")
    if q in ("quit", "exit", "q"):
        break

    messages.append({"role": "user", "content": q})

    r = requests.post(URL, headers=headers,
        json={"model": MODEL, "messages": messages},
        timeout=60)

    if r.status_code != 200:
        print("失败:", r.text[:200])
        messages.pop()          # 把这次失败的问题撤掉，保持历史干净
        continue

    data = r.json()
    answer = data["choices"][0]["message"]["content"]
    print("AI：", answer)

    messages.append({"role": "assistant", "content": answer})