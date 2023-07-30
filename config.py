from telebot.async_telebot import AsyncTeleBot
from Plugin.databesas import *




session_data = Session_databesas()
STATS = {"online":False}

bot = AsyncTeleBot("6615093788:AAHt8MENTCFljLaYTk4E4yBOkqQs00DxVZc")



temp_handler = {}

ADD_ACCONET_STATE = {
    'API_HASH_STATE':False,
    'API_ID_STATE':False,
    'CODE_STATE':False,
    'PHONE_STATE':False,
    'PASSORD_STATE':False
}



ADMINE_STATE = {'add_acconet':False,'add_username':False,'session_id':'session_1'}

