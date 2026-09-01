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
        
        self.turnos.append(nuevo_turno)
        print(f"Turno agendado con exito para {nuevo_turno.paciente.nombre}")
    
    def listar_turnos(self):
        print("Turnos registrados en la agenda")
        if len(self.turnos) == 0:
            print("No hay turnos")
            return
        
        for t in self.turnos:
            print(t.arregla_texto())
            
