#!/usr/bin/python
#
# Ejercicio 3
# Escribe un programa en Python que gestione la creación de identificadores únicos para los
# socios de un club.
# El programa debe solicitar al usuario el nombre completo y el DNI de cada socio, y generar
# automáticamente un identificador personal compuesto por las primeras dos letras de cada
# nombre y apellido (en caso de que tenga varios) y los últimos 3 dígitos del DNI.
# Utiliza funciones para:
# a) Comprobar la veracidad del DNI
#    a. Número de dígitos (7 u 8)
#    b. Letra correcta (Investiga el algoritmo utilizado para la asignación de letras)
# b) Creación del identificador. Ejemplo:
#    a. Nombre: José Manuel López García
#    b. DNI: 12345678Z
#    c. Identificador: jomaloga678 (normaliza el texto de forma que no se incluyan
#       mayúsculas ni acentos)
# c) Muestra todos los identificadores junto con el usuario y su DNI de forma ordenada.
#
# Víctor Manuel Andreu Felipe 2025

from unidecode import unidecode

# función para normalizar texto
def normalizar(texto):

    # convertimos todo a minúsculas
    texto = texto.lower()

    # eliminamos acentos con unidecode
    texto = unidecode(texto)

    # eliminamos cualquier signo de puntuación(apellidos compuestos, apostrofe)
    limpio = ""
    for caracter in texto:
        # si es letra o espacio, lo conservamos
        if caracter.isalpha() or caracter.isspace():
            limpio += caracter
        # si es signo de puntuación NO hacemos nada, simplemente no lo copiamos

    return limpio

# función para validar el nombre
"""
el nombre no puede estar vacío
debe tener al menos nombre y un apellido
no puede contener símbolos ni números, solo letras y espacios
"""
def validar_nombre(nombre):
    nombre = nombre.strip()

    if nombre == "":
        raise ValueError("Nombre vacío.")

    partes = nombre.split()
    if len(partes) < 2:
        raise ValueError("Faltan apellidos. Introduce al menos nombre y un apellido.")

    for c in nombre:
        if not (c.isalpha() or c.isspace()):
            raise ValueError("El nombre no puede contener símbolos ni números.")

    return nombre

"""
el dni tiene 7 u 8 números y una letra final
la letra se calcula con numero % 23 y la cadena TRWAGMYFPDXBNJZSQVHLCKE
comprobamos:
- longitud insuficiente
- letras en la parte numérica
- falta la letra
- letra incorrecta
"""
def validar_dni(dni):
    dni = dni.strip().upper()

    # longitud insuficiente (mínimo 7 u 8 dígitos + 1 letra)
    if len(dni) < 8 or len(dni) > 9:
        raise ValueError("Longitud insuficiente. Debe tener 7 u 8 dígitos y una letra final.")

    # si todos los caracteres son dígitos, falta la letra
    if dni.isdigit():
        raise ValueError("Falta la letra del DNI.")

    numero = dni[:-1]
    letra = dni[-1]

    # letras en la parte numérica
    if not numero.isdigit():
        raise ValueError("La parte numérica del DNI contiene letras.")

    # falta la letra o no es una letra
    if not letra.isalpha():
        raise ValueError("El DNI debe terminar en una letra.")

    # letra correcta según el algoritmo
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero_int = int(numero)
    letra_correcta = tabla[numero_int % 23]

    if letra != letra_correcta:
        raise ValueError(f"Letra incorrecta. Debería ser {letra_correcta}.")

    return dni

"""
coge las dos primeras letras de cada palabra del nombre
normalizadas sin acentos ni mayúsculas
y añade los últimos tres dígitos del dni
comprobamos que el nombre tenga mínimo 2 letras por palabra
"""
def crear_identificador(nombre, dni):
    nombre_norm = normalizar(nombre)
    partes = nombre_norm.split()

    letras = ""
    for p in partes:
        if len(p) < 2:
            raise ValueError("Nombre demasiado corto para generar un identificador (palabras de una sola letra).")
        letras += p[:2]

    # últimos tres dígitos de la parte numérica del dni (antes de la letra)
    parte_numerica = dni[:-1]
    ultimos = parte_numerica[-3:]  # tres últimos números del dni

    return letras + ultimos

# función para mostrar socios ordenados por identificador
def mostrar_socios(diccionario):
    print("\nListado de socios ordenado:\n")
    for identificador in sorted(diccionario):
        nombre, dni = diccionario[identificador]
        print(f"{identificador}: {nombre} - {dni}")
    print()

# función para añadir un socio nuevo
def anadir_socio(socios, dnis_existentes):
    while True:
        try:
            nombre = input("Nombre completo (o EXIT para cancelar): ").strip()
            if nombre.upper() == "EXIT":
                print("Alta cancelada.\n")
                return

            # validar nombre
            validar_nombre(nombre)

            dni = input("DNI (o EXIT para cancelar): ").strip().upper()
            if dni == "EXIT":
                print("Alta cancelada.\n")
                return

            # validar dni (formato, letra, etc.)
            dni = validar_dni(dni)

            # comprobar dni duplicado
            if dni in dnis_existentes:
                print("Error: DNI duplicado, ya existe en el sistema.\n")
                continue

            # crear identificador (puede fallar por nombre corto)
            identificador = crear_identificador(nombre, dni)

            # comprobación de identificador duplicado
            if identificador in socios:
                print("Error: identificador duplicado, cambia el nombre o revisa el DNI.\n")
                continue

            # si todo va bien, guardamos
            socios[identificador] = (nombre, dni)
            dnis_existentes.add(dni)

            print(f"Identificador creado: {identificador}\n")
            break

        except ValueError as e:
            # cualquier error de validación de nombre, dni o identificador
            print("Error:", e, "\n")
            # vuelve al principio del while y repite alta

# programa principal con menú
def menu():
    socios = {}
    dnis_existentes = set()

    try:
        while True:
            print("===== GESTIÓN DE SOCIOS =====")
            print("1. Añadir socio")
            print("2. Mostrar todos los socios")
            print("3. Salir")
            print("=============================")

            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                anadir_socio(socios, dnis_existentes)
            elif opcion == "2":
                mostrar_socios(socios)
            elif opcion == "3":
                print("Hasta luego, buen día.")
                break
            else:
                print("Opción no válida.\n")

    except KeyboardInterrupt:
        print("\nInterrupción por teclado. Saliendo del programa...\n")
        mostrar_socios(socios)

# ejecutar programa
menu()