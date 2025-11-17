#!/usr/bin/python
#
# Ejercicio 1
# Copia y modifica la calculadora (Ejercicio 1 de los tipos de texto) para que admita
# operaciones con un número variable de operandos (Ej. ADD 2 3 5 8). Añade una operación
# unaria, como SQRT (raíz cuadrada). Además, utiliza diccionarios para almacenar las
# operaciones.
#
#   Víctor Manuel Andreu Felipe 2025

import math # para raiz cuadrada

print("Comandos disponibles: ADD, SUB, MUL, DIV, SQRT.")
print("Usa ANS para el último resultado. QUIT para salir.\n")

ans = 0.0 # inicializamos ans

# diccionario de operaciones
operaciones = {
    "ADD": "ADD",
    "SUB": "SUB",
    "MUL": "MUL",
    "DIV": "DIV",
    "SQRT": "SQRT"
}

# iteración que rompemos con quit, exit o q

while True:
    entrada = input("Introduce la operación: ").strip().upper()

    if entrada == "QUIT" or entrada == "EXIT" or entrada == "Q":
        print("Hasta luego, Mari Carmen")
        break
    
    # pequeña comprobación de errores
    partes = entrada.split()

    if len(partes) < 2:
        print("Formato incorrecto.\n")
        continue

    comando = partes[0]

    if comando not in operaciones:
        print("Comando no disponible.\n")
        continue

    # comprobamos si es ANS y si no lo es lo convertimos a float
    operandos_txt = partes[1:]
    numeros = []

    for token in operandos_txt:
        if token == "ANS":
            valor = ans
        else:
            valor = float(token)
        numeros.append(valor)

    # comprobación de errores de sqrt
    if comando == "SQRT":
        if len(numeros) != 1:
            print("SQRT solo utiliza un número.\n")
            continue
        x = numeros[0]

        if x < 0:
            print("No puedes hacer la raíz de un número negativo.\n")
            continue
        ans = math.sqrt(x)

    else:
        # comprobación de errores del resto y operaciones de niño de primaria
        if len(numeros) < 2:
            print("La operación necesita al menos dos números.\n")
            continue
        if comando == "ADD":
            total = 0.0
            for n in numeros:
                total = total + n
            ans = total
        elif comando == "SUB":
            r = numeros[0]
            i = 1
            while i < len(numeros):
                r = r - numeros[i]
                i = i + 1
            ans = r
        elif comando == "MUL":
            r = 1.0
            for n in numeros:
                r = r * n
            ans = r
        elif comando == "DIV":
            r = numeros[0]
            i = 1
            while i < len(numeros):
                if numeros[i] == 0:
                    print("Error: No se puede dividir entre cero.\n") # no hagas eso por favor
                    r = None
                    break
                r = r / numeros[i]
                i = i + 1
            if r is None:
                continue
            ans = r

    # si el resultado es un entero lo mostramos sin coma, si es un decimal, redondeamos a 2 decimales
    if int(ans) == ans:
        print("Resultado =", int(ans), "\n")
    else:
        print("Resultado =", round(ans, 2), "\n")
