import random # importamos la librería random para poder generar nros al azar

CTD_PERSONAS = 10
LIMITE_CUENTA = 25

persona = random.randint(0, CTD_PERSONAS - 1) # solo utilizamos un nro random para ver qué persona comienza el conteo
sentidoRonda = "horario"

for cuenta in range(1, LIMITE_CUENTA + 1):
	if (sentidoRonda == "horario"):
		if (persona < CTD_PERSONAS):
			persona = persona + 1
		else:
			persona = 1 # no podemos superar CTD_PERSONAS, si persona no es <, vuelve a 1
	else:
		if (persona > 1):
			persona = persona - 1
		else:
			persona = CTD_PERSONAS # no podemos bajar de 1, si persona no es > 1, vuelve a CTD_PERSONAS

	if (cuenta % 8 == 0): # verificamos si cuenta es perfectamente divisible por 8 p/ cambiar el sentido de giro
		if (sentidoRonda == "horario"):
			sentidoRonda = "antihorario"
		else:
			sentidoRonda = "horario"
	
	if (cuenta % 12 == 0):
		# La intención es verificar si cuenta es perfectamente divisible por 11, no obstante utilizamos 12 en el if
		# para que el cálculo de persona se realice antes del salto, caso contrario quedaría desfazado por 1
		if (sentidoRonda == "horario"):
			persona = persona + 1
		else:
			persona = persona - 1

	print("sentido:", sentidoRonda, " | persona:", persona, " | cuenta:", cuenta)
