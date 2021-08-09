# Ejemplo de threading para ejecución de tareas en paralelo
import time
import threading


# Función llamada por la tarea1
def contar(contador, espera):
	while(True):
		contador += 1
		print(contador)
		time.sleep(espera)

# Función llamada por la tarea2
def notificar(msj, espera):
	while(True):
		print(msj)
		time.sleep(espera)


if (__name__ == '__main__'):
	# Se crean 2 tareas periódicas independientes, una correrá cada 1 segundo
	# y la otra cada 3.5 segundos
	tarea1 = threading.Thread(target=contar, args=(0, 1))
	tarea2 = threading.Thread(target=notificar, args=("Control", 3.25))
	
	tarea1.start()
	tarea2.start()
