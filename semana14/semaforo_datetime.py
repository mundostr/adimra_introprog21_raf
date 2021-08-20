# Librerías
import time
import datetime
import keyboard


MODO_DIURNO_INI = datetime.time(6, 0, 0)
MODO_DIURNO_FIN = datetime.time(23, 59, 0)
LUCES = [
	{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 5 },
	{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 1 },
	{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 5 },
	{ "nombre": "________APA________", "color": "\x1b[0m", "demora": 1 }
]


def controlarModoHorario(modo, luz, luzActiva, timerLuz):
	if not (modo == "FIJO"):
		if (MODO_DIURNO_INI <= datetime.datetime.now().time() <= MODO_DIURNO_FIN):
			if not(modo == "DIURNO"):
				luz = 0
				modo = "DIURNO"
				luzActiva = False
		else:
			if not(modo == "NOCTURNO"):
				luz = 1
				modo = "NOCTURNO"
				luzActiva = False
		
		timerLuz = time.perf_counter()
	
	return modo, luz, luzActiva, timerLuz


# Main
if(__name__ == "__main__"):
	luz = 0
	modo = "INICIAL"
	luzActiva = False
	timerLuz = timer_teclado = timer_control_modo = time.perf_counter()
	modo, luz, luzActiva, timerLuz = controlarModoHorario(modo, luz, luzActiva, timerLuz)
	
	while(True):
		# Control pulsador modo FIJO
		if (time.perf_counter() - timer_teclado >= 0.175):
			if (keyboard.is_pressed('f')):
				print("f presionada")

				if (modo == "FIJO"):
					modo = "INICIAL"
					modo, luz, luzActiva, timerLuz = controlarModoHorario(modo, luz, luzActiva, timerLuz)
				else:
					luz = 0
					modo = "FIJO"
					luzActiva = False
			timer_teclado = time.perf_counter()
		
		# Control horario de modo
		if (time.perf_counter() - timer_control_modo >= 60):
			modo, luz, luzActiva, timerLuz = controlarModoHorario(modo, luz, luzActiva, timerLuz)
			timer_control_modo = time.perf_counter()

		# Modo Fijo
		if (modo == "FIJO"):
			if not (luzActiva):
				print(LUCES[luz]["color"] + LUCES[luz]["nombre"] + "\x1b[0m")
				luzActiva = True

		# Modo diurno
		if (modo == "DIURNO"):
			if not (luzActiva):
				print(LUCES[luz]["color"] + LUCES[luz]["nombre"] + "\x1b[0m")
				luzActiva = True

			if (time.perf_counter() - timerLuz >= LUCES[luz]["demora"]):
				luz += 1
				if (luz == len(LUCES) - 1): luz = 0
				luzActiva = False
				timerLuz = time.perf_counter()
		
		# Modo nocturno
		if (modo == "NOCTURNO"):
			if not (luzActiva):
				print(LUCES[luz]["color"] + LUCES[luz]["nombre"] + "\x1b[0m")
				luzActiva = True
			
			if (time.perf_counter() - timerLuz >= LUCES[luz]["demora"]):
				luz = -1 if (luz == 1) else 1
				luzActiva = False
				timerLuz = time.perf_counter()