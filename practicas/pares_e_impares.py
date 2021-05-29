import random

ctdPares = 0
ctdImpares = 0
ctdNumeros = 0

while(True): # Indefinido
	ctdNumeros = int(input("Ingresar cantidad de números para trabajar: "))
	if (ctdNumeros > 0 and ctdNumeros <= 20):
		break

for iteracciones in range(ctdNumeros): # Finito
	nroAlAzar = random.randint(1, 200)
	print(nroAlAzar)

	if (nroAlAzar % 2 == 0):
		ctdPares = ctdPares + 1
	else:
		ctdImpares = ctdImpares + 1

print()
print("Pares:", ctdPares)
print("Impares:", ctdImpares)
