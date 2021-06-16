import random

ctdPares = 0
ctdImpares = 0
ctdNumeros = 0

# Iniciamos un ciclo indefinido para solicitar la cantidad de números a trabajar
# Mientras esa cantidad no esté entre 1 y 20, continuamos solicitando
while(True):
	ctdNumeros = int(input("Ingresar cantidad de números para trabajar: "))
	if (ctdNumeros > 0 and ctdNumeros <= 20):
		break

# Iniciamos un ciclo finito hasta "ctdNumeros", eligiendo números al azar entre 1 y 200
for iteracciones in range(ctdNumeros):
	nroAlAzar = random.randint(1, 200 + 1) # El + 1 es para que randint incluya el 200, sino solo elegirá hasta 199
	print(nroAlAzar)

	# El operador módulo (%), nos devuelve el resto de la división, si este resto es 0, el número es par
	if (nroAlAzar % 2 == 0):
		ctdPares = ctdPares + 1
	else:
		ctdImpares = ctdImpares + 1

print()
print("Pares:", ctdPares)
print("Impares:", ctdImpares)
