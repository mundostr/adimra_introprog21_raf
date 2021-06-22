# Los 4 modos más genéricos de apertura de archivos
# r -> read (para lectura)
# w -> write (para escritura desde inicio. Si el archivo no existe, lo crea)
# a -> append (para escritura, agregando contenidos)
# w+ -> lectura y escritura

# archivo = open(ARCHIVO_ORIGINAL, "r")
# listaRegistros = archivo.read().split(",")
# archivo.close()

# for indice, item in enumerate(listaRegistros):
# 	listaRegistros[indice] = int(item)

# # print(listaRegistros)

# archivo = open(ARCHIVO_CONVERTIDO, "w")
# for indice, item in enumerate(listaRegistros):
# 	archivo.write(str(listaRegistros[indice]) + "\n")
# archivo.close()

# print("Formato convertido")


RUTA_BASE = "semana8"
ARCHIVO_ORIGINAL = "ingresos_diarios_2020.txt"
ARCHIVO_CONVERTIDO = "ingresos_diarios_2020_saltos.txt"
ARCHIVO_JSON = "datos_clima_rafaela.json"
RUTA_ARCHIVO_CLIMA = f"{RUTA_BASE}/{ARCHIVO_JSON}"

import json

archivo = open(RUTA_ARCHIVO_CLIMA, "r")
datosClima = json.load(archivo)
archivo.close()

print(datosClima)
print(datosClima["hoy"])
print(datosClima["hoy"]["actual"])
