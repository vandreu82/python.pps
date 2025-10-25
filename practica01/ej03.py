#!/usr/bin/python
#
# Ejercicio 3
# Calculadora de edad. Usando el módulo ‘datetime’. El usuario introduce su fecha de nacimiento y el
# método calcula su edad. A tener en cuenta:
#   • Año actual – Año de nacimiento = edad
#   • Si Mes actual < Mes nacimiento: edad – 1
#   • Sino, si Mes actual = mes nacimiento
#       ◦ Si Día actual < Día nacimiento: edad – 1
#
#   Víctor Manuel Andreu Felipe 2025

from datetime import date

fecha = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")

dia_str, mes_str, anio_str = fecha.split("/")

dia = int(dia_str)
mes = int(mes_str)
anio = int(anio_str)

edad = date.today().year - anio

if date.today().month < mes:
    edad -= 1
elif date.today().month == mes and date.today().day < dia:
    edad -= 1
    
print("Tienes", edad, "años.")


