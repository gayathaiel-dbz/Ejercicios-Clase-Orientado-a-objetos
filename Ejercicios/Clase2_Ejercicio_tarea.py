class Paciente:
    def _init_(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    def arregla_texto(devuelve):
        return f"{devuelve.nombre} (DNI: {devuelve.dni})"