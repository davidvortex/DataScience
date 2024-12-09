# funcion independiente
def pedir_nombre():
    nombre = input("Introduce nombre: ")
    return nombre

# funcion independiente
def pedir_apellido():
    apellido = input("Introduce apellido: ")
    return apellido

# esta funcion esta sola
def pedir_edad():
    edad = int(input("Introduce edad: "))
    return edad

# llamar de una funcion a otra funcion
def saludar():
    saludar = f"Hola, {pedir_nombre()} {pedir_apellido()}, con edad de {pedir_edad()}"
    return saludar
print(saludar())

