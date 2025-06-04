from usuario import Administrador, Cliente
from db import cursor

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
    admin = Administrador(nombre, email)
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


def login_admin():
    print("Iniciar sesión como Administrador")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ? AND tipo = 'admin' AND password = ?",
        (email, password)
    )
    usuario = cursor.fetchone()
    if usuario:
        print(f"\n✅ Bienvenido administrador {usuario[1]}!")  # Asumiendo que nombre está en posición 1
        # Aquí podés agregar la lógica para mostrar menú admin o seguir con el programa
    else:
        print("\n❌ Usuario o contraseña incorrectos. Intenta de nuevo.\n")
        login_admin()  # Reintentar login (podés limitar intentos para evitar bucle infinito)


def login_cliente():
    print("Iniciar sesión como Cliente")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ? AND tipo = 'cliente' AND password = ?",
        (email, password)
    )
    usuario = cursor.fetchone()
    if usuario:
        print(f"\n✅ Bienvenido cliente {usuario[1]}!")  # Asumiendo que nombre está en posición 1
        # Aquí podés agregar la lógica para mostrar menú cliente o seguir con el programa
    else:
        print("\n❌ Usuario o contraseña incorrectos. Intenta de nuevo.\n")
        login_cliente()  # Reintentar login (podés limitar intentos)



def gestionar_usuario(tipo):
    while True:
        respuesta = input(f"¿Ya tienes usuario {tipo}? (s/n): ").strip().lower()
        if respuesta == "s":
            if tipo == "admin":
                login_admin()   # función para login admin (deberías implementarla)
            else:
                login_cliente() # función para login cliente (deberías implementarla)
            break
        elif respuesta == "n":
            if tipo == "admin":
                crear_admin()
            else:
                crear_cliente()
            break
        else:
            print("Por favor, responde 's' o 'n'.")