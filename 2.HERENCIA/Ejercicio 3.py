class Instrumento:
    # constructor
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = float(input("Precio del instrumento:"))

    # método público
    def registrar(self):
        print("-----------------------")
        print("INSTRUMENTO REGISTRADO")
        print("-----------------------")
        print("Tipo de instrumento:", self.tipo)
        print("Marca:", self.marca)
        print("Material:", self.material)
        print("Precio: $", self.precio)

class Guitarra(Instrumento): # subclase Guitarra
    # constructor
    def __init__(self, tipo, marca, material, cuerdas):
        super().__init__(tipo, marca, material) # super clase heredada
        self.cuerdas = cuerdas # atributo privado
        self.acordes = input("¿Qué acordes básicos conoces? ")

    # método privado
    def tocar(self):
        print("Acordes proporcionados:", self.acordes)
        
        if self.acordes:
            print("-----------------------")
            print(f"La guitarra {self.marca}, con {self.cuerdas} cuerdas, está tocando los acordes {self.acordes}!!")
        else:
            print("-----------------------")
            print(f"La guitarra {self.marca}, con {self.cuerdas} cuerdas, no puede tocar porque no se conocen acordes.")

# instanciando la subclase guitarra
objeto_guitarra = Guitarra('Guitarra', 'Fender', 'Madera', 6)
objeto_guitarra.registrar() # registrando el instrumento
objeto_guitarra.tocar() # simulando tocar la guitarra
