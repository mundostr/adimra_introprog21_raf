import time
import keyboard


def principal():
	estadoLed = "encendido"
	marcaTiempoInicial = time.perf_counter()

	while(True):
		# print("LED", estadoLed)
		# time.sleep(1)
		# estadoLed = "apagado" if (estadoLed == "encendido") else "encendido"

		ahora = time.perf_counter()
		if (ahora - marcaTiempoInicial >= 1):
			print("LED", estadoLed)
			estadoLed = "apagado" if (estadoLed == "encendido") else "encendido"
			marcaTiempoInicial = ahora

		if (keyboard.is_pressed('S')):
			break
	
	print("Parpadeo terminado")


if (__name__ == "__main__"):
	principal()
