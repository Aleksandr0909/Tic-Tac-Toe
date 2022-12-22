import telebot
from bot2 import get_price
import config

bot = telebot.TeleBot(config.TOKEN_3)




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message,
                 f"Welcome,this bot gets the value of any cryptocurrency! To start, use the /exchange command! ")


def complete_exchange(message: telebot.types.Message):
    convert, convert_to = message.text.split(' ')
    price = get_price(convert, convert_to)
    bot.send_message(message.chat.id, f'{convert_to} to {convert} = {price}')


@bot.message_handler(commands=['exchange'])
def exchange(message: telebot.types.Message):
    bot.send_message(message.chat.id,
                     'select the currency to convert and currency to exchange. Example: "BTC USD" - converts BTC to USD')
    bot.register_next_step_handler(message, complete_exchange)


bot.infinity_polling()

# Имя бота Cryptocurrency Exchanger
