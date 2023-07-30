from config import *
from pyrogram.errors import FloodWait ,BadRequest ,NotAcceptable,Unauthorized,SessionPasswordNeeded, PhoneCodeInvalid, PasswordHashInvalid
from telebot.async_telebot import types
from pyrogram import Client
from Plugin.helpers import *





class ADD_SESSION_HANDLER:

    def __init__(self ,call : types.CallbackQuery):
        self.chat_id = call.message.chat.id
        self.message_id = call.message.id


        self.user_dict = {
            'API_HASH':None,
            'API_ID':None,
            'PHONE_NUMBER':None,
            'CODE_HASH':None,
            'CODE':None,
            'PASSURD':None
            }
     



    # START HANLDER 
    async def START(self, ):
        await bot.edit_message_text(text="𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚊𝚙𝚒_𝚑𝚊𝚜𝚑 𝚝𝚎𝚡𝚝 ." ,chat_id=self.chat_id ,
         message_id=self.message_id,reply_markup=BACK_HOME_KEYBOARD())
        ADD_ACCONET_STATE['API_HASH_STATE'] = True
        await self.API_HASH_HANDLER()
        
    async def API_HASH_HANDLER(self, ): # api_hash hanler
        @bot.message_handler(func=lambda hndler: ADD_ACCONET_STATE['API_HASH_STATE'] == True and ADMINE_STATE['add_acconet']  == True)
        async def API_HASH_HAND(message):
            self.user_dict['API_HASH'] = message.text
            ADD_ACCONET_STATE['API_HASH_STATE'] = False
            ADD_ACCONET_STATE['API_ID_STATE'] = True
            await bot.send_message(text='𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚊𝚙𝚒_𝚒𝚍 𝚗𝚞𝚖𝚋𝚎𝚛 .',chat_id=self.chat_id,reply_markup=BACK_HOME_KEYBOARD())
            await self.API_ID_HANDLER()

    async def API_ID_HANDLER(self, ): # api_id handler
        @bot.message_handler(func=lambda hndler: ADD_ACCONET_STATE['API_ID_STATE'] == True and ADMINE_STATE['add_acconet']  == True)
        async def API_ID_HAND(message):
            self.user_dict['API_ID'] = message.text
            ADD_ACCONET_STATE['API_ID_STATE'] = False
            ADD_ACCONET_STATE['PHONE_STATE'] = True
            await bot.send_message(text='𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚎𝚗𝚍 𝙿𝚑𝚘𝚗𝚎 𝙽𝚞𝚖𝚋𝚎𝚛 .',chat_id=self.chat_id,reply_markup=BACK_HOME_KEYBOARD())
            await self.PHONE_NUMBER()

    async def PHONE_NUMBER(self, ): # phone_number 
        @bot.message_handler(func=lambda hndler: ADD_ACCONET_STATE['PHONE_STATE'] == True and ADMINE_STATE['add_acconet']  == True)
        async def PHONE_NUMBER_HAND(message):
            self.user_dict['PHONE_NUMBER'] = message.text
            message_edit = await bot.send_message(text='𝙿𝚕𝚎𝚊𝚜𝚎 𝚆𝚒𝚝𝚎 𝙲𝚑𝚊𝚌𝚔 𝙸𝚗𝚏𝚘 .',chat_id=self.chat_id)
            try:
                if session_data.CHACHK_SESSION(self.user_dict['API_HASH'],self.user_dict['API_ID'],
                self.user_dict['PHONE_NUMBER']) == True:
                    # chack info from session 
                    self.client = Client('session' ,api_hash=self.user_dict["API_HASH"] ,
                    api_id=self.user_dict['API_ID'] ,in_memory=True) # start client pyrogram
                    # connect client 
                    await self.client.connect()
                    # send code from phone number
                    code_coinfig = await self.client.send_code(self.user_dict['PHONE_NUMBER'])
                    # get code hash 
                    self.user_dict['CODE_HASH'] = code_coinfig.phone_code_hash
                    # edit STATE
                    ADD_ACCONET_STATE['PHONE_STATE'] = False
                    ADD_ACCONET_STATE['CODE_STATE'] = True
                    await bot.edit_message_text(text="𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚎𝚗𝚍 𝚟𝚎𝚛𝚒𝚏𝚒𝚌𝚊𝚝𝚒𝚘𝚗 𝚌𝚘𝚍𝚎 ,𝚂𝚎𝚗𝚍 𝙵𝚛𝚘𝚖 𝙿𝚑𝚘𝚗𝚎 𝙽𝚞𝚖𝚋𝚎𝚛 .", chat_id=self.chat_id ,message_id=
                        message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                    # get coinfig code start
                    await self.COINFIG_CODE()
                else: 
                    await bot.edit_message_text(text="𝚃𝚑𝚎 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 𝚑𝚊𝚜 𝚊𝚕𝚛𝚎𝚊𝚍𝚢 𝚋𝚎𝚎𝚗 𝚊𝚍𝚍𝚎𝚍 .", chat_id=self.chat_id ,message_id=
                        message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                    ADD_ACCONET_STATE['PHONE_STATE'] = False
                    
            # FloodWait error : 420
            except FloodWait as Err:
                await bot.edit_message_text(text=f"𝙱𝙻𝙾𝙲𝙺 𝙰𝚌𝚌𝚘𝚗𝚎𝚝 𝚏𝚛𝚘𝚖 𝚂𝚒𝚐𝚗 𝚒𝚜  ❲ {Err.value} ❳ 𝚜𝚎𝚌𝚞𝚒𝚗𝚎𝚍 .", chat_id=self.chat_id ,message_id=
                    message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                ADD_ACCONET_STATE['PHONE_STATE'] = False
            # BadRequest error : 400
            except BadRequest as Err:
                # api_id/api_hash not faund
                if Err.ID == 'API_ID_INVALID':
                    await bot.edit_message_text(text="𝙴𝚛𝚛𝚘𝚛 𝙰𝙿𝙸_𝙷𝙰𝚂𝙷/𝙰𝙿𝙸_𝙸𝙳 𝙽𝚘𝚝 𝙵𝚊𝚞𝚗𝚎𝚍 .", chat_id=self.chat_id ,message_id=
                        message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                    ADD_ACCONET_STATE['PHONE_STATE'] = False
                # Phone Not Faunde
                elif Err.ID == 'PHONE_NUMBER_INVALID':
                    await bot.edit_message_text(text="𝙴𝚛𝚛𝚘𝚛 𝙿𝙷𝙾𝙽𝙴 𝙽𝚄𝙼𝙱𝙴𝚁 𝙽𝙾𝚃 𝙵𝙰𝚄𝙽𝙴𝙳 ,𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚎𝚗𝚍 𝙿𝚑𝚘𝚗𝚎 .", chat_id=self.chat_id ,message_id=
                        message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                else:
                    await bot.send_message(text=Err,chat_id=self.chat_id,reply_markup=BACK_HOME_KEYBOARD())
            except NotAcceptable as Err:
                if Err.ID == 'PHONE_NUMBER_INVALID':
                    await bot.edit_message_text(text="𝙴𝚛𝚛𝚘𝚛 𝙿𝙷𝙾𝙽𝙴 𝙽𝚄𝙼𝙱𝙴𝚁 𝙽𝙾𝚃 𝙵𝙰𝚄𝙽𝙴𝙳 ,𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚎𝚗𝚍 𝙿𝚑𝚘𝚗𝚎 .", chat_id=self.chat_id ,message_id=
                    message_edit.message_id,reply_markup=BACK_HOME_KEYBOARD())
                else:
                    await bot.send_message(text=Err,chat_id=self.chat_id,reply_markup=BACK_HOME_KEYBOARD())
    
    async def COINFIG_CODE(self, ): # get coinfig code 
        @bot.message_handler(func=lambda hndler: ADD_ACCONET_STATE['CODE_STATE']== True and ADMINE_STATE['add_acconet']  == True)
        async def COINFIG_CODE_HAND(message):
            self.user_dict['CODE'] = message.text
      
            message_edit_wite = await bot.send_message(message.chat.id ,
                text='𝚆𝚒𝚝𝚑 𝚂𝚒𝚐𝚗 𝙰𝚌𝚌𝚘𝚗𝚎𝚝 .' )
            try:
                # singe acconet
                await self.client.sign_in(phone_number=self.user_dict['PHONE_NUMBER'] 
                ,phone_code_hash=self.user_dict['CODE_HASH'] ,phone_code=self.user_dict['CODE'])
                await self.ADD_SESSION(message_edit_wite)

            except SessionPasswordNeeded:
                await bot.edit_message_text(text="𝙸𝚏 𝚢𝚘𝚞𝚛 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 𝚒𝚜 𝚕𝚘𝚌𝚔𝚎𝚍, 𝚋𝚞𝚝 𝚢𝚘𝚞 𝚑𝚊𝚟𝚎 𝚎𝚗𝚝𝚎𝚛𝚎𝚍 𝚊 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍, 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚝𝚑𝚎 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 .", chat_id=self.chat_id ,message_id=
                    message_edit_wite.message_id,reply_markup=BACK_HOME_KEYBOARD())
                ADD_ACCONET_STATE['CODE_STATE'] = False
                ADD_ACCONET_STATE['PASSORD_STATE'] = True
                await self.PASSURD_CACK()

            except PhoneCodeInvalid:
                await bot.edit_message_text(text="𝚃𝚑𝚎 𝚟𝚎𝚛𝚒𝚏𝚒𝚌𝚊𝚝𝚒𝚘𝚗 𝚌𝚘𝚍𝚎 𝚒𝚜 𝚒𝚗𝚌𝚘𝚛𝚛𝚎𝚌𝚝. 𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚊 𝚟𝚊𝚕𝚒𝚍 𝚌𝚘𝚍𝚎 .", chat_id=self.chat_id ,message_id=
                    message_edit_wite.message_id,reply_markup=BACK_HOME_KEYBOARD())


    
     
    async def PASSURD_CACK(self, ): # get coinfig code 
        @bot.message_handler(func=lambda hndler: ADD_ACCONET_STATE['PASSORD_STATE'] == True and ADMINE_STATE['add_acconet']  == True)
        async def PASSURD_HAND(message):
            PASSURD = message.text
            self.user_dict['PASSURD'] = PASSURD
            message_edit_wite = await bot.send_message(message.chat.id ,
                    text='𝚆𝚒𝚝𝚑 Cahck passurd' )
            try:
                await self.client.check_password(PASSURD)
                ADD_ACCONET_STATE['PASSORD_STATE'] = False
                await self.ADD_SESSION(message_edit_wite)

            except PasswordHashInvalid:
                await bot.edit_message_text(text="𝚃𝚑𝚎 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝚒𝚜 𝚒𝚗𝚌𝚘𝚛𝚛𝚎𝚌𝚝. 𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚗𝚍 𝚊 𝚟𝚊𝚕𝚒𝚍 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 .", chat_id=self.chat_id ,message_id=
                    message_edit_wite.message_id,reply_markup=BACK_HOME_KEYBOARD())

        
    async def ADD_SESSION(self, message_edit_wite):
        # export session_string
        self.session_string = await self.client.export_session_string()
        # send message from acconet
        await self.client.send_message('me', 'done sessions')
        ACCONET_INFO = await self.client.get_me()
        # edit state 
        ADD_ACCONET_STATE['CODE_STATE'] = False
        # add session data
        session_data.ADD_SESSION(self.user_dict['API_HASH'],self.user_dict['API_ID'],
            self.user_dict['PHONE_NUMBER'],
            self.session_string,ACCONET_INFO.first_name ,ACCONET_INFO.id,ACCONET_INFO.username)
        # edit message 
        await bot.edit_message_text(text="𝙳𝚘𝚗𝚎 𝙰𝚍𝚍 𝙰𝚌𝚘𝚗𝚎𝚝", chat_id=self.chat_id ,message_id=
            message_edit_wite.message_id,reply_markup=BACK_HOME_KEYBOARD())









