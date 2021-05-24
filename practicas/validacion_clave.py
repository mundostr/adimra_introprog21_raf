MAX_INTENTOS = 3

clInterna = "123Abcde"
usuarioValidado = False

for intentos in range(MAX_INTENTOS): # solo permitimos MAX_INTENTOS intentos
	clave = input("Ingresar clave: ")
	if (clave == clInterna):
		usuarioValidado = True # usuarioValidado es en este caso un flag o indicador verdadero / falso
		print("Clave correcta")
		break
	else:
		print("Clave incorrecta")

if(usuarioValidado == True):
	print("SISTEMA OK")
else:
	print("SISTEMA BLOQUEADO")
