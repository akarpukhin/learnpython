import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot_v2.log'
                    )


def start_bot(bot, update):
    print(update)
    mytext = "Привет {}! Я простой бот и понимаю только команду {}".format(update.message.chat.first_name, '/start')

    update.message.reply_text(mytext)


def main():
    updtr = Updater("366340595:AAFyTYshBiFi9_ornCx2LnyDfl6sgI0Cmmg")

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()