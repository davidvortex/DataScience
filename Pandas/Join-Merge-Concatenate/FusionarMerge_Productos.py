import pandas as pd

productos = pd.DataFrame({
    'ID': [10, 11, 12],
    'Nombre': ['Teclado', 'Mouse', 'Monitor'],
    'Marca': ['Logitech', 'Razer', 'Dell']
})

reviews = pd.DataFrame({
    'ID': [10, 11, 12],
    'Calificación': [5, 4, 4],
    'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
})

productos_reviews = pd.merge(productos, reviews, left_index=True, right_index=True)