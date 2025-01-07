import pandas as pd
frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])

filtro = frutas.str.contains("e")
frutas_con_e = frutas[filtro]
print(frutas[filtro])