import telebot, os
from timeit import default_timer as timer
bot     = telebot.TeleBot("TOKEN")
ids     = open("ids.txt","r").readlines()
message = open("msg.txt","r").read()
i       = 0
F       = 0
T       = 0
os.system('clear')
start   = timer()
for Id in ids:
    i = i+1
    try:
        bot.send_message(Id,message)
        print(f"""
==================DONE==================
ID: {Id}
NUMBER: {i}/{len(ids)}
STATUS: Success

""")
        T = T+1
    except Exception as e:
        print(f"""
==================FAIL==================
ID {Id}
NUMBER: {i}/{len(ids)}
STATUS: Fail
{e}

""")
        F = F+1
end = timer()
ttt = end-start
print(f"""
==================BROD==================
BROD TO {len(ids)}
SUCCESS: {T}/{len(ids)}
FAIL: {F}/{len(ids)}
TIME: {ttt}""")
