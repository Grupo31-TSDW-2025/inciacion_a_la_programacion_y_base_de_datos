from db import cursor

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
