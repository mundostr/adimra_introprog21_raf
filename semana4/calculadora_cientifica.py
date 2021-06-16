# importamos la librería math para acceder a las funciones como seno, coseno, tangente, etc
import math

# Activamos un ciclo indefinido, que se rompe solo al ingresar 0 en numeroIngresado
while(True):
	numeroIngresado = float(input("Ingresar número para cálculo: ")) # solicitamos el ingreso de un número, y lo convertimos a coma flotante
	if (numeroIngresado == 0):
		break
	else:
		print("OPERACIONES DISPONIBLES PARA CALCULO")
		print("1- Seno")
		print("2 - Coseno")
		print("3 - Tangente")
		print("4 - Elevado al cuadrado")
		print("5 - Raíz cuadrada")
		operacion = input("Seleccionar operación: ")

		# Solo evaluamos en orden si la operación ingresada está entre 1 y 5
		# Si es así, ejecutamos el cálculo correspondiente, caso contrario generamos mensaje de error
		if (operacion == "1"):
			print(math.sin(numeroIngresado))
		elif (operacion == "2"):
			print(math.cos(numeroIngresado))
		elif (operacion == "3"):
			print(math.tan(numeroIngresado))
		elif (operacion == "4"):
			print(numeroIngresado * numeroIngresado)
		elif (operacion == "5"):
			print(math.sqrt(numeroIngresado))
		else:
			print("Operaciones válidas, solo de 1 a 5")

print("Calculadora finalizada.")
