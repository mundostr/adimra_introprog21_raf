# pip3 install pymysql o python -m pip install pymysql
# pip3 install sqlalchemy o python -m pip install sqlalchemy

# Librerías
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


# Definiciones
SERVIDOR = "pad19.com"
USUARIO = "adimra"
CLAVE = "adm2021"
BBDD = "adimra_introprog21"


# Funciones
def conectarMysql():
	motorMysql = create_engine(f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}/{BBDD}", pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False


# Main
if (__name__ == "__main__"):
	resultado = conectarMysql()

	if (resultado):
		print("Conectado a la bbdd, listo para consultas")
	else:
		print("Error al conectar con la bbdd")
