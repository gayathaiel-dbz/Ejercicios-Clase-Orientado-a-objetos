class Personajes(ABC):
    def __init__(self,nombre):
        self.nombre = nombre
    
    @abstractmethod
    def atacar(self):