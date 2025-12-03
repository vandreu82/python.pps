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
