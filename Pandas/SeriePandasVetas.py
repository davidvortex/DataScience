import pandas as pd

# Serie de ventas del mes
ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 190, 215, 275, 222, 218, 245, 233, 210, 290, 210,
                        215, 220, 225, 230, 245, 250, 260, 270, 280, 295])

total_ventas_mes = ventas_mes.sum()
print(total_ventas_mes)
dia_ventas_mas_bajas = ventas_mes.min()
print(dia_ventas_mas_bajas)
promedio_ventas_mes =  ventas_mes.mean()
print(promedio_ventas_mes)