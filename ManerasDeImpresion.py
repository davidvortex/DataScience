saludo = "hola"
nombre = "david"
frase = nombre +" "+nombre

edad = 24

frase2 = saludo +" "+nombre+ "tu edad: "+str(edad)+"años"
print(frase2)
frase3=("HOLA {} tienes {} años.".format(nombre,edad))
print(frase3)
frase4 = f"hola {nombre}, tu edad es:{edad} años"
print(frase4)