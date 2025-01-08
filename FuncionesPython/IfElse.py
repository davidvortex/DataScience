calificacion= int(input("Ingrese su calicacion: "))  # Si quieres pedir la calificación al usuario
# calificacion = 8  # Calificación predefinida para probar el código

if calificacion > 10:
    print("Calificación no válida")
elif calificacion >= 9:  # Para calificaciones 9 o 10
    print("Sobresaliente")
elif calificacion >= 7:  # Para calificaciones entre 7 y 8
    print("Notable")
elif calificacion >= 5:  # Para calificaciones entre 5 y 6
    print("Aprobado")
else:  # Si la calificación es menor a 5
    print("Insuficiente")
