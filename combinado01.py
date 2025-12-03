# #!/usr/bin/python
# #
# # Ejercicio 1 
# # Adivinar número aleatorio. Usando el módulo ‘random’, método ‘randint’. Se calcula un número 
# # aleatorio entre 0 y n y se solicita al usuario que introduzca números hasta que acierte el elegido, 
# # dando pistas sobre si el número elegido es mayor o menor que el introducido
# #
# #   Víctor Manuel Andreu Felipe 2025

# import random

# max = int(input("Voy a pensar un número entre 0 y: "))

# ran = random.randint(0, max)

# # inicializamos n a -1 porque no trabajamos con negatividad

# n = -1

# # iteración hasta que se adivine el número

# while n != ran:
#     n = int(input("Adivinalo: "))
#     if n < ran:
#         print("El número es mayor.")
#     elif n > ran:
#         print("El número es menor.")
#     else:
#         print("Felicidades, el número es: ", n, ".")

# #!/usr/bin/python
# #
# # Ejercicio 2
# # Una calculadora que pida comandoes al usuario: ADD, SUB, MUL, DIV, EXIT. Si el usuario no ha
# # introducido el comando QUIT, solicita 2 números a los que aplica la operación (en el caso de DIV,
# # el primer número es el numerador y el segundo el denominador). Mejora opcional, usar ‘ANS’ para
# # referirse a cualquiera de los 2 operandos para reutilizar el resultado de la operación anterior
# #
# #   Víctor Manuel Andreu Felipe 2025

# print("Comandoes disponibles: ADD, SUB, MUL, DIV. ANS para utilizar el resultado anterior. QUIT para salir")

# ans = 0
# comando = ""

# # iteración que rompemos con quit o exit

# while True:     
#     comando = input("Introduce un comando: ").strip().upper()
    
#     if comando == "QUIT" or comando == "EXIT":
#         print("Hasta luego, Mari Carmen")
#         break
    
#     # pequeña comprobación de errores
#     if comando not in ["ADD", "SUB", "MUL", "DIV"]:
#         print("Comando no disponible.")
#         continue
    
#     n1 = input("Introduce el primer número (o 'ANS'): ").strip().upper()
#     n2 = input("Introduce el segundo número (o 'ANS'): ").strip().upper()
    
#     # comprobamos si es ANS y si no lo es lo convertimos a float
    
#     if n1 == "ANS":
#         n1 = ans
#     else:
#         n1 = float(n1)

#     if n2 == "ANS":
#         n2 = ans
#     else:
#         n2 = float(n2)
    
#     # operaciones de niño de primaria
    
#     if comando == "ADD":
#         ans = n1 + n2
#     elif comando == "SUB":
#         ans = n1 - n2
#     elif comando == "MUL":
#         ans = n1 * n2
#     elif comando == "DIV":
#         if n2 == 0:
#             print("Error: No se puede dividir entre cero.") # no hagas eso por favor
#             continue
#         ans = n1 / n2
    
#     # si el resultado es un entero lo mostramos sin coma, si es un decimal, redondeamos a 2 decimales
    
#     if int(ans) == ans:
#         print("Resultado =", int(ans), "\n")
#     else:
#         print("Resultado =", round(ans, 2), "\n")
        
# #!/usr/bin/python
# #
# # Ejercicio 3
# # Calculadora de edad. Usando el módulo ‘datetime’. El usuario introduce su fecha de nacimiento y el
# # método calcula su edad. A tener en cuenta:
# #   • Año actual – Año de nacimiento = edad
# #   • Si Mes actual < Mes nacimiento: edad – 1
# #   • Sino, si Mes actual = mes nacimiento
# #       ◦ Si Día actual < Día nacimiento: edad – 1
# #
# #   Víctor Manuel Andreu Felipe 2025

# from datetime import date

# fecha = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")

# dia_str, mes_str, anio_str = fecha.split("/")

# dia = int(dia_str)
# mes = int(mes_str)
# anio = int(anio_str)

# edad = date.today().year - anio

# if date.today().month < mes:
#     edad -= 1
# elif date.today().month == mes and date.today().day < dia:
#     edad -= 1
    
# print("Tienes", edad, "años.")


# #!/usr/bin/python
# #
# # Ejercicio 4
# # Conversor de divisas: USD, EUR, GBP, CAD, y JPY. Se le pasa “divisa de origen”, “divisa destino”
# # y “cantidad”. Proceso a seguir: ?????
# #
# #   Víctor Manuel Andreu Felipe 2025

# print("Conversor de divisas disponibles: USD, EUR, GBP, CAD, JPY")
# print("Escribe 'SALIR' para terminar.\n")

# # tasa de cambio con el euro
# usd = 1.16
# gbp = 0.87
# cad = 1.63
# jpy = 177.66
# eur = 1.0

# # iteración con salida

# while True:
#     origen = input("Divisa de origen: ").strip().upper()
#     if origen == "SALIR":
#         print("Hasta luego, buen día.")
#         break

#     destino = input("Divisa de destino: ").strip().upper()
    
#     cantidad = float(input("Cantidad a convertir: "))

