import aiml
import logging
#import glob, os, psutil, sys, subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#chat_id = CHAT_ID  # telegram chat_id (user or group)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("I'm a bot, please talk to me!\n"
                                "/matricula - Take a snapshot and send it: uses fswebcam to take a picture and immediately send it to the Telegram chat.\n"
                                "/conversa - Start motion surveillance: start the Motion software with the personalised configuration file\n"
                                "/stopmotion - Stop motion surveillance: stop the Motion software with proc.kill()\n"
                                "/checkmotion - Check if motion surveillance is on: check from ps if the Motion software is running\n"
                                "/sendlast - Send last picture taken by motion surveillance: pictures are taken during the motion detection, the last one saved in the /pics folder is sent via Telegram\n"
                                "/cleanpics - Delete all pictures taken by motion surveillance: this delete all the .jpg files in the pics directory.")


def dialog(update, context):
    """Echo the user message."""
    bot = aiml.Kernel()
    bot.learn('./bot-start.xml')
    bot.respond('INITIALIZING')
    update.message.reply_text(bot.respond(update.message.text))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    
    updater = Updater("1373542959:AAF56dUyZ6yN16tl1tWxKiYSr_ckf1546ko")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, dialog))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

#--------------------------------------------------

# import aiml

# bot = aiml.Kernel()
# bot.learn('/home/kamila/Documentos/chatbot_AIML/conversa.xml')

# print(bot.respond("OLA ASSISTENTE"))
# while True:
#     r = input("Aluno ->")
#     r = bot.respond(r).split("/n")
#     print("Assistente ->")
#     for i in r:
#         print(i)
