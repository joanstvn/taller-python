"""Ejercicio 6. Análisis de saldos bancarios

Cree una lista con los saldos de cinco clientes.
El programa debe:

● Imprimir todos los saldos almacenados en la lista.
● Mostrar el saldo más alto.
● Mostrar el saldo más bajo.
● Calcular e imprimir el promedio de los saldos registrados."""

# Lista de saldos
saldos = [1200000, 800000, 2500000, 950000, 1750000]

# Función para obtener el saldo mayor
def obtener_mayor(lista):
    mayor = lista[0]

    for saldo in lista:
        if saldo > mayor:
            mayor = saldo

    return mayor


# Función para obtener el saldo menor
def obtener_menor(lista):
    menor = lista[0]

    for saldo in lista:
        if saldo < menor:
            menor = saldo

    return menor


# Función para calcular el promedio
def calcular_promedio(lista):
    suma = 0

    for saldo in lista:
        suma += saldo

    promedio = suma / len(lista)

    return promedio


# Llamar las funciones
mayor = obtener_mayor(saldos)
menor = obtener_menor(saldos)
promedio = calcular_promedio(saldos)

# Mostrar resultados
print("Saldos de los clientes:", saldos)
print("El saldo más alto es:", mayor)
print("El saldo más bajo es:", menor)
print("El promedio de los saldos es:", promedio)