#!/usr/bin/python
#
# Ejercicio 2
# Crea un programa que solicite al usuario números, la lectura finalizará cuando ingrese la
# palabra “EXIT”. Haz uso de funciones para:
#   a) Comprobar si el número ingresado es primo.
#       a. Si es primo, indicar en qué posición está dentro de los números primos
#       b. Si no es primo mostrar por pantalla la descomposición en números primos
#
# ¿Donde está la b)? XD
#
# Víctor Manuel Andreu Felipe 2025

# función para comprobar si un número es primo 
"""
los números 0 y 1 no son primos
hacemos un bucle desde 2 hasta la raíz cuadrada de el número + 1,
porque el mayor divisor es siempre la raíz cuadrada
Si tiene un divisor, no es primo
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# función para calcular la posición del número dentro de los números primos
"""
bucle que va recorriendo los números primos hasta el número introducido
y sumando en un contador. al final devuelve la posición.
"""
def posicion_primo(n):
    contador = 0
    actual = 2

    while True:
        if es_primo(actual):
            contador += 1
            if actual == n:
                return contador
        actual += 1

# función para descomponer un número en factores primos
"""
crea una lista vacia donde iremos guardando los factores
mientras n sea mayor que 1 y mientras n sea divisible entre divisor,
valor que se va incrementando, añadirá el divisor a la lista
"""
def descomponer(n):
    factores = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1

    return factores

# función para convertir un número en superíndice
def superindice(n):
    mapa = {
        "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
        "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
    }
    resultado = ""
    for c in str(n):
        resultado += mapa[c]
    return resultado

# función para mostrar la descomposición bonita
def descomponer_bonito(n):
    factores = descomponer(n)
    
    # contar cuántas veces aparece cada factor
    conteo = {}
    for f in factores:
        conteo[f] = conteo.get(f, 0) + 1

    partes = []
    for f in sorted(conteo):
        if conteo[f] == 1:
            partes.append(str(f))
        else:
            partes.append(f"{f}{superindice(conteo[f])}")

    return " x ".join(partes)

# programa principal
def menu():
    print("Introduce números enteros. Escribe EXIT para terminar.\n")

    while True:
        entrada = input("Número: ").strip().upper()

        if entrada == "EXIT":
            print("Hasta luego, Mari Carmen")
            break

        # comprobación de errores
        if not entrada.isdigit():
            print("Entrada no válida, introduce un número entero.\n")
            continue

        numero = int(entrada)

        # comprobamos si es primo
        if es_primo(numero):
            pos = posicion_primo(numero)
            print(f"El número {numero} es primo y está en la posición {pos}.\n")
        else:
            # mostrar resultado bonito
            bonito = descomponer_bonito(numero)
            print(f"El número {numero} NO es primo. {numero} = {bonito}\n")

# ejecutar programa
menu()
