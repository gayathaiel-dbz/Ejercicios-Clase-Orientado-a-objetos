from abc import ABC, abstractmethod
class Personajes(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    @abstractmethod
    def atacar(self):
        pass
    
class Guerrero(Personajes):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def atacar(self):
        print(f"{self.nombre} (Guerrero) ataca con su arma")

class Mago(Personajes):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def atacar(self):
        print(f"{self.nombre} (Mago) ataca con hechizo")

class Arquero(Personajes):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def atacar(self):
        print(f"{self.nombre} (Arquero) ataca con flecha")

print("Simulacion")
equipo = [Guerrero("Mordred"), Mago("Tamamo"), Arquero("Robin Hood")]

for personajes in equipo:
    personajes.atacar()