# 1) Al menos una clase base y una clase derivada, demostrando el concepto de herencia.

# Definición de la clase base
class Animal:
    # Métodos
    def hacer_sonido(self):
        """
        Método que debe ser sobrescrito por las subclases.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Definición de la clase derivada Perro
class Perro(Animal):
    # Métodos
    def hacer_sonido(self):
        """
        Método sobrescrito que define el sonido que hace el perro.
        """
        return "El perro ladra"

# Definición de la clase derivada Gato
class Gato(Animal):
    # Métodos
    def hacer_sonido(self):
        """
        Método sobrescrito que define el sonido que hace el gato.
        """
        return "El gato maulla"

# Crear instancias de las clases derivadas y utilizar sus métodos
mi_perro = Perro()
mi_gato = Gato()

print(mi_perro.hacer_sonido())  # Salida: El perro ladra
print(mi_gato.hacer_sonido())   # Salida: El gato maulla


# 2) Implementación de encapsulación en al menos una clase

class Persona:
    # Atributos privados
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado

    # Métodos públicos para acceder y modificar los atributos privados
    def obtener_nombre(self):
        """
        Método para obtener el valor del atributo privado nombre.
        """
        return self.__nombre

    def establecer_nombre(self, nombre):
        """
        Método para establecer el valor del atributo privado nombre.
        """
        self.__nombre = nombre

    def obtener_edad(self):
        """
        Método para obtener el valor del atributo privado edad.
        """
        return self.__edad

    def establecer_edad(self, edad):
        """
        Método para establecer el valor del atributo privado edad.
        """
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo.")

# Crear una instancia de la clase Persona y utilizar sus métodos
persona = Persona("Juan", 30)

# Acceder a los atributos privados a través de los métodos públicos
print(persona.obtener_nombre())  # Salida: Juan
print(persona.obtener_edad())    # Salida: 30

# Modificar los atributos privados a través de los métodos públicos
persona.establecer_nombre("Carlos")
persona.establecer_edad(35)

print(persona.obtener_nombre())  # Salida: Carlos
print(persona.obtener_edad())    # Salida: 35



# 3) 3.	Un ejemplo de polimorfismo, ya sea a través de métodos sobrescritos 
# o utilizando argumentos múltiples/variables.

# Definición de la clase base
class Animal:
    # Métodos
    def hacer_sonido(self):
        """
        Método que debe ser sobrescrito por las subclases.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Definición de la clase derivada Perro
class Perro(Animal):
    # Métodos
    def hacer_sonido(self):
        """
        Método sobrescrito que define el sonido que hace el perro.
        """
        return "El perro ladra"

# Definición de la clase derivada Gato
class Gato(Animal):
    # Métodos
    def hacer_sonido(self):
        """
        Método sobrescrito que define el sonido que hace el gato.
        """
        return "El gato maulla"

# Función que demuestra el polimorfismo
def imprimir_sonido(animal):
    """
    Función que recibe un objeto de tipo Animal y llama al método hacer_sonido.
    """
    print(animal.hacer_sonido())

# Crear instancias de las clases derivadas y utilizar sus métodos
mi_perro = Perro()
mi_gato = Gato()

imprimir_sonido(mi_perro)  # Salida: El perro ladra
imprimir_sonido(mi_gato)   # Salida: El gato maulla
