from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint
from token1 import TOKEN

bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# pip install python-telegram-bot==13.14
# Updater → Dispatсher → Handlers → start → wait_for_the_end
# Updater - взаимодействие между клиентом и сервером
# Dispatсher - отвечает за вызов обработчика сообщений
# Handlers - обработчики сообщений


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет!")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "это бот")


def roll(update, context):
    context.bot.send_message(update.effective_chat.id, text=str(randint(1, 6)))


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
roll_handler = CommandHandler('roll', roll)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(roll_handler)
updater.start_polling()
updater.idle()