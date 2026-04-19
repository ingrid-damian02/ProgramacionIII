class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class ABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)
        return raiz

    def buscar(self, raiz, valor):
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izq, valor)
        return self.buscar(raiz.der, valor)