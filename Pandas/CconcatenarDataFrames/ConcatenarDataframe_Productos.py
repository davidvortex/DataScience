import pandas as pd

ventas_enero = pd.DataFrame({
    'Producto': ["Manzanas", "Bananas", "Naranjas"], 
    'Cantidad': [300, 200, 150]
})
ventas_febrero = pd.DataFrame({
    'Producto': ["Manzanas", "Bananas", "Naranjas"], 
    'Cantidad': [350, 210, 170]
})

ventas_total = pd.concat([ventas_enero,ventas_febrero], ignore_index = True)
print(ventas_total)