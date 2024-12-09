# range()
# type()
# len()

# "CHANGOS".upper()
# [1,2,3].sort()
# (1,2,3).count()

#esta es la forma de hacer que las funciones sean llamadas

def saludo():
    print("Como estas pa")
saludo()

#en este tipo de funciones tengo de clarar variables 

def chagitos(nombre):
    print(f"tu nombres {nombre}")
chagitos("roberto")

def sumar (a,b):
    res = a+b
    print(f"Tu nsuma es: {res}")
    return res
numero = sumar(8,9)

numero * 3
print(numero)

# esta funcion sirve imprimir los numeros pares que hay entre el rango del numero que se fedefine por la variable que noosotros poponemos n
def imprimir_pares(n):
    for numeros in range(n):
        if numeros % 2 == 0:
            print(f"Numero par es: {numeros}")
imprimir_pares(10)

