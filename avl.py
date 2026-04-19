from abb import ABB, Nodo

class AVL(ABB):

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)

        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        if balance > 1 and valor < raiz.izq.valor:
            return self.rotar_derecha(raiz)

        if balance < -1 and valor > raiz.der.valor:
            return self.rotar_izquierda(raiz)

        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)

        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.izq = self.eliminar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.eliminar(raiz.der, valor)
        else:
            if not raiz.izq:
                return raiz.der
            elif not raiz.der:
                return raiz.izq

            temp = self.minimo(raiz.der)
            raiz.valor = temp.valor
            raiz.der = self.eliminar(raiz.der, temp.valor)

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        if balance > 1 and self.balance(raiz.izq) >= 0:
            return self.rotar_derecha(raiz)

        if balance > 1 and self.balance(raiz.izq) < 0:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)

        if balance < -1 and self.balance(raiz.der) <= 0:
            return self.rotar_izquierda(raiz)

        if balance < -1 and self.balance(raiz.der) > 0:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz