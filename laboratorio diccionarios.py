import string

# Paso a: Leer el texto y convertirlo a minúsculas
texto = input("Por favor, ingrese un texto largo: ")
texto = texto.lower()

# Paso b: Eliminar signos de puntuación
for signo in string.punctuation:
    texto = texto.replace(signo, " ")

# Paso c: Contar la frecuencia de cada palabra
palabras = texto.split()
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Paso d: Encontrar las 10 palabras más comunes sin key o lambda
palabras_ordenadas = list(frecuencia_palabras.items())
palabras_ordenadas.sort()

# Función para obtener la frecuencia de una palabra en el ordenamiento
def obtener_frecuencia(palabra_frecuencia):
    return palabra_frecuencia[1]

palabras_ordenadas.sort(key=obtener_frecuencia, reverse=True)

print("Las 10 palabras más comunes en el texto y su frecuencia son:")
for palabra, frecuencia in palabras_ordenadas[:10]:
    print(f"{palabra}: {frecuencia}")
