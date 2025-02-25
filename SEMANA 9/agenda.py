#[] = listas
#() = tuplas
#{} = Diccionarios y conjuntos

from contacto import clase_contacto

class clase_agenda:
    def __init__(self):
        self.lista_contacto = {}
        self.contador_contactos = 1
        
    def agregar(self, nombre, direccion, telefono, email, edad):
        #Instancia de un objeto
        variable_contacto = clase_contacto(nombre, direccion, telefono, email, edad)  
        #self.lista_contacto.append(variable_contacto)
        self.lista_contacto[self.contador_contactos] = variable_contacto
        self.contador_contactos += 1
        
    def todos(self):
        if not self.lista_contacto:
            print("No existen contactos disponibles")
            return
        print("\n Lista de contactos")
        print("-" * 20)
        for contacto in self.lista_contacto.values():
            print(contacto)
        print()
               
    def actualizar(self, id_contacto, nombre, direccion, telefono, email, edad):
        if id_contacto in self.lista_contacto:
            self.lista_contacto[id_contacto].actualizar_metodo(nombre, direccion, telefono, email, edad)
            print("Se actualizo con exito")
        else:
            print("No se encontro el contacto")
            
    def eliminar(self, id_contacto):
        if id_contacto in self.lista_contacto:
            del self.lista_contacto[id_contacto]
        else:
            print("No se encontro el contacto")