import pandas as pd
df = pd.read_csv("/Users/david/Downloads/Precipitaciones.csv")
print(df.head())

serie = df["region"]
print(serie.head(3))


datos = [20,30,40,50]
serie2 = pd.Series(datos)
print(serie2)

indice = ['a','b','c','d']
serie2 = pd.Series(datos,indice)
print(serie2)

print(serie[40])

# Crear series a partir de diccionarios
control = { "razer": "blue",
           "octupus": "dark",
           "gamekill": "yellow",
            "Sony": "withe"
}

serie3 = pd.Series(control)
print(serie3)
print(serie3["withe"])

