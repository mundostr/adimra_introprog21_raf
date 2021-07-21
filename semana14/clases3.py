# Librerías


# Definiciones
# Clase muy sencilla y general (Mascota), solo recibe en su constructor un atributo (nombre)
# y cuenta con un único método (mostrarNombre)
class Mascota:
	def __init__(self, nombre):
		self.nombre = nombre
	
	def mostrarNombre(self):
		print(f"La mascota es {self.nombre}")


# Otra clase sencilla (Perro), que HEREDA de Mascota (observar que se le pasa Mascota como parámetro).
# De esta forma, cualquier instancia de Perro, podrá llamar al método ladrar o a mostrarNombre, ya que
# este último método se encuentra definido en su clase padre (parent).
class Perro(Mascota):
	def ladrar(self):
		print(f"{self.nombre} ladra")

# Idem Perro
class Gato(Mascota):
	def maullar(self):
		print("Maullido")

# Idem Perro
class Pajaro(Mascota):
	def cantar(self):
		print("Canto")


# Main
def main():
	# Instanciamos objetos a través de las clases hijo (child), es decir,
	# Perro, Gato o Pajaro, cada una tiene un método propio, solo disponible para esa clase,
	# pero las 3 pueden utilizar el método mostrarNombre declarado en su parent.
	perro = Perro("Batuque")
	perro.mostrarNombre()
	perro.ladrar()

	# gato = Gato("Felpudo")
	# gato.mostrarNombre()
	# gato.maullar()

	# canario = Pajaro("Corbata")
	# canario.mostrarNombre()
	# canario.cantar()

if __name__ == '__main__':
	main()
