# Importamos la librería random para generar números enteros al azar mediante randint
import random

TEMP_MIN = 100
TEMP_MAX = 200
TEMP_TOLERANCIA = 2
CTD_LECTURAS_SENSOR = 10

print("CONTROL TEMPERATURA HORNO")
while(True):
	# La temperatura objetivo, la generamos al azar, solo para practicar el uso de un método desde librería
	temperaturaObjetivo = random.randint(TEMP_MIN, TEMP_MAX + 1) # +1 ya que randint no incluye el límite superior en el rango
	print("Temperatura objetivo:", temperaturaObjetivo)
	
	# La temperatura de prueba es ingresada por teclado, controlando que no se pase de los límites
	temperaturaPrueba = int(input("Temperatura de prueba: "))
	if (temperaturaPrueba == 0):
		print("Finalizado")
		break
	elif (temperaturaPrueba >= TEMP_MIN and temperaturaPrueba <= TEMP_MAX):
		print("Temperatura prueba:", temperaturaPrueba)
		
		# Las lecturas del sensor de temperatura, son simuladas generándolas también al azar
		# partiendo de la temperatura de prueba ingresada y obteniendo el promedio
		lecturas = 0
		for x in range(CTD_LECTURAS_SENSOR):
			lecturas += random.randint(temperaturaPrueba - TEMP_TOLERANCIA, temperaturaPrueba + TEMP_TOLERANCIA + 1)
		promedio = lecturas / CTD_LECTURAS_SENSOR
		print("Temperatura promedio", promedio)
		print()
		
		# Finalmente comparamos el promedio obtenido con el objetivo, considerando la tolerancia
		if (temperaturaObjetivo - TEMP_TOLERANCIA <= promedio <= temperaturaObjetivo + TEMP_TOLERANCIA):
			print("Horno estable")
		elif (promedio < temperaturaObjetivo - TEMP_TOLERANCIA):
			print("Temperatura baja, se enciende quemador")
		elif (promedio > temperaturaObjetivo + TEMP_TOLERANCIA):
			print("Temperatura alta, se apaga quemador")
	else:
		print("Solo se aceptan temperaturas de prueba entre " + str(TEMP_MIN) + " y " + str(TEMP_MAX) + "")
	print()
