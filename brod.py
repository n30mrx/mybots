import telebot, os
bot     = telebot.TeleBot("TOKEN")
ids     = open("ids.txt","r").readlines()
message = open("msg.txt","r").read()
i       = 0
f       = 0
t       = 0
os.system('clear')
for id in ids:
    i = i+1
    try:
        bot.send_message(id,message)
        print(f"==================DONE==================\nID: {id}\nNUMBER: {i}/{len(ids)}\nSTATUS: Success\n\n")
        t = t+1
    except Exception as e:
        print(f"==================FAIL==================\nID {id}\nNUMBER: {i}/{len(ids)}\nSTATUS: Fail\n{e}\n\n")
        f = f+1
print(f"==================BROD==================\nBROD TO {len(ids)}\nSUCCESS: {t}/{len(ids)}\nFAIL: {f}/{len(ids)}\n")