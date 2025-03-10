from libro import Libro
from usuario import Usuario

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # Añadir libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido.")

    # Quitar libro
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")

    # Dar de baja usuario
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print("ID de usuario o ISBN no válido.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.devolver_libro(isbn)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.titulo_autor[0]}' devuelto.")
                    return
            print(f"El usuario no tiene el libro con ISBN {isbn}.")
        else:
            print("ID de usuario no válido.")

    # Buscar libros
    def buscar_libros(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, key) == value for key, value in criterios.items()):
                resultados.append(libro)
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con los criterios.")

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("ID de usuario no válido.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Ficción", "1234567890")
libro2 = Libro("1984", "George Orwell", "Distopía", "0987654321")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Ana", "U001")
usuario2 = Usuario("Luis", "U002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "1234567890")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "1234567890")
biblioteca.listar_libros_prestados("U001")

# Buscar libros
biblioteca.buscar_libros(categoria="Distopía")