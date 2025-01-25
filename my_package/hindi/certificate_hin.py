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


async def certificate_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("हल्का संगीत", callback_data='3.2.3.1'),
            InlineKeyboardButton("छंद शास्र", callback_data='3.2.3.2')
        ],
        [
            InlineKeyboardButton("कला और शिल्प", callback_data='3.2.3.3'),
            InlineKeyboardButton("डेटा साइंस ब्रोशर", callback_data='3.2.3.4')
        ],
        [
            InlineKeyboardButton("कंप्यूटर हार्डवेयर और नेटवर्क प्रौद्योगिकी में प्रमाणपत्र", callback_data='3.2.3.5'),
            InlineKeyboardButton("सोलर फोटोवोल्टिक तकनीशियन (सीएसपीटी) में प्रमाणपत्र", callback_data='3.2.3.6')
        ],
        [
            InlineKeyboardButton("पीछे", callback_data='certi_back_in')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रमाणपत्र : ",reply_markup=reply_markup)
