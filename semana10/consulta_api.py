# Ejemplo de consulta remota directa a https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt
# para procesar y obtener datos del Aeropuerto de Sauce Viejo, sin necesidad de tener el archivo grabado localmente.

# DEFINICIONES
import re # para manejo de expresiones regulares
import requests as req # para manejo de solicitudes remotas

RUTA_API = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"
# Las expresiones regulares (re, regex) nos permiten buscar coincidencias de contenidos de manera muy eficiente
EXPRESION_REGULAR = "^SAUCE VIEJO AERO\\tTemperatura mínima \\("


# FUNCIONES
def filtrarInfoRemota(resultado, formato, separador, expresion):
	# Toma el resultado de la consulta remota como texto, y lo separa de acuerdo a "separador" para insertarlo en una lista
	lista = resultado.text.split(separador)

	for linea in lista:
		# Recorre la lista buscando una coincidencia con la expresión regular "expresion"
		if (re.match(expresion, linea)):
			# Si la encuentra, remueve el \r\n y separa el texto en una nueva lista, por tabulador (\t)
			datos = linea.removesuffix("\r").removesuffix("\n").split("\t")
			# Quita los 2 primeros items (que son ubicación y tipo de dato), para retornar solo los valores
			datos.pop(0)
			datos.pop(0)
	
	if (formato == "texto"):
		return datos
	elif (formato == "numerico"):
		# Notación alternativa con map y función lambda para iterar la lista y convertir los items a coma flotante
		return list(map(lambda item: float(item), datos))
	else:
		return False

def main():
	# "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&APPID=bbbe84df6ab458740a22a2e0a1eb7663"
	# "https://httpbin.org/delay/1"
	consultaRemota = req.get(RUTA_API)
	resultado = filtrarInfoRemota(consultaRemota, "numerico", "\n", EXPRESION_REGULAR)
	print(resultado)


# PRINCIPAL
# Si el script es llamado de forma directa, se ejecuta main()
if __name__ == '__main__':
	main()
