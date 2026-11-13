// Nombre del archivo: Tarea3_GeneradorCURP.psc
// Descripción: Algoritmo generador de la CURP (Clave Única de Registro de Población) en sus primeros 16 caracteres
// Autor: Ángel Adrián Barragán Ruiz y Khristo Ricardo Rodriguez Valencia
// Grupo: 7
// Fecha: 11/10/2026

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Nombre de la función: SacarPrimeraConsInterna
//Explicación de la función: Checa cada caracter de la palabra que ingresa para saber si no es vocal o algunos de ciertos símbolos (/, -, .) y devuelve la consonante o vuelve vacía.
//PARÁMETROS
//palabra: Espera recibir una cadena, puede ser cualquier palabra.
//DEVUELTO
//consonante: Devuelve la primera letra consonante que encuentre en el parámetro. En caso de que no encuentre una consonante en la palabra, entonces se devuelve como una cadena vacía.
Funcion consonante <- SacarPrimeraConsInterna(palabra)
	
	//Definición de variables
	Definir consonante Como Caracter
	Definir contadorCaracter, longitudPalabra Como Entero
	Definir esCons Como Logico
	
	//Inicialización de variables
	contadorCaracter <- 2
	longitudPalabra <- Longitud(palabra)
	esCons <- Falso
	
	//Ciclo, no para hasta que termina la palabra o hasta llegar a una consonante
	Mientras !esCons y contadorCaracter <= longitudPalabra Hacer
		
		//Inicialización de variables
		consonante <- Subcadena(palabra, contadorCaracter, contadorCaracter)
		esCons <- Verdadero
		
		//Verificación de la letra actual agarrada para saber si es vocal o alguno de los símbolos posibles, si lo es entonces no es consonante 
		Segun consonante Hacer
			"A": esCons <- Falso
			"E": esCons <- Falso
			"I": esCons <- Falso
			"O": esCons <- Falso
			"U": esCons <- Falso
			"/": esCons <- Falso
			"-": esCons <- Falso
			".": esCons <- Falso
		FinSegun
		
		//Aumento del contador
		contadorCaracter <- contadorCaracter + 1
		
		
	FinMientras
	
	//En caso de salir del ciclo sin encontrar consonante, entonces se devuelve el resultado como vacío
	Si !esCons Entonces
		consonante <- ""
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: SacarPrimeraVocal
//Explicación de la función: Checa cada caracter de la palabra que ingresa para buscar la primera vocal, ignorando ciertos símbolos (/, -, .) y devuelve la vocal o vuelve vacía.
//PARÁMETROS
//palabra: Espera recibir una cadena, puede ser cualquier palabra.
//DEVUELTO
//vocal: Devuelve la primera letra vocal que encuentre en el parámetro. En caso de que no encuentre una vocal en la palabra, entonces se devuelve como una cadena vacía.
Funcion vocal <- SacarPrimeraVocal(palabra)
	
	//Definición de variables
	Definir vocal Como Caracter
	Definir contadorCaracter, longitudPalabra Como Entero
	Definir esVocal Como Logico
	
	//Inicialización de variables
	contadorCaracter <- 2
	longitudPalabra <- Longitud(palabra)
	esVocal <- Falso
	
	//Ciclo, no para hasta que termina la palabra o hasta llegar a una vocal
	Mientras !esVocal y contadorCaracter <= longitudPalabra Hacer
		
		//Inicialización de variables
		vocal <- Subcadena(palabra, contadorCaracter, contadorCaracter)
		
		//Verificación de la letra actual agarrada para saber si es vocal o alguno de los símbolos posibles
		Segun vocal Hacer
			"A": esVocal <- Verdadero
			"E": esVocal <- Verdadero
			"I": esVocal <- Verdadero
			"O": esVocal <- Verdadero
			"U": esVocal <- Verdadero
			"/": esVocal <- Verdadero
			"-": esVocal <- Verdadero
			".": esVocal <- Verdadero
		FinSegun
		
		//Aumento del contador
		contadorCaracter <- contadorCaracter + 1
		
		
	FinMientras
	
	//En caso de salir del ciclo sin encontrar vocal, entonces se devuelve el resultado como vacío
	Si !esVocal Entonces
		vocal <- ""
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: ChecarProposicionesNA
//Explicación de la función: Checa si la palabra ingresada es una preposición, contracción o conjunción que debe omitirse.
//PARÁMETROS
//nombreApellido: Espera recibir una cadena, que es una parte del nombre o apellido.
//DEVUELTO
//noEsProposicion: Devuelve Verdadero si la palabra no es preposición, y Falso si sí lo es.
Funcion noEsProposicion <- ChecarProposicionesNA(nombreApellido)
	
	//Definición de variables
	Definir noEsProposicion Como Logico
	
	//Verificación de la longitud de la palabra
	Si Longitud(nombreApellido) > 3 Entonces
		noesProposicion <- Verdadero
	SiNo
		//Verificación de la palabra agarrada para saber si es alguna de las preposiciones posibles
		Segun nombreApellido Hacer
			"DA": noesProposicion <- Falso
			"DAS": noesProposicion <- Falso
			"DE": noesProposicion <- Falso
			"DEL": noesProposicion <- Falso
			"DER": noesProposicion <- Falso
			"DI": noesProposicion <- Falso
			"DIE": noesProposicion <- Falso
			"DD": noesProposicion <- Falso
			"EL": noesProposicion <- Falso
			"LA": noesProposicion <- Falso
			"LOS": noesProposicion <- Falso
			"LAS": noesProposicion <- Falso
			"LE": noesProposicion <- Falso
			"LES": noesProposicion <- Falso
			"MAC": noesProposicion <- Falso
			"MC": noesProposicion <- Falso
			"VAN": noesProposicion <- Falso
			"VON": noesProposicion <- Falso
			"Y": noesProposicion <- Falso
			De Otro Modo: noesProposicion <- Verdadero
		FinSegun
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: ArreglarAcentosNA
//Explicación de la función: Checa cada caracter de la palabra para cambiar las vocales acentuadas y diéresis por su letra normal.
//PARÁMETROS
//nombreApellido (Por Referencia): Espera recibir una cadena, que se modificará directamente.
Funcion ArreglarAcentosNA(nombreApellido Por Referencia)
	
	//Definición de variables
	Definir contadorCaracter, longitudNombreApellido Como Entero
	Definir caracterActual, caracterNuevo Como Caracter
	
	//Inicialización de variables
	contadorCaracter <- 1
	longitudNombreApellido <- Longitud(nombreApellido)
	
	//Ciclo, no para hasta checar todos los caracteres de la palabra
	Mientras contadorCaracter <= longitudNombreApellido Hacer
		
		//Inicialización de variables
		caracterActual <- Subcadena(nombreApellido, contadorCaracter, contadorCaracter)
		caracterNuevo <- ""
		
		//Verificación de la letra actual agarrada para saber si tiene acento o diéresis
		Segun caracterActual Hacer
			"Á": 
				caracterNuevo <- "A"
			"É": 
				caracterNuevo <- "E"
			"Í": 
				caracterNuevo <- "I"
			"Ó": 
				caracterNuevo <- "O"
			"Ú": 
				caracterNuevo <- "U"
			"Ü": 
				caracterNuevo <- "U"
		FinSegun
		
		//Concatenación de la palabra con la nueva letra reemplazada
		Si caracterNuevo <> "" Entonces
			nombreApellido <- Concatenar(Subcadena(nombreApellido, 1, contadorCaracter - 1), Concatenar(caracterNuevo, Subcadena(nombreApellido, contadorCaracter + 1, longitudNombreApellido)))
		FinSi
		
		//Aumento del contador
		contadorCaracter <- contadorCaracter + 1
		
		
	FinMientras
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: ArreglarFormatoNA
//Explicación de la función: Convierte a mayúsculas, quita acentos y filtra los nombres y apellidos omitiendo preposiciones y nombres comunes.
//PARÁMETROS
//nombres: Espera recibir una cadena con los nombres.
//primerNombre (Por Referencia): Devuelve una uníca palabra de los nombres recibidos antes según las excepciones, y con buen formato (sin acentos ni diéresis y todo mayúsculas ).
//primerApellido (Por Referencia): Recibe lo ingresado por el usuario y termina devolviendo la primera palabra válida del primer apellido con buen formato (sin acentos ni diéresis, todo mayúsculas y únicamente la palabra del apellido que sea válida).
//segundoApellido (Por Referencia): Recibe lo ingresado por el usuario y termina devolviendo la primera palabra válida del segundo apellido con buen formato (sin acentos ni diéresis, todo mayúsculas y únicamente la palabra del apellido que sea válida).
Funcion ArreglarFormatoNA(nombres, primerNombre Por Referencia, primerApellido Por Referencia, segundoApellido Por Referencia)
	
	//Conversión de variables a mayúsculas
	nombres <- Mayusculas(nombres)
	primerApellido <- Mayusculas(primerApellido)
	segundoApellido <- Mayusculas(segundoApellido)
	
	//Llamado a función para quitar acentos
	ArreglarAcentosNA(nombres)
	ArreglarAcentosNA(primerApellido)
	ArreglarAcentosNA(segundoApellido)
	
	//Definición de variables
	Definir i, longitudNombres, contadorNombres, contadorNombresComunes Como Entero
	Definir caracterAux, auxNombre Como Caracter
	Definir esNombreComun, noEsProposicion, guardadoHecho Como Logico
	
	//Inicialización de variables
	contadorNombres <- 0
	contadorNombresComunes <- 0
	guardadoHecho <- Falso
	longitudNombres <- Longitud(nombres)
	i <- 1
	
	//Ciclo, no para hasta llegar al final de la primera palabra válida
	Repetir
		
		//Inicialización de variables
		primerNombre <- ""
		caracterAux <- Subcadena(nombres, i, i) 
		
		//Ciclo, no para hasta llegar al final de una palabra
		Mientras i <= longitudNombres y caracterAux <> " " Hacer
			primerNombre <- Concatenar(primerNombre, caracterAux)
			i <- i + 1
			caracterAux <- Subcadena(nombres, i, i)
		FinMientras
		
		//Aumento de contadores y llamado a función
		contadorNombres <- contadorNombres + 1
		i <- i + 1
		noEsProposicion <- ChecarProposicionesNA(primerNombre)
		
		//Verificación del nombre actual agarrado para saber si es un nombre común
		Segun primerNombre Hacer
			"MARIA": esNombreComun <- Verdadero;
			"MA.": esNombreComun <- Verdadero; 
			"MA": esNombreComun <- Verdadero; 
			"JOSE": esNombreComun <- Verdadero; 
			"J.": esNombreComun <- Verdadero; 
			"J": esNombreComun <- Verdadero; 
			De Otro Modo: esNombreComun <- Falso
		FinSegun
		
		//Respaldo del primer nombre válido
		Si noEsProposicion y contadorNombres == 2 y esNombreComun Entonces
			auxNombre <- primerNombre
			guardadoHecho <- Verdadero
		FinSi
		
		//Verificación de fin de cadena
		Si i >= longitudNombres Entonces
			
			//Asignación del nombre común respaldado
			Si !noEsProposicion y esNombreComun Entonces
				primerNombre <- auxNombre
				esNombreComun <- Falso
				noEsProposicion <- Verdadero
			FinSi
			
		FinSi
		
	Hasta Que noEsProposicion y !esNombreComun o i >= longitudNombres 
	
	//Definición de variables
	Definir auxApellido Como Caracter
	Definir longitudPrimerApellido, longitudSegundoApellido Como Entero
	Definir esEspacio Como Logico
	
	//Inicialización de variables
	auxApellido <- ""
	i <- 1
	longitudPrimerApellido <- Longitud(primerApellido)
	esEspacio <- Falso
	noEsProposicion <- Verdadero
	
	//Ciclo, no para hasta llegar al final de la primera palabra válida del apellido
	Mientras noEsProposicion y !esEspacio y i - 1 <= longitudPrimerApellido Hacer
		
		//Inicialización de variables
		caracterAux <- Subcadena(primerApellido, i, i)
		
		//Verificación de espacio o letra
		Si caracterAux == " " Entonces
			esEspacio <- Verdadero
			noEsProposicion <- ChecarProposicionesNA(auxApellido)
		SiNo
			auxApellido <- Concatenar(auxApellido, caracterAux)
			i <- i + 1
		FinSi
		
		//Reinicio de variables si es preposición
		Si !noEsProposicion Entonces
			auxApellido <- ""
			esEspacio <- Falso
			noEsProposicion <- Verdadero
			i <- i + 1
		FinSi
		
	FinMientras
	
	//Asignación de variable
	primerApellido <- auxApellido
	
	//Verificación de si existe segundo apellido
	Si segundoApellido <> "" Entonces
		
		//Inicialización de variables
		auxApellido <- ""
		i <- 1
		longitudSegundoApellido <- Longitud(segundoApellido)
		esEspacio <- Falso
		noEsProposicion <- Verdadero
		
		//Ciclo, no para hasta llegar al final de la primera palabra válida del segundo apellido
		Mientras noEsProposicion y !esEspacio y i - 1 <= longitudSegundoApellido Hacer
			
			//Inicialización de variables
			caracterAux <- Subcadena(segundoApellido, i, i)
			
			//Verificación de espacio o letra
			Si caracterAux == " " Entonces
				esEspacio <- Verdadero
				noEsProposicion <- ChecarProposicionesNA(auxApellido)
			SiNo
				auxApellido <- Concatenar(auxApellido, caracterAux)
				i <- i + 1
			FinSi
			
			//Reinicio de variables si es preposición
			Si !noEsProposicion Entonces
				auxApellido <- ""
				esEspacio <- Falso
				noEsProposicion <- Verdadero
				i <- i + 1
			FinSi
			
		FinMientras
		
		//Asignación de variable
		segundoApellido <- auxApellido
		
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: ArreglarFormatoFecha
//Explicación de la función: Checa y arregla el formato de la fecha de nacimiento y valida si la fecha es posible.
//PARÁMETROS
//fechaNacimiento: Espera recibir una cadena con la fecha de nacimiento.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//fechaBuenFormato: Devuelve una cadena de la fecha acomodada sin separadores. (DDMMAAAA)
Funcion fechaBuenFormato <- ArreglarFormatoFecha(fechaNacimiento, exitoFunciones Por Referencia)
	
	//Verificación de cadena vacía
	Si fechaNacimiento <> "" Entonces
		
		//Definición de variables
		Definir posicionDatoFecha Como Entero
		Definir caracterActual, datoFecha, fechaBuenFormato Como Caracter
		Definir longitudFecha, contador Como Entero
		
		//Inicialización de variables
		fechaBuenFormato <- ""
		longitudFecha <- Longitud(fechaNacimiento)
		datoFecha <- ""
		posicionDatoFecha <- 1
		
		//Ciclo, no para hasta checar todos los caracteres de la fecha
		Para contador <- 1 Hasta longitudFecha Con Paso 1 Hacer
			
			//Inicialización de variables
			caracterActual <- Subcadena(fechaNacimiento, contador, contador)
			
			//Verificación de separadores o final de la palabra
			Si caracterActual <> "/" y caracterActual <> "-" y contador <> longitudFecha Entonces
				datoFecha <- Concatenar(datoFecha, caracterActual)
			SiNo
				
				//Verificación del bloque de día
				Si posicionDatoFecha == 1 Entonces
					//Verificación de un solo dígito
					Si Longitud(datoFecha) == 1 Entonces
						datoFecha <- Concatenar("0", datoFecha)
					FinSi
					//Verificación básica del límite de día
					Si Longitud(datoFecha) == 2 Entonces
						fechaBuenFormato <- datoFecha
						Si ConvertirANumero(fechaBuenFormato) > 31 Entonces
							exitoFunciones <- Falso
						FinSi
					SiNo
						exitoFunciones <- Falso
					FinSi
					
				FinSi
				
				//Verificación del bloque de mes
				Si posicionDatoFecha == 2 Entonces
					
					//Verificación de un solo dígito
					Si Longitud(datoFecha) == 1 Entonces
						datoFecha <- Concatenar("0", datoFecha)
					FinSi
					
					//Verificación del límite de mes
					Si Longitud(datoFecha) == 2 Entonces
						fechaBuenFormato <- Concatenar(fechaBuenFormato, datoFecha)
						Si ConvertirANumero(Subcadena(fechaBuenFormato, 3, 4)) > 12 Entonces
							exitoFunciones <- Falso
						FinSi
					SiNo
						exitoFunciones <- Falso
					FinSi
				FinSi
				
				//Verificación del último bloque para terminar agregando el último dígito de la fecha
				Si contador == longitudFecha Entonces
					datoFecha <- Concatenar(datoFecha, caracterActual)
				FinSi
				
				//Verificación del bloque de año
				Si posicionDatoFecha == 3 Entonces
					Si Longitud(datoFecha) == 4 Entonces
						fechaBuenFormato <- Concatenar(fechaBuenFormato, datoFecha)
					SiNo
						exitoFunciones <- Falso
					FinSi
				FinSi
				
				//Verificación de la cantidad de bloques
				Si posicionDatoFecha > 3 Entonces
					exitoFunciones <- Falso
				FinSi
				
				//Reinicio de variables y aumento de contador
				datoFecha <- ""
				posicionDatoFecha <- posicionDatoFecha + 1
				
			FinSi
			
		FinPara
		
		//Definición de variables
		Definir mes, dia Como Entero
		
		//Guardado del mes y del día en variable entera
		mes <- ConvertirANumero(Subcadena(fechaBuenFormato, 3, 4))
		dia <- ConvertirANumero(Subcadena(fechaBuenFormato, 1, 2))
		
		//Verificación de mes de febrero
		Si mes == 2 Entonces
			
			//Definición de variables
			Definir anio Como Entero
			
			//Guardado del año en variable entera
			anio <- ConvertirANumero(Subcadena(fechaBuenFormato, 5, 8))
			
			//Verificación de año bisiesto
			Si anio % 400 == 0 o anio % 4 == 0 y anio % 100 <> 0 Entonces
				//Verificación de límite de día en bisiesto
				Si dia > 29 Entonces
					exitoFunciones <- Falso
				FinSi
				
			SiNo
				//Verificación de límite de día sin bisiesto
				Si dia > 28 Entonces
					exitoFunciones <- Falso
				FinSi
			FinSi
			
		FinSi
		
		//Verificación de meses con 30 días
		Si mes == 4 o mes == 6 o mes == 9 o mes == 11 Entonces
			Si dia > 30 Entonces
				exitoFunciones <- Falso
			FinSi
		FinSi
		
	SiNo
		exitoFunciones <- Falso
	FinSi
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: GenerarCaracteres1a4
//Explicación de la función: Genera los primeros 4 caracteres de la CURP en base a los nombres y apellidos y checa si se forma una palabra altisonante.
//PARÁMETROS
//primerNombre: Espera recibir una cadena, la primera palabra del nombre.
//primerApellido: Espera recibir una cadena, la primera palabra del apellido.
//segundoApellido: Espera recibir una cadena, la primera palabra del segundo apellido.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP1a4: Devuelve una cadena con los primeros 4 caracteres de la CURP.
Funcion CURP1a4 <- GenerarCaracteres1a4(primerNombre, primerApellido, segundoApellido , exitoFunciones Por Referencia)
	
	//Definición de variables
	Definir CURP1a4 Como Caracter
	Definir Caracter_1, Caracter_2, Caracter_3, Caracter_4 Como Caracter
	
	//Asignación de la primera letra del primer apellido, y asignación como X en caso de excepción
	Caracter_1 <- Subcadena(primerApellido, 1, 1)
	Si Caracter_1 == "Ñ" o Caracter_1 == "/" o Caracter_1 == "-" o Caracter_1 == "." Entonces
		Caracter_1 <- "X"
	FinSi
	
	//Asignación de la primera vocal interna del primer apellido, y asignación como X en caso de excepción
	Caracter_2 <- SacarPrimeraVocal(primerApellido)
	Si Caracter_2 == "" o Caracter_2 == "Ñ" o Caracter_2 == "/" o Caracter_2 == "-" o Caracter_2 == "." Entonces
		Caracter_2 <- "X"
	FinSi
	
	
	//Asignación de la primera letra del segundo apellido, y asignación como X en caso de excepción
	Si segundoApellido <> "" Entonces
		Caracter_3 <- Subcadena(segundoApellido, 1, 1)
		Si Caracter_3 == "Ñ" o Caracter_3 == "/" o Caracter_3 == "-" o Caracter_3 == "." Entonces
			Caracter_3 <- "X"
		FinSi
	SiNo
		Caracter_3 <- "X"
	FinSi
	
	//Asignación de la primera letra del primer nombre, y asignación como X en caso de excepción
	Caracter_4 <- Subcadena(primerNombre, 1, 1)
	Si Caracter_4 == "Ñ" o Caracter_4 == "/" o Caracter_4 == "-" o Caracter_4 == "." Entonces
		Caracter_4 <- "X"
	FinSi
	
	//Concatenación de los 4 caracteres
	CURP1a4 <- Concatenar(Caracter_1, Concatenar(Caracter_2, Concatenar(Caracter_3, Caracter_4)))
	
	//Filtro para optiimización del código, reduce un porcentaje considerable de entradas a la verificación dentro de este filtro
	SI Caracter_1 == "B" o Caracter_1 == "C" o CURP1a4 == "FALO" o CURP1a4 == "FETO" o Caracter_1 == "G" o CURP1a4 == "JETA" o CURP1a4 == "JOTO" o Caracter_1 == "K" o Caracter_1 == "L" o Caracter_1 == "M" o CURP1a4 == "NACA" o CURP1a4 == "NACO" o Caracter_1 == "P" o CURP1a4 == "QULO"  o Caracter_1 == "R" o CURP1a4 == "SENO" o CURP1a4 == "TETA"  o Caracter_1 == "V" o CURP1a4 == "WUEY" o CURP1a4 == "WUEI" Entonces
		//Reemplazo de la segunda letra si es palabra altisonante
		Segun CURP1a4 Hacer
			"BACA": Caracter_2 <- "X"
			"BAKA": Caracter_2 <- "X"
			"BUEI": Caracter_2 <- "X"
			"BUEY": Caracter_2 <- "X"
			"CACA": Caracter_2 <- "X"
			"CACO": Caracter_2 <- "X"
			"CAGA": Caracter_2 <- "X"
			"CAGO": Caracter_2 <- "X"
			"CAKA": Caracter_2 <- "X"
			"CAKO": Caracter_2 <- "X"
			"COGE": Caracter_2 <- "X"
			"COGI": Caracter_2 <- "X"
			"COJA": Caracter_2 <- "X"
			"COJE": Caracter_2 <- "X"
			"COJI": Caracter_2 <- "X"
			"COJO": Caracter_2 <- "X"
			"COLA": Caracter_2 <- "X"
			"CULO": Caracter_2 <- "X"
			"FALO": Caracter_2 <- "X"
			"FETO": Caracter_2 <- "X"
			"GETA": Caracter_2 <- "X"
			"GUEI": Caracter_2 <- "X"
			"GUEY": Caracter_2 <- "X"
			"JETA": Caracter_2 <- "X"
			"JOTO": Caracter_2 <- "X"
			"KACA": Caracter_2 <- "X"
			"KACO": Caracter_2 <- "X"
			"KAGA": Caracter_2 <- "X"
			"KAGO": Caracter_2 <- "X"
			"KAKA": Caracter_2 <- "X"
			"KAKO": Caracter_2 <- "X"
			"KOGE": Caracter_2 <- "X"
			"KOGI": Caracter_2 <- "X"
			"KOJA": Caracter_2 <- "X"
			"KOJE": Caracter_2 <- "X"
			"KOJI": Caracter_2 <- "X"
			"KOJO": Caracter_2 <- "X"
			"KOLA": Caracter_2 <- "X"
			"KULO": Caracter_2 <- "X"
			"LILO": Caracter_2 <- "X"
			"LOCA": Caracter_2 <- "X"
			"LOCO": Caracter_2 <- "X"
			"LOKA": Caracter_2 <- "X"
			"LOKO": Caracter_2 <- "X"
			"MAME": Caracter_2 <- "X"
			"MAMO": Caracter_2 <- "X"
			"MEAR": Caracter_2 <- "X"
			"MEAS": Caracter_2 <- "X"
			"MEON": Caracter_2 <- "X"
			"MIAR": Caracter_2 <- "X"
			"MION": Caracter_2 <- "X"
			"MOCO": Caracter_2 <- "X"
			"MOKO": Caracter_2 <- "X"
			"MULA": Caracter_2 <- "X"
			"MULO": Caracter_2 <- "X"
			"NACA": Caracter_2 <- "X"
			"NACO": Caracter_2 <- "X"
			"PEDA": Caracter_2 <- "X"
			"PEDO": Caracter_2 <- "X"
			"PENE": Caracter_2 <- "X"
			"PIPI": Caracter_2 <- "X"
			"PITO": Caracter_2 <- "X"
			"POPO": Caracter_2 <- "X"
			"PUTA": Caracter_2 <- "X"
			"PUTO": Caracter_2 <- "X"
			"QULO": Caracter_2 <- "X"
			"RATA": Caracter_2 <- "X"
			"ROBA": Caracter_2 <- "X"
			"ROBE": Caracter_2 <- "X"
			"ROBO": Caracter_2 <- "X"
			"RUIN": Caracter_2 <- "X"
			"SENO": Caracter_2 <- "X"
			"TETA": Caracter_2 <- "X"
			"VACA": Caracter_2 <- "X"
			"VAGA": Caracter_2 <- "X"
			"VAGO": Caracter_2 <- "X"
			"VAKA": Caracter_2 <- "X"
			"VUEI": Caracter_2 <- "X"
			"VUEY": Caracter_2 <- "X"
			"WUEI": Caracter_2 <- "X"
			"WUEY": Caracter_2 <- "X"
		FinSegun
	FinSi
	
	//Concatenación de los 4 caracteres, después de checar por palabras altisonantes
	CURP1a4 <- Concatenar(Caracter_1, Concatenar(Caracter_2, Concatenar(Caracter_3, Caracter_4)))
	
	//Verificación de la longitud final
	Si Longitud(CURP1a4) <> 4 Entonces
		exitoFunciones <- Falso
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: GenerarCaracteres5a10
//Explicación de la función: Genera los caracteres 5 al 10 de la CURP usando la fecha de nacimiento en formato AAMMDD.
//PARÁMETROS
//fechaNacimiento (Por Referencia): Espera recibir una cadena con la fecha de nacimiento.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP5a10: Devuelve una cadena con los caracteres 5 al 10 de la CURP.
Funcion CURP5a10 <- GenerarCaracteres5a10(fechaNacimiento Por Referencia, exitoFunciones Por Referencia)
	
	//Definición de variables
	Definir CURP5a10, fechaBuenFormato Como Caracter
	
	//Llamado a función para arreglar el formato de la fecha
	fechaBuenFormato <- ArreglarFormatoFecha(fechaNacimiento, exitoFunciones)
	
	//Verificación de éxito de funciones
	Si exitoFunciones Entonces
		
		//Concatenación de año, mes y día según el formato establecido (DD/MM/AAAA)
		CURP5a10 <- Subcadena(fechaBuenFormato, 7, 8)
		CURP5a10 <- Concatenar(CURP5a10, Subcadena(fechaBuenFormato, 3, 4))
		CURP5a10 <- Concatenar(CURP5a10, Subcadena(fechaBuenFormato, 1, 2))
	FinSi
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: GenerarCaracter11
//Explicación de la función: Genera el caracter 11 de la CURP según el sexo ingresado.
//PARÁMETROS
//sexo: Espera recibir una cadena con el sexo.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP11: Devuelve el caracter correspondiente al sexo.
Funcion CURP11 <- GenerarCaracter11(sexo, exitoFunciones Por Referencia) 
	
	//Definición de variables
	Definir CURP11 Como Caracter
	
	//Conversión a mayúsculas y llamado a función para quitar acentos
	sexo <- Mayusculas(sexo)
	ArreglarAcentosNA(sexo)
	
	//Verificación de sexo hombre
	Si sexo == "HOMBRE" o sexo == "H" Entonces
		CURP11 <- "H"
	SiNo
		//Verificación de sexo mujer
		Si sexo == "MUJER" o sexo == "M" Entonces
			CURP11 <- "M"
		SiNo
			exitoFunciones <- Falso
		FinSi
	FinSi
	
