""" Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea(). 
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el método realizar_tarea() 
de manera específica según su especialidad"""

from abc import ABC, abstractmethod

# Clase abstracta
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase concreta para Ingeniero
class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def realizar_tarea(self):
        return f"{self.nombre} está diseñando un sistema en el área de {self.especialidad}."

# Clase concreta para Doctor
class Doctor(TareaEmpleado):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def realizar_tarea(self):
        return f"{self.nombre} está atendiendo pacientes en el área de {self.especialidad}."

# Ejemplo de uso
if __name__ == "__main__":
    ingeniero = Ingeniero("Jose", "Software")
    doctor = Doctor("Erica", "Pediatría")

    print(ingeniero.realizar_tarea())
    print(doctor.realizar_tarea())
