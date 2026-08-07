import sqlite3


conn = sqlite3.connect("chat_history.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()



def save_message(role, message):
    cursor.execute(
        "INSERT INTO chats (role, message) VALUES (?, ?)",
        (role, message)
    )
    conn.commit()



def load_messages():
    cursor.execute(
        "SELECT role, message FROM chats ORDER BY id"
    )
    return cursor.fetchall()



def clear_history():
    cursor.execute("DELETE FROM chats")
    conn.commit()



def delete_message(chat_id):
    cursor.execute(
        "DELETE FROM chats WHERE id=?",
        (chat_id,)
    )
    conn.commit()



def update_message(chat_id, new_message):
    cursor.execute(
        "UPDATE chats SET message=? WHERE id=?",
        (new_message, chat_id)
    )
    conn.commit()


# Close database connection (optional)
def close_connection():
    conn.close()