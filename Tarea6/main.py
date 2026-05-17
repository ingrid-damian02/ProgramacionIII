import csv
from graphviz import Digraph


class NodoB:
    def __init__(self, hoja=False):
        self.claves = []
        self.hijos = []
        self.hoja = hoja


class ArbolB:
    def __init__(self, grado):
        self.raiz = NodoB(True)
        self.grado = grado 


    def insertar(self, clave):
        raiz = self.raiz

        if len(raiz.claves) == (2 * self.grado) - 1:
            nueva_raiz = NodoB(False)
            nueva_raiz.hijos.append(raiz)
            self.dividir_hijo(nueva_raiz, 0)
            self.insertar_no_lleno(nueva_raiz, clave)
            self.raiz = nueva_raiz
        else:
            self.insertar_no_lleno(raiz, clave)

    def insertar_no_lleno(self, nodo, clave):
        i = len(nodo.claves) - 1

        if nodo.hoja:
            nodo.claves.append(None)

            while i >= 0 and clave < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1

            nodo.claves[i + 1] = clave
        else:
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1

            i += 1

            if len(nodo.hijos[i].claves) == (2 * self.grado) - 1:
                self.dividir_hijo(nodo, i)

                if clave > nodo.claves[i]:
                    i += 1

            self.insertar_no_lleno(nodo.hijos[i], clave)

    def dividir_hijo(self, padre, indice):
        grado = self.grado
        hijo = padre.hijos[indice]
        nuevo = NodoB(hijo.hoja)

        padre.claves.insert(indice, hijo.claves[grado - 1])
        padre.hijos.insert(indice + 1, nuevo)

        nuevo.claves = hijo.claves[grado:]
        hijo.claves = hijo.claves[:grado - 1]

        if not hijo.hoja:
            nuevo.hijos = hijo.hijos[grado:]
            hijo.hijos = hijo.hijos[:grado]

    def buscar(self, clave, nodo=None):
        if nodo is None:
            nodo = self.raiz

        i = 0

        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and clave == nodo.claves[i]:
            return True

        if nodo.hoja:
            return False

        return self.buscar(clave, nodo.hijos[i])

    def eliminar(self, clave):
        self._eliminar(self.raiz, clave)

        if len(self.raiz.claves) == 0 and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]

    def _eliminar(self, nodo, clave):
        grado = self.grado
        indice = self._buscar_indice(nodo, clave)

        if indice < len(nodo.claves) and nodo.claves[indice] == clave:
            if nodo.hoja:
                nodo.claves.pop(indice)
            else:
                self._eliminar_interno(nodo, clave, indice)
        else:
            if nodo.hoja:
                print("La clave no existe en el árbol.")
                return

            bandera = indice == len(nodo.claves)

            if len(nodo.hijos[indice].claves) < grado:
                self._llenar(nodo, indice)

            if bandera and indice > len(nodo.claves):
                self._eliminar(nodo.hijos[indice - 1], clave)
            else:
                self._eliminar(nodo.hijos[indice], clave)

    def _buscar_indice(self, nodo, clave):
        indice = 0

        while indice < len(nodo.claves) and nodo.claves[indice] < clave:
            indice += 1

        return indice

    def _eliminar_interno(self, nodo, clave, indice):
        grado = self.grado

        if len(nodo.hijos[indice].claves) >= grado:
            predecesor = self._obtener_predecesor(nodo, indice)
            nodo.claves[indice] = predecesor
            self._eliminar(nodo.hijos[indice], predecesor)

        elif len(nodo.hijos[indice + 1].claves) >= grado:
            sucesor = self._obtener_sucesor(nodo, indice)
            nodo.claves[indice] = sucesor
            self._eliminar(nodo.hijos[indice + 1], sucesor)

        else:
            self._fusionar(nodo, indice)
            self._eliminar(nodo.hijos[indice], clave)

    def _obtener_predecesor(self, nodo, indice):
        actual = nodo.hijos[indice]

        while not actual.hoja:
            actual = actual.hijos[-1]

        return actual.claves[-1]

    def _obtener_sucesor(self, nodo, indice):
        actual = nodo.hijos[indice + 1]

        while not actual.hoja:
            actual = actual.hijos[0]

        return actual.claves[0]

    def _llenar(self, nodo, indice):
        if indice != 0 and len(nodo.hijos[indice - 1].claves) >= self.grado:
            self._prestar_anterior(nodo, indice)

        elif indice != len(nodo.hijos) - 1 and len(nodo.hijos[indice + 1].claves) >= self.grado:
            self._prestar_siguiente(nodo, indice)

        else:
            if indice != len(nodo.hijos) - 1:
                self._fusionar(nodo, indice)
            else:
                self._fusionar(nodo, indice - 1)

    def _prestar_anterior(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice - 1]

        hijo.claves.insert(0, nodo.claves[indice - 1])

        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())

        nodo.claves[indice - 1] = hermano.claves.pop()

    def _prestar_siguiente(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice + 1]

        hijo.claves.append(nodo.claves[indice])

        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))

        nodo.claves[indice] = hermano.claves.pop(0)

    def _fusionar(self, nodo, indice):
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice + 1]

        hijo.claves.append(nodo.claves.pop(indice))
        hijo.claves.extend(hermano.claves)

        if not hijo.hoja:
            hijo.hijos.extend(hermano.hijos)

        nodo.hijos.pop(indice + 1)

    def mostrar(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz

        print("Nivel", nivel, ":", nodo.claves)

        if not nodo.hoja:
            for hijo in nodo.hijos:
                self.mostrar(hijo, nivel + 1)

    def graficar(self, nombre_archivo="arbol_b"):
        dot = Digraph(comment="Árbol B")
        dot.attr(rankdir="TB")

        self._agregar_nodos_graphviz(dot, self.raiz)

        dot.render(nombre_archivo, format="png", cleanup=True)
        print(f"Imagen generada: {nombre_archivo}.png")

    def _agregar_nodos_graphviz(self, dot, nodo, contador=[0]):
        id_nodo = str(contador[0])
        contador[0] += 1

        etiqueta = " | ".join(str(clave) for clave in nodo.claves)
        dot.node(id_nodo, etiqueta, shape="record")

        for hijo in nodo.hijos:
            id_hijo = self._agregar_nodos_graphviz(dot, hijo, contador)
            dot.edge(id_nodo, id_hijo)

        return id_nodo


def cargar_csv(arbol, nombre_archivo):
    try:
        with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            for fila in lector:
                for dato in fila:
                    dato = dato.strip()

                    if dato.isdigit():
                        arbol.insertar(int(dato))

        print("Los datos han sido cargados correctamente")

    except FileNotFoundError:
        print("No se ha encontrado el archivo")
    except Exception as e:
        print("Error al cargar el archivo:", e)


def menu():
    print("----------- ÁRBOL B -----------")
    grado = int(input("Ingrese el grado mínimo del Árbol B: "))

    if grado < 2:
        print("El grado mínimo (debe ser 2 o mayor)")
        return

    arbol = ArbolB(grado)

    while True:
        print("\n----------MENÚ ---------")
        print("1. Insertar clave")
        print("2. Buscar clave")
        print("3. Eliminar clave")
        print("4. Cargar datos desde CSV")
        print("5. Mostrar árbol en consola")
        print("6. Generar imagen con Graphviz")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = int(input("Ingrese la clave a insertar: "))
            arbol.insertar(clave)
            print("Clave insertada correctamente.")

        elif opcion == "2":
            clave = int(input("Ingrese la clave a buscar: "))

            if arbol.buscar(clave):
                print("La clave sí existe en el árbol.")
            else:
                print("La clave no existe en el árbol.")

        elif opcion == "3":
            clave = int(input("Ingrese la clave a eliminar: "))
            arbol.eliminar(clave)
            print("Proceso de eliminación finalizado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del archivo CSV: ")
            cargar_csv(arbol, nombre)

        elif opcion == "5":
            print("\nRepresentación del árbol:")
            arbol.mostrar()

        elif opcion == "6":
            arbol.graficar()

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()