class nodo:
    def __init__(self, carnet, nombre):
        self.carnet=carnet
        self.nombre=nombre
        self.siguiente=None

class lista:
    def __init__(self):
        self.inicio=None

    def agregar(self, carnet, nombre):
        self.nd=nodo(carnet,nombre)
        self.nd.siguiente=self.inicio
        self.inicio=self.nd

    def mostrar(self):
        self.temp=self.inicio
        while(self.temp!=None):
            print(self.temp.nombre)
            self.temp=self.temp.siguiente

    def vaciar(self):
        self.inicio=None
        
estudiantes=lista()
estudiantes.agregar(123,"Juan")
estudiantes.agregar(124,"Pedro")
estudiantes.agregar(125,"Maria")
print(estudiantes.mostrar())




"""
nd1=nodo(123,"Juan")
nd2=nodo(124,"Pedro")
nd3=nodo(125,"Maria")
nd1.siguiente=nd2
nd2.siguiente=nd3
print(nd1.siguiente.nombre)
print(nd2.nombre)
"""

