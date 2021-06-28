# LIBRERIAS
# Podemos utilizar from para importar solo los métodos que necesitamos en lugar de la librería completa
from math import perm
# itertools nos brinda métodos cómodos para manejar permutaciones y combinaciones
from itertools import permutations, combinations


# DEFINICIONES


# FUNCIONES
def calcularPermutaciones(lista):
	totalPermutaciones = perm(len(lista))
	permutaciones = permutations(lista)
	
	print("Total:", totalPermutaciones)
	for item in permutaciones: print(item)

def calcularCombinaciones(lista, tomados):
	totalCombinaciones = 0
	# totalCombinaciones = comb(len(lista), tomados)
	combinaciones = combinations(lista, tomados)
	
	for item in combinaciones:
		# Alternativamente, en lugar de importar el método comb desde math
		# aprovechamos el ciclo en el que mostramos todas las combinaciones
		# para obtener el total.
		totalCombinaciones += 1
		print(item)
	print("Total:", totalCombinaciones)

def main():
	lista = (1, 2, 3, 4)
	# calcularPermutaciones(lista)
	calcularCombinaciones(lista, 2)


# PRINCIPAL
if (__name__ == "__main__"):
	main()
