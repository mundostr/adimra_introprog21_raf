# Solicitamos el ingreso de 5 nros, y en cada iteracción comparamos para terminar almacenando
# en la variable "mayor" el mayor ingresado.
for x in range (5): # ciclo finito que itera 5 veces, x va de 0 a 4
	ingreso = int(input("Ingresar nro: "))
	if (x == 0):
		mayor = ingreso
	else:
		if (ingreso > mayor):
			mayor = ingreso
print(mayor)
