from telegram import Bot
import os

TOKEN = os.environ.get('TOKEN')

bot = Bot(TOKEN)

url = 'https://python2022p.pythonanywhere.com/bot'

print(bot.set_webhook(url))
print(bot.get_webhook_info())