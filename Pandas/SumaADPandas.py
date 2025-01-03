import pandas as pd
serie_desde_diccionario =  pd.Series({'a':30, 'b':70, 'c':160, 'd':50})
suma_ad = serie_desde_diccionario['a'] + serie_desde_diccionario['d']

def imprimir_suma_ad():
    print(suma_ad)

