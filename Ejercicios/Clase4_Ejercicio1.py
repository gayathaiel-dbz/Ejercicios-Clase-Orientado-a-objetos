class Personajes(ABC):
    def __init__(self,nombre):
        self.nombre = nombre
    
    @abstractmethod
    def atacar(self):
        pass
    
class Guerrero(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def atacar(self):
        print(f"{self.nombre} (Guerrero) ataca con su arma")