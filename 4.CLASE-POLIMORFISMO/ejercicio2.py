"""Ejercicio 2: Clases de  Vehículos con Polimorfismo
Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() que describa el tipo de vehículo."""

# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        pass
    
class Carro:
    def __init__(self, marca, modelo, anio, puertas):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.puertas = puertas
        
    def mostrar_info(self):
        print("\nEste es un carro:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"año: {self.anio}")
        print(f"Número de puertas: {self.puertas}")

# Clase Moto
class Moto:
    def __init__(self, marca, modelo, anio, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.cilindrada = cilindrada
        
    def mostrar_info(self):
        print("\nEsta es una moto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"año: {self.anio}")
        print(f"Cilindrada: {self.cilindrada} cc")

# Clase Bicicleta
class Bicicleta:
    def __init__(self, marca, tipo, cambios):
        self.marca = marca
        self.tipo = tipo
        self.cambios = cambios
        
    def mostrar_info(self):
        print("\nEsta es una bicicleta:")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Número de cambios: {self.cambios}")

# Función que muestra la información del vehículo usando polimorfismo
def mostrar_informacion(vehiculo):
    vehiculo.mostrar_info()

# Creando instancias de cada clase
carro = Carro("Toyota", "Corolla",2024, 4)
moto = Moto("Yamaha", "MT-07", 2022, 689)
bicicleta = Bicicleta("Trek", "Montaña", 21)

# Llamando a la función para mostrar información de cada vehículo
mostrar_informacion(carro)
mostrar_informacion(moto)
mostrar_informacion(bicicleta)


