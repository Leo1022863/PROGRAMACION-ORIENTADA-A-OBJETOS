#Ejemplo 1: Gestión de Inventario en una Tienda

#En este ejemplo, vamos a modelar la gestión de inventario de una tienda que vende productos.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad_vendida):
        if self.cantidad >= cantidad_vendida:
            self.cantidad -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente inventario de {self.nombre} para vender {cantidad_vendida} unidades.")

    def reponer(self, cantidad_repuesta):
        self.cantidad += cantidad_repuesta
        print(f"Se han repuesto {cantidad_repuesta} unidades de {self.nombre}.")

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"El producto '{producto.nombre}' ha sido agregado a la tienda.")

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: ${producto.precio:.2f}, Cantidad: {producto.cantidad} unidades")

# Ejemplo de uso
tienda = Tienda()
producto1 = Producto("Manzanas", 0.50, 100)
producto2 = Producto("Naranjas", 0.75, 50)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_inventario()

producto1.vender(20)
tienda.mostrar_inventario()

producto2.reponer(30)
tienda.mostrar_inventario()


#Ejemplo 2: Sistema de Reservas de Hotel

#En este ejemplo, vamos a modelar un sistema de reservas de habitaciones de hotel.

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ha sido liberada.")
        else:
            print(f"La habitación {self.numero} ya está libre.")

class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"La habitación {habitacion.numero} ha sido agregada al hotel.")

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            estado = "ocupada" if habitacion.ocupada else "libre"
            print(f"Número: {habitacion.numero}, Tipo: {habitacion.tipo}, Precio: ${habitacion.precio:.2f}, Estado: {estado}")

# Ejemplo de uso
hotel = Hotel()
habitacion1 = Habitacion(101, "Sencilla", 50.00)
habitacion2 = Habitacion(102, "Doble", 80.00)

hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

hotel.mostrar_habitaciones()

habitacion1.reservar()
hotel.mostrar_habitaciones()

habitacion1.liberar()
hotel.mostrar_habitaciones()
