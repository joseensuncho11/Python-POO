# Clase persona con atributos encapsulados o privados
class Personas: 
    # Método constructor
    def __init__(self, nombres, apellidos, identidad, fechanacimiento, sexo):
        self.__nombres = nombres  # Privado
        self.__apellidos = apellidos  # Privado
        self.__identidad = identidad  # Privado
        self.fechanacimiento = fechanacimiento  # Público
        self.sexo = sexo  # Público

    # Método getter
    def obtener_nombres(self):
        return self.__nombres

    # Método getter
    def obtener_apellidos(self):
        return self.__apellidos

    # Método getter
    def obtener_identidad(self):
        return self.__identidad

    # Método setter
    def establecer_nombres(self, nuevo_nombres):
        self.__nombres = nuevo_nombres

    # Método setter
    def establecer_apellidos(self, nuevo_apellidos):
        self.__apellidos = nuevo_apellidos

    # Método mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombres: {self.__nombres}")
        print(f"Apellidos: {self.__apellidos}")
        print(f"N° Identidad: {self.__identidad}")
        print(f"Fecha nacimiento: {self.fechanacimiento}")
        print(f"Sexo: {self.sexo}")

# Creación del objeto
persona = Personas("Jorge", "Rojas", 1102345678, "14/09/2000", "M")

# Imprimir atributos públicos y privados
persona.mostrar_detalles()

print("---------------------------")

# Modificar e imprimir atributos encapsulados
persona.establecer_nombres("Carlos")  # Setter
print(f"Nombres: {persona.obtener_nombres()}")  # Getter
persona.establecer_apellidos("Perez")  # Setter
print(f"Apellidos: {persona.obtener_apellidos()}")  # Getter
print(f"N° Identidad: {persona.obtener_identidad()}")  # Getter
print(f"Fecha de nacimiento: {persona.fechanacimiento}")  # Público
print(f"Sexo: {persona.sexo}")  # Público

    