FinFuncion

//Nombre de la función: GenerarCaracteres12a13
//Explicación de la función: Genera los caracteres 12 y 13 de la CURP según el estado de nacimiento.
//PARÁMETROS
//lugarNacimiento: Espera recibir un número entero del estado.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP12a13: Devuelve una cadena con los caracteres correspondientes al estado.
Funcion CURP12a13 <- GenerarCaracteres12a13(lugarNacimiento, exitoFunciones Por Referencia)
	
	//Definición de variables
	Definir CURP12a13 Como Caracter
	
	//Verificación del número del estado y asignación de caracteres
	Segun lugarNacimiento Hacer
		0: CURP12a13 <- "NE"
		1: CURP12a13 <- "AS"
		2: CURP12a13 <- "BC"
		3: CURP12a13 <- "BS"
		4: CURP12a13 <- "CC"
		5: CURP12a13 <- "CS"
		6: CURP12a13 <- "CH"
		7: CURP12a13 <- "DF"
		8: CURP12a13 <- "CL"
		9: CURP12a13 <- "CM"
		10: CURP12a13 <- "DG"
		11: CURP12a13 <- "MC"
		12: CURP12a13 <- "GT"
		13: CURP12a13 <- "GR"
		14: CURP12a13 <- "HG"
		15: CURP12a13 <- "JC"
		16: CURP12a13 <- "MN"
		17: CURP12a13 <- "MS"
		18: CURP12a13 <- "NT"
		19: CURP12a13 <- "NL"
		20: CURP12a13 <- "OC"
		21: CURP12a13 <- "PL"
		22: CURP12a13 <- "QT"
		23: CURP12a13 <- "QR"
		24: CURP12a13 <- "SP"
		25: CURP12a13 <- "SL"
		26: CURP12a13 <- "SR"
		27: CURP12a13 <- "TC"
		28: CURP12a13 <- "TS"
		29: CURP12a13 <- "TL"
		30: CURP12a13 <- "VZ"
		31: CURP12a13 <- "YN"
		32: CURP12a13 <- "ZS"
		De Otro Modo: exitoFunciones <- Falso
	FinSegun
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: GenerarCaracteres14a16
//Explicación de la función: Genera los caracteres 14, 15 y 16 de la CURP obteniendo la primera consonante interna de los nombres y apellidos.
//PARÁMETROS
//primerNombre: Espera recibir una cadena, la primera palabra del nombre.
//primerApellido: Espera recibir una cadena, la primera palabra del apellido.
//segundoApellido: Espera recibir una cadena, la primera palabra del segundo apellido.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP14a16: Devuelve una cadena con los caracteres 14, 15 y 16 de la CURP.
Funcion CURP14a16 <- GenerarCaracteres14a16(primerNombre, primerApellido, segundoApellido, exitoFunciones Por Referencia)
	
	//Definición de variables
	Definir CURP14a16, Caracter_14, Caracter_15, Caracter_16 Como Caracter
	
	//Asignación de la consonante interna del primer apellido, y asignación como X en caso de excepción
	Caracter_14 <- SacarPrimeraConsInterna(primerApellido)
	Si Caracter_14 == "" o Caracter_14 == "Ñ" Entonces
		Caracter_14 <- "X"
	FinSi
	
	//Asignación de la consonante interna del segundo apellido, y asignación como X en caso de excepción
	Caracter_15 <- SacarPrimeraConsInterna(segundoApellido)
	Si Caracter_15 == "" o Caracter_15 == "Ñ" Entonces
		Caracter_15 <- "X"
	FinSi
	
	//Asignación de la consonante interna del primer nombre, y asignación como X en caso de excepción
	Caracter_16 <- SacarPrimeraConsInterna(primerNombre)
	Si Caracter_16 == "" o Caracter_16 == "Ñ" Entonces
		Caracter_16 <- "X"
	FinSi
	
	//Concatenación de los 3 caracteres
	CURP14a16 <- Concatenar(Caracter_14, Concatenar(Caracter_15, Caracter_16))
	
