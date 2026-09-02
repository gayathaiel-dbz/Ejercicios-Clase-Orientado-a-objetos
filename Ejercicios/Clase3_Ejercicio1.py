class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    @property
    def precio(self):
        return self._precio 
    
    @precio.setter
    def precio(self, nuevo_precio):
     if nuevo_precio > 0:
        self._precio = nuevo_precio
     else:
         print("Error")