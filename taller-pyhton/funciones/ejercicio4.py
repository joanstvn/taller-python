"""Ejercicio 4. Validación de retiro en cajero automático

Un cajero automático debe verificar si un cliente tiene saldo suficiente para realizar un
retiro.

Cree una función llamada validar_retiro() que reciba:

● El saldo actual de la cuenta.
● El valor que desea retirar el cliente.

La función debe:

● Determinar si el retiro puede realizarse.
● Retornar un mensaje indicando si la operación fue aprobada o rechazada por saldo
insuficiente.

El programa debe:

● Solicitar los datos al usuario.
● Llamar a la función.

● Imprimir el resultado de la operación."""

saldo = float(input("Ingrese el saldo actual de la cuenta: "))
retiro = float(input("Ingrese el valor que desea retirar: "))

def validar_retiro(saldo, retiro):
    if retiro <= saldo:
        mensaje = "Operacion aprobada. Puede retirar el dinero."
    else:
        mensaje = "Operacion rechazada. Saldo insuficiente."
    return mensaje

resultado = validar_retiro(saldo, retiro)

print(resultado)
