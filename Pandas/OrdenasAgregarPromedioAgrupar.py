import pandas as pd
datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E'],
    'género': ['Acción', 'Drama', 'Acción', 'Comedia', 'Drama'],
    'rating': [7.2, 8.5, 9.1, 6.5, 7.8]
}

df = pd.DataFrame(datos)
promedio_rating_por_genero = df.groupby('género')['rating'].mean()
