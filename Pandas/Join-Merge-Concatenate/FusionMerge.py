import pandas as pd
df_inicial = pd.DataFrame({
    'id':[1,2,3],
    'nombre':['david','jesus','rut']
    })
df_secundario = pd.DataFrame({
    'id':[1,2,3],
    'edad':[12,23,12]
    })

df_combinar = pd.merge(df_inicial,df_secundario, on='id', how='inner' ) 
# para how hay tres tipos de casos innner = por defecto, outer = retornar en 2 dataframe, left = incluir las filas del data frame a la izquierda
# right =incluir las filas del data frame a la derecha
print(df_combinar)

df_conjuntoIndex = pd.merge(df_inicial,df_secundario, left_index=True, right_index=True)
print(df_conjuntoIndex)





