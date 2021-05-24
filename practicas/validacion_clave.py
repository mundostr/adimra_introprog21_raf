MAX_INTENTOS = 3

clInterna = "123Abcde"
usuarioValidado = False

for intentos in range(MAX_INTENTOS):
	clave = input("Ingresar clave: ")
	if (clave == clInterna):
		usuarioValidado = True
		print("Clave correcta")
		break
	else:
		print("Clave incorrecta")

if(usuarioValidado == True):
	print("SISTEMA OK")
else:
	print("SISTEMA BLOQUEADO")
