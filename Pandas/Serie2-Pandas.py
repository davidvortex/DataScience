import pandas as pd
serie_con_indices = pd.Series([10,20,30,40],['a','b','c','d'])
valor_c = serie_con_indices['c']

def imprimir_valor_c():
    print(valor_c)

print(imprimir_valor_c)


