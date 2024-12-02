#creamos una tupla
info_ciudades = (("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), ("Tokio", 13929286, "Japón"))
([EstadoArg,PoblacionArg,PaisArg],[EstadoEsp,PoblacionEsp,PaisEsp],[EstadoJap,PoblacionJap,PaisJap]) = info_ciudades

print(f"La ciudad de {EstadoArg} en {PaisArg} tiene una población de {PoblacionArg} habitantes")
print(f"La ciudad de {EstadoEsp} en {PaisEsp} tiene una población de {PoblacionEsp} habitantes")
print(f"La ciudad de {EstadoJap} en {PaisJap} tiene una población de {PoblacionJap} habitantes")