FinFuncion

///////////////////////////////////////////////////////////

//Nombre de la función: GestionarGenCURP
//Explicación de la función: Revisa que los datos obligatorios no estén vacíos y manda a llamar a todas las funciones para generar la CURP completa.
//PARÁMETROS
//nombres: Espera recibir una cadena con los nombres.
//primerApellido: Espera recibir una cadena con el primer apellido.
//segundoApellido: Espera recibir una cadena con el segundo apellido.
//fechaNacimiento: Espera recibir una cadena con la fecha de nacimiento.
//sexo: Espera recibir una cadena con el sexo.
//lugarNacimiento: Espera recibir un número entero del estado.
//exitoFunciones (Por Referencia): Variable lógica que indica si hubo algún error en los datos.
//DEVUELTO
//CURP: Devuelve la cadena final con los 16 caracteres de la CURP.
Funcion CURP <- GestionarGenCURP(nombres, primerApellido, segundoApellido, fechaNacimiento, sexo, lugarNacimiento, exitoFunciones Por Referencia)
	
	//Definición de variables
	Definir CURP, primerNombre Como Caracter
	exitoFunciones <- Verdadero
	
	//Verificación de cadenas vacías
	Si nombres <> "" y primerApellido <> "" y fechaNacimiento <> "" y sexo <> "" Entonces
		
		//Llamado a función para arreglar los nombres y apellidos
		ArreglarFormatoNA(nombres, primerNombre, primerApellido, segundoApellido)
		
		//Concatenación de todas las partes de la CURP
		CURP <- GenerarCaracteres1a4(primerNombre, primerApellido, segundoApellido, exitoFunciones)
		CURP <- Concatenar(CURP, GenerarCaracteres5a10(fechaNacimiento, exitoFunciones))
		CURP <- Concatenar(CURP, GenerarCaracter11(sexo, exitoFunciones))
		CURP <- Concatenar(CURP, GenerarCaracteres12a13(lugarNacimiento, exitoFunciones))
		CURP <- Concatenar(CURP, GenerarCaracteres14a16(primerNombre, primerApellido, segundoApellido, exitoFunciones))
		
	SiNo
		exitoFunciones <- Falso
	FinSi
	
	
