CTD_MIN_NROS = 5

contador = 0
listaIngresos = [] # Los [] identifican listas

while(True):
	ingreso = int(input("número: "))
	if (ingreso == 0):
		if (contador >= CTD_MIN_NROS):
			break
	else:
		listaIngresos.append(ingreso) # append permite agregar items a una lista
		contador = contador + 1 # o contador += 1

listaIngresos.sort(reverse = True) # reverse = True para ordenar DESCENDENTE
sumatoria = listaIngresos[0] + listaIngresos[1] + listaIngresos[2] # [x] x es el índice del item a acceder, comenzando SIEMPRE desde 0

print(sumatoria)
