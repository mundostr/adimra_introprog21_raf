import random

CTD_NUMEROS = 5

sumatoria = 0

for c1 in range(CTD_NUMEROS):
	numero = random.randint(0, 100)
	print(numero)
	sumatoria = sumatoria + numero

print()
print(sumatoria)
