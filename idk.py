# telegram bot
# Copyright (C) 2023  Mr.X, tshreeb
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
print("""    telegram bot  Copyright (C) 2023  Mr.X and tshreeb
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions;""")
import telebot
import requests
from telebot import types
from openpyxl import load_workbook

id = '0'
token = '-7hiM3AK9r2KEEpuzawam8'
bot = telebot.TeleBot(token)

o = 0

@bot.message_handler(commands=['start'])
def phone(message):
    key = types.InlineKeyboardMarkup()
    key.row_width = 2
    btnn = types.InlineKeyboardButton(text="- Dev", url="t.me/huks3")
    btn = types.InlineKeyboardButton(text="- واتساب .", callback_data="s")
    key.add(btn, btnn)
    rp = open(f"baned.txt").read()
    uu = str(message.from_user.id)
    
    if message.from_user.id == int(id):
        pp = open("baned.txt", "r")
        o = len(pp.readlines())
        bot.reply_to(message, f'اهلا بك ايها المطور\nعدد الموجودين في البوت {o}', reply_markup=key)
        
    elif not uu in rp:
        bot.reply_to(message, '- اهلا بك مجددًا اختر من تحت ماذا تريد .', reply_markup=key)
        
    else:
        pass

@bot.callback_query_handler(func=lambda m: True)
def qu(call):
    if call.data == 'wa':
        h = bot.send_message(call.message.chat.id, '- ارسل الاسم الآن .')
        bot.register_next_step_handler(h, b3)



def maysan(message):
    bot.send_message(message.chat.id, f"- يتم الان محاوله العثور على العائلة .. قد ياخذ بعض الوقت")
    wb = load_workbook("daddy.xlsx", read_only=True)
    ws = wb.active
    
    for row in ws.rows:
        name = f"{message.text}"
        
        if str(name.split()[0]) in str(f"{row[3].value}"):
            ae = f"{row[3].value} {row[4].value} {row[5].value} {row[7].value}".replace("„", "")
            
            if name == ae:
                bot.reply_to(message, f"تم العثور على الشخص .. يتم الان جلب عائلتة .")
                idF = f'{row[1].value}'.replace("„", "")
                
                d = 0
                for i in ws.rows:
                    if idF in str(f"{i[1].value}"):
                        d += 1
                        k = f"""
- الاسم : {i[3].value} {i[4].value} {i[5].value} {i[7].value}   .
- العائلة : {i[1].value} .
                        """.replace("„", "")
                        
                        bot.send_message(message.chat.id, k)
                    
                    if d >= 2:
                        if idF in str(f"{i[1].value}"):
                            pass
                        else:
                            break

bot.infinity_polling()