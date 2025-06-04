from usuario import Administrador, Cliente

def bienvenida():
    print("="*40)
    print("🟢 Bienvenido al Sistema de Usuarios 🟢")
    print("="*40)
    print("¿Quién eres?")
    print("1. Soy Administrador")
    print("2. Soy Cliente")
    print("3. Salir")

    return input("Elige una opción (1/2/3): ")

def crear_admin():
    print("🔐 Creando Administrador...")
    nombre = input("Nombre: ")
    email = input("Email: ")
    permisos = input("Permisos (separados por coma): ").split(",")
    admin = Administrador(nombre, email, permisos)
    admin.guardar()
    print("✅ Administrador guardado.\n")
    admin.mostrar_info()

def crear_cliente():
    print("👤 Creando Cliente...")
    nombre = input("Nombre: ")
    email = input("Email: ")
    direccion = input("Dirección: ")
    cliente = Cliente(nombre, email, direccion)
    cliente.guardar()
    print("✅ Cliente guardado.\n")
    cliente.mostrar_info()