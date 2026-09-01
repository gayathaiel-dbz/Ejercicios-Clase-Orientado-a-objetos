class Paciente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def arregla_texto(self):
        return f"{self.nombre} (DNI: {self.dni})"


class Turnos:
    def __init__(self, paciente, fecha, hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora

    def arregla_texto(self):
        return f"Fecha: {self.fecha} | Hora: {self.hora} | Paciente: {self.paciente.arregla_texto()}"


class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, nuevo_turno):
        for t in self.turnos:
            if t.fecha == nuevo_turno.fecha and t.hora == nuevo_turno.hora:
                print(f"Error: El horario {nuevo_turno.fecha} a las {nuevo_turno.hora} ya está ocupado.")
                return

        self.turnos.append(nuevo_turno)
        print(f"Turno agendado con éxito para {nuevo_turno.paciente.nombre}")

    def listar_turnos(self):
        print("Turnos registrados en la agenda")

        if len(self.turnos) == 0:
            print("No hay turnos")
            return

        for t in self.turnos:
            print(t.arregla_texto())