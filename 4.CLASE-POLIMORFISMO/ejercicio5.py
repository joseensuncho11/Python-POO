"""Ejercicio 5: Clases de Profesiones con Polimorfismo
Crea tres clases: Médico, Ingeniero, y Docente, cada una con un método trabajar() que describa la información técnica del profesional."""
# Clase Profesion
class Profesion:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        pass

# Clase Médico
class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def mostrar_info(self):
        print("\nEste es un médico:")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Descripción: El médico {self.nombre} es especialista en {self.especialidad}.")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        
    def mostrar_info(self):
        print("\nEste es un ingeniero:")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Descripción: El ingeniero {self.nombre} se especializa en {self.especialidad}.")

# Clase Docente
class Docente:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        
    def mostrar_info(self):
        print("\nEste es un docente:")
        print(f"Nombre: {self.nombre}")
        print(f"Materia: {self.materia}")
        print(f"Descripción: El docente {self.nombre} enseña {self.materia}.")

# Función que muestra la información del profesional usando polimorfismo
def mostrar_informacion(profesional):
    profesional.mostrar_info()

# Creando instancias de cada clase
medico = Medico("Dr. Pérez", "Cardiología")
ingeniero = Ingeniero("Ing. López", "Civil")
docente = Docente("Prof. García", "Matemáticas")

# Llamando a la función para mostrar información de cada profesional
mostrar_informacion(medico)
mostrar_informacion(ingeniero)
mostrar_informacion(docente)
