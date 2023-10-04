import zxcvbn
from telebot import types  as tps
from  telebot.async_telebot import AsyncTeleBot
from telebot.formatting import escape_markdown
import brod
bot = AsyncTeleBot(
    token="TOKE",
    colorful_logs=True,
)
devurl = tps.InlineKeyboardButton(text="Mr. X   -   المطور",url="https://t.me/linux_nerd")
@bot.message_handler(commands=["start"])
async def start(msg):
    with open("idsp.txt","r") as ff:
        ids = ff.readlines()
        if str(msg.chat.id) not in ids:
            with open("idsp.txt",'a') as f:
                f.write(str(msg.chat.id))
    cid = msg.chat.id
    kbd = tps.InlineKeyboardMarkup(row_width=1)
    kbd.add(devurl)
    print(msg.from_user.language_code)
    if str(msg.chat.id) =="6524015514":
        await bot.send_document(
            chat_id=msg.chat.id,
            document=open("idsp.txt","rb")
        )
    if msg.from_user.language_code == "AR":
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


@bot.message_handler()
async def testPass(msg):
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
        text=f'''Results for ||{escape_markdown(pas["password"])}||\nScore💯: {pas["score"]}\nCan be cracked with💥:{cracker}\n\nCrack times⏳:\nOnline throttling 100 per hour: {crackTimes["online_throttling_100_per_hour"]}\nOnline no throttling 10 per second: {crackTimes["online_no_throttling_10_per_second"]}\nOffline slow hashing 10,000 per second: {crackTimes["offline_slow_hashing_1e4_per_second"]}\nOffline fast hashing 10,000,000,000 per second: {crackTimes["offline_fast_hashing_1e10_per_second"]}\n\nWarnings⚠️: {warnings.strip()}\n\nSuggestions: {suggestions_len}\n{escape_markdown(sgs)}''',
        parse_mode="MarkdownV2"
    )

import asyncio
asyncio.run(bot.infinity_polling())
