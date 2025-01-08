import pandas as pd
# Lista de edades
edades = [23, 30, 26, 27, 22, 24, 25, 28]

df = pd.Series(edades)
promedio_edades = df.mean() #  .mean sirve para hacer el Promedio de todos los atributos

