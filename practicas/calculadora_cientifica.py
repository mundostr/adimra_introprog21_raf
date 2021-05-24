import math

while(True):
	numeroIngresado = float(input("Ingresar número para cálculo: "))
	if (numeroIngresado == 0):
		break
	else:
		print("OPERACIONES DISPONIBLES")
		print("1- Seno")
		print("2 - Coseno")
		print("3 - Tangente")
		print("4 - Elevado al cuadrado")
		print("5 - Raíz cuadrada")
		operacion = input("Seleccionar operación: ")

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
