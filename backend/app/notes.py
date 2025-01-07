from app.database import get_db_connection

def get_notes(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT note FROM notes WHERE user_id = %s", (user_id,))
    notes = cursor.fetchall()
    conn.close()
    return [note[0] for note in notes]

def add_note(user_id, note):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (user_id, note) VALUES (%s, %s)", (user_id, note))
    conn.commit()
    conn.close()