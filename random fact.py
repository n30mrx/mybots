# Random facts telegram bot
# Copyright (C) 2023  Mr.X
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
print("""    Random facts  Copyright (C) 2023  Mr.X
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions;""")
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