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


async def mca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Admission", callback_data='1.2.2.1.1'),
            InlineKeyboardButton("Syllabus", callback_data='1.2.2.1.2')
        ],
        [
            InlineKeyboardButton("Faculty", callback_data='1.2.2.1.3'),
            InlineKeyboardButton("Facilities", callback_data='1.2.2.1.4')
        ],
        [
            InlineKeyboardButton("Placement", callback_data='1.2.2.1.5')            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="MASTER IN COMPUTER APPLICATION",reply_markup=reply_markup)

async def mca_admission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fees", callback_data='1.2.2.1.1.1'),
            InlineKeyboardButton("Eligibility", callback_data='1.2.2.1.1.2')
        ],
        [
            InlineKeyboardButton("Intake", callback_data='1.2.2.1.1.3'),
            InlineKeyboardButton("Duration", callback_data='1.2.2.1.1.4')
        ],
        [
            InlineKeyboardButton("BACK", callback_data="mca_back"),
            InlineKeyboardButton("HOME", callback_data="mca_home")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_package/image/MCA_ADM.jpg', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Admission Process Link. https://www.gujaratvidyapith.org/admission/index.php",reply_markup=reply_markup)