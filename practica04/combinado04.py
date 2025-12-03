#!/usr/bin/python
#
# Ejercicio 1
# Modifica el conversor de divisas (Ejercicio 2 de colecciones) para que:
#  a) cree nuevas monedas con su factor de conversión
#  b) permita modificar los factores de conversión
#  c) permita eliminar una tasa de conversión
#  d) muestre todos los factores de conversión ordenados
#
#   Víctor Manuel Andreu Felipe 2025


# diccionario de tasas de conversión respecto al euro
tasas = {
    "EUR": 1.0,
    "USD": 1.16,
    "GBP": 0.88,
    "JPY": 180.98,
    "CAD": 1.62
}

# función para crear una moneda nueva
def crear_moneda():

    # pedir código hasta que no exista
    while True:
        codigo = input("Introduce el código de la nueva moneda: ").strip().upper()
        # comprobación de errores
        if codigo in tasas:
            print("Esa moneda ya existe.\n")
        else:
            break

    # pedir factor hasta que sea válido
    while True:
        try:
            factor = float(input(f"Introduce el factor de conversión EUR -> {codigo}: "))
            break
        except ValueError:
            print("El factor debe ser un número.\n")

    tasas[codigo] = factor
    print(f"Moneda {codigo} añadida con factor {factor}\n")

# función para modificar la tasa de una moneda existente
def modificar_tasa():

    # pedir código hasta que exista
    while True:
        codigo = input("Introduce el código de la moneda a modificar: ").strip().upper()
        # comprobación de errores
        if codigo not in tasas:
            print("Esa moneda no existe.\n")
        else:
            break

    # pedir nuevo factor hasta que sea válido
    while True:
        try:
            factor = float(input(f"Introduce el nuevo factor de conversión EUR -> {codigo}: "))
            break
        except ValueError:
            print("El factor debe ser un número.\n")

    tasas[codigo] = factor
    print(f"Factor de {codigo} actualizado a {factor}\n")

# función para eliminar una moneda
def eliminar_moneda():

    # pedir código hasta que exista y no sea EUR
    while True:
        codigo = input("Introduce el código de la moneda a eliminar: ").strip().upper()
        # comprobación de errores
        if codigo not in tasas:
            print("Esa moneda no existe.\n")
        elif codigo == "EUR":
            print("No se puede eliminar EUR.\n")
        else:
            break

    del tasas[codigo]
    print(f"Moneda {codigo} eliminada correctamente.\n")

# función para mostrar las tasas ordenadas por código
def mostrar_tasas():
    print("\nTasas de conversión (EUR -> Divisa), ordenadas por código:")
    for codigo in sorted(tasas):
        print(f"  {codigo}: {tasas[codigo]}")
    print()

# función principal de conversión de divisas
def convertir_divisas():
    print("Conversor de divisas")
    print("Divisas disponibles:", ", ".join(sorted(tasas.keys())))
    print()

    # pedir origen hasta que sea válido
    while True:
        origen = input("Divisa de origen: ").strip().upper()
        # comprobación de errores
        if origen not in tasas:
            print("Divisa de origen no válida.\n")
        else:
            break

    # pedir destino hasta que sea válido
    while True:
        destino = input("Divisa de destino: ").strip().upper()
        if destino not in tasas:
            print("Divisa de destino no válida.\n")
        else:
            break

    # pedir cantidad hasta que sea válida
    while True:
        try:
            cantidad = float(input("Cantidad a convertir: "))
            break
        except ValueError:
            print("La cantidad debe ser un número.\n")

    # convertimos a euro
    cantidad_eur = cantidad / tasas[origen]

    # convertimos a la divisa final
    cantidad_final = cantidad_eur * tasas[destino]

    # resultado redondeado
    if int(cantidad) == cantidad:
        cantidad_mostrar = int(cantidad)
    else:
        cantidad_mostrar = round(cantidad, 2)

    if int(cantidad_final) == cantidad_final:
        cantidad_final_mostrar = int(cantidad_final)
    else:
        cantidad_final_mostrar = round(cantidad_final, 2)

    print(cantidad_mostrar, origen, "=", cantidad_final_mostrar, destino, "\n")

# menú principal
def menu():
    while True:
        print("===== CONVERSOR DE DIVISAS =====")
        print("1. Convertir divisas")
        print("2. Crear nueva moneda")
        print("3. Modificar tasa de conversión")
        print("4. Eliminar moneda")
        print("5. Mostrar todas las tasas")
        print("6. Salir")
        print("================================")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            convertir_divisas()
        elif opcion == "2":
            crear_moneda()
        elif opcion == "3":
            modificar_tasa()
        elif opcion == "4":
            eliminar_moneda()
        elif opcion == "5":
            mostrar_tasas()
        elif opcion == "6":
            print("Hasta luego, buen día.")
            break
        else:
            print("Opción no válida.\n")

# ejecutar el menú
menu()


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