import pandas as pd
print("Modificar los dias 1 modo")
fechas = pd.Series(pd.date_range('20240201', periods=6))
print(fechas)

print("modidificar los dias 2 modo")
# Modifica el dia
fechas = pd.Series(pd.date_range('20240201', periods=8,freq='D'))
print(fechas)

print("Modificar los meses")
# Modifica el mes
fechas = pd.Series(pd.date_range('20240201', periods=8,freq='M'))
print(fechas)

print("Modoficar los años para el perdiodo")
# Modificia el año
fechas = pd.Series(pd.date_range('20240201', periods=8,freq='Y'))
print(fechas)

print("Modoficar los tiempo")
# Modificia el año
fechas = pd.Series(pd.date_range('20240201', periods=8,freq='MIN'))
print(fechas)

print("Modoficar los tiempo con saltos")
# Modificia el año
fechas = pd.Series(pd.date_range('20240201', periods=8,freq='5D'))
print(fechas)

df = pd.read_csv("Pandas/Join-Merge-Concatenate/Mercado.csv")
print(df)

print(df['Fecha'][0])

print(type(df['Fecha'][0])) # este me ayudara para identificar que tipo de dato o esta utilizando el excel
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
print(df)

