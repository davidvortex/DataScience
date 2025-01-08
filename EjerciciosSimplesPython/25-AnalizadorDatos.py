#esta linea sirve para agregar texto
texto = input("texto de almenos 10  palabras")

# contar numeros en texto
Nu_caracterristicas = len(texto)
Nu_caracterristicas

#contar numeros con caracteres sin incluir espacios
NumEspacios = texto.count(" ")
NumCaracteresSinEspacio = Nu_caracterristicas - NumEspacios
NumCaracteresSinEspacio

#contar numero de vocales 
a = texto.count("a")
e = texto.count("e")
i = texto.count("i")
o = texto.count("o")
u = texto.count("u")
vocales = a+e+i+o+u

NumeroPalabras = NumEspacios + 1
print(NumeroPalabras)

#para borrar la primera palabra
primero_espacio = texto.find(" ")
BorrarPalabra = texto[primero_espacio + 1]

#la siguiente linea de codigo nos ayuda para reemplazar lo que queresmos buscar
guiones = texto.replace(" " , "-")
guiones


alcontrario= texto.swapcase()


print(f"El numero de caractere es {Nu_caracterristicas}")
print(f"y si no contamos los espacios tienes {NumCaracteresSinEspacio} caracteres")
print(f"de los caracteres de tecto hay {vocales} que son volcaes")
print(f"si contamos las palabras con el texto tiene {NumeroPalabras} palabras")
print(f"eliminamos la primera palabra que daria asi: {BorrarPalabra}")
print(f"cambiamos o reemplazamos la palabra con: {guiones}")
print(f"cambiamos mayusuclas por minusculas y queda:{alcontrario}")
