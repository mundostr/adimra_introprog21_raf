class Circulo:
	PI = 3.141592654

	@staticmethod
	def superficie(r):
		return Circulo.PI * r * r
	
	@staticmethod
	def perimetro(r):
		return 2 * Circulo.PI * r


if (__name__ == '__main__'):
	print(Circulo.superficie(16))
	print(Circulo.perimetro(16))
