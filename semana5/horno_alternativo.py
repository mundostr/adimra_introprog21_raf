# LIBRERIAS
import random


# DEFINICIONES
TEMP_MIN = 100
TEMP_MAX = 200
TEMP_TOL = 2
TEMP_OBJ = 150
TEMP_PRUEBA = 145


# FUNCIONES
def generarArchivoRandomSensor():
	# r = read (lectura)
	# w = write (escritura sobreescrita)
	# a = append (escritura agregada)
	archivo = open("lecturas_horno.txt", "w")
	for x in range(50):
		valorRandom = random.randint(TEMP_PRUEBA - TEMP_TOL, TEMP_PRUEBA + TEMP_TOL + 1)
		valorRandom = str(valorRandom) + "\n"
		archivo.write(valorRandom)
	archivo.close()
	print("Archivo generado")

def verificarTemperatura():
	# Recuperación de lecturas de sensor
	archivo = open("lecturas_horno.txt", "r")
	lista = archivo.read().split("\n")
	archivo.close()

	# Obtención de promedio
	totalLecturas = 0
	for indice, item in enumerate(lista):
		lista[indice] = int(item) # lista[indice] = int(lista[indice])
		totalLecturas = totalLecturas + lista[indice]
	promedio = totalLecturas / 50
	print(promedio)

	# Comparación de promedio con obj
	OBJ_MIN = TEMP_OBJ - TEMP_TOL
	OBJ_MAX = TEMP_OBJ + TEMP_TOL
	# if (promedio >= OBJ_MIN and promedio <= OBJ_MAX):
	if (OBJ_MIN <= promedio <= OBJ_MAX):
		print("Horno estable")
	elif (promedio > OBJ_MAX):
		print("Horno muy caliente, apagar quemador")
	else:
		print("Horno frío, encender quemador")



# PRINCIPAL
# generarArchivoRandomSensor()
verificarTemperatura()
