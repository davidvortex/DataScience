# Declarar la variable frase
frase = "Esta es una frase de ejemplo para contar palabras"  # Cambia la frase según prefieras

# Contar el número de palabras
# Usamos el método split para dividir la frase en palabras y luego len para contar el número de elementos
numero_palabras = len(frase.split())

# Mostrar el resultado
print(f"La frase contiene {numero_palabras} palabras.")