import math

# Función para calcular el área de un triángulo
def area_triangulo(base: float, altura: float) -> float:
    return 0.5 * base * altura

# Función para calcular el área de un círculo
def area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)

# Función para calcular el área de un cuadrado
def area_cuadrado(lado: float) -> float:
    return lado * lado

# Ejemplo de uso
base_triangulo = 5.0
altura_triangulo = 10.0
radio_circulo = 7.0
lado_cuadrado = 4.0

area_t = area_triangulo(base_triangulo, altura_triangulo)
area_c = area_circulo(radio_circulo)
area_q = area_cuadrado(lado_cuadrado)

print(f"El área del triángulo es: {area_t} unidades cuadradas")
print(f"El área del círculo es: {area_c:.2f} unidades cuadradas")
print(f"El área del cuadrado es: {area_q} unidades cuadradas")
