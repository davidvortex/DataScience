import pandas as pd

data = {
    'Nombre': ['Ana','Luis','Carlos','Sara'],
    'Edad':[25,30,22,27],
    'cuidad':['Madrid','Barcelona','Valencia','Bilbao']
}

df = pd.DataFrame(data)
print(df)

df['Salario'] = [3000, 4500, 3800 , 3200]
print(df)
df['Salario'] = df['Salario'] + 200
print(df)

