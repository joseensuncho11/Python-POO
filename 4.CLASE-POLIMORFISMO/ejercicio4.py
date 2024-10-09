"""Ejercicio 4: Instrumentos Musicales con Polimorfismo
Crea clases: Guitarra, Piano, y Trompeta, cada una con un método tocar() que describa la información técnica del instrumento."""
# Clase base Instrumento
# Clase Instrumento
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        pass

# Clase Guitarra
class Guitarra:
    def __init__(self, nombre, num_cuerdas):
        self.nombre = nombre
        self.num_cuerdas = num_cuerdas
    
    def mostrar_info(self):
        print("\nEste es una guitarra:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de cuerdas: {self.num_cuerdas}")
        print(f"Descripción: Tocando la guitarra {self.nombre} con {self.num_cuerdas} cuerdas.")

# Clase Piano
class Piano:
    def __init__(self, nombre, num_teclas):
        self.nombre = nombre
        self.num_teclas = num_teclas
        
    def mostrar_info(self):
        print("\nEste es un piano:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de teclas: {self.num_teclas}")
        print(f"Descripción: Tocando el piano {self.nombre} con {self.num_teclas} teclas.")

# Clase Trompeta
class Trompeta:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mostrar_info(self):
        print("\nEste es una trompeta:")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: Tocando la trompeta {self.nombre}.")

# Función que muestra la información del instrumento usando polimorfismo
def mostrar_informacion(instrumento):
    instrumento.mostrar_info()

# Creando instancias de cada clase
guitarra = Guitarra("Guitarra Española", 6)
piano = Piano("Piano de Cola", 88)
trompeta = Trompeta("Trompeta")

# Llamando a la función para mostrar información de cada instrumento
mostrar_informacion(guitarra)
mostrar_informacion(piano)
mostrar_informacion(trompeta)

