import pandas as pd
df = pd.read_csv("Pandas/medallas.csv")
encabezado = df.head()
final = df.tail()
print(encabezado)
print(final)

df.isnull


valores_nuevos = {"Oro":0, 
                  "Plata":0,
                  "Bronce":0
                  }
df_rellenar = df.fillna (valores_nuevos) # aqui lo que hago es reemplazar los valores que no tengo para reemplazarlos
print(df_rellenar)


df_ordenado = df.sort_values(by="Oro", ascending=False)
top_oro = df_ordenado.head(3)
print(top_oro)

print("Aqui en esta parte es para saber quien tiene mas de 10 medallas")
filtro = df["Total"] > 10  #hago referencia a el excel el que tenga mas de 10 en total
serie_medallas10 = df[filtro] #lo que quiero hacer es un filtro el cual obtiene dataframe
print (serie_medallas10) #llamo a la variable que obtiene los resultados




