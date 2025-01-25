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


async def cspt_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("પ્રવેશ", callback_data='2.2.3.6.1'),
            InlineKeyboardButton("અભ્યાસક્રમ", callback_data='2.2.3.6.2')
        ],
        [
            InlineKeyboardButton("સુવિધાઓ", callback_data='2.2.3.6.4')
        ],
        [
            InlineKeyboardButton("પાછળ",callback_data="cspt_back_guj"),
            InlineKeyboardButton("હોમ",callback_data="cspt_home_guj")
        ]
    ]  

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="સોલર ફોટોવોલ્ટિક ટેકનિશિયન (CSPT) માં પ્રમાણપત્ર",reply_markup=reply_markup)

async def cspt_admission_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="સોલર ફોટોવોલ્ટિક ટેકનિશિયન (CSPT) માં પ્રમાણપત્ર : ત્રણ મહિનાનો પાર્ટ-ટાઇમ CSPT એ ફાઉન્ડેશન કોર્સ છે જેનો હેતુ સોલાર ફોટોવોલ્ટિક પ્રોફેશનલ્સ દ્વારા જરૂરી ટેકનિક અને સ્વભાવ આપવાનો છે. આ ઉદ્દેશ્યો સિદ્ધ કરવા માટે, અમે તેમને સોલર પીવી જાળવણી અને ઇન્સ્ટોલેશનની સઘન અને વ્યાપક તાલીમ આપીએ છીએ. આ કાર્યક્રમ વિદ્યાર્થીઓને નોકરીઓ ઓફર કરીને કેટલીક અગ્રણી સંસ્થાઓ તરફથી સક્રિય સહકાર પ્રાપ્ત કરી રહ્યો છે.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ઇન્ટેક : 20 વિદ્યાર્થીઓ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="સમયગાળો : ત્રણ મહિના")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્રવેશ પ્રક્રિયા લિંક. : https://www.gujaratvidyapith.org/admission/index.php")