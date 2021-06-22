# Apertura del archivo local en modo lectura
archivo = open("estadisticas_clima.txt", "r")
lineas = archivo.readlines()

contador = 0
lineaPrecipitacion = ""
# Iteracción manual de la lista "lineas", separándola por tabulador (\t) y buscando SAUCE VIEJO AERO en el primer item
# También podrían utilizarse expresiones regulares para encontrar la coincidencia de manera más eficiente.
for linea in (lineas):
	partesLinea = linea.split("\t")
	if (partesLinea[0] == "SAUCE VIEJO AERO"):
		contador += 1
		if (contador == 7):
			lineaPrecipitacion = linea

lineaPrecipitacion = lineaPrecipitacion.removesuffix("\n")
datosPrecipitacion = lineaPrecipitacion.split("\t")

datosFinalesPrecipitacion = []
for index, item in enumerate(datosPrecipitacion):
	if(index > 1):
		datosFinalesPrecipitacion.append(float(item))

datosFinalesPrecipitacion.sort()

print(f"Sauce Viejo, mayor precipitación media período 1981-2010: {datosFinalesPrecipitacion[-1]}")
print(f"Sauce Viejo, menor precipitación media período 1981-2010: {datosFinalesPrecipitacion[0]}")
