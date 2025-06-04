def menu_cliente(cliente):
    while True:
        print("""
        Menú Cliente
        1. Ver mis datos
        2. Ver tablas de productos
        3. Salir
        """)
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            cliente.mostrar_info()
        elif opcion == "2":
            ver_tabla_productos()
        elif opcion == "3":
            print("Saliendo del menú cliente...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


def menu_admin(admin):
    while True:
        print("""
        Menú Administrador
        1. Ver mis datos
        2. Crear tabla de productos
        3. Ver tablas de productos
        4. Salir
        """)
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            admin.mostrar_info()
        elif opcion == "2":
            crear_tabla_productos()
        elif opcion == "3":
            ver_tabla_productos()
        elif opcion == "4":
            print("Saliendo del menú administrador...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

