import pandas as pd
empleados = {"nombre":["Ana","Luis","Carlos"], "edad":[30,25,40]}
df_empleados = pd.DataFrame(empleados)
shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index
print(shape_df)
print(columns_df)
print(index_df)