from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.carnet})"

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.colas = None


    def insertar_al_principio(self, nodo):
        if self.cabeza is None:
            self.cabeza = self.colas = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza.anterior = nodo
            self.cabeza = nodo

    def insertar_al_final(self, nodo):
        if self.cabeza is None:
            self.cabeza = self.colas = nodo
        else:
            self.colas.siguiente = nodo
            nodo.anterior = self.colas
            self.colas = nodo

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.colas = actual.anterior
                print(f"Nodo con carnet {carnet} eliminado.")
                return
            actual = actual.siguiente
        print(f"No se encontró nodo con carnet {carnet}.")

    def mostrar_lista(self):
        actual = self.cabeza
        print("None <- ", end="")
        while actual:
            print(str(actual), end=" <-> " if actual.siguiente else " -> None\n")
            actual = actual.siguiente

    def generar_grafo(self, nombre_archivo="lista"):
        dot = Digraph(comment='Lista Doblemente Enlazada')
        actual = self.cabeza
       
        while actual:
            dot.node(actual.carnet, str(actual))
            actual = actual.siguiente
        actual = self.cabeza
        while actual:
            if actual.siguiente:
                dot.edge(actual.carnet, actual.siguiente.carnet, constraint='true')
                dot.edge(actual.siguiente.carnet, actual.carnet, constraint='true')
            actual = actual.siguiente
        dot.render(nombre_archivo, format='png', view=True)

def menu():
    lista = ListaDoblementeEnlazada()
    while True:
        print("\n--- Lista Doblemente Enlazada ---")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            nodo = Nodo(nombre, apellido, carnet)
            lista.insertar_al_principio(nodo)
            lista.generar_grafo("lista")
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            nodo = Nodo(nombre, apellido, carnet)
            lista.insertar_al_final(nodo)
            lista.generar_grafo("lista")
        elif opcion == "3":
            carnet = input("Carnet del nodo a eliminar: ")
            lista.eliminar_por_valor(carnet)
            lista.generar_grafo("lista")
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            print("¡Saliendo!")
            break
        else:
            print("Opción no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    menu()