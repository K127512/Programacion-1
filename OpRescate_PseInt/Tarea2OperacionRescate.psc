// Nombre del archivo: Tarea2OperacionRescate.psc
// Descripción del programa: Programa para calcular y clasificar las posibilidades de cada estudiante de obtener promedios sobresalintes, regulares, suficientes o reprobatorios, según resultados de 3 exámenes anteriores y uno más aún sin evaluar.
// Autores: Angel Adrián Barragán Ruiz y Khristo Ricardo Rodriguez Valencia
// Grupo: 7
// Fecha: 17/09/2026

Proceso Tarea2OperacionRescate
	//Definición de variables
	Definir cantEstudiantes, contEstudiantes, califE1, califE2, califE3, califMinSuf, califMinReg, califMinSobre, estudiantesPosSobre, estudiantesPosReg, estudiantesPosSuf, estudiantesSinPos Como Entero
    
    //Encabezado
    Escribir "Bienvenido, en este programa podrá ingresar la calificación de los primeros 3 exámenes de sus estudiantes y,  conocer sus estadísticas para el cuarto examen y posibilidades del promedio."
	
	//Lectura de la cantidad de estudiantes a evaluar
	Escribir "Ingrese la cantidad de estudiantes a evaluar: " Sin Saltar
	Leer cantEstudiantes
	
    //Validación del valor de estudiantes mayor a 0
	Mientras cantEstudiantes < 1 Hacer
		Escribir "Error: No puede ingresar un número menor a 1."
		Escribir "Ingrese la cantidad de estudiantes a evaluar: " Sin Saltar
		Leer cantEstudiantes
	FinMientras
	
    //Inicialización de variables
	contEstudiantes <- 1
    estudiantesPosSobre <- 0
    estudiantesPosReg <- 0
    estudiantesPosSuf <- 0
    estudiantesSinPos <- 0
	
    LimpiarPantalla
	
    //Ciclo para la lectura de cada examen de cada estudiante y cálculos de promedios, posibilidades e incremento de acumuladores
	Mientras contEstudiantes <= cantEstudiantes Hacer
		
        //Lectura de la calificación del primer examen y verificación de que siempre escriba un valor válido
		Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del primer examen (0-100): " Sin Saltar
        Leer califE1
		Mientras califE1 < 0 o califE1 > 100 Hacer
            Escribir "Error: Valor ingresado incorrecto. Siga las indicaciones, valor entre 0 y 100."
			Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del primer examen (0-100): " Sin Saltar
        	Leer califE1
	    FinMientras
        
		//Lectura de la calificación del segundo examen y verificación de que siempre escriba un valor válido
        Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del segundo examen (0-100): " Sin Saltar
		Leer califE2
		Mientras califE2 < 0 o califE2 > 100 Hacer
            Escribir "Error: Valor ingresado incorrecto. Siga las indicaciones, valor entre 0 y 100."
			Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del segundo examen (0-100): " Sin Saltar
        	Leer califE2
	    FinMientras
		
		//Lectura de la calificación del tercer examen y verificación de que siempre escriba un valor válido
        Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del tercer examen (0-100): " Sin Saltar
		Leer califE3
		Mientras califE3 < 0 o califE3 > 100 Hacer
            Escribir "Error: Valor ingresado incorrecto. Siga las indicaciones, valor entre 0 y 100."
			Escribir "Ingrese la calificación del estudiante #", contEstudiantes, " del tercer examen (0-100): " Sin Saltar
        	Leer califE3
	    FinMientras
		
        //Calificación mínima del cuarto examen para cada categoría
		califMinSuf <- 240 - califE1 - califE2 - califE3
        califMinReg <- 244 - califE1 - califE2 - califE3
		califMinSobre <- 360 - califE1 - califE2 - califE3
		
        //Impresión de resultados por estudiante
        Escribir " ---- Resultados del estudiante #", contEstudiantes, " ---- "
		Escribir "Promedio actual (considerando los tres exámenes aplicados): ", redon((califE1 + califE2 + califE3) / 3)
		
		//Verificación de no mostrar una calificación para examen imposible (negativa)
		Si califMinSobre <= 100 Entonces
			Escribir "Calificación necesaria en el cuarto examen para obtener un promedio final de 90: ", califMinSobre
		SiNo
			Escribir "El estudiante no puede llegar con ninguna calificación en el cuarto examen a un promedio final de 90 o más"
		FinSi
		
		//Verificación de no mostrar una calificación para examen imposible (negativa, 0 o mayor a 100)
		Si califMinSuf <= 100 y califMinSuf >= 1 Entonces
			Escribir "Calificación necesaria en el cuarto examen para obtener un promedio final de 60: ", califMinSuf
		SiNo
			Si califMinSuf > 100 Entonces
				Escribir "El estudiante no puede llegar con ninguna calificación en el cuarto examen a un promedio final de 60 o más"
			SiNo
				Escribir "Con cualquier calificación, el estudiante llegará a un promedio de 60 o más"
			FinSi
		FinSi
		
		//Verificación de meta de promedio sobresaliente alcanzable o inalcanzable
		Si califMinSobre <= 100 Entonces
			Escribir "Obtener un promedio final de 90 es alcanzable."
		SiNo
			Escribir "Obtener un promedio final de 90 es inalcanzable."
		FinSi
		
		//Verificación de meta de promedio suficiente alcanzable, inalcanzable o inevitable
		Si califMinSuf <= 100 y califMinSuf >= 0 Entonces
			Escribir "Obtener un promedio final de 60 es alcanzable."
		SiNo
			Si califMinSuf <= 0 Entonces
				Escribir "Obtener un promedio final de 90 es inevitable."
			SiNo
				Escribir "Obtener un promedio final de 60 es inalcanzable."
			FinSi
		FinSi
		
        //Clasificaciones y aumento del acumulador según la categoría correspondiente del estudiante
        Si califMinSobre <= 100 Entonces
            Escribir "Categoría: Sobresaliente potencial"
            estudiantesPosSobre <- estudiantesPosSobre + 1
        SiNo
            Si califMinReg <= 100 Entonces
                Escribir "Categoría: Rendimiento regular potencial"
                estudiantesPosReg <- estudiantesPosReg + 1
            SiNo
                Si califMinSuf <= 100 Entonces
                    Escribir "Categoría: Puede rescatar el semestre"
                    estudiantesPosSuf <- estudiantesPosSuf + 1
                SiNo
                    Escribir "Categoría: Reprobado inevitable"
                    estudiantesSinPos <- estudiantesSinPos + 1
                FinSi
            FinSi
        FinSi
		
		//Salto de línea para separación visual
        Escribir ""
		
		//Incremento al contador
        contEstudiantes <- contEstudiantes + 1
	FinMientras
	
    //Impresión de los resultados finales
    Escribir " ------ RESULTADOS FINALES  ------ "
    Escribir "Cantidad de estudiantes con posibilidad de obtener un promedio sobresaliente: ", estudiantesPosSobre
    Escribir "Cantidad de estudiantes con posibilidad de obtener un rendimiento regular: ", estudiantesPosReg 
    Escribir "Cantidad de estudiantes que pueden rescatar el semestre: ", estudiantesPosSuf
    Escribir "Cantidad de estudiantes que reprobarán inevitablemente: ", estudiantesSinPos
FinProceso
