class Motor:
    def arrancar(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()
    
    def arrancar(self):
        self.motor.arrancar()
        
        
mi_auto = Auto()
mi_auto.arrancar()