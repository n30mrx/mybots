import telebot
import qrcode
bot = telebot.TeleBot("TOKEN")

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
