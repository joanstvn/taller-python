"""Ejercicio 9. Movimientos de una cuenta bancaria

Cree una tupla con siete valores numéricos que representen los movimientos realizados en
una cuenta durante una semana.

El programa debe:

● Imprimir todos los movimientos almacenados en la tupla.
● Mostrar el movimiento de mayor valor.
● Mostrar el movimiento de menor valor.
● Calcular e imprimir la suma total de los movimientos."""

# Tupla con los movimientos de la semana
movimientos = (150000, -50000, 200000, -30000, 100000, -20000, 80000)

# Función para obtener el movimiento mayor
def obtener_mayor(tupla):
    mayor = tupla[0]

    for movimiento in tupla:
        if movimiento > mayor:
            mayor = movimiento

    return mayor


# Función para obtener el movimiento menor
def obtener_menor(tupla):
    menor = tupla[0]

    for movimiento in tupla:
        if movimiento < menor:
            menor = movimiento

    return menor


# Función para calcular la suma de los movimientos
def calcular_suma(tupla):
    suma = 0

    for movimiento in tupla:
        suma += movimiento

    return suma


# Llamar las funciones
mayor = obtener_mayor(movimientos)
menor = obtener_menor(movimientos)
suma = calcular_suma(movimientos)

# Mostrar resultados
print("Movimientos de la semana:", movimientos)
print("El movimiento más alto fue:", mayor)
print("El movimiento más bajo fue:", menor)
print("La suma total de los movimientos es:", suma)