import pandas as pd
df = pd.read_csv("/Users/david/Downloads/Precipitaciones.csv")
# presenta la cabeza pero maximo mostrara 5 datos
print(df.head())
# presenta la parte de la cabeza a diferenca del otro puedo decif que este llega a 3 por que tiene limitacion
print(df.head(3))
# presenta la parte de las colas
print(df.tail())

print(df.shape)




