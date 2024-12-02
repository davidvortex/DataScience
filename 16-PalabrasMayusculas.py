# Declarar la variable palabra
palabra = "coronado"

# Verificar el tipo de dato de palabra
print(type(palabra))  # Esto imprime: <class 'str'>

# Convertir palabra a mayúsculas y asignarlo a palabra_may
palabra_may = palabra.upper()

# Imprimir palabra en mayúsculas
print(palabra_may)  # Esto imprime: CORONADO

# Aplicar el método capitalize() para convertir solo la primera letra a mayúscula
print(palabra.capitalize())  # Esto imprime: Coronado