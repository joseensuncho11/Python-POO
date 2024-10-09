"""Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta."""

from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, tarifa_hora, horas_trabajadas):
        self.nombre = nombre
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.tarifa_hora * self.horas_trabajadas

# Ejemplo de uso
if __name__ == "__main__":
    empleado1 = EmpleadoTiempoCompleto("Alice", 1800000)
    empleado2 = EmpleadoPorHoras("Bob", 48, 34500)

    print(f"Salario de {empleado1.nombre}: ${empleado1.calcular_salario()}")
    print(f"Salario de {empleado2.nombre}: ${empleado2.calcular_salario()}")
