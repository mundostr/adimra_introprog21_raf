# La librería re permite trabajar con Expresiones Regulares (Regular Expressions o Regex)
# Las expresiones regulares permiten armar cadenas de caracteres para especificar patrones de búsqueda.
# Este tipo de herramienta es muy utilizada en el ambito de los diferentes lenguajes.
import re

# En este caso tenemos necesidad de cargar datos desde un archivo local, recorrerlos y obtener de ellos
# un fragmento de datos específicos, pero a diferencia de casos anteriores, el formato de este archivo
# no es homogéneo, lo cual complica más la búsqueda si se realiza manualmente. En este tipo de situaciones
# las expresiones regulares son realmente muy cómodas
archivo = open("e:/estadisticas_clima.txt", "r")
lista = archivo.readlines()

for index, linea in enumerate(lista):
	# Con esta expresión regular, buscamos una línea específica que comience con SAUCE VIEJO AERO,
	# contenga luego un tabulador y una P mayúscula.
	if (re.match("^SAUCE VIEJO AERO\\tP", linea)):
		datos = linea.removesuffix("\n").split("\t")

dic = { "Aeropuerto": datos[0], "Tipo registro": datos[1], "datos": [datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11], datos[12], datos[13]] }

print(dic)

dic["datos"] = [float(item) for item in dic["datos"]]

print(dic)
