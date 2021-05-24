import random

CTD_PERSONAS = 10
LIMITE_CUENTA = 25

persona = random.randint(0, CTD_PERSONAS - 1)
sentidoRonda = "horario"

for cuenta in range(1, LIMITE_CUENTA + 1):
	if (sentidoRonda == "horario"):
		if (persona < 10):
			persona = persona + 1
		else:
			persona = 1
	else:
		if (persona > 1):
			persona = persona - 1
		else:
			persona = CTD_PERSONAS

	if (cuenta % 8 == 0):
		if (sentidoRonda == "horario"):
			sentidoRonda = "antihorario"
		else:
			sentidoRonda = "horario"
	
	if (cuenta % 12 == 0):
		if (sentidoRonda == "horario"):
			persona = persona + 1
		else:
			persona = persona - 1

	print("sentido:", sentidoRonda, " | persona:", persona, " | cuenta:", cuenta)
