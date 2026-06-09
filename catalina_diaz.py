from abc import ABC, abstractmethod
class producto(ABC):
    def __init__(self,nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock 
    def get_nombre (self):
        return self.__nombre
    def get_precio (self):
        return self.__precio
    def get_stock (self):
        return self.__stock
    
    @abstractmethod
    def descuento(self):
        pass

class ropa (producto):
    def __init__(self, nombre, precio,stock,talla, telas): 
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.telas = telas

    def descuento(self):
       return self.get_precio() * 0.5

class electrodomestico (producto):
    def __init__(self, nombre, precio, stock, uso, marca):
        super().__init__(nombre, precio, stock)
        self.uso = uso
        self.marca = marca
    def descuento(self):
        return self.get_precio() * 0.9

class juguetes (producto):
    def __init__(self, nombre, precio, stock, edad, tipo):
        super().__init__(nombre, precio, stock)
        self.edad = edad
        self.tipo = tipo
    def descuento(self):
        return self.get_precio() * 0.8

class limpieza (producto):
    def __init__(self, nombre, precio, stock, olor, marca):
        super().__init__(nombre, precio, stock)
        self.olor = olor
        self.marca = marca
    def descuento(self):
        return self.get_precio() * 0.5
Productos = [
    ropa("Vestido", 15990, 15, "XS", "Poliester"),
    electrodomestico("Lavadora", 120000, 6, "Domestico", "LG"),
    juguetes("Barbie", 15990, 45, "3+", "Muñeca"),
    limpieza("Ciff", 2990, 67, "Limón", "Unilever")
]
for producto in Productos:
    print("Nombre:", producto.get_nombre(), "Precio:", producto.descuento(), "Stock:", producto.get_stock())