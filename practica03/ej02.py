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