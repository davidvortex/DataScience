import pandas as pd

cursos = pd.DataFrame({
    'curso_id': [101, 102, 103],
    'nombre_curso': ['Introducción a Python', 'Data Science con Python', 'Machine Learning Avanzado']
})

inscripciones = pd.DataFrame({
    'curso_id': [102, 102, 101, 104],
    'fecha_inscripcion': ['2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']
})

cursos_inscripciones = pd.merge(inscripciones,cursos, how='left')
print(cursos)