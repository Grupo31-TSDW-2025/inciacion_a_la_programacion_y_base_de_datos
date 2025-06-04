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
        print(f"Cliente -> Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.password}")

    def guardar(self):
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, tipo, extra) VALUES (?, ?, ?, ?)",
            (self.nombre, self.email, "cliente", self.password)
        )
        conn.commit()

class Administrador(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email)
        self.password = password  # permisos es una lista

    def mostrar_info(self):
        print(f"Administrador -> Nombre: {self.nombre}, Email: {self.email}, Password: {self.password}")

    def guardar(self):
        password = self.password  # Aquí podrías aplicar hashing si es necesario
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, tipo, extra) VALUES (?, ?, ?, ?)",
            (self.nombre, self.email, "admin", password)
        )
        conn.commit()

