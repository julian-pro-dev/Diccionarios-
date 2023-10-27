agenda_peliculas = []

def agregar_pelicula():
    nombre = input("Nombre de la película: ")
    genero = input("Género(s) separado por comas: ")
    año = int(input("Año de estreno: "))
    duracion = int(input("Duración en minutos: "))
    clasificacion = input("Clasificación por edad (todos/7+/13+/16+/18+): ")
    dia = input("Día de la semana para verla: ")
    hora = int(input("Hora de inicio (en formato de 24 horas): "))

    pelicula = {
        "Nombre": nombre,
        "Género": genero,
        "Año": año,
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
    # Busca la película en la agenda por su nombre
    pelicula = None
    for p in agenda_peliculas:
        if p["Nombre"] == nombre:
            pelicula = p
            break

    if pelicula:
        # Comprueba si hay un conflicto de horario
        conflicto = False
        for otra_pelicula in agenda_peliculas:
            if (
                otra_pelicula != pelicula and
                otra_pelicula["Día"] == nuevo_dia and
                otra_pelicula["Hora"] == nueva_hora
            ):
                conflicto = True
                break

        if not conflicto:
            if considerar_preferencias:
                if (
                    "Documental" in pelicula["Género"] and
                    nueva_hora >= 2200
                ):
                    print("No se puede reagendar la película de género Documental a esta hora para evitar dormirse.")
                elif (
                    "Drama" in pelicula["Género"] and
                    nuevo_dia == "Viernes"
                ):
                    print("No se puede reagendar la película de género Drama los Viernes para no entristecerse.")
                elif (
                    (nueva_hora >= 2300 or nueva_hora < 600) or
                    (nueva_hora < 1800 and nueva_hora >= 600 and nuevo_dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
                ):
                    print("No se puede reagendar la película en este horario para evitar trasnochar en semana.")
                else:
                    # Reagenda la película con el nuevo día y hora
                    pelicula["Día"] = nuevo_dia
                    pelicula["Hora"] = nueva_hora
                    print(f"La película '{nombre}' ha sido reagendada para el {nuevo_dia} a las {nueva_hora}.")
            else:
                # Reagenda la película sin considerar preferencias
                pelicula["Día"] = nuevo_dia
                pelicula["Hora"] = nueva_hora
                print(f"La película '{nombre}' ha sido reagendada para el {nuevo_dia} a las {nueva_hora}.")
        else:
            print("Conflicto de horario. No se puede reagendar la película.")
    else:
        print("La película no se encuentra en la agenda.")

def decidir_invitar(nombre_pelicula, edad_invitado, autorizacion_padres):
    # Busca la película en la agenda por su nombre
    pelicula = None
    for p in agenda_peliculas:
        if p["Nombre"] == nombre_pelicula:
            pelicula = p
            break

    if pelicula:
        clasificacion = pelicula["Clasificación"]

        if edad_invitado >= 18:
            print("Puedes invitar a la persona a ver la película, ya que es mayor de edad.")
        elif (
            edad_invitado < 15 and "Terror" in pelicula["Género"]
        ):
            print("No puedes invitar a personas menores de 15 años a ver esta película de género Terror.")
        elif (
            edad_invitado <= 10 and "Familiar" not in pelicula["Género"]
        ):
            print("Solo puedes invitar a personas de 10 años o menos a ver películas de género Familiar.")
        elif (
            not autorizacion_padres and not (
                "Documental" in pelicula["Género"] or
                clasificacion == "7+" or
                clasificacion == "todos"
            )
        ):
            print("El invitado necesita autorización de los padres para ver esta película.")
        else:
            print("Puedes invitar a la persona a ver la película.")
    else:
        print("La película no se encuentra en la agenda.")

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
        desde_ano = int(input("Ingrese el año de referencia: "))
        estrenos = buscar_estrenos(desde_ano)
        if estrenos:
            print(f"Estrenos a partir de {desde_ano}:")
            for estreno in estrenos:
                print(estreno["Nombre"])
        else:
            print("No hay estrenos en la agenda.")
    elif opcion == "5":
        cantidad_18_plus = contar_clasificacion_18_plus()
        print(f"Cantidad de películas con clasificación 18+: {cantidad_18_plus}")
    elif opcion == "6":
        nombre = input("Ingrese el nombre de la película a reagendar: ")
        nuevo_dia = input("Ingrese el nuevo día: ")
        nueva_hora = int(input("Ingrese la nueva hora (en formato de 24 horas): "))
        considerar_preferencias = input("¿Desea considerar sus preferencias? (Sí/No): ").lower()
        if considerar_preferencias == "sí":
            considerar_preferencias = True
        else:
            considerar_preferencias = False
        reagendar_pelicula(nombre, nuevo_dia, nueva_hora, considerar_preferencias)
    elif opcion == "7":
        nombre_pelicula = input("Ingrese el nombre de la película que desea invitar: ")
        edad_invitado = int(input("Edad del invitado: "))
        autorizacion_padres = input("¿Tiene autorización de los padres? (Sí/No): ").lower()
        if autorizacion_padres == "sí":
            autorizacion_padres = True
        else:
            autorizacion_padres = False
        decidir_invitar(nombre_pelicula, edad_invitado, autorizacion_padres)
    elif opcion == "8":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
