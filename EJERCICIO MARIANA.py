
# Crear un diccionario vacío para almacenar los pedidos
pedidos = {}

# Función para registrar un nuevo pedido
def registrar_pedido():
    # Solicitar la información del cliente
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    sexo = input("Ingrese el sexo del cliente: ")
    descripcion = input("Ingrese la descripción de la casa o lugar para guiar al personal de entrega: ")

    # Solicitar la información del producto
    producto = input("Ingrese el nombre del producto: ")
    referencia = input("Ingrese la referencia del producto: ")
    cantidad = int(input("Ingrese la cantidad a solicitar: "))

    # Crear un diccionario con la información del pedido
    pedido = {
        "Nombre del cliente": nombre,
        "Dirección": direccion,
        "Contacto": contacto,
        "Sexo": sexo,
        "Descripción": descripcion,
        "Producto": producto,
        "Referencia": referencia,
        "Cantidad": cantidad
    }

    # Agregar el pedido al diccionario de pedidos
    pedidos[len(pedidos) + 1] = pedido

    print("El pedido ha sido registrado exitosamente.")

# Función para ver todos los pedidos realizados
def ver_pedidos():
    if len(pedidos) == 0:
        print("No se han registrado pedidos.")
    else:
        for numero, pedido in pedidos.items():
            print(f"Pedido #{numero}:")
            for clave, valor in pedido.items():
                print(f"{clave}: {valor}")
            print()

# Menú principal
while True:
    print("1. Registrar un nuevo pedido")
    print("2. Ver todos los pedidos realizados")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        registrar_pedido()
    elif opcion == "2":
        ver_pedidos()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")