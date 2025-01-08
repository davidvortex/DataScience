import pandas as pd
valores = pd.Series([18, 22, 7, 9, 15, 8])

condicion_valores_pares = valores % 2 == 0
print(valores[condicion_valores_pares])