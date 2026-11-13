"""
# Programa: Tarea_Figuras.py

Programa que imprime ciertas figuras rellenas y huecas.

---

* **Autores:** Khristo Ricardo Rodriguez Valencia / Ángel Adrián Barragán Ruiz
* **Grupo:** 7
* **Fecha:** 04/11/2026
"""

def ImprimirReloj(simbolo:str, dimension:int) -> None:
    """
        Imprime dos figuras de reloj de arena (una rellena y una hueca) según los valores de los parámetros recibidos.
    
        Parameters:
        
            simbolo (str): Cadena de un sólo carácter con el símbolo a usar al imprimir la figura.
            dimension (int): Entero impar de las dimensiones de la impresión de la figura.
    
        Returns:
        
            None: Devuelve None, ya que imprime directamente con print la figura correspondientemente a los parámetros.
    
        Raises:
        
            ValueError: Si simbolo no tiene un solo carácter, si dimension sale del rango de 5-99, y si dimension no es impar.
            TypeError: Si simbolo no es un string(cadena), o si dimension no es un integer(entero).
    
    """
    # Verificación de validez de parámetros recibidos (solamente hecho para futura utilización fuera de este programa)
    if not isinstance(simbolo, str) or not isinstance(dimension, int):
        raise TypeError("El argumento simbolo debe ser string(cadena) y el argumento dimension debe ser integer(entero).")
    if not len(simbolo) == 1:
        raise ValueError("El argumento simbolo debe contener un solo carácter en la cadena.")
    if 5 > dimension or dimension > 99:
        raise ValueError("El argumento dimension debe ser un entero impar entre 5 y 99 (incluidos los límites).")
    if dimension % 2 == 0:
        raise ValueError("El argumento dimension debe ser un entero impar dentro del rango.")

    # RELOJ DE ARENA RELLENO
    #Impresión del triángulo superior invertido del reloj de arena 
    for i in range(dimension, 0, -2):
        print((i*simbolo).center(dimension))
    
    #Impresión del triángulo inferior del reloj de arena (omitiendo el punto final superior, ya que se imprime en el ciclo anterior)
    for i in range(3, dimension + 1, 2):
        print((i*simbolo).center(dimension))

    #Separación
    print("\n\n")

    # RELOJ DE ARENA HUECO
    #Impresión de la primera línea del reloj de arena que siempre es completa
    print(simbolo*dimension)

    #Inicialización de variables
    espacio = 1
    hueco = dimension - 4
    #Impresión desde la segunda línea hasta una antes de la mitad del reloj de arena
    for i in range(0, dimension - 3, 2):
        print(espacio*" " + simbolo + hueco*" " + simbolo + espacio*" ")
        espacio += 1
        hueco -= 2
    
    #Impresión del punto único centrado de la mitad del reloj de arena
    print(simbolo.center(dimension))

    #Inicialización de variables
    hueco = 1
    espacio = int((dimension - 3) / 2)
    #Impresión desde la línea siguiente de la mitad hasta una antes del final del reloj de arena
    for i in range(0, dimension - 3, 2):
        print(espacio*" " + simbolo + hueco*" " + simbolo + espacio*" ")
        espacio -= 1
        hueco += 2
    
    #Impresión de la última línea del reloj de arena que siempre es completa
    print(simbolo*dimension)
    return

#######################################################

