# Clase Libro con atributos privados y públicos
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor  # Atributo privado
        self.__isbn = isbn  # Atributo privado
        self.editorial = editorial  # Atributo público
    
    # Método getter para titulo
    def obtener_titulo(self):
        return self.__titulo
    
    # Método getter para autor
    def obtener_autor(self):
        return self.__autor
    
        # Método getter para isbn
    def obtener_isbn(self):
        return self.__isbn
    
    # Método setter para titulo
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo
    
    # Método setter para autor
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
    
    # Método setter para isbn
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn
    
    # Método para mostrar la información completa del libro
    def mostrar_informacion(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# Ejemplo de uso
libro = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0", "Sudamericana")

# Mostrar información del libro
libro.mostrar_informacion()

print("---------------------------")

# Modificar atributos privados usando los setters
libro.establecer_titulo("El amor en los tiempos del cólera")
print(f"Titulo: {libro.obtener_titulo()}")
libro.establecer_autor("Gabriel García Márquez")
print(f"Autor: {libro.obtener_autor()}")
libro.establecer_isbn("978-0-14-103243-6")
print(f"Isbn: {libro.obtener_isbn()}")
print(f"Editoria: {libro.editorial}")

