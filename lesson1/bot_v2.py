from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater)

def main():
    updtr = Updater("366340595:AAFyTYshBiFi9_ornCx2LnyDfl6sgI0Cmmg")

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

    updtr.start_polling()
    updtr.idle()


if __name == "__main__":
    main()