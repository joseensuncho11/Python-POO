"""Ejercicio 3: Animales con Polimorfismo
Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente."""
# Clase Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        pass

# Clase Perro
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_info(self):
        print("\nEste es un perro:")
        print(f"Nombre: {self.nombre}")
        print(f"Sonido: {self.sonido()}")

    def sonido(self):
        return "Guau"

# Clase Gato
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mostrar_info(self):
        print("\nEste es un gato:")
        print(f"Nombre: {self.nombre}")
        print(f"Sonido: {self.sonido()}")

    def sonido(self):
        return "Miau"

# Clase Pajaro
class Pajaro:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_info(self):
        print("\nEste es un pájaro:")
        print(f"Nombre: {self.nombre}")
        print(f"Sonido: {self.sonido()}")

    def sonido(self):
        return "fiufiufiu"

# Función que muestra la información del animal usando polimorfismo
def mostrar_informacion(animal):
    animal.mostrar_info()

# Creando instancias de cada clase
perro = Perro("Balton")
gato = Gato("Garfield")
pajaro = Pajaro("Piolin")

# Llamando a la función para mostrar información de cada animal
mostrar_informacion(perro)
mostrar_informacion(gato)
mostrar_informacion(pajaro)
