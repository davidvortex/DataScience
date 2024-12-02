t = 1,2
#Es te tipo de dato es de tipo tupla
type(t)

tt=1,2
#dato dd tipo tupla
type(tt)

tm = ("fernando", "raul", 50)
#tipo de dato es de tupla
type(tm)

tupla=[1,2,3,4,5]
elemento = tupla[2]
print(elemento)

SubTupla = tupla[1:3]
print(SubTupla)

tupla[1] = 8
tupla.count(2)
# tupla.index[3]
print(tupla)

#la tupla puede se desempaquegar
tupla2 = (1,2,3)
#aqui puedo hacer una referencia a la tubla
a,b,c =tupla2
#las tuplas ayuda a haber que tipo de valor y sea de manera seguro
print(c)

nacimiento = (1986 , 9, 25)
nombre =("david", "jesus")
cliente = (nombre,nacimiento)

#una manera para acceder a los datos que tiene mis tuplas es de la siguente manera
print(cliente[0][1])

# las tublas sirven para no modificar y tambine se puede usar una tubla de variables
autos = ("Mark2","azul","Generico", 2023, 5, 2.16)
(marca , color, tipo, año, cilindros, motor) = autos
print(año,color)


