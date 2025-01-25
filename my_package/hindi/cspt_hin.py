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


async def cspt_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("प्रवेश", callback_data='3.2.3.6.1'),
            InlineKeyboardButton("पाठ्यक्रम", callback_data='3.2.3.6.2')
        ],
        [
            InlineKeyboardButton("सुविधाएँ", callback_data='3.2.3.6.4')
        ],
        [
            InlineKeyboardButton("पीछे", callback_data='cspt_back_hin'),
            InlineKeyboardButton("होम", callback_data='cspt_home_hin')
        ]
    ]  

    reply_markup = InlineKeyboardMarkup(keyboard)
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="सोलर फोटोवोल्टिक तकनीशियन (सीएसपीटी) में सर्टिफिकेट",reply_markup=reply_markup)

async def cspt_admission_hin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    # query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # await query.answer()
    
    # await update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="सोलर फोटोवोल्टिक तकनीशियन (सीएसपीटी) में सर्टिफिकेट : तीन महीने का अंशकालिक सीएसपीटी एक फाउंडेशन कोर्स है जिसका उद्देश्य सौर फोटोवोल्टिक पेशेवरों द्वारा आवश्यक तकनीकों और स्वभाव को प्रदान करना है। इन उद्देश्यों को प्राप्त करने के लिए, हम उन्हें सोलर पीवी रखरखाव और स्थापना में गहन और व्यापक प्रशिक्षण प्रदान करते हैं। कार्यक्रम को कुछ प्रमुख संस्थानों से छात्रों को नौकरी देकर सक्रिय सहयोग मिल रहा है।")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रवेश : 20 छात्र")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="अवधि : तीन महीने")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="प्रवेश प्रक्रिया लिंक : https://www.gujaratvidyapith.org/admission/index.php")