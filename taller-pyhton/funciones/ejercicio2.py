"""Ejercicio 2. Cálculo de interés bancario

Un banco ofrece una rentabilidad anual sobre el dinero depositado por sus clientes.
Cree una función llamada calcular_interes() que reciba:

● El saldo de una cuenta.
● El porcentaje de interés.

La función debe:

● Calcular el valor generado por intereses.
● Retornar el resultado.

El programa debe:

● Solicitar los datos necesarios.
● Imprimir el valor de los intereses generados."""

def calcular_interes(saldo, porcentaje):
    interes = saldo * (porcentaje / 100)
    return interes

saldo = float(input("Ingrese el saldo de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de interes: "))

interes_generado = calcular_interes(saldo, porcentaje)

print("El interes generado es:", interes_generado)
