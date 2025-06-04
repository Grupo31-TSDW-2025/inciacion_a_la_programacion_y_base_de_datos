from db import cursor, conn

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar(self):
        raise NotImplementedError("Implementar en subclases.")

class Cliente(Usuario):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.direccion = direccion

    def mostrar_info(self):
        print(f"Cliente -> Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, tipo, extra) VALUES (?, ?, ?, ?)",
            (self.nombre, self.email, "cliente", self.direccion)
        )
        conn.commit()

class Administrador(Usuario):
    def __init__(self, nombre, email, permisos):
        super().__init__(nombre, email)
        self.permisos = permisos  # permisos es una lista

    def mostrar_info(self):
        permisos_str = ", ".join(self.permisos)
        print(f"Administrador -> Nombre: {self.nombre}, Email: {self.email}, Permisos: {permisos_str}")

    def guardar(self):
        permisos_str = ",".join(self.permisos)
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, tipo, extra) VALUES (?, ?, ?, ?)",
            (self.nombre, self.email, "admin", permisos_str)
        )
        conn.commit()

