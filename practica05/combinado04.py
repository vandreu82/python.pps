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

# excepción personalizada para operaciones no válidas
class OperacionNoValida(Exception):
    pass

# iteración que rompemos con quit, exit o q
try:
    while True:
        try:
            entrada = input("Introduce la operación: ").strip().upper()

            if entrada == "QUIT" or entrada == "EXIT" or entrada == "Q":
                print("Hasta luego, Mari Carmen")
                break
            
            # pequeña comprobación de errores
            partes = entrada.split()

            # si no hay al menos operación y un operando
            if len(partes) < 2:
                # índice fuera de rango equivalente a “faltan operandos”
                raise IndexError("La operación necesita al menos un operando.")

            comando = partes[0]

            if comando not in operaciones:
                # en vez de solo imprimir, lanzamos la excepción personalizada
                raise OperacionNoValida(comando)

            # comprobamos si es ANS y si no lo es lo convertimos a float
            operandos_txt = partes[1:]
            numeros = []

            for token in operandos_txt:
                if token == "ANS":
                    valor = ans
                else:
                    # aquí puede saltar ValueError si no es número
                    valor = float(token)
                numeros.append(valor)

            # comprobación de errores de sqrt
            if comando == "SQRT":
                # demasiados o insuficientes operandos para sqrt
                if len(numeros) != 1:
                    raise IndexError("SQRT solo utiliza un número.")
                x = numeros[0]

                if x < 0:
                    print("No puedes hacer la raíz de un número negativo.\n")
                    continue

                ans = math.sqrt(x)

            else:
                # comprobación de errores del resto y operaciones de niño de primaria
                if len(numeros) < 2:
                    # menos de dos números para ADD/SUB/MUL/DIV = IndexError
                    raise IndexError("La operación necesita al menos dos números.")

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
                        # aquí, si numeros[i] es 0, Python lanzará ZeroDivisionError(por favor, no hagas eso)
                        r = r / numeros[i]
                        i = i + 1
                    ans = r

            # si el resultado es un entero lo mostramos sin coma, si es un decimal, redondeamos a 2 decimales
            if int(ans) == ans:
                print("Resultado =", int(ans), "\n")
            else:
                print("Resultado =", round(ans, 2), "\n")

        except ValueError:
            print("Error: alguno de los operandos no es numérico.\n")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.\n")
        except IndexError as e:
            print("Error de número de operandos:", e, "\n")
        except OperacionNoValida as e:
            print(f"Error: el comando '{e}' no está disponible.\n")

except KeyboardInterrupt:
    print("\nEjecución interrumpida por el usuario. Hasta luego, Mari Carmen\n")


#!/usr/bin/python
#
# Ejercicio 2
# Modifica el ejercicio 3 de funciones para practicar el manejo de interrupciones. Se debe evitar la
# interrupción del programa tras:
# - Introducir erróneamente el nombre:
#   o Nombre vacío
#   o Faltan apellidos
#   o Uso de símbolos
# - Introducir erróneamente un DNI:
#   o Longitud insuficiente
#   o Letras en la parte numérica
#   o Falta la letra
#   o Letra incorrecta (algoritmo)
#   o DNI duplicado
# - Errores en el identificador:
#   o Identificador duplicado
#   o Nombre demasiado corto para generar un identificador
# - Interrupción del usuario por teclado
#
# Víctor Manuel Andreu Felipe 2025

from unidecode import unidecode

# excepciones personalizadas
class NombreInvalido(Exception):
    pass

class DNIInvalido(Exception):
    pass

class IdentificadorInvalido(Exception):
    pass

# función para normalizar texto usando el estilo de ejercicios anteriores
def normalizar(texto):

    # convertimos todo a minúsculas
    texto = texto.lower()

    # eliminamos acentos con unidecode
    texto = unidecode(texto)

    # eliminamos cualquier signo de puntuación (apellidos compuestos, apostrofe)
    limpio = ""
    for caracter in texto:
        # si es letra o espacio, lo conservamos
        if caracter.isalpha() or caracter.isspace():
            limpio += caracter
        # si es signo de puntuación NO hacemos nada, simplemente no lo copiamos

    return limpio

"""
comprobamos si el nombre es válido:
- no puede estar vacío
- debe tener al menos nombre y un apellido
- no puede contener símbolos (solo letras y espacios)
"""
def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        raise NombreInvalido("Nombre vacío.")

    partes = nombre.split()
    if len(partes) < 2:
        raise NombreInvalido("Faltan apellidos (mínimo nombre y un apellido).")

    # comprobamos que solo haya letras y espacios
    for c in nombre:
        if not (c.isalpha() or c.isspace()):
            raise NombreInvalido("El nombre no puede contener símbolos ni números.")

    return nombre

