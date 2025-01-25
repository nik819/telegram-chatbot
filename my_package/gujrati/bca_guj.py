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


async def bca_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("પ્રવેશ", callback_data='2.2.1.1.1'),
            InlineKeyboardButton("અભ્યાસક્રમ", callback_data='2.2.1.1.2')
        ],
        [
            InlineKeyboardButton("ફેકલ્ટી", callback_data='2.2.1.1.3'),
            InlineKeyboardButton("સુવિધાઓ", callback_data='2.2.1.1.4')
        ],
        [
            InlineKeyboardButton("પાછળ",callback_data="bca_back_guj"),
            InlineKeyboardButton("હોમ",callback_data="bca_home_guj")
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="બેચલર ઈન કોમ્પ્યુટર એપ્લિકેશન",reply_markup=reply_markup)

async def bca_admission_guj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_package/image/BCA_ADM.jpg', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ઇન્ટેક : 60 વિદ્યાર્થીઓ")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="સમયગાળો : 3 વર્ષ (છ સેમેસ્ટર)")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="પ્રવેશ માહિતી લિંક. https://gujaratvidyapith.org/dcs/bca.php")