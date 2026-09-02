class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class CarritoCompra:
    def __init__(self):
        self.productos = []
    def agregar(self, producto: Producto):
        if producto.precio > 0:
            self.productos.append(producto)
        else:
            print(f"No se pudo agregar '{producto.nombre}': el precio debe ser mayor a 0.")
    def total(self) -> float:
        return sum(p.precio for p in self.productos)
    def mostrar(self):
        if not self.productos:
            print("El carrito está vacío.")
            return

        print("--- Carrito de Compras ---")
        for p in self.productos:
            print(p) 
        print(f"Total a pagar: ${self.total():.2f}")


p1 = Producto("copa del mundo", 0)
p2 = Producto("tarjeta grafica", 190.000)
p3 = Producto("buzo de bokita", 129.999)

carrito = CarritoCompra()
carrito.agregar(p1)
carrito.agregar(p2)
carrito.agregar(p3)
carrito.mostrar()