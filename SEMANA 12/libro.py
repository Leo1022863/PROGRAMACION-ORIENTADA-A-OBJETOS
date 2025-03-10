# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable (Título, Autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        titulo, autor = self.titulo_autor
        return f"{titulo} por {autor} | Categoría: {self.categoria} | ISBN: {self.isbn}"





