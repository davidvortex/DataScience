paises = ['Francia', 'Alemania', 'España', 'Italia', 'Chile']

for pais in paises:
    # Contar la cantidad de letras "a" en el nombre del país actual
    letra_a = pais.lower().count("a")
    if letra_a > 0:
        print(pais)
