from interfaz import bienvenida, crear_admin, crear_cliente
from db import inicializar_db

def main():
    inicializar_db()

    while True:
        opcion = bienvenida()

        if opcion == "1":
            print("\n🔐 Accediste como ADMINISTRADOR\n")
            crear_admin()
            break
        elif opcion == "2":
            print("\n👤 Accediste como CLIENTE\n")
            crear_cliente()
            break
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    main()
