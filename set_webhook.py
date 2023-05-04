from telegram import Bot
import os

TOKEN = '6157245486:AAG2GbeqAuhCRMuGL2vtwx6OaSaegVyghAs'

bot = Bot(TOKEN)

url = 'https://DarmayedNarkosh.pythonanywhere.com/bot'

print(bot.set_webhook(url))
# print(bot.delete_webhook())
print(bot.get_webhook_info())