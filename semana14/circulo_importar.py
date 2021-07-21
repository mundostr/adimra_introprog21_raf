# Ejemplo de importación de clase específica
# Si se utilizan subdirectorios, se necesita el archivo de inicialización __init__.py
# Simplemente crear en el subdirectorio (semana14 en este caso), un archivo vacío con nombre __init__.py
from circulo import Circulo

if (__name__ == '__main__'):
	# Observar que estamos utilizando de manera directa la clase importada
	# y la llamada a sus métodos (perimetro y superficie), sin haber instanciado un objeto de tipo Circulo.
	# Podemos hacer ésto, debido a que ambos métodos están declarados como estáticos (ver circulo.py).
	# Otro aspecto de este tipo de métodos es que no pueden modificar estados ni de objetos ni de la propia clase.
	print(Circulo.perimetro(12))
	print(Circulo.superficie(14))
