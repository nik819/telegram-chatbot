import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://github.com/python-telegram-bot/python-telegram-bot/tree/v{TG_VER}/examples"
#     )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def pgdca_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("પ્રવેશ", callback_data='2.2.4.3.1'),
            InlineKeyboardButton("અભ્યાસક્રમ", callback_data='2.2.4.3.2')
        ],
        [
            InlineKeyboardButton("ફેકલ્ટી", callback_data='2.2.4.3.3'),
            InlineKeyboardButton("સુવિધાઓ", callback_data='2.2.4.3.4')
        ],
        [
            InlineKeyboardButton("પાછળ",callback_data="pgdca_back_guj"),
            InlineKeyboardButton("હોમ",callback_data="pgdca_home_guj")
        ]
    ]  
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="કોમ્પ્યુટર એપ્લિકેશનમાં પોસ્ટ ગ્રેજ્યુએટ ડિપ્લોમા",reply_markup=reply_markup)

async def pgdca_admission_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_package/image/MCA_ADM.jpg', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="P.G.D.C.A. 1 વર્ષનો પોસ્ટ ગ્રેજ્યુએટ ડિપ્લોમા પ્રોગ્રામ (બે સેમેસ્ટર) છે. P.G.D.C.A.નું એક મૌન લક્ષણ પ્રોગ્રામ એ બે થી ત્રણ મહિનાનો ઔદ્યોગિક પ્રોજેક્ટ છે. આનાથી વિદ્યાર્થીઓ આગળના વાહક માટે તેમની કુશળતાને સારી રીતે ગોઠવી શકે છે. આ કાર્યક્રમને કેટલીક અગ્રણી સંસ્થાઓ તરફથી સક્રિય સહકાર મળી રહ્યો છે. ઘણીવાર પ્રોજેક્ટ તાલીમાર્થીઓને તેમના પ્રોજેક્ટ સફળતાપૂર્વક પૂર્ણ થયા પછી યજમાન સંસ્થાઓ દ્વારા નોકરીની ઓફર કરવામાં આવે છે.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ઇન્ટેક : 45 વિદ્યાર્થીઓ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="સમયગાળો : 1 વર્ષ (બે સેમેસ્ટર)")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્રવેશ પ્રક્રિયા લિંક : https://www.gujaratvidyapith.org/admission/index.php")