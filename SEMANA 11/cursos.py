from alumnos import clase_alumnos

class clase_curso:
    def __init__(self, nombre = None, paralelo = None):
        self.nombre = nombre
        self.paraleo = paralelo
        self.lista_curso =[]
        
    def agregar_curso_alumno(self, alumno:clase_alumnos):
        self.lista_curso.append(self.nombre, self.paraleo, alumno)
        
    def informacion(self):
        return self.lista_curso
    
    