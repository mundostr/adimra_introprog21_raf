for ciclo in range (5):
	ingreso = int(input("Ingresar nro: "))
	if (ciclo == 0):
		mayor = ingreso
	else:
		if (ingreso > mayor):
			mayor = ingreso
print(mayor)
