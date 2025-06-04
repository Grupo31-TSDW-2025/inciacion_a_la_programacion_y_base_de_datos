from db import cursor, conn

def crear_tabla_productos():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conn.commit()
    print("✅ Tabla 'productos' creada o ya existía.\n")

def ver_tabla_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if productos:
        print("\nLista de productos:")
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Precio: ${prod[2]:.2f}")
        print("")
    else:
        print("\n⚠️ No hay productos para mostrar.\n")
