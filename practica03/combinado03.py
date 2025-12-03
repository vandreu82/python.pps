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

#!/usr/bin/python
#
# Ejercicio 2
# Copia y modifica el conversor de divisas para que haga uso de diccionarios (Ejercicio 4 de
# los tipos numéricos)
#
#   Víctor Manuel Andreu Felipe 2025

print("Conversor de divisas disponibles: USD, EUR, GBP, CAD, JPY")
print("Escribe 'SALIR', 'EXIT' o 'Q' para terminar.\n")

# diccionario de divisas

divisas = {
    "EUR": 1.0,
    "USD": 1.16,
    "GBP": 0.88,
    "CAD": 1.63,
    "JPY": 177.88
}

# iteración con salida

while True:
    origen = input("Divisa de origen: ").strip().upper()
    if origen == "SALIR" or origen == "EXIT" or origen == "Q":
        print("Hasta luego, buen día.")
        break

    # comprobación de errores
    if origen not in divisas:
        print("Divisa de origen no válida.\n")
        continue

    destino = input("Divisa de destino: ").strip().upper()

    if destino not in divisas:
        print("Divisa de destino no válida.\n")
        continue
    cantidad = float(input("Cantidad a convertir: "))

    # convertimos a euro usando el diccionario
    cantidad_eur = cantidad / divisas[origen]

    # convertimos de euro a la divisa final
    cantidad_final = cantidad_eur * divisas[destino]


    # resultado maquillado
    if int(cantidad) == cantidad:
        cantidad_mostrar = int(cantidad)
    else:
        cantidad_mostrar = round(cantidad, 2)

    if int(cantidad_final) == cantidad_final:
        cantidad_final_mostrar = int(cantidad_final)
    else:
        cantidad_final_mostrar = round(cantidad_final, 2)

    print(cantidad_mostrar, origen, "=", cantidad_final_mostrar, destino, "\n")

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

#!/usr/bin/python
#
# Ejercicio 4 
# Registro de alumnos. Crea un registro que permita almacenar distinta información de 
# alumnos, tal como: 
#     • NRE (Número Regional de Estudiante) 
#     • Nombre 
#     • Apellidos 
#     • Número de teléfono 
#     • Lista de asistencia (fecha, asiste o no) 
# Crea un par de alumnos “a mano” e imprime el diccionario 
# Opcional: Modifica el programa para que el usuario pueda introducir nuevos alumnos y 
# registrar asistencias a través del teclado (input()) 
#
#   Víctor Manuel Andreu Felipe 2025

print("*" * 34)
print("*      REGISTRO DE ALUMNOS       *")
print("*" * 34)

# diccionario principal que almacenará los alumnos. la clave será NRE
registro = {}

# dos alumnos a mano

registro["654987"] = {
    "nombre": "Pablo",
    "apellidos": "Motos Burgos",
    "telefono": "666777888",
    "asistencia": [
        ["15/11/25", True],
        ["03/12/25", False]
    ]
}

registro["321456"] = {
    "nombre": "David",
    "apellidos": "Broncano Aguilera",
    "telefono": "654321987",
    "asistencia": [
        ["01/01/25", True]
    ]
}

# menú asteriscado y bonito

while True:
    print("\n" + "*" * 34)
    print("* Menú principal                 *")
    print("*" * 34)
    print("* [1] Añadir alumno nuevo        *")
    print("* [2] Registrar asistencia       *")
    print("* [3] Mostrar registro completo  *")
    print("* [4] Salir                      *")
    print("*" * 34)

    opcion = input("Elige una opción (1-4): ").strip()

    # opcion 1: añadir nuevo alumno
    if opcion == "1":

        print("\n== Añadir alumno ==")

        nre = input("NRE del alumno: ").strip()

        # comprobamos que no exista ya
        if nre in registro:
            print("Ese NRE ya existe.\n")
            continue

        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        telefono = input("Teléfono: ").strip()

        # guardamos el alumno
        registro[nre] = {
            "nombre": nombre,
            "apellidos": apellidos,
            "telefono": telefono,
            "asistencia": []
        }

        print("Alumno añadido correctamente.\n")

    # opcion 2: registrar asistencia
    elif opcion == "2":

        print("\n== Registrar asistencia ==")

        nre = input("Introduce el NRE del alumno: ").strip()

        if nre not in registro:
            print("No existe un alumno con ese NRE.\n")
            continue

        # pedimos la fecha sin validación
        fecha = input("Fecha (DD/MM/YY): ").strip()

        estado_txt = input("¿Asiste? (S/N): ").strip().upper()

        if estado_txt == "S":
            estado = True
        else:
            estado = False

        # añadimos la asistencia a la lista
        registro[nre]["asistencia"].append([fecha, estado])

        print("Asistencia registrada.\n")

    # opcion 3: mostrar registro completo
    elif opcion == "3":

        print("\n== Registro completo ==\n")

        if len(registro) == 0:
            print("No hay alumnos registrados.\n")
        else:
            for nre in registro:
                print("*" * 34)
                print("NRE: ", nre)
                print("  Nombre:   ", registro[nre]["nombre"])
                print("  Apellidos:", registro[nre]["apellidos"])
                print("  Teléfono: ", registro[nre]["telefono"])
                print("  Asistencias: ")

                asistencias = registro[nre]["asistencia"]

                if len(asistencias) == 0:
                    print("    (Sin asistencias registradas)")
                else:
                    for entrada in asistencias:
                        fecha = entrada[0]
                        asistio = entrada[1]

                        if asistio:
                            estado = "Asiste"
                        else:
                            estado = "No asiste"

                        print("    -", fecha, "->", estado)

                print()  # línea en blanco entre alumnos

    # opcion 4: salir
    elif opcion == "4":
        print("\nGracias por usar el registro. Hasta luego.")
        break
    # comprobación
    else:
        print("Opción no válida. Elige 1, 2, 3 o 4.\n")

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