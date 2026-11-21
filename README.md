# Programación 1
Este repositorio contiene los programas y ejercicios
desarrollados durante la materia de Programación 1.
Los ejercicios están organizados por temas, y cada
programa se encuentra en su propia carpeta.

## Contenido
| Programa | Función |
| --- | --- |
| `IMC_PseInt/IMCyCategorias.psc` | El programa evalúa la edad del usuario, en caso de tener la edad mínima requerida, se calculará su IMC y se le dará aconocer al usuario su índice junto a su categoría correspondiente. |
| `OpRescate_PseInt/Tarea2OperacionRescate.psc` | Programa para calcular y clasificar las posibilidades de cada estudiante de obtener promedios sobresalintes, regulares, suficientes o reprobatorios, según resultados de 3 exámenes anteriores y uno más aún sin evaluar. |
| `GenCURP_PseInt/Tarea3_GeneradorCURP.psc` | Genera los primeros 16 dígitos de la CURP de una persona a partir de sus datos ingresados. |
| `FigurasTerminal_Python/Tarea_Figuras.py` | Imprime en la terminal las figuras que elija el usuario (Reloj de arena, Rombo, Moño, Copa, y todos los anteriores) de NxN de dimensión, siendo N un número que ingresa el usuario. |
| `BlackJack_Python/BlackJack.py` | Simulación del juego BlackJack o 21, implementando una interfaz gráfica con Tkinter. (SIN APUESTAS) |
| `Funcion_ContraseñaSegura_Python/ContraSegura.py` | Función que verifica si la contraseña recibida es segura o no. |

## Requisitos

**Para los archivos .psc**
- Usar PseInt para realizar la ejecución de los programas. (O el programa que desee utilisar para ejecutar archivos .psc)

**Para los archivos .py**
- Tener instalado Python 3.

## Ejecución del programa

### Figuras en Terminal - Python
Ejecute el archivo principal y elija la figura/s
que desea ver impresas en terminal.

**Requisitos:**
- Tener instalado Python 3.

**Ubicación:** `FigurasTerminal_Python/Tarea_Figuras.py`

**Para ejecutarlo:**

```bash
python3 FigurasTerminal_Python/Tarea_Figuras.py
```

## Ejemplo de funcionamiento

Al ejecutar el programa `Tarea_Figuras.py`, se muestra una pequeña descripción del programa y un menú de opciones a elegir para la acción que se desea realizar.

**Ejemplo de entrada y salida:**

```text
Programa para imprimir las algunas figuras rellenas y huecas con cualquier carácter

Opciones a elegir:

        0) Salir del programa

        FIGURAS:
        1) Reloj de arena
        2) Rombo
        3) Moño
        4) Copa
        5) Todas
        
Ingrese el número de la opción que desea seleccionar: 5
Ingrese el carácter o símbolo a utilizar para imprimir la figura: *
Dimensión mínima: 5
Dimensión máxima: 29
Ingrese la dimensión (impar) que desea para la/las figura/as a imprimir: 5
*****      *      *   *    *****
 ***      ***     ** **     *** 
  *      *****    *****      *  
 ***      ***     ** **      *  
*****      *      *   *    *****




*****      *      *   *    *****
 * *      * *     ** **     * * 
  *      *   *    * * *      *  
 * *      * *     ** **      *  
*****      *      *   *    *****
```

![Ejecución del programa](capturas/ejecicion.png)

## Autor
#### Khristo Ricardo Rodriguez Valencia
Estudiante de la Universidad de Sonora