#!/usr/bin/python
#
# Ejercicio 2
# Una calculadora que pida comandoes al usuario: ADD, SUB, MUL, DIV, EXIT. Si el usuario no ha
# introducido el comando QUIT, solicita 2 números a los que aplica la operación (en el caso de DIV,
# el primer número es el numerador y el segundo el denominador). Mejora opcional, usar ‘ANS’ para
# referirse a cualquiera de los 2 operandos para reutilizar el resultado de la operación anterior
#
#   Víctor Manuel Andreu Felipe 2025

print("Comandoes disponibles: ADD, SUB, MUL, DIV. ANS para utilizar el resultado anterior. QUIT para salir")

ans = 0
comando = ""

# iteración que rompemos con quit o exit

while True:     
    comando = input("Introduce un comando: ").strip().upper()
    
    if comando == "QUIT" or comando == "EXIT":
        print("Hasta luego, Mari Carmen")
        break
    
    # pequeña comprobación de errores
    if comando not in ["ADD", "SUB", "MUL", "DIV"]:
        print("Comando no disponible.")
        continue
    
    n1 = input("Introduce el primer número (o 'ANS'): ").strip().upper()
    n2 = input("Introduce el segundo número (o 'ANS'): ").strip().upper()
    
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