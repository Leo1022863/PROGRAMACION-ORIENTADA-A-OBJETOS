from datetime import datetime

# Función para agregar un empleado
def agregar_empleado(empleados, nombre, edad, salario, fecha_ingreso):
    empleados.append({
        'nombre': nombre,
        'edad': edad,
        'salario': salario,
        'fecha_ingreso': datetime.strptime(fecha_ingreso, "%Y-%m-%d")
    })

# Función para mostrar la información de los empleados
def mostrar_empleados(empleados):
    for empleado in empleados:
        print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}, Fecha de Ingreso: {empleado['fecha_ingreso'].strftime('%Y-%m-%d')}")

# Función para buscar un empleado por nombre
def buscar_empleado(empleados, nombre):
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre.lower():
            return empleado
    return None

# Lista para almacenar empleados
empleados = []

# Ejemplo de uso
agregar_empleado(empleados, 'Juan Perez', 30, 2500.50, '2023-01-15')
agregar_empleado(empleados, 'Maria Lopez', 25, 2700.75, '2022-06-20')
agregar_empleado(empleados, 'Carlos Gomez', 40, 3200.00, '2021-12-01')

print("Lista de empleados:")
mostrar_empleados(empleados)

# Buscar un empleado por nombre
nombre_buscar = 'Maria Lopez'
empleado = buscar_empleado(empleados, nombre_buscar)
if empleado:
    print(f"\nEmpleado encontrado: Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}, Fecha de Ingreso: {empleado['fecha_ingreso'].strftime('%Y-%m-%d')}")
else:
    print(f"\nEmpleado con nombre {nombre_buscar} no encontrado.")
