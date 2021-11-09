import telegram, logging
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters)

import constants, telegramCommands
 

def telegramMessage(update, context):
    text_content = update.message.text
    userID = update.message.chat_id

    #l = logicClass.logic()
    response = "hola"

    update.message.reply_text(response)

def responseTelegram():
    bot = telegram.Bot(token=constants.BOT_TOKEN)
    print(bot.get_me())

    updater = Updater(token=constants.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # commands handlers
    start_handler = CommandHandler('start', telegramCommands.start)
    help_handler = CommandHandler('help', telegramCommands.help)

    # add commands handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    # add messages handlers
    dispatcher.add_handler(MessageHandler(Filters.text, telegramMessage))

    # start the Bot
    updater.start_polling()

if __name__ == '__main__':
    responseTelegram()
