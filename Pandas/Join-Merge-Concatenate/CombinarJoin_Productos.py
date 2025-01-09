import pandas as pd

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID') # El set_index normal mente lo usare de id 

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID') #el set_index normal mente lo usare como id

df_combinado =  productos_df.join(categorias_df)
print(df_combinado)