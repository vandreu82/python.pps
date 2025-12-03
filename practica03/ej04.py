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