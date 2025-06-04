from interfaz import bienvenida, crear_admin, crear_cliente, login_admin, login_cliente
from db import inicializar_db
from usuario import Administrador, Cliente

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

def main():
    inicializar_db()

    while True:
        opcion = bienvenida()

        if opcion == "1":
            print("\n🔐 Accediste como ADMINISTRADOR\n")
            gestionar_usuario("admin")
            break
        elif opcion == "2":
            print("\n👤 Accediste como CLIENTE\n")
            gestionar_usuario("cliente")
            break
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    main()
