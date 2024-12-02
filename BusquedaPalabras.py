palabra =  "coronado"
type(palabra)

dir(palabra)

print(palabra.count("a"))

oracion = "Yo estoy Jugando videojuegos"
print(oracion.count(" "))
print(oracion.count(" ") + 1)

#no conto los spacios de los laterales
oracion1 = " Yo estoy Jugando videojuegos "
print(oracion1.strip().count(" ") + 1)

print(oracion1.strip().split(" "))
