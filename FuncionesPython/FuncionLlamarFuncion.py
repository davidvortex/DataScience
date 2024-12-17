def solicitar_nombre():
    nombre = input("Ingrese Nombre: ")
    return nombre
    
def saludar():
    salu = f"¡Hola {solicitar_nombre()}!"
    return salu
    
print(saludar())