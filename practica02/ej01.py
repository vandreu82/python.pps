#!/usr/bin/python
#
# Ejercicio 1
# Copia y modifica la calculadora (Ejercicio 2 de los tipos numéricos) para que acepte las
# operaciones de la siguiente forma:
# “ADD 26 16”,
# “MUL ANS 2”
#
#   Víctor Manuel Andreu Felipe 2025

print("Comandoes disponibles: ADD, SUB, MUL, DIV. ANS para utilizar el resultado anterior. QUIT para salir")

ans = 0

# iteración que rompemos con quit o exit

while True:     
    entrada = input("Introduce la operación (por ejemplo: ADD 5 3): ").strip().upper()

    if entrada == "QUIT" or entrada == "EXIT":
        print("Hasta luego, Mari Carmen")
        break

    # dividimos la entrada en partes (comando + dos operandos)
    partes = entrada.split()

    # pequeña comprobación de errores de formato
    if len(partes) != 3:
        print("Formato incorrecto. Ejemplo correcto: ADD 5 3\n")
        continue

    comando = partes[0]
    n1 = partes[1]
    n2 = partes[2]

    # pequeña comprobación de errores
    if comando not in ["ADD", "SUB", "MUL", "DIV"]:
        print("Comando no disponible.")
        continue
    
    # comprobamos si es ANS y si no lo es lo convertimos a float
    
    if n1 == "ANS":
        n1 = ans
    else:
        n1 = float(n1)

    if n2 == "ANS":
        n2 = ans
    else:
        n2 = float(n2)
    
    # operaciones de niño de primaria
    
    if comando == "ADD":
        ans = n1 + n2
    elif comando == "SUB":
        ans = n1 - n2
    elif comando == "MUL":
        ans = n1 * n2
    elif comando == "DIV":
        if n2 == 0:
            print("Error: No se puede dividir entre cero.") # no hagas eso por favor
            continue
        ans = n1 / n2
    
    # si el resultado es un entero lo mostramos sin coma, si es un decimal, redondeamos a 2 decimales
    
    if int(ans) == ans:
        print("Resultado =", int(ans), "\n")
    else:
        print("Resultado =", round(ans, 2), "\n")