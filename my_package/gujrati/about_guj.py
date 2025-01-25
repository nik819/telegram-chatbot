
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


async def about_us_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("ઝાંખી", callback_data='2.1.1'),
            InlineKeyboardButton("ઇતિહાસ", callback_data='2.1.2')
        ],
        [
            InlineKeyboardButton("સામાન્ય માહિતી", callback_data='2.1.3'),
            InlineKeyboardButton("મૂલ્યો", callback_data='2.1.4')
        ],
        [
            InlineKeyboardButton("પ્રતીક", callback_data='2.1.5'),
            InlineKeyboardButton("વાર્ષિક હિસાબ", callback_data='2.1.6')
        ],
        [
            InlineKeyboardButton("IIQA ઉપક્રમ", callback_data='2.1.7')
        ],
        [
            InlineKeyboardButton("પાછળ", callback_data='about_back_guj')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ગુજરાત વિદ્યાપીઠ વિશે",reply_markup=reply_markup)