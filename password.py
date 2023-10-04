license = """zxcvbn password tester telegram bot
Copyright (C) 2023  Mr.X
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
print(license)
import zxcvbn
import asyncio
import os
from telebot import types  as tps
from  telebot.async_telebot import AsyncTeleBot
from telebot.formatting import escape_markdown

# set token as env var
bot = AsyncTeleBot(
    token=str(os.getenv("TOKEN")),
    colorful_logs=True,
)
devurl = tps.InlineKeyboardButton(text="Mr. X   -   المطور",url="https://t.me/linux_nerd")
giturl = tps.InlineKeyboardButton(text="Source code   -   كود البوت",url="https://github.com/n30mrx/mybots/tree/main/password.py")
srcsnd = tps.InlineKeyboardButton(text="Send python file",callback_data="sendsrc")
@bot.message_handler(commands=["start"])
async def start(msg):
    with open("idsp.txt","r") as ff:
        ids = ff.readlines()
        if str(msg.chat.id) not in ids:
            with open("idsp.txt",'a') as f:
                f.write(f"\n{str(msg.chat.id)}")
    cid = msg.chat.id
    kbd = tps.InlineKeyboardMarkup(row_width=1)
    kbd.add(devurl)
    kbd.add(giturl)
    kbd.add(srcsnd)
    print(msg.from_user.language_code)
    if str(msg.chat.id) =="6524015514":
        await bot.send_document(
            chat_id=msg.chat.id,
            document=open("idsp.txt","rb")
        )
    if msg.from_user.language_code == "ar":
        await bot.send_message(
            chat_id=cid,
            text="اهلا بك في بوت اختبار كلمات المرور, ارسل كلمة مرور ليتم اختبار قوتها",
            reply_markup=kbd
        )
    else:
        await bot.send_message(
            chat_id=cid,
            text="Hi! Welcome to PasswordTester bot. \nsend me a password and I will tell you how strong it is",
            reply_markup=kbd
        )

def score(scr):
    match scr:
        case 1:
            return "poor"
        case 2:
            return "weak"
        case 3:
            return "good"
        case 4:
            return "excelent"



@bot.message_handler(regexp= r'^[a-zA-Z0-9\W_]+$')
async def testPass(msg):
    if any([" "in msg.text, "\t"in msg.text]):
        pass
    else:
        pas = zxcvbn.zxcvbn(msg.text)
        cid = msg.chat.id
        warnings = "none"if  len(pas["feedback"]["warning"])==0 else escape_markdown(pas["feedback"]["warning"])
        suggestions_len = "none"if  len(pas["feedback"]["suggestions"])==0 else len(pas["feedback"]["suggestions"])
        suggestions = pas["feedback"]["suggestions"]
        sgs = "\n".join(suggestions)
        cracker = pas["sequence"][0]["pattern"]
        crackTimes = pas["crack_times_display"]
        await bot.send_message(
            chat_id=cid,
            reply_to_message_id=msg.id,
            text=f'''Results for ||{escape_markdown(pas["password"])}||\nScore💯: {score(int(pas["score"]))}\nCan be cracked with💥:{cracker}\n\nCrack times⏳:\nOnline throttling 100 per hour: {crackTimes["online_throttling_100_per_hour"]}\nOnline no throttling 10 per second: {crackTimes["online_no_throttling_10_per_second"]}\nOffline slow hashing 10,000 per second: {crackTimes["offline_slow_hashing_1e4_per_second"]}\nOffline fast hashing 10,000,000,000 per second: {crackTimes["offline_fast_hashing_1e10_per_second"]}\n\nWarnings⚠️: {warnings.strip()}\n\nSuggestions: {suggestions_len}\n{escape_markdown(sgs)}''',
            parse_mode="MarkdownV2",
            protect_content=True,
        )

@bot.callback_query_handler(func=lambda call:call.data=="sendsrc")
async def sendsrc(call):
    kbd = tps.InlineKeyboardMarkup(row_width=1)
    kbd.add(devurl)
    kbd.add(giturl)
    with open("password.py","rb") as ff:
        await bot.send_document(
            chat_id=call.message.chat.id,
            document=ff,
            reply_markup=kbd,
            caption=f"Bot's source code, by @linux_nerd"
        )
        await bot.answer_callback_query(
            callback_query_id=call.id
        )


asyncio.run(bot.infinity_polling())