#     # convertimos a euro
#     if origen == "EUR":
#         cantidad_eur = cantidad
#     elif origen == "USD":
#         cantidad_eur = cantidad / usd
#     elif origen == "GBP":
#         cantidad_eur = cantidad / gbp
#     elif origen == "CAD":
#         cantidad_eur = cantidad / cad
#     elif origen == "JPY":
#         cantidad_eur = cantidad / jpy
#     else:
#         print("Divisa de origen no válida.\n")
#         continue

#     # convertimos a divisa final
#     if destino == "EUR":
#         cantidad_final = cantidad_eur * eur
#     elif destino == "USD":
#         cantidad_final = cantidad_eur * usd
#     elif destino == "GBP":
#         cantidad_final = cantidad_eur * gbp
#     elif destino == "CAD":
#         cantidad_final = cantidad_eur * cad
#     elif destino == "JPY":
#         cantidad_final = cantidad_eur * jpy
#     else:
#         print("Divisa de destino no válida.\n")
#         continue

#     # resultado maquillado
#     if int(cantidad) == cantidad:
#         cantidad_mostrar = int(cantidad)
#     else:
#         cantidad_mostrar = round(cantidad, 2)

#     if int(cantidad_final) == cantidad_final:
#         cantidad_final_mostrar = int(cantidad_final)
#     else:
#         cantidad_final_mostrar = round(cantidad_final, 2)

#     print(cantidad_mostrar, origen, "=", cantidad_final_mostrar, destino, "\n")

# #!/usr/bin/python
# #
# # Ejercicio 5
# # Juego de piedra, papel, tijera. Se elige una jugada aleatoria entre ‘PIEDRA’, ‘PAPEL’ o ‘TIJERA’.
# # Se solicita al usuario ‘PIEDRA’, ‘PAPEL’, ‘TIJERA’ o ‘EXIT’ y se le indica el resultado de la
# # partida. Se debe crear un marcador en el que se vea el número de victorias, derrotas y empates tras
# # cada partida. Se juegan partidas hasta que se indique con EXIT (cada partida, el programa elegirá
# # una jugada aleatoria)
# #
# #   Víctor Manuel Andreu Felipe 2025

# import random

# print("Juego de Piedra, Papel o Tijera. Escribe EXIT para salir.\n")

# # variables de conteo

# victorias = 0
# empates = 0
# derrotas = 0

# # iteración hasta que el usuario quiera salir
# while True:
#     jugador = input("Elige PIEDRA, PAPEL, TIJERA. EXIT para salir: ").strip().upper()
    
#     if jugador == "EXIT":
#             print("\nJuego finalizado.\n")
#             break

#     if jugador != "PIEDRA" and jugador != "PAPEL" and jugador != "TIJERA":
#         print("Opción no válida. Intenta de nuevo.\n")
#         continue

#     # random entre piedra papel o tijera
#     numero = random.randint(1, 3)
#     if numero == 1:
#         ordenador = "PIEDRA"
#     elif numero == 2:
#         ordenador = "PAPEL"
#     else:
#         ordenador = "TIJERA"

#     print("Tú sacas:", jugador)
#     print("Yo saco:", ordenador)

#     # comprobar resultado
#     if jugador == ordenador:
#         print("Empate.\n")
#         empates += 1
#     elif (jugador == "PIEDRA" and ordenador == "TIJERA") or \
#         (jugador == "PAPEL" and ordenador == "PIEDRA") or \
#         (jugador == "TIJERA" and ordenador == "PAPEL"):
#         print("¡Has ganado!\n")
#         victorias += 1
#     else:
#         print("Has perdido.\n")
#         derrotas += 1
        
#     # marcador temporal
#     print("Victorias:", victorias)
#     print("Empates:", empates)
#     print("Derrotas:", derrotas)

# # resultado final
# print("Victorias:", victorias)
# print("Empates:", empates)
# print("Derrotas:", derrotas, "\n")
# if victorias > derrotas:
#     print("A Winner is you!!")
# elif victorias < derrotas:
#     print("DERROTA")
# else:
#     print("Empate, ¿otra ronda?")

# #!/usr/bin/python
# #
# # Ejercicio 1
# # Copia y modifica la calculadora (Ejercicio 2 de los tipos numéricos) para que acepte las
# # operaciones de la siguiente forma:
# # “ADD 26 16”,
# # “MUL ANS 2”
# #
# #   Víctor Manuel Andreu Felipe 2025

# print("Comandoes disponibles: ADD, SUB, MUL, DIV. ANS para utilizar el resultado anterior. QUIT para salir")

# ans = 0

# # iteración que rompemos con quit o exit

# while True:     
#     entrada = input("Introduce la operación (por ejemplo: ADD 5 3): ").strip().upper()

#     if entrada == "QUIT" or entrada == "EXIT":
#         print("Hasta luego, Mari Carmen")
#         break

#     # dividimos la entrada en partes (comando + dos operandos)
#     partes = entrada.split()

#     # pequeña comprobación de errores de formato
#     if len(partes) != 3:
#         print("Formato incorrecto. Ejemplo correcto: ADD 5 3\n")
#         continue

