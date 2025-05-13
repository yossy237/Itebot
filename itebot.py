from telegram import Update 
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler
from archivotron import busca_con_archivos  # <--- Importamos la función correcta
from dotenv import load_dotenv
import os

#TOKEN = "8062691778:AAF4oSo-s7TGAcKqHlGwT4324maFvittF5U"
load_dotenv() # This line brings all environment variable from .env int
token_telegram = os.environ['token']
app = Application.builder().token(token_telegram).build()

# Función para responder al comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy un bot que filtra palabras. ¡Escríbeme algo!")

# Función de Echo: Responde con el resultado de la búsqueda
async def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    palabras = user_text.split()  # Separar el texto en palabras

    # Filtrar cada palabra usando busca_con_archivos
    respuestas = []
    for palabra in palabras:
        resultado = busca_con_archivos(palabra)
        respuestas.append(f"{palabra}: {resultado}")

    # Responder al usuario con las respuestas
    await update.message.reply_text("\n".join(respuestas))

# Configuración del bot
app = Application.builder().token(token_telegram).build()

# Agregar manejadores (Handlers)
app.add_handler(CommandHandler("start", start))  # Maneja el comando /start
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Maneja cualquier mensaje de texto

# Iniciar el bot en modo polling (escucha mensajes constantemente)
print("Bot de Echo iniciado...")
app.run_polling()