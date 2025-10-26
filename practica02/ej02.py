#!/usr/bin/python
#
# Ejercicio 2
# Crea un contador de palabras. Pasado un texto debe contar el número de palabras que contiene.
# A continuación, se deber añadir una palabra palabra_busca para ver el número de ocurrencias de dicha
# palabra en el texto.

#   Víctor Manuel Andreu Felipe 2025

texto = input("Introduce un texto: ")

# convertimos todo a minúsculas
texto = texto.lower()

# eliminamos signos de puntuación.
limpio = ""
for caracter in texto:
    if caracter not in ".,;:!?¡¿()[]{}\"'":
        limpio += caracter
    else:
        limpio += " "

# spliteamos el texto en palabras para contarlas
palabras = limpio.split()

print("\nEl texto tiene ", len(palabras), " palabras.")

# creamos el diccionario contador en el que almacenaremos palabra: número de veces que aparece
contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

# pedimos la palabra a consultar(en minúsculas)
palabra_busca = input("\nIntroduce una palabra para contar(en minúsculas, por favor): ").lower()

if palabra_busca in contador:
    print("La palabra", "'", palabra_busca, "'", "sale", contador[palabra_busca], "veces.")
else:
    print("La palabra", "'", palabra_busca, "'", "no está.")