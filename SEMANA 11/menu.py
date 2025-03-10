from alumnos import clase_alumnos
from cursos import clase_curso


opcion = int(input("Ingrese una opcion: "))
alumno = clase_alumnos()
curso = clase_curso()
    
    
while True:
    print("-"*20)
    print("----------Bienvenidos al sistema de distribucion de cursos")
    print("1. Crear alumno")
    print("2. Crear Curso")
    print("3. Asignar el alumno al curso")
    print("4. Lista de cursos")
    print("5. Salir ")
    
    if opcion == 1:
        id=0
        nombre = input("Ingrese el nombre")
        apellido = input("Ingrese el apellido")
        telefono = input("Ingrese el telefono")
    
        alumno = clase_alumnos(id, nombre, apellido, telefono)
    
    if opcion == 2:
        nombre_curso = input("Ingrese el nombre del curso")
        paralelo = input("Ingrese el nombre del paralelo:  ")
        paralelo = input("Ingrese el nombre del paralelo:  ")
        curso = clase_curso(nombre,paralelo)
        
        
    if opcion == 3:
        curso.agregar_curso_alumno(alumno)
        
    if opcion == 3:
        print(curso.informacion())
        
    