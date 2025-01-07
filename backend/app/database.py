import mysql.connector
from app.config import Config

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",  # Use "127.0.0.1" instead of "localhost" to force TCP/IP
        port=3306,         # Default MySQL port
        user="niaassistant",
        password="niaassistant123",
        database="ai_assistant"
    )

def test_db_connection():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    conn.close()
    return result

print(test_db_connection())  # Should print: (1,)