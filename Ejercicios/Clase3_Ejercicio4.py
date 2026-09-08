class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    


    @property
    def area(self):
        return self.ancho * self.alto 


    @property
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

ancho = float(input("Ingresa el ancho del rectangulo: "))
alto = float(input("Ingresa el alto del rectangulo: "))
rectangulo = Rectangulo(ancho, alto)
print("Area: ", rectangulo.area)
print("Perimetro: ", rectangulo.perimetro)