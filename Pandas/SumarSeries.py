import pandas as pd
serie =  pd.Series([ 10, 20 , 30, 40, 50])
print(serie)
print("serie sin movimientos")
serie[0] = serie[0] + 10 # de esta manera solo sumo una sola parte de mi indice o el objetivo 
print(serie)
print("serie sumar 10+10 al indice 0")

serie = serie + 10 # para sumar toda la siere sumarle todos los valores mas 10
# los resultados deberias de sumar 20,30....
print(serie)
print("serie con sumatoria de 10")
serie = serie * 2 # para que toda la serie sea multiplicado por 2
# resultados serian que los numero mostrados deberian ser 40,60,...  etc
print(serie)
print("serie con multiplicacion")






