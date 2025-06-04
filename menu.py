from products import crear_tabla_productos, ver_tabla_productos

def menu_admin(admin):
    while True:
        print("Menú Administrador:")
        print("1. Ver mis datos")
        print("2. Crear tabla de productos")
        print("3. Ver tabla de productos")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            admin.mostrar_info()
        elif opcion == "2":
            crear_tabla_productos()
        elif opcion == "3":
            ver_tabla_productos()
        elif opcion == "4":
            print("Saliendo del menú administrador...\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")

def menu_cliente(cliente):
    while True:
        print("Menú Cliente:")
        print("1. Ver mis datos")
        print("2. Ver tabla de productos")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            cliente.mostrar_info()
        elif opcion == "2":
            ver_tabla_productos()
        elif opcion == "3":
            print("Saliendo del menú cliente...\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")