FinFuncion

///////////////////////////////////////////////////////////
/// **************** Proceso Principal **************** ///
///////////////////////////////////////////////////////////

Proceso Tarea3_GeneradorCURP
	
	//Definición de variables
	Definir nombres, primerApellido, segundoApellido, fechaNacimiento, sexo, CURP Como Caracter
	Definir lugarNacimiento Como Entero
	Definir exitoFunciones Como Logico
	
	//Encabezado
	Escribir "Programa generador de la CURP (Clave Única de Registro de Población) en sus primeros 16 caracteres"
	Escribir "Recuerde que los últimos 2 caracteres de su CURP (17 y 18) son generados por la SEGOB, por lo que no le podemos generar esos datos con certeza."
	Escribir ""
	Escribir "------------- Ingrese los siguientes datos correspondientes -------------"
	Escribir ""
	//Lectura de nombres
	Escribir "Ingrese su nombre (o nombres): "
	Leer nombres
	
	//Lectura de primer apellido
	Escribir "Ingrese su primer apellido: "
	Leer primerApellido
	
	//Lectura de segundo apellido
	Escribir "Ingrese su segundo apellido: "
	Leer segundoApellido
	
	//Lectura de fecha de nacimiento
	Escribir "Ingrese su fecha de nacimiento (DD/MM/AAAA): "
	Leer fechaNacimiento
	
	//Lectura de sexo
	Escribir "Ingrese la letra correspondiente a su sexo (H: Hombre / M: Mujer): "
	Leer sexo
	
	//Impresión del menú de estados y su lectura
	Escribir "- EXTRANJERO: 0"
	Escribir "- AGUASCALIENTES: 1         - MORELOS: 17"
	Escribir "- BAJA CALIFORNIA: 2        - NAYARIT: 18"
	Escribir "- BAJA CALIFORNIA SUR: 3    - NUEVO LEÓN: 19"
	Escribir "- CAMPECHE: 4               - OAXACA: 20"
	Escribir "- CHIAPAS: 5                - PUEBLA: 21"
	Escribir "- CHIHUAHUA: 6              - QUERÉTARO: 22"
	Escribir "- CIUDAD DE MÉXICO: 7       - QUINTANA ROO: 23"
	Escribir "- COAHUILA: 8               - SAN LUIS POTOSÍ: 24"
	Escribir "- COLIMA: 9                 - SINALOA: 25"
	Escribir "- DURANGO: 10               - SONORA: 26"
	Escribir "- ESTADO DE MÉXICO: 11      - TABASCO: 27"
	Escribir "- GUANAJUATO: 12            - TAMAULIPAS: 28"
	Escribir "- GUERRERO: 13              - TLAXCALA: 29"
	Escribir "- HIDALGO: 14               - VERACRUZ: 30"
	Escribir "- JALISCO: 15               - YUCATÁN: 31"
	Escribir "- MICHOACÁN: 16             - ZACATECAS: 32"
	Escribir "Ingrese el número correspondiente a su estado de nacimiento: "
	Leer lugarNacimiento
	
	//Llamado a función general
	CURP <- GestionarGenCURP(nombres, primerApellido, segundoApellido, fechaNacimiento, sexo, lugarNacimiento, exitoFunciones)
	
	
	//Verificación de éxito de las funciones
	Si exitoFunciones Entonces
		//Mensaje de éxito
		Escribir "Los primeros 16 caracteres de su Clave Única de Registro de Población (CURP) son: ", CURP
	SiNo
		//Mensaje de error
		Escribir "Alguno de los datos ingresados incorrectamente. Por favor, revise los datos y las instrucciones, y vuelva a intentar."
	FinSi
	
FinProceso

// PROBAR NUEVAMENTE TODOS LOS CASOS