def ImprimirRombo(simbolo:str, dimension:int) -> None:
    """
        Imprime dos figuras de rombo (una rellena y una hueca) según los valores de los parámetros recibidos.
    
        Parameters:
        
            simbolo (str): Cadena de un sólo carácter con el símbolo a usar al imprimir la figura.
            dimension (int): Entero impar de las dimensiones de la impresión de la figura.
    
        Returns:
        
            None: Devuelve None, ya que imprime directamente con print la figura correspondientemente a los parámetros.
    
        Raises:
        
            ValueError: Si simbolo no tiene un solo carácter, si dimension sale del rango de 5-99, y si dimension no es impar.
            TypeError: Si simbolo no es un string(cadena), o si dimension no es un integer(entero).
    
    """
    # Verificación de validez de parámetros recibidos (solamente hecho para futura utilización fuera de este programa)
    if not isinstance(simbolo, str) or not isinstance(dimension, int):
        raise TypeError("El argumento simbolo debe ser string(cadena) y el argumento dimension debe ser integer(entero).")
    if not len(simbolo) == 1:
        raise ValueError("El argumento simbolo debe contener un solo carácter en la cadena.")
    if 5 > dimension or dimension > 99:
        raise ValueError("El argumento dimension debe ser un entero impar entre 5 y 99 (incluidos los límites).")
    if dimension % 2 == 0:
        raise ValueError("El argumento dimension debe ser un entero impar dentro del rango.")

    # ROMBO RELLENO
    #Inicialización de variables
    espacio = dimension - 1
    #Impresión del rombo completo
    for i in range(1, dimension + 1):
        print(abs(int(espacio / 2))*" " + (dimension-abs(espacio))*simbolo + abs(int(espacio / 2))*" ")
        espacio -= 2

    #Separación
    print("\n\n")

    # ROMBO HUECO
    #Impresión de la primera línea del rombo que siempre es un símbolo centrado
    print(simbolo.center(dimension))

    #Inicialización de variables
    espacio = dimension - 3
    hueco = 1
    #Impresión de la segunda línea a la penúltima línea del rombo
    for i in range(1, dimension - 1):
        print(abs(int(espacio / 2))*" " + simbolo + hueco*" " + simbolo + abs(int(espacio / 2))*" ")
        espacio -= 2
        hueco = dimension - 2 - abs(espacio)
    #Impresión de la última línea del rombo que siempre es un símbolo centrado
    print(simbolo.center(dimension))
    return

#######################################################

def ImprimirMono(simbolo:str, dimension:int) -> None:
    """
        Imprime dos figuras de moño (una rellena y una hueca) según los valores de los parámetros recibidos.
    
        Parameters:
        
            simbolo (str): Cadena de un sólo carácter con el símbolo a usar al imprimir la figura.
            dimension (int): Entero impar de las dimensiones de la impresión de la figura.
    
        Returns:
        
            None: Devuelve None, ya que imprime directamente con print la figura correspondientemente a los parámetros.
    
        Raises:
        
            ValueError: Si simbolo no tiene un solo carácter, si dimension sale del rango de 5-99, y si dimension no es impar.
            TypeError: Si simbolo no es un string(cadena), o si dimension no es un integer(entero).
    
    """
    # Verificación de validez de parámetros recibidos (solamente hecho para futura utilización fuera de este programa)
    if not isinstance(simbolo, str) or not isinstance(dimension, int):
        raise TypeError("El argumento simbolo debe ser string(cadena) y el argumento dimension debe ser integer(entero).")
    if not len(simbolo) == 1:
        raise ValueError("El argumento simbolo debe contener un solo carácter en la cadena.")
    if 5 > dimension or dimension > 99:
        raise ValueError("El argumento dimension debe ser un entero impar entre 5 y 99 (incluidos los límites).")
    if dimension % 2 == 0:
        raise ValueError("El argumento dimension debe ser un entero impar dentro del rango.")

    # MOÑO RELLENO
    #Inicialización de variables
    hueco = dimension - 2
    #Impresión desde la primera línea hasta una antes de la mitad del moño
    for i in range(2, dimension, 2):
        print(int(i/2)*simbolo + hueco*" " + int(i/2)*simbolo)
        hueco -= 2

    #Impresión de la mitad del moño
    print(dimension*simbolo)

    #Inicialización de variables
    hueco = 1
    #Impresión del resto del moño, desde la siguiente después de la mitad hasta la última línea
    for i in range(dimension - 1, 0, -2):
        print(int(i/2)*simbolo + hueco*" " + int(i/2)*simbolo)
        hueco += 2

    #Separación
    print("\n\n")

    # MOÑO HUECO
    #Impresión de la primera línea del moño
    print(simbolo + (dimension - 2)*" " + simbolo)

    #Inicialización de variables
    hueco = dimension - 4
    espacio = 0
    #Impresión de la segunda línea a una antes de la mitad del moño
    for i in range(0, int((dimension - 1) / 2) - 1):
        print(simbolo + espacio*" " + simbolo + hueco*" " + simbolo + espacio*" " + simbolo)
        hueco -= 2
        espacio += 1

    #Impresión de la mitad del moño
    print(simbolo + int((dimension - 3)/2)*" " + simbolo + int((dimension - 3)/2)*" " + simbolo)

    #Inicialización de variables
    hueco = 1
    espacio = int((dimension - 5) / 2)
    #Impresión desde la línea después de la mitad a la penúltima línea del moño
    for i in range(0, int((dimension - 1) / 2) - 1):
            print(simbolo + espacio*" " + simbolo + hueco*" " + simbolo + espacio*" " + simbolo)
            hueco += 2
            espacio -= 1

    #Impresión de la última línea del moño
    print(simbolo + (dimension - 2)*" " + simbolo)

    return

