frutas = ["manzana","aceituna","kiwi","sandia"]
type (frutas)

BolsaDeNumeros = [1,3,4,5]
MiNumeros = [2,1,6 ],["A","b","C"],["reyes","hernandez","sanhcez"]

print(frutas[0])

#con el primer cochete seleccionamos la lista en este caso 2 tenemos 
#que iniciar desde 0 despues de seleccionar dentro de la lista selecionamos el dato
print(MiNumeros[2][1])

#esta linea de codigo agrega al arreglo mas datos
frutas.append("papaya")
print(frutas)

frutas.sort()
#hace que la lista este de forma ordenada
print(frutas)

frutas.sort(reverse = True)
#hace que la lista este de forma ordenada pero al reverso
print(frutas)

frutas.remove("manzana")
#esta linea borra la palabra reservada manzana
print(frutas)

len(frutas)

lista = [1,2,3,4,5]
lista2 = [6,7,8,9]
combinacion = lista + lista2
print(combinacion)

type(combinacion)

repetir = lista * 2
print(repetir)

SubLista = combinacion[1:6]
print(SubLista)

