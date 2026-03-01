class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def mostrar(self):
        if self.cabeza is None:
            print("La lista esta vacia")
            return
        
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

def convertir_a_binario(n):
        if n < 2:
            return str(n)
        else:
            return convertir_a_binario(n//2)+str(n%2)
        
def contar_digitos(n):
        n = abs(n)
        if n < 10:
            return 1
        return 1 + contar_digitos(n//10)
    
def calcular_raiz_cuadrada(n, num=0):
    if num * num > n:
        return num - 1
    return calcular_raiz_cuadrada(n, num + 1)


def raiz_cuadrada_entera(n):
    if n < 0:
        return None
    return calcular_raiz_cuadrada(n)

    
def convertir_a_decimal(num):
        valores = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

        if len(num)==1:
            return valores[num]
        
        if valores[num[0]] < valores[num[1]]:
            return valores[num[1]] - valores[num[0]] + convertir_a_decimal(num[2:])
        else:
            return valores[num[0]] + convertir_a_decimal(num[1:])
    
def suma_numeros_enteros(n):
        if n==0:
            return 0
        return n+suma_numeros_enteros(n-1)
    
lista = ListaEnlazada()

while True:
    print("\n============MENU============")
    print("1. Convertir numero entero a binario")
    print ("2. contar digitos")
    print ("3. Raiz cuadrada entera")
    print ("4. Romano a decimal")
    print ("5. Suma de numero enteros")
    print ("6. Mostrar lista enlazada")
    print ("7. Salir")

    
    opcion = input("elija una opcion: ")

    if opcion == "1":
        num = int(input("ingrese un numero: "))
        resultado = convertir_a_binario(num)
        lista.insertar(f"binario de {num}: {resultado}")
        print("resultado guardado en lista.")

    elif opcion == "2":
        num = int(input("Ingrese un numero: "))
        resultado = contar_digitos(num)
        lista.insertar(f"raiz entera de {num}: {resultado}")
        print("resultado guardado")

    elif opcion == "3":
        num = int(input("Ingrese un numero: "))
        resultado = raiz_cuadrada_entera(num)
        lista.insertar(f"Raiz entera de {num}: {resultado}")
        print("Resultado guardado.")

    elif opcion == "4":
        num = input("ingrese un numero romano: ").upper()
        resultado =convertir_a_decimal(num)
        lista.insertar(f"romano{num} a decimal: {resultado}")
        print("Resultdo guardado")

    elif opcion == "5":
        num = int(input("Ingrese un numero: "))
        resultado = suma_numeros_enteros(num)
        lista.insertar(f"suma hasta {num}: {resultado}")
        print("Resultado guardado")

    elif opcion == "6":
        print("\n============Resultado guardado==============")
        lista.mostrar()

    elif opcion == "7":
        print("Saliendo..........")
        break

    else:
        print("Opcion no valida, vuelva a intentarlo")