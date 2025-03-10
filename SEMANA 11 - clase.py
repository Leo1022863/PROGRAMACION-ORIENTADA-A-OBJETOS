import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para almacenar los productos

    def agregar_producto(self, producto):
        if producto.obtener_id() not in self.productos:
            self.productos[producto.obtener_id()] = producto
            return True
        return False

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            return True
        return False

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.obtener_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        return list(self.productos.values())

    def guardar_inventario(self, nombre_archivo="inventario.json"):
        with open(nombre_archivo, 'w') as archivo:
            productos_serializados = {id_producto: producto.__dict__ for id_producto, producto in self.productos.items()}
            json.dump(productos_serializados, archivo, indent=4)

    def cargar_inventario(self, nombre_archivo="inventario.json"):
        try:
            with open(nombre_archivo, 'r') as archivo:
                productos_serializados = json.load(archivo)
                for id_producto, datos_producto in productos_serializados.items():
                    producto = Producto(datos_producto['id_producto'], datos_producto['nombre'], datos_producto['cantidad'], datos_producto['precio'])
                    self.productos[id_producto] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
