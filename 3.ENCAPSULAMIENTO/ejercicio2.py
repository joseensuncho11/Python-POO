# Clase Producto con atributos privados y públicos
class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado
        self.cantidad = cantidad  # Atributo público
        self.categoria = categoria  # Atributo público
    
    # Método getter para nombre
    def obtener_nombre(self):
        return self.__nombre
    
    # Método getter para precio
    def obtener_precio(self):
        return self.__precio
    
     # Método setter para nombre
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    # Método setter para precio
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
    
    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Creacion del objeto
producto = Producto("portatil", 1200000, 10, "Electrónica")

# imprimir información del producto publico y privado
producto.mostrar_informacion()

print("---------------------------")

# Modificar e imprimir los atributos encapsulados
producto.establecer_nombre("Portatil Gamer") # Setter
print(f"Nombre: {producto.obtener_nombre()}") # Getter
producto.establecer_precio(1500000) # Setter
print(f"Precio: {producto.obtener_precio()}") # Getter
print(f"Cantidad: {producto.cantidad}") # Publico
print(f"Categoria: {producto.categoria}") # Publico


