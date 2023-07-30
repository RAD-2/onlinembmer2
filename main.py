from config import *
import threading
import asyncio
from pyrogram import Client
from Plugin.add_acconet_handler import *
from Plugin.helpers import *


async def TRHID_ON_MEM(session_id : str):
    sessions = session_data.READ_SESSIONS()['sessions']
    session = sessions[session_id]['session']
    if STATS["online"] == False:
        print(f'STOP STATE SESSION {session_id}')
        return
    async with Client('::memeory::', session_string=session) as app:
        await app.send_message('me', 'START THRI')
        while STATS["online"] == True:
            await asyncio.sleep(7)
            print(session_id)


def START_THRIDE(session : str):
    asyncio.run(TRHID_ON_MEM(session))

async def ONLINE_STAT(session : str): # PIN USER
    NEW_THRID  = threading.Thread(target=START_THRIDE, args=(session,))
    NEW_THRID.start()


@bot.message_handler(commands=['start'])
async def START_BOT(message):
    await bot.send_message(message.chat.id,text='START OLINE MEMBERS .',reply_markup=HOME_KEYBOARD())


@bot.callback_query_handler(func=lambda c: c.data == "start_stat")
async def CALL_START(call : CallbackQuery):
    
    message_edit = await bot.edit_message_text(text=f'START ONLINE STAT ( 0/{str(session_data.GET_SESSION_COUNT())} )...',chat_id=call.message.chat.id,message_id=call.message.message_id)
    sessions = session_data.READ_SESSIONS()['sessions']
    STATS["online"] = True
    STAT_count  = 0 
    for session in sessions:
        STAT_count+=1
        await bot.edit_message_text(text=f'START ONLINE STAT  ( {STAT_count }/{str(session_data.GET_SESSION_COUNT())}...',chat_id=call.message.chat.id,message_id=message_edit.message_id)
        await ONLINE_STAT(session)
        print(f'[INFO] STRAT THRID {session}')
    
    await bot.edit_message_text(text=f'DONE START ALL STST ( {STAT_count } )',chat_id=call.message.chat.id,message_id=message_edit.message_id)
    await asyncio.sleep(2)
    await bot.edit_message_text(text='START OLINE MEMBERS .',reply_markup=HOME_KEYBOARD(),chat_id=call.message.chat.id,message_id=message_edit.message_id)

@bot.callback_query_handler(func=lambda c: c.data == "off_stat")
async def CALL_START(call : CallbackQuery):
    STATS["online"] = False
    message_edit = await bot.edit_message_text(text=f'Done Stop All Stat',chat_id=call.message.chat.id,message_id=call.message.message_id)
    await asyncio.sleep(2)
    await bot.edit_message_text(text='START OLINE MEMBERS .',reply_markup=HOME_KEYBOARD(),chat_id=call.message.chat.id,message_id=message_edit.message_id)



@bot.callback_query_handler(func=lambda c: c.data == "add_Acconet")
async def CALL_START(call : CallbackQuery):
    ADMINE_STATE['add_acconet'] = True
    hand =  ADD_SESSION_HANDLER(call)
    await hand.START()

@bot.callback_query_handler(func=lambda c: c.data == "show_acconet")
async def CALL_START(call : CallbackQuery):
    await bot.edit_message_text(text='THIS ALL ACCONET ',reply_markup=SHOW_ALL_SESSION(),chat_id=call.message.chat.id,message_id=call.message.message_id)



@bot.callback_query_handler(func=lambda c: c.data == "back")
async def CALL_START(call : CallbackQuery):
    await bot.edit_message_text(text='START OLINE MEMBERS .',reply_markup=HOME_KEYBOARD(),chat_id=call.message.chat.id,message_id=call.message.message_id)
    ADMINE_STATE['add_acconet'] = False
    ADMINE_STATE['add_username'] = False
    ADD_ACCONET_STATE['API_HASH_STATE'] = False
    ADD_ACCONET_STATE['API_ID_STATE'] = False
    ADD_ACCONET_STATE['CODE_STATE'] = False
    ADD_ACCONET_STATE['PHONE_STATE'] = False
    ADD_ACCONET_STATE['PASSORD_STATE'] = False
            






asyncio.run(bot.polling())