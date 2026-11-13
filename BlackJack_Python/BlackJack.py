"""
Nombre del archivo: BlackJack.py
Descripción del programa: Es programa que simula el juego de BlackJack o 21, utilizando una librería de interfaz gráfica (sin apuestas).
Autores: Khristo Ricardo Rodriguez Valencia / Ángel Adrián Barragán Ruiz
Fecha: 10/11/2026
Grupo: 7
"""

# Importe de librerías
import tkinter as tk
from random import shuffle

# Definición de variables globales
DENOMINACIONES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
PALOS = ["♥", "♦", "♣", "♠"]
baraja = []
crupier = []
segundaCartaCrupier = []
puntCrupier = 0
jugador = []
puntJugador = 0

# ╔═══════ ≪ ° </Función Arreglar Valores> ° ≫ ═══════╗

def ArreglarValores(esJugador: bool, carta: tuple) -> tuple:
    """

        Asigna el valor numérico correspondiente a una carta especial ("A", "J", "Q", "K").

        Si la carta es un As ("A"), evalúa si su valor debe ser 1 u 11 dependiendo de si
        la puntuación total superaría los 21 puntos.

        Parameters:

            esJugador (bool): `True` si se evalúa la carta del jugador, `False` si es del crupier.
            carta (tuple): Tupla que contiene la carta a evaluar.

        Returns:

            tuple: Nueva tupla con el valor numérico ajustado y el mismo palo.

    """

    # Evalúa si se esta corrigiendo al jugador o al crupier.
    if esJugador:
        # Si la carta es jota, reina o rey devuelve la denominación 10.
        if carta[0] in "JQK":
            return (10,carta[1])

        # Si es un As, devuelve la denominación que más le combiene al jugador, ya sea 11 o 1.
        else:
            if 11 + puntJugador > 21:
                return (1,carta[1])
            else:
                return (11,carta[1])
    else:
        # Si la carta es jota, reina o rey devuelve la denominación 10.
        if carta[0] in "JQK":
            return (10,carta[1])

        # Si es un As, devuelve la denominación que más le combiene al crupier, ya sea 11 o 1.
        else:
            if 11 + puntCrupier > 21:
                return (1,carta[1])
            else:
                return (11,carta[1])

# ╚═══════ ≪ ° </Función Arreglar Valores> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Mostrar Carta> ° ≫ ═══════╗

