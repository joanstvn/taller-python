"""Ejercicio 7. Búsqueda de clientes

Cree una lista con diez nombres de clientes.
El programa debe:

● Solicitar al usuario el nombre de un cliente.
● Verificar si el nombre se encuentra registrado en la lista.
● Imprimir un mensaje indicando si el cliente fue encontrado o no."""

clientes = ["Ana", "Carlos", "Luisa", "Pedro", "Marta",
            "Jorge", "Sofia", "Daniel", "Camila", "Andres"]

# Función para buscar un cliente en la lista
def buscar_cliente(lista, nombre):

    encontrado = False

    for cliente in lista:
        if cliente == nombre:
            encontrado = True

    return encontrado


# Solicitar el nombre al usuario
nombre_buscado = input("Ingrese el nombre del cliente que desea buscar: ")

# Llamar la función
encontrado = buscar_cliente(clientes, nombre_buscado)

# Mostrar el resultado
if encontrado:
    print("El cliente", nombre_buscado, "fue encontrado en la lista.")
else:
    print("El cliente", nombre_buscado, "no está registrado.")