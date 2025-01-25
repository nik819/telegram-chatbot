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


async def certificate_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("લાઇટ મ્યુઝિક", callback_data='2.2.3.1'),
            InlineKeyboardButton("છંદ શાસ્ત્ર", callback_data='2.2.3.2')
        ],
        [
            InlineKeyboardButton("કલા અને હસ્તકલા", callback_data='2.2.3.3'),
            InlineKeyboardButton("ડેટા સાયન્સનું બ્રોશર", callback_data='2.2.3.4')
        ],
        [
            InlineKeyboardButton("કમ્પ્યુટર હાર્ડવેર અને નેટવર્ક ટેકનોલોજીમાં પ્રમાણપત્ર", callback_data='2.2.3.5'),
            InlineKeyboardButton("સોલર ફોટોવોલ્ટિક ટેકનિશિયન (CSPT) માં પ્રમાણપત્ર", callback_data='2.2.3.6')
        ],
        [
            InlineKeyboardButton("પાછળ", callback_data='certi_back_guj')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્રમાણપત્ર : ",reply_markup=reply_markup)
