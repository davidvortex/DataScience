import pandas as pd

datos_clima =  pd.read_csv("clima.csv")

#extraer el primer dato
head_df = datos_clima.head(1)
#extraer el el ulitmo dato
tail_df = datos_clima.tail(1)