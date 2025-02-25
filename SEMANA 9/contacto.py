class clase_contacto:
    def __init__(self, id_contacto:int, nombre:str, direccion:str, telefono:str, email:str, edad:int):
        self.id_contacto = id_contacto
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.edad = edad
        
    def actualizar_metodo(self, nombre=None, direccion=None, telefono=None, email=None, edad=None):
        if nombre:
            self.nombre = nombre
        if direccion is not None:
            self.direccion = direccion
        if telefono is not None:
            self.telefono = telefono
        if email is not None:
            self.email = email
        if edad is not None:
            self.edad = edad
            
    def __str__(self):
        return f"id: {self.id_contacto} Nombre: {self.nombre} Direccion: {self.direccion} telefono: {self.telefono}"
        