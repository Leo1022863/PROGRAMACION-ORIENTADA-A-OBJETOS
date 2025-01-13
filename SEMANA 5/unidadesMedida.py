# Función para convertir metros a kilómetros
def metros_a_kilometros(metros: float) -> float:
    return metros / 1000.0

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

# Función para convertir kilogramos a libras
def kilogramos_a_libras(kilogramos: float) -> float:
    return kilogramos * 2.20462

# Ejemplo de uso
metros = 5000.0
celsius = 25.0
kilogramos = 70.0

kilometros = metros_a_kilometros(metros)
fahrenheit = celsius_a_fahrenheit(celsius)
libras = kilogramos_a_libras(kilogramos)

print(f"{metros} metros son {kilometros} kilómetros")
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
print(f"{kilogramos} kilogramos son {libras} libras")
