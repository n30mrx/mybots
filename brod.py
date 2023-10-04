license = """telegram bot brodcast script
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
from timeit import default_timer as timer
from telebot.util import antiflood


def Brod(bot,message,ids):
    

    i ,F ,T = 0,0,0
    start   = timer()

    brodMM  = bot.send_message(
        chat_id=message.from_user.id,
        text=f"""Brodcast started:
Amount  : {len(ids)}
Success : {T}/{T+F}  -  0%
Fail    : {F}/{T+F}  -  0%
Progress: 0%"""
    )

    for Id in ids:
        i = i+1
        try:
            antiflood(
                bot.copy_message,
                Id,message.chat.id,
                message.id
                )
            # bot.copy_message(
            #     chat_id=Id,
            #     message_id=message.id,
            #     from_chat_id=message.chat.id,
            # )
            
            T = T+1
        except Exception as e:
            F = F+1
        if i%2==0:
            bot.edit_message_text(
                    chat_id=brodMM.chat.id,
                    message_id=brodMM.id,
                    text=f"""Brodcast started:
    Amount  : {len(ids)}
    Success : {T}/{T+F}  -  {round((T/(T+F))*100,2)}%
    Fail    : {F}/{T+F}  -  {round((F/(T+F))*100,2)}%
    Progress: {round(((T+F)/len(ids))*100,2)}%"""
                )
    end = timer()
    ttt = end-start
    bot.edit_message_text(
                chat_id=brodMM.chat.id,
                message_id=brodMM.id,
                text=f"""Brodcast ended:
Amount  : {len(ids)}
Success : {T}/{T+F}  -  {round((T/(T+F))*100,2)}%
Fail    : {F}/{T+F}  -  {round((F/(T+F))*100,2)}%
Progress: {round(((T+F)/len(ids))*100,2)}%
Time    : {round(ttt/60,1)} Minute"""
            )