#######################################################

def ImprimirCopa(simbolo:str, dimension:int) -> None:
    """
        Imprime dos figuras de copa (una rellena y una hueca) según los valores de los parámetros recibidos.
    
        Parameters:
        
            simbolo (str): Cadena de un sólo carácter con el símbolo a usar al imprimir la figura.
            dimension (int): Entero impar de las dimensiones de la impresión de la figura.
    
        Returns:
        
            None: Devuelve None, ya que imprime directamente con print la figura correspondientemente a los parámetros.
    
        Raises:
        
            ValueError: Si simbolo no tiene un solo carácter, si dimension sale del rango de 5-99, y si dimension no es impar.
            TypeError: Si simbolo no es un string(cadena), o si dimension no es un integer(entero).
    
    """
    # Verificación de validez de parámetros recibidos (solamente hecho para futura utilización fuera de este programa)
    if not isinstance(simbolo, str) or not isinstance(dimension, int):
        raise TypeError("El argumento simbolo debe ser string(cadena) y el argumento dimension debe ser integer(entero).")
    if not len(simbolo) == 1:
        raise ValueError("El argumento simbolo debe contener un solo carácter en la cadena.")
    if 5 > dimension or dimension > 99:
        raise ValueError("El argumento dimension debe ser un entero impar entre 5 y 99 (incluidos los límites).")
    if dimension % 2 == 0:
        raise ValueError("El argumento dimension debe ser un entero impar dentro del rango.")

    # COPA RELLENA
    #Impresión del triángulo invertido superior de la copa, sin imprimir la punta de un sólo símbolo
    for i in range(dimension, 2, -2):
        print((i*simbolo).center(dimension))

    #Impresión de todas las líneas de un sólo símbolo de la copa
    for i in range(0, int(dimension / 2)):
        print(simbolo.center(dimension))

    #Impresión de la última línea de la copa
    print(dimension*simbolo)

    #Separación
    print("\n\n")

    # COPA HUECA
    #Impresión de la primera línea de la copa
    print(dimension*simbolo)

    #Inicialización de variables
    espacio = 1
    hueco = dimension - 4
    #Impresión de la segunda línea de la copa hasta una antes del inicio de las líneas de un sólo símbolo
    for i in range(dimension, 4, -2):
        print(espacio*" " + simbolo + hueco*" " + simbolo + espacio*" ")
        espacio += 1
        hueco -= 2

    #Impresión de todas las líneas de un sólo símbolo de la copa
    for i in range(0, int(dimension/2)):
        print(simbolo.center(dimension))

    #Impresión de la última línea de la copa
    print(dimension*simbolo)

    return

#######################################################

