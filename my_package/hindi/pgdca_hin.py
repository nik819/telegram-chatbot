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


async def pgdca_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("प्रवेश", callback_data='3.2.4.3.1'),
            InlineKeyboardButton("पाठ्यक्रम", callback_data='3.2.4.3.2')
        ],
        [
            InlineKeyboardButton("शिक्षक", callback_data='3.2.4.3.3'),
            InlineKeyboardButton("सुविधाएँ", callback_data='3.2.4.3.4')
        ],
        [
            InlineKeyboardButton("पीछे", callback_data='pgdca_back_hin'),
            InlineKeyboardButton("होम", callback_data='pgdca_home_hin')
        ]
    ]  
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="कंप्यूटर एप्लीकेशन में पोस्ट ग्रेजुएट डिप्लोमा",reply_markup=reply_markup)

async def pgdca_admission_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('my_package/image/MCA_ADM.jpg', 'rb'))
    await context.bot.send_message(chat_id=update.effective_chat.id, text="पी.जी.डी.सी.ए 1 वर्षीय स्नातकोत्तर डिप्लोमा कार्यक्रम (दो सेमेस्टर) है। पीजीडीसीए का साइलेंट फीचर प्रोग्राम दो से तीन महीने की औद्योगिक परियोजना है। यह छात्रों को अगले कैरियर के लिए अपने कौशल को बेहतर ढंग से समायोजित करने की अनुमति देता है। कार्यक्रम को कुछ प्रमुख संगठनों से सक्रिय समर्थन मिल रहा है। अक्सर परियोजना प्रशिक्षुओं को उनकी परियोजनाओं के सफलतापूर्वक पूरा होने के बाद मेजबान संगठनों द्वारा नौकरी की पेशकश की जाती है।")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रवेश : 45 छात्र")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="अवधि : 1 वर्ष (दो सेमेस्टर)")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रवेश प्रक्रिया लिंक : https://www.gujaratvidyapith.org/admission/index.php")