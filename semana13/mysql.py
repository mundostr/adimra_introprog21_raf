# pip3 install pymysql o python -m pip install pymysql
# pip3 install sqlalchemy o python -m pip install sqlalchemy
# recordar inicializar el archivo .env con las variables de entorno necesarias

# Librerías
import os
from dotenv.main import load_dotenv
from sqlalchemy import create_engine
load_dotenv()
import random as rnd
from datetime import datetime


# Definiciones
MYSQL_SERVIDOR = os.getenv("MYSQL_SERVIDOR")
MYSQL_USUARIO = os.getenv("MYSQL_USUARIO")
MYSQL_CLAVE = os.getenv("MYSQL_CLAVE")
MYSQL_BBDD = "adimra_introprog21"


# Funciones
def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{MYSQL_USUARIO}:{MYSQL_CLAVE}@{MYSQL_SERVIDOR}/{MYSQL_BBDD}", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def solicitarRegistros(conn):
	# sql = "SELECT * FROM clasificacion_f1 ORDER BY puntos DESC"
	# sql = "SELECT * FROM sensor_presion ORDER BY timestamp ASC"
	# sql = "SELECT MAX(promedio) FROM sensor_presion"
	sql = "SELECT * FROM sensor_presion ORDER BY promedio ASC"
	resultado = conn.execute(sql)
	for registro in resultado:
		print(registro)
		# timestampEs = datetime.strftime(registro[2], "%d-%m-%Y a las %H:%M")
		# print(registro[2])
		# print(timestampEs)

def insertarRegistroSensor(conn, idUsuario, promedio):
	sql = f"INSERT INTO sensor_presion (id_usuario, promedio) VALUES({idUsuario}, {promedio})"
	print(sql)
	return conn.execute(sql)

def actualizarRegistroSensor(conn, idRegistro, promedio):
	sql = f"UPDATE sensor_presion SET promedio = {promedio} WHERE id = {idRegistro}"
	print(sql)
	return conn.execute(sql)

def borrarRegistroSensor(conn, idRegistro):
	sql = f"DELETE FROM sensor_presion WHERE id = {idRegistro}"
	print(sql)
	return conn.execute(sql)

def main():
	conexion = conectarMysql()

	if (conexion):
		solicitarRegistros(conexion)

		# promedio = 0
		# muestras = 50
		# idUsuario = 33
		# for i in range(muestras):
		# 	promedio = promedio + rnd.randint(100, 200) / muestras
		# insertarRegistroSensor(conexion, idUsuario, promedio)
		
		# actualizarRegistroSensor(conexion, 2, 140.3)

		# borrarRegistroSensor(conexion, 5)

		conexion.close()


# Main
if (__name__ == "__main__"):
	main()
