# Definir las variables
producto = "papas"
cantidad = 10 # Cantidad de producto
precio_por_unidad = 0.30  # Precio por unidad del producto

# Calcular el precio total
precio_total = cantidad * precio_por_unidad

# Imprimir la frase utilizando un f-string
print("Hay {} {} con un precio total de {}.".format(cantidad,producto,precio_total))
