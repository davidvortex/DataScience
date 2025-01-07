import pandas as pd

serie_numeros = pd.Series(list(range(1,21)))
filtro = serie_numeros > 10
print(filtro)

