import random

# parte 1 - personajes (héroes)

class Personaje:
    def __init__(self, nombre, clase, vida_max, ataque_base, clase_armadura, velocidad):
        # constructor de la clase se ejecuta al crear un nuevo personaje.
        self.nombre = nombre
        self.clase = clase
        self.vida_max = vida_max
        self.vida = vida_max  # vida actual
        self.ataque_base = ataque_base
        self.clase_armadura = clase_armadura
        self.velocidad = velocidad

    # comprueba si el personaje sigue con vida
    def esta_vivo(self):
        return self.vida > 0

    # aplica daño al personaje sin bajar de 0
    def recibir_daño(self, cantidad):
        cantidad = max(0, cantidad)
        self.vida = max(0, self.vida - cantidad)
        print(f"{self.nombre} recibe {cantidad} puntos de daño. Vida actual: {self.vida}/{self.vida_max}")

    # simula un dado de 20 caras
    def tirar_d20(self):
        return random.randint(1, 20)

    # ataque genérico reutilizable por las subclases
    def atacar(self, objetivo, modificador_atributo, dado_ataque):
        d20 = self.tirar_d20()
        total_ataque = d20 + modificador_atributo
        print(f"{self.nombre} ataca a {objetivo.nombre}. Tirada d20: {d20} + modificador {modificador_atributo} = {total_ataque}")

        if total_ataque >= objetivo.clase_armadura:
            daño = random.randint(1, dado_ataque)
            print(f"¡Impacto! {self.nombre} hace {daño} puntos de daño.")
            objetivo.recibir_daño(daño)
        else:
            print(f"{self.nombre} falla el ataque contra {objetivo.nombre} (CA objetivo: {objetivo.clase_armadura}).")

    # representación en texto del personaje
    def __str__(self):
        return (f"{self.nombre} ({self.clase}) - Vida: {self.vida}/{self.vida_max}, "
                f"CA: {self.clase_armadura}, Velocidad: {self.velocidad}")


