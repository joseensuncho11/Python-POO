class Electronico:
    # Constructor
    def __init__(self, marca, modelo, procesador):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = int(input("Cantidad de memoria RAM en GB: "))

    # Método público para registrar los detalles del dispositivo
    def registrar(self):
        print("-----------------------")
        print("DISPOSITIVO ELECTRÓNICO REGISTRADO")
        print("-----------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")


class Laptop(Electronico):  # Subclase Laptop
    # Constructor
    def __init__(self, marca, modelo, procesador, disco_duro):
        super().__init__(marca, modelo, procesador)  # Hereda de la clase Electronico
        self.disco_duro = disco_duro  # Atributo para el tipo de disco duro
        self.bateria = int(input("Duración de la batería en horas: "))

    # Método para simular encender la laptop
    def encender(self):
        print("-----------------------")
        print("Intentando encender la laptop...")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Disco duro: {self.disco_duro}")
        print(f"Batería: {self.bateria} horas")

        if self.bateria > 2:
            print("Encendido exitoso, batería suficiente.")
        else:
            print("Batería baja, conecte el cargador para encender la laptop.")


# Instanciando un objeto de la subclase Laptop
mi_laptop = Laptop("Dell", "Inspiron 15", "Intel Core i7", "SSD 512GB")

# Registrando los detalles de la laptop
mi_laptop.registrar()

# Simulando encender la laptop
mi_laptop.encender()
