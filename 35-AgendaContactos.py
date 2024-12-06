# Diccionario para almacenar los contactos y no perder los datos ingresados al momento
contactos = {}


while True:
    # Imprimir el menú de opciones
    print("\n* Agenda de contactos *")
    print("1- Agregar Contactos")
    print("2- Buscar Contacto")
    print("3- Editar contacto")
    print("4- Eliminar contacto")
    print("5- Mostrar todos los contactos")
    print("6- Salir")

    # Captura la entrada del usuario con manejo de errores
    try:
        # debo de hacer una variable de tipo entero para que cargue bien el try y se ejecute bien el problema
        # esto pasa por que necesito una variable de tipo entero el cual el try necesita un valor para tomar lo en cuenta
        respuesta = int(input("Ingrese lo que desea realizar: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue  # Vuelve al menú sin hacer nada si la entrada es inválida

    # Agregar contacto
    if respuesta == 1:
        nombre = input("Ingrese el nombre del contacto: ") # ingresamos el valor de la variable nombres
        telefono = input("Ingrese su teléfono: ") #ingresamos el valor de telefono
        contactos[nombre] = telefono # auqi se carga los contactos que se registro al momento
        print(f"Contacto {nombre} con el numero {telefono} fue agregado.") # imprimimos el nombre y telefono

    # Buscar contacto
    elif respuesta == 2:
        nombre_buscar = input("¿Qué contacto quieres buscar? ")
        #lo que quiero hacer aqui es hacer la sentencia que busque en el arreglo mediante la variable que apenas le meti
        if nombre_buscar in contactos:
            # aqui solo presenta el nombre de la variable buscada
            print(f"Contacto encontrado: {nombre_buscar} - {contactos[nombre_buscar]}")
        else:
            # solo en caso de que no encuentre dentro de mi arreglo
            print("Contacto no encontrado.")

    # Editar contacto
    elif respuesta == 3:
        nombre_editar = input("Ingrese el nombre del contacto a editar: ")
        # busque el nombre dentro de contactos para editarlo
        if nombre_editar in contactos:
            #ingresar nuevo numero
            nuevo_telefono = input(f"Ingrese el nuevo teléfono para {nombre_editar}: ")
            # editamos solo el numero del contacto
            contactos[nombre_editar] = nuevo_telefono
            print(f"Contacto {nombre_editar} actualizado.")
        else:
            print("Contacto no encontrado.")

    # Eliminar contacto
    elif respuesta == 4:
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre_eliminar in contactos:
            # aqui lo que hace esta linea es buscar en el diccionario para eliminar
            del contactos[nombre_eliminar]
            print(f"Contacto {nombre_eliminar} eliminado.")
        else:
            print("Contacto no encontrado.")

    # Mostrar todos los contactos
    elif respuesta == 5:
        if contactos:
            print("A continuación se presentan todos los contactos:")
            for nombre, telefono in contactos.items():
                print(f"{nombre}: {telefono}")
        else:
            print("No hay contactos en la agenda.")

    # Opción para salir
    elif respuesta == 6:
        print("Gracias por usar la agenda. ¡Hasta luego!")
        break  # Sale del bucle y termina el programa

    else:
        print("Opción no válida. Por favor, ingrese de nuevo dato")

