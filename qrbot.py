# Qr code telegram bot
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
import telebot
import qrcode
bot = telebot.TeleBot("TOKEN")
print("""    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions;""")

def crqr(message):
    if len(message.text)>0:
        img = qrcode.make(message.text)
        img.save(f"qr{message.chat.id}{message.id}.png")
        bot.send_document(message.chat.id,open(f"qr{message.chat.id}{message.id}.png","rb"))

# start 
@bot.message_handler(commands=['start'])
def startt(message):
    bot.reply_to(message,"Hi!\nYou can use this bot to create QRcodes for any string, just send me a link or any tryp of text and I will turn it into a QRcode!\n\nMade by: @linux_nerd Idea by: @iqsys\nMy channel: @n30arch")

# create qr
@bot.message_handler()
def crr(message):
    crqr(message)




bot.infinity_polling()
