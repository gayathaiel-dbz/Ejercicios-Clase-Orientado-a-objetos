class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)


biblioteca = Biblioteca("Biblioteca Central")

libro1 = Libro("Dragon Ball", "Akira Toriyama", 1984)
libro2 = Libro("Blue Lock", "Muneyuki Kaneshiro", 2022)
libro3 = Libro("Sword Art Online", "Reki Kawahara", 2010)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)