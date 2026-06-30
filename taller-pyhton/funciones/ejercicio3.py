"""Ejercicio 3. Promedio y estado académico

Cree una función llamada evaluar_estudiante() que reciba tres notas.
La función debe:

● Calcular el promedio.
● Determinar si el estudiante aprueba o no aprueba.
● Retornar el promedio y el resultado obtenido.

El programa debe imprimir ambos resultados."""

def evaluar_estudiante(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    if promedio >= 3:
        estado = "Aprueba"
    else:
        estado = "No aprueba"
    return promedio, estado

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio, estado = evaluar_estudiante(nota1, nota2, nota3)

print("El promedio es:", promedio)
print("El estudiante:", estado)
