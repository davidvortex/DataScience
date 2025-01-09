import pandas as pd

datos_cliente = pd.DataFrame({
    'Nombre': ["Ana", "Luis", "Marta"], 
    'Edad': [34, 45, 28]
})
compras_cliente = pd.DataFrame({
    'Producto': ["Libro", "Lápiz", "Cuaderno"], 
    'Precio': [15.50, 0.50, 2.00]
})

info_cliente = pd.concat([datos_cliente,compras_cliente], axis =1)
