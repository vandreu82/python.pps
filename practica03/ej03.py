#!/usr/bin/python
#
# Ejercicio 3 
# Copia y modifica el contador de palabras (Ejercicio 2 de los tipos de texto) para que 
# devuelva el número de apariciones de cada palabra (cuando no se le indica una palabra clave 
# por parámetro)
#
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

palabra_busca = input("\nIntroduce una palabra para contar (ENTER para mostrar todas): ").lower()

# si se pulsa ENTER sin escribir nada devolvemos el número de veces que aparece la palabra
if palabra_busca == "":
    print("\nNúmero de apariciones de cada palabra:\n")
    for clave in contador:
        print("La palabra", clave, "sale", contador[clave], "veces")
else:
    # búsqueda normal de una sola palabra
    if palabra_busca in contador:
        print("\nLa palabra", "'", palabra_busca, "'", "sale", contador[palabra_busca], "veces.")
    else:
        print("\nLa palabra", "'", palabra_busca, "'", "no está.")
