# Crear un diccionario para realizar un seguimiento de las puntuaciones de los jugadores
puntuaciones = {}

# Función para permitir a los jugadores acumular puntos
def acumular_puntos():
    nombre = input("Ingrese el nombre del jugador: ")
    puntos = int(input("Ingrese la cantidad de puntos a sumar: "))
    
    if nombre in puntuaciones:
        puntuaciones[nombre] += puntos
    else:
        puntuaciones[nombre] = puntos
    print(f"{nombre} ha acumulado {puntos} puntos.")

# Función para mostrar la puntuación total de cada jugador
def mostrar_puntuaciones():
    print("Puntuaciones de los jugadores:")
    for jugador, puntuacion in puntuaciones.items():
        print(f"{jugador}: {puntuacion} puntos")

# Función para anunciar al jugador con la puntuación más alta
def jugador_con_puntuacion_mas_alta():
    if not puntuaciones:
        print("No hay jugadores y puntuaciones registrados.")
    else:
        max_puntuacion = max(puntuaciones.values())
        mejores_jugadores = [jugador for jugador, puntuacion in puntuaciones.items() if puntuacion == max_puntuacion]
        if len(mejores_jugadores) == 1:
            print(f"{mejores_jugadores[0]} tiene la puntuación más alta con {max_puntuacion} puntos.")
        else:
            print("Empate entre los siguientes jugadores con la puntuación más alta:")
            for jugador in mejores_jugadores:
                print(f"{jugador}: {max_puntuacion} puntos")

# Menú de opciones
while True:
    print("\nMenú de Opciones:")
    print("1. Acumular Puntos")
    print("2. Mostrar Puntuaciones")
    print("3. Jugador con Puntuación Más Alta")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        acumular_puntos()
    elif opcion == "2":
        mostrar_puntuaciones()
    elif opcion == "3":
        jugador_con_puntuacion_mas_alta()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
