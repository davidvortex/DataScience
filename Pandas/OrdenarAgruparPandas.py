import pandas as pd
df = pd.read_csv("Pandas/Top-Peliculas.csv")

df_ordenado2 = df.sort_values(by="rating", ascending=False)
print(df_ordenado2.head(10))
print("###################################")

df_ordenado = df.sort_values(by=['rating','recaudación(M)'], ascending=False)
print(df_ordenado.head(10))
print("###################################")

#agrupaciones
df_agrupacion = df.groupby('género')['rating'].mean()
print(df_agrupacion)
print("###################################")

df_agrupacion2 = df.groupby('año')['recaudación(M)'].mean()
print(df_agrupacion2)

print("###################################")

#agrupacion por suma de recaudacion de los años
df_agrupacion3 = df.groupby('año')['recaudación(M)'].sum()
df_agrupacion3.sort_values(ascending=False).head(10)
print(df_agrupacion3)

print("###################################")








