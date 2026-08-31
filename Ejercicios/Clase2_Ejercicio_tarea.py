class Paciente:
    def _init_(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    def devuelve_estado(devuelve):
        return f"{devuelve.nombre} (DNI: {devuelve.dni})"