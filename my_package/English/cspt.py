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


async def cspt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Admission", callback_data='1.2.3.6.1'),
            InlineKeyboardButton("Syllabus", callback_data='1.2.3.6.2')
        ],
        [
            InlineKeyboardButton("Facilities", callback_data='1.2.3.6.4')
        ],
        [
            InlineKeyboardButton("BACK", callback_data="cspt_back"),
            InlineKeyboardButton("HOME", callback_data="cspt_home")
        ]
    ]  
    
    query = update.callback_query
    await query.answer()

    # await query.edit_message_text(text=f"Selected option: {query.data}")
    button_choice=query.data
    print(type(button_choice))

    # if button_choice=='1.2.1.1.1':
    #      await context.bot.send_message(chat_id=update.effective_chat.id, text="Admission Link : https://gujaratvidyapith.org/dcs/bca.php")
    # if button_choice=='1.2.1.1.2':
    #      await context.bot.send_message(chat_id=update.effective_chat.id, text="Syllabus : ")
    # if button_choice=='1.2.1.1.3':
    #      await context.bot.send_message(chat_id=update.effective_chat.id, text="Faculty : ")
    # if button_choice=='1.2.1.1.4':
    #      await context.bot.send_message(chat_id=update.effective_chat.id, text="Facilities :")

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Certificate in Solar Photovoltic Technician (CSPT)",reply_markup=reply_markup)

async def cspt_admission(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Certificate in Solar Photovoltic Technician (CSPT) : The three month part-time CSPT is foundation course aimed at imparting technique and temperament required by the Solar Photovoltic professionals. To accomplish this objectives, we are given them an intensive and comprehensive training in Solar PV maintenance and installation. The programme has been receiving active cooperation from some leading organizations by offering jobs to students.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="INTAKE : 20 Students")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="DURATION : Three Months")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Admission Process Link. https://www.gujaratvidyapith.org/admission/index.php")