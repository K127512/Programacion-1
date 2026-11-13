"""
Nombre del archivo: ContraSegura.py
Descripción del algoritmo: Función que verifica si la contraseña recibida es segura o no.
Autor: Khristo Ricardo Rodriguez Valencia
Fecha: 29/10/2026
"""
def EsSegura(contrasena: str) -> bool:
    """
        Devuelve True si la cadena recibida es segura, False si no lo es.
    
        Parameters:
        
            contrasena (str): Cadena que se desea saber si es una contraseña segura o no.
    
        Returns:
        
            bool: True si la cadena es una contraseña segura, False si no es una contraseña segura.
    
        Raises:
        
            TypeError: Si contrasena no es un string(cadena).
    
        Examples:
        
            >>> EsSegura("Hola8/")
            True
            >>> EsSegura("Hola8")
            False
            >>> EsSegura(2)
            Traceback (most recent call last):
            ...
            TypeError: El argumento contrasena debe ser un string(cadena).
    """
    if not isinstance(contrasena, str):
        raise TypeError("El argumento contra debe ser un string(cadena).")

    if len(contrasena) < 5:
        return False

    hayMinuscula = hayMayuscula = hayNumero = haySimbolo = False 
    letrasMin = "abcdefghijklmnñopqrstuvwxyzáéíóúü"
    letrasMay = letrasMin.upper()
    numeros = "0123456789"
    simbolos = "|'\"¿´+{-.,<>;:_[¨*]}¡?=)(/&%$#!°¬\\~@`^ "

    for i in range(0, len(contrasena)):
        caracter = contrasena[i]
        if not hayMinuscula and caracter in letrasMin and caracter == caracter.lower():
            hayMinuscula = True
        if not hayMayuscula and caracter in letrasMay and caracter == caracter.upper():
            hayMayuscula = True
        if not hayNumero and caracter in numeros:
            hayNumero = True
        if not haySimbolo and caracter in simbolos:
            haySimbolo = True
        if hayMinuscula and hayMayuscula and hayNumero and haySimbolo:
            return True

    return False