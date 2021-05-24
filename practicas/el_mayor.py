for x in range (5): # ciclo finito que itera 5 veces, x va de 0 a 4
	ingreso = int(input("Ingresar nro: "))
	if (x == 0):
		mayor = ingreso
	else:
		if (ingreso > mayor):
			mayor = ingreso
print(mayor)
