# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# Librerías
import os
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from dotenv.main import load_dotenv
import requests as sr
load_dotenv()


# Globales
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(TELEGRAM_TOKEN)


# Funciones
def devolverInfo(update, context):
	# context.bot.send_message(chat_id=update.effective_chat.id, text="Más info sobre librería Pandas: https://www.youtube.com/watch?v=8ASjvOIyyl8")
	consulta = sr.get("https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&APPID=bbbe84df6ab458740a22a2e0a1eb7663")
	if (consulta.status_code == 200):
		consultaJson = consulta.json()
		temperatura = consultaJson["list"][0]["main"]["temp"]
		presion = consultaJson["list"][0]["main"]["pressure"]
		humedad = consultaJson["list"][0]["main"]["humidity"]
		cadena = f"CLIMA RAFAELA 04ago21 18:49\nTmp: {temperatura} C\nPresión: {presion} hPa\nHumedad: {humedad} %"
		context.bot.send_message(chat_id=update.effective_chat.id, text=cadena)


def gestionarBot():
	updater = Updater(TELEGRAM_TOKEN, use_context=True)
	dispatcher = updater.dispatcher
	comando1 = CommandHandler("clima", devolverInfo)
	dispatcher.add_handler(comando1)	
	print("Gestor bot activo")

	updater.start_polling()
	updater.idle()

def main():
	gestionarBot()


# Main
if (__name__ == "__main__"):
	main()
