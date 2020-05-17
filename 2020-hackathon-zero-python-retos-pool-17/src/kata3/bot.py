import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Bot configurado con BotFather
# Obtuve /token, /newbot = Hackathon name=rool_78_bot... t.me/rool_78_bot
# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return update.message.reply_text("Hola, rool_78_bot!")

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    return update.message.reply_text("Ayudame!")

def mayus(update, context):
    result = str(context.args[0])
    return update.message.reply_text(result.upper())

def alreves(update, context):
    msg = str(update.message.text)
    msg = msg[::-1]
    return context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1151787036:AAGiFzyi253o0qLEJfWNuqP6xt11ds7bcl0", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    #dp.add_handler(CommandHandler("", alreves))

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    echo_handler = MessageHandler(Filters.text & (~Filters.command), alreves)
    dp.add_handler(echo_handler)
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
