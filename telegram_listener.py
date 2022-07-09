import telebot

import config
from config import TOKEN
from twitter_sender import TwiAPI


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['status'])
def handle_status(message):
    bot.reply_to(message, 'Current status: I\'m alive!')


@bot.message_handler(commands=['send_tweet'])
def handle_send(message):
    api = TwiAPI()
    text = message.text[12:]
    if text == '' or text == None:
        response = 'Empty message'
    else:
        response = api.send_status(text)

    bot.reply_to(message, response)


@bot.message_handler(commands=['del_tweet'])
def handle_del(message):
    api = TwiAPI()
    id_str = int(message.text[11:])
    response = api.del_status(id_str)
    bot.reply_to(message, response)

    
bot.polling(none_stop=True)