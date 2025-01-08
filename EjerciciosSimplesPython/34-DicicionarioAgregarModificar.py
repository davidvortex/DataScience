edades = {"Juan": 28, "Elena": 32, "Marcos": 17}

# cambiar el valor de juan
edades["Juan"] = 29
print(edades.get("Juan"))

# imprimir solo el Valor de elena
print(edades.get("Elena"))

# y agregar a luisa
edades["Luisa"] = 25
print(edades)