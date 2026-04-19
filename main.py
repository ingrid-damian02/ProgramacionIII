from avl import AVL
from utils import cargar_csv, graficar

def menu():
    arbol = AVL()

    while True:
        print("\n--- MENÚ AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Visualizar")
        print("6. Salir")

        op = input("Opción: ")

        if op == "1":
            val = int(input("Valor: "))
            arbol.raiz = arbol.insertar(arbol.raiz, val)

        elif op == "2":
            val = int(input("Buscar: "))
            res = arbol.buscar(arbol.raiz, val)
            print("Encontrado" if res else "No encontrado")

        elif op == "3":
            val = int(input("Eliminar: "))
            arbol.raiz = arbol.eliminar(arbol.raiz, val)

        elif op == "4":
            ruta = input("Ruta CSV: ")
            cargar_csv(ruta, arbol)

        elif op == "5":
            graficar(arbol)

        elif op == "6":
            break

if __name__ == "__main__":
    menu()
