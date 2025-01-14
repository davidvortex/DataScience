import pandas as pd

#creamos nuestros data Frame Con el producto y estos se aran en uno solo seran 2 serieas y 1 dataframe
tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 'Cantidad': [500, 300]})
tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 'Cantidad': [400, 250]})

# Concatenamos tiena a y tienda b para juntarlos y tener la separacion del producto
ventas_tienda = pd.concat([tienda_a, tienda_b], keys=['Tienda A','Tienda B'])
print(ventas_tienda)
