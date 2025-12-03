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
