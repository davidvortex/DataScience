lista = [22,44,35,10,57]

def cuadrado(n):
    return n * n

def calcular_lista(numeros):
    for numero in numeros:
        respuesta = cuadrado(numero)
        print(f"El numero de {numero} es {respuesta}")

calcular_lista(lista)