#!/usr/bin/python
#
# Ejercicio 5
# Calculadora de anagramas. Para un texto determinado, detecta todos los anagramas
# (palabras que tienen las mismas letras, pero en distinto orden). Por ejemplo: “acontecido” es
# anagrama de “anecdótico”, y “anecdótico” es anagrama de “acontecido”. Para eliminar los
# acentos se puede utilizar la librería no estándar “unidecode”
#
#   Víctor Manuel Andreu Felipe 2025

from unidecode import unidecode  # librería no estándar para quitar acentos

texto = input("Introduce un texto: ")

# convertimos todo a minúsculas
texto = texto.lower()

# eliminamos acentos con unidecode (á -> a, é -> e, ñ -> n, etc.)
texto = unidecode(texto)

# eliminamos signos de puntuación
limpio = ""
for caracter in texto:
    if caracter not in ".,;:!?¡¿()[]{}\"'":
        limpio += caracter
    else:
        limpio += " "

# spliteamos el texto en palabras
palabras = limpio.split()

# creamos el diccionario de anagramas
# clave: letras ordenadas de la palabra
# valor: lista de palabras que comparten esas letras
anagramas = {}

for palabra in palabras:
    # la firma de la palabra será sus letras ordenadas alfabéticamente
    firma = "".join(sorted(palabra))

    if firma in anagramas:
        # si ya tenemos esa firma, añadimos la palabra
        anagramas[firma].append(palabra)
    else:
        # si no existe, la creamos con una lista que contiene la palabra
        anagramas[firma] = [palabra]

# mostramos los anagramas encontrados
print("\nAnagramas encontrados:\n")

hay_anagramas = False

# eliminación de duplicados
for firma in anagramas:
    grupo = anagramas[firma]

    # quitamos duplicados dentro del grupo
    grupo_unico = []
    for palabra in grupo:
        if palabra not in grupo_unico:
            grupo_unico.append(palabra)

    # solo nos interesan los grupos con más de una palabra distinta
    if len(grupo_unico) > 1:
        hay_anagramas = True
        print(", ".join(grupo_unico))

if not hay_anagramas:
    print("No se han encontrado anagramas en el texto.")