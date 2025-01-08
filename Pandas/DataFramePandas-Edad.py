import pandas as pd

# Datos proporcionados
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data) # hacemos el diccionario
df_filtrado = df[df['Edad'] >= 25] #hacemos la condicion que deben ser igual o mayor de 25