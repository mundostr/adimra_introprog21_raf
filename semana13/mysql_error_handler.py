# pip3 install pymysql o python -m pip install mymysql
# pip3 install sqlalchemy o python -m pip install sqlalchemy

# Librerías
import os
from dotenv.main import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
load_dotenv()


# Definiciones
MYSQL_SERVIDOR = os.getenv("MYSQL_SERVIDOR")
MYSQL_USUARIO = os.getenv("MYSQL_USUARIO")
MYSQL_CLAVE = os.getenv("MYSQL_CLAVE")
MYSQL_TABLA = "adimra_introprog21"


# Funciones
def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{MYSQL_USUARIO}:{MYSQL_CLAVE}@{MYSQL_SERVIDOR}/{MYSQL_TABLA}", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def main():
	conexion = conectarMysql()

	if (conexion):
		try:
			# registro = 1
			sql = f"SELECT * FROM clasificacion_f1 ORDER BY ptos DESC"
			resultado = conexion.execute(sql)
			
			for linea in resultado:
				print(linea)
		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			print(error)


# Main
if (__name__ == "__main__"):
	main()
