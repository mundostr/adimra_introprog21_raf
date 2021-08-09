# Como sabemos, Python no cuenta con un mecanismo explícito para declarar constantes
# Esta es una alternativa, utilizando la librería enum

from enum import Enum

class Constantes(Enum):
	ANCHO = 640
	ALTO = 360
	MODO = "YOUTUBE"

# Podemos acceder a los valores mediante value
print(Constantes.ANCHO.value)
print(Constantes.ANCHO.value)
print(Constantes.MODO.value)

# Si intentamos modificar un valor, se generará un error
# Constantes.ANCHO.value = 800
