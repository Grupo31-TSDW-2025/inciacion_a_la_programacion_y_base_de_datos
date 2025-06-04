from usuario import Administrador, Cliente

def crear_admin():
    print("🔐 Creando Administrador...")
    nombre = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    admin = Administrador(nombre, email, password)
    admin.guardar()
    print("✅ Administrador guardado.\n")
    admin.mostrar_info()


def crear_cliente():
    print("👤 Creando Cliente...")
    nombre = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    cliente = Cliente(nombre, email, password)
    cliente.guardar()
    print("✅ Cliente guardado.\n")
    cliente.mostrar_info()