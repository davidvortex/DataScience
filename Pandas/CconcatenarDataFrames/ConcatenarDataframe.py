import pandas as pd
df1 = pd.DataFrame({
    'nombre':["Gabriela","Juan","elena"],
    'edad':[23,31,21]
    })
df2 = pd.DataFrame({
    'nombre':["Carmela","Max","Laura"],
    'edad':[34,25,91]
    })

#contenido concatenado forma verticzal
df_concatenado = pd.concat([df1, df2]) 
print(df_concatenado)
print("################################")

# contenido concatenado forma horizontal
df_concatenado2 = pd.concat([df1, df2], axis=1)
print(df_concatenado2)
print("################################")

# contenido concatenado elimnando que el contado em vez de inicar desde 0 el contados siga
df_concatenado3 = pd.concat([df1, df2], ignore_index=True)
print(df_concatenado3)
print("################################")

# contenido concatenado en esta parte se agrega los valores donde dice la cantidad de cada dataset ejemplo
#       nombre  edad
#df1 0  Gabriela    23
#    1      Juan    31
#    2     elena    21
#df2 0   Carmela    34
#    1       Max    25
#    2     Laura    91
df_concatenado4 = pd.concat([df1, df2],keys=['df1','df2'])
print(df_concatenado4)
print("################################")

# tambien puede funcionar como un separador o un marcador en caso de algo importante
df_concatenado5 = pd.concat([df1, df2],keys=['Enero','Fabrero'])
print(df_concatenado5)
print("################################")

