//Nombre del archivo: IMCyCategorias.psc
//Descripción del programa: El programa evalúa la edad del usuario, en caso de tener la edad mínima requerida, se calculará su IMC y se le dará a conocer al usuario su índice junto a su categoría correspondiente .
//Autores: Ángel Adrián Barragán Ruiz y Khristo Ricardo Rodriguez Valencia
//Fecha: 26/08/2026

Proceso IMCyCategorias
	//Definición de variables
	Definir peso, estatura, IMC Como Real
	Definir edad Como Entero
	
	//Encabezado
	Escribir "Bienvenido, aquí conocerás tu IMC y tu categoría correspondiente según la OMS"
	
	//Solicitud y lectura de edad
	Escribir "Ingrese su edad en años:"
	Leer edad
	
	//Verificación de la edad mínima de 20 años
	Si edad >= 20 Entonces
		//Solicitud y lectura del peso
		Escribir "Ingrese su peso en kg:"
		Leer peso
		
		//Verificación del peso mínimo mayor a 0
		Si peso > 0 Entonces
			//Solicitud y lectura de la estatura
			Escribir "Ingrese su estatura en metros:"
			Leer estatura
			
			//Verificación de la estatura mínima mayor a 0
			Si estatura > 0 Entonces
				//Cálculo del IMC
				IMC <- peso / estatura ^ 2
				
				//Escritura de su IMC calculado
				Escribir "Su IMC es de: ", IMC
				
				//Verificación por categorías:
				//Categoría de bajo peso severo
				Si IMC < 16.5 Entonces
					Escribir "Usted entra en la categoría: Bajo peso severo."
				FinSi
				//Categoría de bajo peso 
				Si IMC >= 16.5 y IMC < 18.5 Entonces
					Escribir "Usted entra en la categoría: Bajo peso."
				FinSi
				//Categoría de peso saludable
				Si IMC >= 18.5 y IMC < 25 Entonces
					Escribir "Usted entra en la categoría: Peso saludable."
				FinSi
				//Categoría de sobrepeso
				Si IMC >= 25 y IMC < 30 Entonces
					Escribir "Usted entra en la categoría: Sobrepeso."
				FinSi
				//Categoría de obesidad tipo I (moderada)
				Si IMC >= 30 y IMC < 35 Entonces
					Escribir "Usted entra en la categoría: Obesidad tipo I (moderada)."
				FinSi
				//Categoría de obesidad tipo II (severa)
				Si IMC >= 35 y IMC < 40 Entonces
					Escribir "Usted entra en la categoría: Obesidad tipo II (severa)."
				FinSi
				//Categoría de obesidad tipo III (mórbida)
				Si IMC >= 40 Entonces
					Escribir "Usted entra en la categoría: Obesidad tipo III (mórbida)."
				FinSi
				//Escritura de la explicación de las categorías
				Escribir "Estas categorías son utilizadas por la OMS (Organización Mundial de la Salud) desde 1995 y son adoptadas por prácticamente todas las autoridades sanitarias."
			SiNo
				//Escritura de la explicación del error por estatura menor o igual a 0
				Escribir "[Error] No se puede ingresar una estatura menor o igual a 0."
			FinSi
		SiNo
			//Escritura de la explicación del error por peso menor o igual a 0
			Escribir "[Error] No se puede ingresar un peso menor o igual a 0."
		FinSi
	SiNo
		//Verificación del error por edad menor a 0, o detección de una edad real pero menor a 20
		Si edad <= 0 Entonces
			//Escritura de la explicación del error por edad menor o igual a 0
			Escribir "[Error] No se puede ingresar una edad menor o igual a 0."
		SiNo
			//Escritura de la explicación por no poder calcular su IMC y categoría correctamente si es menor a 20 años
			Escribir "Lo siento, no podemos calcular su IMC y categoría correctamente si es menor de 20 años."
		FinSi
	FinSi
FinProceso
