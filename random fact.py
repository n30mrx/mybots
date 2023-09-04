import telebot, requests
from telebot import types
from googletrans import Translator
bot = telebot.TeleBot("TOKEN")


# Buttons
devurl     = types.InlineKeyboardButton("Mr. X - المطور",  url="https://t.me/linux_nerd") # Set your name and username here
gimmefact  = types.InlineKeyboardButton("Gimme fact", callback_data="gimmef")
keyboard   = types.InlineKeyboardMarkup(row_width=2)
keyboard.row(gimmefact)
keyboard.add(devurl)


# Start message
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Hi!\nThis bot can give you a random useless fact!\nClick the button below to get a random fact :)",reply_markup=keyboard)

# Button callback handler
@bot.callback_query_handler(func=lambda call:True)
def gimmef(call):
    fact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random").json()["text"]
    datat = Translator().translate(fact,dest="ar")
    bot.send_message(chat_id=call.message.chat.id, text=datat, reply_markup=keyboard)
    return

bot.infinity_polling()