from agenda import clase_agenda

def mostar_menu():
    
    agenda = clase_agenda()
    
    while True:
        print("------------- Agenda de Contactos-------------")
        print("1 Listas de todos los contactos")
        print("2 Agregar")
        print("3 Actualizar")
        print("4 Eliminar")
        print("5 Salir")
        
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            agenda.todos()
        if opcion == 2:
            print("Ingreso de un nuevo contacto")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la direccion: ")
            telefono = input("Ingrese el telefono: ")
            email = input("Ingrese el email: ")
            edad = input("Ingrese la edad: ")               
            try:
                agenda.agregar(nombre, direccion, telefono, email, edad)
                print("Se borro con exito")
        
            except:
                print("Ocurrio un error al guardar")
                
        if opcion == 3:
            agenda.todos()
            id = input("Ingrese el id: ")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la direccion: ")
            telefono = input("Ingrese el telefono: ")
            email = input("Ingrese el email: ")
            edad = input("Ingrese la edad: ")
            
            try:
                agenda.agregar(id, nombre, direccion, telefono, email, edad)
                print("Se guardo con exito")
        
            except:
                print("Ocurrio un error al guardar")
                
        if opcion == 4:
            agenda.todos()
            id = input("Ingrese el id: ")
            try:
                agenda.eliminar(id)
                print("Se guardo con exito")
        
            except:
                print("Ocurrio un error al elimina")
                
        if opcion == 5:
            print("Gracias por su colaboracion ")
            break

if __name__ == "__main__":
    mostar_menu()