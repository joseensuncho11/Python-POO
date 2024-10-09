class Electrodomestico:
    # constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo = int(input("Consumo eléctrico en kWh:"))

    # método público
    def registrar(self):
        print("-----------------------")
        print("ELECTRODOMÉSTICO REGISTRADO")
        print("-----------------------")
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Capacidad (L):", self.capacidad)
        print("Consumo eléctrico (kWh):", self.consumo)

class Refrigerador(Electrodomestico): # subclase Refrigerador
    # constructor
    def __init__(self, marca, color, capacidad, tipo):
        super().__init__(marca, color, capacidad) # super clase heredada
        self.tipo = tipo # atributo privado
        self.temperatura = int(input("Temperatura inicial en grados Centígrados:"))

    # método privado
    def ajustar_temperatura(self):
        print("Temperatura actual:", self.temperatura)
        
        if self.temperatura < 0:
            print("-----------------------")
            print(f"El refrigerador {self.marca}, de tipo {self.tipo}, está demasiado frío!!")
        elif self.temperatura > 8:
            print("-----------------------")
            print(f"El refrigerador {self.marca}, de tipo {self.tipo}, está demasiado caliente!!")
        else:
            print("-----------------------")
            print(f"El refrigerador {self.marca}, de tipo {self.tipo}, está a una temperatura óptima.")
        
# instanciando la subclase refrigerador
objeto_refrigerador = Refrigerador('LG', 'Plata', '400', 'No Frost')
objeto_refrigerador.registrar() # registrando el electrodoméstico
objeto_refrigerador.ajustar_temperatura() # ajustando la temperatura
