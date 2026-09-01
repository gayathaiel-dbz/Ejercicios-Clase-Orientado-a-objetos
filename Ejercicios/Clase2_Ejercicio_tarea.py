class Paciente:
    def _init_(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        
    def arregla_texto(devuelve):
        return f"{devuelve.nombre} (DNI: {devuelve.dni})"

class Turnos:
    def _init_(self, paciente, fecha, hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
    
    def arregla_texto(devuelve):
        return f"Fecha : {devuelve.fecha} | Hora: {devuelve.hora} | Paciente: {devuelve.paciente}"
    
class Agenda: 
    def _init_(self):
        self.turnos
        
    def agregar_turno(self, nuevo_turno):
        for t in self.turnos:
            if t.fecha == nuevo_turno.fecha and t.hora == nuevo_turno.hora: 
                print(f" Error: El horario {nuevo_turno.fecha} a las {nuevo_turno.hora}")
                return 