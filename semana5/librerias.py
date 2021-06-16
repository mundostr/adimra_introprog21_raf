# El comando import, nos permite importar ya sea de forma parcial o completa una librería disponible en el sistema
import random

CTD_NUMEROS = 5

sumatoria = 0

for c1 in range(CTD_NUMEROS):
	# Una vez importada la librería, accedemos a sus métodos utilizando la notación de puntos,
	# como es en este caso random.randint()
	numero = random.randint(0, 100)
	print(numero)
	sumatoria = sumatoria + numero

print()
print(sumatoria)
