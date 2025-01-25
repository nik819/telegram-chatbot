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


async def pg_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("एम.सी.ए.", callback_data='3.2.2.1'),
            InlineKeyboardButton("एम.एस.डब्ल्यू", callback_data='3.2.2.2')
        ],
        [
            InlineKeyboardButton("एम.एड.", callback_data='3.2.2.3'),
            InlineKeyboardButton("एम.पी.एड.", callback_data='3.2.2.4')
        ],
        [
            InlineKeyboardButton("एम.पी.ई.एस", callback_data='3.2.2.5'),
            InlineKeyboardButton("एम.ए.", callback_data='3.2.2.6')
        ],
        [
            InlineKeyboardButton("एम.लिब", callback_data='3.2.2.7'),
            InlineKeyboardButton("एम.एस.सी - कीटाणु-विज्ञान", callback_data='3.2.2.8')
        ],
        [
            InlineKeyboardButton("एम.बी.ए.", callback_data='3.2.2.9'),
            InlineKeyboardButton("एम.एस.सी पर्यावरण विज्ञान और प्रौद्योगिकी में", callback_data='3.2.2.10')
        ],
        [
            InlineKeyboardButton("पीछे", callback_data='pg_back_hin')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="अनु-स्नातक",reply_markup=reply_markup)
