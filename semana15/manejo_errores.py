def contar_digitos(nro):
	digitos = 0
	while (nro != 0):
		nro //= 10
		digitos += 1
	return digitos


def main():
	id_validado = False

	while not(id_validado):
		id = input("ID Usuario (solo números, max 8 dígitos): ")
		
		try:
			id = int(id)
			if (contar_digitos(id) <= 8):
				id_validado = True
				break
			print("Max 8 dígitos")
		except:
			print("ID no válido")

	print(id)


if (__name__ == "__main__"):
	main()