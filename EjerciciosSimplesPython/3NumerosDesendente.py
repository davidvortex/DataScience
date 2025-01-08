x1, x2, x3 = 3, 2, 1

# Encuentra el máximo entre los tres números
if x1 > x2 and x1 > x3:
    maximo = x1
    if x2 > x3:
        medio = x2
        minimo = x3
    else:
        medio = x3
        minimo = x2
elif x2 > x1 and x2 > x3:
    maximo = x2
    if x1 > x3:
        medio = x1
        minimo = x3
    else:
        medio = x3
        minimo = x1
else:
    maximo = x3
    if x1 > x2:
        medio = x1
        minimo = x2
    else:
        medio = x2
        minimo = x1

# Imprimir los números en orden ascendente
print("Los números en orden ascendente son:", minimo, medio, maximo)
