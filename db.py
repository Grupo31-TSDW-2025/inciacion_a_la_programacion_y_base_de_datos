import sqlite3

# Conexión en memoria (puede cambiarse por archivo .db)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

def inicializar_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT,
            tipo TEXT,
            extra TEXT
        )
    """)
    conn.commit()
