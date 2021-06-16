sumatoria = 0

# Ciclo finito que se repite 5 veces
for ciclo in range (5):
	ingreso = int(input("Ingresar nro: "))
	sumatoria = sumatoria + ingreso # puede escribirse también como sumatoria += ingreso
	# esto es lo que normalmente se identifica como acumulador, una variable que es sobreescrita por el valor de sí misma más otra variable

print(sumatoria)
