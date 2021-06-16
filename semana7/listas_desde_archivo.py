# Generamos una lista vacía
mtrDatos = []

# Abrimos el archivo datos.txt para lectura (r)
# datos.txt en este caso se encuentra en el mismo directorio
archivoDatos = open("datos.txt", "r")
# Realizamos la lectura del archivo y separamos utilizando como referencia la coma
# De esta forma podemos tomar la cadena de texto del archivo y convertirla en items para agregar a mtrDatos
mtrDatos = archivoDatos.read().split(",")
archivoDatos.close()

# Con este mecanismo convertimos todos los items de la lista a enteros, para poder operar
for indice, item in enumerate(mtrDatos):
	mtrDatos[indice] = int(item)

print(mtrDatos)
