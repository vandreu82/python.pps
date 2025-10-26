#!/usr/bin/python
#
# Ejercicio 4
# Conversor de divisas: USD, EUR, GBP, CAD, y JPY. Se le pasa “divisa de origen”, “divisa destino”
# y “cantidad”. Proceso a seguir: ?????
#
#   Víctor Manuel Andreu Felipe 2025

print("Conversor de divisas disponibles: USD, EUR, GBP, CAD, JPY")
print("Escribe 'SALIR' para terminar.\n")

# tasa de cambio con el euro
usd = 1.16
gbp = 0.87
cad = 1.63
jpy = 177.66
eur = 1.0

# iteración con salida

while True:
    origen = input("Divisa de origen: ").strip().upper()
    if origen == "SALIR":
        print("Hasta luego, buen día.")
        break

    destino = input("Divisa de destino: ").strip().upper()
    
    cantidad = float(input("Cantidad a convertir: "))

    # convertimos a euro
    if origen == "EUR":
        cantidad_eur = cantidad
    elif origen == "USD":
        cantidad_eur = cantidad / usd
    elif origen == "GBP":
        cantidad_eur = cantidad / gbp
    elif origen == "CAD":
        cantidad_eur = cantidad / cad
    elif origen == "JPY":
        cantidad_eur = cantidad / jpy
    else:
        print("Divisa de origen no válida.\n")
        continue

    # convertimos a divisa final
    if destino == "EUR":
        cantidad_final = cantidad_eur * eur
    elif destino == "USD":
        cantidad_final = cantidad_eur * usd
    elif destino == "GBP":
        cantidad_final = cantidad_eur * gbp
    elif destino == "CAD":
        cantidad_final = cantidad_eur * cad
    elif destino == "JPY":
        cantidad_final = cantidad_eur * jpy
    else:
        print("Divisa de destino no válida.\n")
        continue

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

