import logging

from telegram import __version__ as TG_VER

from my_package.English.bca import bca, bca_admission

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


async def ug(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("BCA", callback_data='1.2.1.1'),
            InlineKeyboardButton("B.Ed", callback_data='1.2.1.2')
        ],
        [
            InlineKeyboardButton("B.Ed (Hindi)", callback_data='1.2.1.3'),
            InlineKeyboardButton("B.A.(Hindi)", callback_data='1.2.1.4')
        ],
        [
            InlineKeyboardButton("B.A.(History)", callback_data='1.2.1.5'),
            InlineKeyboardButton("B.A.(Gujarati)", callback_data='1.2.1.6')
        ],
        [
            InlineKeyboardButton("B.A.(English)", callback_data='1.2.1.7'),
            InlineKeyboardButton("B.Sc.(Micro)", callback_data='1.2.1.8')
        ],
        [
            InlineKeyboardButton("B.Voc. - Food Process", callback_data='1.2.1.9'),
            InlineKeyboardButton("B.Voc. - Fashion Tech", callback_data='1.2.1.10')
        ],
        [
            InlineKeyboardButton("B.A.(Economic)", callback_data='1.2.1.11'),
            InlineKeyboardButton("B.A.(Sociology)", callback_data='1.2.1.12')
        ],
        [
            InlineKeyboardButton("B.R.S.", callback_data='1.2.1.13'),
            InlineKeyboardButton("BPES", callback_data='1.2.1.14')
        ],
        [
            InlineKeyboardButton("B.P.Ed.", callback_data='1.2.1.15'),
            InlineKeyboardButton("B.Lib.I.Sc.", callback_data='1.2.1.16')
        ],
        [
            InlineKeyboardButton("BACK", callback_data='0.1.2.1')
        ]
    ]

    query = update.callback_query

    await query.answer()

    # await query.edit_message_text(text=f"Selected option: {query.data}")
    button_choice=query.data
    print(type(button_choice))

    # if button_choice=='1.2.1.1':
    #     await bca(update,context)
    

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Graduation :",reply_markup=reply_markup)
