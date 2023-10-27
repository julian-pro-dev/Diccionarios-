agenda_peliculas = []

def agregar_pelicula():
    nombre = input("Nombre de la película: ")
    genero = input("Género(s) separado por comas: ")
    ano = int(input("Año de estreno: "))
    duracion = int(input("Duración en minutos: "))
    clasificacion = input("Clasificación por edad (todos/7+/13+/16+/18+): ")
    dia = input("Día de la semana para verla: ")
    hora = int(input("Hora de inicio (en formato de 24 horas): "))

    pelicula = {
        "Nombre": nombre,
        "Género": genero,
        "Año": ano,
        "Duración": duracion,
        "Clasificación": clasificacion,
        "Día": dia,
        "Hora": hora
    }
    
    agenda_peliculas.append(pelicula)
    print("Película agregada a la agenda.")

def pelicula_mas_larga():
    if not agenda_peliculas:
        return None

    pelicula_mas_larga = max(agenda_peliculas, key=lambda x: x["Duración"])
    return pelicula_mas_larga

def duracion_promedio():
    if not agenda_peliculas:
        return "00:00"

    total_duracion = sum(pelicula["Duración"] for pelicula in agenda_peliculas)
    duracion_promedio_minutos = total_duracion / len(agenda_peliculas)
    horas, minutos = divmod(duracion_promedio_minutos, 60)
    return f"{int(horas):02d}:{int(minutos):02d}"

def buscar_estrenos(desde_ano):
    estrenos = [pelicula for pelicula in agenda_peliculas if pelicula["Año"] >= desde_ano]
    return estrenos

def contar_clasificacion_18_plus():
    return len([pelicula for pelicula in agenda_peliculas if pelicula["Clasificación"] == "18+"])

def reagendar_pelicula(nombre, nuevo_dia, nueva_hora, considerar_preferencias):
    # Implementa la lógica para reagendar la película
    pass

def decidir_invitar(nombre_pelicula, edad_invitado, autorizacion_padres):
    # Implementa la lógica para decidir si puedes invitar a alguien
    pass

while True:
    print("\nMenú de Opciones:")
    print("1. Agregar Película")
    print("2. Consultar Película Más Larga")
    print("3. Consultar Duración Promedio")
    print("4. Buscar Estrenos")
    print("5. Contar Películas 18+")
    print("6. Reagendar Película")
    print("7. Decidir Invitar")
    print("8. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6/7/8): ")

    if opcion == "1":
        agregar_pelicula()
    elif opcion == "2":
        pelicula_larga = pelicula_mas_larga()
        if pelicula_larga:
            print("Película más larga:")
            print(pelicula_larga)
        else:
            print("No hay películas en la agenda.")
    elif opcion == "3":
        promedio = duracion_promedio()
        print(f"Duración promedio de las películas en la agenda: {promedio}")
    elif opcion == "4":
        ano = int(input("Ingrese el año de referencia: "))
        estrenos = buscar_estrenos(ano)
        if estrenos:
            print(f"Estrenos a partir de {ano}:")
            for estreno in estrenos:
                print(estreno["Nombre"])
        else:
            print("No hay estrenos en la agenda.")
    elif opcion == "5":
        cantidad_18_plus = contar_clasificacion_18_plus()
        print(f"Cantidad de películas con clasificación 18+: {cantidad_18_plus}")
    elif opcion == "6":
        # Llama a la función para reagendar una película
        pass
    elif opcion == "7":
        # Llama a la función para decidir si puedes invitar a alguien
        pass
    elif opcion == "8":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
