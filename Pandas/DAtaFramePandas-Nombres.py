import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
#en esta parte nos sive para aunmenta 10 años mas
df['Edad_en_10_años'] = df['Edad'] + 10
print(df)

#esta parte las palabras en mayusculas
df['Ciudad'] = df['Ciudad'].str.upper()
print(df)

#aqui solo se toman en cuenta lo mayor que son
df['Es_Mayor_de_25'] = df['Edad'] >= 25
print(df)