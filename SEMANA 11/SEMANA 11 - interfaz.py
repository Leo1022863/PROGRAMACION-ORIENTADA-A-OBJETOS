def mostrar_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("0. Salir")

def main():
    inventario = Inventario()
    inventario.cargar_inventario()  # Cargar inventario al iniciar el programa

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("Producto agregado con éxito.")
            else:
                print("Error: El ID del producto ya existe.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado con éxito.")
            else:
                print("Error: Producto no encontrado.")

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado con éxito.")
            else:
                print("Error: Producto no encontrado.")

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            productos = inventario.mostrar_inventario()
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("El inventario está vacío.")

        elif opcion == '6':
            inventario.guardar_inventario()
            print("Inventario guardado con éxito.")

        elif opcion == '7':
            inventario.cargar_inventario()
            print("Inventario cargado con éxito.")

        elif opcion == '0':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
