# Verificar si la edad es mayor o menor de 18
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Mayor")
else:
    print("Menor")

# Verificar la cantidad de canicas
canicas = int(input("Ingrese su cantidad de canicas: "))
if canicas >= 20:
    print("Muchas")
elif canicas <= 18:
    print("Pocas")
else:
    print("Agrega canicas")

# Encontrar el máximo entre tres números
a1, a2, a3 = (int(input("Ingresa el primer dato: ")), 
              int(input("Ingresa el segundo dato: ")), 
              int(input("Ingresa el tercer dato: ")))

if a1 > a2:
    if a1 > a3:
        maximo = a1
    else:
        maximo = a3
else:
    if a2 > a3:
        maximo = a2
    else:
        maximo = a3

print("El máximo es:", maximo)


