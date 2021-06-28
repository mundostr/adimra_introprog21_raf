# LIBRERIAS
# La librería requests, nos permite realizar solicitudes remotas vía protocolo http o https
import requests


# DEFINICIONES
URL_HISTORICO_SMN = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"
URL_API_CLIMA = "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&appid=bbbe84df6ab458740a22a2e0a1eb7663"



# FUNCIONES
def recuperarUrl(destino, formato):
	# Se utilizar el método get de requests para obtener el contenido remoto
	consulta = requests.get(destino)

	# Si status_code es 200, significa que la solicitud fue exitosa,
	# entonces se realiza la conversión del contenido según lo que se indique en formato y se retorna el resultado.
	# Si es 429 significa que hemos excedido el límite de solicitudes por minuto, sino se trata de otro error que
	# estará detallado en consulta.message.
	if (consulta):
		if (consulta.status_code == 200):
			if (formato == "original"):
				return consulta.content
			elif (formato == "texto"):
				return consulta.text
			elif (formato == "json"):
				return consulta.json()
			else:
				return False
		elif (consulta.status_code == 429):
			print ("Demasiadas solicitudes por minuto")
			return False
		else:
			print(f"ERROR al recuperar contenidos: {consulta.message}")
			return False
	else:
		print("ERRROR general en la solicitud")

def main():
	# Se realiza la llamada a la función recuperarUlr, pasándole como argumentos la url y el formato.
	infoClima = recuperarUrl(URL_API_CLIMA, "json")
	if (infoClima):
		# Se extraen los datos de interés desde el json y se muestran
		temperatura = f'{infoClima["list"][0]["main"]["temp"]:.1f}'
		humedad = infoClima["list"][0]["main"]["humidity"]
		presion = infoClima["list"][0]["main"]["pressure"]
		
		print(f"Temperatura: {temperatura} C")
		print(f"Humedad: {humedad} %")
		print(f"Presión: {presion} hPa")


# PRINCIPAL
# Controlamos si el script está siendo ejecutado de manera directa o no, si es de manera directa,
# iniciamos llamando a la función main()
if (__name__ == "__main__"):
	main()
