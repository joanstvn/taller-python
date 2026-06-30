"""Ejercicio 8. Información de una cuenta bancaria

Cree una tupla que almacene la siguiente información:

● Número de cuenta.
● Nombre del titular.
● Tipo de cuenta.
● Saldo disponible.

El programa debe:

● Imprimir la información completa de la tupla.
● Imprimir cada dato por separado utilizando su posición dentro de la tupla."""

cuenta = (1234567890, "Joan Rios", "Ahorros", 1000000000)

print("Informacion completa de la cuenta:", cuenta)

print("Numero de cuenta:", cuenta[0])
print("Nombre del titular:", cuenta[1])
print("Tipo de cuenta:", cuenta[2])
print("Saldo disponible:", cuenta[3])