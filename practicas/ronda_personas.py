LIMITE_CUENTA = 100
CANTIDAD_PERSONAS = 10

cuenta = 0
persona = 0
sentidoGiro = "horario"

for ciclo in range(LIMITE_CUENTA):
	# Incremento de cuenta
	cuenta += 1 # cuenta = cuenta + 1

	# Control de persona dentro del límite de la ronda
	if (sentidoGiro == "horario"):
		if (persona < CANTIDAD_PERSONAS):
			persona = persona + 1
		else:
			persona = 1
	else:
		if (persona > 1):
			persona = persona - 1
		else:
			persona = CANTIDAD_PERSONAS
	
	# Control de cuenta perfectamente divisible por 8
	if (cuenta % 8 == 0):
		if (sentidoGiro == "horario"):
			sentidoGiro = "antihorario"
		else:
			sentidoGiro = "horario"
	
	print(cuenta, persona, sentidoGiro)
