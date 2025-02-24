class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
    
    
    import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()


#imprimen mensajes de éxito o error después de intentar guardar los cambios en el archivo.

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            if self.guardar_inventario():
                print("Producto agregado correctamente al inventario y al archivo.")
            else:
                print("Error al agregar el producto al archivo.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        if self.guardar_inventario():
            print("Producto eliminado correctamente del inventario y del archivo.")
        else:
            print("Error al eliminar el producto del archivo.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                if self.guardar_inventario():
                    print("Producto actualizado correctamente en el inventario y en el archivo.")
                else:
                    print("Error al actualizar el producto en el archivo.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


#Los métodos guardar_inventario() y cargar_inventario() 
# ahora incluyen bloques try...except para capturar 
# FileNotFoundError, PermissionError y ValueError

    def guardar_inventario(self):
        try:
            with open(self.archivo, "inventario.txt") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.get_id()},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            return True
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")
            return False

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    id_producto, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado correctamente desde el archivo.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except (ValueError, FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo de inventario: {e}")
            
            
        inventario = Inventario()   
            