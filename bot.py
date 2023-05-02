from telegram.ext import Updater, CommandHandler
import os

from main import start

TOKEN = os.environ.get('TOKEN')

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
