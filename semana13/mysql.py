# pip3 install pymysql o python -m pip install pymysql
# pip3 install sqlalchemy o python -m pip install sqlalchemy
# recordar inicializar el archivo .env con las variables de entorno necesarias

# Librerías
import os
from dotenv.main import load_dotenv
from sqlalchemy import create_engine
load_dotenv()


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


# Main
def main():
	conexion = conectarMysql()

	if (conexion):
		print("Sistema conectado")
		conexion.close()

# Main
if (__name__ == "__main__"):
	main()
