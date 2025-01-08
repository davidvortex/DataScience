import pandas as pd
data = { "Id_producto":[1001,1002,1003,1003],
        "Cantidad_vendida":[30,None,25,25],
        "Precio":[20.5, 15.0, None, 22.5]
}

df = pd.DataFrame(data)
print(data)

# Solucionar problmeas de datos duplicados
df.isnull() #datos nulos de nuestro dataframe
df.isnull().sum() # esto nos ayuda  a sumar las casillas que tenemos null practicamente hace un contador
df_eliminar = df.dropna() #simple mente elimino los valores que tenga en mi dataframe
print(df_eliminar)

# Los valores que deseo eliminar deberan ser como estan en dataframe o en el excel ya de no ser asi no se aplicaran las correcciones
valores_nuevos = {"Cantidad_vendida":0, # Aqui hago que mi cantidad vendida los que tengan un NaN sean reemplazados por cantidad venida
                  "Precio":df["Precio"].mean() # Aqui lo que hago es hacer que las NaN tengan un promedio de los Precios
                  }
df_rellenar = df.fillna (valores_nuevos) # aqui lo que hago es reemplazar los valores que no tengo para reemplazarlos
print(df_rellenar)

# Correcion de tipos de datos
df_rellenar["Cantidad_vendida"] = df_rellenar["Cantidad_vendida"].astype(int)
print(df_rellenar)

# ver si hay duplicados y no querer duplicados
df_unicos = df_rellenar.drop_duplicates() # eliminar solo si todo es igual del producto
print(df_unicos)

df_unicos = df_rellenar.drop_duplicates(subset="Id_producto") #elimina una parte donde este igual aqui lo buscamos por el producto
print(df_unicos)

