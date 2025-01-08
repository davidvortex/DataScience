import pandas as pd

libros = {
    "Titulo":["El Quijote", "Cien años de soledad", "La odisea"],
    "Autor":["Miguel de Cervantes", "Gabriel García Márquez", "Homero"],
    "Año":[1605,1967,-800]
}

libros_df = pd.DataFrame(libros)