#     comando = partes[0]
#     n1 = partes[1]
#     n2 = partes[2]

#     # pequeña comprobación de errores
#     if comando not in ["ADD", "SUB", "MUL", "DIV"]:
#         print("Comando no disponible.")
#         continue
    
#     # comprobamos si es ANS y si no lo es lo convertimos a float
    
#     if n1 == "ANS":
#         n1 = ans
#     else:
#         n1 = float(n1)

#     if n2 == "ANS":
#         n2 = ans
#     else:
#         n2 = float(n2)
    
#     # operaciones de niño de primaria
    
#     if comando == "ADD":
#         ans = n1 + n2
#     elif comando == "SUB":
#         ans = n1 - n2
#     elif comando == "MUL":
#         ans = n1 * n2
#     elif comando == "DIV":
#         if n2 == 0:
#             print("Error: No se puede dividir entre cero.") # no hagas eso por favor
#             continue
#         ans = n1 / n2
    
#     # si el resultado es un entero lo mostramos sin coma, si es un decimal, redondeamos a 2 decimales
    
#     if int(ans) == ans:
#         print("Resultado =", int(ans), "\n")
#     else:
#         print("Resultado =", round(ans, 2), "\n")
        
        
# #!/usr/bin/python
# #
# # Ejercicio 2
# # Crea un contador de palabras. Pasado un texto debe contar el número de palabras que contiene.
# # A continuación, se deber añadir una palabra palabra_busca para ver el número de ocurrencias de dicha
# # palabra en el texto.

# #   Víctor Manuel Andreu Felipe 2025

# texto = input("Introduce un texto: ")

# # convertimos todo a minúsculas
# texto = texto.lower()

# # eliminamos signos de puntuación.
# limpio = ""
# for caracter in texto:
#     if caracter not in ".,;:!?¡¿()[]{}\"'":
#         limpio += caracter
#     else:
#         limpio += " "

# # spliteamos el texto en palabras para contarlas
# palabras = limpio.split()

# print("\nEl texto tiene ", len(palabras), " palabras.")

# # creamos el diccionario contador en el que almacenaremos palabra: número de veces que aparece
# contador = {}

# for palabra in palabras:
#     if palabra in contador:
#         contador[palabra] += 1
#     else:
#         contador[palabra] = 1

# # pedimos la palabra a consultar(en minúsculas)
# palabra_busca = input("\nIntroduce una palabra para contar(en minúsculas, por favor): ").lower()

# if palabra_busca in contador:
#     print("La palabra", "'", palabra_busca, "'", "sale", contador[palabra_busca], "veces.")
# else:
#     print("La palabra", "'", palabra_busca, "'", "no está.")
    
# #!/usr/bin/python
# #
# # Ejercicio 3
# # Crea un programa que calcule el factorial de un número dado y el número de 0s que quedan a la
# # derecha del número. Por ejemplo:
# # factorial(5) = 120, con 1 único cero a la derecha

# #   Víctor Manuel Andreu Felipe 2025

# n = int(input("Introduce un número para calcular su factorial: "))

# # calculamos el factorial desde 1 hasta n
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i

# print("El factorial de", n, "es:", factorial)

# # contamos los ceros de la derecha
# ceros = 0
# num = factorial

# # mientras el resto de num entre 10 sea 0 contar un 0 y seguir dividiendo entre 10

# while num % 10 == 0:
#     ceros += 1
#     num = num // 10

# # sacamos por pantalla el resultado de la forma del ejemplo
# if ceros == 0:
#     print("factorial(" + str(n) + ") =", factorial, ", sin ceros a la derecha")
# elif ceros == 1:
#     print("factorial(" + str(n) + ") =", factorial, ", con 1 único cero a la derecha")
# else:
#     print("factorial(" + str(n) + ") =", factorial, ", con", ceros, "ceros a la derecha")
    
    
# #!/usr/bin/python
# #
# # Ejercicio 4
# # Crea un programa que compruebe si una frase es palíndromo. Intenta normalizar lo máximo que
# # puedas el texto, eliminando todo carácter no alfanumérico. Por ejemplo:
# # • “Ateo por Arabia, iba raro poeta” debería quedar así: “ateoporarabiaibararopoeta”
# # Conseguir esto usando librerías estándar de Python (solamente necesitas una función de str) es
# # relativamente fácil, pero eliminar los acentos te costará más. Para ello, recomiendo que investigues
# # cómo hacerlo con la librería “unidecode”
# # • “Adán y raza; azar y nada” debería quedar así: “adanyrazaazarynada”.

# from unidecode import unidecode

# frase = input("Introduce una frase: ")

# # pasamos el texto a minúsculas
# frase = frase.lower()

# # eliminamos acentos con unidecode
# frase = unidecode(frase)

# # eliminamos no alfanuméricos
# normalizada = ""
# for ch in frase:
#     if ch.isalnum():
#         normalizada += ch

# # comprobamos que sea un palíndromo
# if normalizada == normalizada[::-1]:
#     print("Resultado: ES un palíndromo.")
# else:
#     print("Resultado: NO es un palíndromo.")