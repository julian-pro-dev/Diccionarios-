# Crear un diccionario que actúe como un traductor simple
diccionario = {
    "hello": "hola",
    "goodbye": "adiós",
    "apple": "manzana",
    "cat": "gato",
    # Agrega más palabras y traducciones aquí
}

# Función para permitir al usuario ingresar una palabra en el primer idioma
def traducir_palabra():
    palabra = input("Ingrese una palabra en el primer idioma: ")
    if palabra in diccionario:
        traduccion = diccionario[palabra]
        print(f"La traducción de '{palabra}' es '{traduccion}' en el segundo idioma.")
    else:
        print(f"No se encontró una traducción para '{palabra}' en el diccionario.")

# Menú de opciones
while True:
    print("\nMenú de Opciones:")
    print("1. Traducir Palabra")
    print("2. Salir")

    opcion = input("Seleccione una opción (1/2): ")

    if opcion == "1":
        traducir_palabra()
    elif opcion == "2":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
