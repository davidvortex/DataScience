# loop sirve para iterar para entrar dentro del un secuencia
for item in [0,1,2,3,4]:
    print(item)

for letras in "python":
    print(letras)

paises = ["mexco","argentina","Colombia"]

for Pais in paises:
    largo = len(Pais) #cuenta la cantidad de letras que tiene el arreglo paises
    print(f"{Pais} tiene {largo} letras ")

#verificar que la palabra tiene mayor de 5 letras
for p in paises:
    if len(p) > 5:
        print(p)

colores = ["azul","rojo","amarillo"]
prendas = ["sobrero", "gorra", "zapato"]

for color in colores:
    for prenda in prendas:
        print (color,prenda)

