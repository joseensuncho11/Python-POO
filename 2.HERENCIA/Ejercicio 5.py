class Reloj:
    # Constructor
    def __init__(self, marca, tipo, material):
        self.marca = marca
        self.tipo = tipo
        self.material = material
        self.precio = float(input("Precio del reloj: $"))

    # Método público para registrar los detalles del reloj
    def registrar(self):
        print("-----------------------")
        print("RELOJ REGISTRADO")
        print("-----------------------")
        print(f"Marca: {self.marca}")
        print(f"Tipo de reloj: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio: ${self.precio}")


class RelojInteligente(Reloj):  # Subclase RelojInteligente
    # Constructor
    def __init__(self, marca, tipo, material, pantalla):
        super().__init__(marca, tipo, material)  # Herencia de la clase Reloj
        self.pantalla = pantalla  # Atributo adicional para el tipo de pantalla
        self.sistema_operativo = input("Sistema operativo del reloj inteligente: ")

    # Método para simular encender el reloj inteligente
    def encender(self):
        print("-----------------------")
        print("Encendiendo reloj inteligente...")
        print(f"Marca: {self.marca}")
        print(f"Tipo de reloj: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Pantalla: {self.pantalla}")
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Precio: ${self.precio}")

        # Condiciones para el tipo de pantalla
        if self.pantalla == "OLED":
            print("Pantalla OLED de alta calidad, ideal para visibilidad en cualquier condición.")
        else:
            print("Pantalla estándar, suficiente para uso general.")

        # Condiciones para el sistema operativo
        if self.sistema_operativo == "Wear OS":
            print("Sistema operativo Wear OS: acceso a una amplia gama de aplicaciones.")
        elif self.sistema_operativo == "Tizen":
            print("Sistema operativo Tizen: integrado con dispositivos Samsung.")
        else:
            print("Sistema operativo desconocido. Verifique la compatibilidad.")

        print("Reloj inteligente encendido con éxito!")


# Instanciando un objeto de la subclase RelojInteligente
mi_reloj = RelojInteligente("Apple", "Deportivo", "Silicona", "OLED")

# Registrando los detalles del reloj inteligente
mi_reloj.registrar()

# Simulando encender el reloj inteligente
mi_reloj.encender()
