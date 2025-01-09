import pandas as pd

# Creación del DataFrame df_a
df_a = pd.DataFrame({ #diccionario
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True) # por el valor por los que los busco para combinar


# Creación del DataFrame df_b
df_b = pd.DataFrame({ # diccionario
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True) # por el valor por los que los busco para combinar


df_combinado = df_a.join(df_b)
print(df_combinado)

