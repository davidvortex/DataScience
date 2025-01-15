import pandas as pd

df = pd.read_csv('fechas.csv')

# convertir la colmna a tipo de dato a dia
df['fecha'] = pd.to_datetime(df['fecha'], format='%d-%m-%Y')

# que la fecha tenga un salto de dias de 5
df['fecha'] = df['fecha'] +  pd.Timedelta(days=5)