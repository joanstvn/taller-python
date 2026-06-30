"""Ejercicio 10. Gestión básica de cuentas bancarias

Cree una lista que almacene los saldos de cinco cuentas bancarias.
El programa debe:

● Imprimir todos los saldos registrados.
● Calcular el saldo total almacenado en las cuentas.
● Determinar cuántas cuentas tienen un saldo superior a $1.000.000.
● Mostrar el saldo más alto registrado.
● Imprimir todos los resultados obtenidos."""

# Lista de saldos
saldos = [1500000, 900000, 2200000, 700000, 1300000]

# Función para calcular el saldo total
def calcular_total(lista):
    total = 0

    for saldo in lista:
        total += saldo

    return total


# Función para contar los saldos mayores a $1.000.000
def contar_saldos_mayores(lista):
    cantidad = 0

    for saldo in lista:
        if saldo > 1000000:
            cantidad += 1

    return cantidad


# Función para obtener el saldo más alto
def obtener_saldo_mayor(lista):
    mayor = lista[0]

    for saldo in lista:
        if saldo > mayor:
            mayor = saldo

    return mayor


# Llamar las funciones
total = calcular_total(saldos)
cantidad_mayores = contar_saldos_mayores(saldos)
saldo_mas_alto = obtener_saldo_mayor(saldos)

# Mostrar resultados
print("Saldos registrados:", saldos)
print("El saldo total de las cuentas es:", total)
print("Cantidad de cuentas con saldo superior a $1.000.000:", cantidad_mayores)
print("El saldo más alto registrado es:", saldo_mas_alto)