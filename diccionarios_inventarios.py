# Crear un diccionario para representar el inventario
inventario = {}

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(f"{nombre} ha sido agregado al inventario.")

# Función para actualizar el precio y la cantidad en stock de un producto existente
def actualizar_producto():
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")
    if nombre in inventario:
        precio = float(input("Nuevo precio del producto: "))
        cantidad = int(input("Nueva cantidad en stock: "))
        inventario[nombre]["precio"] = precio
        inventario[nombre]["cantidad"] = cantidad
        print(f"{nombre} ha sido actualizado en el inventario.")
    else:
        print(f"{nombre} no se encuentra en el inventario.")

# Función para buscar un producto por nombre y mostrar su información
def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Información del producto:")
        print(f"Nombre: {nombre}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad en stock: {producto['cantidad']}")
    else:
        print(f"{nombre} no se encuentra en el inventario.")

# Menú de opciones
while True:
    print("\nMenú de Opciones:")
    print("1. Agregar Producto al Inventario")
    print("2. Actualizar Producto en el Inventario")
    print("3. Buscar Producto en el Inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
