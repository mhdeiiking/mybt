import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5448584711:AAEJ_LUBZF-6HaWoLOkxMB0motL5h5fkDo8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def start(message):

    x = InlineKeyboardMarkup()

    a = InlineKeyboardButton("Dev", url="t.me/zdddu")

    b = InlineKeyboardButton("Channel", url="t.me/y88f8")

    x.add(a,b)

    bot.reply_to(message, "test", reply_markup=x)

    

print("[√] Your client has been started successfully")

bot.infinity_polling()

