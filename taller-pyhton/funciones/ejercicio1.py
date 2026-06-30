"""Ejercicio 1. Determinar el saldo mayor entre tres cuentas

Una entidad bancaria desea identificar cuál de tres cuentas posee el saldo más alto.
Cree una función llamada saldo_mayor() que reciba los saldos de tres cuentas bancarias.
La función debe:

● Determinar cuál saldo es el mayor.
● Retornar el valor encontrado.

El programa debe:

● Solicitar los tres saldos.
● Llamar a la función.
● Imprimir el saldo mayor."""

saldo1 = float(input("Ingrese el saldo de la cuenta 1: "))
saldo2 = float(input("Ingrese el saldo de la cuenta 2: "))
saldo3 = float(input("Ingrese el saldo de la cuenta 3: "))

def saldo_mayor(saldo1, saldo2, saldo3):
    mayor = saldo1
    if saldo2 > mayor:
        mayor = saldo2
    if saldo3 > mayor:
        mayor = saldo3
    return mayor

resultado = saldo_mayor(saldo1, saldo2, saldo3)

print("El saldo mayor es:", resultado)  