def ImprimirTodasFiguras(simbolo:str, dimension:int) -> None:
    """
        Imprime dos de cada una de las siguientes figuras: reloj de arena, rombo, moño y copa (una rellena y una hueca por cada una). Según los valores de los parámetros recibidos.
    
        Parameters:
        
            simbolo (str): Cadena de un sólo carácter con el símbolo a usar al imprimir las figuras.
            dimension (int): Entero impar de las dimensiones de la impresión de las figuras.
    
        Returns:
        
            None: Devuelve None, ya que imprime directamente con print las figuras correspondientemente a los parámetros.
    
        Raises:
        
            ValueError: Si simbolo no tiene un solo carácter, si dimension sale del rango de 5-29, y si dimension no es impar.
            TypeError: Si simbolo no es un string(cadena), o si dimension no es un integer(entero).
    
    """
    # Verificación de validez de parámetros recibidos (solamente hecho para futura utilización fuera de este programa)
    if not isinstance(simbolo, str) or not isinstance(dimension, int):
        raise TypeError("El argumento simbolo debe ser string(cadena) y el argumento dimension debe ser integer(entero).")
    if not len(simbolo) == 1:
        raise ValueError("El argumento simbolo debe contener un solo carácter en la cadena.")
    if 5 > dimension or dimension > 29:
        raise ValueError("El argumento dimension debe ser un entero impar entre 5 y 99 (incluidos los límites).")
    if dimension % 2 == 0:
        raise ValueError("El argumento dimension debe ser un entero impar dentro del rango.")

    # FIGURAS RELLENAS
    #Impresión de todas las primeras líneas de las figuras
    f1 = dimension*simbolo
    f2 = simbolo.center(dimension)
    f3 = simbolo + (dimension - 2)*" " + simbolo
    f4 = dimension*simbolo
    print(f1, f2, f3, f4, sep="    ")

    #Ciclo para toda la parte media de las figuras, desde las segunda hasta la penúltima línea de las figuras
    for i in range(2, dimension):

        #Creación de las líneas de las figuras desde la segunda hasta una antes de la mitad
        if 1 < i <= int(dimension / 2):
            espacio = i - 1
            f1 = espacio*" " + (dimension - espacio * 2)*simbolo + espacio*" "
            f2 = ((i * 2 - 1)*simbolo).center(dimension)
            f3 = i*simbolo + (dimension - 2 * i)*" " + i*simbolo
            f4 = f1

        #Creación de la línea media de las figuras e inicialización de variables para la siguiente etapa
        if i == int(dimension / 2) + 1:
            f1 = simbolo.center(dimension)
            f2 = dimension*simbolo
            f3 = dimension*simbolo
            f4 = simbolo.center(dimension)
            j = 2
            cantf3 = int(dimension / 2)

        #Creación de las líneas de las figuras desde la siguiente después de la mitad hasta la penúltima línea
        if int(dimension / 2) + 1 < i < dimension:
            f1 = ((j * 2 - 1)*simbolo).center(dimension)
            espacio = j - 1
            f2 = espacio*" " + (dimension - espacio * 2)*simbolo + espacio*" "
            f3 = (cantf3*simbolo + (dimension - cantf3 * 2)*" " + cantf3*simbolo)
            cantf3 -= 1
            f4 = simbolo.center(dimension)
            j += 1

        #Impresión de las líneas correspondientes creadas
        print(f1, f2, f3, f4, sep="    ")

    #Impresión de la última línea de todas las figuras
    f1 = dimension*simbolo
    f2 = simbolo.center(dimension)
    f3 = simbolo + (dimension - 2)*" " + simbolo
    f4 = dimension*simbolo
    print(f1, f2, f3, f4, sep="    ")

    #Separación
    print("\n\n\n")

    # FIGURAS HUECAS
    #Impresión de todas las primeras líneas de las figuras
    f1 = dimension*simbolo
    f2 = simbolo.center(dimension)
    f3 = simbolo + (dimension - 2)*" " + simbolo
    f4 = dimension*simbolo
    print(f1, f2, f3, f4, sep="    ")

    #Inicialización de variables
    huecof2 = 1
    #Ciclo para toda la parte media de las figuras, desde las segunda hasta la penúltima línea de las figuras
    for i in range(2, dimension):

        #Creación de las líneas de las figuras desde la segunda hasta una antes de la mitad
        if 1 < i <= int(dimension / 2):
            f1 = (i - 1)*" " + simbolo + (dimension - (i - 1) * 2 -2)*" " + simbolo + (i - 1)*" "
            f2 = int((dimension - 2 - huecof2) / 2)*" " + simbolo + huecof2*" " + simbolo + int((dimension - 2 - huecof2) / 2)*" "
            f3 = simbolo + (i - 2)*" " + simbolo + (dimension - 4 - (i - 2) * 2)*" " + simbolo + (i - 2)* " " + simbolo
            f4 = f1
            huecof2 += 2

        #Creación de la línea media de las figuras e inicialización de variables para la siguiente etapa
        if i == int(dimension / 2) + 1:
            f1 = simbolo.center(dimension)
            f2 = simbolo + (dimension - 2)*" " + simbolo
            f3 = simbolo + int((dimension - 3) / 2)*" " + simbolo + int((dimension - 3) / 2)*" " + simbolo
            f4 = simbolo.center(dimension)
            j = 1
            espacio = 1

        #Creación de las líneas de las figuras desde la siguiente después de la mitad hasta la penúltima línea
        if int(dimension / 2) + 1 < i < dimension:
            f1 = (simbolo + j*" " + simbolo).center(dimension)
            f2 = espacio*" " + simbolo + (dimension - 2 - espacio * 2)*" " + simbolo + espacio*" "
            f3 = simbolo + int((dimension - 4 - j) / 2)*" " + simbolo + j*" " + simbolo + int((dimension - 4 - j) / 2)*" " + simbolo
            f4 = simbolo.center(dimension)
            j += 2
            espacio += 1

        #Impresión de las líneas correspondientes creadas
        print(f1, f2, f3, f4, sep="    ")

    #Impresión de la última línea de todas las figuras
    f1 = dimension*simbolo
    f2 = simbolo.center(dimension)
    f3 = simbolo + (dimension - 2)*" " + simbolo
    f4 = dimension*simbolo
    print(f1, f2, f3, f4, sep="    ")
    
    return