class Guerrero(Personaje):
    def __init__(self, nombre):
        # se inicializa con valores propios de un guerrero
        super().__init__(nombre, "Guerrero", vida_max=40, ataque_base=10, clase_armadura=15, velocidad=10)
        self.fuerza = 4  # modificador de atributo

    # ataque básico del guerrero
    def atacar_basico(self, objetivo):
        self.atacar(objetivo, self.fuerza, self.ataque_base)

    # habilidad especial del guerrero
    def abocajarro(self, objetivo):
        print(f"{self.nombre} usa ABOCAJARRO contra {objetivo.nombre}.")
        d20 = self.tirar_d20()
        total_ataque = d20 + self.fuerza
        print(f"Tirada d20: {d20} + fuerza {self.fuerza} = {total_ataque}")

        if total_ataque >= objetivo.clase_armadura:
            daño = random.randint(1, self.ataque_base + self.fuerza)
            print(f"¡ABOCAJARRO impacta! Daño infligido: {daño}")
            objetivo.recibir_daño(daño)
            daño_rebote = max(1, self.fuerza // 2)
            print(f"Como penalización, {self.nombre} recibe {daño_rebote} puntos de daño de rebote.")
            self.recibir_daño(daño_rebote)
        else:
            print(f"{self.nombre} falla el ataque ABOCAJARRO contra {objetivo.nombre}.")


class Mago(Personaje):
    def __init__(self, nombre):
        # se inicializa con valores propios de un mago
        super().__init__(nombre, "Mago", vida_max=25, ataque_base=8, clase_armadura=12, velocidad=12)
        self.inteligencia = 5

    # ataque básico del mago
    def atacar_basico(self, objetivo):
        self.atacar(objetivo, self.inteligencia, self.ataque_base)

    # habilidad especial del mago
    def bola_fuego(self, objetivo):
        print(f"{self.nombre} lanza BOLA DE FUEGO a {objetivo.nombre}.")
        d20 = self.tirar_d20()
        total_ataque = d20 + self.inteligencia
        print(f"Tirada d20: {d20} + inteligencia {self.inteligencia} = {total_ataque}")

        if total_ataque >= objetivo.clase_armadura:
            daño = random.randint(1, self.inteligencia * 2)
            print(f"¡La bola de fuego impacta! Daño infligido: {daño}")
            objetivo.recibir_daño(daño)
        else:
            print(f"{self.nombre} falla la BOLA DE FUEGO contra {objetivo.nombre}.")


class Asesino(Personaje):
    def __init__(self, nombre):
        # se inicializa con valores propios de un asesino
        super().__init__(nombre, "Asesino", vida_max=30, ataque_base=9, clase_armadura=13, velocidad=14)
        self.destreza = 5

    # ataque básico del asesino
    def atacar_basico(self, objetivo):
        self.atacar(objetivo, self.destreza, self.ataque_base)

    # habilidad especial del asesino
    def ataque_critico(self, objetivo):
        print(f"{self.nombre} intenta un ATAQUE CRÍTICO contra {objetivo.nombre}.")
        d20 = self.tirar_d20()
        total_ataque = d20 + self.destreza
        print(f"Tirada d20: {d20} + destreza {self.destreza} = {total_ataque}")

        if total_ataque >= objetivo.clase_armadura:
            base_daño = random.randint(1, self.ataque_base)
            if d20 % 2 == 0:
                daño = base_daño * 2
                print(f"Tirada par → DAÑO CRÍTICO. {base_daño} x 2 = {daño}")
            else:
                daño = max(1, base_daño // 2)
                print(f"Tirada impar → daño reducido. {base_daño} // 2 = {daño}")
            objetivo.recibir_daño(daño)
        else:
            print(f"{self.nombre} falla el ATAQUE CRÍTICO contra {objetivo.nombre}.")


class Clerigo(Personaje):
    def __init__(self, nombre):
        # se inicializa con valores propios de un clérigo
        super().__init__(nombre, "Clérigo", vida_max=32, ataque_base=6, clase_armadura=14, velocidad=8)
        self.fe = 5

    # ataque básico del clérigo
    def atacar_basico(self, objetivo):
        self.atacar(objetivo, self.fe, self.ataque_base)

    # habilidad especial del clérigo (curación)
    def curar(self, objetivo):
        print(f"{self.nombre} lanza un hechizo de CURACIÓN sobre {objetivo.nombre}.")
        cantidad = random.randint(1, self.fe * 2)
        vida_antes = objetivo.vida
        objetivo.vida = min(objetivo.vida_max, objetivo.vida + cantidad)
        curado = objetivo.vida - vida_antes
        print(f"{objetivo.nombre} recupera {curado} puntos de vida. Vida actual: {objetivo.vida}/{objetivo.vida_max}")


# parte 2 - monstruos

class Monstruo:
    def __init__(self, nombre, ataque, vida_max, clase_armadura, velocidad, ataque_base):
        # datos básicos del monstruo
        self.nombre = nombre
        self.ataque = ataque
        self.vida_max = vida_max
        self.vida = vida_max
        self.clase_armadura = clase_armadura
        self.velocidad = velocidad
        self.ataque_base = ataque_base

    # comprueba si el monstruo sigue vivo
    def esta_vivo(self):
        return self.vida > 0

    # aplica daño al monstruo sin bajar de 0
    def recibir_daño(self, cantidad):
        cantidad = max(0, cantidad)
        self.vida = max(0, self.vida - cantidad)
        print(f"{self.nombre} recibe {cantidad} puntos de daño. Vida actual: {self.vida}/{self.vida_max}")

    # simula un dado de 20 caras
    def tirar_d20(self):
        return random.randint(1, 20)

    # ataque genérico del monstruo contra un héroe
    def atacar(self, heroe):
        d20 = self.tirar_d20()
        total_ataque = d20 + self.ataque
        print(f"{self.nombre} ataca a {heroe.nombre}. Tirada d20: {d20} + ataque {self.ataque} = {total_ataque}")

        if total_ataque >= heroe.clase_armadura:
            daño = random.randint(1, self.ataque_base)
            print(f"¡El ataque del monstruo impacta! {self.nombre} hace {daño} puntos de daño.")
            heroe.recibir_daño(daño)
        else:
            print(f"{self.nombre} falla el ataque contra {heroe.nombre} (CA objetivo: {heroe.clase_armadura}).")

    # representación en texto del monstruo
    def __str__(self):
        return (f"{self.nombre} (Monstruo) - Vida: {self.vida}/{self.vida_max}, "
                f"CA: {self.clase_armadura}, Velocidad: {self.velocidad}")


class Goblin(Monstruo):
    def __init__(self, nombre="Goblin"):
        # goblin con estadísticas predeterminadas
        super().__init__(nombre, ataque=2, vida_max=15, clase_armadura=11, velocidad=11, ataque_base=6)


class Orco(Monstruo):
    def __init__(self, nombre="Orco"):
        # orco con estadísticas predeterminadas
        super().__init__(nombre, ataque=4, vida_max=25, clase_armadura=13, velocidad=9, ataque_base=8)


# parte 3 - creación del grupo de héroes

def elegir_clase():
    while True:
        print("\n" + "=" * 50)
        print("             SELECCIÓN DE CLASE")
        print("=" * 50)
        print("1. Guerrero")
        print("2. Mago")
        print("3. Asesino")
        print("4. Clérigo")
        print("-" * 50)

        opcion = input("Elige una clase (1-4): ").strip()
        if opcion == "1":
            return "Guerrero"
        elif opcion == "2":
            return "Mago"
        elif opcion == "3":
            return "Asesino"
        elif opcion == "4":
            return "Clérigo"
        else:
            # mensaje de error sin emotes
            print("\nOpción no válida. Intenta de nuevo.")


def crear_heroe():
    print("\n" + "=" * 50)
    print("             CREACIÓN DE HÉROE")
    print("=" * 50)
    nombre = input("Introduce el nombre del héroe: ").strip()
    if not nombre:
        nombre = "Héroe sin nombre"

    clase = elegir_clase()

    # se devuelve una instancia según la clase elegida
    if clase == "Guerrero":
        return Guerrero(nombre)
    elif clase == "Mago":
        return Mago(nombre)
    elif clase == "Asesino":
        return Asesino(nombre)
    elif clase == "Clérigo":
        return Clerigo(nombre)


def mostrar_grupo(grupo):
    print("\n" + "=" * 50)
    print("             GRUPO ACTUAL")
    print("=" * 50)
    if not grupo:
        print("El grupo de héroes está vacío.")
        print("=" * 50)
        return

    # se muestra cada héroe con su índice
    for i, heroe in enumerate(grupo, start=1):
        print(f"{i}. {heroe}")
    print("=" * 50)


def eliminar_heroe(grupo):
    if not grupo:
        print("\nNo hay héroes que eliminar.")
        return

    mostrar_grupo(grupo)
    while True:
        opcion = input("Elige el número del héroe a eliminar (Enter para cancelar): ").strip()
        if opcion == "":
            print("Eliminación cancelada.")
            return
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(grupo):
                eliminado = grupo.pop(idx)
                print(f"Héroe eliminado: {eliminado.nombre}")
                return
        print("Opción no válida, intenta de nuevo.")


def menu_creacion_campaña():
    grupo = []

    while True:
        print("\n" + "=" * 50)
        print("       CREACIÓN DE PERSONAJES DE CAMPAÑA")
        print("=" * 50)
        print(f"Héroes en el grupo: {len(grupo)}/3")
        print("-" * 50)
        print("1. Añadir nuevo héroe")
        print("2. Ver grupo actual")
        print("3. Eliminar héroe")
        print("4. Terminar creación y continuar")
        print("-" * 50)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            if len(grupo) >= 3:
                print("\n Ya tienes el máximo de 3 héroes.")
            else:
                heroe = crear_heroe()
                grupo.append(heroe)
                print(f"\n Héroe añadido: {heroe.nombre} ({heroe.clase})")

        elif opcion == "2":
            mostrar_grupo(grupo)

        elif opcion == "3":
            eliminar_heroe(grupo)

        elif opcion == "4":
            if len(grupo) == 3:
                print("\n Creación completada. ¡A la aventura!")
                return grupo
            else:
                print("\n Debes tener exactamente 3 héroes antes de continuar.")

        else:
            # mensaje de opción inválida sin emotes
            print("\n Opción inválida. Intenta de nuevo.")


# parte 4 - sistema de combate

def heroes_vivos(grupo_heroes):
    # devuelve la lista de héroes que aún tienen vida
    return [h for h in grupo_heroes if h.esta_vivo()]


def monstruos_vivos(grupo_monstruos):
    # devuelve la lista de monstruos que aún tienen vida
    return [m for m in grupo_monstruos if m.esta_vivo()]


def elegir_objetivo_monstruo(monstruos):
    vivos = [m for m in monstruos if m.esta_vivo()]
    if not vivos:
        return None

    while True:
        print("\nElige un monstruo a atacar:")
        for i, m in enumerate(vivos, start=1):
            print(f"{i}. {m}")
        opcion = input("Número de monstruo: ").strip()
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(vivos):
                return vivos[idx]
        print("Opción no válida, intenta de nuevo.")


def elegir_aliado_para_curar(grupo_heroes):
    vivos = [h for h in grupo_heroes if h.esta_vivo()]
    if not vivos:
        return None

    while True:
        print("\nElige un aliado para curar:")
        for i, h in enumerate(vivos, start=1):
            print(f"{i}. {h}")
        opcion = input("Número de héroe: ").strip()
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(vivos):
                return vivos[idx]
        print("Opción no válida, intenta de nuevo.")


def turno_heroe(heroe, grupo_heroes, grupo_monstruos):
    # si el héroe está muerto, se salta su turno
    if not heroe.esta_vivo():
        return

    print("\n" + "-" * 50)
    print(f"Turno de {heroe.nombre} ({heroe.clase}) - Vida: {heroe.vida}/{heroe.vida_max}")
    print("-" * 50)
    while True:
        print("Acciones:")
        print("1. Ataque básico")
        print("2. Usar habilidad especial")
        print("3. Pasar turno")
        opcion = input("Elige una acción: ").strip()

        if opcion == "1":
            objetivo = elegir_objetivo_monstruo(grupo_monstruos)
            if objetivo:
                heroe.atacar_basico(objetivo)
            return

        elif opcion == "2":
            # cada clase usa su habilidad especial
            if isinstance(heroe, Clerigo):
                aliado = elegir_aliado_para_curar(grupo_heroes)
                if aliado:
                    heroe.curar(aliado)
            elif isinstance(heroe, Guerrero):
                objetivo = elegir_objetivo_monstruo(grupo_monstruos)
                if objetivo:
                    heroe.abocajarro(objetivo)
            elif isinstance(heroe, Mago):
                objetivo = elegir_objetivo_monstruo(grupo_monstruos)
                if objetivo:
                    heroe.bola_fuego(objetivo)
            elif isinstance(heroe, Asesino):
                objetivo = elegir_objetivo_monstruo(grupo_monstruos)
                if objetivo:
                    heroe.ataque_critico(objetivo)
            return

        elif opcion == "3":
            print(f"{heroe.nombre} pasa su turno.")
            return

        else:
            print("Opción no válida, intenta de nuevo.")


def turno_monstruo(monstruo, grupo_heroes):
    # si el monstruo está muerto, no hace nada
    if not monstruo.esta_vivo():
        return

    objetivos = [h for h in grupo_heroes if h.esta_vivo()]
    if not objetivos:
        return

    # el monstruo elige un héroe al azar
    objetivo = random.choice(objetivos)
    print("\n" + "-" * 50)
    print(f"Turno del monstruo: {monstruo.nombre}")
    monstruo.atacar(objetivo)


def combate(grupo_heroes, grupo_monstruos):
    # bucle principal de combate por rondas
    ronda = 1
    while heroes_vivos(grupo_heroes) and monstruos_vivos(grupo_monstruos):
        print("\n" + "=" * 50)
        print(f"                 RONDA {ronda}")
        print("=" * 50)

        vivos_heroes = heroes_vivos(grupo_heroes)
        vivos_monstruos = monstruos_vivos(grupo_monstruos)
        combatientes = vivos_heroes + vivos_monstruos

        # orden por velocidad (mayor primero) y héroes antes que monstruos en empate
        combatientes.sort(key=lambda c: (-c.velocidad, 0 if isinstance(c, Personaje) else 1))

        for combatiente in combatientes:
            # se comprueba en cada iteración si aún hay combate
            if not heroes_vivos(grupo_heroes) or not monstruos_vivos(grupo_monstruos):
                break

            if isinstance(combatiente, Personaje):
                turno_heroe(combatiente, grupo_heroes, grupo_monstruos)
            else:
                turno_monstruo(combatiente, grupo_heroes)

        ronda += 1

    if heroes_vivos(grupo_heroes):
        print("\n¡VICTORIA! Los héroes han derrotado a todos los monstruos.")
    else:
        print("\nDERROTA... Los héroes han caído en combate.")


# parte 5 - aventura

def aventura(grupo_heroes):
    print("\n\n" + "=" * 50)
    print("          COMIENZA LA AVENTURA EN PYTHONIA")
    print("=" * 50)
    print("Los héroes se adentran en una mazmorra llena de peligros...")

    # grupo fijo de monstruos para el encuentro
    grupo_monstruos = [
        Goblin("Goblin 1"),
        Goblin("Goblin 2"),
        Orco("Orco jefe")
    ]

    print("\nEnemigos encontrados:")
    for m in grupo_monstruos:
        print(f"- {m}")

    combate(grupo_heroes, grupo_monstruos)

    if heroes_vivos(grupo_heroes):
        print("\nLos héroes sobreviven a este encuentro... ¡por ahora!")
    else:
        print("\nEl reino de Pythonia queda sumido en la oscuridad...")


# bloque principal

if __name__ == "__main__":
    print("=" * 50)
    print("             ¡SALVEMOS PYTHONIA!")
    print("=" * 50)
    grupo = menu_creacion_campaña()
    aventura(grupo)
    print("\nGracias por jugar. Fin de la partida.")