import telebot, os, time
bot = telebot.TeleBot('TOKEN')
while True:
    os.system("wget https://cataas.com/cat  --output-document=cat.jpg")
    bot.send_photo(chat_id="@linux_nerdcat",photo=open('cat.jpg','rb'))
    time.sleep(60)
