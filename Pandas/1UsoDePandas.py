import pandas as pd
datos = {'nombre':['Pedro','Juan','lorena'],'edad':[25,30,19]}
df = pd.DataFrame(datos)
type(df)
print(df["nombre"])
print(df["edad"])
