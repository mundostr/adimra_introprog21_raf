# DEFINICIONES
# Simplemente por orden, declaramos algunas constantes y variables generales al inicio
# Recordar que Python no cuenta con un comando para declarar constantes, básicamente todos
# los elementos son considerados variables, por esa razón elegimos utilizar nomenclatura
# en MAYUSCULAS que nos permita ubicar fácilmente las constantes de forma visual.
ANIO = 365
SEMESTRE1 = 183
SEMESTRE2 = 182
INGRESO_ALTO = 8000

ingresosTotales = 0
ingresosSemestre1 = 0
ingresosSemestre2 = 0
promedioSemestre1 = 0
promedioSemestre2 = 0
promedioGeneral = 0
diasAltoIngreso = 0
porcDiasAltoIngreso = 0


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


# BLOQUE CENTRAL
# Llamamos a la función cargarDatosIntDesdeArchivo(), pasándole un argumento que
# es el nombre del archivo desde el cual debe recuperar los registros.
# La función nos "devolverá" una lista de enteros que asignaremos a listaIngresos
listaIngresos = cargarDatosIntDesdeArchivo("ingresos_diarios_2020.txt")

# Cálculos requeridos
# Utilizamos 3 veces un ciclo for(), para iterar listaIngresos y realizar
# los diferentes cálculos. Intentar compactar este proceso en un único for()
# y encapsular también en una función, para mayor orden.
for indice, item in enumerate(listaIngresos):
	if (indice < SEMESTRE1):
		ingresosSemestre1 = ingresosSemestre1 + item
promedioSemestre1 = int(ingresosSemestre1 / SEMESTRE1)

for indice, item in enumerate(listaIngresos):
	if (indice >= SEMESTRE1 and indice < ANIO):
		ingresosSemestre2 = ingresosSemestre2 + item
promedioSemestre2 = int(ingresosSemestre2 / SEMESTRE2)

promedioGeneral = (promedioSemestre1 + promedioSemestre2) / 2

for indice, item in enumerate(listaIngresos):
	if (item >= INGRESO_ALTO):
		diasAltoIngreso = diasAltoIngreso + 1
porcDiasAltoIngreso = int((diasAltoIngreso / ANIO) * 100)

# Salida de información
# Repasamos 4 alternativas para mostrar datos por consola o formatearlos para futuro uso.
# Para desarrollo y depuración, podemos aplicar simplemente la opción "plana", imprimiendo
# el / los nombres de variables que necesitamos. Si debemos imprimir varios en una misma línea,
# solo los separamos por comas -> print(promedioSemestre1, promedioSemestre2, etc)
print(promedioSemestre1)

# Esta es otra variante, del lado izquierdo colocamos un "título", y luego las variables a mostrar,
# con la misma idea del caso anterior. Si es más de una, separaremos por comas.
print("Promedio diario 2do semestre:", promedioSemestre2)

# En este caso estamos formando un texto único, "concatenando" 3 "eslabones" mediante el signo +.
# Lógicamente las partes que ya sean cadenas se escriben de forma directa, y las que no, se
# convierten utilizando la función str(), caso contrario el intérprete generará un error al
# momento de evaluar el comando.
print("Promedio diario general: $ " + str(promedioGeneral) + " AR")

# Esta alternativa es más actual y "limpia", porque no necesitamos realizar el casting, es decir
# las conversiones a cadena. Tan solo armamos un único texto del lado izquierdo, con "placeholders".
# En este caso los placeholders se especifican con llaves y un índice, comenzando en 0. Si en la
# cadena se desea colocar 3 variables, los placeholders serán {0}, {1} y {2}, y en forma()
# listaremos las variables separadas por comas.
print("Porcentaje días con alto ingreso: {0} %".format(porcDiasAltoIngreso))
