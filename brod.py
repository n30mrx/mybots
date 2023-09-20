from timeit import default_timer as timer


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
            bot.copy_message(
                chat_id=Id,
                message_id=message.id,
                from_chat_id=message.chat.id,
            )
            
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
