import time

def imprime_lento(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.05)
    print()

def entrada_jugador():
    respuesta = input("> ").lower()
    return respuesta

def intro():
    imprime_lento("¡Bienvenido a 'La Aventura del Disco Perdido'!")
    imprime_lento("Año: 1977")
    imprime_lento("Ubicación: Una oscura discoteca en las afueras de la ciudad.")
    imprime_lento("Tu misión: encontrar el disco de vinilo perdido de la banda de rock 'Los Rizos Eléctricos'.")
    imprime_lento("¿Estás listo para comenzar? (si/no)")

    respuesta = entrada_jugador()
    if respuesta == "si":
        juego()
    else:
        imprime_lento("Tal vez en otra ocasión, amigo.")

def juego():
    imprime_lento("Te encuentras en la pista de baile de la discoteca.")
    imprime_lento("Luces de colores giran y la música retumba a tu alrededor.")
    imprime_lento("¿Qué quieres hacer?")
    imprime_lento("1. Ir a la barra")
    imprime_lento("2. Preguntarle al DJ")
    imprime_lento("3. Buscar en los reservados")

    respuesta = entrada_jugador()
    if respuesta == "1":
        barra()
    elif respuesta == "2":
        dj()
    elif respuesta == "3":
        reservados()
    else:
        imprime_lento("No entendí esa opción. Intenta de nuevo.")
        juego()

def barra():
    imprime_lento("Te acercas a la barra y ves a un cantinero de aspecto rudo secando un vaso.")
    imprime_lento("¿Qué quieres hacer?")
    imprime_lento("1. Pedir una bebida")
    imprime_lento("2. Preguntarle por el disco perdido")
    imprime_lento("3. Volver a la pista de baile")

    respuesta = entrada_jugador()
    if respuesta == "1":
        imprime_lento("El cantinero te mira con desconfianza y te sirve un trago.")
        imprime_lento("Después de unos tragos, tu cabeza da vueltas y decides volver a la pista.")
        juego()
    elif respuesta == "2":
        imprime_lento("'¿El disco perdido? No sé nada de eso, amigo. Pero escuché que el DJ podría saber algo.'")
        imprime_lento("El cantinero vuelve a sus quehaceres, ignorándote.")
        barra()
    elif respuesta == "3":
        juego()
    else:
        imprime_lento("No entendí esa opción. Intenta de nuevo.")
        barra()

def dj():
    imprime_lento("Te abres paso entre la multitud hasta llegar a la cabina del DJ.")
    imprime_lento("El DJ, un tipo con lentes de espejo y un afro impresionante, está mezclando discos.")
    imprime_lento("¿Qué quieres hacer?")
    imprime_lento("1. Preguntarle por el disco perdido")
    imprime_lento("2. Tratar de distraerlo para husmear en su equipo")
    imprime_lento("3. Volver a la pista de baile")

    respuesta = entrada_jugador()
    if respuesta == "1":
        imprime_lento("'¿El disco perdido de Los Rizos Eléctricos? Sí, escuché algo sobre eso.'")
        imprime_lento("'Dicen que el bajista lo tiene escondido en uno de los reservados privados.'")
        imprime_lento("'Pero no sé más, amigo. Tendrás que investigar por tu cuenta.'")
        dj()
    elif respuesta == "2":
        imprime_lento("Intentas distraer al DJ, pero es demasiado profesional.")
        imprime_lento("Te descubre husmeando y te echa a empujones de la cabina.")
        imprime_lento("Mejor no intentar eso de nuevo...")
        dj()
    elif respuesta == "3":
        juego()
    else:
        imprime_lento("No entendí esa opción. Intenta de nuevo.")
        dj()

def reservados():
    imprime_lento("Te diriges a la zona de reservados privados, ubicada en un rincón oscuro de la discoteca.")
    imprime_lento("Hay varias puertas con cortinas de cuentas colgando, cada una con un número.")
    imprime_lento("¿Qué quieres hacer?")
    imprime_lento("1. Intentar abrir una puerta al azar")
    imprime_lento("2. Buscar pistas sobre qué reservado podría ser")
    imprime_lento("3. Volver a la pista de baile")

    respuesta = entrada_jugador()
    if respuesta == "1":
        imprime_lento("Abres una puerta al azar y te encuentras con una pareja en una situación comprometida.")
        imprime_lento("Te echan a gritos y decides que es mejor no seguir intentando eso.")
        reservados()
    elif respuesta == "2":
        imprime_lento("Buscas alrededor y notas que hay un pequeño afiche en la pared.")
        imprime_lento("En él se anuncia que 'Los Rizos Eléctricos' estarán en el reservado 7 esta noche.")
        imprime_lento("¿Quieres intentar abrir el reservado 7? (si/no)")
        respuesta = entrada_jugador()
        if respuesta == "si":
            reservado_7()
        else:
            reservados()
    elif respuesta == "3":
        juego()
    else:
        imprime_lento("No entendí esa opción. Intenta de nuevo.")
        reservados()

def reservado_7():
    imprime_lento("Abres sigilosamente la puerta del reservado 7...")
    # Agregar lógica adicional aquí, como encontrar el disco, enfrentarse al bajista, etc.

intro()