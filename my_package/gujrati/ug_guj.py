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


async def ug_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("બીસીએ", callback_data='2.2.1.1'),
            InlineKeyboardButton("બી.એડ", callback_data='2.2.1.2')
        ],
        [
            InlineKeyboardButton("બી.એડ (હિન્દી)", callback_data='2.2.1.3'),
            InlineKeyboardButton("બી.એ(હિન્દી)", callback_data='2.2.1.4')
        ],
        [
            InlineKeyboardButton("બી.એ(ઇતિહાસ)", callback_data='2.2.1.5'),
            InlineKeyboardButton("બી.એ(ગુજરાતી)", callback_data='2.2.1.6')
        ],
        [
            InlineKeyboardButton("બી.એ(અંગ્રેજી)", callback_data='2.2.1.7'),
            InlineKeyboardButton("બી.એસસી.(સૂક્ષ્મ)", callback_data='2.2.1.8')
        ],
        [
            InlineKeyboardButton("બી વોક- ફૂડ પ્રોસેસ ટેકનોલોજી", callback_data='2.2.1.9'),
            InlineKeyboardButton("બી વોક- ફેશન ટેકનોલોજી અને એપેરલ ડિઝાઇનિંગ", callback_data='2.2.1.10')
        ],
        [
            InlineKeyboardButton("બી.એ.(આર્થિક)", callback_data='2.2.1.11'),
            InlineKeyboardButton("બી.એ.(સમાજશાસ્ત્ર)", callback_data='2.2.1.12')
        ],
        [
            InlineKeyboardButton("ગ્રામીણ અભ્યાસમાં સ્નાતક", callback_data='2.2.1.13'),
            InlineKeyboardButton("શારીરિક શિક્ષણ અને રમતગમતમાં સ્નાતક", callback_data='2.2.1.14')
        ],
        [
            InlineKeyboardButton("શારીરિક શિક્ષણમાં સ્નાતક", callback_data='2.2.1.15'),
            InlineKeyboardButton("B.Lib.I.Sc.", callback_data='2.2.1.16')
        ],
        [
            InlineKeyboardButton("પાછળ",callback_data="ug_back_guj")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ગ્રેજ્યુએશન : ",reply_markup=reply_markup)
