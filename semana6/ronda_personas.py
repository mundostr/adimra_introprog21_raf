LIMITE_CUENTA = 100
CANTIDAD_PERSONAS = 10

cuenta = 0
persona = 0
sentidoGiro = "horario"
variacionConteoPersona = 1

# Ciclamos de manera finita hasta LIMITE_CUENTA
for ciclo in range(LIMITE_CUENTA):
	# Incremento de cuenta
	cuenta += 1 # cuenta = cuenta + 1

	# Controlamos persona dentro del límite de la ronda, en ambos sentidos
	if (sentidoGiro == "horario"):
		if (persona < CANTIDAD_PERSONAS):
			persona = persona + variacionConteoPersona
			# Retornamos variacionConteoPersona a 1, ya que solo debemos ejecutarlo 1 vez cuando esté en 2
			if (variacionConteoPersona == 2): variacionConteoPersona = 1
		else:
			persona = 1
	else:
		if (persona > 1):
			persona = persona - variacionConteoPersona
			# Retornamos variacionConteoPersona a 1, ya que solo debemos ejecutarlo 1 vez cuando esté en 2
			if (variacionConteoPersona == 2): variacionConteoPersona = 1
		else:
			persona = CANTIDAD_PERSONAS
	
	# Control de cuenta perfectamente divisible por 8 para cambiar de sentido la ronda
	if (cuenta % 8 == 0):
		if (sentidoGiro == "horario"):
			sentidoGiro = "antihorario"
		else:
			sentidoGiro = "horario"
	
	# Control de cuenta perfectamente divisible por 11 para saltar persona
	if (cuenta % 11 == 0):
		variacionConteoPersona = 2
	
	print(cuenta, persona, sentidoGiro)
