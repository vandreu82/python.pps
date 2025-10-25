#!/usr/bin/python
#
# Ejercicio 1 
# Adivinar número aleatorio. Usando el módulo ‘random’, método ‘randint’. Se calcula un número 
# aleatorio entre 0 y n y se solicita al usuario que introduzca números hasta que acierte el elegido, 
# dando pistas sobre si el número elegido es mayor o menor que el introducido
#
#   Víctor Manuel Andreu Felipe 2025

import random

max = int(input("Voy a pensar un número entre 0 y: "))

ran = random.randint(0, max)

# inicializamos n a -1 porque no trabajamos con negatividad

n = -1

# iteración hasta que se adivine el número

while n != ran:
    n = int(input("Adivinalo: "))
    if n < ran:
        print("El número es mayor.")
    elif n > ran:
        print("El número es menor.")
    else:
        print("Felicidades, el número es: ", n, ".")
