# Librerías
# python -m pip install enum34
import time
import datetime as dt
import keyboard
from enum import Enum


# Objs globales
HORARIO_NORMAL_MIN = dt.time(6, 0)
HORARIO_NORMAL_MAX = dt.time(23, 59)
ESTADO = Enum("estado", "DESACTIVADO FIJO NORMAL INTERMITENTE")


# Declaraciones
def activarLuz(luz, tiempo):
	print(luz)
	time.sleep(tiempo)

def horarioNormal(inicio, fin):
	ahora = dt.datetime.now().time()
	return inicio <= ahora <= fin


# Main
def main():
	# Control horario
	if (horarioNormal(HORARIO_NORMAL_MIN, HORARIO_NORMAL_MAX)):
		estadoActual = ESTADO.NORMAL
	else:
		estadoActual = ESTADO.INTERMITENTE

	# Control luces
	notificado = False
	while(True):
		if keyboard.is_pressed("a"):
			estadoActual = ESTADO.NORMAL
		
		if keyboard.is_pressed("d"):
			estadoActual = ESTADO.DESACTIVADO

		if (estadoActual == ESTADO.DESACTIVADO):
			if not (notificado):
				print("El semáforo está desactivado")
				notificado = True

		elif (estadoActual == ESTADO.FIJO):
			if not (notificado):
				print("El semáforo está fijo")
				notificado = True

		elif (estadoActual == ESTADO.NORMAL):
			print()
			activarLuz("verde", 3)
			activarLuz("amarillo", 1)
			activarLuz("rojo", 5)

		elif (estadoActual == ESTADO.INTERMITENTE):
			print()
			activarLuz("amarillo", 1)
			activarLuz("apagado", 1)

	# if not (horarioNormal(HORARIO_NORMAL_MIN, HORARIO_NORMAL_MAX)):
	# 	while(True):
	# 		print()
	# 		activarLuz("verde", 3)
	# 		activarLuz("amarillo", 1)
	# 		activarLuz("rojo", 5)
	# else:
	# 	while(True):
	# 		print()
	# 		activarLuz("amarillo", 1)
	# 		activarLuz("apagado", 1)

	# while(True):
		# print("Verde")
		# time.sleep(3)
		# print("Amarillo")
		# time.sleep(1)
		# print("Rojo")
		# time.sleep(5)

		# activarLuz("verde", 3)
		# activarLuz("amarillo", 1)
		# activarLuz("rojo", 5)

if (__name__ == "__main__"):
	main()
