# Paso 1: Asignar strings usando comillas simples y dobles
texto1 = 'Viva python'
texto2 = "Viva python"

# Paso 2: Comprobar si texto1 y texto2 son iguales
sonIguales = texto1 == texto2
print(sonIguales)  # Esto imprimirá: True

# Paso 3: Concatenar 'Viva' y 'python'
texto1 = 'Viva'
texto2 = "python"
sonIguales = f"{texto1} {texto2}"  # Usamos f-strings para concatenar con un espacio
print(sonIguales)  # Esto imprimirá: Viva python
