def controlParametros(params: list):
	params2 = params[:]
	# params.append(16)
	# params.append(200)
	print("params2:", params2)

def controlParametro(param: int):
	param = 15


def main():
	param = 16
	params = (23, 15, 100, 1)

	print("params antes:", params)
	controlParametros(params)
	print("params despues", params)

	print()

	print ("param antes:", param)
	controlParametro(param)
	print ("param despues:", param)


if (__name__ == "__main__"):
	main()
