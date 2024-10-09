"""Crea tres clases: Aprendiz, instructor y coordinador, cada una con un metodo mostrar_info()
que describa el tipo de vehiculo y una funcion para mostrar el polimorfismo mostrar_informacion()"""
# Clase Aprendiz
class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo): 
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formacion: ")
        self.regional = input("Regional")
        
    def mostrar_info(self):
        print("Hola soy un aprendiz SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Sexo. {self.sexo}")
        print(f"Estudiante del programa: {self.formacion} de la Regional {self.regional}")
        
# Clase Instructor
class Instructor: 
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area
        
    def mostrar_info(self):
        print("Hola, soy un instructor de SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Area de instruccion: {self.area}")
        
# Clase Coordinador
class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento
        
    def mostrar_info(self):
        print("Hola, soy un coordinador del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}")
        
# Funcion que muestra la informacion de cualquier tipo de objeto
def mostrar_informacion(persona):
    persona.mostrar_info()
    
# Instancia de cada clase
objeto_aprendiz = Aprendiz("Jose Daniel", "Ensuncho Benitez", "0000000001", "Masculino")
objeto_instructor = Instructor("Esperanza", "Gomez", "11111111111111", "Programacion")
objeto_coordinador = Coordinador("Carlos", "Gil", "123456789", "Recursos Humanos")

# Llamado al metodo mostrar_info para cada objeto
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)

