from db import cursor, conn

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar(self):
        raise NotImplementedError("Implementar en subclases.")

class Cliente(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password

    def mostrar_info(self):
        print(f"Cliente -> Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.password}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO clientes (nombre, email, password) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.password)
        )
        conn.commit()

class Administrador(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password

    def mostrar_info(self):
        print(f"Administrador -> Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.password}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO administradores (nombre, email, password) VALUES (?, ?, ?)",
            (self.nombre, self.email, self.password)
        )
        conn.commit()

    def eliminar_cliente(self):

        cursor.execute("SELECT id, nombre, email FROM clientes")
        clientes = cursor.fetchall()

        if not clientes:
            print("❌ No hay clientes registrados.")
            return

        print("\n📋 Lista de clientes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}")

        id_cliente = input("🔍 Ingrese el ID del cliente que desea eliminar: ").strip()

        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()

        if cliente:
            confirmacion = input(f"¿Está seguro que desea eliminar al cliente '{cliente[1]}'? (s/n): ").lower()
            if confirmacion == 's':
                cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
                conn.commit()
                print("✅ Cliente eliminado correctamente.")
            else:
                print("❎ Operación cancelada.")
        else:
            print("❌ Cliente no encontrado.")
