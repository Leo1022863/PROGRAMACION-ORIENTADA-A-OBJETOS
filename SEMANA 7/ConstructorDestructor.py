#EJERCICIO 1

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        print("Se ha creado una cuenta para", self.titular)

    def __del__(self):
        print("La cuenta de", self.titular, "ha sido cerrada")

# Creando un objeto
cuenta = CuentaBancaria("Pedro", 1000)

# Accediendo a atributos y modificando el saldo
print("El saldo actual es:", cuenta.saldo)
cuenta.saldo += 500

# Destruyendo el objeto (explícitamente)
del cuenta


#EJERCICIO 2

class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.
        Inicializa los atributos nombre y edad de la persona.

        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una persona llamada {nombre}")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se ejecuta cuando el objeto se destruye.
        """
        print(f"Adiós, {self.nombre}")

# Creando objetos
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)

# Los destructores se llaman automáticamente cuando los objetos salen de alcance