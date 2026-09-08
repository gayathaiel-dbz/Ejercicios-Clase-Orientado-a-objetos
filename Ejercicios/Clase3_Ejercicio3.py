class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def trabajar(self):
        return f"{self.nombre} esta haciendo tareas generales"

class Programador(Empleado):
    def trabajar(self):
        return f"{self.nombre} esta programando en python"

class Diseñador(Empleado):
    def trabajar(self):
        return f"{self.nombre} esta diseñando interfaces"
