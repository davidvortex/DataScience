#implementamos DoWhile

contador = 0

while contador < 5:
    print(contador)
    contador += 1

print(" ")
print(" ")
# break corta la estructura de control
# continue sirve para continuar la estructura de control
contador1 = 0
while contador1 < 10:
    contador1 += 1
    print(f"conteo {contador1}")
    if contador1 == 5:
        print("apunto de terminar")
        print(contador1)
        continue
    if contador1 == 8:
        #terminare el contador del numero
        print(f"llegue a {contador1} termino")
        break
        #break corta el ciclo



