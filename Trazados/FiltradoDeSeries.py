# El filtrado de Series es como hacer una pregunta sobre nuestros datos y nos contestan
import pandas as pd
data = pd.Series([5,10,15,20,25])
filtro = data > 15
serie_filtrada = data[filtro]
print(serie_filtrada)


serie2 = pd.Series(["banana","manzana","melon","sandia"])
filtro2 = serie2.str.contains("m") # esto lo que hace que me da una lista de los cuales son falsos y verdaderos con los cuales tienen la letra m
print(filtro2)# muestra si contienen la m como verdadero o falso
# para solicitar es primero la serie y despues el filtrado
print(serie2[filtro2])# me arroja los datos con tienen la letra m