def MostrarCarta(carta: tuple, esJugador: bool):
    """

        Genera y coloca gráficamente una carta en la interfaz (Tkinter).

        Si es la segunda carta del crupier en el turno inicial, se imprime boca abajo
        (oculta) hasta que sea su turno de revelarla.

        Parameters:

            carta (tuple): Tupla que representa la carta (valor, palo).
            esJugador (bool): `True` si la carta pertenece al jugador, `False` al crupier.

        Raises:

            TypeError: Si `carta` no es tupla o `esJugador` no es booleano.
            ValueError: Si el formato de la carta es inválido.

    """
    # Evalúa las excepciones.
    if not isinstance(carta, tuple) or not isinstance(esJugador, bool):
        raise TypeError("El argumento carta debe ser una tupla y el argumento es jugador debe ser un lógico")
    if not len(carta) == 2:
        raise ValueError("El argumento carta debe tener 2 elementos dentro de la tupla.")
    if not 1 <= len(carta[0]) <= 2 or not carta[1] in PALOS:
        raise ValueError("El primer elemento del argumento carta debe tener 1 o 2 caracteres, o el segundo elemento del argumento carta debe estar en la constante PALOS.")
    if len(carta[0]) == 2 and not carta[0] == "10":
        raise ValueError("El primer elemento del argumento carta que tiene 2 caracteres debe ser la cadena '10'.")
    global crupier, jugador, segundaCartaCrupier

    # Se asignan el valor y el palo a las variables.
    valor = carta[0]
    palo = carta[1]

    # En caso de que sea un solo dígito se dibuja una carta a la medida.
    if len(valor) == 1:
        textoCarta = (
            f"┌───────┐\n"
            f"│{valor}      │\n"
            f"│       │\n"
            f"│   {palo}   │\n"
            f"│       │\n"
            f"│      {valor}│\n"
            f"└───────┘"
        )
    # En caso de que sea de 2 dígitos se dibuja una carta a la medida.
    else:
        textoCarta = (
            f"┌───────┐\n"
            f"│{valor}     │\n"
            f"│       │\n"
            f"│   {palo}   │\n"
            f"│       │\n"
            f"│     {valor}│\n"
            f"└───────┘"
        )

    # Evalúa si es el jugador o es el crupier.
    # Caso Jugador:
    if esJugador:
        # Muestra la carta normal sin taparla.
        dibujoCarta = tk.Label(marcoManoJugador, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")
        dibujoCarta.grid(column=jugador.index(carta), row=0, sticky="w")
    else:
        # Evalúa si aún no existe la segunda carta del crupier y si la carta obtenida es la segunda carta del crupier.
        # En el caso que se cumplan las premisas anteriores, entonces se imprime la carta sin tapar.
        # En caso de que no se cumpla alguna o ninguna de las premisas, significa que estamos en la segunda carta y se muestra oculta. 
        if len(segundaCartaCrupier) != 0 and carta == segundaCartaCrupier[0]:
            dibujoCarta = tk.Label(marcoManoCrupier, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")
            dibujoCarta.grid(column=4, row=0, sticky="e")
        else:
            if len(crupier) == 2 and crupier.index(carta) == 1:
                textoCarta = (
                    f"┌───────┐\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"└───────┘"
                )
                segundaCartaCrupier.append(carta)
            dibujoCarta = tk.Label(marcoManoCrupier, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")

            # Si la carta es la segunda, se imprime siempre en el espacio para la segunda, de lo contrario se le asigna el espacio correspondiente.
            if carta in segundaCartaCrupier:
                dibujoCarta.grid(column=4, row=0, sticky="e")
            else:
                columna_pos = 5 - (len(crupier) - 1)
                dibujoCarta.grid(column=columna_pos, row=0, sticky="e")

# ╚═══════ ≪ ° </Función Mostrar Carta> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Verificar Blackjack> ° ≫ ═══════╗

def VerificarBlackjack() -> int:
    """

        Evalúa si el puntaje del crupier o del jugador es exactamente 21 puntos.

        Returns:

            int: Devuelve `0` si nadie tiene 21 (el juego sigue), `1` si el crupier tiene 21,
            `2` si el jugador tiene 21, y `3` si ambos tienen 21 (empate).

        Examples:

            >>> puntJugador = 21
            >>> puntCrupier = 17
            >>> VerificarBlackjack()
            2

    """
    # Se definen las variables globales
    global puntJugador, puntCrupier

    # Se evalúa si hubo un empate de blackjack natural, un blackjack del jugador natural o un blackjack del crupier natural,
    # en caso de no haber pasado ninguna de las 3 devuelve 0
    if puntCrupier == 21 and puntJugador == 21:
        return 3
    elif puntJugador == 21:
        return 2
    elif puntCrupier == 21:
        return 1
    else:
        return 0

# ╚═══════ ≪ ° </Función Verificar Blackjack> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Verificar Sobre-puntaje> ° ≫ ═══════╗

def VerificarSobrepuntaje() -> int:
    """

        Evalúa si el puntaje del crupier o del jugador superó los 21 puntos.

        Returns:

            int: Devuelve `0` si nadie se ha pasado, `1` si el crupier se pasó de 21,
            `2` si el jugador se pasó de 21.

    """
    # Se definen las variables globales
    global puntJugador, puntCrupier

    # Evalúa si se pasó de 21 el crupier o el jugador, en caso de que no devuelve 0
    if puntCrupier > 21:
        return 1
    elif puntJugador > 21:
        return 2
    return 0

# ╚═══════ ≪ ° </Función Verificar Sobre-puntaje> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Verificar Puntajes Finales> ° ≫ ═══════╗

def VerificarPuntajesFinales() -> int:
    """

        Evalúa el puntaje final del crupier y del jugador para determinar al ganador.

        Esta función asume que ninguno de los jugadores se ha pasado de 21 puntos.

        Returns:

            int: Devuelve `1` si el crupier ganó, `2` si el jugador ganó,
            y `3` si fue un empate.

    """
    # Se definen las variables globales
    global puntJugador, puntCrupier

    # Evalúa si hubo un empate, si ganó el jugador o si ganó el crupier, todo legal sin pasarse de 21,
    # en caso de que ninguna de las 3 suceda devuelve 0.
    if (puntJugador == puntCrupier) and (puntJugador <= 21 and puntCrupier <= 21):
        return 3
    elif (puntJugador > puntCrupier) and puntJugador <= 21:
        return 2
    elif (puntCrupier > puntJugador) and puntCrupier <= 21:
        return 1
    else:
        return 0

# ╚═══════ ≪ ° </Función Verificar Puntajes Finales> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Jalar Carta> ° ≫ ═══════╗

def JalarCarta(esJugador: bool):
    """

        Agrega una carta de la baraja a la mano del jugador o del crupier.

        Actualiza las variables globales correspondientes (`jugador` o `crupier`),
        ajusta el puntaje y renderiza la barra de progreso en la interfaz.

        Parameters:

            esJugador (bool): `True` si el que pide la carta es el jugador, `False` si es el crupier.

        Raises:

            TypeError: Si el argumento `esJugador` no es un booleano.

        Examples:

            >>> JalarCarta(True)
            >>> JalarCarta(False)

    """
    # Se tratan las excepciones
    if not isinstance(esJugador, bool):
        raise TypeError("ERROR: El argumento esJugador no es un booleano.")

    # Se definen las variables globales
    global crupier, jugador, puntCrupier, puntJugador

    # Evalúa si es el jugador o el crupier el que pidió la carta.
    if esJugador:
        # Se saca una carta de la baraja y se agrega a la mano del jugador y se muestra la carta.
        carta = baraja.pop()
        jugador.append(carta)
        MostrarCarta(carta, True)

        # Si es un As, Jota, Reina o Rey se manda a llamar a la función arreglar valores y
        # se le asigna el valor devuelto por la función a la puntuación del jugador.
        if carta[0] in "AJQK":
            jugador.pop()
            jugador.append(ArreglarValores(True, carta))
        puntJugador += int(jugador[-1][0])
        textoPuntJugador.configure(text=f"{puntJugador}/21")

        # Se le cambia el color a la barra de puntuación según si es menor o igual a 21 o no.
        if puntJugador <= 21:
            bordeBarraJugador.columnconfigure(0, weight=puntJugador)
            bordeBarraJugador.columnconfigure(1, weight=(21 - puntJugador))
        else:
            bordeBarraJugador.columnconfigure(0, weight=21)
            bordeBarraJugador.columnconfigure(1, weight=0)
            barraPuntJugador.configure(bg="red")
    else:
        # Se saca una carta de la baraja y se agrega a la mano del crupier y se muestra la carta.
        carta = baraja.pop()
        crupier.append(carta)
        MostrarCarta(carta, False)

        # Si es un As, Jota, Reina o Rey se manda a llamar a la función arreglar valores y
        # se le asigna el valor devuelto por la función a la puntuación del crupier.
        if carta[0] in "AJQK":
            crupier.pop()
            crupier.append(ArreglarValores(False, carta))
        puntCrupier += int(crupier[-1][0])

        # En caso de que el jugador todavía no se haya plantado, oculta la carta y puntuación del crupier,
        # Si no, muestra el puntaje actual del crupier y le cambia el color a la barra de puntuación según si es menor o igual a 21 o no.
        if len(crupier) <= 2:
            textoPuntCrupier.configure(text=f"?/21")
            puntCrupierConocida = int(crupier[0][0])
            bordeBarraCrupier.columnconfigure(0, weight=puntCrupierConocida)
            bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupierConocida))
            barraPuntCrupier.configure(bg="yellow")
        else:
            textoPuntCrupier.configure(text=f"{puntCrupier}/21")
            if puntCrupier <= 21:
                bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
                bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
                barraPuntCrupier.configure(bg="green")
            else:
                bordeBarraCrupier.columnconfigure(0, weight=21)
                bordeBarraCrupier.columnconfigure(1, weight=0)
                barraPuntCrupier.configure(bg="red")

# ╚═══════ ≪ ° </Función Jalar Carta> ° ≫ ═══════╝

# ╔═══════ ≪ ° <Función Iniciar Juego> ° ≫ ═══════╗

def InicioJuego() -> None:
    """
        Inicializa la partida repartiendo dos cartas de manera alternada al crupier y al jugador.
        Limpia la mesa, restablece las variables globales y reparte las manos iniciales.
        Posteriormente verifica si con la mano inicial hay algún Blackjack y decide al ganador, de lo contrario sigue el juego normal.

        Globals:
        PALOS (list): Palos predefinidos de las cartas.
        DENOMINACIONES (list): Denominaciones predefinidas de las cartas.
        Baraja (list): Baraja completa de 52 combinaciones según los palos y denominaciones.
        crupier (list): Mano del crupier.
        segundaCartaCrupier (list): Segunda carta del crupier la cual esta oculta.
        puntCrupier (int): Puntuación total actual del crupier.
        jugador (list): Mano del jugador.
        puntJugador (int): Puntuación total actual del jugador.
    """
    global PALOS, DENOMINACIONES, baraja, crupier, segundaCartaCrupier, puntCrupier, jugador, puntJugador

    # Se esconde el menú, se reinicia la mesa, se acomodan los botones y se ponen disponibles para el usuario.
    menu.place_forget()
    textoMenu.grid_forget()
    botonInicio.grid_forget()
    botonSalir.grid_forget()
    botonPedir.config(state="normal")
    botonPlantar.config(state="normal")
    for dibujo in marcoManoCrupier.winfo_children():
        dibujo.destroy()
    for dibujo in marcoManoJugador.winfo_children():
        dibujo.destroy()
    barraPuntJugador.config(bg="green")

    # Se reinician las variables globales para el siguiente juego y se barajea.
    baraja = [(den, palo) for palo in PALOS for den in DENOMINACIONES]
    crupier = []
    segundaCartaCrupier = []
    puntCrupier = 0
    jugador = []
    puntJugador = 0

    shuffle(baraja)

    # Entrega 4 cartas de forma alternada, 2 para el jugador y 2 para el crupier.
    for i in range(2):
        JalarCarta(True)
        JalarCarta(False)

    # Se verifica si alguno de los dos hizo blackjack de manera natural,
    # si es asi muestra las cartas del crupier y determina el ganador finalizando el juego.
    estado = VerificarBlackjack()
    if estado != 0:
        hijos = marcoManoCrupier.winfo_children()
        hijos[1].destroy()
        MostrarCarta(segundaCartaCrupier[0], False)
        textoPuntCrupier.configure(text=f"{puntCrupier}/21")
        bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
        bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
        barraPuntCrupier.configure(bg="green")
        if estado == 1:
            MostrarFinJuego(1)
        elif estado == 2:
            MostrarFinJuego(2)
        elif estado == 3:
            MostrarFinJuego(3)

# ╚═══════ ≪ ° </Función Iniciar Juego> ° ≫ ═══════╝

# ╔═══════ ≪ ° <Función Pedir> ° ≫ ═══════╗

def Pedir():
    """
        Función ejecutada por el botón "Pedir".
        Le entrega una carta adicional al jugador y evalúa si este excedió los 21 puntos.
        De ser así, se revela la carta oculta del crupier y la partida termina en victoria para la casa.
    """
    # Llama a la función Jalar carta y se la asigna al jugador.
    JalarCarta(True)

    # Verifica si el jugador se paso del puntaje, muestra las cartas del crupier y finaliza el juego.
    if VerificarSobrepuntaje() == 2:
        hijos = marcoManoCrupier.winfo_children()
        hijos[1].destroy()
        MostrarCarta(segundaCartaCrupier[0], False)
        textoPuntCrupier.configure(text=f"{puntCrupier}/21")
        bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
        bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
        barraPuntCrupier.configure(bg="green")
        MostrarFinJuego(1)

    # Planta al jugador directamente si obtiene 21 al pedir la carta.
    if VerificarBlackjack() == 2:
        Plantarse()

# ╚═══════ ≪ ° </Función Pedir> ° ≫ ═══════╝

# ╔═══════ ≪ ° <Función Plantarse> ° ≫ ═══════╗

def Plantarse() -> None:
    """
        Función ejecutada por el botón "Plantar".
        Da por terminado el turno del jugador. Revela la carta oculta del crupier y
        hace que este pida cartas obligatoriamente hasta alcanzar al menos 17 puntos.
        Posteriormente, verifica los puntajes finales y decide al ganador.
    """

    # Deshabilita los botones de pedir y plantar.
    botonPedir.config(state="disabled")
    botonPlantar.config(state="disabled")

    # Muestra la segunda carta del crupier, y ajusta la barra de puntuos y su puntuación en el texto.
    hijos = marcoManoCrupier.winfo_children()
    hijos[1].destroy()
    MostrarCarta(segundaCartaCrupier[0], False)
    textoPuntCrupier.configure(text=f"{puntCrupier}/21")
    bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
    bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
    barraPuntCrupier.configure(bg="green")

    # Jala carta para el dealer si aún no llega a los 17 puntos mínimos para plantarse
    while puntCrupier < 17:
        JalarCarta(False)

    # Verifica si el crupier se pasó de 21, y luego evalúa si fue un empate, si ganó el jugador por mayoría de puntos sin pasarse o
    # si ganó el crupier por mayoría de puntos sin pasarse.
    if VerificarSobrepuntaje() == 1:
        MostrarFinJuego(2)
    estado = VerificarPuntajesFinales()
    if estado == 3:
        MostrarFinJuego(3)
    elif estado == 1:
        MostrarFinJuego(1)
    elif estado == 2:
        MostrarFinJuego(2)

# ╚═══════ ≪ ° </Función Plantarse> ° ≫ ═══════╝

# ╔═══════ ≪ ° </Función Mostrar Fin Juego> ° ≫ ═══════╗

def MostrarFinJuego(estado: int):
    """
        Muestra la interfaz de final de partida.

        Despliega un menú superpuesto anunciando al ganador, desactiva los botones
        de pedir y plantar, y muestra las opciones de "REINICIAR" o "SALIR".

        Parameters:

            estado (int): Representa el resultado (1 = Gana Crupier, 2 = Gana Jugador, 3 = Empate).

        Raises:

            TypeError: Si el `estado` proporcionado no es un número entero.
            ValueError: Si el `estado` no está en el rango válido (1, 2, 3).

    """
    # Evalúa las excepciones.
    if not isinstance(estado, int):
        raise TypeError("El argumento estado debe ser un número entero.")
    if not 1 <= estado <= 3:
        raise ValueError("El argumento estado debe ser un número entero de 1 a 3.")

    # Se deshabilitan los botones para la partida y se muestra el menú.
    botonPedir.config(state="disabled")
    botonPlantar.config(state="disabled")
    menu.place(width=app.winfo_width(), height=180, y=(app.winfo_height()-180))
    menu.rowconfigure((0, 1), weight=1)
    menu.columnconfigure(0, weight=1)

    # Evalúa si ganó el crupier, si hubo un empate o si ganó el jugador
    if estado == 1:
        textoEstado = "Gana CRUPIER!"
    elif estado == 2:
        textoEstado = "Gana JUGADOR!"
    else:
        textoEstado = "EMPATE!"

    # Muestra el mensaje de ganador, perdedor o empate según el resultado y muestra las opciones de volver a iniciar un juego o salir del programa.
    textoMenu.config(text=textoEstado, font=("OCR A EXTENDED", 50, "bold"), bg="#58101b")
    textoMenu.grid(column=0, row=0, sticky="n", pady=(15, 0))

    botonInicio.config(text="REINICIAR", font=("Courier New", 20, "bold"), bg="green", command=InicioJuego)
    botonSalir.config(text="SALIR", font=("Courier New", 20, "bold"), bg="red", command=exit)

    botonInicio.grid(column=0, row=1, sticky="s", pady=(0,15), padx=(0, 200))
    botonSalir.grid(column=0, row=1, sticky="s", pady=(0,15), padx=(200, 0))

# ╚═══════ ≪ ° </Función Mostrar Fin Juego> ° ≫ ═══════╝

# ! ////////////Programa Principal/////////////////

if __name__ == "__main__":

    # Ventana del programa.
    app = tk.Tk()
    app.title("BlackJack LCC")
    app.geometry("900x600")
    app.resizable(False, False)

    # Marco total del programa sobre el que todo se muestra.
    marcoPrincipal = tk.Frame(app, bg="pale green", highlightbackground="brown", highlightthickness=20)
    marcoPrincipal.pack(fill="both", expand=True)
    marcoPrincipal.rowconfigure(0, weight=4)
    marcoPrincipal.rowconfigure(1, weight=1)
    marcoPrincipal.columnconfigure(0, weight=1)

    # Marco del espacio para las manos y los puntajes.
    marcoManos = tk.Frame(marcoPrincipal, bg="pale green")
    marcoManos.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 10))
    marcoManos.rowconfigure(0, weight=1)
    marcoManos.rowconfigure(1, weight=1)
    marcoManos.columnconfigure(0, weight=1)

    # Marco del espacio para la puntuación y la mano del crupier.
    marcoCrupier = tk.Frame(marcoManos, bg="pale green")
    marcoCrupier.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
    marcoCrupier.columnconfigure(0, weight=1)
    marcoCrupier.columnconfigure(1, weight=3)
    marcoCrupier.rowconfigure(0, weight=1)

    # Marco del espacio para la puntuación del crupier.
    marcoPuntCrupier = tk.Frame(marcoCrupier, bg="snow", highlightbackground="goldenrod3", highlightthickness=5)
    marcoPuntCrupier.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)
    marcoPuntCrupier.rowconfigure((0, 1, 2), weight=1)
    marcoPuntCrupier.columnconfigure(0, weight=1)
    marcoPuntCrupier.grid_propagate(False)

    # Etiqueta de texto con el nombre de "CRUPIER"
    nombreCrupier = tk.Label(marcoPuntCrupier, text="CRUPIER", font=("Small Fonts", 20, "bold"), bg="snow")
    nombreCrupier.grid(row=0, column=0, sticky="n", pady=(15, 0))

    # Cuadro de barra de puntuación del crupier. (borde)
    bordeBarraCrupier = tk.Frame(marcoPuntCrupier, bg="white", highlightbackground="black", highlightthickness=5, width=160, height=25)
    bordeBarraCrupier.grid(row=1, column=0, sticky="n", pady=(20,0))
    bordeBarraCrupier.columnconfigure(0, weight=0)
    bordeBarraCrupier.columnconfigure(1, weight=21)
    bordeBarraCrupier.rowconfigure(0, weight=1)
    bordeBarraCrupier.grid_propagate(False)

    # Línea de la puntuación del crupier. (Línea verde, amarilla o roja)
    barraPuntCrupier = tk.Frame(bordeBarraCrupier, bg="light green")
    barraPuntCrupier.grid(row=0, column=0, sticky="nsew")

    # Línea del espacio faltante para que la puntuación del crupier llegue a 21.
    barraNoPuntCrupier = tk.Frame(bordeBarraCrupier, bg="white")
    barraNoPuntCrupier.grid(row=0, column=1, sticky="nsew")

    # Texto de la puntuación del crupier.
    textoPuntCrupier = tk.Label(marcoPuntCrupier, text="0/21", font=("Small Fonts", 20), bg="snow")
    textoPuntCrupier.grid(row=2, column=0, sticky="sw", pady=10, padx=(15, 0))

    # Marco del espacio para la mano del crupier.
    marcoManoCrupier = tk.Frame(marcoCrupier, bg="pale green")
    marcoManoCrupier.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=20)
    marcoManoCrupier.grid_propagate(False)
    marcoManoCrupier.rowconfigure(0, weight=1)
    marcoManoCrupier.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # Marco del espacio para la mano y la puntuación del jugador.
    marcoJugador = tk.Frame(marcoManos, bg="pale green")
    marcoJugador.grid(row=1, column=0, sticky="nsew", pady=(5, 0))
    marcoJugador.columnconfigure(0, weight=3)
    marcoJugador.columnconfigure(1, weight=1)
    marcoJugador.rowconfigure(0, weight=1)

    # Marco del espacio para la mano del jugador.
    marcoManoJugador = tk.Frame(marcoJugador, bg="pale green")
    marcoManoJugador.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=20)
    marcoManoJugador.grid_propagate(False)
    marcoManoJugador.rowconfigure(0, weight=1)
    marcoManoJugador.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # Marco del espacio para la puntuación del jugador.
    marcoPuntJugador = tk.Frame(marcoJugador, bg="snow", highlightbackground="goldenrod3", highlightthickness=5)
    marcoPuntJugador.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=10)
    marcoPuntJugador.rowconfigure((0, 1, 2), weight=1)
    marcoPuntJugador.columnconfigure(0, weight=1)
    marcoPuntJugador.grid_propagate(False)

    # Etiqueta de texto con el nombre de "JUGADOR"
    nombreJugador = tk.Label(marcoPuntJugador, text="JUGADOR", font=("Small Fonts", 20, "bold"), bg="snow")
    nombreJugador.grid(row=0, column=0, sticky="n", pady=(15, 0))

    # Cuadro de barra de puntuación del jugador. (borde)
    bordeBarraJugador = tk.Frame(marcoPuntJugador, bg="white", highlightbackground="black", highlightthickness=5, width=160, height=25)
    bordeBarraJugador.grid(row=1, column=0, sticky="n", pady=(20,0))
    bordeBarraJugador.columnconfigure(0, weight=0)
    bordeBarraJugador.columnconfigure(1, weight=21)
    bordeBarraJugador.rowconfigure(0, weight=1)
    bordeBarraJugador.grid_propagate(False)

    # Línea de la puntuación del jugador. (Línea verde o roja)
    barraPuntJugador = tk.Frame(bordeBarraJugador, bg="green")
    barraPuntJugador.grid(row=0, column=0, sticky="nsew")

    # Línea del espacio faltante para que la puntuación del jugador llegue a 21.
    barraNoPuntJugador = tk.Frame(bordeBarraJugador, bg="white")
    barraNoPuntJugador.grid(row=0, column=1, sticky="nsew")

    # Texto de la puntuación del jugador.
    textoPuntJugador = tk.Label(marcoPuntJugador, text="0/21", font=("Small Fonts", 20), bg="snow")
    textoPuntJugador.grid(row=2, column=0, sticky="se", pady=10, padx=(0, 15))

    # Marco del espacio para los botones "Pedir" y "Plantar"
    marcoBotones = tk.Frame(marcoPrincipal, bg="pale green")
    marcoBotones.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))
    marcoBotones.columnconfigure((0, 1), weight=1)
    marcoBotones.rowconfigure(0, weight=1)

    # Botón Pedir y Plantar
    botonPedir = tk.Button(marcoBotones, text="Pedir", width=20, font=("Courier New", 16, "bold"), command=Pedir)
    botonPlantar = tk.Button(marcoBotones, text="Plantar", width=20, font=("Courier New", 16, "bold"), command=Plantarse)
    botonPedir.configure(bg="green", bd=5, relief=tk.RAISED, state="disabled")
    botonPlantar.configure(bg="indian red", bd=5, relief=tk.RAISED, state="disabled")
    botonPedir.grid(row=0, column=0, sticky="w", padx=(80, 0))
    botonPlantar.grid(row=0, column=1, sticky="e", padx=(0, 80))

    # Marco del menú superpuesto.
    menu = tk.Frame(app, bg="#58101b", highlightbackground="gold", highlightthickness="10")
    menu.place(relwidth=app.winfo_width(), height=250, y=125)
    menu.rowconfigure((0,1), weight=1)
    menu.columnconfigure(0, weight=1)

    # Etiqueta de texto del nombre del juego ("BLACKJACK") o del resultado de la última partida.
    textoMenu = tk.Label(menu, text="BLACKJACK", font=("OCR A EXTENDED", 50, "bold"), bg="#58101b", fg="gold")
    textoMenu.grid(column=0, row=0, sticky="n", pady=(30, 0))

    # Botones de reinicio de partida y de salida del programa.
    botonInicio = tk.Button(menu, text="INICIAR", font=("Courier New", 20, "bold"), bg="green", command=InicioJuego)
    botonSalir = tk.Button(menu, text="SALIR", font=("Courier New", 20, "bold"), bg="red", command=exit)
    botonInicio.grid(column=0, row=1, sticky="s", pady=(0,30), padx=(0, 200))
    botonSalir.grid(column=0, row=1, sticky="s", pady=(0,30), padx=(200, 0))

    # Ciclo de la ventana
    app.mainloop()