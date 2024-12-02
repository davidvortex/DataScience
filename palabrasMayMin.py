frase = "hola mundo"
type(frase)

print(frase)

#Para hacer la palbra mayuscula pero solo se aria una vez
frase.upper()
print(frase)
print(frase)
#ahora para siempre conservarla en mayuscula se tiene que convertir en una nueva variable ejemplo
fraseMayuscula = frase.upper()
print(fraseMayuscula)

dir(frase)
#explica para que sirve la funcion
help(frase.capitalize())

#esta funcion sirve para que la primera letra de la palabra inicie con la letra mayuscula
frase.capitalize()