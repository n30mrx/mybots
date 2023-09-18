#!/usr/bin/python3
import telebot, requests
from telebot import types

bot    = telebot.TeleBot("6110163742:AAEOL9RWspDFdZZkat1TbcMyz_uXAmrzsPY")
devurl = types.InlineKeyboardButton(text="Mr. X      -      المطور", url="https://t.me/linux_nerd")
key = types.InlineKeyboardMarkup(row_width=3)
button_Meme = types.InlineKeyboardButton(text="Gimme meme", callback_data="gimme")
key.add(button_Meme)
key.row(devurl)

def getBool(inp):
    if inp == "true":
        return True
    elif inp == "false":
        return False
    
def memeCaption(reqJ):
    url = reqJ['url']
    nsfw = getBool(reqJ['nsfw'])
    title = reqJ['title']
    author = reqJ['author']
    link = reqJ['postLink']
    ups = reqJ['ups']
    subreddit = reqJ['subreddit']
    nsfwText = ""
    if nsfw:
        nsfwText = "⚠️WARNING⚠️ ⚠\n️⚠️NSFW MEME AHEAD ⚠️⚠️\n\n"
    message =  f"{nsfwText}💬[{title}]({link})💬\n⬇️{ups}⬆️\n\n👥[subreddit link](https://reddit.com/r/{subreddit})👥\n✏️By: [{author}](https://reddit.com/u/{author})✏️\n"
    return message
    

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(chat_id=msg.chat.id,  text="Hey!\nYou can use this bot to get a random meme from reddit!", reply_markup=key)

@bot.callback_query_handler(func=lambda query:query.data == "gimme")
def gimme(query):
    req = requests.get("https://meme-api.com/gimme")
    reqJ = req.json()
    url = reqJ['url']
    nsfw  = getBool(reqJ['nsfw'])
    message = memeCaption(reqJ)
    print(message)
    bot.send_photo(chat_id=query.from_user.id, photo=url, has_spoiler=nsfw,caption=message,parse_mode="MarkDown",reply_markup=key)
    bot.answer_callback_query(query.id,"Here! enjoy your meme",False)
bot.infinity_polling()