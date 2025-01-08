import pandas as pd
df = pd.read_csv("Pandas/medallas.csv")
encabezado = df.head()
final = df.tail()
print(encabezado)
print(final)
#hacer que los valores NaN tenga un valor a 0
df.isnull

valores_nuevos = {"Oro":0, 
                  "Plata":0,
                  "Bronce":0
                  }
df_rellenar = df.fillna (valores_nuevos) # aqui lo que hago es reemplazar los valores que no tengo para reemplazarlos
print(df_rellenar)

# tambien puede valer esta linea de codigo
# df_rellenar = df.fillna(0)
# print(df_rellenar)

# o tambien se puede realizar otro conmando mas simple
# df.fillna(0, inplace=True)
# print(df)

# Rellenar valores nulos con 0 y luego convertir a tipo entero
df["Oro"] = df["Oro"].fillna(0).astype(int)
df["Plata"] = df["Plata"].fillna(0).astype(int)
df["Bronce"] = df["Bronce"].fillna(0).astype(int)
print(df)

df_ordenado = df.sort_values(by="Oro", ascending=False) # sort.values ordena los valores de un eje que yo elija folse sirve para hacerlo de mayor a menos, true del menos a mayor
top_oro = df_ordenado.head(3)
print(top_oro)

# otra manera de hacer esta linea de codgigo seria de la siguiente manera
# df_ordenado = df.sort_values(by="Oro", ascending=false).head(3)
# prin(df_ordenado)

print("Aqui en esta parte es para saber quien tiene mas de 10 medallas")

# Filtrar las filas donde 'Total' sea mayor a 10
filtro = df['Total'] > 10
serie_medallas10 = df[filtro]  # Genera un DataFrame filtrado

# Ordenar por la columna 'Total' en orden decendente los 3 primeros
serie_medallas10 = serie_medallas10.sort_values(by='Total', ascending=False).head(3)

# Imprimir el DataFrame resultante
print(serie_medallas10)







