#!/usr/bin/python
#
# Ejercicio 4
# Crea un programa que compruebe si una frase es palíndromo. Intenta normalizar lo máximo que
# puedas el texto, eliminando todo carácter no alfanumérico. Por ejemplo:
# • “Ateo por Arabia, iba raro poeta” debería quedar así: “ateoporarabiaibararopoeta”
# Conseguir esto usando librerías estándar de Python (solamente necesitas una función de str) es
# relativamente fácil, pero eliminar los acentos te costará más. Para ello, recomiendo que investigues
# cómo hacerlo con la librería “unidecode”
# • “Adán y raza; azar y nada” debería quedar así: “adanyrazaazarynada”.

from unidecode import unidecode

frase = input("Introduce una frase: ")

# pasamos el texto a minúsculas
frase = frase.lower()

# eliminamos acentos con unidecode
frase = unidecode(frase)

# eliminamos no alfanuméricos
normalizada = ""
for ch in frase:
    if ch.isalnum():
        normalizada += ch

# comprobamos que sea un palíndromo
if normalizada == normalizada[::-1]:
    print("Resultado: ES un palíndromo.")
else:
    print("Resultado: NO es un palíndromo.")