import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]
}

df = pd.DataFrame(data)
df_sin_duplicados = df.drop_duplicates(subset="ID")
print(df_sin_duplicados)