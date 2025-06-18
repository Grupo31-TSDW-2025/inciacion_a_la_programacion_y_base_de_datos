import sqlite3

def inicializar_db():
    with open("crear_tablas.sql", "r", encoding="utf-8") as f:
        script = f.read()
        cursor.executescript(script)
    conn.commit()
