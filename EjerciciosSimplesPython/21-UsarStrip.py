# Declarar la variable frase con espacios al inicio y al final
frase = " Python es genial "

# Eliminar los espacios al inicio y al final
frase_sin_espacios = frase.strip()

# Contar el número de palabras contenidas en la frase
palabras_en_frase = len(frase_sin_espacios.split())

# Mostrar el resultado
print(f"La frase después de eliminar los espacios es: '{frase_sin_espacios}' ")
print(f"El número de palabras contenidas en la frase es: {palabras_en_frase}")
