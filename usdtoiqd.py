import telebot, requests, logging
from telebot import types

logger = telebot.logging
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot("TOKEN") # TOKEN

#  Start meaages
startAR    = "اهلا! يمكنك استعمال هذا البوت لتحويل العملات من الدينار العراقي الى الدولار الامريكي والعكس!"
startEN    = "Hi! you can use this bot to convert currencies from IQD to USD and vice versa!"

#  USD -> IQD
usdtoiqdAR = "ارسل الكمية بالدولار بالارقام الانكليزية من دون علامة الدولار"
usdtoiqdEN = "Send the amount in usd without the dollar sign"

# IQD -> USD
iqdtousdAR = "ارسل الكمية بالدينار بالارقام الانكليزية"
iqdtousdEN = "Send the amount in iqd"

# Buttons
keyboard   = types.InlineKeyboardMarkup(row_width=2)
usdtoiqd   = types.InlineKeyboardButton("USD → IQD", callback_data="usdtoiqd")
iqdtousd   = types.InlineKeyboardButton("IQD → USD", callback_data="iqdtousd")
devurl     = types.InlineKeyboardButton("Mr. X - المطور",  url="https://t.me/linux_nerd") # Set your name and username here
keyboard.row(usdtoiqd,iqdtousd)
keyboard.row(devurl)


# usdtoiqd function
def usdtoiqdF(message):
    messageT = message.text
    # check if the message is a valid number
    if messageT.isdigit():
        iqd = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/iqd.min.json").json()["iqd"]
        usd = float(messageT)
        converted = round(usd*iqd, 1)
        bot.reply_to(message,f"{messageT}USD ⟶ {converted}IQD")
    else:
        wrongM = bot.reply_to(message, "Sorry, but the amount you entered is invalid\nعذراً, الكمية المدخلة غير صحيحة")
        bot.register_next_step_handler(wrongM, usdtoiqdF)

# iqdtousd function
def iqdtousdF(message):
    messageT = message.text
    # check if the message is a valid number
    if messageT.isdigit():
        usd = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/iqd/usd.min.json").json()["usd"]
        iqd = float(messageT)
        converted = round(usd*iqd, 1)
        bot.reply_to(message,f"{messageT}IQD ⟶ {converted}USD")
    else:
        wrongM = bot.reply_to(message, "Sorry, but the amount you entered is invalid\nعذراً, الكمية المدخلة غير صحيحة")
        bot.register_next_step_handler(wrongM, iqdtousdF)


# start message handler
@bot.message_handler(commands=['start'])
def start(message):
    startMSG = bot.send_message(message.chat.id, f"{startEN}\n{startAR}", reply_markup=keyboard)
    

# callback handler
@bot.callback_query_handler(func=lambda call: True)
def callBackHandler(calldata):
    
    # USD -> IQD
    if calldata.data == "usdtoiqd":
        usdtoiqdM = bot.send_message(calldata.message.chat.id, f"{usdtoiqdEN}\n{usdtoiqdAR}")
        bot.register_next_step_handler(usdtoiqdM, usdtoiqdF)

    #  IQD -> USD
    elif calldata.data == "iqdtousd":
        iqdtousdM = bot.send_message(calldata.message.chat.id, f"{iqdtousdEN}\n{iqdtousdAR}")
        bot.register_next_step_handler(iqdtousdM, iqdtousdF)


# start the bot
bot.infinity_polling()