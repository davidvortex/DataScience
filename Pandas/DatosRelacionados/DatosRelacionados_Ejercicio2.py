import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('fechas.csv')
 
# Convertir la columna de fechas de string a datetime en el formato año/mes/dia
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y/%m/%d')
 
# Cambiar el formato de la fecha a día/mes/año
df['fecha'] = df['fecha'].dt.strftime('%d/%m/%Y')