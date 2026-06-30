"""Ejercicio 5. Tabla de amortización simple

Cree una función llamada cuotas_prestamo() que reciba:

● El valor total de un préstamo.
● El número de cuotas.

La función debe:

● Calcular el valor de cada cuota utilizando una división simple.
● Retornar el valor de la cuota.

El programa debe:

● Solicitar los datos.
● Imprimir el valor de cada cuota."""

def cuotas_prestamo(valor_prestamo, numero_cuotas):
    valor_cuota = valor_prestamo / numero_cuotas
    return valor_cuota

valor_prestamo = float(input("Ingrese el valor total del prestamo: "))
numero_cuotas = int(input("Ingrese el numero de cuotas: "))

valor_cuota = cuotas_prestamo(valor_prestamo, numero_cuotas)

print("El valor de cada cuota es:", valor_cuota)
