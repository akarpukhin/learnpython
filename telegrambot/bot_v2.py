import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from datetime import datetime
import settings
import ephem
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "telegrambot/logs/bot_v2.log")

if not os.path.exists(LOG_FILE):
    os.mkdir(os.path.dirname(LOG_FILE))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=LOG_FILE
                    )


def start_bot(bot, update):
    mytext = "Привет {}! Я простой бот и понимаю только команду {}".format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)


def plannet(bot, update, args):
    get_command = update.message.text
    logging.info('Была вызвана такая команда: \"{get_command}\", пользователем \"{user}\"'.
        format(get_command=get_command, user=update.message.chat.username))
    if not args:
        update.message.reply_text(
"""Вы не ввели планету!
---
Пример: /planet Mars""")
    elif re.match('[A-Za-z]', args[0]):
        planet = args[0].capitalize()
        planet = getattr(ephem, planet)
        planet = planet(datetime.now().strftime("%Y/%m/%d"))
        where_planet = ephem.constellation(planet)
        update.message.reply_text(where_planet)
    else:
        update.message.reply_text(
"""WARNING!
Что-то пошло не так...
Вы ввели команду: {get_text}
---
Пример: /planet mars""".format(get_text=get_command))


def wordcount(bot, update, args):
    pass


def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)


def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(CommandHandler("planet", plannet, pass_args=True))
    updtr.dispatcher.add_handler(CommandHandler("wordcount", wordcount, pass_args=True))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()