"""
el dni tiene 7 u 8 números y una letra final
la letra se calcula con numero % 23 y la cadena TRWAGMYFPDXBNJZSQVHLCKE
también comprobamos que no esté duplicado
"""
def validar_dni(dni, dnis_existentes):
    dni = dni.strip().upper()

    # longitud insuficiente (mínimo 8: 7 números + 1 letra)
    if len(dni) < 8:
        raise DNIInvalido("Longitud de DNI insuficiente (mínimo 7 u 8 dígitos y una letra).")

    # falta la letra o formato raro
    # si todos son dígitos, falta la letra
    if dni.isdigit():
        raise DNIInvalido("Falta la letra del DNI.")

    numero = dni[:-1]
    letra = dni[-1]

    # letras en la parte numérica
    if not numero.isdigit():
        raise DNIInvalido("La parte numérica del DNI contiene letras.")

    # letra debe ser alfabética
    if not letra.isalpha():
        raise DNIInvalido("El DNI debe terminar en una letra.")

    # letra incorrecta (algoritmo)
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero_int = int(numero)
    letra_correcta = tabla[numero_int % 23]

    if letra != letra_correcta:
        raise DNIInvalido(f"Letra incorrecta, debería ser {letra_correcta}.")

    # dni duplicado
    if dni in dnis_existentes:
        raise DNIInvalido("DNI duplicado, ya existe en el sistema.")

    return dni

"""
coge las dos primeras letras de cada palabra del nombre
normalizadas sin acentos ni mayúsculas
y añade los últimos tres dígitos del dni
comprueba que el nombre tenga suficiente longitud para generar el identificador
"""
def crear_identificador(nombre, dni, ids_existentes):
    nombre_norm = normalizar(nombre)
    partes = nombre_norm.split()

    letras = ""
    for p in partes:
        if len(p) < 2:
            raise IdentificadorInvalido("Nombre demasiado corto para generar identificador.")
        letras += p[:2]

    # últimos tres dígitos del dni (antes de la letra)
    parte_numerica = dni[:-1]
    ultimos = parte_numerica[-3:]

    identificador = letras + ultimos

    # identificador duplicado
    if identificador in ids_existentes:
        raise IdentificadorInvalido("Identificador duplicado, cambia el nombre o revisa el DNI.")

    return identificador

# función para mostrar socios ordenados por identificador
def mostrar_socios(diccionario):
    print("\nListado de socios ordenado:\n")
    for identificador in sorted(diccionario):
        nombre, dni = diccionario[identificador]
        print(f"{identificador}: {nombre} - {dni}")
    print()

# programa principal
def menu():
    socios = {}          # identificador -> (nombre, dni)
    dnis_existentes = set()
    ids_existentes = set()

    print("Gestión de socios. CTRL + C o EXIT en nombre/DNI para terminar.\n")

    while True:
        try:
            # pedimos nombre hasta que sea válido
            while True:
                nombre = input("Nombre completo: ").strip()
                if nombre.upper() == "EXIT":
                    print("Hasta luego, Mari Carmen")
                    mostrar_socios(socios)
                    return
                try:
                    nombre = validar_nombre(nombre)
                    break
                except NombreInvalido as e:
                    print("Error en el nombre:", e, "\n")

            # pedimos dni hasta que sea válido
            while True:
                dni = input("DNI: ").strip().upper()
                if dni == "EXIT":
                    print("Hasta luego, Mari Carmen")
                    mostrar_socios(socios)
                    return
                try:
                    dni = validar_dni(dni, dnis_existentes)
                    break
                except DNIInvalido as e:
                    print("Error en el DNI:", e, "\n")

            # creamos identificador (puede dar errores)
            try:
                identificador = crear_identificador(nombre, dni, ids_existentes)
            except IdentificadorInvalido as e:
                print("Error en el identificador:", e, "\n")
                # si el identificador falla, no guardamos nada y volvemos a empezar con este socio
                continue

            # guardamos datos
            socios[identificador] = (nombre, dni)
            dnis_existentes.add(dni)
            ids_existentes.add(identificador)

            print(f"Identificador creado: {identificador}\n")

        except KeyboardInterrupt:
            print("\nInterrupción por teclado. Mostrando socios y saliendo...\n")
            mostrar_socios(socios)
            break

# ejecutar programa
menu()
