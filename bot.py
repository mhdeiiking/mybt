import telebot

bot = telebot.TeleBot("5448584711:AAEDCP1Glg7fjIhBWnaROKsKBWQHY-nJWGw")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,f"- هلاو")
bot.infinity_polling()
