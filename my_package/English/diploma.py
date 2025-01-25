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


async def diploma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Yogik Art and Science", callback_data='1.2.4.1'),
            InlineKeyboardButton("Audio Visual Production (TV)", callback_data='1.2.4.2')
        ],
        [
            InlineKeyboardButton("P.G.D.C.A.", callback_data='1.2.4.3'),
            InlineKeyboardButton("P.G.D.C.H.N.", callback_data='1.2.4.4')
        ],
        [
            InlineKeyboardButton("Prayojanmulak Hindi", callback_data='1.2.4.5'),
            InlineKeyboardButton("Translation Hindi", callback_data='1.2.4.6')
        ],
        [
            InlineKeyboardButton("BACK", callback_data='diploma_back')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Diploma Cources : ",reply_markup=reply_markup)
