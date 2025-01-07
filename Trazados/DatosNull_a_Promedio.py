import pandas as pd
    
data = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]
    
}
df = pd.DataFrame(data)
valores_nuevos = {"Precio":df["Precio"].mean() # Aqui lo que hago es hacer que las NaN tengan un promedio de los Precios
                  }
df_rellenar = df.fillna (valores_nuevos) # aqui lo que hago es reemplazar los valores que no tengo para reemplazarlos
print(df_rellenar)