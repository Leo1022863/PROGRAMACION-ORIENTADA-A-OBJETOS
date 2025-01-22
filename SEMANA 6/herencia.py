## La mama de las clases

class Madre:
    def __init__(self, casa, auto):
        self.casa = casa
        self.auto = auto
        
    def vivir(self):
        return f"Mi madre vive en la casa {self.casa}"
    def conducir(self):
        return f"Mi madre conduce un auto {self.auto}"
    
class Hijo(Madre): ##Herencia
    def __init__(self, casa, auto, moto):
        super().__init__(casa, auto)
        self.moto = moto
            
    def conducir(self):  #polimorfismo
        return f"El hijo conduce una moto {self.moto}"
    
    def vive(self):
        return f"El hijo vive en {self.casa}"
    
    def imprimirMoto(self):
        return f"imprime la marca de la moto {self.moto}"
    
    
    #Objeto Madre
mi_clase_madre = Madre("Ambato","Nissan 1200")
    
    #Objeto Hijo
el_hijo = Hijo("Quito","Ford 150","Yamaha")
    #el_hijo = Hijo("Quito","Ford 150","Yamaha")

print(mi_clase_madre.conducir())
print(mi_clase_madre.vivir())
print(el_hijo.conducir())
print(el_hijo.vive())
print(el_hijo.imprimirMoto())