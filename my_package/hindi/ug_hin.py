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

async def ug_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("बी.सी.ए", callback_data='3.2.1.1'),
            InlineKeyboardButton("बी.ऐड", callback_data='3.2.1.2')
        ],
        [
            InlineKeyboardButton("बी.ऐड(हिन्दी)", callback_data='3.2.1.3'),
            InlineKeyboardButton("बी.ऐ(हिन्दी)", callback_data='3.2.1.4')
        ],
        [
            InlineKeyboardButton("बी.ऐ(इतिहास)", callback_data='3.2.1.5'),
            InlineKeyboardButton("बी.ऐ(गुजराती)", callback_data='3.2.1.6')
        ],
        [
            InlineKeyboardButton("बी.ऐ(अंग्रेज़ी)", callback_data='3.2.1.7'),
            InlineKeyboardButton("बी.एस.सी(माइक्रोबायोलोजी)", callback_data='3.2.1.8')
        ],
        [
            InlineKeyboardButton("बी वॉक- फूड प्रोसेस टेक्नोलॉजी", callback_data='3.2.1.9'),
            InlineKeyboardButton("बी वॉक - फैशन टेक्नोलॉजी और अपैरल डिजाइनिंग", callback_data='3.2.1.10')
        ],
        [
            InlineKeyboardButton("बी.ए.(अर्थशास्त्र)", callback_data='3.2.1.11'),
            InlineKeyboardButton("बी.ए.(समाजशास्त्र)", callback_data='3.2.1.12')
        ],
        [
            InlineKeyboardButton("ग्रामीण अध्ययन में स्नातक", callback_data='3.2.1.13'),
            InlineKeyboardButton("शारीरिक शिक्षा और खेल में स्नातक", callback_data='3.2.1.14')
        ],
        [
            InlineKeyboardButton("शारीरिक शिक्षा में स्नातक", callback_data='3.2.1.15'),
            InlineKeyboardButton("बी.लिब.आई.एससी.", callback_data='3.2.1.16')
        ],
        [
            InlineKeyboardButton("पीछे", callback_data='ug_back_hin')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="स्नातक",reply_markup=reply_markup)
