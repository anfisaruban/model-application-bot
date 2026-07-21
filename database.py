import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS business_chats (
    chat_id INTEGER PRIMARY KEY
)
""")

conn.commit()


def is_known_chat(chat_id: int) -> bool:
    cursor.execute(
        "SELECT 1 FROM business_chats WHERE chat_id = ?",
        (chat_id,)
    )
    return cursor.fetchone() is not None


def add_chat(chat_id: int):
    cursor.execute(
        "INSERT OR IGNORE INTO business_chats(chat_id) VALUES (?)",
        (chat_id,)
    )
    conn.commit()