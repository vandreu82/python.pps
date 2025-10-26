#!/usr/bin/python
#
# Ejercicio 3
# Crea un programa que calcule el factorial de un número dado y el número de 0s que quedan a la
# derecha del número. Por ejemplo:
# factorial(5) = 120, con 1 único cero a la derecha

#   Víctor Manuel Andreu Felipe 2025

n = int(input("Introduce un número para calcular su factorial: "))

# calculamos el factorial desde 1 hasta n
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("El factorial de", n, "es:", factorial)

# contamos los ceros de la derecha
ceros = 0
num = factorial

# mientras el resto de num entre 10 sea 0 contar un 0 y seguir dividiendo entre 10

while num % 10 == 0:
    ceros += 1
    num = num // 10

# sacamos por pantalla el resultado de la forma del ejemplo
if ceros == 0:
    print("factorial(" + str(n) + ") =", factorial, ", sin ceros a la derecha")
elif ceros == 1:
    print("factorial(" + str(n) + ") =", factorial, ", con 1 único cero a la derecha")
else:
    print("factorial(" + str(n) + ") =", factorial, ", con", ceros, "ceros a la derecha")