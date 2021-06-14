# DEFINICIONES
# Simplemente por orden, declaramos algunas constantes y variables generales al inicio
# Recordar que Python no cuenta con un comando para declarar constantes, básicamente todos
# los elementos son considerados variables, por esa razón elegimos utilizar nomenclatura
# en MAYUSCULAS que nos permita ubicar fácilmente las constantes de forma visual.
ANIO = 365
SEMESTRE1 = 183
SEMESTRE2 = 182
INGRESO_ALTO = 8000

# ingresosSemestre1 = 0
# ingresosSemestre2 = 0
# diasAltoIngreso = 0
# promedioGeneral = 0
# cpromedioSemestre1 = 0
# promedioSemestre2 = 0
# porcDiasAltoIngreso = 0


# FUNCIONES
# Declaramos las funciones a utilizar, recordar hacerlo previamente a su llamado.
def cargarDatosIntDesdeArchivo(ruta):
	# Abrimos ruta para lectura.
	archivo = open(ruta, "r")
	# Leemos el contenido, separándolo por comas y cargándolo en la lista lectura.
	lectura = archivo.read().split(",")
	archivo.close()

	for indice, item in enumerate(lectura):
		# Recorremos la lista para convertir cada item a entero mediante la función int().
		# A esto se lo conoce normalmente con el término casting.
		lectura[indice] = int(item)

	# Finalmente la función "devuelve" la lista convertida
	return lectura

def procesarCalculos():
	# global ingresosSemestre1, ingresosSemestre2, diasAltoIngreso
	# global promedioSemestre1, promedioSemestre2, promedioGeneral, porcDiasAltoIngreso

	ingresosSemestre1 = 0
	ingresosSemestre2 = 0
	diasAltoIngreso = 0
	
	for indice, item in enumerate(listaIngresos):
		if (indice < SEMESTRE1):
			ingresosSemestre1 = ingresosSemestre1 + item
		else:
			ingresosSemestre2 = ingresosSemestre2 + item
		
		if (item >= INGRESO_ALTO):
			diasAltoIngreso = diasAltoIngreso + 1

	promedioSemestre1 = int(ingresosSemestre1 / SEMESTRE1)
	promedioSemestre2 = int(ingresosSemestre2 / SEMESTRE2)
	promedioGeneral = (promedioSemestre1 + promedioSemestre2) / 2
	porcDiasAltoIngreso = int((diasAltoIngreso / ANIO) * 100)

	return promedioSemestre1, promedioSemestre2, promedioGeneral, porcDiasAltoIngreso


# BLOQUE CENTRAL
# Llamamos a la función cargarDatosIntDesdeArchivo(), pasándole un argumento que
# es el nombre del archivo desde el cual debe recuperar los registros.
# La función nos "devolverá" una lista de enteros que asignaremos a listaIngresos
listaIngresos = cargarDatosIntDesdeArchivo("ingresos_diarios_2020.txt")

# Ejemplo alcance de variables (Scope)
ps1, ps2, pg, dai = procesarCalculos()

# SALIDAS
print("Promedio diario semestre 1, 2 y general: $ {0} AR | $ {1} AR | $ {2} AR".format(ps1, ps2, pg))
print("Porcentaje días con alto ingreso: {0} %".format(dai))
