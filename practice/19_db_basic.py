import sqlite3

conn = sqlite3.connect("chat.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")


cur.execute("INSERT INTO messages (role,content) VALUES (?, ?)",("user", "你好"))
cur.execute("INSERT INTO messages (role,content) VALUES (?, ?)",("assistant", "你好呀"))
cur.execute("INSERT INTO messages (role,content) VALUES (?, ?)",("user", "我叫小明"))


cur.execute("SELECT id, role, content,created_at FROM messages ORDER BY id")
for row in cur.fetchall():
    print(row)


conn.commit()
conn.close()