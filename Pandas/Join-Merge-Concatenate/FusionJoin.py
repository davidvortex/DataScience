import pandas as pd
df1 = pd.DataFrame({
    'Salario':[3000,2000,4000],
    'Antiguedad':[9,13,25]},
    index=[1,2,3]
)
df2 = pd.DataFrame({
    'Cuidad':["Madrid","Barcelona","Valencia"],
    'Jerarquia':["Baja","Media","Alta"]},
    index=[1,2,4]
)

# aqui solo une o combina las tablas o los diccionarios aun que on partenesca o no tenfan datos aun que tengan la misma cantidad el indice no es igual
df_unir = df1.join(df2)
print(df_unir)

# aqui esta parte solo acepta las interceciones las cuales son las que unen solo asi los presenta o los imprime
df_unir = df1.join(df2, how='inner')
print(df_unir)