#######################################################
################# PROGRAMA PRINCIPAL ##################
#######################################################

if __name__ == "__main__":
    #Ciclo de ejecución del programa
    while True:
        #Encabezado
        print("Programa para imprimir las algunas figuras rellenas y huecas con cualquier carácter")

        #Impresión del menú
        print("\nOpciones a elegir:")
        print("""
        0) Salir del programa

        FIGURAS:
        1) Reloj de arena
        2) Rombo
        3) Moño
        4) Copa
        5) Todas
        """)

        #Ciclo de verificación de la opción elegida por el usuario y procesamiento de excepciones
        while True:
            try:
                opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
                if  0 <= opcion <= 5:
                    break
                else:
                    raise ValueError 
            except TypeError:
                print("ERROR: Por favor, ingrese uno de los números de las opciones para continuar.")
                continue
            except ValueError:
                print("ERROR: Por favor, ingrese uno de los números de las opciones para continuar.")
                continue
            except Exception as error:
                print(f"ERROR: {error}")
                continue

        #Validación de que no eligió cerrar el programa
        if opcion != 0:

            #Ciclo para la lectura del símbolo para la impresión de las figuras, así como el procesamiento de las excepciones
            while True:
                try:
                    simbolo = input("Ingrese el carácter o símbolo a utilizar para imprimir la figura: ")
                    if len(simbolo) != 1:
                        raise ValueError
                    break
                except ValueError:
                    print("ERROR: Por favor, ingrese un sólo símbolo o carácter para continuar.")
                    continue
                except Exception as error:
                    print(f"ERROR: {error}")
                    continue

            #Ciclo para la lectura de la dimensión para la impresión de las figuras, así como el procesamiento de las excepciones
            while True:
                try:
                    print("Dimensión mínima: 5")
                    if opcion == 5: 
                        print("Dimensión máxima: 29")
                    else:
                        print("Dimensión máxima: 99")
                    dimension = int(input("Ingrese la dimensión (impar) que desea para la/las figura/as a imprimir: "))
                    if (opcion != 5 and 4 < dimension < 100) or (opcion == 5 and 4 < dimension < 30): 
                        if dimension % 2 == 0:
                            raise ValueError 
                        break
                    else:
                        print("Por favor, ingrese un valor dentro del rango de la dimensión máxima.")
                except TypeError:
                    print("ERROR: Por favor, ingrese un número entero impar para continuar.")
                    continue
                except ValueError:
                    print("ERROR: Por favor, ingrese un número entero impar para continuar.")
                    continue
                except Exception as error:
                    print(f"ERROR: {error}")
                    continue

        #Escenarios de las opciones elegidas y su proceso correspondiente a realizar
        match opcion:
            case 0:
                print("Gracias por usar el programa.")
                break
            case 1: 
                ImprimirReloj(simbolo, dimension)
            case 2: 
                ImprimirRombo(simbolo, dimension)
            case 3: 
                ImprimirMono(simbolo, dimension)
            case 4: 
                ImprimirCopa(simbolo, dimension)
            case 5: 
                ImprimirTodasFiguras(simbolo, dimension)#