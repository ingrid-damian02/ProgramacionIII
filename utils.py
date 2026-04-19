import csv
import os
from graphviz import Digraph

def cargar_csv(ruta, arbol):
    base = os.path.dirname(__file__)
    ruta_completa = os.path.join(base, ruta)

    with open(ruta_completa, newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            for valor in fila:
                arbol.raiz = arbol.insertar(arbol.raiz, int(valor.strip()))
def graficar(arbol):
    dot = Digraph()

    def recorrer(nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izq:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                recorrer(nodo.izq)
            if nodo.der:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                recorrer(nodo.der)

    recorrer(arbol.raiz)
    dot.render('arbol_avl', view=True)