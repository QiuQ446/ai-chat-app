import db
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from secret import API_KEY
from fastapi.responses import FileResponse

app = FastAPI()
db.init_db()

URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/history")
def history():
    rows = db.load_messages(20)
    return {"messages": [{"role": r, "content": c} for r, c in rows]}

@app.post("/chat")
def chat(req: ChatRequest):
    db.save_message("user", req.message) 

    rows = db.load_messages(20)
    history = [{"role": r, "content": c} for r, c in rows]
    
    payload = {
        "model": MODEL,
        "messages": history,
    }
    r = requests.post(URL,headers=headers,json=payload,timeout=60)

    if r.status_code !=200:
        return {"error":r.text[:200]}

    data = r.json()
    answer = data["choices"][0]["message"]["content"]

    db.save_message("assistant", answer)          # ← 存 AI 的话

    return {"answer": answer}