#!/usr/bin/python3
#
# Ejercicio 5
# Juego de piedra, papel, tijera. Se elige una jugada aleatoria entre ‘PIEDRA’, ‘PAPEL’ o ‘TIJERA’.
# Se solicita al usuario ‘PIEDRA’, ‘PAPEL’, ‘TIJERA’ o ‘EXIT’ y se le indica el resultado de la
# partida. Se debe crear un marcador en el que se vea el número de victorias, derrotas y empates tras
# cada partida. Se juegan partidas hasta que se indique con EXIT (cada partida, el programa elegirá
# una jugada aleatoria)
#
#   Víctor Manuel Andreu Felipe 2025

import random

print("Juego de Piedra, Papel o Tijera. Escribe EXIT para salir.\n")

# variables de conteo

victorias = 0
empates = 0
derrotas = 0

# iteración hasta que el usuario quiera salir
while True:
    jugador = input("Elige PIEDRA, PAPEL, TIJERA. EXIT para salir: ").strip().upper()
    
    if jugador == "EXIT":
            print("\nJuego finalizado.\n")
            break

    if jugador != "PIEDRA" and jugador != "PAPEL" and jugador != "TIJERA":
        print("Opción no válida. Intenta de nuevo.\n")
        continue

    # random entre piedra papel o tijera
    numero = random.randint(1, 3)
    if numero == 1:
        ordenador = "PIEDRA"
    elif numero == 2:
        ordenador = "PAPEL"
    else:
        ordenador = "TIJERA"

    print("Tú sacas:", jugador)
    print("Yo saco:", ordenador)

    # comprobar resultado
    if jugador == ordenador:
        print("Empate.\n")
        empates += 1
    elif (jugador == "PIEDRA" and ordenador == "TIJERA") or \
        (jugador == "PAPEL" and ordenador == "PIEDRA") or \
        (jugador == "TIJERA" and ordenador == "PAPEL"):
        print("¡Has ganado!\n")
        victorias += 1
    else:
        print("Has perdido.\n")
        derrotas += 1
        
    # marcador temporal
    print("Victorias:", victorias)
    print("Empates:", empates)
    print("Derrotas:", derrotas)

# resultado final
print("Victorias:", victorias)
print("Empates:", empates)
print("Derrotas:", derrotas, "\n")
if victorias > derrotas:
    print("A Winner is you!!")
elif victorias < derrotas:
    print("DERROTA")
else:
    print("Empate, ¿otra ronda?")
