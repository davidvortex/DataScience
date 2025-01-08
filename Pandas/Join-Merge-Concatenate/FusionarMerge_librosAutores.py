import pandas as pd

libros = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 'El Principito']
})
autores = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 'J.K. Rowling']
})

libros_autores = pd.merge(libros,autores, how = 'outer')