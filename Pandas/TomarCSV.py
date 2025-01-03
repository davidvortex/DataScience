import pandas as pd
df = pd.read_csv("/Users/david/Downloads/Precipitaciones.csv")
# presenta la cabeza pero maximo mostrara 5 datos
print(df.head())

# presenta la parte de la cabeza a diferenca del otro puedo decif que este llega a 3 por que tiene limitacion
print(df.head(3))

# presenta la parte de las colas y tomara los datos los ultimos 5
print(df.tail())

# nos dira primero la cantidad de filas y despues nos arrojara la cantidad de columnas ejemplo(12,3) 12 filas, 3 columnas
print(df.shape)

# Lista de los encabezado de nuestra base de datos
print(df.columns())

# de vuelve una lista de informacion la cal contiene
print(df.info())

# Lista de los encabezado de nuestra base de datos
print(df.describe())



