import pandas as pd

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})
productos_df = productos_df.set_index('ProductoID')


categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')
df_combinado = categorias_df.join(productos_df, how='right') #en mi data frame la estoy combianndo para meter mis datos a la 
print(df_combinado)

