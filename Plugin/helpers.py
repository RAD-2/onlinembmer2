from telebot.types import InlineKeyboardMarkup as Markup ,InlineKeyboardButton as Button,CallbackQuery
from telebot.types import InlineKeyboardMarkup  ,InlineKeyboardButton ,CallbackQuery

from config import *

bandstat = {
    True : '𝗕𝗔𝗡𝗗',
    False : '𝗡𝗢'
}
# KEyboard 
def HOME_KEYBOARD():
    keyboard = Markup()
    keyboard.add(Button('ACCONET STAT', callback_data='NOT'),Button(str(STATS['online']), callback_data='NOT'))
    keyboard.add(Button('START', callback_data='start_stat'),Button('STOP', callback_data='off_stat'))
    keyboard.add(Button('ADD ACCONET', callback_data='add_Acconet'),Button('SHOW ACCONET', callback_data='show_acconet'))
    return keyboard
def BACK_HOME_KEYBOARD():
    keyboard = Markup()
    keyboard.add(Button('BACK', callback_data='back'))
    return keyboard



def SHOW_ALL_SESSION():
    sessions = session_data.READ_SESSIONS()
    keyboard = InlineKeyboardMarkup(row_width=4)
    keyboard.add(
        InlineKeyboardButton("𝙄𝘿", callback_data="NOT"),
        InlineKeyboardButton("𝙉𝘼𝙈𝙀", callback_data="NOT"),
        InlineKeyboardButton("𝘽𝘼𝙉𝘿", callback_data="NOT"),
        InlineKeyboardButton("𝘿𝙀𝙇𝙀𝙏", callback_data="NOT"))

    if len(sessions['sessions']) != 0:
        for i in sessions['sessions']:
            session = sessions['sessions'][i]
            band = False if session['is_block'] == False or session['floodwait_block'] == False else True
            keyboard.add(
                InlineKeyboardButton(i.split('_')[1], callback_data="NOT"),
                InlineKeyboardButton(session['first_name'], url=f"t.me/{session['username']}"),
                InlineKeyboardButton(bandstat[band], callback_data=f"band_inf:{i}"),
                InlineKeyboardButton('𝙳𝙴𝙻𝙴𝚃', callback_data=f"del_ses:{i}"))

        
    elif len(sessions['sessions']) == 0:
        keyboard.add(InlineKeyboardButton("𝙉𝙊 𝘼𝘾𝘾𝙊𝙉𝙀𝙏", callback_data="barck"))

    keyboard.add(InlineKeyboardButton("•BACK ⌫", callback_data="back"))
    return keyboard
