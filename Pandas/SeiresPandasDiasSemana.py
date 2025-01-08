import pandas as pd
ventas = [120, 150, 90, 200, 210, 130, 160]
dias_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado', 'Domingo']

serie = pd.Series(ventas,dias_semana)
suma_total_ventas = serie.sum()
dia_mayores_ventas =  serie.max()
promedio_ventas = serie.mean()

print(suma_total_ventas)
print(dia_mayores_ventas)
print(promedio_ventas)