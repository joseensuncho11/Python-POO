class Dispositivo:
    # constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Capacidad de la batería (mAh):"))

    # método público
    def registrar(self):
        print("-----------------------")
        print("DISPOSITIVO REGISTRADO")
        print("-----------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año de fabricación:", self.año)
        print("Capacidad de la batería (mAh):", self.capacidad_bateria)

class Smartphone(Dispositivo): # subclase Smartphone
    # constructor
    def __init__(self, marca, modelo, año, sistema_operativo):
        super().__init__(marca, modelo, año) # super clase heredada
        self.sistema_operativo = sistema_operativo # atributo privado
        self.conectividad = input("Tipo de conectividad (4G, 5G):")

    # método privado
    def encender(self):
        print("Encendiendo...")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Sistema Operativo:", self.sistema_operativo)
        print("Conectividad:", self.conectividad)
        
        if self.capacidad_bateria > 0:
            print("-----------------------")
            print(f"El smartphone {self.marca} {self.modelo} con {self.sistema_operativo} y conectividad {self.conectividad} está encendido!!")
        else:
            print("-----------------------")
            print(f"El smartphone {self.marca} {self.modelo} con {self.sistema_operativo} no tiene suficiente batería para encender!!")

# instanciando la subclase smartphone
objeto_smartphone = Smartphone('Apple', 'iPhone 12', '2020', 'iOS')
objeto_smartphone.registrar() # registrando el dispositivo
objeto_smartphone.encender() # encendiendo el smartphone
